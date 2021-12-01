# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import viewo_talk.action


TITLE, CONTENT = viewo_talk.action.answer_split("""\
Sämtliche ??? ignorieren

Sie haben 5x ??Finding?? ??XX?? ignoriert. Möchten Sie die restlichen
??XX?? ebenfalls ignorieren?
""")


class DeleteAll(viewo_talk.action.ActionMixin):

    INVOCATION_MAX = 5

    def __init__(self):
        super().__init__()
        self.deleted = collections.Counter()

    def run(self, item: viewo_talk.action.Action):
        self.deleted[item.user] += 1
        if self.deleted[item.user] != DeleteAll.INVOCATION_MAX:
            return
        self.send_msg(
            user=item.user,
            title=TITLE,
            content=CONTENT,
            question=True,
        )
