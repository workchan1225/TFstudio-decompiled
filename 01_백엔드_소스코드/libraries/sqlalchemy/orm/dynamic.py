# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dynamic.pyc (Python 3.11)

'''Dynamic collection API.

Dynamic collections act like Query() objects for read operations and support
basic add/delete mutation.

.. legacy:: the "dynamic" loader is a legacy feature, superseded by the
 "write_only" loader.


'''
from __future__ import annotations
from typing import Any
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import attributes
from  import exc as orm_exc
from  import relationships
from  import util as orm_util
from base import PassiveFlag
from query import Query
from session import object_session
from writeonly import AbstractCollectionWriter
from writeonly import WriteOnlyAttributeImpl
from writeonly import WriteOnlyHistory
from writeonly import WriteOnlyLoader
from  import util
from engine import result
if TYPE_CHECKING:
    from  import QueryableAttribute
    from mapper import Mapper
    from relationships import _RelationshipOrderByArg
    from session import Session
    from state import InstanceState
    from util import AliasedClass
    from event import _Dispatch
    from sql.elements import ColumnElement
_T = TypeVar('_T', bound = Any)

def DynamicCollectionHistory():
    '''DynamicCollectionHistory'''
    
    def __init__(self = None, attr = None, state = None, passive = (None,), apply_to = ('attr', 'DynamicAttributeImpl', 'state', 'InstanceState[_T]', 'passive', 'PassiveFlag', 'apply_to', 'Optional[DynamicCollectionHistory[_T]]', 'return', 'None')):
        if apply_to:
            coll = AppenderQuery(attr, state).autoflush(False)
            self.unchanged_items = util.OrderedIdentitySet(coll)
            self.added_items = apply_to.added_items
            self.deleted_items = apply_to.deleted_items
            self._reconcile_collection = True
            return None
        self.deleted_items = None.OrderedIdentitySet()
        self.added_items = util.OrderedIdentitySet()
        self.unchanged_items = util.OrderedIdentitySet()
        self._reconcile_collection = False


DynamicCollectionHistory = <NODE:27>(DynamicCollectionHistory, 'DynamicCollectionHistory', WriteOnlyHistory[_T])

class DynamicAttributeImpl(WriteOnlyAttributeImpl):
    _supports_dynamic_iteration = True
    query_class: 'Type[AppenderMixin[Any]]' = DynamicCollectionHistory[Any]
    
    def __init__(self, class_, key = None, dispatch = None, target_mapper = None, order_by = (None,), query_class = ('class_', 'Union[Type[Any], AliasedClass[Any]]', 'key', 'str', 'dispatch', '_Dispatch[QueryableAttribute[Any]]', 'target_mapper', 'Mapper[_T]', 'order_by', '_RelationshipOrderByArg', 'query_class', 'Optional[Type[AppenderMixin[_T]]]', 'kw', 'Any', 'return', 'None'), **kw):
        pass
    # WARNING: Decompyle incomplete


DynaLoader = <NODE:12>()

def AppenderMixin():
    '''AppenderMixin'''
    pass
# WARNING: Decompyle incomplete

AppenderMixin = <NODE:27>(AppenderMixin, 'AppenderMixin', AbstractCollectionWriter[_T])

def AppenderQuery():
    '''AppenderQuery'''
    __doc__ = 'A dynamic query that supports basic collection storage operations.\n\n    Methods on :class:`.AppenderQuery` include all methods of\n    :class:`_orm.Query`, plus additional methods used for collection\n    persistence.\n\n\n    '

AppenderQuery = <NODE:27>(AppenderQuery, 'AppenderQuery', AppenderMixin[_T], Query[_T])

def mixin_user_query(cls = None):
    '''Return a new class with AppenderQuery functionality layered over.'''
    name = 'Appender' + cls.__name__
    return type(name, (AppenderMixin, cls), {
        'query_class': cls })
