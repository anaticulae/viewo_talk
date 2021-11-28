# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask

import viewo_talk

api_talk = flask.Blueprint(
    name='api_talk',
    import_name=__name__,
    static_folder=os.path.join(viewo_talk.ROOT, 'viewo_talk/static'),
    template_folder=os.path.join(viewo_talk.ROOT, 'viewo_talk/templates'),
)

__all__ = ['api_talk', 'present']
