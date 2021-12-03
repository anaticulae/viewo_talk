# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import threading
import time

import pytest
from viewvisitor.fixture import selenium_driver as driver  # pylint:disable=W0611

import viewo_talk.app

LOCK = threading.Lock()
COUNTER = 4200


@contextlib.contextmanager
def newport():
    with LOCK:
        global COUNTER  # pylint:disable=global-statement
        COUNTER += 1
        yield COUNTER


@pytest.fixture(scope='session')
def webview():
    with newport() as port:
        appx = viewo_talk.app.create_app()
        runner = threading.Thread(
            target=appx.run,
            daemon=True,
            kwargs=dict(port=port),
        )
        runner.start()
    try:
        # wait for startup?
        time.sleep(0.01)  # do not show flask startup message
        yield f'http://localhost:{port}/'
    except Exception as error:
        raise error from None
    appx.talker.stop()  # pylint:disable=E1101


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    # remove old running instances
    pass
