# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cymysql.pyc (Python 3.11)

"""

.. dialect:: mysql+cymysql
    :name: CyMySQL
    :dbapi: cymysql
    :connectstring: mysql+cymysql://<username>:<password>@<host>/<dbname>[?<options>]
    :url: https://github.com/nakagami/CyMySQL

.. note::

    The CyMySQL dialect is **not tested as part of SQLAlchemy's continuous
    integration** and may have unresolved issues.  The recommended MySQL
    dialects are mysqlclient and PyMySQL.

"""
from __future__ import annotations
from typing import Any
from typing import Iterable
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from base import MySQLDialect
from mysqldb import MySQLDialect_mysqldb
from types import BIT
from  import util
if TYPE_CHECKING:
    from engine.base import Connection
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import Dialect
    from engine.interfaces import PoolProxiedConnection
    from sql.type_api import _ResultProcessorType

class _cymysqlBIT(BIT):
    
    def result_processor(self = None, dialect = None, coltype = None):
        """Convert MySQL's 64 bit, variable length binary string to a long."""
        
        def process(value = None):
            pass
        # WARNING: Decompyle incomplete

        return process



class MySQLDialect_cymysql(MySQLDialect_mysqldb):
    driver = 'cymysql'
    supports_statement_cache = True
    description_encoding = None
    supports_sane_rowcount = True
    supports_sane_multi_rowcount = False
    supports_unicode_statements = True
    colspecs = util.update_copy(MySQLDialect.colspecs, {
        BIT: _cymysqlBIT })
    import_dbapi = (lambda cls = None: __import__('cymysql'))()
    
    def _detect_charset(self = None, connection = None):
        return connection.connection.charset

    
    def _extract_error_code(self = None, exception = None):
        return exception.errno

    
    def is_disconnect(self = None, e = None, connection = None, cursor = ('e', 'DBAPIModule.Error', 'connection', 'Optional[Union[PoolProxiedConnection, DBAPIConnection]]', 'cursor', 'Optional[DBAPICursor]', 'return', 'bool')):
        if isinstance(e, self.loaded_dbapi.OperationalError):
            return self._extract_error_code(e) in (2006, 2013, 2014, 2045, 2055)
        if None(e, self.loaded_dbapi.InterfaceError):
            return True


dialect = MySQLDialect_cymysql
