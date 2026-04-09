# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: notemacs.pyc (Python 3.11)

import os

history

lineobj
import pyreadline3.logger as logger
import pyreadline3.lineeditor.lineobj, lineeditor
from pyreadline3.logger import log
from  import basemode

class NotEmacsMode(basemode.BaseMode):
    pass
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
