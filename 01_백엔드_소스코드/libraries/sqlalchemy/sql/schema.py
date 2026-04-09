# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: schema.pyc (Python 3.11)

'''The schema module provides the building blocks for database metadata.

Each element within this module describes a database entity which can be
created and dropped, or is otherwise part of such an entity.  Examples include
tables, columns, sequences, and indexes.

All entities are subclasses of :class:`~sqlalchemy.schema.SchemaItem`, and as
defined in this module they are intended to be agnostic of any vendor-specific
constructs.

A collection of entities are grouped into a unit called
:class:`~sqlalchemy.schema.MetaData`. MetaData serves as a logical grouping of
schema elements, and can also be associated with an actual database connection
such that operations involving the contained elements can contact the database
as needed.

Two of the elements here also build upon their "syntactic" counterparts, which
are defined in :class:`~sqlalchemy.sql.expression.`, specifically
:class:`~sqlalchemy.schema.Table` and :class:`~sqlalchemy.schema.Column`.
Since these objects are part of the SQL expression language, they are usable
as components in SQL expressions.

'''
from __future__ import annotations
from abc import ABC
import collections
from enum import Enum
import operator
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence as _typing_Sequence
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import coercions
from  import ddl
from  import roles
from  import type_api
from  import visitors
from base import _DefaultDescriptionTuple
from base import _NoArg
from base import _NoneName
from base import _SentinelColumnCharacterization
from base import _SentinelDefaultCharacterization
from base import DedupeColumnCollection
from base import DialectKWArgs
from base import Executable
from base import SchemaEventTarget
from base import SchemaVisitable
from coercions import _document_text_coercion
from elements import ClauseElement
from elements import ColumnClause
from elements import ColumnElement
from elements import quoted_name
from elements import TextClause
from selectable import TableClause
from type_api import to_instance
from visitors import ExternallyTraversible
from  import event
from  import exc
from  import inspection
from  import util
from util import HasMemoized
from util.typing import Final
from util.typing import Literal
from util.typing import Protocol
from util.typing import Self
from util.typing import TypedDict
from util.typing import TypeGuard
if typing.TYPE_CHECKING:
    from _typing import _AutoIncrementType
    from _typing import _CreateDropBind
    from _typing import _DDLColumnArgument
    from _typing import _InfoType
    from _typing import _TextCoercedExpressionArgument
    from _typing import _TypeEngineArgument
    from base import ColumnSet
    from base import ReadOnlyColumnCollection
    from compiler import DDLCompiler
    from elements import BindParameter
    from elements import KeyedColumnElement
    from functions import Function
    from type_api import TypeEngine
    from visitors import anon_map
    from engine import Connection
    from engine import Engine
    from engine.interfaces import _CoreMultiExecuteParams
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.interfaces import ExecutionContext
    from engine.reflection import _ReflectionInfo
    from sql.selectable import FromClause
_T = TypeVar('_T', bound = 'Any')
_SI = TypeVar('_SI', bound = 'SchemaItem')
_TAB = TypeVar('_TAB', bound = 'Table')
_ConstraintNameArgument = Optional[Union[(str, _NoneName)]]
_ServerDefaultArgument = Union[('FetchedValue', str, TextClause, ColumnElement[Any])]
_ServerOnUpdateArgument = _ServerDefaultArgument

class SchemaConst(Enum):
    RETAIN_SCHEMA = 1
    BLANK_SCHEMA = 2
    NULL_UNSPECIFIED = 3

RETAIN_SCHEMA: 'Final[Literal[SchemaConst.RETAIN_SCHEMA]]' = SchemaConst.RETAIN_SCHEMA
BLANK_SCHEMA: 'Final[Literal[SchemaConst.BLANK_SCHEMA]]' = SchemaConst.BLANK_SCHEMA
NULL_UNSPECIFIED: 'Final[Literal[SchemaConst.NULL_UNSPECIFIED]]' = SchemaConst.NULL_UNSPECIFIED

def _get_table_key(name = None, schema = None):
    pass
# WARNING: Decompyle incomplete


def _copy_expression(expression = None, source_table = None, target_table = None):
    pass
# WARNING: Decompyle incomplete

SchemaItem = <NODE:12>()

