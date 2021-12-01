#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

__version__ = '0.1.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# pylint:disable=C0413
from viewo_talk.api import api_talk  # isort:skip
from viewo_talk.app import register_talkme  # isort:skip
from viewo_talk.action import Message  # isort:skip
from viewo_talk.action import Question  # isort:skip
from viewo_talk.action import ActionMixin  # isort:skip
