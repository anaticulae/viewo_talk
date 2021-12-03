# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import time

import utilatest


@utilatest.nightly
@utilatest.displayed
def test_view_welcome(driver, webview):
    driver.get(webview)
    mbox = driver.find_element_by_id('mbox')
    assert not mbox.is_displayed()
    time.sleep(5)
    assert mbox.is_displayed()