class HasConditionalDDL:
    '''define a class that includes the :meth:`.HasConditionalDDL.ddl_if`
    method, allowing for conditional rendering of DDL.

    Currently applies to constraints and indexes.

    .. versionadded:: 2.0


    '''
    _ddl_if: 'Optional[ddl.DDLIf]' = None
    
    def ddl_if(self = None, dialect = None, callable_ = None, state = (None, None, None)):
        '''apply a conditional DDL rule to this schema item.

        These rules work in a similar manner to the
        :meth:`.ExecutableDDLElement.execute_if` callable, with the added
        feature that the criteria may be checked within the DDL compilation
        phase for a construct such as :class:`.CreateTable`.
        :meth:`.HasConditionalDDL.ddl_if` currently applies towards the
        :class:`.Index` construct as well as all :class:`.Constraint`
        constructs.

        :param dialect: string name of a dialect, or a tuple of string names
         to indicate multiple dialect types.

        :param callable\\_: a callable that is constructed using the same form
         as that described in
         :paramref:`.ExecutableDDLElement.execute_if.callable_`.

        :param state: any arbitrary object that will be passed to the
         callable, if present.

        .. versionadded:: 2.0

        .. seealso::

            :ref:`schema_ddl_ddl_if` - background and usage examples


        '''
        self._ddl_if = ddl.DDLIf(dialect, callable_, state)
        return self



class HasSchemaAttr(SchemaItem):
    schema: 'Optional[str]' = 'schema item that includes a top-level schema name'


def Table():
    '''Table'''
    pass
# WARNING: Decompyle incomplete

Table = <NODE:27>(Table, 'Table', DialectKWArgs, HasSchemaAttr, TableClause, inspection.Inspectable['Table'])

def Column():
    '''Column'''
    pass
# WARNING: Decompyle incomplete

Column = <NODE:27>(Column, 'Column', DialectKWArgs, SchemaItem, ColumnClause[_T])

def insert_sentinel(name = None, type_ = inspection._self_inspects, *, default, omit_from_statements):
    '''Provides a surrogate :class:`_schema.Column` that will act as a
    dedicated insert :term:`sentinel` column, allowing efficient bulk
    inserts with deterministic RETURNING sorting for tables that
    don\'t otherwise have qualifying primary key configurations.

    Adding this column to a :class:`.Table` object requires that a
    corresponding database table actually has this column present, so if adding
    it to an existing model, existing database tables would need to be migrated
    (e.g. using ALTER TABLE or similar) to include this column.

    For background on how this object is used, see the section
    :ref:`engine_insertmanyvalues_sentinel_columns` as part of the
    section :ref:`engine_insertmanyvalues`.

    The :class:`_schema.Column` returned will be a nullable integer column by
    default and make use of a sentinel-specific default generator used only in
    "insertmanyvalues" operations.

    .. seealso::

        :func:`_orm.orm_insert_sentinel`

        :paramref:`_schema.Column.insert_sentinel`

        :ref:`engine_insertmanyvalues`

        :ref:`engine_insertmanyvalues_sentinel_columns`


    .. versionadded:: 2.0.10

    '''
    pass
# WARNING: Decompyle incomplete


