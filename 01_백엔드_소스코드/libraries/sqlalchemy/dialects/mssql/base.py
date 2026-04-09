# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

__doc__ = '\n.. dialect:: mssql\n    :name: Microsoft SQL Server\n    :normal_support: 2012+\n    :best_effort: 2005+\n\n.. _mssql_external_dialects:\n\nExternal Dialects\n-----------------\n\nIn addition to the above DBAPI layers with native SQLAlchemy support, there\nare third-party dialects for other DBAPI layers that are compatible\nwith SQL Server. See the "External Dialects" list on the\n:ref:`dialect_toplevel` page.\n\n.. _mssql_identity:\n\nAuto Increment Behavior / IDENTITY Columns\n------------------------------------------\n\nSQL Server provides so-called "auto incrementing" behavior using the\n``IDENTITY`` construct, which can be placed on any single integer column in a\ntable. SQLAlchemy considers ``IDENTITY`` within its default "autoincrement"\nbehavior for an integer primary key column, described at\n:paramref:`_schema.Column.autoincrement`.  This means that by default,\nthe first integer primary key column in a :class:`_schema.Table` will be\nconsidered to be the identity column - unless it is associated with a\n:class:`.Sequence` - and will generate DDL as such::\n\n    from sqlalchemy import Table, MetaData, Column, Integer\n\n    m = MetaData()\n    t = Table(\n        "t",\n        m,\n        Column("id", Integer, primary_key=True),\n        Column("x", Integer),\n    )\n    m.create_all(engine)\n\nThe above example will generate DDL as:\n\n.. sourcecode:: sql\n\n    CREATE TABLE t (\n        id INTEGER NOT NULL IDENTITY,\n        x INTEGER NULL,\n        PRIMARY KEY (id)\n    )\n\nFor the case where this default generation of ``IDENTITY`` is not desired,\nspecify ``False`` for the :paramref:`_schema.Column.autoincrement` flag,\non the first integer primary key column::\n\n    m = MetaData()\n    t = Table(\n        "t",\n        m,\n        Column("id", Integer, primary_key=True, autoincrement=False),\n        Column("x", Integer),\n    )\n    m.create_all(engine)\n\nTo add the ``IDENTITY`` keyword to a non-primary key column, specify\n``True`` for the :paramref:`_schema.Column.autoincrement` flag on the desired\n:class:`_schema.Column` object, and ensure that\n:paramref:`_schema.Column.autoincrement`\nis set to ``False`` on any integer primary key column::\n\n    m = MetaData()\n    t = Table(\n        "t",\n        m,\n        Column("id", Integer, primary_key=True, autoincrement=False),\n        Column("x", Integer, autoincrement=True),\n    )\n    m.create_all(engine)\n\n.. versionchanged::  1.4   Added :class:`_schema.Identity` construct\n   in a :class:`_schema.Column` to specify the start and increment\n   parameters of an IDENTITY. These replace\n   the use of the :class:`.Sequence` object in order to specify these values.\n\n.. deprecated:: 1.4\n\n   The ``mssql_identity_start`` and ``mssql_identity_increment`` parameters\n   to :class:`_schema.Column` are deprecated and should we replaced by\n   an :class:`_schema.Identity` object. Specifying both ways of configuring\n   an IDENTITY will result in a compile error.\n   These options are also no longer returned as part of the\n   ``dialect_options`` key in :meth:`_reflection.Inspector.get_columns`.\n   Use the information in the ``identity`` key instead.\n\n.. deprecated:: 1.3\n\n   The use of :class:`.Sequence` to specify IDENTITY characteristics is\n   deprecated and will be removed in a future release.   Please use\n   the :class:`_schema.Identity` object parameters\n   :paramref:`_schema.Identity.start` and\n   :paramref:`_schema.Identity.increment`.\n\n.. versionchanged::  1.4   Removed the ability to use a :class:`.Sequence`\n   object to modify IDENTITY characteristics. :class:`.Sequence` objects\n   now only manipulate true T-SQL SEQUENCE types.\n\n.. note::\n\n    There can only be one IDENTITY column on the table.  When using\n    ``autoincrement=True`` to enable the IDENTITY keyword, SQLAlchemy does not\n    guard against multiple columns specifying the option simultaneously.  The\n    SQL Server database will instead reject the ``CREATE TABLE`` statement.\n\n.. note::\n\n    An INSERT statement which attempts to provide a value for a column that is\n    marked with IDENTITY will be rejected by SQL Server.   In order for the\n    value to be accepted, a session-level option "SET IDENTITY_INSERT" must be\n    enabled.   The SQLAlchemy SQL Server dialect will perform this operation\n    automatically when using a core :class:`_expression.Insert`\n    construct; if the\n    execution specifies a value for the IDENTITY column, the "IDENTITY_INSERT"\n    option will be enabled for the span of that statement\'s invocation.However,\n    this scenario is not high performing and should not be relied upon for\n    normal use.   If a table doesn\'t actually require IDENTITY behavior in its\n    integer primary key column, the keyword should be disabled when creating\n    the table by ensuring that ``autoincrement=False`` is set.\n\nControlling "Start" and "Increment"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nSpecific control over the "start" and "increment" values for\nthe ``IDENTITY`` generator are provided using the\n:paramref:`_schema.Identity.start` and :paramref:`_schema.Identity.increment`\nparameters passed to the :class:`_schema.Identity` object::\n\n    from sqlalchemy import Table, Integer, Column, Identity\n\n    test = Table(\n        "test",\n        metadata,\n        Column(\n            "id", Integer, primary_key=True, Identity(start=100, increment=10)\n        ),\n        Column("name", String(20)),\n    )\n\nThe CREATE TABLE for the above :class:`_schema.Table` object would be:\n\n.. sourcecode:: sql\n\n   CREATE TABLE test (\n     id INTEGER NOT NULL IDENTITY(100,10) PRIMARY KEY,\n     name VARCHAR(20) NULL,\n   )\n\n.. note::\n\n   The :class:`_schema.Identity` object supports many other parameter in\n   addition to ``start`` and ``increment``. These are not supported by\n   SQL Server and will be ignored when generating the CREATE TABLE ddl.\n\n.. versionchanged:: 1.3.19  The :class:`_schema.Identity` object is\n   now used to affect the\n   ``IDENTITY`` generator for a :class:`_schema.Column` under  SQL Server.\n   Previously, the :class:`.Sequence` object was used.  As SQL Server now\n   supports real sequences as a separate construct, :class:`.Sequence` will be\n   functional in the normal way starting from SQLAlchemy version 1.4.\n\n\nUsing IDENTITY with Non-Integer numeric types\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nSQL Server also allows ``IDENTITY`` to be used with ``NUMERIC`` columns.  To\nimplement this pattern smoothly in SQLAlchemy, the primary datatype of the\ncolumn should remain as ``Integer``, however the underlying implementation\ntype deployed to the SQL Server database can be specified as ``Numeric`` using\n:meth:`.TypeEngine.with_variant`::\n\n    from sqlalchemy import Column\n    from sqlalchemy import Integer\n    from sqlalchemy import Numeric\n    from sqlalchemy import String\n    from sqlalchemy.ext.declarative import declarative_base\n\n    Base = declarative_base()\n\n\n    class TestTable(Base):\n        __tablename__ = "test"\n        id = Column(\n            Integer().with_variant(Numeric(10, 0), "mssql"),\n            primary_key=True,\n            autoincrement=True,\n        )\n        name = Column(String)\n\nIn the above example, ``Integer().with_variant()`` provides clear usage\ninformation that accurately describes the intent of the code. The general\nrestriction that ``autoincrement`` only applies to ``Integer`` is established\nat the metadata level and not at the per-dialect level.\n\nWhen using the above pattern, the primary key identifier that comes back from\nthe insertion of a row, which is also the value that would be assigned to an\nORM object such as ``TestTable`` above, will be an instance of ``Decimal()``\nand not ``int`` when using SQL Server. The numeric return type of the\n:class:`_types.Numeric` type can be changed to return floats by passing False\nto :paramref:`_types.Numeric.asdecimal`. To normalize the return type of the\nabove ``Numeric(10, 0)`` to return Python ints (which also support "long"\ninteger values in Python 3), use :class:`_types.TypeDecorator` as follows::\n\n    from sqlalchemy import TypeDecorator\n\n\n    class NumericAsInteger(TypeDecorator):\n        "normalize floating point return values into ints"\n\n        impl = Numeric(10, 0, asdecimal=False)\n        cache_ok = True\n\n        def process_result_value(self, value, dialect):\n            if value is not None:\n                value = int(value)\n            return value\n\n\n    class TestTable(Base):\n        __tablename__ = "test"\n        id = Column(\n            Integer().with_variant(NumericAsInteger, "mssql"),\n            primary_key=True,\n            autoincrement=True,\n        )\n        name = Column(String)\n\n.. _mssql_insert_behavior:\n\nINSERT behavior\n^^^^^^^^^^^^^^^^\n\nHandling of the ``IDENTITY`` column at INSERT time involves two key\ntechniques. The most common is being able to fetch the "last inserted value"\nfor a given ``IDENTITY`` column, a process which SQLAlchemy performs\nimplicitly in many cases, most importantly within the ORM.\n\nThe process for fetching this value has several variants:\n\n* In the vast majority of cases, RETURNING is used in conjunction with INSERT\n  statements on SQL Server in order to get newly generated primary key values:\n\n  .. sourcecode:: sql\n\n    INSERT INTO t (x) OUTPUT inserted.id VALUES (?)\n\n  As of SQLAlchemy 2.0, the :ref:`engine_insertmanyvalues` feature is also\n  used by default to optimize many-row INSERT statements; for SQL Server\n  the feature takes place for both RETURNING and-non RETURNING\n  INSERT statements.\n\n  .. versionchanged:: 2.0.10 The :ref:`engine_insertmanyvalues` feature for\n     SQL Server was temporarily disabled for SQLAlchemy version 2.0.9 due to\n     issues with row ordering. As of 2.0.10 the feature is re-enabled, with\n     special case handling for the unit of work\'s requirement for RETURNING to\n     be ordered.\n\n* When RETURNING is not available or has been disabled via\n  ``implicit_returning=False``, either the ``scope_identity()`` function or\n  the ``@@identity`` variable is used; behavior varies by backend:\n\n  * when using PyODBC, the phrase ``; select scope_identity()`` will be\n    appended to the end of the INSERT statement; a second result set will be\n    fetched in order to receive the value.  Given a table as::\n\n        t = Table(\n            "t",\n            metadata,\n            Column("id", Integer, primary_key=True),\n            Column("x", Integer),\n            implicit_returning=False,\n        )\n\n    an INSERT will look like:\n\n    .. sourcecode:: sql\n\n        INSERT INTO t (x) VALUES (?); select scope_identity()\n\n  * Other dialects such as pymssql will call upon\n    ``SELECT scope_identity() AS lastrowid`` subsequent to an INSERT\n    statement. If the flag ``use_scope_identity=False`` is passed to\n    :func:`_sa.create_engine`,\n    the statement ``SELECT @@identity AS lastrowid``\n    is used instead.\n\nA table that contains an ``IDENTITY`` column will prohibit an INSERT statement\nthat refers to the identity column explicitly.  The SQLAlchemy dialect will\ndetect when an INSERT construct, created using a core\n:func:`_expression.insert`\nconstruct (not a plain string SQL), refers to the identity column, and\nin this case will emit ``SET IDENTITY_INSERT ON`` prior to the insert\nstatement proceeding, and ``SET IDENTITY_INSERT OFF`` subsequent to the\nexecution.  Given this example::\n\n    m = MetaData()\n    t = Table(\n        "t", m, Column("id", Integer, primary_key=True), Column("x", Integer)\n    )\n    m.create_all(engine)\n\n    with engine.begin() as conn:\n        conn.execute(t.insert(), {"id": 1, "x": 1}, {"id": 2, "x": 2})\n\nThe above column will be created with IDENTITY, however the INSERT statement\nwe emit is specifying explicit values.  In the echo output we can see\nhow SQLAlchemy handles this:\n\n.. sourcecode:: sql\n\n    CREATE TABLE t (\n        id INTEGER NOT NULL IDENTITY(1,1),\n        x INTEGER NULL,\n        PRIMARY KEY (id)\n    )\n\n    COMMIT\n    SET IDENTITY_INSERT t ON\n    INSERT INTO t (id, x) VALUES (?, ?)\n    ((1, 1), (2, 2))\n    SET IDENTITY_INSERT t OFF\n    COMMIT\n\n\n\nThis is an auxiliary use case suitable for testing and bulk insert scenarios.\n\nSEQUENCE support\n----------------\n\nThe :class:`.Sequence` object creates "real" sequences, i.e.,\n``CREATE SEQUENCE``:\n\n.. sourcecode:: pycon+sql\n\n    >>> from sqlalchemy import Sequence\n    >>> from sqlalchemy.schema import CreateSequence\n    >>> from sqlalchemy.dialects import mssql\n    >>> print(\n    ...     CreateSequence(Sequence("my_seq", start=1)).compile(\n    ...         dialect=mssql.dialect()\n    ...     )\n    ... )\n    {printsql}CREATE SEQUENCE my_seq START WITH 1\n\nFor integer primary key generation, SQL Server\'s ``IDENTITY`` construct should\ngenerally be preferred vs. sequence.\n\n.. tip::\n\n    The default start value for T-SQL is ``-2**63`` instead of 1 as\n    in most other SQL databases. Users should explicitly set the\n    :paramref:`.Sequence.start` to 1 if that\'s the expected default::\n\n        seq = Sequence("my_sequence", start=1)\n\n.. versionadded:: 1.4 added SQL Server support for :class:`.Sequence`\n\n.. versionchanged:: 2.0 The SQL Server dialect will no longer implicitly\n   render "START WITH 1" for ``CREATE SEQUENCE``, which was the behavior\n   first implemented in version 1.4.\n\nMAX on VARCHAR / NVARCHAR\n-------------------------\n\nSQL Server supports the special string "MAX" within the\n:class:`_types.VARCHAR` and :class:`_types.NVARCHAR` datatypes,\nto indicate "maximum length possible".   The dialect currently handles this as\na length of "None" in the base type, rather than supplying a\ndialect-specific version of these types, so that a base type\nspecified such as ``VARCHAR(None)`` can assume "unlengthed" behavior on\nmore than one backend without using dialect-specific types.\n\nTo build a SQL Server VARCHAR or NVARCHAR with MAX length, use None::\n\n    my_table = Table(\n        "my_table",\n        metadata,\n        Column("my_data", VARCHAR(None)),\n        Column("my_n_data", NVARCHAR(None)),\n    )\n\nCollation Support\n-----------------\n\nCharacter collations are supported by the base string types,\nspecified by the string argument "collation"::\n\n    from sqlalchemy import VARCHAR\n\n    Column("login", VARCHAR(32, collation="Latin1_General_CI_AS"))\n\nWhen such a column is associated with a :class:`_schema.Table`, the\nCREATE TABLE statement for this column will yield:\n\n.. sourcecode:: sql\n\n    login VARCHAR(32) COLLATE Latin1_General_CI_AS NULL\n\nLIMIT/OFFSET Support\n--------------------\n\nMSSQL has added support for LIMIT / OFFSET as of SQL Server 2012, via the\n"OFFSET n ROWS" and "FETCH NEXT n ROWS" clauses.  SQLAlchemy supports these\nsyntaxes automatically if SQL Server 2012 or greater is detected.\n\n.. versionchanged:: 1.4 support added for SQL Server "OFFSET n ROWS" and\n   "FETCH NEXT n ROWS" syntax.\n\nFor statements that specify only LIMIT and no OFFSET, all versions of SQL\nServer support the TOP keyword.   This syntax is used for all SQL Server\nversions when no OFFSET clause is present.  A statement such as::\n\n    select(some_table).limit(5)\n\nwill render similarly to:\n\n.. sourcecode:: sql\n\n    SELECT TOP 5 col1, col2.. FROM table\n\nFor versions of SQL Server prior to SQL Server 2012, a statement that uses\nLIMIT and OFFSET, or just OFFSET alone, will be rendered using the\n``ROW_NUMBER()`` window function.   A statement such as::\n\n    select(some_table).order_by(some_table.c.col3).limit(5).offset(10)\n\nwill render similarly to:\n\n.. sourcecode:: sql\n\n    SELECT anon_1.col1, anon_1.col2 FROM (SELECT col1, col2,\n    ROW_NUMBER() OVER (ORDER BY col3) AS\n    mssql_rn FROM table WHERE t.x = :x_1) AS\n    anon_1 WHERE mssql_rn > :param_1 AND mssql_rn <= :param_2 + :param_1\n\nNote that when using LIMIT and/or OFFSET, whether using the older\nor newer SQL Server syntaxes, the statement must have an ORDER BY as well,\nelse a :class:`.CompileError` is raised.\n\n.. _mssql_comment_support:\n\nDDL Comment Support\n--------------------\n\nComment support, which includes DDL rendering for attributes such as\n:paramref:`_schema.Table.comment` and :paramref:`_schema.Column.comment`, as\nwell as the ability to reflect these comments, is supported assuming a\nsupported version of SQL Server is in use. If a non-supported version such as\nAzure Synapse is detected at first-connect time (based on the presence\nof the ``fn_listextendedproperty`` SQL function), comment support including\nrendering and table-comment reflection is disabled, as both features rely upon\nSQL Server stored procedures and functions that are not available on all\nbackend types.\n\nTo force comment support to be on or off, bypassing autodetection, set the\nparameter ``supports_comments`` within :func:`_sa.create_engine`::\n\n    e = create_engine("mssql+pyodbc://u:p@dsn", supports_comments=False)\n\n.. versionadded:: 2.0 Added support for table and column comments for\n   the SQL Server dialect, including DDL generation and reflection.\n\n.. _mssql_isolation_level:\n\nTransaction Isolation Level\n---------------------------\n\nAll SQL Server dialects support setting of transaction isolation level\nboth via a dialect-specific parameter\n:paramref:`_sa.create_engine.isolation_level`\naccepted by :func:`_sa.create_engine`,\nas well as the :paramref:`.Connection.execution_options.isolation_level`\nargument as passed to\n:meth:`_engine.Connection.execution_options`.\nThis feature works by issuing the\ncommand ``SET TRANSACTION ISOLATION LEVEL <level>`` for\neach new connection.\n\nTo set isolation level using :func:`_sa.create_engine`::\n\n    engine = create_engine(\n        "mssql+pyodbc://scott:tiger@ms_2008", isolation_level="REPEATABLE READ"\n    )\n\nTo set using per-connection execution options::\n\n    connection = engine.connect()\n    connection = connection.execution_options(isolation_level="READ COMMITTED")\n\nValid values for ``isolation_level`` include:\n\n* ``AUTOCOMMIT`` - pyodbc / pymssql-specific\n* ``READ COMMITTED``\n* ``READ UNCOMMITTED``\n* ``REPEATABLE READ``\n* ``SERIALIZABLE``\n* ``SNAPSHOT`` - specific to SQL Server\n\nThere are also more options for isolation level configurations, such as\n"sub-engine" objects linked to a main :class:`_engine.Engine` which each apply\ndifferent isolation level settings.  See the discussion at\n:ref:`dbapi_autocommit` for background.\n\n.. seealso::\n\n    :ref:`dbapi_autocommit`\n\n.. _mssql_reset_on_return:\n\nTemporary Table / Resource Reset for Connection Pooling\n-------------------------------------------------------\n\nThe :class:`.QueuePool` connection pool implementation used\nby the SQLAlchemy :class:`.Engine` object includes\n:ref:`reset on return <pool_reset_on_return>` behavior that will invoke\nthe DBAPI ``.rollback()`` method when connections are returned to the pool.\nWhile this rollback will clear out the immediate state used by the previous\ntransaction, it does not cover a wider range of session-level state, including\ntemporary tables as well as other server state such as prepared statement\nhandles and statement caches.   An undocumented SQL Server procedure known\nas ``sp_reset_connection`` is known to be a workaround for this issue which\nwill reset most of the session state that builds up on a connection, including\ntemporary tables.\n\nTo install ``sp_reset_connection`` as the means of performing reset-on-return,\nthe :meth:`.PoolEvents.reset` event hook may be used, as demonstrated in the\nexample below. The :paramref:`_sa.create_engine.pool_reset_on_return` parameter\nis set to ``None`` so that the custom scheme can replace the default behavior\ncompletely.   The custom hook implementation calls ``.rollback()`` in any case,\nas it\'s usually important that the DBAPI\'s own tracking of commit/rollback\nwill remain consistent with the state of the transaction::\n\n    from sqlalchemy import create_engine\n    from sqlalchemy import event\n\n    mssql_engine = create_engine(\n        "mssql+pyodbc://scott:tiger^5HHH@mssql2017:1433/test?driver=ODBC+Driver+17+for+SQL+Server",\n        # disable default reset-on-return scheme\n        pool_reset_on_return=None,\n    )\n\n\n    @event.listens_for(mssql_engine, "reset")\n    def _reset_mssql(dbapi_connection, connection_record, reset_state):\n        if not reset_state.terminate_only:\n            dbapi_connection.execute("{call sys.sp_reset_connection}")\n\n        # so that the DBAPI itself knows that the connection has been\n        # reset\n        dbapi_connection.rollback()\n\n.. versionchanged:: 2.0.0b3  Added additional state arguments to\n   the :meth:`.PoolEvents.reset` event and additionally ensured the event\n   is invoked for all "reset" occurrences, so that it\'s appropriate\n   as a place for custom "reset" handlers.   Previous schemes which\n   use the :meth:`.PoolEvents.checkin` handler remain usable as well.\n\n.. seealso::\n\n    :ref:`pool_reset_on_return` - in the :ref:`pooling_toplevel` documentation\n\nNullability\n-----------\nMSSQL has support for three levels of column nullability. The default\nnullability allows nulls and is explicit in the CREATE TABLE\nconstruct:\n\n.. sourcecode:: sql\n\n    name VARCHAR(20) NULL\n\nIf ``nullable=None`` is specified then no specification is made. In\nother words the database\'s configured default is used. This will\nrender:\n\n.. sourcecode:: sql\n\n    name VARCHAR(20)\n\nIf ``nullable`` is ``True`` or ``False`` then the column will be\n``NULL`` or ``NOT NULL`` respectively.\n\nDate / Time Handling\n--------------------\nDATE and TIME are supported.   Bind parameters are converted\nto datetime.datetime() objects as required by most MSSQL drivers,\nand results are processed from strings if needed.\nThe DATE and TIME types are not available for MSSQL 2005 and\nprevious - if a server version below 2008 is detected, DDL\nfor these types will be issued as DATETIME.\n\n.. _mssql_large_type_deprecation:\n\nLarge Text/Binary Type Deprecation\n----------------------------------\n\nPer\n`SQL Server 2012/2014 Documentation <https://technet.microsoft.com/en-us/library/ms187993.aspx>`_,\nthe ``NTEXT``, ``TEXT`` and ``IMAGE`` datatypes are to be removed from SQL\nServer in a future release.   SQLAlchemy normally relates these types to the\n:class:`.UnicodeText`, :class:`_expression.TextClause` and\n:class:`.LargeBinary` datatypes.\n\nIn order to accommodate this change, a new flag ``deprecate_large_types``\nis added to the dialect, which will be automatically set based on detection\nof the server version in use, if not otherwise set by the user.  The\nbehavior of this flag is as follows:\n\n* When this flag is ``True``, the :class:`.UnicodeText`,\n  :class:`_expression.TextClause` and\n  :class:`.LargeBinary` datatypes, when used to render DDL, will render the\n  types ``NVARCHAR(max)``, ``VARCHAR(max)``, and ``VARBINARY(max)``,\n  respectively.  This is a new behavior as of the addition of this flag.\n\n* When this flag is ``False``, the :class:`.UnicodeText`,\n  :class:`_expression.TextClause` and\n  :class:`.LargeBinary` datatypes, when used to render DDL, will render the\n  types ``NTEXT``, ``TEXT``, and ``IMAGE``,\n  respectively.  This is the long-standing behavior of these types.\n\n* The flag begins with the value ``None``, before a database connection is\n  established.   If the dialect is used to render DDL without the flag being\n  set, it is interpreted the same as ``False``.\n\n* On first connection, the dialect detects if SQL Server version 2012 or\n  greater is in use; if the flag is still at ``None``, it sets it to ``True``\n  or ``False`` based on whether 2012 or greater is detected.\n\n* The flag can be set to either ``True`` or ``False`` when the dialect\n  is created, typically via :func:`_sa.create_engine`::\n\n        eng = create_engine(\n            "mssql+pymssql://user:pass@host/db", deprecate_large_types=True\n        )\n\n* Complete control over whether the "old" or "new" types are rendered is\n  available in all SQLAlchemy versions by using the UPPERCASE type objects\n  instead: :class:`_types.NVARCHAR`, :class:`_types.VARCHAR`,\n  :class:`_types.VARBINARY`, :class:`_types.TEXT`, :class:`_mssql.NTEXT`,\n  :class:`_mssql.IMAGE`\n  will always remain fixed and always output exactly that\n  type.\n\n.. _multipart_schema_names:\n\nMultipart Schema Names\n----------------------\n\nSQL Server schemas sometimes require multiple parts to their "schema"\nqualifier, that is, including the database name and owner name as separate\ntokens, such as ``mydatabase.dbo.some_table``. These multipart names can be set\nat once using the :paramref:`_schema.Table.schema` argument of\n:class:`_schema.Table`::\n\n    Table(\n        "some_table",\n        metadata,\n        Column("q", String(50)),\n        schema="mydatabase.dbo",\n    )\n\nWhen performing operations such as table or component reflection, a schema\nargument that contains a dot will be split into separate\n"database" and "owner"  components in order to correctly query the SQL\nServer information schema tables, as these two values are stored separately.\nAdditionally, when rendering the schema name for DDL or SQL, the two\ncomponents will be quoted separately for case sensitive names and other\nspecial characters.   Given an argument as below::\n\n    Table(\n        "some_table",\n        metadata,\n        Column("q", String(50)),\n        schema="MyDataBase.dbo",\n    )\n\nThe above schema would be rendered as ``[MyDataBase].dbo``, and also in\nreflection, would be reflected using "dbo" as the owner and "MyDataBase"\nas the database name.\n\nTo control how the schema name is broken into database / owner,\nspecify brackets (which in SQL Server are quoting characters) in the name.\nBelow, the "owner" will be considered as ``MyDataBase.dbo`` and the\n"database" will be None::\n\n    Table(\n        "some_table",\n        metadata,\n        Column("q", String(50)),\n        schema="[MyDataBase.dbo]",\n    )\n\nTo individually specify both database and owner name with special characters\nor embedded dots, use two sets of brackets::\n\n    Table(\n        "some_table",\n        metadata,\n        Column("q", String(50)),\n        schema="[MyDataBase.Period].[MyOwner.Dot]",\n    )\n\n.. versionchanged:: 1.2 the SQL Server dialect now treats brackets as\n   identifier delimiters splitting the schema into separate database\n   and owner tokens, to allow dots within either name itself.\n\n.. _legacy_schema_rendering:\n\nLegacy Schema Mode\n------------------\n\nVery old versions of the MSSQL dialect introduced the behavior such that a\nschema-qualified table would be auto-aliased when used in a\nSELECT statement; given a table::\n\n    account_table = Table(\n        "account",\n        metadata,\n        Column("id", Integer, primary_key=True),\n        Column("info", String(100)),\n        schema="customer_schema",\n    )\n\nthis legacy mode of rendering would assume that "customer_schema.account"\nwould not be accepted by all parts of the SQL statement, as illustrated\nbelow:\n\n.. sourcecode:: pycon+sql\n\n    >>> eng = create_engine("mssql+pymssql://mydsn", legacy_schema_aliasing=True)\n    >>> print(account_table.select().compile(eng))\n    {printsql}SELECT account_1.id, account_1.info\n    FROM customer_schema.account AS account_1\n\nThis mode of behavior is now off by default, as it appears to have served\nno purpose; however in the case that legacy applications rely upon it,\nit is available using the ``legacy_schema_aliasing`` argument to\n:func:`_sa.create_engine` as illustrated above.\n\n.. deprecated:: 1.4\n\n   The ``legacy_schema_aliasing`` flag is now\n   deprecated and will be removed in a future release.\n\n.. _mssql_indexes:\n\nClustered Index Support\n-----------------------\n\nThe MSSQL dialect supports clustered indexes (and primary keys) via the\n``mssql_clustered`` option.  This option is available to :class:`.Index`,\n:class:`.UniqueConstraint`. and :class:`.PrimaryKeyConstraint`.\nFor indexes this option can be combined with the ``mssql_columnstore`` one\nto create a clustered columnstore index.\n\nTo generate a clustered index::\n\n    Index("my_index", table.c.x, mssql_clustered=True)\n\nwhich renders the index as ``CREATE CLUSTERED INDEX my_index ON table (x)``.\n\nTo generate a clustered primary key use::\n\n    Table(\n        "my_table",\n        metadata,\n        Column("x", ...),\n        Column("y", ...),\n        PrimaryKeyConstraint("x", "y", mssql_clustered=True),\n    )\n\nwhich will render the table, for example, as:\n\n.. sourcecode:: sql\n\n  CREATE TABLE my_table (\n    x INTEGER NOT NULL,\n    y INTEGER NOT NULL,\n    PRIMARY KEY CLUSTERED (x, y)\n  )\n\nSimilarly, we can generate a clustered unique constraint using::\n\n    Table(\n        "my_table",\n        metadata,\n        Column("x", ...),\n        Column("y", ...),\n        PrimaryKeyConstraint("x"),\n        UniqueConstraint("y", mssql_clustered=True),\n    )\n\nTo explicitly request a non-clustered primary key (for example, when\na separate clustered index is desired), use::\n\n    Table(\n        "my_table",\n        metadata,\n        Column("x", ...),\n        Column("y", ...),\n        PrimaryKeyConstraint("x", "y", mssql_clustered=False),\n    )\n\nwhich will render the table, for example, as:\n\n.. sourcecode:: sql\n\n  CREATE TABLE my_table (\n    x INTEGER NOT NULL,\n    y INTEGER NOT NULL,\n    PRIMARY KEY NONCLUSTERED (x, y)\n  )\n\nColumnstore Index Support\n-------------------------\n\nThe MSSQL dialect supports columnstore indexes via the ``mssql_columnstore``\noption.  This option is available to :class:`.Index`. It be combined with\nthe ``mssql_clustered`` option to create a clustered columnstore index.\n\nTo generate a columnstore index::\n\n    Index("my_index", table.c.x, mssql_columnstore=True)\n\nwhich renders the index as ``CREATE COLUMNSTORE INDEX my_index ON table (x)``.\n\nTo generate a clustered columnstore index provide no columns::\n\n    idx = Index("my_index", mssql_clustered=True, mssql_columnstore=True)\n    # required to associate the index with the table\n    table.append_constraint(idx)\n\nthe above renders the index as\n``CREATE CLUSTERED COLUMNSTORE INDEX my_index ON table``.\n\n.. versionadded:: 2.0.18\n\nMSSQL-Specific Index Options\n-----------------------------\n\nIn addition to clustering, the MSSQL dialect supports other special options\nfor :class:`.Index`.\n\nINCLUDE\n^^^^^^^\n\nThe ``mssql_include`` option renders INCLUDE(colname) for the given string\nnames::\n\n    Index("my_index", table.c.x, mssql_include=["y"])\n\nwould render the index as ``CREATE INDEX my_index ON table (x) INCLUDE (y)``\n\n.. _mssql_index_where:\n\nFiltered Indexes\n^^^^^^^^^^^^^^^^\n\nThe ``mssql_where`` option renders WHERE(condition) for the given string\nnames::\n\n    Index("my_index", table.c.x, mssql_where=table.c.x > 10)\n\nwould render the index as ``CREATE INDEX my_index ON table (x) WHERE x > 10``.\n\n.. versionadded:: 1.3.4\n\nIndex ordering\n^^^^^^^^^^^^^^\n\nIndex ordering is available via functional expressions, such as::\n\n    Index("my_index", table.c.x.desc())\n\nwould render the index as ``CREATE INDEX my_index ON table (x DESC)``\n\n.. seealso::\n\n    :ref:`schema_indexes_functional`\n\nCompatibility Levels\n--------------------\nMSSQL supports the notion of setting compatibility levels at the\ndatabase level. This allows, for instance, to run a database that\nis compatible with SQL2000 while running on a SQL2005 database\nserver. ``server_version_info`` will always return the database\nserver version information (in this case SQL2005) and not the\ncompatibility level information. Because of this, if running under\na backwards compatibility mode SQLAlchemy may attempt to use T-SQL\nstatements that are unable to be parsed by the database server.\n\n.. _mssql_triggers:\n\nTriggers\n--------\n\nSQLAlchemy by default uses OUTPUT INSERTED to get at newly\ngenerated primary key values via IDENTITY columns or other\nserver side defaults.   MS-SQL does not\nallow the usage of OUTPUT INSERTED on tables that have triggers.\nTo disable the usage of OUTPUT INSERTED on a per-table basis,\nspecify ``implicit_returning=False`` for each :class:`_schema.Table`\nwhich has triggers::\n\n    Table(\n        "mytable",\n        metadata,\n        Column("id", Integer, primary_key=True),\n        # ...,\n        implicit_returning=False,\n    )\n\nDeclarative form::\n\n    class MyClass(Base):\n        # ...\n        __table_args__ = {"implicit_returning": False}\n\n.. _mssql_rowcount_versioning:\n\nRowcount Support / ORM Versioning\n---------------------------------\n\nThe SQL Server drivers may have limited ability to return the number\nof rows updated from an UPDATE or DELETE statement.\n\nAs of this writing, the PyODBC driver is not able to return a rowcount when\nOUTPUT INSERTED is used.    Previous versions of SQLAlchemy therefore had\nlimitations for features such as the "ORM Versioning" feature that relies upon\naccurate rowcounts in order to match version numbers with matched rows.\n\nSQLAlchemy 2.0 now retrieves the "rowcount" manually for these particular use\ncases based on counting the rows that arrived back within RETURNING; so while\nthe driver still has this limitation, the ORM Versioning feature is no longer\nimpacted by it. As of SQLAlchemy 2.0.5, ORM versioning has been fully\nre-enabled for the pyodbc driver.\n\n.. versionchanged:: 2.0.5  ORM versioning support is restored for the pyodbc\n   driver.  Previously, a warning would be emitted during ORM flush that\n   versioning was not supported.\n\n\nEnabling Snapshot Isolation\n---------------------------\n\nSQL Server has a default transaction\nisolation mode that locks entire tables, and causes even mildly concurrent\napplications to have long held locks and frequent deadlocks.\nEnabling snapshot isolation for the database as a whole is recommended\nfor modern levels of concurrency support.  This is accomplished via the\nfollowing ALTER DATABASE commands executed at the SQL prompt:\n\n.. sourcecode:: sql\n\n    ALTER DATABASE MyDatabase SET ALLOW_SNAPSHOT_ISOLATION ON\n\n    ALTER DATABASE MyDatabase SET READ_COMMITTED_SNAPSHOT ON\n\nBackground on SQL Server snapshot isolation is available at\nhttps://msdn.microsoft.com/en-us/library/ms175095.aspx.\n\n'
from __future__ import annotations
import codecs
import datetime
import operator
import re
from typing import overload
from typing import TYPE_CHECKING
from uuid import UUID as _python_UUID
from  import information_schema as ischema
from json import JSON
from json import JSONIndexType
from json import JSONPathType
from  import exc
from  import Identity
from  import schema as sa_schema
from  import Sequence
from  import sql
from  import text
from  import util
from engine import cursor as _cursor
from engine import default
from engine import reflection
from engine.reflection import ReflectionDefaults
from sql import coercions
from sql import compiler
from sql import elements
from sql import expression
from sql import func
from sql import quoted_name
from sql import roles
from sql import sqltypes
from sql import try_cast
from sql import util as sql_util
from sql._typing import is_sql_compiler
from sql.compiler import InsertmanyvaluesSentinelOpts
from sql.elements import TryCast
from types import BIGINT
from types import BINARY
from types import CHAR
from types import DATE
from types import DATETIME
from types import DECIMAL
from types import FLOAT
from types import INTEGER
from types import NCHAR
from types import NUMERIC
from types import NVARCHAR
from types import SMALLINT
from types import TEXT
from types import VARCHAR
from util import update_wrapper
from util.typing import Literal
if TYPE_CHECKING:
    from sql.dml import DMLState
    from sql.selectable import TableClause
