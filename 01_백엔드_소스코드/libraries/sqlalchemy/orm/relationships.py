# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: relationships.pyc (Python 3.11)

'''Heuristics related to join conditions as used in
:func:`_orm.relationship`.

Provides the :class:`.JoinCondition` object, which encapsulates
SQL annotation and aliasing behavior focused on the `primaryjoin`
and `secondaryjoin` aspects of :func:`_orm.relationship`.

'''
from __future__ import annotations
import collections
from collections import abc
import dataclasses
import inspect as _py_inspect
import itertools
import re
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import strategy_options
from _typing import insp_is_aliased_class
from _typing import is_has_collection_adapter
from base import _DeclarativeMapped
from base import _is_mapped_class
from base import class_mapper
from base import DynamicMapped
from base import LoaderCallableStatus
from base import PassiveFlag
from base import state_str
from base import WriteOnlyMapped
from interfaces import _AttributeOptions
from interfaces import _IntrospectsAnnotations
from interfaces import MANYTOMANY
from interfaces import MANYTOONE
from interfaces import ONETOMANY
from interfaces import PropComparator
from interfaces import RelationshipDirection
from interfaces import StrategizedProperty
from util import _orm_annotate
from util import _orm_deannotate
from util import CascadeOptions
from  import exc as sa_exc
from  import Exists
from  import log
from  import schema
from  import sql
from  import util
from inspection import inspect
from sql import coercions
from sql import expression
from sql import operators
from sql import roles
from sql import visitors
from sql._typing import _ColumnExpressionArgument
from sql._typing import _HasClauseElement
from sql.annotation import _safe_annotate
from sql.elements import ColumnClause
from sql.elements import ColumnElement
from sql.util import _deep_annotate
from sql.util import _deep_deannotate
from sql.util import _shallow_annotate
from sql.util import adapt_criterion_to_null
from sql.util import ClauseAdapter
from sql.util import join_condition
from sql.util import selectables_overlap
from sql.util import visit_binary_product
from util.typing import de_optionalize_union_types
from util.typing import Literal
from util.typing import resolve_name_to_real_class_name
if typing.TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _ExternalEntityType
    from _typing import _IdentityKeyType
    from _typing import _InstanceDict
    from _typing import _InternalEntityType
    from _typing import _O
    from _typing import _RegistryType
    from base import Mapped
    from clsregistry import _class_resolver
    from clsregistry import _ModNS
    from decl_base import _ClassScanMapperConfig
    from dependency import DependencyProcessor
    from mapper import Mapper
    from query import Query
    from session import Session
    from state import InstanceState
    from strategies import LazyLoader
    from util import AliasedClass
    from util import AliasedInsp
    from sql._typing import _CoreAdapterProto
    from sql._typing import _EquivalentColumnMap
    from sql._typing import _InfoType
    from sql.annotation import _AnnotationDict
    from sql.annotation import SupportsAnnotations
    from sql.elements import BinaryExpression
    from sql.elements import BindParameter
    from sql.elements import ClauseElement
    from sql.schema import Table
    from sql.selectable import FromClause
    from util.typing import _AnnotationScanType
    from util.typing import RODescriptorReference
_T = TypeVar('_T', bound = Any)
_T1 = TypeVar('_T1', bound = Any)
_T2 = TypeVar('_T2', bound = Any)
_PT = TypeVar('_PT', bound = Any)
_PT2 = TypeVar('_PT2', bound = Any)
_RelationshipArgumentType = Union[(str, Type[_T], Callable[([], Type[_T])], 'Mapper[_T]', 'AliasedClass[_T]', Callable[([], 'Mapper[_T]')], Callable[([], 'AliasedClass[_T]')])]
_LazyLoadArgumentType = Literal[('select', 'joined', 'selectin', 'subquery', 'raise', 'raise_on_sql', 'noload', 'immediate', 'write_only', 'dynamic', True, False, None)]
_RelationshipJoinConditionArgument = Union[(str, _ColumnExpressionArgument[bool])]
_RelationshipSecondaryArgument = Union[('FromClause', str, Callable[([], 'FromClause')])]
_ORMOrderByArgument = Union[(Literal[False], str, _ColumnExpressionArgument[Any], Callable[([], _ColumnExpressionArgument[Any])], Callable[([], Iterable[_ColumnExpressionArgument[Any]])], Iterable[Union[(str, _ColumnExpressionArgument[Any])]])]
ORMBackrefArgument = Union[(str, Tuple[(str, Dict[(str, Any)])])]
_ORMColCollectionElement = Union[(ColumnClause[Any], _HasClauseElement[Any], roles.DMLColumnRole, 'Mapped[Any]')]
_ORMColCollectionArgument = Union[(str, Sequence[_ORMColCollectionElement], Callable[([], Sequence[_ORMColCollectionElement])], Callable[([], _ORMColCollectionElement)], _ORMColCollectionElement)]
_CEA = TypeVar('_CEA', bound = _ColumnExpressionArgument[Any])
_CE = TypeVar('_CE', bound = 'ColumnElement[Any]')
_ColumnPairIterable = Iterable[Tuple[(ColumnElement[Any], ColumnElement[Any])]]
_ColumnPairs = Sequence[Tuple[(ColumnElement[Any], ColumnElement[Any])]]
_MutableColumnPairs = List[Tuple[(ColumnElement[Any], ColumnElement[Any])]]

