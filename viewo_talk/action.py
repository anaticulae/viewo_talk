# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import viewo_talk.config


@dataclasses.dataclass
class Action:
    user: int = None
    time: int = None
    msgid: int = None
    path: str = None
    data: str = None


@dataclasses.dataclass
class Answer(Action):
    question: int = None
    answer: bool = False


@dataclasses.dataclass
class Message:
    user: int = None
    time: int = None
    msgid: int = None
    title: str = None
    content: str = None
    index: str = None

    def json(self) -> dict:
        result = dict(
            name=self.__class__.__name__.upper(),
            title=self.title,
            content=self.content,
        )
        return result


@dataclasses.dataclass
class Question(Message):
    """\
    >>> Question(title='Magst du Brot?', index=10).json()
    {'name': 'QUESTION', 'title': 'Magst du Brot?', 'content': None, 'index': 10}
    """

    def json(self) -> dict:
        result = super().json()
        result['index'] = self.index
        return result


class ActionMixin:

    def __init__(self, routes: list = None):
        self.routes = routes if routes else []

    def run(self, item):
        pass

    def register(self, talker):
        self.send_msg = talker.send_msg
        self.send_question = talker.send_question


def answer_split(raw: str):
    raw = raw.strip()
    return raw.split('\n\n', maxsplit=1)


def fromrequest(request) -> Action:
    action = Action(
        user=request.hashed,
        time=request.time,
        path=(request.method, request.path),
        data=request.data,
        msgid=msgid(path=request.path, method=request.method),
    )
    return action


def pth(path: str):
    return f'{viewo_talk.config.API_PREFIX}{path}'


API_LISTEN = pth('/talktome')


def msgid(path, method='GET') -> str:
    if method == 'POST':
        return 'POST'
    if path == API_LISTEN:
        return 'LISTEN'
    return None
