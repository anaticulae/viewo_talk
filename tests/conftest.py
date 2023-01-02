# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilatest

import tests.plan.delete_all
import viewo_talk.action
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


@pytest.fixture
def client_withdelete(client):  # pylint:disable=W0621
    deleteall = tests.plan.delete_all.DeleteAll()
    deleteall.register(client.application.talker)
    client.application.talker.register(deleteall)

    def delete_message() -> str:
        return 'done', 200

    client.application.add_url_rule(
        viewo_talk.action.pth('/talktome/delete'),
        'delete_message',
        delete_message,
        methods=['POST'],
    )
    urlmap = client.application.url_map
    # TODO: CONVERT TO EASIER TO USE METHOD
    # TODO: MAY CHANGE LATER
    rules = urlmap.iter_rules()
    expected = viewo_talk.action.pth('/talktome/delete')
    rules = [item for item in rules if expected in str(item)]
    assert len(rules) == 1
    deleted = rules[0]
    assert 'POST' in deleted.methods
    deleteall.routes.append(('POST', deleted.rule))
    yield client