MS_2017_VERSION = (14,)
MS_2016_VERSION = (13,)
MS_2014_VERSION = (12,)
MS_2012_VERSION = (11,)
MS_2008_VERSION = (10,)
MS_2005_VERSION = (9,)
MS_2000_VERSION = (8,)
RESERVED_WORDS = {
    'as',
    'by',
    'if',
    'in',
    'is',
    'of',
    'on',
    'or',
    'to',
    'add',
    'all',
    'and',
    'any',
    'asc',
    'end',
    'for',
    'key',
    'not',
    'off',
    'set',
    'top',
    'use',
    'bulk',
    'case',
    'dbcc',
    'deny',
    'desc',
    'disk',
    'drop',
    'dump',
    'else',
    'exec',
    'exit',
    'file',
    'from',
    'full',
    'goto',
    'into',
    'join',
    'kill',
    'left',
    'like',
    'load',
    'null',
    'open',
    'over',
    'plan',
    'proc',
    'read',
    'rule',
    'save',
    'some',
    'then',
    'tran',
    'user',
    'view',
    'when',
    'with',
    'alter',
    'begin',
    'break',
    'check',
    'close',
    'cross',
    'fetch',
    'grant',
    'group',
    'index',
    'inner',
    'merge',
    'order',
    'outer',
    'pivot',
    'print',
    'right',
    'table',
    'union',
    'where',
    'while',
    'backup',
    'browse',
    'column',
    'commit',
    'create',
    'cursor',
    'delete',
    'double',
    'errlvl',
    'escape',
    'except',
    'exists',
    'having',
    'insert',
    'lineno',
    'nullif',
    'option',
    'public',
    'return',
    'revert',
    'revoke',
    'schema',
    'select',
    'unique',
    'update',
    'values',
    'between',
    'cascade',
    'collate',
    'compute',
    'convert',
    'current',
    'declare',
    'default',
    'execute',
    'foreign',
    'nocheck',
    'offsets',
    'openxml',
    'percent',
    'primary',
    'restore',
    'setuser',
    'trigger',
    'tsequal',
    'unpivot',
    'varying',
    'waitfor',
    'coalesce',
    'contains',
    'continue',
    'database',
    'distinct',
    'external',
    'freetext',
    'function',
    'holdlock',
    'identity',
    'national',
    'readtext',
    'restrict',
    'rollback',
    'rowcount',
    'shutdown',
    'textsize',
    'truncate',
    'clustered',
    'intersect',
    'openquery',
    'precision',
    'procedure',
    'raiserror',
    'writetext',
    'checkpoint',
    'constraint',
    'deallocate',
    'fillfactor',
    'openrowset',
    'references',
    'rowguidcol',
    'statistics',
    'updatetext',
    'distributed',
    'identitycol',
    'reconfigure',
    'replication',
    'system_user',
    'tablesample',
    'transaction',
    'current_date',
    'current_time',
    'current_user',
    'nonclustered',
    'session_user',
    'authorization',
    'containstable',
    'freetexttable',
    'securityaudit',
    'opendatasource',
    'identity_insert',
    'current_timestamp'}

