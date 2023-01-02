# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import configo

SECRET_KEY = configo.env('CHANIA_SECRET_KEY', default=os.urandom(64))

API_PREFIX = configo.env('CHANIA_API_PREFIX', default='/api/v0')
