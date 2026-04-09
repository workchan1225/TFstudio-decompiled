# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: selectable.pyc (Python 3.11)

'''The :class:`_expression.FromClause` class of SQL expression elements,
representing
SQL tables and derived rowsets.

'''
from __future__ import annotations
import collections
from enum import Enum
import itertools
from typing import AbstractSet
from typing import Any as TODO_Any
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import cache_key
from  import coercions
from  import operators
from  import roles
from  import traversals
from  import type_api
from  import visitors
from _typing import _ColumnsClauseArgument
from _typing import _no_kw
from _typing import _T
from _typing import _TP
from _typing import is_column_element
from _typing import is_select_statement
from _typing import is_subquery
from _typing import is_table
from _typing import is_text_clause
from annotation import Annotated
from annotation import SupportsCloneAnnotations
from base import _clone
from base import _cloned_difference
from base import _cloned_intersection
from base import _entity_namespace_key
from base import _EntityNamespace
from base import _expand_cloned
from base import _from_objects
from base import _generative
from base import _never_select_column
from base import _NoArg
from base import _select_iterables
from base import CacheableOptions
from base import ColumnCollection
from base import ColumnSet
from base import CompileState
from base import DedupeColumnCollection
from base import DialectKWArgs
from base import Executable
from base import Generative
from base import HasCompileState
from base import HasMemoized
from base import Immutable
from coercions import _document_text_coercion
from elements import _anonymous_label
from elements import BindParameter
from elements import BooleanClauseList
from elements import ClauseElement
from elements import ClauseList
from elements import ColumnClause
from elements import ColumnElement
from elements import DQLDMLClauseElement
from elements import GroupedElement
from elements import literal_column
from elements import TableValuedColumn
from elements import UnaryExpression
from operators import OperatorType
from sqltypes import NULLTYPE
from visitors import _TraverseInternalsType
from visitors import InternalTraversal
from visitors import prefix_anon_map
from  import exc
from  import util
from util import HasMemoized_ro_memoized_attribute
from util.typing import Literal
from util.typing import Protocol
from util.typing import Self
and_ = BooleanClauseList.and_
if TYPE_CHECKING:
    from _typing import _ColumnExpressionArgument
    from _typing import _ColumnExpressionOrStrLabelArgument
    from _typing import _FromClauseArgument
    from _typing import _JoinTargetArgument
    from _typing import _LimitOffsetType
    from _typing import _MAYBE_ENTITY
    from _typing import _NOT_ENTITY
    from _typing import _OnClauseArgument
    from _typing import _SelectStatementForCompoundArgument
    from _typing import _T0
    from _typing import _T1
    from _typing import _T2
    from _typing import _T3
    from _typing import _T4
    from _typing import _T5
    from _typing import _T6
    from _typing import _T7
    from _typing import _TextCoercedExpressionArgument
    from _typing import _TypedColumnClauseArgument as _TCCA
    from _typing import _TypeEngineArgument
    from base import _AmbiguousTableNameMap
    from base import ExecutableOption
    from base import ReadOnlyColumnCollection
    from cache_key import _CacheKeyTraversalType
    from compiler import SQLCompiler
    from dml import Delete
    from dml import Update
    from elements import BinaryExpression
    from elements import KeyedColumnElement
    from elements import Label
    from elements import NamedColumn
    from elements import TextClause
    from functions import Function
    from schema import ForeignKey
    from schema import ForeignKeyConstraint
    from sqltypes import TableValueType
    from type_api import TypeEngine
    from visitors import _CloneCallableType
_ColumnsClauseElement = Union[('FromClause', ColumnElement[Any], 'TextClause')]
_LabelConventionCallable = Callable[([
    Union[('ColumnElement[Any]', 'TextClause')]], Optional[str])]

class _JoinTargetProtocol(Protocol):
    _from_objects = (lambda self = None: pass)()
    entity_namespace = (lambda self = None: pass)()

_JoinTargetElement = Union[('FromClause', _JoinTargetProtocol)]
_OnClauseElement = Union[('ColumnElement[bool]', _JoinTargetProtocol)]
_ForUpdateOfArgument = Union[(Union[('_ColumnExpressionArgument[Any]', '_FromClauseArgument')], Sequence['_ColumnExpressionArgument[Any]'])]
_SetupJoinsElement = Tuple[(_JoinTargetElement, Optional[_OnClauseElement], Optional['FromClause'], Dict[(str, Any)])]
_SelectIterable = Iterable[Union[('ColumnElement[Any]', 'TextClause')]]

def _OffsetLimitParam():
    '''_OffsetLimitParam'''
    inherit_cache = True
    _limit_offset_value = (lambda self = None: self.effective_value)()

