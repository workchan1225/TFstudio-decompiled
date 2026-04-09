# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cx_oracle.pyc (Python 3.11)

'''.. dialect:: oracle+cx_oracle
    :name: cx-Oracle
    :dbapi: cx_oracle
    :connectstring: oracle+cx_oracle://user:pass@hostname:port[/dbname][?service_name=<service>[&key=value&key=value...]]
    :url: https://oracle.github.io/python-cx_Oracle/

Description
-----------

cx_Oracle was the original driver for Oracle Database. It was superseded by
python-oracledb which should be used instead.

DSN vs. Hostname connections
-----------------------------

cx_Oracle provides several methods of indicating the target database.  The
dialect translates from a series of different URL forms.

Hostname Connections with Easy Connect Syntax
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given a hostname, port and service name of the target database, for example
from Oracle Database\'s Easy Connect syntax then connect in SQLAlchemy using the
``service_name`` query string parameter::

    engine = create_engine(
        "oracle+cx_oracle://scott:tiger@hostname:port?service_name=myservice&encoding=UTF-8&nencoding=UTF-8"
    )

Note that the default driver value for encoding and nencoding was changed to
“UTF-8” in cx_Oracle 8.0 so these parameters can be omitted when using that
version, or later.

To use a full Easy Connect string, pass it as the ``dsn`` key value in a
:paramref:`_sa.create_engine.connect_args` dictionary::

    import cx_Oracle

    e = create_engine(
        "oracle+cx_oracle://@",
        connect_args={
            "user": "scott",
            "password": "tiger",
            "dsn": "hostname:port/myservice?transport_connect_timeout=30&expire_time=60",
        },
    )

Connections with tnsnames.ora or to Oracle Autonomous Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, if no port, database name, or service name is provided, the
dialect will use an Oracle Database DSN "connection string".  This takes the
"hostname" portion of the URL as the data source name.  For example, if the
``tnsnames.ora`` file contains a TNS Alias of ``myalias`` as below:

.. sourcecode:: text

    myalias =
      (DESCRIPTION =
        (ADDRESS = (PROTOCOL = TCP)(HOST = mymachine.example.com)(PORT = 1521))
        (CONNECT_DATA =
          (SERVER = DEDICATED)
          (SERVICE_NAME = orclpdb1)
        )
      )

The cx_Oracle dialect connects to this database service when ``myalias`` is the
hostname portion of the URL, without specifying a port, database name or
``service_name``::

    engine = create_engine("oracle+cx_oracle://scott:tiger@myalias")

Users of Oracle Autonomous Database should use this syntax. If the database is
configured for mutural TLS ("mTLS"), then you must also configure the cloud
wallet as shown in cx_Oracle documentation `Connecting to Autononmous Databases
<https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html#autonomousdb>`_.

SID Connections
^^^^^^^^^^^^^^^

To use Oracle Database\'s obsolete System Identifier connection syntax, the SID
can be passed in a "database name" portion of the URL::

    engine = create_engine(
        "oracle+cx_oracle://scott:tiger@hostname:port/dbname"
    )

Above, the DSN passed to cx_Oracle is created by ``cx_Oracle.makedsn()`` as
follows::

    >>> import cx_Oracle
    >>> cx_Oracle.makedsn("hostname", 1521, sid="dbname")
    \'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=hostname)(PORT=1521))(CONNECT_DATA=(SID=dbname)))\'

Note that although the SQLAlchemy syntax ``hostname:port/dbname`` looks like
Oracle\'s Easy Connect syntax it is different. It uses a SID in place of the
service name required by Easy Connect.  The Easy Connect syntax does not
support SIDs.

Passing cx_Oracle connect arguments
-----------------------------------

Additional connection arguments can usually be passed via the URL query string;
particular symbols like ``SYSDBA`` are intercepted and converted to the correct
symbol::

    e = create_engine(
        "oracle+cx_oracle://user:pass@dsn?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true"
    )

.. versionchanged:: 1.3 the cx_Oracle dialect now accepts all argument names
   within the URL string itself, to be passed to the cx_Oracle DBAPI.   As
   was the case earlier but not correctly documented, the
   :paramref:`_sa.create_engine.connect_args` parameter also accepts all
   cx_Oracle DBAPI connect arguments.

To pass arguments directly to ``.connect()`` without using the query
string, use the :paramref:`_sa.create_engine.connect_args` dictionary.
Any cx_Oracle parameter value and/or constant may be passed, such as::

    import cx_Oracle

    e = create_engine(
        "oracle+cx_oracle://user:pass@dsn",
        connect_args={
            "encoding": "UTF-8",
            "nencoding": "UTF-8",
            "mode": cx_Oracle.SYSDBA,
            "events": True,
        },
    )

Note that the default driver value for ``encoding`` and ``nencoding`` was
changed to "UTF-8" in cx_Oracle 8.0 so these parameters can be omitted when
using that version, or later.

Options consumed by the SQLAlchemy cx_Oracle dialect outside of the driver
--------------------------------------------------------------------------

There are also options that are consumed by the SQLAlchemy cx_oracle dialect
itself.  These options are always passed directly to :func:`_sa.create_engine`
, such as::

    e = create_engine(
        "oracle+cx_oracle://user:pass@dsn", coerce_to_decimal=False
    )

The parameters accepted by the cx_oracle dialect are as follows:

* ``arraysize`` - set the cx_oracle.arraysize value on cursors; defaults
  to ``None``, indicating that the driver default should be used (typically
  the value is 100).  This setting controls how many rows are buffered when
  fetching rows, and can have a significant effect on performance when
  modified.

  .. versionchanged:: 2.0.26 - changed the default value from 50 to None,
    to use the default value of the driver itself.

* ``auto_convert_lobs`` - defaults to True; See :ref:`cx_oracle_lob`.

* ``coerce_to_decimal`` - see :ref:`cx_oracle_numeric` for detail.

* ``encoding_errors`` - see :ref:`cx_oracle_unicode_encoding_errors` for detail.

.. _cx_oracle_sessionpool:

Using cx_Oracle SessionPool
---------------------------

The cx_Oracle driver provides its own connection pool implementation that may
be used in place of SQLAlchemy\'s pooling functionality. The driver pool
supports Oracle Database features such dead connection detection, connection
draining for planned database downtime, support for Oracle Application
Continuity and Transparent Application Continuity, and gives support for
Database Resident Connection Pooling (DRCP).

Using the driver pool can be achieved by using the
:paramref:`_sa.create_engine.creator` parameter to provide a function that
returns a new connection, along with setting
:paramref:`_sa.create_engine.pool_class` to ``NullPool`` to disable
SQLAlchemy\'s pooling::

    import cx_Oracle
    from sqlalchemy import create_engine
    from sqlalchemy.pool import NullPool

    pool = cx_Oracle.SessionPool(
        user="scott",
        password="tiger",
        dsn="orclpdb",
        min=1,
        max=4,
        increment=1,
        threaded=True,
        encoding="UTF-8",
        nencoding="UTF-8",
    )

    engine = create_engine(
        "oracle+cx_oracle://", creator=pool.acquire, poolclass=NullPool
    )

The above engine may then be used normally where cx_Oracle\'s pool handles
connection pooling::

    with engine.connect() as conn:
        print(conn.scalar("select 1 from dual"))

As well as providing a scalable solution for multi-user applications, the
cx_Oracle session pool supports some Oracle features such as DRCP and
`Application Continuity
<https://cx-oracle.readthedocs.io/en/latest/user_guide/ha.html#application-continuity-ac>`_.

Note that the pool creation parameters ``threaded``, ``encoding`` and
``nencoding`` were deprecated in later cx_Oracle releases.

Using Oracle Database Resident Connection Pooling (DRCP)
--------------------------------------------------------

When using Oracle Database\'s DRCP, the best practice is to pass a connection
class and "purity" when acquiring a connection from the SessionPool.  Refer to
the `cx_Oracle DRCP documentation
<https://cx-oracle.readthedocs.io/en/latest/user_guide/connection_handling.html#database-resident-connection-pooling-drcp>`_.

This can be achieved by wrapping ``pool.acquire()``::

    import cx_Oracle
    from sqlalchemy import create_engine
    from sqlalchemy.pool import NullPool

    pool = cx_Oracle.SessionPool(
        user="scott",
        password="tiger",
        dsn="orclpdb",
        min=2,
        max=5,
        increment=1,
        threaded=True,
        encoding="UTF-8",
        nencoding="UTF-8",
    )


    def creator():
        return pool.acquire(
            cclass="MYCLASS", purity=cx_Oracle.ATTR_PURITY_SELF
        )


    engine = create_engine(
        "oracle+cx_oracle://", creator=creator, poolclass=NullPool
    )

The above engine may then be used normally where cx_Oracle handles session
pooling and Oracle Database additionally uses DRCP::

    with engine.connect() as conn:
        print(conn.scalar("select 1 from dual"))

.. _cx_oracle_unicode:

Unicode
-------

As is the case for all DBAPIs under Python 3, all strings are inherently
Unicode strings. In all cases however, the driver requires an explicit
encoding configuration.

Ensuring the Correct Client Encoding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The long accepted standard for establishing client encoding for nearly all
Oracle Database related software is via the `NLS_LANG
<https://www.oracle.com/database/technologies/faq-nls-lang.html>`_ environment
variable.  Older versions of cx_Oracle use this environment variable as the
source of its encoding configuration.  The format of this variable is
Territory_Country.CharacterSet; a typical value would be
``AMERICAN_AMERICA.AL32UTF8``.  cx_Oracle version 8 and later use the character
set "UTF-8" by default, and ignore the character set component of NLS_LANG.

The cx_Oracle driver also supported a programmatic alternative which is to pass
the ``encoding`` and ``nencoding`` parameters directly to its ``.connect()``
function.  These can be present in the URL as follows::

    engine = create_engine(
        "oracle+cx_oracle://scott:tiger@tnsalias?encoding=UTF-8&nencoding=UTF-8"
    )

For the meaning of the ``encoding`` and ``nencoding`` parameters, please
consult
`Characters Sets and National Language Support (NLS) <https://cx-oracle.readthedocs.io/en/latest/user_guide/globalization.html#globalization>`_.

.. seealso::

    `Characters Sets and National Language Support (NLS) <https://cx-oracle.readthedocs.io/en/latest/user_guide/globalization.html#globalization>`_
    - in the cx_Oracle documentation.


Unicode-specific Column datatypes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Core expression language handles unicode data by use of the
:class:`.Unicode` and :class:`.UnicodeText` datatypes.  These types correspond
to the VARCHAR2 and CLOB Oracle Database datatypes by default.  When using
these datatypes with Unicode data, it is expected that the database is
configured with a Unicode-aware character set, as well as that the ``NLS_LANG``
environment variable is set appropriately (this applies to older versions of
cx_Oracle), so that the VARCHAR2 and CLOB datatypes can accommodate the data.

In the case that Oracle Database is not configured with a Unicode character
set, the two options are to use the :class:`_types.NCHAR` and
:class:`_oracle.NCLOB` datatypes explicitly, or to pass the flag
``use_nchar_for_unicode=True`` to :func:`_sa.create_engine`, which will cause
the SQLAlchemy dialect to use NCHAR/NCLOB for the :class:`.Unicode` /
:class:`.UnicodeText` datatypes instead of VARCHAR/CLOB.

.. versionchanged:: 1.3 The :class:`.Unicode` and :class:`.UnicodeText`
   datatypes now correspond to the ``VARCHAR2`` and ``CLOB`` Oracle Database
   datatypes unless the ``use_nchar_for_unicode=True`` is passed to the dialect
   when :func:`_sa.create_engine` is called.


.. _cx_oracle_unicode_encoding_errors:

Encoding Errors
^^^^^^^^^^^^^^^

For the unusual case that data in Oracle Database is present with a broken
encoding, the dialect accepts a parameter ``encoding_errors`` which will be
passed to Unicode decoding functions in order to affect how decoding errors are
handled.  The value is ultimately consumed by the Python `decode
<https://docs.python.org/3/library/stdtypes.html#bytes.decode>`_ function, and
is passed both via cx_Oracle\'s ``encodingErrors`` parameter consumed by
``Cursor.var()``, as well as SQLAlchemy\'s own decoding function, as the
cx_Oracle dialect makes use of both under different circumstances.

.. versionadded:: 1.3.11


.. _cx_oracle_setinputsizes:

Fine grained control over cx_Oracle data binding performance with setinputsizes
-------------------------------------------------------------------------------

The cx_Oracle DBAPI has a deep and fundamental reliance upon the usage of the
DBAPI ``setinputsizes()`` call.  The purpose of this call is to establish the
datatypes that are bound to a SQL statement for Python values being passed as
parameters.  While virtually no other DBAPI assigns any use to the
``setinputsizes()`` call, the cx_Oracle DBAPI relies upon it heavily in its
interactions with the Oracle Database client interface, and in some scenarios
it is not possible for SQLAlchemy to know exactly how data should be bound, as
some settings can cause profoundly different performance characteristics, while
altering the type coercion behavior at the same time.

Users of the cx_Oracle dialect are **strongly encouraged** to read through
cx_Oracle\'s list of built-in datatype symbols at
https://cx-oracle.readthedocs.io/en/latest/api_manual/module.html#database-types.
Note that in some cases, significant performance degradation can occur when
using these types vs. not, in particular when specifying ``cx_Oracle.CLOB``.

On the SQLAlchemy side, the :meth:`.DialectEvents.do_setinputsizes` event can
be used both for runtime visibility (e.g. logging) of the setinputsizes step as
well as to fully control how ``setinputsizes()`` is used on a per-statement
basis.

.. versionadded:: 1.2.9 Added :meth:`.DialectEvents.setinputsizes`


Example 1 - logging all setinputsizes calls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example illustrates how to log the intermediary values from a
SQLAlchemy perspective before they are converted to the raw ``setinputsizes()``
parameter dictionary.  The keys of the dictionary are :class:`.BindParameter`
objects which have a ``.key`` and a ``.type`` attribute::

    from sqlalchemy import create_engine, event

    engine = create_engine("oracle+cx_oracle://scott:tiger@host/xe")


    @event.listens_for(engine, "do_setinputsizes")
    def _log_setinputsizes(inputsizes, cursor, statement, parameters, context):
        for bindparam, dbapitype in inputsizes.items():
            log.info(
                "Bound parameter name: %s  SQLAlchemy type: %r DBAPI object: %s",
                bindparam.key,
                bindparam.type,
                dbapitype,
            )

Example 2 - remove all bindings to CLOB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``CLOB`` datatype in cx_Oracle incurs a significant performance overhead,
however is set by default for the ``Text`` type within the SQLAlchemy 1.2
series.   This setting can be modified as follows::

    from sqlalchemy import create_engine, event
    from cx_Oracle import CLOB

    engine = create_engine("oracle+cx_oracle://scott:tiger@host/xe")


    @event.listens_for(engine, "do_setinputsizes")
    def _remove_clob(inputsizes, cursor, statement, parameters, context):
        for bindparam, dbapitype in list(inputsizes.items()):
            if dbapitype is CLOB:
                del inputsizes[bindparam]

.. _cx_oracle_lob:

LOB Datatypes
--------------

LOB datatypes refer to the "large object" datatypes such as CLOB, NCLOB and
BLOB. Modern versions of cx_Oracle is optimized for these datatypes to be
delivered as a single buffer. As such, SQLAlchemy makes use of these newer type
handlers by default.

To disable the use of newer type handlers and deliver LOB objects as classic
buffered objects with a ``read()`` method, the parameter
``auto_convert_lobs=False`` may be passed to :func:`_sa.create_engine`,
which takes place only engine-wide.

.. _cx_oracle_returning:

RETURNING Support
-----------------

The cx_Oracle dialect implements RETURNING using OUT parameters.
The dialect supports RETURNING fully.

Two Phase Transactions Not Supported
------------------------------------

Two phase transactions are **not supported** under cx_Oracle due to poor driver
support. The newer :ref:`oracledb` dialect however **does** support two phase
transactions.

.. _cx_oracle_numeric:

Precision Numerics
------------------

SQLAlchemy\'s numeric types can handle receiving and returning values as Python
``Decimal`` objects or float objects.  When a :class:`.Numeric` object, or a
subclass such as :class:`.Float`, :class:`_oracle.DOUBLE_PRECISION` etc. is in
use, the :paramref:`.Numeric.asdecimal` flag determines if values should be
coerced to ``Decimal`` upon return, or returned as float objects.  To make
matters more complicated under Oracle Database, the ``NUMBER`` type can also
represent integer values if the "scale" is zero, so the Oracle
Database-specific :class:`_oracle.NUMBER` type takes this into account as well.

The cx_Oracle dialect makes extensive use of connection- and cursor-level
"outputtypehandler" callables in order to coerce numeric values as requested.
These callables are specific to the specific flavor of :class:`.Numeric` in
use, as well as if no SQLAlchemy typing objects are present.  There are
observed scenarios where Oracle Database may send incomplete or ambiguous
information about the numeric types being returned, such as a query where the
numeric types are buried under multiple levels of subquery.  The type handlers
do their best to make the right decision in all cases, deferring to the
underlying cx_Oracle DBAPI for all those cases where the driver can make the
best decision.

When no typing objects are present, as when executing plain SQL strings, a
default "outputtypehandler" is present which will generally return numeric
values which specify precision and scale as Python ``Decimal`` objects.  To
disable this coercion to decimal for performance reasons, pass the flag
``coerce_to_decimal=False`` to :func:`_sa.create_engine`::

    engine = create_engine("oracle+cx_oracle://dsn", coerce_to_decimal=False)

The ``coerce_to_decimal`` flag only impacts the results of plain string
SQL statements that are not otherwise associated with a :class:`.Numeric`
SQLAlchemy type (or a subclass of such).

.. versionchanged:: 1.2  The numeric handling system for cx_Oracle has been
   reworked to take advantage of newer cx_Oracle features as well
   as better integration of outputtypehandlers.

'''
from __future__ import annotations
import decimal
import random
import re
from  import base as oracle
from base import OracleCompiler
from base import OracleDialect
from base import OracleExecutionContext
from types import _OracleDateLiteralRender
from  import exc
from  import util
from engine import cursor as _cursor
from engine import interfaces
from engine import processors
from sql import sqltypes
from sql._typing import is_sql_compiler
_CX_ORACLE_MAGIC_LOB_SIZE = 131072

