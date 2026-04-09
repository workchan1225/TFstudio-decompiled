# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state.pyc (Python 3.11)

"""Defines instrumentation of instances.

This module is usually not directly visible to user applications, but
defines a large part of the ORM's interactivity.

"""
from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Optional
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
import weakref
from  import base
from  import exc as orm_exc
from  import interfaces
from _typing import _O
from _typing import is_collection_impl
from base import ATTR_WAS_SET
from base import INIT_OK
from base import LoaderCallableStatus
from base import NEVER_SET
from base import NO_VALUE
from base import PASSIVE_NO_INITIALIZE
from base import PASSIVE_NO_RESULT
from base import PASSIVE_OFF
from base import SQL_OK
from path_registry import PathRegistry
from  import exc as sa_exc
from  import inspection
from  import util
from util.typing import Literal
from util.typing import Protocol
if TYPE_CHECKING:
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import _LoaderCallable
    from attributes import AttributeImpl
    from attributes import History
    from base import PassiveFlag
    from collections import _AdaptedCollectionProtocol
    from identity import IdentityMap
    from instrumentation import ClassManager
    from interfaces import ORMOption
    from mapper import Mapper
    from session import Session
    from engine import Row
    from ext.asyncio.session import async_session as _async_provider
    from ext.asyncio.session import AsyncSession
if TYPE_CHECKING:
    _sessions: 'weakref.WeakValueDictionary[int, Session]'
else:
    _sessions = None
if not TYPE_CHECKING:
    _async_provider = None

class _InstanceDictProto(Protocol):
    
    def __call__(self = None):
        pass



def _InstallLoaderCallableProto():
    '''_InstallLoaderCallableProto'''
    __doc__ = 'used at result loading time to install a _LoaderCallable callable\n    upon a specific InstanceState, which will be used to populate an\n    attribute when that attribute is accessed.\n\n    Concrete examples are per-instance deferred column loaders and\n    relationship lazy loaders.\n\n    '
    
    def __call__(self = None, state = None, dict_ = None, row = ('state', 'InstanceState[_O]', 'dict_', '_InstanceDict', 'row', 'Row[Any]', 'return', 'None')):
        pass


_InstallLoaderCallableProto = <NODE:27>(_InstallLoaderCallableProto, '_InstallLoaderCallableProto', Protocol[_O])

def InstanceState():
    '''InstanceState'''
    __doc__ = "Tracks state information at the instance level.\n\n    The :class:`.InstanceState` is a key object used by the\n    SQLAlchemy ORM in order to track the state of an object;\n    it is created the moment an object is instantiated, typically\n    as a result of :term:`instrumentation` which SQLAlchemy applies\n    to the ``__init__()`` method of the class.\n\n    :class:`.InstanceState` is also a semi-public object,\n    available for runtime inspection as to the state of a\n    mapped instance, including information such as its current\n    status within a particular :class:`.Session` and details\n    about data on individual attributes.  The public API\n    in order to acquire a :class:`.InstanceState` object\n    is to use the :func:`_sa.inspect` system::\n\n        >>> from sqlalchemy import inspect\n        >>> insp = inspect(some_mapped_object)\n        >>> insp.attrs.nickname.history\n        History(added=['new nickname'], unchanged=(), deleted=['nickname'])\n\n    .. seealso::\n\n        :ref:`orm_mapper_inspection_instancestate`\n\n    "
    manager: 'ClassManager[_O]' = ('__dict__', '__weakref__', 'class_', 'manager', 'obj', 'committed_state', 'expired_attributes')
    session_id: 'Optional[int]' = None
    key: 'Optional[_IdentityKeyType[_O]]' = None
    runid: 'Optional[int]' = None
    load_options: 'Tuple[ORMOption, ...]' = ()
    load_path: 'PathRegistry' = PathRegistry.root
    insert_order: 'Optional[int]' = None
    committed_state: 'Dict[str, Any]' = None
    modified: 'bool' = False
    expired: 'bool' = False
    _deleted: 'bool' = False
    _load_pending: 'bool' = False
    _orphaned_outside_of_session: 'bool' = False
    is_instance: 'bool' = True
    identity_token: 'object' = None
    _instance_dict: '_InstanceDictProto' = None
    if not TYPE_CHECKING:
        
        def _instance_dict(self):
            """default 'weak reference' for _instance_dict"""
            pass

    expired_attributes: 'Set[str]'
    callables: 'Dict[str, Callable[[InstanceState[_O], PassiveFlag], Any]]'
    if not TYPE_CHECKING:
        callables = util.EMPTY_DICT
    
    def __init__(self = None, obj = None, manager = None):
        self.class_ = obj.__class__
        self.manager = manager
        self.obj = weakref.ref(obj, self._cleanup)
        self.committed_state = { }
        self.expired_attributes = set()

    attrs = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    transient = (lambda self = None:
