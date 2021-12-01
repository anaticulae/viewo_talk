# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import tests


def test_receive_message(client):
    response = utilatest.apicall(client, '/talktome')
    assert not response


def test_receive_welcome(client):
    response = utilatest.apicall(client, '/talktome')
    assert not response
    # wait for processing message
    tests.wait(client)
    response = utilatest.apicall(client, '/talktome')
    messages = response['messages']
    assert len(messages) == 1
