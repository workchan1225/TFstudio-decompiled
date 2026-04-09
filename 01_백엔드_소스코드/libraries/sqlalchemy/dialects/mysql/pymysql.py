# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pymysql.pyc (Python 3.11)

'''

.. dialect:: mysql+pymysql
    :name: PyMySQL
    :dbapi: pymysql
    :connectstring: mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    :url: https://pymysql.readthedocs.io/

Unicode
-------

Please see :ref:`mysql_unicode` for current recommendations on unicode
handling.

.. _pymysql_ssl:

SSL Connections
------------------

The PyMySQL DBAPI accepts the same SSL arguments as that of MySQLdb,
described at :ref:`mysqldb_ssl`.   See that section for additional examples.

If the server uses an automatically-generated certificate that is self-signed
or does not match the host name (as seen from the client), it may also be
necessary to indicate ``ssl_check_hostname=false`` in PyMySQL::

    connection_uri = (
        "mysql+pymysql://scott:tiger@192.168.0.134/test"
        "?ssl_ca=/home/gord/client-ssl/ca.pem"
        "&ssl_cert=/home/gord/client-ssl/client-cert.pem"
        "&ssl_key=/home/gord/client-ssl/client-key.pem"
        "&ssl_check_hostname=false"
    )

MySQL-Python Compatibility
--------------------------

The pymysql DBAPI is a pure Python port of the MySQL-python (MySQLdb) driver,
and targets 100% compatibility.   Most behavioral notes for MySQL-python apply
to the pymysql driver as well.

'''
from __future__ import annotations
from typing import Any
from typing import Dict
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from mysqldb import MySQLDialect_mysqldb
from util import langhelpers
from util.typing import Literal
if TYPE_CHECKING:
    from engine.interfaces import ConnectArgsType
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import PoolProxiedConnection
    from engine.url import URL

class MySQLDialect_pymysql(MySQLDialect_mysqldb):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_pymysql
