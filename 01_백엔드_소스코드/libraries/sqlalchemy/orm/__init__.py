# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Functional constructs for ORM configuration.

See the SQLAlchemy object relational tutorial and mapper configuration
documentation for an overview of how this module is used.

'''
from __future__ import annotations
from typing import Any
from  import exc
from  import mapper as mapperlib
from  import strategy_options
from _orm_constructors import _mapper_fn as mapper
from _orm_constructors import aliased
from _orm_constructors import backref
from _orm_constructors import clear_mappers
from _orm_constructors import column_property
from _orm_constructors import composite
from _orm_constructors import contains_alias
from _orm_constructors import create_session
from _orm_constructors import deferred
from _orm_constructors import dynamic_loader
from _orm_constructors import join
from _orm_constructors import mapped_column
from _orm_constructors import orm_insert_sentinel
from _orm_constructors import outerjoin
from _orm_constructors import query_expression
from _orm_constructors import relationship
from _orm_constructors import synonym
from _orm_constructors import with_loader_criteria
from _orm_constructors import with_polymorphic
from attributes import AttributeEventToken
from attributes import InstrumentedAttribute
from attributes import QueryableAttribute
from base import class_mapper
from base import DynamicMapped
from base import InspectionAttrExtensionType
from base import LoaderCallableStatus
from base import Mapped
from base import NotExtension
from base import ORMDescriptor
from base import PassiveFlag
from base import SQLORMExpression
from base import WriteOnlyMapped
from context import FromStatement
from context import QueryContext
from decl_api import add_mapped_attribute
from decl_api import as_declarative
from decl_api import declarative_base
from decl_api import declarative_mixin
from decl_api import DeclarativeBase
from decl_api import DeclarativeBaseNoMeta
from decl_api import DeclarativeMeta
from decl_api import declared_attr
from decl_api import has_inherited_table
from decl_api import mapped_as_dataclass
from decl_api import MappedAsDataclass
from decl_api import registry
from decl_api import synonym_for
from decl_base import MappedClassProtocol
from descriptor_props import Composite
from descriptor_props import CompositeProperty
from descriptor_props import Synonym
from descriptor_props import SynonymProperty
from dynamic import AppenderQuery
from events import AttributeEvents
from events import InstanceEvents
from events import InstrumentationEvents
from events import MapperEvents
from events import QueryEvents
from events import SessionEvents
from identity import IdentityMap
from instrumentation import ClassManager
from interfaces import EXT_CONTINUE
from interfaces import EXT_SKIP
from interfaces import EXT_STOP
from interfaces import InspectionAttr
from interfaces import InspectionAttrInfo
from interfaces import MANYTOMANY
from interfaces import MANYTOONE
from interfaces import MapperProperty
from interfaces import NO_KEY
from interfaces import NO_VALUE
from interfaces import ONETOMANY
from interfaces import PropComparator
from interfaces import RelationshipDirection
from interfaces import UserDefinedOption
from loading import merge_frozen_result
from loading import merge_result
from mapped_collection import attribute_keyed_dict
from mapped_collection import attribute_mapped_collection
from mapped_collection import column_keyed_dict
from mapped_collection import column_mapped_collection
from mapped_collection import keyfunc_mapping
from mapped_collection import KeyFuncDict
from mapped_collection import mapped_collection
from mapped_collection import MappedCollection
from mapper import configure_mappers
from mapper import Mapper
from mapper import reconstructor
from mapper import validates
from properties import ColumnProperty
from properties import MappedColumn
from properties import MappedSQLExpression
from query import AliasOption
from query import Query
from relationships import foreign
from relationships import Relationship
from relationships import RelationshipProperty
from relationships import remote
from scoping import QueryPropertyDescriptor
from scoping import scoped_session
from session import close_all_sessions
from session import make_transient
from session import make_transient_to_detached
from session import object_session
from session import ORMExecuteState
from session import Session
from session import sessionmaker
from session import SessionTransaction
from session import SessionTransactionOrigin
from state import AttributeState
from state import InstanceState
from strategy_options import contains_eager
from strategy_options import defaultload
from strategy_options import defer
from strategy_options import immediateload
from strategy_options import joinedload
from strategy_options import lazyload
from strategy_options import Load
from strategy_options import load_only
from strategy_options import noload
from strategy_options import raiseload
from strategy_options import selectin_polymorphic
from strategy_options import selectinload
from strategy_options import subqueryload
from strategy_options import undefer
from strategy_options import undefer_group
from strategy_options import with_expression
from unitofwork import UOWTransaction
from util import Bundle
from util import CascadeOptions
from util import LoaderCriteriaOption
from util import object_mapper
from util import polymorphic_union
from util import was_deleted
from util import with_parent
from writeonly import WriteOnlyCollection
from  import util as _sa_util

def __go(lcls = None):
    _sa_util.preloaded.import_prefix('sqlalchemy.orm')
    _sa_util.preloaded.import_prefix('sqlalchemy.ext')

__go(locals())
