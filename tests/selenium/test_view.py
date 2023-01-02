# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import time

import utilatest

import tests.plan.delete_all
import tests.selenium.conftest

# TODO: UNIT THESE TESTS


@utilatest.nightly
@utilatest.displayed
def test_view_welcome(driver):
    with tests.selenium.conftest.webview(talker=True) as (webview, talker):
        driver.get(webview)
        mbox = driver.find_element_by_id('mbox')
        assert not mbox.is_displayed()
        talker.send_msg(
            user=-1399561504684103689,
            title='Das ist hier die Frage',
            content='Frage',
        )
        talker.consume(wait=False)
        time.sleep(3)
        assert mbox.is_displayed()


@utilatest.nightly
@utilatest.displayed
def test_view_question(driver):
    with tests.selenium.conftest.webview(talker=True) as (webview, talker):
        driver.get(webview)
        mbox = driver.find_element_by_id('mbox')
        talker.send_question(
            user=-1399561504684103689,
            title='Das ist hier die Frage',
            content='Frage',
        )
        talker.consume(wait=False)
        time.sleep(3)
        assert mbox.is_displayed()
        done = driver.find_element_by_id('mbox_question_yes')
        done.click()
        assert not mbox.is_displayed()
