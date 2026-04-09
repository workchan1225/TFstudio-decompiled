# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: row.pyc (Python 3.11)

'''Define row constructs including :class:`.Row`.'''
from __future__ import annotations
from abc import ABC
from collections.abc import abc as collections_abc
import operator
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from sql import util as sql_util
from util import deprecated
from util._has_cy import HAS_CYEXTENSION
if not TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_row import BaseRow
else:
    from sqlalchemy.cyextension.resultproxy import BaseRow
if TYPE_CHECKING:
    from result import _KeyType
    from result import _ProcessorsType
    from result import RMKeyView
_T = TypeVar('_T', bound = Any)
_TP = TypeVar('_TP', bound = Tuple[(Any, ...)])

def Row():
    '''Row'''
    __doc__ = 'Represent a single result row.\n\n    The :class:`.Row` object represents a row of a database result.  It is\n    typically associated in the 1.x series of SQLAlchemy with the\n    :class:`_engine.CursorResult` object, however is also used by the ORM for\n    tuple-like results as of SQLAlchemy 1.4.\n\n    The :class:`.Row` object seeks to act as much like a Python named\n    tuple as possible.   For mapping (i.e. dictionary) behavior on a row,\n    such as testing for containment of keys, refer to the :attr:`.Row._mapping`\n    attribute.\n\n    .. seealso::\n\n        :ref:`tutorial_selecting_data` - includes examples of selecting\n        rows from SELECT statements.\n\n    .. versionchanged:: 1.4\n\n        Renamed ``RowProxy`` to :class:`.Row`. :class:`.Row` is no longer a\n        "proxy" object in that it contains the final form of data within it,\n        and now acts mostly like a named tuple. Mapping-like functionality is\n        moved to the :attr:`.Row._mapping` attribute. See\n        :ref:`change_4710_core` for background on this change.\n\n    '
    __slots__ = ()
    
    def __setattr__(self = None, name = None, value = None):
        raise AttributeError("can't set attribute")

    
    def __delattr__(self = None, name = None):
        raise AttributeError("can't delete attribute")

    
    def _tuple(self = None):
        '''Return a \'tuple\' form of this :class:`.Row`.

        At runtime, this method returns "self"; the :class:`.Row` object is
        already a named tuple. However, at the typing level, if this
        :class:`.Row` is typed, the "tuple" return type will be a :pep:`484`
        ``Tuple`` datatype that contains typing information about individual
        elements, supporting typed unpacking and attribute access.

        .. versionadded:: 2.0.19 - The :meth:`.Row._tuple` method supersedes
           the previous :meth:`.Row.tuple` method, which is now underscored
           to avoid name conflicts with column names in the same way as other
           named-tuple methods on :class:`.Row`.

        .. seealso::

            :attr:`.Row._t` - shorthand attribute notation

            :meth:`.Result.tuples`


        '''
        return self

    tuple = (lambda self = None: self._tuple())()
    _t = (lambda self = None: self)()
    t = (lambda self = None: self._t)()()
    _mapping = (lambda self = None: RowMapping(self._parent, None, self._key_to_index, self._data))()
    
    def _filter_on_values(self = None, processor = None):
        return Row(self._parent, processor, self._key_to_index, self._data)

    if not TYPE_CHECKING:
        
        def _special_name_accessor(name = None):
            '''Handle ambiguous names such as "count" and "index" '''
            pass
        # WARNING: Decompyle incomplete

        count = _special_name_accessor('count')
        index = _special_name_accessor('index')
    
    def __contains__(self = None, key = None):
        return key in self._data

    
    def _op(self = None, other = None, op = None):
        return op(self._to_tuple_instance(), other._to_tuple_instance()) if isinstance(other, Row) else op(self._to_tuple_instance(), other)

    __hash__ = BaseRow.__hash__
    if TYPE_CHECKING:
        __getitem__ = (lambda self = None, index = None: pass)()
        __getitem__ = (lambda self = None, index = None: pass)()
        
        def __getitem__(self = None, index = None):
            pass

    
    def __lt__(self = None, other = None):
        return self._op(other, operator.lt)

    
    def __le__(self = None, other = None):
        return self._op(other, operator.le)

    
    def __ge__(self = None, other = None):
        return self._op(other, operator.ge)

    
    def __gt__(self = None, other = None):
        return self._op(other, operator.gt)

    
    def __eq__(self = None, other = None):
        return self._op(other, operator.eq)

    
    def __ne__(self = None, other = None):
        return self._op(other, operator.ne)

    
    def __repr__(self = None):
        return repr(sql_util._repr_row(self))

    _fields = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self._parent.keys())
)()
    
    def _asdict(self = None):
        '''Return a new dict which maps field names to their corresponding
        values.

        This method is analogous to the Python named tuple ``._asdict()``
        method, and works by applying the ``dict()`` constructor to the
        :attr:`.Row._mapping` attribute.

        .. versionadded:: 1.4

        .. seealso::

            :attr:`.Row._mapping`

        '''
        return dict(self._mapping)


