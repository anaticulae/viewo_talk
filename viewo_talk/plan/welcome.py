# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import viewo_talk.action

TITLE, CONTENT = viewo_talk.action.answer_split("""\
Willkommen auf checkitweg.de

Bei Fragen schauen Sie <<hier>>.
""")


class Welcome(viewo_talk.action.ActionMixin):

    def __init__(self):
        super().__init__()
        self.done = utila.Single()

    def run(self, item: viewo_talk.action.Action):
        user = item.user
        if self.done.contains(user):
            return
        self.send_msg(
            user=user,
            title=TITLE,
            content=CONTENT,
        )
