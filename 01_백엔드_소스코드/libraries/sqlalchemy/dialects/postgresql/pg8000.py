# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pg8000.pyc (Python 3.11)

'''
.. dialect:: postgresql+pg8000
    :name: pg8000
    :dbapi: pg8000
    :connectstring: postgresql+pg8000://user:password@host:port/dbname[?key=value&key=value...]
    :url: https://pypi.org/project/pg8000/

.. versionchanged:: 1.4  The pg8000 dialect has been updated for version
   1.16.6 and higher, and is again part of SQLAlchemy\'s continuous integration
   with full feature support.

.. _pg8000_unicode:

Unicode
-------

pg8000 will encode / decode string values between it and the server using the
PostgreSQL ``client_encoding`` parameter; by default this is the value in
the ``postgresql.conf`` file, which often defaults to ``SQL_ASCII``.
Typically, this can be changed to ``utf-8``, as a more useful default::

    # client_encoding = sql_ascii # actually, defaults to database encoding
    client_encoding = utf8

The ``client_encoding`` can be overridden for a session by executing the SQL:

.. sourcecode:: sql

    SET CLIENT_ENCODING TO \'utf8\';

SQLAlchemy will execute this SQL on all new connections based on the value
passed to :func:`_sa.create_engine` using the ``client_encoding`` parameter::

    engine = create_engine(
        "postgresql+pg8000://user:pass@host/dbname", client_encoding="utf8"
    )

.. _pg8000_ssl:

SSL Connections
---------------

pg8000 accepts a Python ``SSLContext`` object which may be specified using the
:paramref:`_sa.create_engine.connect_args` dictionary::

    import ssl

    ssl_context = ssl.create_default_context()
    engine = sa.create_engine(
        "postgresql+pg8000://scott:tiger@192.168.0.199/test",
        connect_args={"ssl_context": ssl_context},
    )

If the server uses an automatically-generated certificate that is self-signed
or does not match the host name (as seen from the client), it may also be
necessary to disable hostname checking::

    import ssl

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    engine = sa.create_engine(
        "postgresql+pg8000://scott:tiger@192.168.0.199/test",
        connect_args={"ssl_context": ssl_context},
    )

.. _pg8000_isolation_level:

pg8000 Transaction Isolation Level
-------------------------------------

The pg8000 dialect offers the same isolation level settings as that
of the :ref:`psycopg2 <psycopg2_isolation_level>` dialect:

* ``READ COMMITTED``
* ``READ UNCOMMITTED``
* ``REPEATABLE READ``
* ``SERIALIZABLE``
* ``AUTOCOMMIT``

.. seealso::

    :ref:`postgresql_isolation_level`

    :ref:`psycopg2_isolation_level`


'''
import decimal
import re
from  import ranges
from array import ARRAY as PGARRAY
from base import _DECIMAL_TYPES
from base import _FLOAT_TYPES
from base import _INT_TYPES
from base import ENUM
from base import INTERVAL
from base import PGCompiler
from base import PGDialect
from base import PGExecutionContext
from base import PGIdentifierPreparer
from json import JSON
from json import JSONB
from json import JSONPathType
from pg_catalog import _SpaceVector
from pg_catalog import OIDVECTOR
from types import CITEXT
from  import exc
from  import util
from engine import processors
from sql import sqltypes
from sql.elements import quoted_name

class _PGString(sqltypes.String):
    render_bind_cast = True


class _PGNumeric(sqltypes.Numeric):
    render_bind_cast = True
    
    def result_processor(self, dialect, coltype):
        if self.asdecimal:
            if coltype in _FLOAT_TYPES:
                return processors.to_decimal_processor_factory(decimal.Decimal, self._effective_decimal_return_scale)
            if None in _DECIMAL_TYPES or coltype in _INT_TYPES:
                return None
            raise None.InvalidRequestError('Unknown PG numeric type: %d' % coltype)
        if coltype in _FLOAT_TYPES:
            return None
        if None in _DECIMAL_TYPES or coltype in _INT_TYPES:
            return processors.to_float
        raise None.InvalidRequestError('Unknown PG numeric type: %d' % coltype)



class _PGFloat(sqltypes.Float, _PGNumeric):
    __visit_name__ = 'float'
    render_bind_cast = True


class _PGNumericNoBind(_PGNumeric):
    
    def bind_processor(self, dialect):
        pass



class _PGJSON(JSON):
    render_bind_cast = True
    
    def result_processor(self, dialect, coltype):
        pass



class _PGJSONB(JSONB):
    render_bind_cast = True
    
    def result_processor(self, dialect, coltype):
        pass