class _OracleInteger(sqltypes.Integer):
    
    def get_dbapi_type(self, dbapi):
        return int

    
    def _cx_oracle_var(self, dialect, cursor, arraysize = (None,)):
        cx_Oracle = dialect.dbapi
    # WARNING: Decompyle incomplete

    
    def _cx_oracle_outputtypehandler(self, dialect):
        pass
    # WARNING: Decompyle incomplete



class _OracleNumeric(sqltypes.Numeric):
    is_number = False
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def result_processor(self, dialect, coltype):
        pass

    
    def _cx_oracle_outputtypehandler(self, dialect):
        pass
    # WARNING: Decompyle incomplete



class _OracleUUID(sqltypes.Uuid):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.STRING



class _OracleBinaryFloat(_OracleNumeric):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.NATIVE_FLOAT



class _OracleBINARY_FLOAT(oracle.BINARY_FLOAT, _OracleBinaryFloat):
    pass


class _OracleBINARY_DOUBLE(oracle.BINARY_DOUBLE, _OracleBinaryFloat):
    pass


class _OracleNUMBER(_OracleNumeric):
    is_number = True


class _CXOracleDate(oracle._OracleDate):
    
    def bind_processor(self, dialect):
        pass

    
    def result_processor(self, dialect, coltype):
        
        def process(value):
            pass
        # WARNING: Decompyle incomplete

        return process



