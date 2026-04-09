# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import warnings
import types
import collections
import itertools
from functools import lru_cache
from typing import List, Union, Iterable
_bslash = chr(92)

class __config_flags:
    '''Internal class for defining compatibility and debugging flags'''
    _all_names: List[str] = []
    _fixed_names: List[str] = []
    _type_desc = 'configuration'
    _set = (lambda cls, dname, value: if dname in cls._fixed_names:
warnings.warn('{}.{} {} is {} and cannot be overridden'.format(cls.__name__, dname, cls._type_desc, str(getattr(cls, dname)).upper()))Noneif None in cls._all_names:
setattr(cls, dname, value)Noneraise None('no such {} {!r}'.format(cls._type_desc, dname)))()
    enable = classmethod((lambda cls, name: cls._set(name, True)))
    disable = classmethod((lambda cls, name: cls._set(name, False)))

col = (lambda loc = None, strg = None: s = strgif  < 0, loc or 0, loc < len(s):
pass1 if s[loc - 1] == '\n' else loc - s.rfind('\n', 0, loc))()
lineno = (lambda loc = None, strg = None: strg.count('\n', 0, loc) + 1)()
line = (lambda loc = None, strg = None: last_cr = strg.rfind('\n', 0, loc)next_cr = strg.find('\n', loc)strg[last_cr + 1:next_cr] if next_cr >= 0 else strg[last_cr + 1:])()

class _UnboundedCache:
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete



class _FifoCache:
    
    def __init__(self, size):
        pass
    # WARNING: Decompyle incomplete



class LRUMemo:
    '''
    A memoizing mapping that retains `capacity` deleted items

    The memo tracks retained items by their access order; once `capacity` items
    are retained, the least recently used item is discarded.
    '''
    
    def __init__(self, capacity):
        self._capacity = capacity
        self._active = { }
        self._memory = collections.OrderedDict()

    
    def __getitem__(self, key):
        
        try:
            return self._active[key]
        except KeyError:
            self._memory.move_to_end(key)
            return 


    
    def __setitem__(self, key, value):
        self._memory.pop(key, None)
        self._active[key] = value

    
    def __delitem__(self, key):
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        self._active.clear()
        self._memory.clear()



class UnboundedMemo(dict):
    '''
    A memoizing mapping that retains all deleted items
    '''
    
    def __delitem__(self, key):
        pass



def _escape_regex_range_chars(s = None):
    for c in '\\^-[]':
        s = s.replace(c, _bslash + c)
        s = s.replace('\n', '\\n')
        s = s.replace('\t', '\\t')
        return str(s)


def _collapse_string_to_ranges(s = None, re_escape = None):
    pass
# WARNING: Decompyle incomplete


def _flatten(ll = None):
    ret = []
    for i in ll:
        if isinstance(i, list):
            ret.extend(_flatten(i))
            continue
        ret.append(i)
        return ret
