# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilatest

import viewo_talk.config

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

utilatest.setup(viewo_talk.config.API_PREFIX)


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # disable tracking in test run # TODO: MOVE TO CONFIG
    application = viewo_talk.app.create_app()
    # ensure to create app context: TODO: THINK ABOUT IT
    with application.app_context():
        yield application


@pytest.fixture
def client(app):  # pylint:disable=W0621
    """A test client for the app."""
    return app.test_client()
