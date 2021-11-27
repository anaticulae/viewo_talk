# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

import viewo_talk
import viewo_talk.config
from viewo_talk.api.present import *  # pylint:disable=W0401,W0614


def create_app() -> flask.Flask:
    # Flask determines template- and static-folder automatically.
    result = flask.Flask(__name__)
    # data API
    result.register_blueprint(
        viewo_talk.api.api_talk,
        url_prefix=viewo_talk.config.API_PREFIX,
    )
    return result
