# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2020 by the contributors (see AUTHORS file).
    :license: BSD-2-Clause, see LICENSE for details.
"""

from .logger import ConfluenceLogger
from sphinx.locale import __
from sphinx.util.console import bold # pylint: disable=no-name-in-module

# load sphinx's progress_message or use a compatible instance
try:
    from sphinx.util import progress_message
except:
    class progress_message:
        def __init__(self, msg):
            self.msg = msg

        def __enter__(self):
            ConfluenceLogger.info(bold(self.msg + '... '), nonl=True)

        def __exit__(self, type, value, traceback):
            if type:
                ConfluenceLogger.info(__('failed'))
            else:
                ConfluenceLogger.info(__('done'))
