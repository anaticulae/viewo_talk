# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib

import tests
import viewo_talk.action
import viewo_talk.plan
import viewo_talk.talk


def test_welcome():
    with worker() as talker:
        info = viewo_talk.action.Action(
            user=tests.USER,
            view=tests.WELCOME,
        )
        talker.append(info)
    msg = talker.msg.get_nowait()
    assert msg.title == viewo_talk.plan.welcome.TITLE


class worker(contextlib.ContextDecorator):  # pylint:disable=C0103

    def __init__(self):
        self.created = viewo_talk.talk.create()

    def __enter__(self):
        return self.created

    def __exit__(self, *exc):
        self.created.run()
        return self.created.msg
