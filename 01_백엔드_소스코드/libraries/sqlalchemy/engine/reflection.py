# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reflection.pyc (Python 3.11)

"""Provides an abstraction for obtaining database schema information.

Usage Notes:

Here are some general conventions when accessing the low level inspector
methods such as get_table_names, get_columns, etc.

1. Inspector methods return lists of dicts in most cases for the following
   reasons:

   * They're both standard types that can be serialized.
   * Using a dict instead of a tuple allows easy expansion of attributes.
   * Using a list for the outer structure maintains order and is easy to work
     with (e.g. list comprehension [d['name'] for d in cols]).

2. Records that contain a name, such as the column name in a column record
   use the key 'name'. So for most return values, each record will have a
   'name' attribute..
"""
from __future__ import annotations
import contextlib
from dataclasses import dataclass
from enum import auto
from enum import Flag
from enum import unique
from typing import Any
from typing import Callable
from typing import Collection
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from base import Connection
from base import Engine
from  import exc
from  import inspection
from  import sql
from  import util
from sql import operators
from sql import schema as sa_schema
from sql.cache_key import _ad_hoc_cache_key_from_args
from sql.elements import quoted_name
from sql.elements import TextClause
from sql.type_api import TypeEngine
from sql.visitors import InternalTraversal
from util import topological
from util.typing import final
if TYPE_CHECKING:
    from interfaces import Dialect
    from interfaces import ReflectedCheckConstraint
    from interfaces import ReflectedColumn
    from interfaces import ReflectedForeignKeyConstraint
    from interfaces import ReflectedIndex
    from interfaces import ReflectedPrimaryKeyConstraint
    from interfaces import ReflectedTableComment
    from interfaces import ReflectedUniqueConstraint
    from interfaces import TableKey
_R = TypeVar('_R')
cache = (lambda fn = None, self = None, con = util.decorator: pass# WARNING: Decompyle incomplete
)()

def flexi_cache(*traverse_args):
    pass
# WARNING: Decompyle incomplete

ObjectKind = <NODE:12>()
ObjectScope = <NODE:12>()