_OffsetLimitParam = <NODE:27>(_OffsetLimitParam, '_OffsetLimitParam', BindParameter[int])

class ReturnsRows(DQLDMLClauseElement, roles.ReturnsRowsRole):
    '''The base-most class for Core constructs that have some concept of
    columns that can represent rows.

    While the SELECT statement and TABLE are the primary things we think
    of in this category,  DML like INSERT, UPDATE and DELETE can also specify
    RETURNING which means they can be used in CTEs and other forms, and
    PostgreSQL has functions that return rows also.

    .. versionadded:: 1.4

    '''
    _is_returns_rows = True
    _is_from_clause = False
    _is_select_base = False
    _is_select_statement = False
    _is_lateral = False
    selectable = (lambda self = None: self)()
    _all_selected_columns = (lambda self = None: raise NotImplementedError())()
    
    def is_derived_from(self = None, fromclause = None):
        """Return ``True`` if this :class:`.ReturnsRows` is
        'derived' from the given :class:`.FromClause`.

        An example would be an Alias of a Table is derived from that Table.

        """
        raise NotImplementedError()

    
    def _generate_fromclause_column_proxies(self, fromclause = None, columns = None, primary_key = None, foreign_keys = ('fromclause', 'FromClause', 'columns', 'ColumnCollection[str, KeyedColumnElement[Any]]', 'primary_key', 'ColumnSet', 'foreign_keys', 'Set[KeyedColumnElement[Any]]', 'return', 'None')):
        '''Populate columns into an :class:`.AliasedReturnsRows` object.'''
        raise NotImplementedError()

    
    def _refresh_for_new_column(self = None, column = None):
        '''reset internal collections for an incoming column being added.'''
        raise NotImplementedError()

    exported_columns = (lambda self = None: raise NotImplementedError())()


class ExecutableReturnsRows(ReturnsRows, Executable):
    '''base for executable statements that return rows.'''
    pass


def TypedReturnsRows():
    '''TypedReturnsRows'''
    __doc__ = 'base for a typed executable statements that return rows.'

TypedReturnsRows = <NODE:27>(TypedReturnsRows, 'TypedReturnsRows', ExecutableReturnsRows, Generic[_TP])

class Selectable(ReturnsRows):
    '''Mark a class as being selectable.'''
    __visit_name__ = 'selectable'
    is_selectable = True
    
    def _refresh_for_new_column(self = None, column = None):
        raise NotImplementedError()

    
    def lateral(self = None, name = None):
        '''Return a LATERAL alias of this :class:`_expression.Selectable`.

        The return value is the :class:`_expression.Lateral` construct also
        provided by the top-level :func:`_expression.lateral` function.

        .. seealso::

            :ref:`tutorial_lateral_correlation` -  overview of usage.

        '''
        return Lateral._construct(self, name = name)

    replace_selectable = (lambda self = None, old = util.deprecated('1.4', message = 'The :meth:`.Selectable.replace_selectable` method is deprecated, and will be removed in a future release.  Similar functionality is available via the sqlalchemy.sql.visitors module.'), alias = util.preload_module('sqlalchemy.sql.util'): util.preloaded.sql_util.ClauseAdapter(alias).traverse(self))()()
    
    def corresponding_column(self = None, column = None, require_embedded = None):
        '''Given a :class:`_expression.ColumnElement`, return the exported
        :class:`_expression.ColumnElement` object from the
        :attr:`_expression.Selectable.exported_columns`
        collection of this :class:`_expression.Selectable`
        which corresponds to that
        original :class:`_expression.ColumnElement` via a common ancestor
        column.

        :param column: the target :class:`_expression.ColumnElement`
                      to be matched.

        :param require_embedded: only return corresponding columns for
         the given :class:`_expression.ColumnElement`, if the given
         :class:`_expression.ColumnElement`
         is actually present within a sub-element
         of this :class:`_expression.Selectable`.
         Normally the column will match if
         it merely shares a common ancestor with one of the exported
         columns of this :class:`_expression.Selectable`.

        .. seealso::

            :attr:`_expression.Selectable.exported_columns` - the
            :class:`_expression.ColumnCollection`
            that is used for the operation.

            :meth:`_expression.ColumnCollection.corresponding_column`
            - implementation
            method.

        '''
        return self.exported_columns.corresponding_column(column, require_embedded)



class HasPrefixes:
    _prefixes: 'Tuple[Tuple[DQLDMLClauseElement, str], ...]' = ()
    _has_prefixes_traverse_internals: '_TraverseInternalsType' = [
        ('_prefixes', InternalTraversal.dp_prefix_sequence)]
    prefix_with = (lambda self = None, *, dialect: pass# WARNING: Decompyle incomplete
)()()