class REAL(sqltypes.REAL):
    pass
# WARNING: Decompyle incomplete


class DOUBLE_PRECISION(sqltypes.DOUBLE_PRECISION):
    pass
# WARNING: Decompyle incomplete


class TINYINT(sqltypes.Integer):
    __visit_name__ = 'TINYINT'


class _MSDate(sqltypes.Date):
    
    def bind_processor(self, dialect):
        
        def process(value):
            if type(value) == datetime.date:
                return datetime.datetime(value.year, value.month, value.day)

        return process

    _reg = re.compile('(\\d+)-(\\d+)-(\\d+)')
    
    def result_processor(self, dialect, coltype):
        pass
    # WARNING: Decompyle incomplete



class TIME(sqltypes.TIME):
    pass
# WARNING: Decompyle incomplete

_MSTime = TIME

class _BASETIMEIMPL(TIME):
    __visit_name__ = '_BASETIMEIMPL'


class _DateTimeBase:
    
    def bind_processor(self, dialect):
        
        def process(value):
            if type(value) == datetime.date:
                return datetime.datetime(value.year, value.month, value.day)

        return process



class _MSDateTime(sqltypes.DateTime, _DateTimeBase):
    pass


class SMALLDATETIME(sqltypes.DateTime, _DateTimeBase):
    __visit_name__ = 'SMALLDATETIME'


