# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import utilotest

import tests


def test_receive_message(client):
    response = utilotest.apicall(client, '/talktome')
    assert not response


def test_receive_welcome(client):
    # ensure that no messages are in queue
    response = utilotest.apicall(client, '/talktome')
    assert not response
    # open main page
    utilotest.get(client, '/')
    # wait for processing message
    tests.wait(client)
    response = utilotest.apicall(client, '/talktome')
    messages = response['messages']
    assert len(messages) == 1


def test_receive_answer(client):
    utilotest.apipost(
        client,
        '/talktome',
        data={
            'question': 13371337,
            'answer': 0
        },
    )
    utilotest.apipost(
        client,
        '/talktome',
        data={
            'question': 'AAAAAAAAA',
            'answer': 0
        },
        expected=http.HTTPStatus.BAD_REQUEST,
    )
