# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pyodbc.pyc (Python 3.11)

'''

.. dialect:: mysql+pyodbc
    :name: PyODBC
    :dbapi: pyodbc
    :connectstring: mysql+pyodbc://<username>:<password>@<dsnname>
    :url: https://pypi.org/project/pyodbc/

.. note::

    The PyODBC for MySQL dialect is **not tested as part of
    SQLAlchemy\'s continuous integration**.
    The recommended MySQL dialects are mysqlclient and PyMySQL.
    However, if you want to use the mysql+pyodbc dialect and require
    full support for ``utf8mb4`` characters (including supplementary
    characters like emoji) be sure to use a current release of
    MySQL Connector/ODBC and specify the "ANSI" (**not** "Unicode")
    version of the driver in your DSN or connection string.

Pass through exact pyodbc connection string::

    import urllib

    connection_string = (
        "DRIVER=MySQL ODBC 8.0 ANSI Driver;"
        "SERVER=localhost;"
        "PORT=3307;"
        "DATABASE=mydb;"
        "UID=root;"
        "PWD=(whatever);"
        "charset=utf8mb4;"
    )
    params = urllib.parse.quote_plus(connection_string)
    connection_uri = "mysql+pyodbc:///?odbc_connect=%s" % params

'''
from __future__ import annotations
import datetime
import re
from typing import Any
from typing import Callable
from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from base import MySQLDialect
from base import MySQLExecutionContext
from types import TIME
from  import exc
from  import util
from connectors.pyodbc import PyODBCConnector
from sql.sqltypes import Time
if TYPE_CHECKING:
    from engine import Connection
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import Dialect
    from sql.type_api import _ResultProcessorType

class _pyodbcTIME(TIME):
    
    def result_processor(self = None, dialect = None, coltype = None):
        
        def process(value = None):
            return value

        return process



class MySQLExecutionContext_pyodbc(MySQLExecutionContext):
    
    def get_lastrowid(self = None):
        cursor = self.create_cursor()
        cursor.execute('SELECT LAST_INSERT_ID()')
        lastrowid = cursor.fetchone()[0]
        cursor.close()
        return lastrowid



class MySQLDialect_pyodbc(MySQLDialect, PyODBCConnector):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_pyodbc
