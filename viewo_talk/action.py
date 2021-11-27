# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses


@dataclasses.dataclass
class Action:
    user: int = None
    time: int = None
    msgid: int = None
    view: str = None
    data: str = None


@dataclasses.dataclass
class Message:
    user: int = None
    time: int = None
    msgid: int = None
    title: str = None
    content: str = None


class ActionMixin:

    def todo(self, item):
        pass

    def register(self, sendtouser):
        self.sendtouser = sendtouser


def answer_split(raw: str):
    return raw.split('\n\n', maxsplit=1)


def fromrequest(request) -> Action:
    action = Action(
        user=request.hashed,
        time=request.time,
        view=request.path,
        data=request.data,
        msgid=msgid(request),
    )
    return action


API_LISTEN = '/api/v0/talktome'


def msgid(request) -> str:
    if request.path == API_LISTEN:
        return 'LISTEN'
    return None
