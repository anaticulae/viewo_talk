# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import tests
import viewo_talk.action
import viewo_talk.plan.welcome
import viewo_talk.talk


def test_welcome():
    with worker() as talker:
        info = viewo_talk.action.Action(
            user=tests.USER,
            path=('GET', tests.WELCOME),
        )
        talker.append(info)
    msg = talker.answers_pop(tests.USER)
    assert msg[0].title == viewo_talk.plan.welcome.TITLE


def test_welcome_single():
    with worker() as talker:
        for _ in range(5):
            info = viewo_talk.action.Action(
                user=tests.USER,
                path=('GET', tests.WELCOME),
            )
            talker.append(info)
    msg = talker.answers_pop(tests.USER)
    assert msg[0].title == viewo_talk.plan.welcome.TITLE
    # only a single message
    assert not talker.answers_pop(tests.USER)


class worker(contextlib.ContextDecorator):  # pylint:disable=C0103

    def __init__(self):
        self.created = viewo_talk.talk.create()

    def __enter__(self):
        return self.created

    def __exit__(self, *exc):
        self.created.consume(wait=False)
        return self.created.msg