def Inspector():
    '''Inspector'''
    info_cache: 'Dict[Any, Any]' = 'Performs database schema inspection.\n\n    The Inspector acts as a proxy to the reflection methods of the\n    :class:`~sqlalchemy.engine.interfaces.Dialect`, providing a\n    consistent interface as well as caching support for previously\n    fetched metadata.\n\n    A :class:`_reflection.Inspector` object is usually created via the\n    :func:`_sa.inspect` function, which may be passed an\n    :class:`_engine.Engine`\n    or a :class:`_engine.Connection`::\n\n        from sqlalchemy import inspect, create_engine\n\n        engine = create_engine("...")\n        insp = inspect(engine)\n\n    Where above, the :class:`~sqlalchemy.engine.interfaces.Dialect` associated\n    with the engine may opt to return an :class:`_reflection.Inspector`\n    subclass that\n    provides additional methods specific to the dialect\'s target database.\n\n    '
    __init__ = (lambda self = None, bind = None: self._init_legacy(bind))()
    _construct = (lambda cls = None, init = None, bind = classmethod: if hasattr(bind.dialect, 'inspector'):
cls = bind.dialect.inspectorself = cls.__new__(cls)init(self, bind)self)()
    
    def _init_legacy(self = None, bind = None):
        if hasattr(bind, 'exec_driver_sql'):
            self._init_connection(bind)
            return None
        None._init_engine(bind)

    
    def _init_engine(self = None, engine = None):
        self.bind = engine
        self.engine = engine
        engine.connect().close()
        self._op_context_requires_connect = True
        self.dialect = self.engine.dialect
        self.info_cache = { }

    
    def _init_connection(self = None, connection = None):
        self.bind = connection
        self.engine = connection.engine
        self._op_context_requires_connect = False
        self.dialect = self.engine.dialect
        self.info_cache = { }

    
    def clear_cache(self = None):
        '''reset the cache for this :class:`.Inspector`.

        Inspection methods that have data cached will emit SQL queries
        when next called to get new data.

        .. versionadded:: 2.0

        '''
        self.info_cache.clear()

    from_engine = (lambda cls = None, bind = classmethod: cls._construct(cls._init_legacy, bind))()()
    _engine_insp = (lambda bind = None: Inspector._construct(Inspector._init_engine, bind))()
    _connection_insp = (lambda bind = None: Inspector._construct(Inspector._init_connection, bind))()
    _operation_context = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _inspection_context = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    default_schema_name = (lambda self = None: self.dialect.default_schema_name)()
    
    def get_schema_names(self = None, **kw):
        '''Return all schema names.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_table_names(self = None, schema = None, **kw):
        """Return all table names within a particular schema.

        The names are expected to be real tables only, not views.
        Views are instead returned using the
        :meth:`_reflection.Inspector.get_view_names` and/or
        :meth:`_reflection.Inspector.get_materialized_view_names`
        methods.

        :param schema: Schema name. If ``schema`` is left at ``None``, the
         database's default schema is
         used, else the named schema is searched.  If the database does not
         support named schemas, behavior is undefined if ``schema`` is not
         passed as ``None``.  For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. seealso::

            :meth:`_reflection.Inspector.get_sorted_table_and_fkc_names`

            :attr:`_schema.MetaData.sorted_tables`

        """
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def has_table(self = None, table_name = None, schema = None, **kw):
        '''Return True if the backend has a table, view, or temporary
        table of the given name.

        :param table_name: name of the table to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 1.4 - the :meth:`.Inspector.has_table` method
           replaces the :meth:`_engine.Engine.has_table` method.

        .. versionchanged:: 2.0:: :meth:`.Inspector.has_table` now formally
           supports checking for additional table-like objects:

           * any type of views (plain or materialized)
           * temporary tables of any kind

           Previously, these two checks were not formally specified and
           different dialects would vary in their behavior.   The dialect
           testing suite now includes tests for all of these object types
           and should be supported by all SQLAlchemy-included dialects.
           Support among third party dialects may be lagging, however.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def has_sequence(self = None, sequence_name = None, schema = None, **kw):
        '''Return True if the backend has a sequence with the given name.

        :param sequence_name: name of the sequence to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 1.4

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def has_index(self = None, table_name = None, index_name = None, schema = (None,), **kw):
        '''Check the existence of a particular index name in the database.

        :param table_name: the name of the table the index belongs to
        :param index_name: the name of the index to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def has_schema(self = None, schema_name = None, **kw):
        '''Return True if the backend has a schema with the given name.

        :param schema_name: name of the schema to check
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_sorted_table_and_fkc_names(self = None, schema = None, **kw):
        '''Return dependency-sorted table and foreign key constraint names in
        referred to within a particular schema.

        This will yield 2-tuples of
        ``(tablename, [(tname, fkname), (tname, fkname), ...])``
        consisting of table names in CREATE order grouped with the foreign key
        constraint names that are not detected as belonging to a cycle.
        The final element
        will be ``(None, [(tname, fkname), (tname, fkname), ..])``
        which will consist of remaining
        foreign key constraint names that would require a separate CREATE
        step after-the-fact, based on dependencies between tables.

        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. seealso::

            :meth:`_reflection.Inspector.get_table_names`

            :func:`.sort_tables_and_constraints` - similar method which works
            with an already-given :class:`_schema.MetaData`.

        '''
        return self.sort_tables_on_foreign_key_dependency(consider_schemas = (schema,))()

    
    def sort_tables_on_foreign_key_dependency(self = None, consider_schemas = None, **kw):
        '''Return dependency-sorted table and foreign key constraint names
        referred to within multiple schemas.

        This method may be compared to
        :meth:`.Inspector.get_sorted_table_and_fkc_names`, which
        works on one schema at a time; here, the method is a generalization
        that will consider multiple schemas at once including that it will
        resolve for cross-schema foreign keys.

        .. versionadded:: 2.0

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_temp_table_names(self = None, **kw):
        '''Return a list of temporary table names for the current bind.

        This method is unsupported by most dialects; currently
        only Oracle Database, PostgreSQL and SQLite implements it.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_temp_view_names(self = None, **kw):
        '''Return a list of temporary view names for the current bind.

        This method is unsupported by most dialects; currently
        only PostgreSQL and SQLite implements it.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_table_options(self = None, table_name = None, schema = None, **kw):
        '''Return a dictionary of options specified when the table of the
        given name was created.

        This currently includes some options that apply to MySQL and Oracle
        Database tables.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dict with the table options. The returned keys depend on the
         dialect in use. Each one is prefixed with the dialect name.

        .. seealso:: :meth:`Inspector.get_multi_table_options`

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_table_options(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, Dict[str, Any]]'), **kw):
        '''Return a dictionary of options specified when the tables in the
        given schema were created.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        This currently includes some options that apply to MySQL and Oracle
        tables.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if options of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries with the table options.
         The returned keys in each dict depend on the
         dialect in use. Each one is prefixed with the dialect name.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_table_options`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_view_names(self = None, schema = None, **kw):
        '''Return all non-materialized view names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.


        .. versionchanged:: 2.0  For those dialects that previously included
           the names of materialized views in this list (currently PostgreSQL),
           this method no longer returns the names of materialized views.
           the :meth:`.Inspector.get_materialized_view_names` method should
           be used instead.

        .. seealso::

            :meth:`.Inspector.get_materialized_view_names`

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_materialized_view_names(self = None, schema = None, **kw):
        '''Return all materialized view names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.Inspector.get_view_names`

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_sequence_names(self = None, schema = None, **kw):
        '''Return all sequence names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_view_definition(self = None, view_name = None, schema = None, **kw):
        '''Return definition for the plain or materialized view called
        ``view_name``.

        :param view_name: Name of the view.
        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_columns(self = None, table_name = None, schema = None, **kw):
        '''Return information about columns in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``,
        return column information as a list of :class:`.ReflectedColumn`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: list of dictionaries, each representing the definition of
         a database column.

        .. seealso:: :meth:`Inspector.get_multi_columns`.

        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def _instantiate_types(self = None, data = None):
        for col_defs in data:
            for col_def in col_defs:
                coltype = col_def['type']
                if not isinstance(coltype, TypeEngine):
                    col_def['type'] = coltype()
                return None

    
    def get_multi_columns(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, List[ReflectedColumn]]'), **kw):
        '''Return information about columns in all objects in the given
        schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of :class:`.ReflectedColumn`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if columns of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of a database column.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_columns`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_pk_constraint(self = None, table_name = None, schema = None, **kw):
        '''Return information about primary key constraint in ``table_name``.

        Given a string ``table_name``, and an optional string `schema`, return
        primary key information as a :class:`.ReflectedPrimaryKeyConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary representing the definition of
         a primary key constraint.

        .. seealso:: :meth:`Inspector.get_multi_pk_constraint`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_pk_constraint(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, ReflectedPrimaryKeyConstraint]'), **kw):
        '''Return information about primary key constraints in
        all tables in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a :class:`.ReflectedPrimaryKeyConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if primary keys of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries, each representing the
         definition of a primary key constraint.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_pk_constraint`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_foreign_keys(self = None, table_name = None, schema = None, **kw):
        '''Return information about foreign_keys in ``table_name``.

        Given a string ``table_name``, and an optional string `schema`, return
        foreign key information as a list of
        :class:`.ReflectedForeignKeyConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         a foreign key definition.

        .. seealso:: :meth:`Inspector.get_multi_foreign_keys`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_foreign_keys(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, List[ReflectedForeignKeyConstraint]]'), **kw):
        '''Return information about foreign_keys in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedForeignKeyConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if foreign keys of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing
         a foreign key definition.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_foreign_keys`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_indexes(self = None, table_name = None, schema = None, **kw):
        '''Return information about indexes in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        index information as a list of :class:`.ReflectedIndex`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of an index.

        .. seealso:: :meth:`Inspector.get_multi_indexes`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_indexes(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, List[ReflectedIndex]]'), **kw):
        '''Return information about indexes in in all objects
        in the given schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of :class:`.ReflectedIndex`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if indexes of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of an index.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_indexes`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_unique_constraints(self = None, table_name = None, schema = None, **kw):
        '''Return information about unique constraints in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        unique constraint information as a list of
        :class:`.ReflectedUniqueConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of an unique constraint.

        .. seealso:: :meth:`Inspector.get_multi_unique_constraints`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_unique_constraints(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, List[ReflectedUniqueConstraint]]'), **kw):
        '''Return information about unique constraints in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedUniqueConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if constraints of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of an unique constraint.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_unique_constraints`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_table_comment(self = None, table_name = None, schema = None, **kw):
        '''Return information about the table comment for ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``,
        return table comment information as a :class:`.ReflectedTableComment`.

        Raises ``NotImplementedError`` for a dialect that does not support
        comments.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary, with the table comment.

        .. versionadded:: 1.2

        .. seealso:: :meth:`Inspector.get_multi_table_comment`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_table_comment(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, ReflectedTableComment]'), **kw):
        '''Return information about the table comment in all objects
        in the given schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a :class:`.ReflectedTableComment`.

        Raises ``NotImplementedError`` for a dialect that does not support
        comments.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if comments of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries, representing the
         table comments.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_table_comment`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_check_constraints(self = None, table_name = None, schema = None, **kw):
        '''Return information about check constraints in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        check constraint information as a list of
        :class:`.ReflectedCheckConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of a check constraints.

        .. seealso:: :meth:`Inspector.get_multi_check_constraints`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def get_multi_check_constraints(self = None, schema = None, filter_names = None, kind = (None, None, ObjectKind.TABLE, ObjectScope.DEFAULT), scope = ('schema', 'Optional[str]', 'filter_names', 'Optional[Sequence[str]]', 'kind', 'ObjectKind', 'scope', 'ObjectScope', 'kw', 'Any', 'return', 'Dict[TableKey, List[ReflectedCheckConstraint]]'), **kw):
        '''Return information about check constraints in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedCheckConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if constraints of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of a check constraints.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_check_constraints`
        '''
        conn = self._operation_context()
    # WARNING: Decompyle incomplete

    
    def reflect_table(self, table, include_columns = None, exclude_columns = None, resolve_fks = None, _extend_on = ((), True, None, None), _reflect_info = ('table', 'sa_schema.Table', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'resolve_fks', 'bool', '_extend_on', 'Optional[Set[sa_schema.Table]]', '_reflect_info', 'Optional[_ReflectionInfo]', 'return', 'None')):
        '''Given a :class:`_schema.Table` object, load its internal
        constructs based on introspection.

        This is the underlying method used by most dialects to produce
        table reflection.  Direct usage is like::

            from sqlalchemy import create_engine, MetaData, Table
            from sqlalchemy import inspect

            engine = create_engine("...")
            meta = MetaData()
            user_table = Table("user", meta)
            insp = inspect(engine)
            insp.reflect_table(user_table, None)

        .. versionchanged:: 1.4 Renamed from ``reflecttable`` to
           ``reflect_table``

        :param table: a :class:`~sqlalchemy.schema.Table` instance.
        :param include_columns: a list of string column names to include
          in the reflection process.  If ``None``, all columns are reflected.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _reflect_column(self, table, col_d = None, include_columns = None, exclude_columns = None, cols_by_orig_name = ('table', 'sa_schema.Table', 'col_d', 'ReflectedColumn', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _reflect_pk(self, _reflect_info, table_key = None, table = None, cols_by_orig_name = None, exclude_columns = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'exclude_columns', 'Collection[str]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _reflect_fk(self, _reflect_info, table_key, table, cols_by_orig_name, include_columns, exclude_columns = None, resolve_fks = None, _extend_on = None, reflection_options = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'resolve_fks', 'bool', '_extend_on', 'Optional[Set[sa_schema.Table]]', 'reflection_options', 'Dict[str, Any]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    _index_sort_exprs = {
        'asc': operators.asc_op,
        'desc': operators.desc_op,
        'nulls_first': operators.nulls_first_op,
        'nulls_last': operators.nulls_last_op }
    
    def _reflect_indexes(self, _reflect_info, table_key, table, cols_by_orig_name = None, include_columns = None, exclude_columns = None, reflection_options = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'reflection_options', 'Dict[str, Any]', 'return', 'None')):
        indexes = _reflect_info.indexes.get(table_key, [])
    # WARNING: Decompyle incomplete

    
    def _reflect_unique_constraints(self, _reflect_info, table_key, table, cols_by_orig_name = None, include_columns = None, exclude_columns = None, reflection_options = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'reflection_options', 'Dict[str, Any]', 'return', 'None')):
        constraints = _reflect_info.unique_constraints.get(table_key, [])
    # WARNING: Decompyle incomplete

    
    def _reflect_check_constraints(self, _reflect_info, table_key, table, cols_by_orig_name = None, include_columns = None, exclude_columns = None, reflection_options = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'cols_by_orig_name', 'Dict[str, sa_schema.Column[Any]]', 'include_columns', 'Optional[Collection[str]]', 'exclude_columns', 'Collection[str]', 'reflection_options', 'Dict[str, Any]', 'return', 'None')):
        constraints = _reflect_info.check_constraints.get(table_key, [])
    # WARNING: Decompyle incomplete

    
    def _reflect_table_comment(self, _reflect_info = None, table_key = None, table = None, reflection_options = ('_reflect_info', '_ReflectionInfo', 'table_key', 'TableKey', 'table', 'sa_schema.Table', 'reflection_options', 'Dict[str, Any]', 'return', 'None')):
        comment_dict = _reflect_info.table_comment.get(table_key)
        if comment_dict:
            table.comment = comment_dict['text']
            return None

    
    def _get_reflection_info(self = None, schema = None, filter_names = None, available = (None, None, None, None), _reflect_info = ('schema', 'Optional[str]', 'filter_names', 'Optional[Collection[str]]', 'available', 'Optional[Collection[str]]', '_reflect_info', 'Optional[_ReflectionInfo]', 'kw', 'Any', 'return', '_ReflectionInfo'), **kw):
        pass
    # WARNING: Decompyle incomplete


Inspector = <NODE:27>(Inspector, 'Inspector', inspection.Inspectable['Inspector'])()
ReflectionDefaults = <NODE:12>()
_ReflectionInfo = <NODE:12>()
