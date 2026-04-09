# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import TYPE_CHECKING
from base import SchemaEventTarget
from  import event
if TYPE_CHECKING:
    from schema import Column
    from schema import Constraint
    from schema import SchemaItem
    from schema import Table
    from engine.base import Connection
    from engine.interfaces import ReflectedColumn
    from engine.reflection import Inspector

def DDLEvents():
    '''DDLEvents'''
    __doc__ = '\n    Define event listeners for schema objects,\n    that is, :class:`.SchemaItem` and other :class:`.SchemaEventTarget`\n    subclasses, including :class:`_schema.MetaData`, :class:`_schema.Table`,\n    :class:`_schema.Column`, etc.\n\n    **Create / Drop Events**\n\n    Events emitted when CREATE and DROP commands are emitted to the database.\n    The event hooks in this category include :meth:`.DDLEvents.before_create`,\n    :meth:`.DDLEvents.after_create`, :meth:`.DDLEvents.before_drop`, and\n    :meth:`.DDLEvents.after_drop`.\n\n    These events are emitted when using schema-level methods such as\n    :meth:`.MetaData.create_all` and :meth:`.MetaData.drop_all`. Per-object\n    create/drop methods such as :meth:`.Table.create`, :meth:`.Table.drop`,\n    :meth:`.Index.create` are also included, as well as dialect-specific\n    methods such as :meth:`_postgresql.ENUM.create`.\n\n    .. versionadded:: 2.0 :class:`.DDLEvents` event hooks now take place\n       for non-table objects including constraints, indexes, and\n       dialect-specific schema types.\n\n    Event hooks may be attached directly to a :class:`_schema.Table` object or\n    to a :class:`_schema.MetaData` collection, as well as to any\n    :class:`.SchemaItem` class or object that can be individually created and\n    dropped using a distinct SQL command. Such classes include :class:`.Index`,\n    :class:`.Sequence`, and dialect-specific classes such as\n    :class:`_postgresql.ENUM`.\n\n    Example using the :meth:`.DDLEvents.after_create` event, where a custom\n    event hook will emit an ``ALTER TABLE`` command on the current connection,\n    after ``CREATE TABLE`` is emitted::\n\n        from sqlalchemy import create_engine\n        from sqlalchemy import event\n        from sqlalchemy import Table, Column, Metadata, Integer\n\n        m = MetaData()\n        some_table = Table("some_table", m, Column("data", Integer))\n\n\n        @event.listens_for(some_table, "after_create")\n        def after_create(target, connection, **kw):\n            connection.execute(\n                text("ALTER TABLE %s SET name=foo_%s" % (target.name, target.name))\n            )\n\n\n        some_engine = create_engine("postgresql://scott:tiger@host/test")\n\n        # will emit "CREATE TABLE some_table" as well as the above\n        # "ALTER TABLE" statement afterwards\n        m.create_all(some_engine)\n\n    Constraint objects such as :class:`.ForeignKeyConstraint`,\n    :class:`.UniqueConstraint`, :class:`.CheckConstraint` may also be\n    subscribed to these events, however they will **not** normally produce\n    events as these objects are usually rendered inline within an\n    enclosing ``CREATE TABLE`` statement and implicitly dropped from a\n    ``DROP TABLE`` statement.\n\n    For the :class:`.Index` construct, the event hook will be emitted\n    for ``CREATE INDEX``, however SQLAlchemy does not normally emit\n    ``DROP INDEX`` when dropping tables as this is again implicit within the\n    ``DROP TABLE`` statement.\n\n    .. versionadded:: 2.0 Support for :class:`.SchemaItem` objects\n       for create/drop events was expanded from its previous support for\n       :class:`.MetaData` and :class:`.Table` to also include\n       :class:`.Constraint` and all subclasses, :class:`.Index`,\n       :class:`.Sequence` and some type-related constructs such as\n       :class:`_postgresql.ENUM`.\n\n    .. note:: These event hooks are only emitted within the scope of\n       SQLAlchemy\'s create/drop methods; they are not necessarily supported\n       by tools such as `alembic <https://alembic.sqlalchemy.org>`_.\n\n\n    **Attachment Events**\n\n    Attachment events are provided to customize\n    behavior whenever a child schema element is associated\n    with a parent, such as when a :class:`_schema.Column` is associated\n    with its :class:`_schema.Table`, when a\n    :class:`_schema.ForeignKeyConstraint`\n    is associated with a :class:`_schema.Table`, etc.  These events include\n    :meth:`.DDLEvents.before_parent_attach` and\n    :meth:`.DDLEvents.after_parent_attach`.\n\n    **Reflection Events**\n\n    The :meth:`.DDLEvents.column_reflect` event is used to intercept\n    and modify the in-Python definition of database columns when\n    :term:`reflection` of database tables proceeds.\n\n    **Use with Generic DDL**\n\n    DDL events integrate closely with the\n    :class:`.DDL` class and the :class:`.ExecutableDDLElement` hierarchy\n    of DDL clause constructs, which are themselves appropriate\n    as listener callables::\n\n        from sqlalchemy import DDL\n\n        event.listen(\n            some_table,\n            "after_create",\n            DDL("ALTER TABLE %(table)s SET name=foo_%(table)s"),\n        )\n\n    **Event Propagation to MetaData Copies**\n\n    For all :class:`.DDLEvent` events, the ``propagate=True`` keyword argument\n    will ensure that a given event handler is propagated to copies of the\n    object, which are made when using the :meth:`_schema.Table.to_metadata`\n    method::\n\n        from sqlalchemy import DDL\n\n        metadata = MetaData()\n        some_table = Table("some_table", metadata, Column("data", Integer))\n\n        event.listen(\n            some_table,\n            "after_create",\n            DDL("ALTER TABLE %(table)s SET name=foo_%(table)s"),\n            propagate=True,\n        )\n\n        new_metadata = MetaData()\n        new_table = some_table.to_metadata(new_metadata)\n\n    The above :class:`.DDL` object will be associated with the\n    :meth:`.DDLEvents.after_create` event for both the ``some_table`` and\n    the ``new_table`` :class:`.Table` objects.\n\n    .. seealso::\n\n        :ref:`event_toplevel`\n\n        :class:`.ExecutableDDLElement`\n\n        :class:`.DDL`\n\n        :ref:`schema_ddl_sequences`\n\n    '
    _target_class_doc = 'SomeSchemaClassOrObject'
    _dispatch_target = SchemaEventTarget
    
    def before_create(self = None, target = None, connection = None, **kw):
        '''Called before CREATE statements are emitted.

        :param target: the :class:`.SchemaObject`, such as a
         :class:`_schema.MetaData` or :class:`_schema.Table`
         but also including all create/drop objects such as
         :class:`.Index`, :class:`.Sequence`, etc.,
         object which is the target of the event.

         .. versionadded:: 2.0 Support for all :class:`.SchemaItem` objects
            was added.

        :param connection: the :class:`_engine.Connection` where the
         CREATE statement or statements will be emitted.
        :param \\**kw: additional keyword arguments relevant
         to the event.  The contents of this dictionary
         may vary across releases, and include the
         list of tables being generated for a metadata-level
         event, the checkfirst flag, and other
         elements used by internal events.

        :func:`.event.listen` accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        :func:`.event.listen` accepts the ``insert=True``
        modifier for this event; when True, the listener function will
        be prepended to the internal list of events upon discovery, and execute
        before registered listener functions that do not pass this argument.

        '''
        pass

    
    def after_create(self = None, target = None, connection = None, **kw):
        '''Called after CREATE statements are emitted.

        :param target: the :class:`.SchemaObject`, such as a
         :class:`_schema.MetaData` or :class:`_schema.Table`
         but also including all create/drop objects such as
         :class:`.Index`, :class:`.Sequence`, etc.,
         object which is the target of the event.

         .. versionadded:: 2.0 Support for all :class:`.SchemaItem` objects
            was added.

        :param connection: the :class:`_engine.Connection` where the
         CREATE statement or statements have been emitted.
        :param \\**kw: additional keyword arguments relevant
         to the event.  The contents of this dictionary
         may vary across releases, and include the
         list of tables being generated for a metadata-level
         event, the checkfirst flag, and other
         elements used by internal events.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        '''
        pass

    
    def before_drop(self = None, target = None, connection = None, **kw):
        '''Called before DROP statements are emitted.

        :param target: the :class:`.SchemaObject`, such as a
         :class:`_schema.MetaData` or :class:`_schema.Table`
         but also including all create/drop objects such as
         :class:`.Index`, :class:`.Sequence`, etc.,
         object which is the target of the event.

         .. versionadded:: 2.0 Support for all :class:`.SchemaItem` objects
            was added.

        :param connection: the :class:`_engine.Connection` where the
         DROP statement or statements will be emitted.
        :param \\**kw: additional keyword arguments relevant
         to the event.  The contents of this dictionary
         may vary across releases, and include the
         list of tables being generated for a metadata-level
         event, the checkfirst flag, and other
         elements used by internal events.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        '''
        pass

    
    def after_drop(self = None, target = None, connection = None, **kw):
        '''Called after DROP statements are emitted.

        :param target: the :class:`.SchemaObject`, such as a
         :class:`_schema.MetaData` or :class:`_schema.Table`
         but also including all create/drop objects such as
         :class:`.Index`, :class:`.Sequence`, etc.,
         object which is the target of the event.

         .. versionadded:: 2.0 Support for all :class:`.SchemaItem` objects
            was added.

        :param connection: the :class:`_engine.Connection` where the
         DROP statement or statements have been emitted.
        :param \\**kw: additional keyword arguments relevant
         to the event.  The contents of this dictionary
         may vary across releases, and include the
         list of tables being generated for a metadata-level
         event, the checkfirst flag, and other
         elements used by internal events.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        '''
        pass

    
    def before_parent_attach(self = None, target = None, parent = None):
        '''Called before a :class:`.SchemaItem` is associated with
        a parent :class:`.SchemaItem`.

        :param target: the target object
        :param parent: the parent to which the target is being attached.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        '''
        pass

    
    def after_parent_attach(self = None, target = None, parent = None):
        '''Called after a :class:`.SchemaItem` is associated with
        a parent :class:`.SchemaItem`.

        :param target: the target object
        :param parent: the parent to which the target is being attached.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        '''
        pass

    
    def _sa_event_column_added_to_pk_constraint(self = None, const = None, col = None):
        '''internal event hook used for primary key naming convention
        updates.

        '''
        pass

    
    def column_reflect(self = None, inspector = None, table = None, column_info = ('inspector', 'Inspector', 'table', 'Table', 'column_info', 'ReflectedColumn', 'return', 'None')):
        '''Called for each unit of \'column info\' retrieved when
        a :class:`_schema.Table` is being reflected.

        This event is most easily used by applying it to a specific
        :class:`_schema.MetaData` instance, where it will take effect for
        all :class:`_schema.Table` objects within that
        :class:`_schema.MetaData` that undergo reflection::

            metadata = MetaData()


            @event.listens_for(metadata, "column_reflect")
            def receive_column_reflect(inspector, table, column_info):
                # receives for all Table objects that are reflected
                # under this MetaData
                ...


            # will use the above event hook
            my_table = Table("my_table", metadata, autoload_with=some_engine)

        .. versionadded:: 1.4.0b2 The :meth:`_events.DDLEvents.column_reflect`
           hook may now be applied to a :class:`_schema.MetaData` object as
           well as the :class:`_schema.MetaData` class itself where it will
           take place for all :class:`_schema.Table` objects associated with
           the targeted :class:`_schema.MetaData`.

        It may also be applied to the :class:`_schema.Table` class across
        the board::

            from sqlalchemy import Table


            @event.listens_for(Table, "column_reflect")
            def receive_column_reflect(inspector, table, column_info):
                # receives for all Table objects that are reflected
                ...

        It can also be applied to a specific :class:`_schema.Table` at the
        point that one is being reflected using the
        :paramref:`_schema.Table.listeners` parameter::

            t1 = Table(
                "my_table",
                autoload_with=some_engine,
                listeners=[("column_reflect", receive_column_reflect)],
            )

        The dictionary of column information as returned by the
        dialect is passed, and can be modified.  The dictionary
        is that returned in each element of the list returned
        by :meth:`.reflection.Inspector.get_columns`:

            * ``name`` - the column\'s name, is applied to the
              :paramref:`_schema.Column.name` parameter

            * ``type`` - the type of this column, which should be an instance
              of :class:`~sqlalchemy.types.TypeEngine`, is applied to the
              :paramref:`_schema.Column.type` parameter

            * ``nullable`` - boolean flag if the column is NULL or NOT NULL,
              is applied to the :paramref:`_schema.Column.nullable` parameter

            * ``default`` - the column\'s server default value.  This is
              normally specified as a plain string SQL expression, however the
              event can pass a :class:`.FetchedValue`, :class:`.DefaultClause`,
              or :func:`_expression.text` object as well.  Is applied to the
              :paramref:`_schema.Column.server_default` parameter

        The event is called before any action is taken against
        this dictionary, and the contents can be modified; the following
        additional keys may be added to the dictionary to further modify
        how the :class:`_schema.Column` is constructed:


            * ``key`` - the string key that will be used to access this
              :class:`_schema.Column` in the ``.c`` collection; will be applied
              to the :paramref:`_schema.Column.key` parameter. Is also used
              for ORM mapping.  See the section
              :ref:`mapper_automated_reflection_schemes` for an example.

            * ``quote`` - force or un-force quoting on the column name;
              is applied to the :paramref:`_schema.Column.quote` parameter.

            * ``info`` - a dictionary of arbitrary data to follow along with
              the :class:`_schema.Column`, is applied to the
              :paramref:`_schema.Column.info` parameter.

        :func:`.event.listen` also accepts the ``propagate=True``
        modifier for this event; when True, the listener function will
        be established for any copies made of the target object,
        i.e. those copies that are generated when
        :meth:`_schema.Table.to_metadata` is used.

        .. seealso::

            :ref:`mapper_automated_reflection_schemes` -
            in the ORM mapping documentation

            :ref:`automap_intercepting_columns` -
            in the :ref:`automap_toplevel` documentation

            :ref:`metadata_reflection_dbagnostic_types` - in
            the :ref:`metadata_reflection_toplevel` documentation

        '''
        pass


DDLEvents = <NODE:27>(DDLEvents, 'DDLEvents', event.Events[SchemaEventTarget])
