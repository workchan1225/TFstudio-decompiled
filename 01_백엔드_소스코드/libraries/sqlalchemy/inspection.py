# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inspection.pyc (Python 3.11)

'''The inspection module provides the :func:`_sa.inspect` function,
which delivers runtime information about a wide variety
of SQLAlchemy objects, both within the Core as well as the
ORM.

The :func:`_sa.inspect` function is the entry point to SQLAlchemy\'s
public API for viewing the configuration and construction
of in-memory objects.   Depending on the type of object
passed to :func:`_sa.inspect`, the return value will either be
a related object which provides a known interface, or in many
cases it will return the object itself.

The rationale for :func:`_sa.inspect` is twofold.  One is that
it replaces the need to be aware of a large variety of "information
getting" functions in SQLAlchemy, such as
:meth:`_reflection.Inspector.from_engine` (deprecated in 1.4),
:func:`.orm.attributes.instance_state`, :func:`_orm.class_mapper`,
and others.    The other is that the return value of :func:`_sa.inspect`
is guaranteed to obey a documented API, thus allowing third party
tools which build on top of SQLAlchemy configurations to be constructed
in a forwards-compatible way.

'''
from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Optional
from typing import overload
from typing import Type
from typing import TypeVar
from typing import Union
from  import exc
from util.typing import Literal
from util.typing import Protocol
_T = TypeVar('_T', bound = Any)
_TCov = TypeVar('_TCov', bound = Any, covariant = True)
_F = TypeVar('_F', bound = Callable[(..., Any)])
_IN = TypeVar('_IN', bound = Any)
_registrars: 'Dict[type, Union[Literal[True], Callable[[Any], Any]]]' = { }

def Inspectable():
    '''Inspectable'''
    __doc__ = 'define a class as inspectable.\n\n    This allows typing to set up a linkage between an object that\n    can be inspected and the type of inspection it returns.\n\n    Unfortunately we cannot at the moment get all classes that are\n    returned by inspection to suit this interface as we get into\n    MRO issues.\n\n    '
    __slots__ = ()

Inspectable = <NODE:27>(Inspectable, 'Inspectable', Generic[_T])

def _InspectableTypeProtocol():
    '''_InspectableTypeProtocol'''
    __doc__ = "a protocol defining a method that's used when a type (ie the class\n    itself) is passed to inspect().\n\n    "
    
    def _sa_inspect_type(self = None):
        pass


_InspectableTypeProtocol = <NODE:27>(_InspectableTypeProtocol, '_InspectableTypeProtocol', Protocol[_TCov])

def _InspectableProtocol():
    '''_InspectableProtocol'''
    __doc__ = "a protocol defining a method that's used when an instance is\n    passed to inspect().\n\n    "
    
    def _sa_inspect_instance(self = None):
        pass


_InspectableProtocol = <NODE:27>(_InspectableProtocol, '_InspectableProtocol', Protocol[_TCov])
inspect = (lambda subject = None, raiseerr = None: pass)()
inspect = (lambda subject = None, raiseerr = None: pass)()
inspect = (lambda subject = None, raiseerr = None: pass)()
inspect = (lambda subject = None, raiseerr = None: pass)()
inspect = (lambda subject = None, raiseerr = None: pass)()

def inspect(subject = None, raiseerr = None):
    '''Produce an inspection object for the given target.

    The returned value in some cases may be the
    same object as the one given, such as if a
    :class:`_orm.Mapper` object is passed.   In other
    cases, it will be an instance of the registered
    inspection type for the given object, such as
    if an :class:`_engine.Engine` is passed, an
    :class:`_reflection.Inspector` object is returned.

    :param subject: the subject to be inspected.
    :param raiseerr: When ``True``, if the given subject
     does not
     correspond to a known SQLAlchemy inspected type,
     :class:`sqlalchemy.exc.NoInspectionAvailable`
     is raised.  If ``False``, ``None`` is returned.

    '''
    type_ = type(subject)
# WARNING: Decompyle incomplete


def _inspects(*types):
    pass
# WARNING: Decompyle incomplete

_TT = TypeVar('_TT', bound = 'Type[Any]')

def _self_inspects(cls = None):
    if cls in _registrars:
        raise AssertionError('Type %s is already registered' % cls)
    _registrars[cls] = True
    return cls