class ForeignKey(SchemaItem, DialectKWArgs):
    '''Defines a dependency between two columns.

    ``ForeignKey`` is specified as an argument to a :class:`_schema.Column`
    object,
    e.g.::

        t = Table(
            "remote_table",
            metadata,
            Column("remote_id", ForeignKey("main_table.id")),
        )

    Note that ``ForeignKey`` is only a marker object that defines
    a dependency between two columns.   The actual constraint
    is in all cases represented by the :class:`_schema.ForeignKeyConstraint`
    object.   This object will be generated automatically when
    a ``ForeignKey`` is associated with a :class:`_schema.Column` which
    in turn is associated with a :class:`_schema.Table`.   Conversely,
    when :class:`_schema.ForeignKeyConstraint` is applied to a
    :class:`_schema.Table`,
    ``ForeignKey`` markers are automatically generated to be
    present on each associated :class:`_schema.Column`, which are also
    associated with the constraint object.

    Note that you cannot define a "composite" foreign key constraint,
    that is a constraint between a grouping of multiple parent/child
    columns, using ``ForeignKey`` objects.   To define this grouping,
    the :class:`_schema.ForeignKeyConstraint` object must be used, and applied
    to the :class:`_schema.Table`.   The associated ``ForeignKey`` objects
    are created automatically.

    The ``ForeignKey`` objects associated with an individual
    :class:`_schema.Column`
    object are available in the `foreign_keys` collection
    of that column.

    Further examples of foreign key configuration are in
    :ref:`metadata_foreignkeys`.

    '''
    _table_column: 'Optional[Column[Any]]' = 'foreign_key'
    
    def __init__(self, column, _constraint, use_alter, name, onupdate, ondelete, deferrable, initially, link_to_name = None, match = None, info = None, comment = (None, False, None, None, None, None, None, False, None, None, None, False), _unresolvable = ('column', '_DDLColumnArgument', '_constraint', 'Optional[ForeignKeyConstraint]', 'use_alter', 'bool', 'name', '_ConstraintNameArgument', 'onupdate', 'Optional[str]', 'ondelete', 'Optional[str]', 'deferrable', 'Optional[bool]', 'initially', 'Optional[str]', 'link_to_name', 'bool', 'match', 'Optional[str]', 'info', 'Optional[_InfoType]', 'comment', 'Optional[str]', '_unresolvable', 'bool', 'dialect_kw', 'Any'), **dialect_kw):
        """
        Construct a column-level FOREIGN KEY.

        The :class:`_schema.ForeignKey` object when constructed generates a
        :class:`_schema.ForeignKeyConstraint`
        which is associated with the parent
        :class:`_schema.Table` object's collection of constraints.

        :param column: A single target column for the key relationship. A
            :class:`_schema.Column` object or a column name as a string:
            ``tablename.columnkey`` or ``schema.tablename.columnkey``.
            ``columnkey`` is the ``key`` which has been assigned to the column
            (defaults to the column name itself), unless ``link_to_name`` is
            ``True`` in which case the rendered name of the column is used.

        :param name: Optional string. An in-database name for the key if
            `constraint` is not provided.

        :param onupdate: Optional string. If set, emit ON UPDATE <value> when
            issuing DDL for this constraint. Typical values include CASCADE,
            DELETE and RESTRICT.

            .. seealso::

                :ref:`on_update_on_delete`

        :param ondelete: Optional string. If set, emit ON DELETE <value> when
            issuing DDL for this constraint. Typical values include CASCADE,
            SET NULL and RESTRICT.  Some dialects may allow for additional
            syntaxes.

            .. seealso::

                :ref:`on_update_on_delete`

        :param deferrable: Optional bool. If set, emit DEFERRABLE or NOT
            DEFERRABLE when issuing DDL for this constraint.

        :param initially: Optional string. If set, emit INITIALLY <value> when
            issuing DDL for this constraint.

        :param link_to_name: if True, the string name given in ``column`` is
            the rendered name of the referenced column, not its locally
            assigned ``key``.

        :param use_alter: passed to the underlying
            :class:`_schema.ForeignKeyConstraint`
            to indicate the constraint should
            be generated/dropped externally from the CREATE TABLE/ DROP TABLE
            statement.  See :paramref:`_schema.ForeignKeyConstraint.use_alter`
            for further description.

            .. seealso::

                :paramref:`_schema.ForeignKeyConstraint.use_alter`

                :ref:`use_alter`

        :param match: Optional string. If set, emit MATCH <value> when issuing
            DDL for this constraint. Typical values include SIMPLE, PARTIAL
            and FULL.

        :param info: Optional data dictionary which will be populated into the
            :attr:`.SchemaItem.info` attribute of this object.

        :param comment: Optional string that will render an SQL comment on
          foreign key constraint creation.

            .. versionadded:: 2.0

        :param \\**dialect_kw:  Additional keyword arguments are dialect
            specific, and passed in the form ``<dialectname>_<argname>``.  The
            arguments are ultimately handled by a corresponding
            :class:`_schema.ForeignKeyConstraint`.
            See the documentation regarding
            an individual dialect at :ref:`dialect_toplevel` for detail on
            documented arguments.

        """
        self._colspec = coercions.expect(roles.DDLReferredColumnRole, column)
        self._unresolvable = _unresolvable
        if isinstance(self._colspec, str):
            self._table_column = None
        else:
            self._table_column = self._colspec
            if not isinstance(self._table_column.table, (type(None), TableClause)):
                raise exc.ArgumentError('ForeignKey received Column not bound to a Table, got: %r' % self._table_column.table)
        self.constraint = _constraint
        self.parent = None
        self.use_alter = use_alter
        self.name = name
        self.onupdate = onupdate
        self.ondelete = ondelete
        self.deferrable = deferrable
        self.initially = initially
        self.link_to_name = link_to_name
        self.match = match
        self.comment = comment
        if info:
            self.info = info
        self._unvalidated_dialect_kw = dialect_kw

    
    def __repr__(self = None):
        return 'ForeignKey(%r)' % self._get_colspec()

    copy = (lambda self = None, *, schema: pass# WARNING: Decompyle incomplete
)()
    
    def _copy(self = None, *, schema, **kw):
        '''Produce a copy of this :class:`_schema.ForeignKey` object.

        The new :class:`_schema.ForeignKey` will not be bound
        to any :class:`_schema.Column`.

        This method is usually used by the internal
        copy procedures of :class:`_schema.Column`, :class:`_schema.Table`,
        and :class:`_schema.MetaData`.

        :param schema: The returned :class:`_schema.ForeignKey` will
          reference the original table and column name, qualified
          by the given string schema name.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_colspec(self = None, schema = None, table_name = None, _is_copy = (None, None, False)):
        '''Return a string based \'column specification\' for this
        :class:`_schema.ForeignKey`.

        This is usually the equivalent of the string-based "tablename.colname"
        argument first passed to the object\'s constructor.

        '''
        pass
    # WARNING: Decompyle incomplete

    _referred_schema = (lambda self = None: self._column_tokens[0])()
    
    def _table_key(self = None):
        pass
    # WARNING: Decompyle incomplete

    target_fullname = property(_get_colspec)
    
    def references(self = None, table = None):
        '''Return True if the given :class:`_schema.Table`
        is referenced by this
        :class:`_schema.ForeignKey`.'''
        return table.corresponding_column(self.column) is not None

    
    def get_referent(self = None, table = None):
        '''Return the :class:`_schema.Column` in the given
        :class:`_schema.Table` (or any :class:`.FromClause`)
        referenced by this :class:`_schema.ForeignKey`.

        Returns None if this :class:`_schema.ForeignKey`
        does not reference the given
        :class:`_schema.Table`.

        '''
        return table.columns.corresponding_column(self.column)

    _column_tokens = (lambda self = None: m = self._get_colspec().split('.')# WARNING: Decompyle incomplete
)()
    
    def _resolve_col_tokens(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _link_to_col_by_colstring(self = None, parenttable = None, table = None, colname = ('parenttable', 'Table', 'table', 'Table', 'colname', 'Optional[str]', 'return', 'Column[Any]')):
        _column = None
    # WARNING: Decompyle incomplete

    
    def _set_target_column(self = None, column = None):
        pass
    # WARNING: Decompyle incomplete

    column = (lambda self = None: self._resolve_column())()
    _resolve_column = (lambda self = None, *, raiseerr: pass)()
    _resolve_column = (lambda self = None, *, raiseerr: pass)()
    
    def _resolve_column(self = None, *, raiseerr):
        if isinstance(self._colspec, str):
            (parenttable, tablekey, colname) = self._resolve_col_tokens()
            if self._unresolvable or tablekey not in parenttable.metadata:
                if not raiseerr:
                    return None
                raise None.NoReferencedTableError(f'''Foreign key associated with column \'{self.parent}\' could not find table \'{tablekey}\' with which to generate a foreign key to target column \'{colname}\'''', tablekey)
            if parenttable.key not in parenttable.metadata:
                if not raiseerr:
                    return None
                raise None.InvalidRequestError(f'''Table {parenttable} is no longer associated with its parent MetaData''')
            table = parenttable.metadata.tables[tablekey]
            return self._link_to_col_by_colstring(parenttable, table, colname)
        if None(self._colspec, '__clause_element__'):
            _column = self._colspec.__clause_element__()
            return _column
        _column = None._colspec
        return _column

    
    def _set_parent(self = None, parent = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _set_remote_table(self = None, table = None):
        (parenttable, _, colname) = self._resolve_col_tokens()
        _column = self._link_to_col_by_colstring(parenttable, table, colname)
        self._set_target_column(_column)
    # WARNING: Decompyle incomplete

    
    def _remove_from_metadata(self = None, metadata = None):
        (parenttable, table_key, colname) = self._resolve_col_tokens()
        fk_key = (table_key, colname)
        if self in metadata._fk_memos[fk_key]:
            metadata._fk_memos[fk_key].remove(self)
            return None

    
    def _set_table(self = None, column = None, table = None):
        pass
    # WARNING: Decompyle incomplete



class DefaultGenerator(SchemaItem, Executable):
    """Base class for column *default* values.

    This object is only present on column.default or column.onupdate.
    It's not valid as a server default.

    """
    __visit_name__ = 'default_generator'
    _is_default_generator = True
    is_sequence = False
    is_identity = False
    is_server_default = False
    is_clause_element = False
    is_callable = False
    is_scalar = False
    has_arg = False
    column: 'Optional[Column[Any]]' = False
    
    def __init__(self = None, for_update = None):
        self.for_update = for_update

    
    def _set_parent(self = None, parent = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _copy(self = None):
        raise NotImplementedError()

    
    def _execute_on_connection(self = None, connection = None, distilled_params = None, execution_options = ('connection', 'Connection', 'distilled_params', '_CoreMultiExecuteParams', 'execution_options', 'CoreExecuteOptionsParameter', 'return', 'Any')):
        util.warn_deprecated('Using the .execute() method to invoke a DefaultGenerator object is deprecated; please use the .scalar() method.', '2.0')
        return self._execute_on_scalar(connection, distilled_params, execution_options)

    
    def _execute_on_scalar(self = None, connection = None, distilled_params = None, execution_options = ('connection', 'Connection', 'distilled_params', '_CoreMultiExecuteParams', 'execution_options', 'CoreExecuteOptionsParameter', 'return', 'Any')):
        return connection._execute_default(self, distilled_params, execution_options)



class ColumnDefault(ABC, DefaultGenerator):
    arg: 'Any' = 'A plain default value on a column.\n\n    This could correspond to a constant, a callable function,\n    or a SQL clause.\n\n    :class:`.ColumnDefault` is generated automatically\n    whenever the ``default``, ``onupdate`` arguments of\n    :class:`_schema.Column` are used.  A :class:`.ColumnDefault`\n    can be passed positionally as well.\n\n    For example, the following::\n\n        Column("foo", Integer, default=50)\n\n    Is equivalent to::\n\n        Column("foo", Integer, ColumnDefault(50))\n\n    '
    __new__ = (lambda cls = None, arg = None, for_update = overload: pass)()
    __new__ = (lambda cls = None, arg = None, for_update = overload: pass)()
    __new__ = (lambda cls = None, arg = None, for_update = overload: pass)()
    
    def __new__(cls = None, arg = None, for_update = None):
        '''Construct a new :class:`.ColumnDefault`.


        :param arg: argument representing the default value.
         May be one of the following:

         * a plain non-callable Python value, such as a
           string, integer, boolean, or other simple type.
           The default value will be used as is each time.
         * a SQL expression, that is one which derives from
           :class:`_expression.ColumnElement`.  The SQL expression will
           be rendered into the INSERT or UPDATE statement,
           or in the case of a primary key column when
           RETURNING is not used may be
           pre-executed before an INSERT within a SELECT.
         * A Python callable.  The function will be invoked for each
           new row subject to an INSERT or UPDATE.
           The callable must accept exactly
           zero or one positional arguments.  The one-argument form
           will receive an instance of the :class:`.ExecutionContext`,
           which provides contextual information as to the current
           :class:`_engine.Connection` in use as well as the current
           statement and parameters.

        '''
        if isinstance(arg, FetchedValue):
            raise exc.ArgumentError('ColumnDefault may not be a server-side default type.')
        if callable(arg):
            cls = CallableColumnDefault
        elif isinstance(arg, ClauseElement):
            cls = ColumnElementColumnDefault
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}({self.arg!r})'''



class ScalarElementColumnDefault(ColumnDefault):
    '''default generator for a fixed scalar Python value

    .. versionadded: 2.0

    '''
    is_scalar = True
    has_arg = True
    
    def __init__(self = None, arg = None, for_update = None):
        self.for_update = for_update
        self.arg = arg

    
    def _copy(self = None):
        return ScalarElementColumnDefault(arg = self.arg, for_update = self.for_update)



class _InsertSentinelColumnDefault(ColumnDefault):
    pass
# WARNING: Decompyle incomplete

_SQLExprDefault = Union[('ColumnElement[Any]', 'TextClause')]

class ColumnElementColumnDefault(ColumnDefault):
    '''default generator for a SQL expression

    .. versionadded:: 2.0

    '''
    is_clause_element = True
    arg: '_SQLExprDefault' = True
    
    def __init__(self = None, arg = None, for_update = None):
        self.for_update = for_update
        self.arg = arg

    
    def _copy(self = None):
        return ColumnElementColumnDefault(arg = self.arg, for_update = self.for_update)

    _arg_is_typed = (lambda self = None: sqltypes = util.preloaded.sql_sqltypesnot isinstance(self.arg.type, sqltypes.NullType))()()


class _CallableColumnDefaultProtocol(Protocol):
    
    def __call__(self = None, context = None):
        pass



class CallableColumnDefault(ColumnDefault):
    '''default generator for a callable Python function

    .. versionadded:: 2.0

    '''
    arg: '_CallableColumnDefaultProtocol' = True
    has_arg = True
    
    def __init__(self = None, arg = None, for_update = None):
        self.for_update = for_update
        self.arg = self._maybe_wrap_callable(arg)

    
    def _copy(self = None):
        return CallableColumnDefault(arg = self.arg, for_update = self.for_update)

    
    def _maybe_wrap_callable(self = None, fn = None):
        """Wrap callables that don't accept a context.

        This is to allow easy compatibility with default callables
        that aren't specific to accepting of a context.

        """
        pass
    # WARNING: Decompyle incomplete



class IdentityOptions:
    '''Defines options for a named database sequence or an identity column.

    .. versionadded:: 1.3.18

    .. seealso::

        :class:`.Sequence`

    '''
    
    def __init__(self, start, increment, minvalue, maxvalue, nominvalue = None, nomaxvalue = None, cycle = None, cache = (None, None, None, None, None, None, None, None, None), order = ('start', 'Optional[int]', 'increment', 'Optional[int]', 'minvalue', 'Optional[int]', 'maxvalue', 'Optional[int]', 'nominvalue', 'Optional[bool]', 'nomaxvalue', 'Optional[bool]', 'cycle', 'Optional[bool]', 'cache', 'Optional[int]', 'order', 'Optional[bool]', 'return', 'None')):
        '''Construct a :class:`.IdentityOptions` object.

        See the :class:`.Sequence` documentation for a complete description
        of the parameters.

        :param start: the starting index of the sequence.
        :param increment: the increment value of the sequence.
        :param minvalue: the minimum value of the sequence.
        :param maxvalue: the maximum value of the sequence.
        :param nominvalue: no minimum value of the sequence.
        :param nomaxvalue: no maximum value of the sequence.
        :param cycle: allows the sequence to wrap around when the maxvalue
         or minvalue has been reached.
        :param cache: optional integer value; number of future values in the
         sequence which are calculated in advance.
        :param order: optional boolean value; if ``True``, renders the
         ORDER keyword.

        '''
        self.start = start
        self.increment = increment
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.nominvalue = nominvalue
        self.nomaxvalue = nomaxvalue
        self.cycle = cycle
        self.cache = cache
        self.order = order

    _increment_is_negative = (lambda self = None: if self.increment is not None:
passself.increment < 0)()


class Sequence(DefaultGenerator, IdentityOptions, HasSchemaAttr):
    pass
# WARNING: Decompyle incomplete

FetchedValue = <NODE:12>()

class DefaultClause(FetchedValue):
    pass
# WARNING: Decompyle incomplete


class Constraint(SchemaItem, HasConditionalDDL, DialectKWArgs):
    '''A table-level SQL constraint.

    :class:`_schema.Constraint` serves as the base class for the series of
    constraint objects that can be associated with :class:`_schema.Table`
    objects, including :class:`_schema.PrimaryKeyConstraint`,
    :class:`_schema.ForeignKeyConstraint`
    :class:`_schema.UniqueConstraint`, and
    :class:`_schema.CheckConstraint`.

    '''
    _column_flag: 'bool' = 'constraint'
    
    def __init__(self, name, deferrable, initially = None, info = None, comment = None, _create_rule = (None, None, None, None, None, None, False), _type_bound = ('name', '_ConstraintNameArgument', 'deferrable', 'Optional[bool]', 'initially', 'Optional[str]', 'info', 'Optional[_InfoType]', 'comment', 'Optional[str]', '_create_rule', 'Optional[Any]', '_type_bound', 'bool', 'dialect_kw', 'Any', 'return', 'None'), **dialect_kw):
        '''Create a SQL constraint.

        :param name:
          Optional, the in-database name of this ``Constraint``.

        :param deferrable:
          Optional bool.  If set, emit DEFERRABLE or NOT DEFERRABLE when
          issuing DDL for this constraint.

        :param initially:
          Optional string.  If set, emit INITIALLY <value> when issuing DDL
          for this constraint.

        :param info: Optional data dictionary which will be populated into the
            :attr:`.SchemaItem.info` attribute of this object.

        :param comment: Optional string that will render an SQL comment on
          foreign key constraint creation.

            .. versionadded:: 2.0

        :param \\**dialect_kw:  Additional keyword arguments are dialect
            specific, and passed in the form ``<dialectname>_<argname>``.  See
            the documentation regarding an individual dialect at
            :ref:`dialect_toplevel` for detail on documented arguments.

        :param _create_rule:
          used internally by some datatypes that also create constraints.

        :param _type_bound:
          used internally to indicate that this constraint is associated with
          a specific datatype.

        '''
        self.name = name
        self.deferrable = deferrable
        self.initially = initially
        if info:
            self.info = info
        self._create_rule = _create_rule
        self._type_bound = _type_bound
        util.set_creation_order(self)
        self._validate_dialect_kwargs(dialect_kw)
        self.comment = comment

    
    def _should_create_for_compiler(self = None, compiler = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    table = (lambda self = None: try:
if isinstance(self.parent, Table):
self.parentexcept AttributeError:
passraise exc.InvalidRequestError('This constraint is not bound to a table.  Did you mean to call table.append_constraint(constraint) ?'))()
    
    def _set_parent(self = None, parent = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    copy = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _copy(self = None, **kw):
        raise NotImplementedError()



class ColumnCollectionMixin:
    _columns: 'DedupeColumnCollection[Column[Any]]' = 'A :class:`_expression.ColumnCollection` of :class:`_schema.Column`\n    objects.\n\n    This collection represents the columns which are referred to by\n    this object.\n\n    '
    _pending_colargs: 'List[Optional[Union[str, Column[Any]]]]' = False
    if TYPE_CHECKING:
        
        def _set_parent_with_dispatch(self = None, parent = None, **kw):
            pass

    
    def __init__(self = None, *, _autoattach, _column_flag, _gather_expressions, *columns):
        self._column_flag = _column_flag
        self._columns = DedupeColumnCollection()
        processed_expressions = _gather_expressions
    # WARNING: Decompyle incomplete

    
    def _check_attach(self = None, evt = None):
        pass
    # WARNING: Decompyle incomplete

    columns = (lambda self = None: self._columns.as_readonly())()
    c = (lambda self = None: self._columns.as_readonly())()
    
    def _col_expressions(self = None, parent = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _set_parent(self = None, parent = None, **kw):
        pass
    # WARNING: Decompyle incomplete



class ColumnCollectionConstraint(Constraint, ColumnCollectionMixin):
    '''A constraint that proxies a ColumnCollection.'''
    
    def columns: 'ReadOnlyColumnCollection[str, Column[Any]]'(self = None, *, name, deferrable, initially, info, _autoattach, _column_flag, _gather_expressions, *columns, **dialect_kw):
        '''
        :param \\*columns:
          A sequence of column names or Column objects.

        :param name:
          Optional, the in-database name of this constraint.

        :param deferrable:
          Optional bool.  If set, emit DEFERRABLE or NOT DEFERRABLE when
          issuing DDL for this constraint.

        :param initially:
          Optional string.  If set, emit INITIALLY <value> when issuing DDL
          for this constraint.

        :param \\**dialect_kw: other keyword arguments including
          dialect-specific arguments are propagated to the :class:`.Constraint`
          superclass.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _set_parent(self = None, parent = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, x = None):
        return x in self._columns

    copy = (lambda self = None, *, target_table: pass# WARNING: Decompyle incomplete
)()
    
    def _copy(self = None, *, target_table, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def contains_column(self = None, col = None):
        '''Return True if this constraint contains the given column.

        Note that this object also contains an attribute ``.columns``
        which is a :class:`_expression.ColumnCollection` of
        :class:`_schema.Column` objects.

        '''
        return self._columns.contains_column(col)

    
    def __iter__(self = None):
        return iter(self._columns)

    
    def __len__(self = None):
        return len(self._columns)



class CheckConstraint(ColumnCollectionConstraint):
    pass
# WARNING: Decompyle incomplete


class ForeignKeyConstraint(ColumnCollectionConstraint):
    '''A table-level FOREIGN KEY constraint.

    Defines a single column or composite FOREIGN KEY ... REFERENCES
    constraint. For a no-frills, single column foreign key, adding a
    :class:`_schema.ForeignKey` to the definition of a :class:`_schema.Column`
    is a
    shorthand equivalent for an unnamed, single column
    :class:`_schema.ForeignKeyConstraint`.

    Examples of foreign key configuration are in :ref:`metadata_foreignkeys`.

    '''
    __visit_name__ = 'foreign_key_constraint'
    
    def __init__(self, columns, refcolumns, name, onupdate, ondelete, deferrable, initially, use_alter, link_to_name = None, match = None, table = None, info = (None, None, None, None, None, False, False, None, None, None, None), comment = ('columns', '_typing_Sequence[_DDLColumnArgument]', 'refcolumns', '_typing_Sequence[_DDLColumnArgument]', 'name', '_ConstraintNameArgument', 'onupdate', 'Optional[str]', 'ondelete', 'Optional[str]', 'deferrable', 'Optional[bool]', 'initially', 'Optional[str]', 'use_alter', 'bool', 'link_to_name', 'bool', 'match', 'Optional[str]', 'table', 'Optional[Table]', 'info', 'Optional[_InfoType]', 'comment', 'Optional[str]', 'dialect_kw', 'Any', 'return', 'None'), **dialect_kw):
        '''Construct a composite-capable FOREIGN KEY.

        :param columns: A sequence of local column names. The named columns
          must be defined and present in the parent Table. The names should
          match the ``key`` given to each column (defaults to the name) unless
          ``link_to_name`` is True.

        :param refcolumns: A sequence of foreign column names or Column
          objects. The columns must all be located within the same Table.

        :param name: Optional, the in-database name of the key.

        :param onupdate: Optional string. If set, emit ON UPDATE <value> when
            issuing DDL for this constraint. Typical values include CASCADE,
            DELETE and RESTRICT.

            .. seealso::

                :ref:`on_update_on_delete`

        :param ondelete: Optional string. If set, emit ON DELETE <value> when
            issuing DDL for this constraint. Typical values include CASCADE,
            SET NULL and RESTRICT.  Some dialects may allow for additional
            syntaxes.

            .. seealso::

                :ref:`on_update_on_delete`

        :param deferrable: Optional bool. If set, emit DEFERRABLE or NOT
          DEFERRABLE when issuing DDL for this constraint.

        :param initially: Optional string. If set, emit INITIALLY <value> when
          issuing DDL for this constraint.

        :param link_to_name: if True, the string name given in ``column`` is
          the rendered name of the referenced column, not its locally assigned
          ``key``.

        :param use_alter: If True, do not emit the DDL for this constraint as
          part of the CREATE TABLE definition. Instead, generate it via an
          ALTER TABLE statement issued after the full collection of tables
          have been created, and drop it via an ALTER TABLE statement before
          the full collection of tables are dropped.

          The use of :paramref:`_schema.ForeignKeyConstraint.use_alter` is
          particularly geared towards the case where two or more tables
          are established within a mutually-dependent foreign key constraint
          relationship; however, the :meth:`_schema.MetaData.create_all` and
          :meth:`_schema.MetaData.drop_all`
          methods will perform this resolution
          automatically, so the flag is normally not needed.

          .. seealso::

                :ref:`use_alter`

        :param match: Optional string. If set, emit MATCH <value> when issuing
          DDL for this constraint. Typical values include SIMPLE, PARTIAL
          and FULL.

        :param info: Optional data dictionary which will be populated into the
            :attr:`.SchemaItem.info` attribute of this object.

        :param comment: Optional string that will render an SQL comment on
          foreign key constraint creation.

            .. versionadded:: 2.0

        :param \\**dialect_kw:  Additional keyword arguments are dialect
          specific, and passed in the form ``<dialectname>_<argname>``.  See
          the documentation regarding an individual dialect at
          :ref:`dialect_toplevel` for detail on documented arguments.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def elements: 'List[ForeignKey]'(self = None, column = None, fk = None):
        self._columns.add(column)
        self.elements.append(fk)

    _elements = (lambda self = None: util.OrderedDict(zip(self.column_keys, self.elements)))()
    _referred_schema = (lambda self = None: for elem in self.elements:
None, elem._referred_schemaNone)()
    referred_table = (lambda self = None: self.elements[0].column.table)()
    
    def _validate_dest_table(self = None, table = None):
        table_keys = self.elements()
        if None not in table_keys or len(table_keys) > 1:
            (elem0, elem1) = sorted(table_keys)[0:2]
            raise exc.ArgumentError(f'''ForeignKeyConstraint on {table.fullname}({self._col_description}) refers to multiple remote tables: {elem0} and {elem1}''')
        return None

    column_keys = (lambda self = None:
