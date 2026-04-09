# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: basemode.pyc (Python 3.11)

import glob
import math
import os
import re
import sys
from pyreadline3.clipboard import clipboard

history

lineobj
from pyreadline3.error import ReadlineError
import pyreadline3.lineeditor.lineobj, lineeditor
from pyreadline3.keysyms.common import make_KeyPress_from_keydescr
from pyreadline3.logger import log
from pyreadline3.py3k_compat import is_callable, is_ironpython
from pyreadline3.unicode_helper import ensure_str, ensure_unicode

class BaseMode(object):
    __module__ = __name__
    __qualname__ = 'BaseMode'
    mode = 'base'
    
    def __init__(self, rlobj):
        self.argument = 0
        self.rlobj = rlobj
        self.exit_dispatch = { }
        self.key_dispatch = { }
        self.argument = 1
        self.prevargument = None
        self.l_buffer = lineobj.ReadLineTextBuffer('')
        self._history = history.LineHistory()
        self.completer_delims = ' \t\n"\\\'`@$><=;|&{('
        self.show_all_if_ambiguous = 'on'
        self.mark_directories = 'on'
        self.complete_filesystem = 'off'
        self.completer = None
        self.begidx = 0
        self.endidx = 0
        self.tabstop = 4
        self.startup_hook = None
        self.pre_input_hook = None
        self.first_prompt = True
        self.cursor_size = 25
        self.prompt = '>>> '
        self.enable_ipython_paste_for_paths = True
        self.enable_ipython_paste_list_of_lists = True
        self.enable_win32_clipboard = True
        self.paste_line_buffer = []
        self._sub_modes = []

    
    def __repr__(self):
        return '<BaseMode>'

    
    def _gs(x):
        pass
    # WARNING: Decompyle incomplete

    
    def _g(x):
        pass
    # WARNING: Decompyle incomplete

    
    def _argreset(self):
        val = self.argument
        self.argument = 0
        if val == 0:
            val = 1
        return val

    argument_reset = property(_argreset)
# WARNING: Decompyle incomplete


def commonprefix(m):
    '''Given a list of pathnames, returns the longest common leading component'''
    if not m:
        return ''
    prefix = None[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i + 1].lower() != item[:i + 1].lower():
                prefix = prefix[:i]
                if i == 0:
                    return ''
            
            return prefix
