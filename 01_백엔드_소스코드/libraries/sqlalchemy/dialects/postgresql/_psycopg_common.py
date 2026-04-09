# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _psycopg_common.pyc (Python 3.11)

from __future__ import annotations
import decimal
from array import ARRAY as PGARRAY
from base import _DECIMAL_TYPES
from base import _FLOAT_TYPES
from base import _INT_TYPES
from base import PGDialect
from base import PGExecutionContext
from hstore import HSTORE
from pg_catalog import _SpaceVector
from pg_catalog import INT2VECTOR
from pg_catalog import OIDVECTOR
from  import exc
from  import types as sqltypes
from  import util
from engine import processors
_server_side_id = util.counter()

class _PsycopgNumeric(sqltypes.Numeric):
    
    def bind_processor(self, dialect):
        pass

    
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



class _PsycopgFloat(_PsycopgNumeric):
    __visit_name__ = 'float'


class _PsycopgHStore(HSTORE):
    pass
# WARNING: Decompyle incomplete


class _PsycopgARRAY(PGARRAY):
    render_bind_cast = True


class _PsycopgINT2VECTOR(INT2VECTOR, _SpaceVector):
    pass


class _PsycopgOIDVECTOR(OIDVECTOR, _SpaceVector):
    pass


class _PGExecutionContext_common_psycopg(PGExecutionContext):
    
    def create_server_side_cursor(self):
        ident = f'''c_{hex(id(self))[2:]!s}_{hex(_server_side_id())[2:]!s}'''
        return self._dbapi_connection.cursor(ident)



class _PGDialect_common_psycopg(PGDialect):
    supports_statement_cache = True
    supports_server_side_cursors = True
    default_paramstyle = 'pyformat'
    _has_native_hstore = True
    colspecs = util.update_copy(PGDialect.colspecs, {
        OIDVECTOR: _PsycopgOIDVECTOR,
        INT2VECTOR: _PsycopgINT2VECTOR,
        sqltypes.ARRAY: _PsycopgARRAY,
        HSTORE: _PsycopgHStore,
        sqltypes.Float: _PsycopgFloat,
        sqltypes.Numeric: _PsycopgNumeric })
    
    def __init__(self, client_encoding, use_native_hstore = (None, True), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def create_connect_args(self, url):
        opts = url.translate_connect_args(username = 'user', database = 'dbname')
        (multihosts, multiports) = self._split_multihost_from_url(url)
        if opts or url.query:
            if not opts:
                opts = { }
            if 'port' in opts:
                opts['port'] = int(opts['port'])
            opts.update(url.query)
            if multihosts:
                opts['host'] = ','.join(multihosts)
                comma_ports = (lambda .0: pass# WARNING: Decompyle incomplete
)(multiports())
                if comma_ports:
                    opts['port'] = comma_ports
            return ([], opts)
        return ([
            None], opts)

    
    def get_isolation_level_values(self, dbapi_connection):
        return ('AUTOCOMMIT', 'READ COMMITTED', 'READ UNCOMMITTED', 'REPEATABLE READ', 'SERIALIZABLE')

    
    def set_deferrable(self, connection, value):
        connection.deferrable = value

    
    def get_deferrable(self, connection):
        return connection.deferrable

    
    def _do_autocommit(self, connection, value):
        connection.autocommit = value

    
    def detect_autocommit_setting(self, dbapi_connection):
        return bool(dbapi_connection.autocommit)

    
    def do_ping(self, dbapi_connection):
        before_autocommit = dbapi_connection.autocommit
        if not before_autocommit:
            dbapi_connection.autocommit = True
        cursor = dbapi_connection.cursor()
        
        try:
            cursor.execute(self._dialect_specific_select_one)
            cursor.close()

        return True
