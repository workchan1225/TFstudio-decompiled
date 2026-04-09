# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import contextlib
import re
from functools import lru_cache, wraps
import inspect
import itertools
import types
from typing import Callable, Union, Iterable, TypeVar, cast
import warnings
_bslash = chr(92)
C = TypeVar('C', bound = Callable)

class __config_flags:
    '''Internal class for defining compatibility and debugging flags'''
    _all_names: list[str] = []
    _fixed_names: list[str] = []
    _type_desc = 'configuration'
    _set = (lambda cls, dname, value: if dname in cls._fixed_names:
warnings.warn(f'''{cls.__name__}.{dname} {cls._type_desc} is {str(getattr(cls, dname)).upper()} and cannot be overridden''', stacklevel = 3)Noneif None in cls._all_names:
setattr(cls, dname, value)Noneraise None(f'''no such {cls._type_desc} {dname!r}'''))()
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
        self._memory = { }

    
    def __getitem__(self, key):
        
        try:
            return self._active[key]
        except KeyError:
            self._memory[key] = self._memory.pop(key)
            return 


    
    def __setitem__(self, key, value):
        self._memory.pop(key, None)
        self._active[key] = value

    
    def __delitem__(self, key):
        
        try:
            value = self._active.pop(key)
            oldest_keys = list(self._memory)[:-(self._capacity + 1)]
            for key_to_delete in oldest_keys:
                self._memory.pop(key_to_delete)
                self._memory[key] = value
                return None
                except KeyError:
                    return None


    
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


class _GroupConsecutive:
    '''
    Used as a callable `key` for itertools.groupby to group
    characters that are consecutive:
    
    .. testcode::

       from itertools import groupby
       from pyparsing.util import _GroupConsecutive

       grouped = groupby("abcdejkmpqrs", key=_GroupConsecutive())
       for index, group in grouped:
           print(tuple([index, list(group)]))

    prints:

    .. testoutput::

       (0, [\'a\', \'b\', \'c\', \'d\', \'e\'])
       (1, [\'j\', \'k\'])
       (2, [\'m\'])
       (3, [\'p\', \'q\', \'r\', \'s\'])
    '''
    
    def __init__(self = None):
        self.prev = 0
        self.counter = itertools.count()
        self.value = -1

    
    def __call__(self = None, char = None):
        c_int = ord(char)
        self.prev, prev = c_int, self.prev
        if c_int - prev > 1:
            self.value = next(self.counter)
        return self.value



def _collapse_string_to_ranges(s = None, re_escape = None):
    """
    Take a string or list of single-character strings, and return
    a string of the consecutive characters in that string collapsed
    into groups, as might be used in a regular expression '[a-z]'
    character set::

        'a' -> 'a' -> '[a]'
        'bc' -> 'bc' -> '[bc]'
        'defgh' -> 'd-h' -> '[d-h]'
        'fdgeh' -> 'd-h' -> '[d-h]'
        'jklnpqrtu' -> 'j-lnp-rtu' -> '[j-lnp-rtu]'

    Duplicates get collapsed out::

        'aaa' -> 'a' -> '[a]'
        'bcbccb' -> 'bc' -> '[bc]'
        'defghhgf' -> 'd-h' -> '[d-h]'
        'jklnpqrjjjtu' -> 'j-lnp-rtu' -> '[j-lnp-rtu]'

    Spaces are preserved::

        'ab c' -> ' a-c' -> '[ a-c]'

    Characters that are significant when defining regex ranges
    get escaped::

        'acde[]-' -> r'\\-\\[\\]ac-e' -> r'[\\-\\[\\]ac-e]'
    """
    pass
# WARNING: Decompyle incomplete


def _flatten(ll = None):
    ret = []
    to_visit = None
# WARNING: Decompyle incomplete


def make_compressed_re(word_list = None, max_level = None, *, non_capturing_groups, _level):
    '''
    Create a regular expression string from a list of words, collapsing by common
    prefixes and optional suffixes.

    Calls itself recursively to build nested sublists for each group of suffixes
    that have a shared prefix.
    '''
    
    def get_suffixes_from_common_prefixes(namelist = None):
        pass
    # WARNING: Decompyle incomplete

    if _level == 1:
        if not word_list:
            raise ValueError('no words given to make_compressed_re()')
        if '' in word_list:
            raise ValueError('word list cannot contain empty string')
    elif not word_list:
        return ''
    word_list = list({ }.fromkeys(word_list))
    if max_level == 0:
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(word_list()):
            return sorted((lambda .0: [ re.escape(wd) for wd in .0 ])(word_list(), key = len, reverse = True))
        return f'''{(lambda .0: pass# WARNING: Decompyle incomplete
)(word_list())}]'''
    ret = None
    sep = ''
    ncgroup = '?:' if non_capturing_groups else ''
    for initial, suffixes in get_suffixes_from_common_prefixes(sorted(word_list)):
        ret.append(sep)
        sep = '|'
        initial = re.escape(initial)
        trailing = ''
        if '' in suffixes:
            trailing = '?'
            suffixes.remove('')
        if len(suffixes) > 1:
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(suffixes()):
                f'''{initial}'''(f'''[{(lambda .0: pass# WARNING: Decompyle incomplete
)(suffixes())}]{trailing}''')
                continue
            if _level < max_level:
                suffix_re = make_compressed_re(sorted(suffixes), max_level, non_capturing_groups = non_capturing_groups, _level = _level + 1)
                ret.append(f'''{initial}({ncgroup}{suffix_re}){trailing}''')
                continue
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(suffixes()):
                f'''{initial}'''(f'''[{(lambda .0: pass# WARNING: Decompyle incomplete
)(suffixes())}]{trailing}''')
                continue
            suffixes.sort(key = len, reverse = True)
            f'''{initial}'''(f'''({ncgroup}{(lambda .0: pass# WARNING: Decompyle incomplete
)(suffixes())}){trailing}''')
            continue
        if suffixes:
            suffix = re.escape(suffixes[0])
            if len(suffix) > 1 and trailing:
                ret.append(f'''{initial}({ncgroup}{suffix}){trailing}''')
                continue
            ret.append(f'''{initial}{suffix}{trailing}''')
            continue
        ret.append(initial)
        return ''.join(ret)


def replaced_by_pep8(compat_name = None, fn = None):
    pass
# WARNING: Decompyle incomplete
