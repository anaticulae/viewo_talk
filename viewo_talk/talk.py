# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import os
import queue
import threading

import utila

import viewo_talk.action
import viewo_talk.plan


class Talker:

    def __init__(self):
        self.tasks = []
        self.running = False
        self.todo = queue.Queue()
        self.msg = collections.defaultdict(list)

    def append(self, item: viewo_talk.action.Action):
        self.todo.put(item)

    def answers_pop(self, user: int = None) -> list:
        if self.msg[user]:
            result = list(self.msg[user])
            self.msg[user].clear()
            return result
        return []

    def consume(self, wait: bool = True) -> bool:
        # use wait:false for unit testing
        if wait:
            job = self.todo.get()
        else:
            try:
                job = self.todo.get_nowait()
            except queue.Empty:
                # nothing todo
                return False
        if job is None:
            # empty job to signal to end processing
            return False
        for task in self.tasks:
            if task.routes and job.path not in task.routes:
                continue
            task.run(job)
        return True

    def run(self):
        while self.running:
            self.consume()

    def start(self):
        # TODO: HOW TO TEAR DOWN THIS THREAD? IS IT GONE AFTER SETTING
        # RUNNING=FALSE
        self.running = True
        threading.Thread(target=self.run).start()

    def stop(self):
        self.running = False
        # ensure that waiting ends
        self.todo.put(None)

    def sendtouser(self, user: str, title: str, **kwargs):
        isquestion = 'question' in kwargs
        ctor = viewo_talk.action.Message
        if isquestion:
            ctor = viewo_talk.action.Question
        msg = ctor(
            user=user,
            time=utila.now(),
            title=title,
            content=kwargs.get('content', None),
        )
        self.msg[user].append(msg)

    def register(self, task):
        self.tasks.append(task)


def collect(packages) -> list:
    if not utila.iterable(packages):
        packages = [packages]
    result = []
    for package in packages:
        source = os.path.split(package.__file__)[0]
        for module in utila.file_list(source, include='py', absolute=True):
            if module.endswith('__init__.py'):
                continue
            loaded = utila.load_module(module)
            for value in vars(loaded).values():
                if not hasattr(value, 'mro'):
                    continue
                if viewo_talk.action.ActionMixin not in value.__mro__:
                    continue
                result.append(value)
    return result


def create(sources=None) -> Talker:
    talker = Talker()
    if not sources:
        sources = [viewo_talk.plan]
    for ctor in collect(sources):
        constructred = ctor()
        constructred.register(talker)
        talker.register(constructred)
    return talker
