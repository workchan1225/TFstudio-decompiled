# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _py_row.pyc (Python 3.11)

from __future__ import annotations
import operator
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Type
if typing.TYPE_CHECKING:
    from result import _KeyType
    from result import _ProcessorsType
    from result import _RawRowType
    from result import _TupleGetterType
    from result import ResultMetaData
MD_INDEX = 0

class BaseRow:
    _data: '_RawRowType' = ('_parent', '_data', '_key_to_index')
    
    def __init__(self, parent = None, processors = None, key_to_index = None, data = ('parent', 'ResultMetaData', 'processors', 'Optional[_ProcessorsType]', 'key_to_index', 'Mapping[_KeyType, int]', 'data', '_RawRowType')):
        '''Row objects are constructed by CursorResult objects.'''
        object.__setattr__(self, '_parent', parent)
        object.__setattr__(self, '_key_to_index', key_to_index)
        if processors:
            '_data'(None, tuple, (lambda .0: for proc, value in .0:
passcontinueproc(value)[value])(zip(processors, data)()))
            return None
        None.__setattr__(self, '_data', tuple(data))

    
    def __reduce__(self = None):
        return (rowproxy_reconstructor, (self.__class__, self.__getstate__()))

    
    def __getstate__(self = None):
        return {
            '_parent': self._parent,
            '_data': self._data }

    
    def __setstate__(self = None, state = None):
        parent = state['_parent']
        object.__setattr__(self, '_parent', parent)
        object.__setattr__(self, '_data', state['_data'])
        object.__setattr__(self, '_key_to_index', parent._key_to_index)

    
    def _values_impl(self = None):
        return list(self)

    
    def __iter__(self = None):
        return iter(self._data)

    
    def __len__(self = None):
        return len(self._data)

    
    def __hash__(self = None):
        return hash(self._data)

    
    def __getitem__(self = None, key = None):
        return self._data[key]

    
    def _get_by_key_impl_mapping(self = None, key = None):
        
        try:
            return self._data[self._key_to_index[key]]
        except KeyError:
            pass

        self._parent._key_not_found(key, False)

    
    def __getattr__(self = None, name = None):
        
        try:
            return self._data[self._key_to_index[name]]
        except KeyError:
            pass

        self._parent._key_not_found(name, True)

    
    def _to_tuple_instance(self = None):
        return self._data



def rowproxy_reconstructor(cls = None, state = None):
    obj = cls.__new__(cls)
    obj.__setstate__(state)
    return obj


def tuplegetter(*indexes):
    pass
# WARNING: Decompyle incomplete
