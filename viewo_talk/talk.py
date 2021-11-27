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

    def consume(self, wait: bool = True):
        # use wait:false for unit testing
        while not self.todo.empty():
            if wait:
                job = self.todo.get()
            else:
                job = self.todo.get_nowait()
            if job is None:
                break
            for task in self.tasks:
                task.todo(job)

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

    def sendtouser(self, user: str, title: str, content: str):
        msg = viewo_talk.action.Message(
            user=user,
            time=utila.now(),
            title=title,
            content=content,
        )
        self.msg[user].append(msg)

    def register(self, task):
        self.tasks.append(task)


def collect(package) -> list:
    source = os.path.split(package.__file__)[0]
    result = []
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


def create() -> Talker:
    talker = Talker()
    for ctor in collect(viewo_talk.plan):
        constructred = ctor()
        constructred.register(talker.sendtouser)
        talker.register(constructred)
    return talker
