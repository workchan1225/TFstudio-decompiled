# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sql.pyc (Python 3.11)

'''
Collection of query wrappers / abstractions to both facilitate data
retrieval and to reduce dependency on DB-specific API.
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from contextlib import ExitStack, contextmanager
from datetime import date, datetime, time
from functools import partial
import re
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas.compat._optional import VERSIONS, import_optional_dependency
from pandas.errors import AbstractMethodError, DatabaseError
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import is_dict_like, is_list_like, is_object_dtype, is_string_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype
from pandas.core.dtypes.missing import isna
from pandas import get_option
from pandas.core.api import DataFrame, Series
from pandas.core.arrays import ArrowExtensionArray
from pandas.core.arrays.string_ import StringDtype
from pandas.core.base import PandasObject

common
from pandas.core.common import maybe_make_list
import pandas.core.common, core
from pandas.core.internals.construction import convert_object_array
from pandas.core.tools.datetimes import to_datetime
from pandas.io._util import arrow_table_to_pandas
if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterator, Mapping
    from sqlalchemy import Table
    from sqlalchemy.sql.expression import Delete, Select, TextClause
    from pandas._typing import DtypeArg, DtypeBackend, IndexLabel
    from pandas import Index

def _process_parse_dates_argument(parse_dates):
    '''Process parse_dates argument for read_sql functions'''
    pass
# WARNING: Decompyle incomplete


def _handle_date_column(col = None, utc = None, format = None):
    pass
# WARNING: Decompyle incomplete


def _parse_date_columns(data_frame = None, parse_dates = None):
    '''
    Force non-datetime columns to be read as such.
    Supports both string formatted and integer timestamp columns.
    '''
    parse_dates = _process_parse_dates_argument(parse_dates)
    for col_name, df_col in enumerate(data_frame.items()):
        if isinstance(df_col.dtype, DatetimeTZDtype) or col_name in parse_dates:
            fmt = parse_dates[col_name]
        else:
            except (KeyError, TypeError):
                fmt = None
            data_frame.isetitem(i, _handle_date_column(df_col, format = fmt))
        return data_frame


def _convert_arrays_to_dataframe(data = None, columns = None, coerce_float = None, dtype_backend = (True, 'numpy')):
    content = lib.to_object_array_tuples(data)
    idx_len = content.shape[0]
    arrays = convert_object_array(list(content.T), dtype = None, coerce_float = coerce_float, dtype_backend = dtype_backend)
    if dtype_backend == 'pyarrow':
        pa = import_optional_dependency('pyarrow')
        result_arrays = []
        for arr in arrays:
            pa_array = pa.array(arr, from_pandas = True)
            if arr.dtype == 'string':
                pa_array = pa_array.cast(pa.string())
            result_arrays.append(ArrowExtensionArray(pa_array))
            arrays = result_arrays
            if arrays:
                return DataFrame._from_arrays(arrays, columns = columns, index = range(idx_len), verify_integrity = False)
            return None(columns = columns)


def _wrap_result(data, columns, index_col = None, coerce_float = None, parse_dates = None, dtype = (None, True, None, None, 'numpy'), dtype_backend = ('coerce_float', 'bool', 'dtype', 'DtypeArg | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame')):
    '''Wrap result set of a SQLAlchemy query in a DataFrame.'''
    frame = _convert_arrays_to_dataframe(data, columns, coerce_float, dtype_backend)
    if dtype:
        frame = frame.astype(dtype)
    frame = _parse_date_columns(frame, parse_dates)
# WARNING: Decompyle incomplete


def _wrap_result_adbc(df = None, *, index_col, parse_dates, dtype, dtype_backend):
    '''Wrap result set of a SQLAlchemy query in a DataFrame.'''
    if dtype:
        df = df.astype(dtype)
    df = _parse_date_columns(df, parse_dates)
# WARNING: Decompyle incomplete

read_sql_table = (lambda table_name, con, schema, index_col, coerce_float = None, parse_dates = None, columns = overload, chunksize = (..., ..., ..., ..., ..., ..., ...), dtype_backend = ('table_name', 'str', 'index_col', 'str | list[str] | None', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'columns', 'list[str] | None', 'chunksize', 'None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame'): pass)()
read_sql_table = (lambda table_name, con, schema, index_col, coerce_float = None, parse_dates = None, columns = overload, chunksize = (..., ..., ..., ..., ..., ..., ...), dtype_backend = ('table_name', 'str', 'index_col', 'str | list[str] | None', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'columns', 'list[str] | None', 'chunksize', 'int', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'Iterator[DataFrame]'): pass)()
read_sql_table = (lambda table_name, con, schema, index_col, coerce_float = None, parse_dates = None, columns = set_module('pandas'), chunksize = (None, None, True, None, None, None, lib.no_default), dtype_backend = ('table_name', 'str', 'schema', 'str | None', 'index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'columns', 'list[str] | None', 'chunksize', 'int | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame | Iterator[DataFrame]'): check_dtype_backend(dtype_backend)if dtype_backend is lib.no_default:
dtype_backend = 'numpy'# WARNING: Decompyle incomplete
)()
read_sql_query = (lambda sql, con, index_col, coerce_float, params = None, parse_dates = None, chunksize = overload, dtype = (..., ..., ..., ..., ..., ..., ...), dtype_backend = ('index_col', 'str | list[str] | None', 'params', 'list[Any] | Mapping[str, Any] | None', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'chunksize', 'None', 'dtype', 'DtypeArg | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame'): pass)()
read_sql_query = (lambda sql, con, index_col, coerce_float, params = None, parse_dates = None, chunksize = overload, dtype = (..., ..., ..., ..., ..., ..., ...), dtype_backend = ('index_col', 'str | list[str] | None', 'params', 'list[Any] | Mapping[str, Any] | None', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'chunksize', 'int', 'dtype', 'DtypeArg | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'Iterator[DataFrame]'): pass)()
read_sql_query = (lambda sql, con, index_col, coerce_float, params = None, parse_dates = None, chunksize = set_module('pandas'), dtype = (None, True, None, None, None, None, lib.no_default), dtype_backend = ('index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'params', 'list[Any] | Mapping[str, Any] | None', 'parse_dates', 'list[str] | dict[str, str] | dict[str, dict[str, Any]] | None', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'DataFrame | Iterator[DataFrame]'): check_dtype_backend(dtype_backend)if dtype_backend is lib.no_default:
dtype_backend = 'numpy'# WARNING: Decompyle incomplete
)()
read_sql = (lambda sql, con, index_col, coerce_float, params, parse_dates = None, columns = None, chunksize = overload, dtype_backend = (..., ..., ..., ..., ..., ..., ..., None), dtype = ('index_col', 'str | list[str] | None', 'columns', 'list[str]', 'chunksize', 'None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'dtype', 'DtypeArg | None', 'return', 'DataFrame'): pass)()
read_sql = (lambda sql, con, index_col, coerce_float, params, parse_dates = None, columns = None, chunksize = overload, dtype_backend = (..., ..., ..., ..., ..., ..., ..., None), dtype = ('index_col', 'str | list[str] | None', 'columns', 'list[str]', 'chunksize', 'int', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'dtype', 'DtypeArg | None', 'return', 'Iterator[DataFrame]'): pass)()
read_sql = (lambda sql, con, index_col, coerce_float, params, parse_dates = None, columns = None, chunksize = set_module('pandas'), dtype_backend = (None, True, None, None, None, None, lib.no_default, None), dtype = ('index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'columns', 'list[str] | None', 'chunksize', 'int | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'dtype', 'DtypeArg | None', 'return', 'DataFrame | Iterator[DataFrame]'): check_dtype_backend(dtype_backend)if dtype_backend is lib.no_default:
dtype_backend = 'numpy'# WARNING: Decompyle incomplete
)()

def to_sql(frame, name, con, schema, if_exists, index, index_label = None, chunksize = None, dtype = None, method = (None, 'fail', True, None, None, None, None, 'auto'), engine = ('name', 'str', 'schema', 'str | None', 'if_exists', "Literal['fail', 'replace', 'append', 'delete_rows']", 'index', 'bool', 'index_label', 'IndexLabel | None', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'method', "Literal['multi'] | Callable | None", 'engine', 'str', 'return', 'int | None'), **engine_kwargs):
    """
    Write records stored in a DataFrame to a SQL database.

    .. warning::
        The pandas library does not attempt to sanitize inputs provided via a to_sql call.
        Please refer to the documentation for the underlying database driver to see if it
        will properly prevent injection, or alternatively be advised of a security risk when
        executing arbitrary commands in a to_sql call.

    Parameters
    ----------
    frame : DataFrame, Series
    name : str
        Name of SQL table.
    con : ADBC Connection, SQLAlchemy connectable, str, or sqlite3 connection
        or sqlite3 DBAPI2 connection
        ADBC provides high performance I/O with native type support, where available.
        Using SQLAlchemy makes it possible to use any DB supported by that
        library.
        If a DBAPI2 object, only sqlite3 is supported.
    schema : str, optional
        Name of SQL schema in database to write to (if database flavor
        supports this). If None, use default schema (default).
    if_exists : {'fail', 'replace', 'append', 'delete_rows'}, default 'fail'
        - fail: If table exists, do nothing.
        - replace: If table exists, drop it, recreate it, and insert data.
        - append: If table exists, insert data. Create if does not exist.
        - delete_rows: If a table exists, delete all records and insert data.
    index : bool, default True
        Write DataFrame index as a column.
    index_label : str or sequence, optional
        Column label for index column(s). If None is given (default) and
        `index` is True, then the index names are used.
        A sequence should be given if the DataFrame uses MultiIndex.
    chunksize : int, optional
        Specify the number of rows in each batch to be written at a time.
        By default, all rows will be written at once.
    dtype : dict or scalar, optional
        Specifying the datatype for columns. If a dictionary is used, the
        keys should be the column names and the values should be the
        SQLAlchemy types or strings for the sqlite3 fallback mode. If a
        scalar is provided, it will be applied to all columns.
    method : {None, 'multi', callable}, optional
        Controls the SQL insertion clause used:

        - None : Uses standard SQL ``INSERT`` clause (one per row).
        - ``'multi'``: Pass multiple values in a single ``INSERT`` clause.
        - callable with signature ``(pd_table, conn, keys, data_iter) -> int | None``.

        Details and a sample callable implementation can be found in the
        section :ref:`insert method <io.sql.method>`.
    engine : {'auto', 'sqlalchemy'}, default 'auto'
        SQL engine library to use. If 'auto', then the option
        ``io.sql.engine`` is used. The default ``io.sql.engine``
        behavior is 'sqlalchemy'

    **engine_kwargs
        Any additional kwargs are passed to the engine.

    Returns
    -------
    None or int
        Number of rows affected by to_sql. None is returned if the callable
        passed into ``method`` does not return an integer number of rows.

    Notes
    -----
    The returned rows affected is the sum of the ``rowcount`` attribute of ``sqlite3.Cursor``
    or SQLAlchemy connectable. If using ADBC the returned rows are the result
    of ``Cursor.adbc_ingest``. The returned value may not reflect the exact number of written
    rows as stipulated in the
    `sqlite3 <https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.rowcount>`__ or
    `SQLAlchemy <https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.BaseCursorResult.rowcount>`__
    """
    if if_exists not in ('fail', 'replace', 'append', 'delete_rows'):
        raise ValueError(f'''\'{if_exists}\' is not valid for if_exists''')
    if isinstance(frame, Series):
        frame = frame.to_frame()
    elif not isinstance(frame, DataFrame):
        raise NotImplementedError("'frame' argument should be either a Series or a DataFrame")
    pandas_sql = pandasSQL_builder(con, schema = schema, need_transaction = True)