class _PGJSONIndexType(sqltypes.JSON.JSONIndexType):
    
    def get_dbapi_type(self, dbapi):
        raise NotImplementedError('should not be here')



class _PGJSONIntIndexType(sqltypes.JSON.JSONIntIndexType):
    __visit_name__ = 'json_int_index'
    render_bind_cast = True


class _PGJSONStrIndexType(sqltypes.JSON.JSONStrIndexType):
    __visit_name__ = 'json_str_index'
    render_bind_cast = True


class _PGJSONPathType(JSONPathType):
    pass


class _PGEnum(ENUM):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.UNKNOWN



class _PGInterval(INTERVAL):
    render_bind_cast = True
    
    def get_dbapi_type(self, dbapi):
        return dbapi.INTERVAL

    adapt_emulated_to_native = (lambda cls, interval: _PGInterval(precision = interval.second_precision))()


class _PGTimeStamp(sqltypes.DateTime):
    render_bind_cast = True


class _PGDate(sqltypes.Date):
    render_bind_cast = True


class _PGTime(sqltypes.Time):
    render_bind_cast = True


class _PGInteger(sqltypes.Integer):
    render_bind_cast = True


class _PGSmallInteger(sqltypes.SmallInteger):
    render_bind_cast = True


class _PGNullType(sqltypes.NullType):
    pass


class _PGBigInteger(sqltypes.BigInteger):
    render_bind_cast = True


class _PGBoolean(sqltypes.Boolean):
    render_bind_cast = True


class _PGARRAY(PGARRAY):
    render_bind_cast = True


class _PGOIDVECTOR(OIDVECTOR, _SpaceVector):
    pass


class _Pg8000Range(ranges.AbstractSingleRangeImpl):
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def result_processor(self, dialect, coltype):
        
        def to_range(value):
            pass
        # WARNING: Decompyle incomplete

        return to_range



class _Pg8000MultiRange(ranges.AbstractMultiRangeImpl):
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def result_processor(self, dialect, coltype):
        
        def to_multirange(value):
            pass
        # WARNING: Decompyle incomplete

        return to_multirange


_server_side_id = util.counter()

class PGExecutionContext_pg8000(PGExecutionContext):
    
    def create_server_side_cursor(self):
        ident = f'''c_{hex(id(self))[2:]!s}_{hex(_server_side_id())[2:]!s}'''
        return ServerSideCursor(self._dbapi_connection.cursor(), ident)

    
    def pre_exec(self):
        if not self.compiled:
            return None



class ServerSideCursor:
    server_side = True
    
    def __init__(self, cursor, ident):
        self.ident = ident
        self.cursor = cursor

    connection = (lambda self: self.cursor.connection)()
    rowcount = (lambda self: self.cursor.rowcount)()
    description = (lambda self: self.cursor.description)()
    
    def execute(self, operation, args, stream = ((), None)):
        op = 'DECLARE ' + self.ident + ' NO SCROLL CURSOR FOR ' + operation
        self.cursor.execute(op, args, stream = stream)
        return self

    
    def executemany(self, operation, param_sets):
        self.cursor.executemany(operation, param_sets)
        return self

    
    def fetchone(self):
        self.cursor.execute('FETCH FORWARD 1 FROM ' + self.ident)
        return self.cursor.fetchone()

    
    def fetchmany(self, num = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self):
        self.cursor.execute('FETCH FORWARD ALL FROM ' + self.ident)
        return self.cursor.fetchall()

    
    def close(self):
        self.cursor.execute('CLOSE ' + self.ident)
        self.cursor.close()

    
    def setinputsizes(self, *sizes):
        pass
    # WARNING: Decompyle incomplete

    
    def setoutputsize(self, size, column = (None,)):
        pass



class PGCompiler_pg8000(PGCompiler):
    
    def visit_mod_binary(self, binary, operator, **kw):
        pass
    # WARNING: Decompyle incomplete



class PGIdentifierPreparer_pg8000(PGIdentifierPreparer):
    
    def __init__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class PGDialect_pg8000(PGDialect):
    __module__ = __name__
    __qualname__ = 'PGDialect_pg8000'
    driver = 'pg8000'
    supports_statement_cache = True
    supports_unicode_statements = True
    supports_unicode_binds = True
    default_paramstyle = 'format'
    supports_sane_multi_rowcount = True
    execution_ctx_cls = PGExecutionContext_pg8000
    statement_compiler = PGCompiler_pg8000
    preparer = PGIdentifierPreparer_pg8000
    supports_server_side_cursors = True
    render_bind_cast = True
    description_encoding = None
# WARNING: Decompyle incomplete

dialect = PGDialect_pg8000