def remote(expr = None):
    """Annotate a portion of a primaryjoin expression
    with a 'remote' annotation.

    See the section :ref:`relationship_custom_foreign` for a
    description of use.

    .. seealso::

        :ref:`relationship_custom_foreign`

        :func:`.foreign`

    """
    return _annotate_columns(coercions.expect(roles.ColumnArgumentRole, expr), {
        'remote': True })


def foreign(expr = None):
    """Annotate a portion of a primaryjoin expression
    with a 'foreign' annotation.

    See the section :ref:`relationship_custom_foreign` for a
    description of use.

    .. seealso::

        :ref:`relationship_custom_foreign`

        :func:`.remote`

    """
    return _annotate_columns(coercions.expect(roles.ColumnArgumentRole, expr), {
        'foreign': True })


def _RelationshipArg():
    '''_RelationshipArg'''
    __doc__ = 'stores a user-defined parameter value that must be resolved and\n    parsed later at mapper configuration time.\n\n    '
    resolved: 'Optional[_T2]' = ('name', 'argument', 'resolved')
    
    def _is_populated(self = None):
        return self.argument is not None

    
    def _resolve_against_registry(self = None, clsregistry_resolver = None):
        attr_value = self.argument
        if isinstance(attr_value, str):
            self.resolved = clsregistry_resolver(attr_value, self.name == 'secondary')()
            return None
        if not None(attr_value) and _is_mapped_class(attr_value):
            self.resolved = attr_value()
            return None
        self.resolved = None


_RelationshipArg = <NODE:27>(_RelationshipArg, '_RelationshipArg', Generic[(_T1, _T2)])()
_RelationshipOrderByArg = Union[(Literal[False], Tuple[(ColumnElement[Any], ...)])]

class _RelationshipArgs(NamedTuple):
    remote_side: '_RelationshipArg[Optional[_ORMColCollectionArgument], Set[ColumnElement[Any]]]' = 'stores user-passed parameters that are resolved at mapper configuration\n    time.\n\n    '


def RelationshipProperty():
    '''RelationshipProperty'''
    pass
# WARNING: Decompyle incomplete

RelationshipProperty = <NODE:27>(RelationshipProperty, 'RelationshipProperty', _IntrospectsAnnotations, StrategizedProperty[_T], log.Identified)()

def _annotate_columns(element = dataclasses.dataclass, annotations = None):
    pass
# WARNING: Decompyle incomplete


class JoinCondition:
    _local_remote_pairs: 'Optional[_ColumnPairs]' = 'JoinCondition'
    
    def __init__(self = None, parent_persist_selectable = None, child_persist_selectable = None, parent_local_selectable = None, child_local_selectable = {
        'primaryjoin': None,
        'secondary': None,
        'secondaryjoin': None,
        'parent_equivalents': None,
        'child_equivalents': None,
        'consider_as_foreign_keys': None,
        'local_remote_pairs': None,
        'remote_side': None,
        'self_referential': False,
        'support_sync': True,
        'can_be_synced_fn': (lambda : True) }, *, primaryjoin, secondary, secondaryjoin, parent_equivalents, child_equivalents, consider_as_foreign_keys, local_remote_pairs, remote_side, self_referential, prop, support_sync, can_be_synced_fn):
        self.parent_persist_selectable = parent_persist_selectable
        self.parent_local_selectable = parent_local_selectable
        self.child_persist_selectable = child_persist_selectable
        self.child_local_selectable = child_local_selectable
        self.parent_equivalents = parent_equivalents
        self.child_equivalents = child_equivalents
        self.primaryjoin_initial = primaryjoin
        self.secondaryjoin = secondaryjoin
        self.secondary = secondary
        self.consider_as_foreign_keys = consider_as_foreign_keys
        self._local_remote_pairs = local_remote_pairs
        self._remote_side = remote_side
        self.prop = prop
        self.self_referential = self_referential
        self.support_sync = support_sync
        self.can_be_synced_fn = can_be_synced_fn
        self._determine_joins()
    # WARNING: Decompyle incomplete

    
    def _log_joins(self = None):
