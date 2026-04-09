# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_link_destination.pyc (Python 3.11)

'''
Parse link destination
'''
from common.utils import charCodeAt, unescapeAll

class _Result:
    __slots__ = ('ok', 'pos', 'str')
    
    def __init__(self = None):
        self.ok = False
        self.pos = 0
        self.str = ''



def parseLinkDestination(string = None, pos = None, maximum = None):
    start = pos
    result = _Result()
# WARNING: Decompyle incomplete