class HasSuffixes:
    _suffixes: 'Tuple[Tuple[DQLDMLClauseElement, str], ...]' = ()
    _has_suffixes_traverse_internals: '_TraverseInternalsType' = [
        ('_suffixes', InternalTraversal.dp_prefix_sequence)]
    suffix_with = (lambda self = None, *, dialect: pass# WARNING: Decompyle incomplete
)()()


class HasHints:
    _hints: 'util.immutabledict[Tuple[FromClause, str], str]' = util.immutabledict()
    _statement_hints: 'Tuple[Tuple[str, str], ...]' = ()
    _has_hints_traverse_internals: '_TraverseInternalsType' = [
        ('_statement_hints', InternalTraversal.dp_statement_hint_list),
        ('_hints', InternalTraversal.dp_table_hint_list)]
    with_statement_hint = (lambda self = None, text = None, dialect_name = _generative: self._with_hint(None, text, dialect_name))()
    with_hint = (lambda self = None, selectable = None, text = _generative, dialect_name = ('*',): self._with_hint(selectable, text, dialect_name))()
    
    def _with_hint(self = None, selectable = None, text = None, dialect_name = ('selectable', 'Optional[_FromClauseArgument]', 'text', 'str', 'dialect_name', 'str', 'return', 'Self')):
        pass
    # WARNING: Decompyle incomplete