class _CXOracleTIMESTAMP(sqltypes.TIMESTAMP, _OracleDateLiteralRender):
    
    def literal_processor(self, dialect):
        return self._literal_processor_datetime(dialect)



class _LOBDataType:
    pass


class _OracleChar(sqltypes.CHAR):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.FIXED_CHAR



class _OracleNChar(sqltypes.NCHAR):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.FIXED_NCHAR



class _OracleUnicodeStringNCHAR(oracle.NVARCHAR2):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.NCHAR



class _OracleUnicodeStringCHAR(sqltypes.Unicode):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.LONG_STRING



class _OracleUnicodeTextNCLOB(oracle.NCLOB, _LOBDataType):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.DB_TYPE_NVARCHAR



class _OracleUnicodeTextCLOB(sqltypes.UnicodeText, _LOBDataType):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.DB_TYPE_NVARCHAR



class _OracleText(sqltypes.Text, _LOBDataType):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.DB_TYPE_NVARCHAR



class _OracleLong(oracle.LONG, _LOBDataType):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.LONG_STRING



class _OracleString(sqltypes.String):
    pass


class _OracleEnum(sqltypes.Enum):
    
    def bind_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete



class _OracleBinary(sqltypes.LargeBinary, _LOBDataType):
    pass
# WARNING: Decompyle incomplete


class _OracleInterval(oracle.INTERVAL):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.INTERVAL



class _OracleRaw(oracle.RAW):
    pass


class _OracleRowid(oracle.ROWID):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.ROWID



class OracleCompiler_cx_oracle(OracleCompiler):
    _oracle_cx_sql_compiler = True
    _oracle_returning = False
    bindname_escape_characters = util.immutabledict({
        '%': 'P',
        '(': 'A',
        ')': 'Z',
        ':': 'C',
        '.': 'C',
        '[': 'C',
        ']': 'C',
        ' ': 'C',
        '\\': 'C',
        '/': 'C',
        '?': 'C' })
    
    def bindparam_string(self, name, **kw):
        pass
    # WARNING: Decompyle incomplete



class OracleExecutionContext_cx_oracle(OracleExecutionContext):
    pass
# WARNING: Decompyle incomplete


class OracleDialect_cx_oracle(OracleDialect):
    pass
# WARNING: Decompyle incomplete

dialect = OracleDialect_cx_oracle
