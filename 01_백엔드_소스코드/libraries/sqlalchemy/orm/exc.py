# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exc.pyc (Python 3.11)

'''SQLAlchemy ORM exceptions.'''
from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from util import _mapper_property_as_plain_name
from  import exc as sa_exc
from  import util
from exc import MultipleResultsFound
from exc import NoResultFound
if TYPE_CHECKING:
    from interfaces import LoaderStrategy
    from interfaces import MapperProperty
    from state import InstanceState
_T = TypeVar('_T', bound = Any)
NO_STATE = (AttributeError, KeyError)

class StaleDataError(sa_exc.SQLAlchemyError):
    '''An operation encountered database state that is unaccounted for.

    Conditions which cause this to happen include:

    * A flush may have attempted to update or delete rows
      and an unexpected number of rows were matched during
      the UPDATE or DELETE statement.   Note that when
      version_id_col is used, rows in UPDATE or DELETE statements
      are also matched against the current known version
      identifier.

    * A mapped object with version_id_col was refreshed,
      and the version number coming back from the database does
      not match that of the object itself.

    * A object is detached from its parent object, however
      the object was previously attached to a different parent
      identity which was garbage collected, and a decision
      cannot be made if the new parent was really the most
      recent "parent".

    '''
    pass

ConcurrentModificationError = StaleDataError

class FlushError(sa_exc.SQLAlchemyError):
    '''A invalid condition was detected during flush().'''
    pass


class MappedAnnotationError(sa_exc.ArgumentError):
    '''Raised when ORM annotated declarative cannot interpret the
    expression present inside of the :class:`.Mapped` construct.

    .. versionadded:: 2.0.40

    '''
    pass


class UnmappedError(sa_exc.InvalidRequestError):
    '''Base for exceptions that involve expected mappings not present.'''
    pass


class ObjectDereferencedError(sa_exc.SQLAlchemyError):
    '''An operation cannot complete due to an object being garbage
    collected.

    '''
    pass


class DetachedInstanceError(sa_exc.SQLAlchemyError):
    '''An attempt to access unloaded attributes on a
    mapped instance that is detached.'''
    code = 'bhk3'


class UnmappedInstanceError(UnmappedError):
    '''An mapping operation was requested for an unknown instance.'''
    __init__ = (lambda self = None, obj = None, msg = util.preload_module('sqlalchemy.orm.base'): base = util.preloaded.orm_baseif not msg:
try:
base.class_mapper(type(obj))name = _safe_cls_name(type(obj))msg = f'''Class {name!r} is mapped, but this instance lacks instrumentation.  This occurs when the instance is created before sqlalchemy.orm.mapper({name!s}) was called.'''except UnmappedClassError:
msg = f'''Class \'{_safe_cls_name(type(obj))}\' is not mapped'''if isinstance(obj, type):
msg += '; was a class (%s) supplied where an instance was required?' % _safe_cls_name(obj)UnmappedError.__init__(self, msg)None)()
    
    def __reduce__(self = None):
        return (self.__class__, (None, self.args[0]))



class UnmappedClassError(UnmappedError):
    '''An mapping operation was requested for an unknown class.'''
    
    def __init__(self = None, cls = None, msg = None):
        if not msg:
            msg = _default_unmapped(cls)
        UnmappedError.__init__(self, msg)

    
    def __reduce__(self = None):
        return (self.__class__, (None, self.args[0]))



class ObjectDeletedError(sa_exc.InvalidRequestError):
    """A refresh operation failed to retrieve the database
    row corresponding to an object's known primary key identity.

    A refresh operation proceeds when an expired attribute is
    accessed on an object, or when :meth:`_query.Query.get` is
    used to retrieve an object which is, upon retrieval, detected
    as expired.   A SELECT is emitted for the target row
    based on primary key; if no row is returned, this
    exception is raised.

    The true meaning of this exception is simply that
    no row exists for the primary key identifier associated
    with a persistent object.   The row may have been
    deleted, or in some cases the primary key updated
    to a new value, outside of the ORM's management of the target
    object.

    """
    __init__ = (lambda self = None, state = None, msg = util.preload_module('sqlalchemy.orm.base'): base = util.preloaded.orm_baseif not msg:
msg = "Instance '%s' has been deleted, or its row is otherwise not present." % base.state_str(state)sa_exc.InvalidRequestError.__init__(self, msg))()
    
    def __reduce__(self = None):
        return (self.__class__, (None, self.args[0]))



class UnmappedColumnError(sa_exc.InvalidRequestError):
    '''Mapping operation was requested on an unknown column.'''
    pass


class LoaderStrategyException(sa_exc.InvalidRequestError):
    '''A loader strategy for an attribute does not exist.'''
    
    def __init__(self, applied_to_property_type, requesting_property = None, applies_to = None, actual_strategy_type = None, strategy_key = ('applied_to_property_type', 'Type[Any]', 'requesting_property', 'MapperProperty[Any]', 'applies_to', 'Optional[Type[MapperProperty[Any]]]', 'actual_strategy_type', 'Optional[Type[LoaderStrategy]]', 'strategy_key', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete



def _safe_cls_name(cls = None):
    pass
# WARNING: Decompyle incomplete

_default_unmapped = (lambda cls = None: base = util.preloaded.orm_basetry:
mappers = base.manager_of_class(cls).mappersexcept (UnmappedClassError, TypeError) + NO_STATE:
mappers = { }name = _safe_cls_name(cls)if not mappers:
f'''Class \'{name}\' is not mapped''')()