class FromClause(Selectable, roles.AnonymizedFromClauseRole):
    '''Represent an element that can be used within the ``FROM``
    clause of a ``SELECT`` statement.

    The most common forms of :class:`_expression.FromClause` are the
    :class:`_schema.Table` and the :func:`_expression.select` constructs.  Key
    features common to all :class:`_expression.FromClause` objects include:

    * a :attr:`.c` collection, which provides per-name access to a collection
      of :class:`_expression.ColumnElement` objects.
    * a :attr:`.primary_key` attribute, which is a collection of all those
      :class:`_expression.ColumnElement`
      objects that indicate the ``primary_key`` flag.
    * Methods to generate various derivations of a "from" clause, including
      :meth:`_expression.FromClause.alias`,
      :meth:`_expression.FromClause.join`,
      :meth:`_expression.FromClause.select`.


    '''
    __visit_name__ = 'fromclause'
    named_with_column = False
    _columns: 'ColumnCollection[Any, Any]' = (lambda self = None: ())()
    schema: 'Optional[str]' = None
    is_selectable = True
    _is_from_clause = True
    _is_join = False
    _use_schema_map = False
    
    def select(self = None):
        '''Return a SELECT of this :class:`_expression.FromClause`.


        e.g.::

            stmt = some_table.select().where(some_table.c.id == 5)

        .. seealso::

            :func:`_expression.select` - general purpose
            method which allows for arbitrary column lists.

        '''
        return Select(self)

    
    def join(self = None, right = None, onclause = None, isouter = (None, False, False), full = ('right', '_FromClauseArgument', 'onclause', 'Optional[_ColumnExpressionArgument[bool]]', 'isouter', 'bool', 'full', 'bool', 'return', 'Join')):
        '''Return a :class:`_expression.Join` from this
        :class:`_expression.FromClause`
        to another :class:`FromClause`.

        E.g.::

            from sqlalchemy import join

            j = user_table.join(
                address_table, user_table.c.id == address_table.c.user_id
            )
            stmt = select(user_table).select_from(j)

        would emit SQL along the lines of:

        .. sourcecode:: sql

            SELECT user.id, user.name FROM user
            JOIN address ON user.id = address.user_id

        :param right: the right side of the join; this is any
         :class:`_expression.FromClause` object such as a
         :class:`_schema.Table` object, and
         may also be a selectable-compatible object such as an ORM-mapped
         class.

        :param onclause: a SQL expression representing the ON clause of the
         join.  If left at ``None``, :meth:`_expression.FromClause.join`
         will attempt to
         join the two tables based on a foreign key relationship.

        :param isouter: if True, render a LEFT OUTER JOIN, instead of JOIN.

        :param full: if True, render a FULL OUTER JOIN, instead of LEFT OUTER
         JOIN.  Implies :paramref:`.FromClause.join.isouter`.

        .. seealso::

            :func:`_expression.join` - standalone function

            :class:`_expression.Join` - the type of object produced

        '''
        return Join(self, right, onclause, isouter, full)

    
    def outerjoin(self = None, right = None, onclause = None, full = (None, False)):
        '''Return a :class:`_expression.Join` from this
        :class:`_expression.FromClause`
        to another :class:`FromClause`, with the "isouter" flag set to
        True.

        E.g.::

            from sqlalchemy import outerjoin

            j = user_table.outerjoin(
                address_table, user_table.c.id == address_table.c.user_id
            )

        The above is equivalent to::

            j = user_table.join(
                address_table, user_table.c.id == address_table.c.user_id, isouter=True
            )

        :param right: the right side of the join; this is any
         :class:`_expression.FromClause` object such as a
         :class:`_schema.Table` object, and
         may also be a selectable-compatible object such as an ORM-mapped
         class.

        :param onclause: a SQL expression representing the ON clause of the
         join.  If left at ``None``, :meth:`_expression.FromClause.join`
         will attempt to
         join the two tables based on a foreign key relationship.

        :param full: if True, render a FULL OUTER JOIN, instead of
         LEFT OUTER JOIN.

        .. seealso::

            :meth:`_expression.FromClause.join`

            :class:`_expression.Join`

        '''
        return Join(self, right, onclause, True, full)

    
    def alias(self = None, name = None, flat = None):
        '''Return an alias of this :class:`_expression.FromClause`.

        E.g.::

            a2 = some_table.alias("a2")

        The above code creates an :class:`_expression.Alias`
        object which can be used
        as a FROM clause in any SELECT statement.

        .. seealso::

            :ref:`tutorial_using_aliases`

            :func:`_expression.alias`

        '''
        return Alias._construct(self, name = name)

    
    def tablesample(self = None, sampling = None, name = None, seed = (None, None)):
        '''Return a TABLESAMPLE alias of this :class:`_expression.FromClause`.

        The return value is the :class:`_expression.TableSample`
        construct also
        provided by the top-level :func:`_expression.tablesample` function.

        .. seealso::

            :func:`_expression.tablesample` - usage guidelines and parameters

        '''
        return TableSample._construct(self, sampling = sampling, name = name, seed = seed)

    
    def is_derived_from(self = None, fromclause = None):
        """Return ``True`` if this :class:`_expression.FromClause` is
        'derived' from the given ``FromClause``.

        An example would be an Alias of a Table is derived from that Table.

        """
        return fromclause in self._cloned_set

    
    def _is_lexical_equivalent(self = None, other = None):
        '''Return ``True`` if this :class:`_expression.FromClause` and
        the other represent the same lexical identity.

        This tests if either one is a copy of the other, or
        if they are the same via annotation identity.

        '''
        return bool(self._cloned_set.intersection(other._cloned_set))

    description = (lambda self = None: getattr(self, 'name', self.__class__.__name__ + ' object'))()
    
    def _generate_fromclause_column_proxies(self, fromclause = None, columns = None, primary_key = None, foreign_keys = ('fromclause', 'FromClause', 'columns', 'ColumnCollection[str, KeyedColumnElement[Any]]', 'primary_key', 'ColumnSet', 'foreign_keys', 'Set[KeyedColumnElement[Any]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    exported_columns = (lambda self = None: self.c)()
    columns = (lambda self = None: self.c)()
    c = (lambda self = None: if '_columns' not in self.__dict__:
self._setup_collections()self._columns.as_readonly())()
    
    def _setup_collections(self = None):
        util.mini_gil
    # WARNING: Decompyle incomplete

    entity_namespace = (lambda self = None: self.c)()
    primary_key = (lambda self = None: self._setup_collections()self.primary_key)()
    foreign_keys = (lambda self = None: self._setup_collections()self.foreign_keys)()
    
    def _reset_column_collection(self = None):
        '''Reset the attributes linked to the ``FromClause.c`` attribute.

        This collection is separate from all the other memoized things
        as it has shown to be sensitive to being cleared out in situations
        where enclosing code, typically in a replacement traversal scenario,
        has already established strong relationships
        with the exported columns.

        The collection is cleared for the case where a table is having a
        column added to it as well as within a Join during copy internals.

        '''
        for key in ('_columns', 'columns', 'c', 'primary_key', 'foreign_keys'):
            self.__dict__.pop(key, None)
            return None

    _select_iterable = (lambda self = None: self.c())()
    _cols_populated = (lambda self = None: '_columns' in self.__dict__)()
    
    def _populate_column_collection(self = None, columns = None, primary_key = None, foreign_keys = ('columns', 'ColumnCollection[str, KeyedColumnElement[Any]]', 'primary_key', 'ColumnSet', 'foreign_keys', 'Set[KeyedColumnElement[Any]]', 'return', 'None')):
        '''Called on subclasses to establish the .c collection.

        Each implementation has a different way of establishing
        this collection.

        '''
        pass

    
    def _refresh_for_new_column(self = None, column = None):
        '''Given a column added to the .c collection of an underlying
        selectable, produce the local version of that column, assuming this
        selectable ultimately should proxy this column.

        this is used to "ping" a derived selectable to add a new column
        to its .c. collection when a Column has been added to one of the
        Table objects it ultimately derives from.

        If the given selectable hasn\'t populated its .c. collection yet,
        it should at least pass on the message to the contained selectables,
        but it will return None.

        This method is currently used by Declarative to allow Table
        columns to be added to a partially constructed inheritance
        mapping that may have already produced joins.  The method
        isn\'t public right now, as the full span of implications
        and/or caveats aren\'t yet clear.

        It\'s also possible that this functionality could be invoked by
        default via an event, which would require that
        selectables maintain a weak referencing collection of all
        derivations.

        '''
        self._reset_column_collection()

    
    def _anonymous_fromclause(self = None, *, name, flat):
        return self.alias(name = name)

    if TYPE_CHECKING:
        
        def self_group(self = None, against = None):
            pass

        return None


class NamedFromClause(FromClause):
    '''A :class:`.FromClause` that has a name.

    Examples include tables, subqueries, CTEs, aliased tables.

    .. versionadded:: 2.0

    '''
    name: 'str' = True
    table_valued = (lambda self = None: TableValuedColumn(self, type_api.TABLEVALUE))()


class SelectLabelStyle(Enum):
    '''Label style constants that may be passed to
    :meth:`_sql.Select.set_label_style`.'''
    LABEL_STYLE_NONE = 0
    LABEL_STYLE_TABLENAME_PLUS_COL = 1
    LABEL_STYLE_DISAMBIGUATE_ONLY = 2
    LABEL_STYLE_DEFAULT = LABEL_STYLE_DISAMBIGUATE_ONLY
    LABEL_STYLE_LEGACY_ORM = 3

(LABEL_STYLE_NONE, LABEL_STYLE_TABLENAME_PLUS_COL, LABEL_STYLE_DISAMBIGUATE_ONLY, _) = list(SelectLabelStyle)
LABEL_STYLE_DEFAULT = LABEL_STYLE_DISAMBIGUATE_ONLY

class Join(FromClause, roles.DMLTableRole):
    pass
# WARNING: Decompyle incomplete


class NoInit:
    
    def __init__(self = None, *arg, **kw):
        raise NotImplementedError(f'''The {self.__class__.__name__!s} class is not intended to be constructed directly.  Please use the {self.__class__.__name__.lower()!s}() standalone function or the {self.__class__.__name__.lower()!s}() method available from appropriate selectable objects.''')



class LateralFromClause(NamedFromClause):
    '''mark a FROM clause as being able to render directly as LATERAL'''
    pass


class AliasedReturnsRows(NamedFromClause, NoInit):
    pass
# WARNING: Decompyle incomplete


class FromClauseAlias(AliasedReturnsRows):
    element: 'FromClause' = 'FromClauseAlias'
    description = (lambda self = None: name = self.nameif isinstance(name, _anonymous_label):
f'''Anonymous alias of {self.element.description}''')()


class Alias(FromClauseAlias, roles.DMLTableRole):
    '''Represents an table or selectable alias (AS).

    Represents an alias, as typically applied to any table or
    sub-select within a SQL statement using the ``AS`` keyword (or
    without the keyword on certain databases such as Oracle Database).

    This object is constructed from the :func:`_expression.alias` module
    level function as well as the :meth:`_expression.FromClause.alias`
    method available
    on all :class:`_expression.FromClause` subclasses.

    .. seealso::

        :meth:`_expression.FromClause.alias`

    '''
    __visit_name__ = 'alias'
    element: 'FromClause' = True
    _factory = (lambda cls = None, selectable = None, name = classmethod, flat = (None, False): coercions.expect(roles.FromClauseRole, selectable, allow_select = True).alias(name = name, flat = flat))()


class TableValuedAlias(Alias, LateralFromClause):
    pass
# WARNING: Decompyle incomplete


class Lateral(LateralFromClause, FromClauseAlias):
    '''Represent a LATERAL subquery.

    This object is constructed from the :func:`_expression.lateral` module
    level function as well as the :meth:`_expression.FromClause.lateral`
    method available
    on all :class:`_expression.FromClause` subclasses.

    While LATERAL is part of the SQL standard, currently only more recent
    PostgreSQL versions provide support for this keyword.

    .. seealso::

        :ref:`tutorial_lateral_correlation` -  overview of usage.

    '''
    __visit_name__ = 'lateral'
    _is_lateral = True
    inherit_cache = True
    _factory = (lambda cls = None, selectable = None, name = classmethod: coercions.expect(roles.FromClauseRole, selectable, explicit_subquery = True).lateral(name = name))()


class TableSample(FromClauseAlias):
    pass
# WARNING: Decompyle incomplete


class CTE(AliasedReturnsRows, HasSuffixes, HasPrefixes, Generative, roles.IsCTERole, roles.DMLTableRole):
    pass
# WARNING: Decompyle incomplete


class _CTEOpts(NamedTuple):
    nesting: 'bool' = '_CTEOpts'


class _ColumnsPlusNames(NamedTuple):
    repeated: 'bool' = '_ColumnsPlusNames'


class SelectsRows(ReturnsRows):
    '''Sub-base of ReturnsRows for elements that deliver rows
    directly, namely SELECT and INSERT/UPDATE/DELETE..RETURNING'''
    _label_style: 'SelectLabelStyle' = LABEL_STYLE_NONE
    
    def _generate_columns_plus_names(self = None, anon_for_dupe_key = None, cols = None):
        """Generate column names as rendered in a SELECT statement by
        the compiler, as well as tokens used to populate the .c. collection
        on a :class:`.FromClause`.

        This is distinct from the _column_naming_convention generator that's
        intended for population of the Select.selected_columns collection,
        different rules.   the collection returned here calls upon the
        _column_naming_convention as well.

        """
        pass
    # WARNING: Decompyle incomplete



class HasCTE(SelectsRows, roles.HasCTERole):
    '''Mixin that declares a class to include CTE support.'''
    _has_ctes_traverse_internals: '_TraverseInternalsType' = [
        ('_independent_ctes', InternalTraversal.dp_clauseelement_list),
        ('_independent_ctes_opts', InternalTraversal.dp_plain_obj)]
    _independent_ctes: 'Tuple[CTE, ...]' = ()
    _independent_ctes_opts: 'Tuple[_CTEOpts, ...]' = ()
    name_cte_columns: 'bool' = False
    add_cte = (lambda self = None, *, nest_here: opt = _CTEOpts(nest_here)for cte in ctes:
cte = coercions.expect(roles.IsCTERole, cte)self)()
    
    def cte(self = None, name = None, recursive = None, nesting = (None, False, False)):
        '''Return a new :class:`_expression.CTE`,
        or Common Table Expression instance.

        Common table expressions are a SQL standard whereby SELECT
        statements can draw upon secondary statements specified along
        with the primary statement, using a clause called "WITH".
        Special semantics regarding UNION can also be employed to
        allow "recursive" queries, where a SELECT statement can draw
        upon the set of rows that have previously been selected.

        CTEs can also be applied to DML constructs UPDATE, INSERT
        and DELETE on some databases, both as a source of CTE rows
        when combined with RETURNING, as well as a consumer of
        CTE rows.

        SQLAlchemy detects :class:`_expression.CTE` objects, which are treated
        similarly to :class:`_expression.Alias` objects, as special elements
        to be delivered to the FROM clause of the statement as well
        as to a WITH clause at the top of the statement.

        For special prefixes such as PostgreSQL "MATERIALIZED" and
        "NOT MATERIALIZED", the :meth:`_expression.CTE.prefix_with`
        method may be
        used to establish these.

        .. versionchanged:: 1.3.13 Added support for prefixes.
           In particular - MATERIALIZED and NOT MATERIALIZED.

        :param name: name given to the common table expression.  Like
         :meth:`_expression.FromClause.alias`, the name can be left as
         ``None`` in which case an anonymous symbol will be used at query
         compile time.
        :param recursive: if ``True``, will render ``WITH RECURSIVE``.
         A recursive common table expression is intended to be used in
         conjunction with UNION ALL in order to derive rows
         from those already selected.
        :param nesting: if ``True``, will render the CTE locally to the
         statement in which it is referenced.   For more complex scenarios,
         the :meth:`.HasCTE.add_cte` method using the
         :paramref:`.HasCTE.add_cte.nest_here`
         parameter may also be used to more carefully
         control the exact placement of a particular CTE.

         .. versionadded:: 1.4.24

         .. seealso::

            :meth:`.HasCTE.add_cte`

        The following examples include two from PostgreSQL\'s documentation at
        https://www.postgresql.org/docs/current/static/queries-with.html,
        as well as additional examples.

        Example 1, non recursive::

            from sqlalchemy import (
                Table,
                Column,
                String,
                Integer,
                MetaData,
                select,
                func,
            )

            metadata = MetaData()

            orders = Table(
                "orders",
                metadata,
                Column("region", String),
                Column("amount", Integer),
                Column("product", String),
                Column("quantity", Integer),
            )

            regional_sales = (
                select(orders.c.region, func.sum(orders.c.amount).label("total_sales"))
                .group_by(orders.c.region)
                .cte("regional_sales")
            )


            top_regions = (
                select(regional_sales.c.region)
                .where(
                    regional_sales.c.total_sales
                    > select(func.sum(regional_sales.c.total_sales) / 10)
                )
                .cte("top_regions")
            )

            statement = (
                select(
                    orders.c.region,
                    orders.c.product,
                    func.sum(orders.c.quantity).label("product_units"),
                    func.sum(orders.c.amount).label("product_sales"),
                )
                .where(orders.c.region.in_(select(top_regions.c.region)))
                .group_by(orders.c.region, orders.c.product)
            )

            result = conn.execute(statement).fetchall()

        Example 2, WITH RECURSIVE::

            from sqlalchemy import (
                Table,
                Column,
                String,
                Integer,
                MetaData,
                select,
                func,
            )

            metadata = MetaData()

            parts = Table(
                "parts",
                metadata,
                Column("part", String),
                Column("sub_part", String),
                Column("quantity", Integer),
            )

            included_parts = (
                select(parts.c.sub_part, parts.c.part, parts.c.quantity)
                .where(parts.c.part == "our part")
                .cte(recursive=True)
            )


            incl_alias = included_parts.alias()
            parts_alias = parts.alias()
            included_parts = included_parts.union_all(
                select(
                    parts_alias.c.sub_part, parts_alias.c.part, parts_alias.c.quantity
                ).where(parts_alias.c.part == incl_alias.c.sub_part)
            )

            statement = select(
                included_parts.c.sub_part,
                func.sum(included_parts.c.quantity).label("total_quantity"),
            ).group_by(included_parts.c.sub_part)

            result = conn.execute(statement).fetchall()

        Example 3, an upsert using UPDATE and INSERT with CTEs::

            from datetime import date
            from sqlalchemy import (
                MetaData,
                Table,
                Column,
                Integer,
                Date,
                select,
                literal,
                and_,
                exists,
            )

            metadata = MetaData()

            visitors = Table(
                "visitors",
                metadata,
                Column("product_id", Integer, primary_key=True),
                Column("date", Date, primary_key=True),
                Column("count", Integer),
            )

            # add 5 visitors for the product_id == 1
            product_id = 1
            day = date.today()
            count = 5

            update_cte = (
                visitors.update()
                .where(
                    and_(visitors.c.product_id == product_id, visitors.c.date == day)
                )
                .values(count=visitors.c.count + count)
                .returning(literal(1))
                .cte("update_cte")
            )

            upsert = visitors.insert().from_select(
                [visitors.c.product_id, visitors.c.date, visitors.c.count],
                select(literal(product_id), literal(day), literal(count)).where(
                    ~exists(update_cte.select())
                ),
            )

            connection.execute(upsert)

        Example 4, Nesting CTE (SQLAlchemy 1.4.24 and above)::

            value_a = select(literal("root").label("n")).cte("value_a")

            # A nested CTE with the same name as the root one
            value_a_nested = select(literal("nesting").label("n")).cte(
                "value_a", nesting=True
            )

            # Nesting CTEs takes ascendency locally
            # over the CTEs at a higher level
            value_b = select(value_a_nested.c.n).cte("value_b")

            value_ab = select(value_a.c.n.label("a"), value_b.c.n.label("b"))

        The above query will render the second CTE nested inside the first,
        shown with inline parameters below as:

        .. sourcecode:: sql

            WITH
                value_a AS
                    (SELECT \'root\' AS n),
                value_b AS
                    (WITH value_a AS
                        (SELECT \'nesting\' AS n)
                    SELECT value_a.n AS n FROM value_a)
            SELECT value_a.n AS a, value_b.n AS b
            FROM value_a, value_b

        The same CTE can be set up using the :meth:`.HasCTE.add_cte` method
        as follows (SQLAlchemy 2.0 and above)::

            value_a = select(literal("root").label("n")).cte("value_a")

            # A nested CTE with the same name as the root one
            value_a_nested = select(literal("nesting").label("n")).cte("value_a")

            # Nesting CTEs takes ascendency locally
            # over the CTEs at a higher level
            value_b = (
                select(value_a_nested.c.n)
                .add_cte(value_a_nested, nest_here=True)
                .cte("value_b")
            )

            value_ab = select(value_a.c.n.label("a"), value_b.c.n.label("b"))

        Example 5, Non-Linear CTE (SQLAlchemy 1.4.28 and above)::

            edge = Table(
                "edge",
                metadata,
                Column("id", Integer, primary_key=True),
                Column("left", Integer),
                Column("right", Integer),
            )

            root_node = select(literal(1).label("node")).cte("nodes", recursive=True)

            left_edge = select(edge.c.left).join(
                root_node, edge.c.right == root_node.c.node
            )
            right_edge = select(edge.c.right).join(
                root_node, edge.c.left == root_node.c.node
            )

            subgraph_cte = root_node.union(left_edge, right_edge)

            subgraph = select(subgraph_cte)

        The above query will render 2 UNIONs inside the recursive CTE:

        .. sourcecode:: sql

            WITH RECURSIVE nodes(node) AS (
                    SELECT 1 AS node
                UNION
                    SELECT edge."left" AS "left"
                    FROM edge JOIN nodes ON edge."right" = nodes.node
                UNION
                    SELECT edge."right" AS "right"
                    FROM edge JOIN nodes ON edge."left" = nodes.node
            )
            SELECT nodes.node FROM nodes

        .. seealso::

            :meth:`_orm.Query.cte` - ORM version of
            :meth:`_expression.HasCTE.cte`.

        '''
        return CTE._construct(self, name = name, recursive = recursive, nesting = nesting)



class Subquery(AliasedReturnsRows):
    '''Represent a subquery of a SELECT.

    A :class:`.Subquery` is created by invoking the
    :meth:`_expression.SelectBase.subquery` method, or for convenience the
    :meth:`_expression.SelectBase.alias` method, on any
    :class:`_expression.SelectBase` subclass
    which includes :class:`_expression.Select`,
    :class:`_expression.CompoundSelect`, and
    :class:`_expression.TextualSelect`.  As rendered in a FROM clause,
    it represents the
    body of the SELECT statement inside of parenthesis, followed by the usual
    "AS <somename>" that defines all "alias" objects.

    The :class:`.Subquery` object is very similar to the
    :class:`_expression.Alias`
    object and can be used in an equivalent way.    The difference between
    :class:`_expression.Alias` and :class:`.Subquery` is that
    :class:`_expression.Alias` always
    contains a :class:`_expression.FromClause` object whereas
    :class:`.Subquery`
    always contains a :class:`_expression.SelectBase` object.

    .. versionadded:: 1.4 The :class:`.Subquery` class was added which now
       serves the purpose of providing an aliased version of a SELECT
       statement.

    '''
    __visit_name__ = 'subquery'
    _is_subquery = True
    element: 'SelectBase' = True
    _factory = (lambda cls = None, selectable = None, name = classmethod: coercions.expect(roles.SelectStatementRole, selectable).subquery(name = name))()
    as_scalar = (lambda self = None: self.element.set_label_style(LABEL_STYLE_NONE).scalar_subquery())()


class FromGrouping(FromClause, GroupedElement):
    '''Represent a grouping of a FROM clause'''
    element: 'FromClause' = [
        ('element', InternalTraversal.dp_clauseelement)]
    
    def __init__(self = None, element = None):
        self.element = coercions.expect(roles.FromClauseRole, element)

    columns = (lambda self = None: self.element.columns)()
    c = (lambda self = None: self.element.columns)()
    primary_key = (lambda self = None: self.element.primary_key)()
    foreign_keys = (lambda self = None: self.element.foreign_keys)()
    
    def is_derived_from(self = None, fromclause = None):
        return self.element.is_derived_from(fromclause)

    
    def alias(self = None, name = None, flat = None):
        return NamedFromGrouping(self.element.alias(name = name, flat = flat))

    
    def _anonymous_fromclause(self = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    _hide_froms = (lambda self = None: self.element._hide_froms)()
    _from_objects = (lambda self = None: self.element._from_objects)()
    
    def __getstate__(self = None):
        return {
            'element': self.element }

    
    def __setstate__(self = None, state = None):
        self.element = state['element']

    if TYPE_CHECKING:
        
        def self_group(self = None, against = None):
            pass

        return None


class NamedFromGrouping(NamedFromClause, FromGrouping):
    '''represent a grouping of a named FROM clause

    .. versionadded:: 2.0

    '''
    inherit_cache = True
    if TYPE_CHECKING:
        
        def self_group(self = None, against = None):
            pass

        return None


class TableClause(NamedFromClause, Immutable, roles.DMLTableRole):
    pass
# WARNING: Decompyle incomplete

ForUpdateParameter = Union[('ForUpdateArg', None, bool, Dict[(str, Any)])]

class ForUpdateArg(ClauseElement):
    skip_locked: 'bool' = [
        ('of', InternalTraversal.dp_clauseelement_list),
        ('nowait', InternalTraversal.dp_boolean),
        ('read', InternalTraversal.dp_boolean),
        ('skip_locked', InternalTraversal.dp_boolean),
        ('key_share', InternalTraversal.dp_boolean)]
    _from_argument = (lambda cls = None, with_for_update = None: if isinstance(with_for_update, ForUpdateArg):
with_for_updateif None in (None, False):
Noneif None is True:
ForUpdateArg()# WARNING: Decompyle incomplete
)()
    
    def __eq__(self = None, other = None):
