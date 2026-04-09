# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _py_util.pyc (Python 3.11)

from __future__ import annotations
import typing
from typing import Any
from typing import Dict
from typing import Tuple
from typing import Union
from util.typing import Literal
if typing.TYPE_CHECKING:
    from cache_key import CacheConst

def prefix_anon_map():
    '''prefix_anon_map'''
    __doc__ = 'A map that creates new keys for missing key access.\n\n    Considers keys of the form "<ident> <name>" to produce\n    new symbols "<name>_<index>", where "index" is an incrementing integer\n    corresponding to <name>.\n\n    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which\n    is otherwise usually used for this type of operation.\n\n    '
    
    def __missing__(self = None, key = None):
        (ident, derived) = key.split(' ', 1)
        anonymous_counter = self.get(derived, 1)
        self[derived] = anonymous_counter + 1
        value = f'''{derived}_{anonymous_counter}'''
        self[key] = value
        return value


prefix_anon_map = <NODE:27>(prefix_anon_map, 'prefix_anon_map', Dict[(str, str)])

def cache_anon_map():
    '''cache_anon_map'''
    __doc__ = 'A map that creates new keys for missing key access.\n\n    Produces an incrementing sequence given a series of unique keys.\n\n    This is similar to the compiler prefix_anon_map class although simpler.\n\n    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which\n    is otherwise usually used for this type of operation.\n\n    '
    _index = 0
    
    def get_anon(self = None, object_ = None):
        idself = id(object_)
    # WARNING: Decompyle incomplete

    
    def __missing__(self = None, key = None):
        self[key] = str(self._index)
        val = str(self._index)
        return val


cache_anon_map = <NODE:27>(cache_anon_map, 'cache_anon_map', Dict[(Union[(int, 'Literal[CacheConst.NO_CACHE]')], Union[(Literal[True], str)])])
