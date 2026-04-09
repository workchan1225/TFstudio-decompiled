# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: writeonly.pyc (Python 3.11)

'''Write-only collection API.

This is an alternate mapped attribute style that only supports single-item
collection mutation operations.   To read the collection, a select()
object must be executed each time.

.. versionadded:: 2.0


'''
from __future__ import annotations
from typing import Any
from typing import Collection
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from sqlalchemy.sql import bindparam
from  import attributes
from  import interfaces
from  import relationships
from  import strategies
from base import NEVER_SET
from base import object_mapper
from base import PassiveFlag
from base import RelationshipDirection
from  import exc
from  import inspect
from  import log
from  import util
from sql import delete
from sql import insert
from sql import select
from sql import update
from sql.dml import Delete
from sql.dml import Insert
from sql.dml import Update
from util.typing import Literal
if TYPE_CHECKING:
    from  import QueryableAttribute
    from _typing import _InstanceDict
    from attributes import AttributeEventToken
    from base import LoaderCallableStatus
    from collections import _AdaptedCollectionProtocol
    from collections import CollectionAdapter
    from mapper import Mapper
    from relationships import _RelationshipOrderByArg
    from state import InstanceState
    from util import AliasedClass
    from event import _Dispatch
    from sql.selectable import FromClause
    from sql.selectable import Select
_T = TypeVar('_T', bound = Any)

def WriteOnlyHistory():
    '''WriteOnlyHistory'''
    _reconcile_collection: 'bool' = 'Overrides AttributeHistory to receive append/remove events directly.'
    
    def __init__(self = None, attr = None, state = None, passive = (None,), apply_to = ('attr', 'WriteOnlyAttributeImpl', 'state', 'InstanceState[_T]', 'passive', 'PassiveFlag', 'apply_to', 'Optional[WriteOnlyHistory[_T]]', 'return', 'None')):
        if apply_to:
            if passive & PassiveFlag.SQL_OK:
                raise exc.InvalidRequestError(f'''Attribute {attr} can\'t load the existing state from the database for this operation; full iteration is not permitted.  If this is a delete operation, configure passive_deletes=True on the {attr} relationship in order to resolve this error.''')
            self.unchanged_items = apply_to.unchanged_items
            self.added_items = apply_to.added_items
            self.deleted_items = apply_to.deleted_items
            self._reconcile_collection = apply_to._reconcile_collection
            return None
        self.deleted_items = None.OrderedIdentitySet()
        self.added_items = util.OrderedIdentitySet()
        self.unchanged_items = util.OrderedIdentitySet()
        self._reconcile_collection = False

    added_plus_unchanged = (lambda self = None: list(self.added_items.union(self.unchanged_items)))()
    all_items = (lambda self = None: list(self.added_items.union(self.unchanged_items).union(self.deleted_items)))()
    
    def as_history(self = None):
        if self._reconcile_collection:
            added = self.added_items.difference(self.unchanged_items)
            deleted = self.deleted_items.intersection(self.unchanged_items)
            unchanged = self.unchanged_items.difference(deleted)
        else:
            deleted = self.deleted_items
            unchanged = self.unchanged_items
            added = self.added_items
        return attributes.History(list(added), list(unchanged), list(deleted))

    
    def indexed(self = None, index = None):
        return list(self.added_items)[index]

    
    def add_added(self = None, value = None):
        self.added_items.add(value)

    
    def add_removed(self = None, value = None):
        if value in self.added_items:
            self.added_items.remove(value)
            return None
        None.deleted_items.add(value)


WriteOnlyHistory = <NODE:27>(WriteOnlyHistory, 'WriteOnlyHistory', Generic[_T])

class WriteOnlyAttributeImpl(attributes.AttributeImpl, attributes.HasCollectionAdapter):
    pass
# WARNING: Decompyle incomplete

WriteOnlyLoader = <NODE:12>()()

class DynamicCollectionAdapter:
    data: 'Collection[Any]' = 'simplified CollectionAdapter for internal API consistency'
    
    def __init__(self = None, data = None):
        self.data = data

    
    def __iter__(self = None):
        return iter(self.data)

    
    def _reset_empty(self = None):
        pass

    
    def __len__(self = None):
        return len(self.data)

    
    def __bool__(self = None):
        return True



