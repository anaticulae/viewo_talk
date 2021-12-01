# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_bootstrap
import viewo_api

import viewo_talk
import viewo_talk.action
import viewo_talk.config
import viewo_talk.talk
from viewo_talk.api.present import *  # pylint:disable=W0401,W0614
from viewo_talk.view import welcome


class Application(flask.Flask):

    def __init__(self):
        super().__init__(__name__)
        register_talkme(self)
        self.register()
        self.create_view()

    def register(self):
        self.register_blueprint(welcome)

    def create_view(self):
        self.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
        # configure extensions
        flask_bootstrap.Bootstrap(app=self)


def register_talkme(app, prefix: str = None, sources: list = None):
    talker = viewo_talk.talk.create(sources=sources)
    app.talker = talker
    app.before_first_request(talker.start)

    @app.teardown_appcontext
    def teardown(exception):  # pylint:disable=W0613
        talker.stop()

    @app.before_request
    def talker_push():
        request = viewo_api.request()
        action = viewo_talk.action.fromrequest(request)
        talker.append(action)

    url_prefix = prefix if prefix else viewo_talk.config.API_PREFIX
    # data API
    app.register_blueprint(viewo_talk.api.api_talk, url_prefix=url_prefix)


def create_app() -> flask.Flask:
    appx = Application()
    return appx
