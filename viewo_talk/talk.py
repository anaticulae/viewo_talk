# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import queue

import utila

import viewo_talk.action
import viewo_talk.plan


class Talker:

    def __init__(self):
        self.todo = queue.Queue()
        self.msg = queue.Queue()
        self.tasks = []

    def append(self, item: viewo_talk.action.Action):
        self.todo.put(item)

    def messages(self):
        result = []
        while not self.msg.empty():
            result.append(self.msg.get_nowait())
        return result

    def sendtouser(self, user: str, title: str, content: str):
        msg = viewo_talk.action.Message(
            user=user,
            time=utila.now(),
            title=title,
            content=content,
        )
        self.msg.put(msg)

    def run(self):
        while not self.todo.empty():
            job = self.todo.get_nowait()
            for task in self.tasks:
                task.todo(job)

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
