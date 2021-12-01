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
    messages = [item.json() for item in messages]
    data = dict(messages=messages) if messages else {}
    result = flask.jsonify(data)
    return result


@viewo_talk.api.api_talk.route('/talktome', methods=['POST'])
def receive_answer() -> str:
    try:
        question = int(flask.request.form.get('question', None))
    except (TypeError, ValueError):
        return viewo_api.bad('invalid question')
    answer = bool(flask.request.form.get('answer', None))
    todo = create_answer(question, answer)
    flask.current_app.talker.append(todo)
    return 'done', 200


def create_answer(question: int, answer: bool):
    request = viewo_api.request()
    result = viewo_talk.action.Answer(
        user=request.hashed,
        time=request.time,
        path=(request.method, request.path),
        data=request.data,
        answer=answer,
        question=question,
    )
    return result
