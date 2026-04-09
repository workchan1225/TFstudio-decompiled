# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

import functools
import inspect
import sys
import typing
from datetime import timedelta
MAX_WAIT = sys.maxsize / 2

def find_ordinal(pos_num = None):
    if pos_num == 0:
        return 'th'
    if None == 1:
        return 'st'
    if None == 2:
        return 'nd'
    if None == 3:
        return 'rd'
    if  <= None, pos_num or None, pos_num <= 20:
        pass
    
    return 'th'
    return find_ordinal(pos_num % 10)


def to_ordinal(pos_num = None):
    return f'''{pos_num}{find_ordinal(pos_num)}'''


def get_callback_name(cb = None):
