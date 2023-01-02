#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

__version__ = '0.3.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# pylint:disable=C0413
from viewo_talk.action import ActionMixin  # isort:skip
from viewo_talk.action import Message  # isort:skip
from viewo_talk.action import Question  # isort:skip
from viewo_talk.action import pth  # isort:skip
from viewo_talk.api import api_talk  # isort:skip
from viewo_talk.app import register_talkme  # isort:skip
from viewo_talk.talk import update  # isort:skip
