# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Constants and rudimental functions used throughout the ORM.'''
from __future__ import annotations
from enum import Enum
import operator
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import no_type_check
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import exc
from _typing import insp_is_mapper
from  import exc as sa_exc
from  import inspection
from  import util
from sql import roles
from sql.elements import SQLColumnExpression
from sql.elements import SQLCoreOperations
from util import FastIntFlag
from util.langhelpers import TypingOnly
from util.typing import Literal
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _ExternalEntityType
    from _typing import _InternalEntityType
    from attributes import InstrumentedAttribute
    from dynamic import AppenderQuery
    from instrumentation import ClassManager
    from interfaces import PropComparator
    from mapper import Mapper
    from state import InstanceState
    from util import AliasedClass
    from writeonly import WriteOnlyCollection
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _InfoType
    from sql.elements import ColumnElement
    from sql.operators import OperatorType
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_O = TypeVar('_O', bound = object)

class LoaderCallableStatus(Enum):
    PASSIVE_NO_RESULT = 0
    PASSIVE_CLASS_MISMATCH = 1
    ATTR_WAS_SET = 2
    ATTR_EMPTY = 3
    NO_VALUE = 4
    NEVER_SET = NO_VALUE

(PASSIVE_NO_RESULT, PASSIVE_CLASS_MISMATCH, ATTR_WAS_SET, ATTR_EMPTY, NO_VALUE) = tuple(LoaderCallableStatus)
NEVER_SET = NO_VALUE

class PassiveFlag(FastIntFlag):
    '''Bitflag interface that passes options onto loader callables'''
    NO_CHANGE = 0
    CALLABLES_OK = 1
    SQL_OK = 2
    RELATED_OBJECT_OK = 4
    INIT_OK = 8
    NON_PERSISTENT_OK = 16
    LOAD_AGAINST_COMMITTED = 32
    NO_AUTOFLUSH = 64
    NO_RAISE = 128
    DEFERRED_HISTORY_LOAD = 256
    INCLUDE_PENDING_MUTATIONS = 512
    PASSIVE_OFF = RELATED_OBJECT_OK | NON_PERSISTENT_OK | INIT_OK | CALLABLES_OK | SQL_OK
    PASSIVE_RETURN_NO_VALUE = PASSIVE_OFF ^ INIT_OK
    PASSIVE_NO_INITIALIZE = PASSIVE_RETURN_NO_VALUE ^ CALLABLES_OK
    PASSIVE_NO_FETCH = PASSIVE_OFF ^ SQL_OK
    PASSIVE_NO_FETCH_RELATED = PASSIVE_OFF ^ RELATED_OBJECT_OK
    PASSIVE_ONLY_PERSISTENT = PASSIVE_OFF ^ NON_PERSISTENT_OK
    PASSIVE_MERGE = PASSIVE_OFF | NO_RAISE

(NO_CHANGE, CALLABLES_OK, SQL_OK, RELATED_OBJECT_OK, INIT_OK, NON_PERSISTENT_OK, LOAD_AGAINST_COMMITTED, NO_AUTOFLUSH, NO_RAISE, DEFERRED_HISTORY_LOAD, INCLUDE_PENDING_MUTATIONS, PASSIVE_OFF, PASSIVE_RETURN_NO_VALUE, PASSIVE_NO_INITIALIZE, PASSIVE_NO_FETCH, PASSIVE_NO_FETCH_RELATED, PASSIVE_ONLY_PERSISTENT, PASSIVE_MERGE) = PassiveFlag.__members__.values()
DEFAULT_MANAGER_ATTR = '_sa_class_manager'
DEFAULT_STATE_ATTR = '_sa_instance_state'

class EventConstants(Enum):
    EXT_CONTINUE = 1
    EXT_STOP = 2
    EXT_SKIP = 3
    NO_KEY = 4

(EXT_CONTINUE, EXT_STOP, EXT_SKIP, NO_KEY) = tuple(EventConstants)

class RelationshipDirection(Enum):
    """enumeration which indicates the 'direction' of a
    :class:`_orm.RelationshipProperty`.

    :class:`.RelationshipDirection` is accessible from the
    :attr:`_orm.Relationship.direction` attribute of
    :class:`_orm.RelationshipProperty`.

    """
    ONETOMANY = 1
    MANYTOONE = 2
    MANYTOMANY = 3

(ONETOMANY, MANYTOONE, MANYTOMANY) = tuple(RelationshipDirection)

class InspectionAttrExtensionType(Enum):
    '''Symbols indicating the type of extension that a
    :class:`.InspectionAttr` is part of.'''
    pass


class NotExtension(InspectionAttrExtensionType):
    NOT_EXTENSION = 'not_extension'

_never_set = frozenset([
    NEVER_SET])
_none_set = frozenset([
    None,
    NEVER_SET,
    PASSIVE_NO_RESULT])
_none_only_set = frozenset([
    None])
_SET_DEFERRED_EXPIRED = util.symbol('SET_DEFERRED_EXPIRED')
_DEFER_FOR_STATE = util.symbol('DEFER_FOR_STATE')
_RAISE_FOR_STATE = util.symbol('RAISE_FOR_STATE')
_F = TypeVar('_F', bound = Callable[(..., Any)])
_Self = TypeVar('_Self')

def _assertions(*assertions):
    pass
# WARNING: Decompyle incomplete


def instance_str(instance = None):
    '''Return a string describing an instance.'''
    return state_str(instance_state(instance))


def state_str(state = None):
    '''Return a string describing an instance via its InstanceState.'''
    pass
# WARNING: Decompyle incomplete


def state_class_str(state = None):
    """Return a string describing an instance's class via its
    InstanceState.
    """
    pass
# WARNING: Decompyle incomplete


def attribute_str(instance = None, attribute = None):
    return instance_str(instance) + '.' + attribute


def state_attribute_str(state = None, attribute = None):
    return state_str(state) + '.' + attribute


def object_mapper(instance = None):
    '''Given an object, return the primary Mapper associated with the object
    instance.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    This function is available via the inspection system as::

        inspect(instance).mapper

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    '''
    return object_state(instance).mapper


def object_state(instance = None):
    '''Given an object, return the :class:`.InstanceState`
    associated with the object.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    Equivalent functionality is available via the :func:`_sa.inspect`
    function as::

        inspect(instance)

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    '''
    state = _inspect_mapped_object(instance)
# WARNING: Decompyle incomplete

_inspect_mapped_object = (lambda instance = None: try:
instance_state(instance)except (exc.UnmappedClassError,) + exc.NO_STATE:
None)()

def _class_to_mapper(class_or_mapper = None):
    insp = inspection.inspect(class_or_mapper, False)
# WARNING: Decompyle incomplete


def _mapper_or_none(entity = None):
    '''Return the :class:`_orm.Mapper` for the given class or None if the
    class is not mapped.
    '''
    insp = inspection.inspect(entity, False)
# WARNING: Decompyle incomplete


def _is_mapped_class(entity = None):
