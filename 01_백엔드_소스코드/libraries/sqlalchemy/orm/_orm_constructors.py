# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _orm_constructors.pyc (Python 3.11)

from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import Collection
from typing import Iterable
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from  import mapperlib
from _typing import _O
from descriptor_props import Composite
from descriptor_props import Synonym
from interfaces import _AttributeOptions
from properties import MappedColumn
from properties import MappedSQLExpression
from query import AliasOption
from relationships import _RelationshipArgumentType
from relationships import _RelationshipDeclared
from relationships import _RelationshipSecondaryArgument
from relationships import RelationshipProperty
from session import Session
from util import _ORMJoin
from util import AliasedClass
from util import AliasedInsp
from util import LoaderCriteriaOption
from  import sql
from  import util
from exc import InvalidRequestError
from sql._typing import _no_kw
from sql.base import _NoArg
from sql.base import SchemaEventTarget
from sql.schema import _InsertSentinelColumnDefault
from sql.schema import SchemaConst
from sql.selectable import FromClause
from util.typing import Annotated
from util.typing import Literal
if TYPE_CHECKING:
    from _typing import _EntityType
    from _typing import _ORMColumnExprArgument
    from descriptor_props import _CC
    from descriptor_props import _CompositeAttrType
    from interfaces import PropComparator
    from mapper import Mapper
    from query import Query
    from relationships import _LazyLoadArgumentType
    from relationships import _ORMColCollectionArgument
    from relationships import _ORMOrderByArgument
    from relationships import _RelationshipJoinConditionArgument
    from relationships import ORMBackrefArgument
    from session import _SessionBind
    from sql._typing import _AutoIncrementType
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _FromClauseArgument
    from sql._typing import _InfoType
    from sql._typing import _OnClauseArgument
    from sql._typing import _TypeEngineArgument
    from sql.elements import ColumnElement
    from sql.schema import _ServerDefaultArgument
    from sql.schema import _ServerOnUpdateArgument
    from sql.selectable import Alias
    from sql.selectable import Subquery
_T = typing.TypeVar('_T')
contains_alias = (lambda alias = None: AliasOption(alias))()

