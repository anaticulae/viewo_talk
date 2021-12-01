# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest


def test_question(client_withdelete):
    # delete some content
    for _ in range(10):
        utilatest.apipost(client_withdelete, '/talktome', data={})
    # wait to process items
    wait(client_withdelete)
    response = utilatest.apicall(client_withdelete, '/talktome')
    assert str(response).count("'name': 'QUESTION'") == 1


def wait(instance):
    talker = instance.application.talker
    while talker.consume(wait=False):
        pass