Row = <NODE:27>(Row, 'Row', BaseRow, Sequence[Any], Generic[_TP])
BaseRowProxy = BaseRow
RowProxy = Row

class ROMappingView(ABC):
    _mapping: "Mapping['_KeyType', Any]" = ()
    
    def __init__(self = None, mapping = None, items = None):
        self._mapping = mapping
        self._items = items

    
    def __len__(self = None):
        return len(self._items)

    
    def __repr__(self = None):
        return '{0.__class__.__name__}({0._mapping!r})'.format(self)

    
    def __iter__(self = None):
        return iter(self._items)

    
    def __contains__(self = None, item = None):
        return item in self._items

    
    def __eq__(self = None, other = None):
        return list(other) == list(self)

    
    def __ne__(self = None, other = None):
        return list(other) != list(self)



def ROMappingKeysValuesView():
    '''ROMappingKeysValuesView'''
    __slots__ = ('_items',)

ROMappingKeysValuesView = <NODE:27>(ROMappingKeysValuesView, 'ROMappingKeysValuesView', ROMappingView, typing.KeysView['_KeyType'], typing.ValuesView[Any])

def ROMappingItemsView():
    '''ROMappingItemsView'''
    __slots__ = ('_items',)

ROMappingItemsView = <NODE:27>(ROMappingItemsView, 'ROMappingItemsView', ROMappingView, typing.ItemsView[('_KeyType', Any)])

def RowMapping():
    '''RowMapping'''
    __doc__ = 'A ``Mapping`` that maps column names and objects to :class:`.Row`\n    values.\n\n    The :class:`.RowMapping` is available from a :class:`.Row` via the\n    :attr:`.Row._mapping` attribute, as well as from the iterable interface\n    provided by the :class:`.MappingResult` object returned by the\n    :meth:`_engine.Result.mappings` method.\n\n    :class:`.RowMapping` supplies Python mapping (i.e. dictionary) access to\n    the  contents of the row.   This includes support for testing of\n    containment of specific keys (string column names or objects), as well\n    as iteration of keys, values, and items::\n\n        for row in result:\n            if "a" in row._mapping:\n                print("Column \'a\': %s" % row._mapping["a"])\n\n            print("Column b: %s" % row._mapping[table.c.b])\n\n    .. versionadded:: 1.4 The :class:`.RowMapping` object replaces the\n       mapping-like access previously provided by a database result row,\n       which now seeks to behave mostly like a named tuple.\n\n    '
    __slots__ = ()
    if TYPE_CHECKING:
        
        def __getitem__(self = None, key = None):
            pass

    else:
        __getitem__ = BaseRow._get_by_key_impl_mapping
    
    def _values_impl(self = None):
        return list(self._data)

    
    def __iter__(self = None):
        return self._parent.keys()

    
    def __len__(self = None):
        return len(self._data)

    
    def __contains__(self = None, key = None):
        return self._parent._has_key(key)

    
    def __repr__(self = None):
        return repr(dict(self))

    
    def items(self = None):
        '''Return a view of key/value tuples for the elements in the
        underlying :class:`.Row`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self = None):
        """Return a view of 'keys' for string column names represented
        by the underlying :class:`.Row`.

        """
        return self._parent.keys

    
    def values(self = None):
        '''Return a view of values for the values represented in the
        underlying :class:`.Row`.

        '''
        return ROMappingKeysValuesView(self, self._values_impl())


RowMapping = <NODE:27>(RowMapping, 'RowMapping', BaseRow, typing.Mapping[('_KeyType', Any)])