def mapped_column(__name_pos = None, __type_pos = None, *, init, repr, default, default_factory, compare, kw_only, hash, nullable, primary_key, deferred, deferred_group, deferred_raiseload, use_existing_column, name, type_, autoincrement, doc, key, index, unique, info, onupdate, insert_default, server_default, server_onupdate, active_history, quote, system, comment, sort_order, dataclass_metadata, *args, **kw):
    '''declare a new ORM-mapped :class:`_schema.Column` construct
    for use within :ref:`Declarative Table <orm_declarative_table>`
    configuration.

    The :func:`_orm.mapped_column` function provides an ORM-aware and
    Python-typing-compatible construct which is used with
    :ref:`declarative <orm_declarative_mapping>` mappings to indicate an
    attribute that\'s mapped to a Core :class:`_schema.Column` object.  It
    provides the equivalent feature as mapping an attribute to a
    :class:`_schema.Column` object directly when using Declarative,
    specifically when using :ref:`Declarative Table <orm_declarative_table>`
    configuration.

    .. versionadded:: 2.0

    :func:`_orm.mapped_column` is normally used with explicit typing along with
    the :class:`_orm.Mapped` annotation type, where it can derive the SQL
    type and nullability for the column based on what\'s present within the
    :class:`_orm.Mapped` annotation.   It also may be used without annotations
    as a drop-in replacement for how :class:`_schema.Column` is used in
    Declarative mappings in SQLAlchemy 1.x style.

    For usage examples of :func:`_orm.mapped_column`, see the documentation
    at :ref:`orm_declarative_table`.

    .. seealso::

        :ref:`orm_declarative_table` - complete documentation

        :ref:`whatsnew_20_orm_declarative_typing` - migration notes for
        Declarative mappings using 1.x style mappings

    :param __name: String name to give to the :class:`_schema.Column`.  This
     is an optional, positional only argument that if present must be the
     first positional argument passed.  If omitted, the attribute name to
     which the :func:`_orm.mapped_column`  is mapped will be used as the SQL
     column name.
    :param __type: :class:`_types.TypeEngine` type or instance which will
     indicate the datatype to be associated with the :class:`_schema.Column`.
     This is an optional, positional-only argument that if present must
     immediately follow the ``__name`` parameter if present also, or otherwise
     be the first positional parameter.  If omitted, the ultimate type for
     the column may be derived either from the annotated type, or if a
     :class:`_schema.ForeignKey` is present, from the datatype of the
     referenced column.
    :param \\*args: Additional positional arguments include constructs such
     as :class:`_schema.ForeignKey`, :class:`_schema.CheckConstraint`,
     and :class:`_schema.Identity`, which are passed through to the constructed
     :class:`_schema.Column`.
    :param nullable: Optional bool, whether the column should be "NULL" or
     "NOT NULL". If omitted, the nullability is derived from the type
     annotation based on whether or not ``typing.Optional`` (or its equivalent)
     is present.  ``nullable`` defaults to ``True`` otherwise for non-primary
     key columns, and ``False`` for primary key columns.
    :param primary_key: optional bool, indicates the :class:`_schema.Column`
     would be part of the table\'s primary key or not.
    :param deferred: Optional bool - this keyword argument is consumed by the
     ORM declarative process, and is not part of the :class:`_schema.Column`
     itself; instead, it indicates that this column should be "deferred" for
     loading as though mapped by :func:`_orm.deferred`.

     .. seealso::

        :ref:`orm_queryguide_deferred_declarative`

    :param deferred_group: Implies :paramref:`_orm.mapped_column.deferred`
     to ``True``, and set the :paramref:`_orm.deferred.group` parameter.

     .. seealso::

        :ref:`orm_queryguide_deferred_group`

    :param deferred_raiseload: Implies :paramref:`_orm.mapped_column.deferred`
     to ``True``, and set the :paramref:`_orm.deferred.raiseload` parameter.

     .. seealso::

        :ref:`orm_queryguide_deferred_raiseload`

    :param use_existing_column: if True, will attempt to locate the given
     column name on an inherited superclass (typically single inheriting
     superclass), and if present, will not produce a new column, mapping
     to the superclass column as though it were omitted from this class.
     This is used for mixins that add new columns to an inherited superclass.

     .. seealso::

        :ref:`orm_inheritance_column_conflicts`

     .. versionadded:: 2.0.0b4

    :param default: Passed directly to the
     :paramref:`_schema.Column.default` parameter if the
     :paramref:`_orm.mapped_column.insert_default` parameter is not present.
     Additionally, when used with :ref:`orm_declarative_native_dataclasses`,
     indicates a default Python value that should be applied to the keyword
     constructor within the generated ``__init__()`` method.

     Note that in the case of dataclass generation when
     :paramref:`_orm.mapped_column.insert_default` is not present, this means
     the :paramref:`_orm.mapped_column.default` value is used in **two**
     places, both the ``__init__()`` method as well as the
     :paramref:`_schema.Column.default` parameter. While this behavior may
     change in a future release, for the moment this tends to "work out"; a
     default of ``None`` will mean that the :class:`_schema.Column` gets no
     default generator, whereas a default that refers to a non-``None`` Python
     or SQL expression value will be assigned up front on the object when
     ``__init__()`` is called, which is the same value that the Core
     :class:`_sql.Insert` construct would use in any case, leading to the same
     end result.

     .. note:: When using Core level column defaults that are callables to
        be interpreted by the underlying :class:`_schema.Column` in conjunction
        with :ref:`ORM-mapped dataclasses
        <orm_declarative_native_dataclasses>`, especially those that are
        :ref:`context-aware default functions <context_default_functions>`,
        **the** :paramref:`_orm.mapped_column.insert_default` **parameter must
        be used instead**.  This is necessary to disambiguate the callable from
        being interpreted as a dataclass level default.

     .. seealso::

        :ref:`defaults_default_factory_insert_default`

        :paramref:`_orm.mapped_column.insert_default`

        :paramref:`_orm.mapped_column.default_factory`

    :param insert_default: Passed directly to the
     :paramref:`_schema.Column.default` parameter; will supersede the value
     of :paramref:`_orm.mapped_column.default` when present, however
     :paramref:`_orm.mapped_column.default` will always apply to the
     constructor default for a dataclasses mapping.

     .. seealso::

        :ref:`defaults_default_factory_insert_default`

        :paramref:`_orm.mapped_column.default`

        :paramref:`_orm.mapped_column.default_factory`

    :param sort_order: An integer that indicates how this mapped column
     should be sorted compared to the others when the ORM is creating a
     :class:`_schema.Table`. Among mapped columns that have the same
     value the default ordering is used, placing first the mapped columns
     defined in the main class, then the ones in the super classes.
     Defaults to 0. The sort is ascending.

     .. versionadded:: 2.0.4

    :param active_history=False:

        When ``True``, indicates that the "previous" value for a
        scalar attribute should be loaded when replaced, if not
        already loaded. Normally, history tracking logic for
        simple non-primary-key scalar values only needs to be
        aware of the "new" value in order to perform a flush. This
        flag is available for applications that make use of
        :func:`.attributes.get_history` or :meth:`.Session.is_modified`
        which also need to know the "previous" value of the attribute.

        .. versionadded:: 2.0.10


    :param init: Specific to :ref:`orm_declarative_native_dataclasses`,
     specifies if the mapped attribute should be part of the ``__init__()``
     method as generated by the dataclass process.
    :param repr: Specific to :ref:`orm_declarative_native_dataclasses`,
     specifies if the mapped attribute should be part of the ``__repr__()``
     method as generated by the dataclass process.
    :param default_factory: Specific to
     :ref:`orm_declarative_native_dataclasses`,
     specifies a default-value generation function that will take place
     as part of the ``__init__()``
     method as generated by the dataclass process.

     .. seealso::

        :ref:`defaults_default_factory_insert_default`

        :paramref:`_orm.mapped_column.default`

        :paramref:`_orm.mapped_column.insert_default`

    :param compare: Specific to
     :ref:`orm_declarative_native_dataclasses`, indicates if this field
     should be included in comparison operations when generating the
     ``__eq__()`` and ``__ne__()`` methods for the mapped class.

     .. versionadded:: 2.0.0b4

    :param kw_only: Specific to
     :ref:`orm_declarative_native_dataclasses`, indicates if this field
     should be marked as keyword-only when generating the ``__init__()``.

    :param hash: Specific to
     :ref:`orm_declarative_native_dataclasses`, controls if this field
     is included when generating the ``__hash__()`` method for the mapped
     class.

     .. versionadded:: 2.0.36

    :param dataclass_metadata: Specific to
     :ref:`orm_declarative_native_dataclasses`, supplies metadata
     to be attached to the generated dataclass field.

     .. versionadded:: 2.0.42

    :param \\**kw: All remaining keyword arguments are passed through to the
     constructor for the :class:`_schema.Column`.

    '''
    pass
# WARNING: Decompyle incomplete


def orm_insert_sentinel(name = None, type_ = None, *, default, omit_from_statements):
    """Provides a surrogate :func:`_orm.mapped_column` that generates
    a so-called :term:`sentinel` column, allowing efficient bulk
    inserts with deterministic RETURNING sorting for tables that don't
    otherwise have qualifying primary key configurations.

    Use of :func:`_orm.orm_insert_sentinel` is analogous to the use of the
    :func:`_schema.insert_sentinel` construct within a Core
    :class:`_schema.Table` construct.

    Guidelines for adding this construct to a Declarative mapped class
    are the same as that of the :func:`_schema.insert_sentinel` construct;
    the database table itself also needs to have a column with this name
    present.

    For background on how this object is used, see the section
    :ref:`engine_insertmanyvalues_sentinel_columns` as part of the
    section :ref:`engine_insertmanyvalues`.

    .. seealso::

        :func:`_schema.insert_sentinel`

        :ref:`engine_insertmanyvalues`

        :ref:`engine_insertmanyvalues_sentinel_columns`


    .. versionadded:: 2.0.10

    """
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
