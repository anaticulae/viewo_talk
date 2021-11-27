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

import viewo_talk.action
import viewo_talk.api


@viewo_talk.api.api_talk.route('/talktome', methods=['GET'])
def receive_message() -> str:
    userid = viewo_api.user_current()
    messages = flask.current_app.talker.answers_pop(userid)
    # convert to JSON
    messages = [viewo_talk.action.message_raw(item) for item in messages]
    result = flask.jsonify({
        'messages': messages,
    })
    return result
