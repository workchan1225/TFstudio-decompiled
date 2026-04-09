# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mariadbconnector.pyc (Python 3.11)

'''

.. dialect:: mysql+mariadbconnector
    :name: MariaDB Connector/Python
    :dbapi: mariadb
    :connectstring: mariadb+mariadbconnector://<user>:<password>@<host>[:<port>]/<dbname>
    :url: https://pypi.org/project/mariadb/

Driver Status
-------------

MariaDB Connector/Python enables Python programs to access MariaDB and MySQL
databases using an API which is compliant with the Python DB API 2.0 (PEP-249).
It is written in C and uses MariaDB Connector/C client library for client server
communication.

Note that the default driver for a ``mariadb://`` connection URI continues to
be ``mysqldb``. ``mariadb+mariadbconnector://`` is required to use this driver.

.. mariadb: https://github.com/mariadb-corporation/mariadb-connector-python

'''
from __future__ import annotations
import re
from typing import Any
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from uuid import UUID as _python_UUID
from base import MySQLCompiler
from base import MySQLDialect
from base import MySQLExecutionContext
from  import sql
from  import util
from sql import sqltypes
if TYPE_CHECKING:
    from engine.base import Connection
    from engine.interfaces import ConnectArgsType
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import Dialect
    from engine.interfaces import IsolationLevel
    from engine.interfaces import PoolProxiedConnection
    from engine.url import URL
    from sql.compiler import SQLCompiler
    from sql.type_api import _ResultProcessorType
mariadb_cpy_minimum_version = (1, 0, 1)

def _MariaDBUUID():
    '''_MariaDBUUID'''
    
    def result_processor(self = None, dialect = None, coltype = None):
        if self.as_uuid:
            
            def process(value = None):
                pass
            # WARNING: Decompyle incomplete

            return process
        
        def process(value = None):
            pass
        # WARNING: Decompyle incomplete

        return process


_MariaDBUUID = <NODE:27>(_MariaDBUUID, '_MariaDBUUID', sqltypes.UUID[sqltypes._UUID_RETURN])

class MySQLExecutionContext_mariadbconnector(MySQLExecutionContext):
    pass
# WARNING: Decompyle incomplete


class MySQLCompiler_mariadbconnector(MySQLCompiler):
    pass


class MySQLDialect_mariadbconnector(MySQLDialect):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_mariadbconnector
