# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import configo

SECRET_KEY = configo.env('CHANIA_SECRET_KEY', os.urandom(64))

API_PREFIX = configo.env('CHANIA_API_PREFIX', '/api/v0')
