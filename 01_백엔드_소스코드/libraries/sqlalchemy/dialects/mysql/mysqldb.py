# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mysqldb.pyc (Python 3.11)

'''

.. dialect:: mysql+mysqldb
    :name: mysqlclient (maintained fork of MySQL-Python)
    :dbapi: mysqldb
    :connectstring: mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    :url: https://pypi.org/project/mysqlclient/

Driver Status
-------------

The mysqlclient DBAPI is a maintained fork of the
`MySQL-Python <https://sourceforge.net/projects/mysql-python>`_ DBAPI
that is no longer maintained.  `mysqlclient`_ supports Python 2 and Python 3
and is very stable.

.. _mysqlclient: https://github.com/PyMySQL/mysqlclient-python

.. _mysqldb_unicode:

Unicode
-------

Please see :ref:`mysql_unicode` for current recommendations on unicode
handling.

.. _mysqldb_ssl:

SSL Connections
----------------

The mysqlclient and PyMySQL DBAPIs accept an additional dictionary under the
key "ssl", which may be specified using the
:paramref:`_sa.create_engine.connect_args` dictionary::

    engine = create_engine(
        "mysql+mysqldb://scott:tiger@192.168.0.134/test",
        connect_args={
            "ssl": {
                "ca": "/home/gord/client-ssl/ca.pem",
                "cert": "/home/gord/client-ssl/client-cert.pem",
                "key": "/home/gord/client-ssl/client-key.pem",
            }
        },
    )

For convenience, the following keys may also be specified inline within the URL
where they will be interpreted into the "ssl" dictionary automatically:
"ssl_ca", "ssl_cert", "ssl_key", "ssl_capath", "ssl_cipher",
"ssl_check_hostname". An example is as follows::

    connection_uri = (
        "mysql+mysqldb://scott:tiger@192.168.0.134/test"
        "?ssl_ca=/home/gord/client-ssl/ca.pem"
        "&ssl_cert=/home/gord/client-ssl/client-cert.pem"
        "&ssl_key=/home/gord/client-ssl/client-key.pem"
    )

.. seealso::

    :ref:`pymysql_ssl` in the PyMySQL dialect


Using MySQLdb with Google Cloud SQL
-----------------------------------

Google Cloud SQL now recommends use of the MySQLdb dialect.  Connect
using a URL like the following:

.. sourcecode:: text

    mysql+mysqldb://root@/<dbname>?unix_socket=/cloudsql/<projectid>:<instancename>

Server Side Cursors
-------------------

The mysqldb dialect supports server-side cursors. See :ref:`mysql_ss_cursors`.

'''
from __future__ import annotations
import re
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING
from base import MySQLCompiler
from base import MySQLDialect
from base import MySQLExecutionContext
from base import MySQLIdentifierPreparer
from  import util
from util.typing import Literal
if TYPE_CHECKING:
    from engine.base import Connection
    from engine.interfaces import _DBAPIMultiExecuteParams
    from engine.interfaces import ConnectArgsType
    from engine.interfaces import DBAPIConnection
    from engine.interfaces import DBAPICursor
    from engine.interfaces import DBAPIModule
    from engine.interfaces import ExecutionContext
    from engine.interfaces import IsolationLevel
    from engine.url import URL

class MySQLExecutionContext_mysqldb(MySQLExecutionContext):
    pass


class MySQLCompiler_mysqldb(MySQLCompiler):
    pass


class MySQLDialect_mysqldb(MySQLDialect):
    pass
# WARNING: Decompyle incomplete

dialect = MySQLDialect_mysqldb
