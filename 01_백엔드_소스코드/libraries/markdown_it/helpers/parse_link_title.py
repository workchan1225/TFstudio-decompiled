# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_link_title.pyc (Python 3.11)

'''Parse link title'''
from common.utils import charCodeAt, unescapeAll

class _State:
    __slots__ = ('can_continue', 'marker', 'ok', 'pos', 'str')
    
    def __init__(self = None):
        self.ok = False
        self.can_continue = False
        self.pos = 0
        self.str = ''
        self.marker = 0

    
    def __str__(self = None):
        return self.str



def parseLinkTitle(string = None, start = None, maximum = None, prev_state = (None,)):
    '''Parse link title within `str` in [start, max] range,
    or continue previous parsing if `prev_state` is defined (equal to result of last execution).
    '''
    pos = start
    state = _State()
# WARNING: Decompyle incomplete
