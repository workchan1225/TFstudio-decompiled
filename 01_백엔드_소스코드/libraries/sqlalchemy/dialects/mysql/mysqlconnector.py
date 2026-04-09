# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mysqlconnector.pyc (Python 3.11)

'''
.. dialect:: mysql+mysqlconnector
    :name: MySQL Connector/Python
    :dbapi: myconnpy
    :connectstring: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    :url: https://pypi.org/project/mysql-connector-python/

Driver Status
-------------

MySQL Connector/Python is supported as of SQLAlchemy 2.0.39 to the
degree which the driver is functional.   There are still ongoing issues
with features such as server side cursors which remain disabled until
upstream issues are repaired.

.. warning:: The MySQL Connector/Python driver published by Oracle is subject
   to frequent, major regressions of essential functionality such as being able
   to correctly persist simple binary strings which indicate it is not well
   tested.  The SQLAlchemy project is not able to maintain this dialect fully as
   regressions in the driver prevent it from being included in continuous
   integration.

.. versionchanged:: 2.0.39

    The MySQL Connector/Python dialect has been updated to support the
    latest version of this DBAPI.   Previously, MySQL Connector/Python
    was not fully supported.  However, support remains limited due to ongoing
    regressions introduced in this driver.

Connecting to MariaDB with MySQL Connector/Python
--------------------------------------------------

MySQL Connector/Python may attempt to pass an incompatible collation to the
database when connecting to MariaDB.  Experimentation has shown that using
``?charset=utf8mb4&collation=utfmb4_general_ci`` or similar MariaDB-compatible
charset/collation will allow connectivity.


'''
from __future__ import annotations
import re
from typing import Any
from typing import cast
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from base import MariaDBIdentifierPreparer
from base import MySQLCompiler
from base import MySQLDialect
from base import MySQLExecutionContext
from base import MySQLIdentifierPreparer
from mariadb import MariaDBDialect
from types import BIT
from  import util
if TYPE_CHECKING:
    from engine.base import Connection
    from engine.cursor import CursorResult
    from engine.interfaces import ConnectArgsType
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import IsolationLevel
    from engine.interfaces import PoolProxiedConnection
    from engine.row import Row
    from engine.url import URL
    from sql.elements import BinaryExpression

class MySQLExecutionContext_mysqlconnector(MySQLExecutionContext):
    
    def create_server_side_cursor(self = None):
        return self._dbapi_connection.cursor(buffered = False)

    
    def create_default_cursor(self = None):
        return self._dbapi_connection.cursor(buffered = True)



class MySQLCompiler_mysqlconnector(MySQLCompiler):
    
    def visit_mod_binary(self = None, binary = None, operator = None, **kw):
        pass
    # WARNING: Decompyle incomplete



class IdentifierPreparerCommon_mysqlconnector:
    _double_percents = (lambda self = None: False)()
    _double_percents = (lambda self = None, value = None: pass)()
    
    def _escape_identifier(self = None, value = None):
        value = value.replace(self.escape_quote, self.escape_to_quote)
        return value



class MySQLIdentifierPreparer_mysqlconnector(MySQLIdentifierPreparer, IdentifierPreparerCommon_mysqlconnector):
    pass


class MariaDBIdentifierPreparer_mysqlconnector(MariaDBIdentifierPreparer, IdentifierPreparerCommon_mysqlconnector):
    pass


class _myconnpyBIT(BIT):
    
    def result_processor(self = None, dialect = None, coltype = None):
        '''MySQL-connector already converts mysql bits, so.'''
        pass



class MySQLDialect_mysqlconnector(MySQLDialect):
    pass
# WARNING: Decompyle incomplete


class MariaDBDialect_mysqlconnector(MySQLDialect_mysqlconnector, MariaDBDialect):
    supports_statement_cache = True
    _allows_uuid_binds = False
    preparer = MariaDBIdentifierPreparer_mysqlconnector

dialect = MySQLDialect_mysqlconnector
mariadb_dialect = MariaDBDialect_mysqlconnector