class DATETIME2(sqltypes.DateTime, _DateTimeBase):
    pass
# WARNING: Decompyle incomplete


class DATETIMEOFFSET(sqltypes.DateTime, _DateTimeBase):
    pass
# WARNING: Decompyle incomplete


class _UnicodeLiteral:
    
    def literal_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete



class _MSUnicode(sqltypes.Unicode, _UnicodeLiteral):
    pass


class _MSUnicodeText(sqltypes.UnicodeText, _UnicodeLiteral):
    pass


class TIMESTAMP(sqltypes._Binary):
    pass
# WARNING: Decompyle incomplete


class ROWVERSION(TIMESTAMP):
    '''Implement the SQL Server ROWVERSION type.

    The ROWVERSION datatype is a SQL Server synonym for the TIMESTAMP
    datatype, however current SQL Server documentation suggests using
    ROWVERSION for new datatypes going forward.

    The ROWVERSION datatype does **not** reflect (e.g. introspect) from the
    database as itself; the returned datatype will be
    :class:`_mssql.TIMESTAMP`.

    This is a read-only datatype that does not support INSERT of values.

    .. versionadded:: 1.2

    .. seealso::

        :class:`_mssql.TIMESTAMP`

    '''
    __visit_name__ = 'ROWVERSION'


class NTEXT(sqltypes.UnicodeText):
    '''MSSQL NTEXT type, for variable-length unicode text up to 2^30
    characters.'''
    __visit_name__ = 'NTEXT'


class VARBINARY(sqltypes.LargeBinary, sqltypes.VARBINARY):
    pass
# WARNING: Decompyle incomplete


class IMAGE(sqltypes.LargeBinary):
    __visit_name__ = 'IMAGE'


class XML(sqltypes.Text):
    '''MSSQL XML type.

    This is a placeholder type for reflection purposes that does not include
    any Python-side datatype support.   It also does not currently support
    additional arguments, such as "CONTENT", "DOCUMENT",
    "xml_schema_collection".

    '''
    __visit_name__ = 'XML'


class BIT(sqltypes.Boolean):
    """MSSQL BIT type.

    Both pyodbc and pymssql return values from BIT columns as
    Python <class 'bool'> so just subclass Boolean.

    """
    __visit_name__ = 'BIT'


class MONEY(sqltypes.TypeEngine):
    __visit_name__ = 'MONEY'


class SMALLMONEY(sqltypes.TypeEngine):
    __visit_name__ = 'SMALLMONEY'


class MSUUid(sqltypes.Uuid):
    
    def bind_processor(self, dialect):
