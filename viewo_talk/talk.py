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

    def register(self, task):
        self.tasks.append(task)

    def sendtouser(self, user: str, title: str, content: str):
        msg = viewo_talk.action.Message(
            user=user,
            time=utila.now(),
            title=title,
            content=content,
        )
        self.msg.put(msg)


def collect(package) -> list:
    source = os.path.split(package.__file__)[0]
    for module in utila.file_list(source, include='py'):
        print(module)


def create() -> Talker:
    result = Talker()
    for item in collect(viewo_talk.plan):
        result.register(item)
    return result