# WARNING: Decompyle incomplete


def has_table(table_name = None, con = None, schema = None):
    '''
    Check if DataBase has named table.

    Parameters
    ----------
    table_name: string
        Name of SQL table.
    con: ADBC Connection, SQLAlchemy connectable, str, or sqlite3 connection
        ADBC provides high performance I/O with native type support, where available.
        Using SQLAlchemy makes it possible to use any DB supported by that
        library.
        If a DBAPI2 object, only sqlite3 is supported.
    schema : string, default None
        Name of SQL schema in database to write to (if database flavor supports
        this). If None, use default schema (default).

    Returns
    -------
    boolean
    '''
    pandas_sql = pandasSQL_builder(con, schema = schema)
    None(None, None)
    return 
    with None:
        if not None, pandas_sql.has_table(table_name):
            pass

table_exists = has_table

def pandasSQL_builder(con = None, schema = None, need_transaction = None):
    '''
    Convenience function to return the correct PandasSQL subclass based on the
    provided parameters.  Also creates a sqlalchemy connection and transaction
    if necessary.
    '''
    import sqlite3
# WARNING: Decompyle incomplete


class SQLTable(PandasObject):
    '''
    For mapping Pandas tables to SQL tables.
    Uses fact that table is reflected by SQLAlchemy to
    do better type conversions.
    Also holds various flags needed to avoid having to
    pass them between functions all the time.
    '''
    
    def __init__(self, name, pandas_sql_engine, frame, index, if_exists, prefix = None, index_label = None, schema = None, keys = (None, True, 'fail', 'pandas', None, None, None, None), dtype = ('name', 'str', 'index', 'bool | str | list[str] | None', 'if_exists', "Literal['fail', 'replace', 'append', 'delete_rows']", 'prefix', 'str', 'dtype', 'DtypeArg | None', 'return', 'None')):
        self.name = name
        self.pd_sql = pandas_sql_engine
        self.prefix = prefix
        self.frame = frame
        self.index = self._index_name(index, index_label)
        self.schema = schema
        self.if_exists = if_exists
        self.keys = keys
        self.dtype = dtype
    # WARNING: Decompyle incomplete

    
    def exists(self):
        return self.pd_sql.has_table(self.name, self.schema)

    
    def sql_schema(self = None):
        CreateTable = CreateTable
        import sqlalchemy.schema
        return str(CreateTable(self.table).compile(self.pd_sql.con))

    
    def _execute_create(self = None):
        self.table = self.table.to_metadata(self.pd_sql.meta)
        self.pd_sql.run_transaction()
        self.table.create(bind = self.pd_sql.con)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def create(self = None):
        if self.exists():
            if self.if_exists == 'fail':
                raise ValueError(f'''Table \'{self.name}\' already exists.''')
            if self.if_exists == 'replace':
                self.pd_sql.drop_table(self.name, self.schema)
                self._execute_create()
                return None
            if None.if_exists == 'append':
                return None
            if None.if_exists == 'delete_rows':
                self.pd_sql.delete_rows(self.name, self.schema)
                return None
            raise None(f'''\'{self.if_exists}\' is not valid for if_exists''')
        self._execute_create()

    
    def _execute_insert(self = None, conn = None, keys = None, data_iter = ('keys', 'list[str]', 'return', 'int')):
        '''
        Execute SQL statement inserting data

        Parameters
        ----------
        conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
        keys : list of str
           Column names
        data_iter : generator of list
           Each item contains a list of values to be inserted
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _execute_insert_multi(self = None, conn = None, keys = None, data_iter = ('keys', 'list[str]', 'return', 'int')):
        '''
        Alternative to _execute_insert for DBs support multi-value INSERT.

        Note: multi-value insert is usually faster for analytics DBs
        and tables containing a few columns
        but performance degrades quickly with increase of columns.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def insert_data(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def insert(self = None, chunksize = None, method = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _query_iterator(self, result, exit_stack, chunksize = None, columns = None, coerce_float = None, parse_dates = (True, None, 'numpy'), dtype_backend = ('exit_stack', 'ExitStack', 'chunksize', 'int | None', 'coerce_float', 'bool', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'Generator[DataFrame]')):
        '''Return generator through chunked result set.'''
        pass
    # WARNING: Decompyle incomplete

    
    def read(self, exit_stack, coerce_float = None, parse_dates = None, columns = None, chunksize = (True, None, None, None, 'numpy'), dtype_backend = ('exit_stack', 'ExitStack', 'coerce_float', 'bool', 'chunksize', 'int | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame | Iterator[DataFrame]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _index_name(self, index, index_label):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_column_names_and_types(self, dtype_mapper):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_table_setup(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _harmonize_columns(self = None, parse_dates = None, dtype_backend = None):
        """
        Make the DataFrame's column types align with the SQL table
        column types.
        Need to work around limited NA value support. Floats are always
        fine, ints must always be floats if there are Null values.
        Booleans are hard because converting bool column with None replaces
        all Nones with false. Therefore only convert bool if there are no
        NA values.
        Datetimes should already be converted to np.datetime64 if supported,
        but here we also force conversion if required.
        """
        parse_dates = _process_parse_dates_argument(parse_dates)
        for sql_col in self.table.columns:
            col_name = sql_col.name
            df_col = self.frame[col_name]
            if col_name in parse_dates:
                fmt = parse_dates[col_name]
            else:
                except TypeError:
                    fmt = None
                self.frame[col_name] = _handle_date_column(df_col, format = fmt)
            col_type = self._get_dtype(sql_col.type)
            if col_type is datetime and col_type is date or col_type is DatetimeTZDtype:
                utc = col_type is DatetimeTZDtype
                self.frame[col_name] = _handle_date_column(df_col, utc = utc)
            elif dtype_backend == 'numpy' and col_type is float:
                self.frame[col_name] = df_col.astype(col_type)
            elif using_string_dtype() and is_string_dtype(col_type) and is_object_dtype(self.frame[col_name]):
                self.frame[col_name] = df_col.astype(col_type)
            elif dtype_backend == 'numpy' and len(df_col) == df_col.count():
                if col_type is np.dtype('int64') or col_type is bool:
                    self.frame[col_name] = df_col.astype(col_type)
            except KeyError:
                continue
            return None

    
    def _sqlalchemy_type(self = None, col = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_dtype(self, sqltype):
        TIMESTAMP = TIMESTAMP
        Boolean = Boolean
        Date = Date
        DateTime = DateTime
        Float = Float
        Integer = Integer
        String = String
        import sqlalchemy.types
        if isinstance(sqltype, Float):
            return float
        if None(sqltype, Integer):
            return np.dtype('int64')
        if None(sqltype, TIMESTAMP):
            if not sqltype.timezone:
                return datetime
            return None
        if None(sqltype, DateTime):
            return datetime
        if None(sqltype, Date):
            return date
        if None(sqltype, Boolean):
            return bool
        if None(sqltype, String) and using_string_dtype():
            return StringDtype(na_value = np.nan)



class PandasSQL(ABC, PandasObject):
    '''
    Subclasses Should define read_query and to_sql.
    '''
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *args):
        pass

    
    def read_table(self, table_name, index_col, coerce_float, parse_dates = None, columns = None, schema = None, chunksize = (None, True, None, None, None, None, 'numpy'), dtype_backend = ('table_name', 'str', 'index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'schema', 'str | None', 'chunksize', 'int | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame | Iterator[DataFrame]')):
        raise NotImplementedError

    read_query = (lambda self, sql, index_col, coerce_float, parse_dates = None, params = None, chunksize = abstractmethod, dtype = (None, True, None, None, None, None, 'numpy'), dtype_backend = ('sql', 'str', 'index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame | Iterator[DataFrame]'): pass)()
    to_sql = (lambda self, frame, name, if_exists, index, index_label, schema = None, chunksize = None, dtype = abstractmethod, method = ('fail', True, None, None, None, None, None, 'auto'), engine = ('name', 'str', 'if_exists', "Literal['fail', 'replace', 'append', 'delete_rows']", 'index', 'bool', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'method', "Literal['multi'] | Callable | None", 'engine', 'str', 'return', 'int | None'): pass)()
    execute = (lambda self = None, sql = None, params = abstractmethod: pass)()
    has_table = (lambda self = None, name = None, schema = abstractmethod: pass)()
    _create_sql_schema = (lambda self, frame = None, table_name = None, keys = abstractmethod, dtype = (None, None, None), schema = ('frame', 'DataFrame', 'table_name', 'str', 'keys', 'list[str] | None', 'dtype', 'DtypeArg | None', 'schema', 'str | None', 'return', 'str'): pass)()


class BaseEngine:
    
    def insert_records(self, table, con, frame, name = None, index = None, schema = None, chunksize = (True, None, None, None), method = ('table', 'SQLTable', 'name', 'str', 'index', 'bool | str | list[str] | None', 'chunksize', 'int | None', 'return', 'int | None'), **engine_kwargs):
        '''
        Inserts data into already-prepared table
        '''
        raise AbstractMethodError(self)



class SQLAlchemyEngine(BaseEngine):
    
    def __init__(self = None):
        import_optional_dependency('sqlalchemy', extra = 'sqlalchemy is required for SQL support.')

    
    def insert_records(self, table, con, frame, name = None, index = None, schema = None, chunksize = (True, None, None, None), method = ('table', 'SQLTable', 'name', 'str', 'index', 'bool | str | list[str] | None', 'chunksize', 'int | None', 'return', 'int | None'), **engine_kwargs):
        exc = exc
        import sqlalchemy
        
        try:
            return table.insert(chunksize = chunksize, method = method)
        except exc.StatementError:
            err = None
            msg = '(\\(1054, "Unknown column \'inf(e0)?\' in \'field list\'"\\))(?#\n            )|inf can not be used with MySQL'
            err_text = str(err.orig)
            if re.search(msg, err_text):
                raise ValueError('inf cannot be used with MySQL'), err
            raise err
            err = None
            del err




def get_engine(engine = None):
    '''return our implementation'''
    if engine == 'auto':
        engine = get_option('io.sql.engine')
    if engine == 'auto':
        engine_classes = [
            SQLAlchemyEngine]
        error_msgs = ''
        for engine_class in engine_classes:
            
            return None, engine_class()
            except ImportError:
                error_msgs += '\n - ' + str(err) = None
                err = None
                del err
                continue
                err = None
                del err
            raise ImportError(f'''Unable to find a usable engine; tried using: \'sqlalchemy\'.\nA suitable version of sqlalchemy is required for sql I/O support.\nTrying to import the above resulted in these errors:{error_msgs}''')
            if engine == 'sqlalchemy':
                return SQLAlchemyEngine()
            raise None("engine must be one of 'auto', 'sqlalchemy'")


class SQLDatabase(PandasSQL):
    '''
    This class enables conversion between DataFrame and SQL databases
    using SQLAlchemy to handle DataBase abstraction.

    Parameters
    ----------
    con : SQLAlchemy Connectable or URI string.
        Connectable to connect with the database. Using SQLAlchemy makes it
        possible to use any DB supported by that library.
    schema : string, default None
        Name of SQL schema in database to write to (if database flavor
        supports this). If None, use default schema (default).
    need_transaction : bool, default False
        If True, SQLDatabase will create a transaction.

    '''
    
    def __init__(self = None, con = None, schema = None, need_transaction = (None, False)):
        create_engine = create_engine
        import sqlalchemy
        Engine = Engine
        import sqlalchemy.engine
        MetaData = MetaData
        import sqlalchemy.schema
        self.exit_stack = ExitStack()
        if isinstance(con, str):
            con = create_engine(con)
            self.exit_stack.callback(con.dispose)
        if isinstance(con, Engine):
            con = self.exit_stack.enter_context(con.connect())
        if not need_transaction and con.in_transaction():
            self.exit_stack.enter_context(con.begin())
        self.con = con
        self.meta = MetaData(schema = schema)
        self.returns_generator = False

    
    def __exit__(self = None, *args):
        if not self.returns_generator:
            self.exit_stack.close()
            return None

    run_transaction = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def execute(self = None, sql = None, params = contextmanager):
        '''Simple passthrough to SQLAlchemy connectable'''
        SQLAlchemyError = SQLAlchemyError
        import sqlalchemy.exc
    # WARNING: Decompyle incomplete

    
    def read_table(self, table_name, index_col, coerce_float, parse_dates = None, columns = None, schema = None, chunksize = (None, True, None, None, None, None, 'numpy'), dtype_backend = ('table_name', 'str', 'index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'schema', 'str | None', 'chunksize', 'int | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame | Iterator[DataFrame]')):
        '''
        Read SQL database table into a DataFrame.

        Parameters
        ----------
        table_name : str
            Name of SQL table in database.
        index_col : string, optional, default: None
            Column to set as index.
        coerce_float : bool, default True
            Attempts to convert values of non-string, non-numeric objects
            (like decimal.Decimal) to floating point. This can result in
            loss of precision.
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg}``, where the arg corresponds
              to the keyword arguments of :func:`pandas.to_datetime`.
              Especially useful with databases without native Datetime support,
              such as SQLite.
        columns : list, default: None
            List of column names to select from SQL table.
        schema : string, default None
            Name of SQL schema in database to query (if database flavor
            supports this).  If specified, this overwrites the default
            schema of the SQL database object.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.
        dtype_backend : {\'numpy_nullable\', \'pyarrow\'}
            Back-end data type applied to the resultant :class:`DataFrame`
            (still experimental). If not specified, the default behavior
            is to not use nullable data types. If specified, the behavior
            is as follows:

            * ``"numpy_nullable"``: returns nullable-dtype-backed :class:`DataFrame`
            * ``"pyarrow"``: returns pyarrow-backed nullable
              :class:`ArrowDtype` :class:`DataFrame`

            .. versionadded:: 2.0

        Returns
        -------
        DataFrame

        See Also
        --------
        pandas.read_sql_table
        SQLDatabase.read_query

        '''
        self.meta.reflect(bind = self.con, only = [
            table_name], views = True)
        table = SQLTable(table_name, self, index = index_col, schema = schema)
    # WARNING: Decompyle incomplete

    _query_iterator = (lambda result, exit_stack, chunksize, columns, index_col = None, coerce_float = None, parse_dates = staticmethod, dtype = (None, True, None, None, 'numpy'), dtype_backend = ('exit_stack', 'ExitStack', 'chunksize', 'int', 'coerce_float', 'bool', 'dtype', 'DtypeArg | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'Generator[DataFrame]'): pass# WARNING: Decompyle incomplete
)()
    
    def read_query(self, sql, index_col, coerce_float, parse_dates = None, params = None, chunksize = None, dtype = (None, True, None, None, None, None, 'numpy'), dtype_backend = ('sql', 'str', 'index_col', 'str | list[str] | None', 'coerce_float', 'bool', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'dtype_backend', "DtypeBackend | Literal['numpy']", 'return', 'DataFrame | Iterator[DataFrame]')):
        """
        Read SQL query into a DataFrame.

        Parameters
        ----------
        sql : str
            SQL query to be executed.
        index_col : string, optional, default: None
            Column name to use as index for the returned DataFrame object.
        coerce_float : bool, default True
            Attempt to convert values of non-string, non-numeric objects (like
            decimal.Decimal) to floating point, useful for SQL result sets.
        params : list, tuple or dict, optional, default: None
            List of parameters to pass to execute method.  The syntax used
            to pass parameters is database driver dependent. Check your
            database driver documentation for which of the five syntax styles,
            described in PEP 249's paramstyle, is supported.
            Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg dict}``, where the arg dict
              corresponds to the keyword arguments of
              :func:`pandas.to_datetime` Especially useful with databases
              without native Datetime support, such as SQLite.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.
        dtype : Type name or dict of columns
            Data type for data or columns. E.g. np.float64 or
            {'a': np.float64, 'b': np.int32, 'c': 'Int64'}

        Returns
        -------
        DataFrame

        See Also
        --------
        read_sql_table : Read SQL database table into a DataFrame.
        read_sql

        """
        result = self.execute(sql, params)
        columns = result.keys()
    # WARNING: Decompyle incomplete

    read_sql = read_query
    
    def prep_table(self, frame, name, if_exists = None, index = None, index_label = None, schema = ('fail', True, None, None, None), dtype = ('name', 'str', 'if_exists', "Literal['fail', 'replace', 'append', 'delete_rows']", 'index', 'bool | str | list[str] | None', 'dtype', 'DtypeArg | None', 'return', 'SQLTable')):
        '''
        Prepares table in the database for data insertion. Creates it if needed, etc.
        '''
        if dtype:
            if not is_dict_like(dtype):
                dtype = dict.fromkeys(frame, dtype)
            else:
                dtype = cast(dict, dtype)
            TypeEngine = TypeEngine
            import sqlalchemy.types
            for col, my_type in dtype.items():
                if isinstance(my_type, type) and issubclass(my_type, TypeEngine):
                    continue
                if isinstance(my_type, TypeEngine):
                    continue
                raise ValueError(f'''The type of {col} is not a SQLAlchemy type''')
                table = SQLTable(name, self, frame = frame, index = index, if_exists = if_exists, index_label = index_label, schema = schema, dtype = dtype)
                table.create()
                return table

    
    def check_case_sensitive(self = None, name = None, schema = None):
        '''
        Checks table name for issues with case-sensitivity.
        Method is called after data is inserted.
        '''
        if not name.isdigit() or name.islower():
            sqlalchemy_inspect = inspect
            import sqlalchemy
            insp = sqlalchemy_inspect(self.con)
            if not schema:
                table_names = insp.get_table_names(schema = self.meta.schema)
                if name not in table_names:
                    msg = f'''The provided table name \'{name}\' is not found exactly as such in the database after writing the table, possibly due to case sensitivity issues. Consider using lower case table names.'''
                    warnings.warn(msg, UserWarning, stacklevel = find_stack_level())
                    return None
                return None
            return schema

    
    def to_sql(self, frame, name, if_exists, index, index_label, schema = None, chunksize = None, dtype = None, method = ('fail', True, None, None, None, None, None, 'auto'), engine = ('name', 'str', 'if_exists', "Literal['fail', 'replace', 'append', 'delete_rows']", 'index', 'bool', 'schema', 'str | None', 'chunksize', 'int | None', 'dtype', 'DtypeArg | None', 'method', "Literal['multi'] | Callable | None", 'engine', 'str', 'return', 'int | None'), **engine_kwargs):
        """
        Write records stored in a DataFrame to a SQL database.

        Parameters
        ----------
        frame : DataFrame
        name : string
            Name of SQL table.
        if_exists : {'fail', 'replace', 'append', 'delete_rows'}, default 'fail'
            - fail: If table exists, do nothing.
            - replace: If table exists, drop it, recreate it, and insert data.
            - append: If table exists, insert data. Create if does not exist.
            - delete_rows: If a table exists, delete all records and insert data.
        index : boolean, default True
            Write DataFrame index as a column.
        index_label : string or sequence, default None
            Column label for index column(s). If None is given (default) and
            `index` is True, then the index names are used.
            A sequence should be given if the DataFrame uses MultiIndex.
        schema : string, default None
            Name of SQL schema in database to write to (if database flavor
            supports this). If specified, this overwrites the default
            schema of the SQLDatabase object.
        chunksize : int, default None
            If not None, then rows will be written in batches of this size at a
            time.  If None, all rows will be written at once.
        dtype : single type or dict of column name to SQL type, default None
            Optional specifying the datatype for columns. The SQL type should
            be a SQLAlchemy type. If all columns are of the same type, one
            single value can be used.
        method : {None', 'multi', callable}, default None
            Controls the SQL insertion clause used:

            * None : Uses standard SQL ``INSERT`` clause (one per row).
            * 'multi': Pass multiple values in a single ``INSERT`` clause.
            * callable with signature ``(pd_table, conn, keys, data_iter)``.

            Details and a sample callable implementation can be found in the
            section :ref:`insert method <io.sql.method>`.
        engine : {'auto', 'sqlalchemy'}, default 'auto'
            SQL engine library to use. If 'auto', then the option
            ``io.sql.engine`` is used. The default ``io.sql.engine``
            behavior is 'sqlalchemy'

        **engine_kwargs
            Any additional kwargs are passed to the engine.
        """
        sql_engine = get_engine(engine)
        table = self.prep_table(frame = frame, name = name, if_exists = if_exists, index = index, index_label = index_label, schema = schema, dtype = dtype)
    # WARNING: Decompyle incomplete

    tables = (lambda self: self.meta.tables)()
    
    def has_table(self = None, name = None, schema = property):
