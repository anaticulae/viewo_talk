# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import viewo_api

import viewo_talk
import viewo_talk.action
import viewo_talk.config
import viewo_talk.talk
from viewo_talk.api.present import *  # pylint:disable=W0401,W0614


class Application(flask.Flask):

    def __init__(self):
        super().__init__(__name__)
        self.talker = viewo_talk.talk.create()
        self.register()
        self.before_first_request(self.talker.start)
        self.teardown_appcontext(self.teardown)
        self.before_request(self.talker_push)

    def teardown(self, exception):  # pylint:disable=W0613
        self.talker.stop()

    def talker_push(self):
        request = viewo_api.request()
        action = viewo_talk.action.fromrequest(request)
        self.talker.append(action)

    def register(self):
        # data API
        self.register_blueprint(
            viewo_talk.api.api_talk,
            url_prefix=viewo_talk.config.API_PREFIX,
        )


def create_app() -> flask.Flask:
    appx = Application()
    return appx
