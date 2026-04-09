# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: descriptor_props.pyc (Python 3.11)

'''Descriptor properties are more "auxiliary" properties
that exist as configurational elements, but don\'t participate
as actively in the load/persist ORM loop.

'''
from __future__ import annotations
from dataclasses import is_dataclass
import inspect
import itertools
import operator
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import util as orm_util
from base import _DeclarativeMapped
from base import LoaderCallableStatus
from base import Mapped
from base import PassiveFlag
from base import SQLORMOperations
from interfaces import _AttributeOptions
from interfaces import _IntrospectsAnnotations
from interfaces import _MapsColumns
from interfaces import MapperProperty
from interfaces import PropComparator
from util import _none_set
from util import de_stringify_annotation
from  import event
from  import exc as sa_exc
from  import schema
from  import sql
from  import util
from sql import expression
from sql import operators
from sql.elements import BindParameter
from util.typing import get_args
from util.typing import is_fwd_ref
from util.typing import is_pep593
if typing.TYPE_CHECKING:
    from _typing import _InstanceDict
    from _typing import _RegistryType
    from attributes import History
    from attributes import InstrumentedAttribute
    from attributes import QueryableAttribute
    from context import ORMCompileState
    from decl_base import _ClassScanMapperConfig
    from mapper import Mapper
    from properties import ColumnProperty
    from properties import MappedColumn
    from state import InstanceState
    from engine.base import Connection
    from engine.row import Row
    from sql._typing import _DMLColumnArgument
    from sql._typing import _InfoType
    from sql.elements import ClauseList
    from sql.elements import ColumnElement
    from sql.operators import OperatorType
    from sql.schema import Column
    from sql.selectable import Select
    from util.typing import _AnnotationScanType
    from util.typing import CallableReference
    from util.typing import DescriptorReference
    from util.typing import RODescriptorReference
_T = TypeVar('_T', bound = Any)
_PT = TypeVar('_PT', bound = Any)

def DescriptorProperty():
    '''DescriptorProperty'''
    __doc__ = ':class:`.MapperProperty` which proxies access to a\n    user-defined descriptor.'
    doc: 'Optional[str]' = None
    uses_objects = False
    descriptor: 'DescriptorReference[Any]' = False
    
    def _column_strategy_attrs(self = None):
        raise NotImplementedError('This MapperProperty does not implement column loader strategies')

    
    def get_history(self = None, state = None, dict_ = None, passive = (PassiveFlag.PASSIVE_OFF,)):
        raise NotImplementedError()

    
    def instrument_class(self = None, mapper = None):
        pass
    # WARNING: Decompyle incomplete


DescriptorProperty = <NODE:27>(DescriptorProperty, 'DescriptorProperty', MapperProperty[_T])
_CompositeAttrType = Union[(str, 'Column[_T]', 'MappedColumn[_T]', 'InstrumentedAttribute[_T]', 'Mapped[_T]')]
_CC = TypeVar('_CC', bound = Any)
_composite_getters: 'weakref.WeakKeyDictionary[Type[Any], Callable[[Any], Tuple[Any, ...]]]' = weakref.WeakKeyDictionary()

def CompositeProperty():
    '''CompositeProperty'''
    pass
# WARNING: Decompyle incomplete

CompositeProperty = <NODE:27>(CompositeProperty, 'CompositeProperty', _MapsColumns[_CC], _IntrospectsAnnotations, DescriptorProperty[_CC])

def Composite():
    '''Composite'''
    __doc__ = 'Declarative-compatible front-end for the :class:`.CompositeProperty`\n    class.\n\n    Public constructor is the :func:`_orm.composite` function.\n\n    .. versionchanged:: 2.0 Added :class:`_orm.Composite` as a Declarative\n       compatible subclass of :class:`_orm.CompositeProperty`.\n\n    .. seealso::\n\n        :ref:`mapper_composite`\n\n    '
    inherit_cache = True

Composite = <NODE:27>(Composite, 'Composite', CompositeProperty[_T], _DeclarativeMapped[_T])

def ConcreteInheritedProperty():
    '''ConcreteInheritedProperty'''
    pass
# WARNING: Decompyle incomplete

ConcreteInheritedProperty = <NODE:27>(ConcreteInheritedProperty, 'ConcreteInheritedProperty', DescriptorProperty[_T])

def SynonymProperty():
    '''SynonymProperty'''
    pass
# WARNING: Decompyle incomplete

SynonymProperty = <NODE:27>(SynonymProperty, 'SynonymProperty', DescriptorProperty[_T])

def Synonym():
    '''Synonym'''
    __doc__ = 'Declarative front-end for the :class:`.SynonymProperty` class.\n\n    Public constructor is the :func:`_orm.synonym` function.\n\n    .. versionchanged:: 2.0 Added :class:`_orm.Synonym` as a Declarative\n       compatible subclass for :class:`_orm.SynonymProperty`\n\n    .. seealso::\n\n        :ref:`synonyms` - Overview of synonyms\n\n    '
    inherit_cache = True

Synonym = <NODE:27>(Synonym, 'Synonym', SynonymProperty[_T], _DeclarativeMapped[_T])