def AbstractCollectionWriter():
    '''AbstractCollectionWriter'''
    __doc__ = 'Virtual collection which includes append/remove methods that synchronize\n    into the attribute event system.\n\n    '
    if not TYPE_CHECKING:
        __slots__ = ()
    instance: '_T'
    _from_obj: 'Tuple[FromClause, ...]'
    
    def __init__(self = None, attr = None, state = None):
        instance = state.obj()
    # WARNING: Decompyle incomplete

    
    def _add_all_impl(self = None, iterator = None):
        for item in iterator:
            self.attr.append(attributes.instance_state(self.instance), attributes.instance_dict(self.instance), item, None)
            return None

    
    def _remove_impl(self = None, item = None):
        self.attr.remove(attributes.instance_state(self.instance), attributes.instance_dict(self.instance), item, None)


AbstractCollectionWriter = <NODE:27>(AbstractCollectionWriter, 'AbstractCollectionWriter', Generic[_T])

def WriteOnlyCollection():
    '''WriteOnlyCollection'''
    __doc__ = 'Write-only collection which can synchronize changes into the\n    attribute event system.\n\n    The :class:`.WriteOnlyCollection` is used in a mapping by\n    using the ``"write_only"`` lazy loading strategy with\n    :func:`_orm.relationship`.     For background on this configuration,\n    see :ref:`write_only_relationship`.\n\n    .. versionadded:: 2.0\n\n    .. seealso::\n\n        :ref:`write_only_relationship`\n\n    '
    __slots__ = ('instance', 'attr', '_where_criteria', '_from_obj', '_order_by_clauses')
    
    def __iter__(self = None):
        raise TypeError("WriteOnly collections don't support iteration in-place; to query for collection items, use the select() method to produce a SQL statement and execute it with session.scalars().")

    
    def select(self = None):
        '''Produce a :class:`_sql.Select` construct that represents the
        rows within this instance-local :class:`_orm.WriteOnlyCollection`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def insert(self = None):
        '''For one-to-many collections, produce a :class:`_dml.Insert` which
        will insert new rows in terms of this this instance-local
        :class:`_orm.WriteOnlyCollection`.

        This construct is only supported for a :class:`_orm.Relationship`
        that does **not** include the :paramref:`_orm.relationship.secondary`
        parameter.  For relationships that refer to a many-to-many table,
        use ordinary bulk insert techniques to produce new objects, then
        use :meth:`_orm.AbstractCollectionWriter.add_all` to associate them
        with the collection.


        '''
        state = inspect(self.instance)
        mapper = state.mapper
        prop = mapper._props[self.attr.key]
        if prop.direction is not RelationshipDirection.ONETOMANY:
            raise exc.InvalidRequestError('Write only bulk INSERT only supported for one-to-many collections; for many-to-many, use a separate bulk INSERT along with add_all().')
        dict_ = { }
    # WARNING: Decompyle incomplete

    
    def update(self = None):
        '''Produce a :class:`_dml.Update` which will refer to rows in terms
        of this instance-local :class:`_orm.WriteOnlyCollection`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None):
        '''Produce a :class:`_dml.Delete` which will refer to rows in terms
        of this instance-local :class:`_orm.WriteOnlyCollection`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_all(self = None, iterator = None):
        """Add an iterable of items to this :class:`_orm.WriteOnlyCollection`.

        The given items will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
        self._add_all_impl(iterator)

    
    def add(self = None, item = None):
        """Add an item to this :class:`_orm.WriteOnlyCollection`.

        The given item will be persisted to the database in terms of
        the parent instance's collection on the next flush.

        """
        self._add_all_impl([
            item])

    
    def remove(self = None, item = None):
        """Remove an item from this :class:`_orm.WriteOnlyCollection`.

        The given item will be removed from the parent instance's collection on
        the next flush.

        """
        self._remove_impl(item)


WriteOnlyCollection = <NODE:27>(WriteOnlyCollection, 'WriteOnlyCollection', AbstractCollectionWriter[_T])
