# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: type_api.pyc (Python 3.11)

'''Base types API.'''
from __future__ import annotations
from enum import Enum
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Mapping
from typing import NewType
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from base import SchemaEventTarget
from cache_key import CacheConst
from cache_key import NO_CACHE
from operators import ColumnOperators
from visitors import Visitable
from  import exc
from  import util
from util.typing import Protocol
from util.typing import Self
from util.typing import TypeAliasType
from util.typing import TypedDict
from util.typing import TypeGuard
if typing.TYPE_CHECKING:
    from _typing import _TypeEngineArgument
    from elements import BindParameter
    from elements import ColumnElement
    from operators import OperatorType
    from sqltypes import _resolve_value_to_type
    from sqltypes import BOOLEANTYPE
    from sqltypes import INDEXABLE
    from sqltypes import INTEGERTYPE
    from sqltypes import MATCHTYPE
    from sqltypes import NULLTYPE
    from sqltypes import NUMERICTYPE
    from sqltypes import STRINGTYPE
    from sqltypes import TABLEVALUE
    from engine.interfaces import DBAPIModule
    from engine.interfaces import Dialect
    from util.typing import GenericProtocol
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_T_con = TypeVar('_T_con', bound = Any, contravariant = True)
_O = TypeVar('_O', bound = object)
_TE = TypeVar('_TE', bound = 'TypeEngine[Any]')
_CT = TypeVar('_CT', bound = Any)
_RT = TypeVar('_RT', bound = Any)
_MatchedOnType = Union[('GenericProtocol[Any]', TypeAliasType, NewType, Type[Any])]

class _NoValueInList(Enum):
    NO_VALUE_IN_LIST = 0

_NO_VALUE_IN_LIST = _NoValueInList.NO_VALUE_IN_LIST

def _LiteralProcessorType():
    '''_LiteralProcessorType'''
    
    def __call__(self = None, value = None):
        pass


_LiteralProcessorType = <NODE:27>(_LiteralProcessorType, '_LiteralProcessorType', Protocol[_T_co])

def _BindProcessorType():
    '''_BindProcessorType'''
    
    def __call__(self = None, value = None):
        pass


_BindProcessorType = <NODE:27>(_BindProcessorType, '_BindProcessorType', Protocol[_T_con])

def _ResultProcessorType():
    '''_ResultProcessorType'''
    
    def __call__(self = None, value = None):
        pass


_ResultProcessorType = <NODE:27>(_ResultProcessorType, '_ResultProcessorType', Protocol[_T_co])

def _SentinelProcessorType():
    '''_SentinelProcessorType'''
    
    def __call__(self = None, value = None):
        pass


_SentinelProcessorType = <NODE:27>(_SentinelProcessorType, '_SentinelProcessorType', Protocol[_T_co])

class _BaseTypeMemoDict(TypedDict):
    result: 'Dict[Any, Optional[_ResultProcessorType[Any]]]' = '_BaseTypeMemoDict'


def _TypeMemoDict():
    '''_TypeMemoDict'''
    custom: 'Dict[Any, object]' = '_TypeMemoDict'

_TypeMemoDict = <NODE:27>(_TypeMemoDict, '_TypeMemoDict', _BaseTypeMemoDict, total = False)

def _ComparatorFactory():
    '''_ComparatorFactory'''
    
    def __call__(self = None, expr = None):
        pass


_ComparatorFactory = <NODE:27>(_ComparatorFactory, '_ComparatorFactory', Protocol[_T])

def TypeEngine():
    '''TypeEngine'''
    __doc__ = 'The ultimate base class for all SQL datatypes.\n\n    Common subclasses of :class:`.TypeEngine` include\n    :class:`.String`, :class:`.Integer`, and :class:`.Boolean`.\n\n    For an overview of the SQLAlchemy typing system, see\n    :ref:`types_toplevel`.\n\n    .. seealso::\n\n        :ref:`types_toplevel`\n\n    '
    _sqla_type = True
    _isnull = False
    _is_tuple_type = False
    _is_table_value = False
    _is_array = False
    _is_type_decorator = False
    render_bind_cast = False
    render_literal_cast = False
    
    def Comparator():
        '''TypeEngine.Comparator'''
        __doc__ = 'Base class for custom comparison operations defined at the\n        type level.  See :attr:`.TypeEngine.comparator_factory`.\n\n\n        '
        type: 'TypeEngine[_CT]' = ('expr', 'type')
        
        def __clause_element__(self = None):
            return self.expr

        
        def __init__(self = None, expr = None):
            self.expr = expr
            self.type = expr.type

        
        def __reduce__(self = None):
            return (self.__class__, (self.expr,))

        operate = (lambda self = None, op = None, *, result_type, other = None: pass)()
        operate = (lambda self = None, op = None: pass)()
        operate = (lambda self = None, op = None: default_comparator = util.preloaded.sql_default_comparator(op_fn, addtl_kw) = default_comparator.operator_lookup[op.__name__]if kwargs:
addtl_kw = addtl_kw.union(kwargs)# WARNING: Decompyle incomplete
)()
        reverse_operate = (lambda self = None, op = None, other = util.preload_module('sqlalchemy.sql.default_comparator'): default_comparator = util.preloaded.sql_default_comparator(op_fn, addtl_kw) = default_comparator.operator_lookup[op.__name__]if kwargs:
addtl_kw = addtl_kw.union(kwargs)# WARNING: Decompyle incomplete
)()
        
        def _adapt_expression(self = None, op = None, other_comparator = None):
            '''evaluate the return type of <self> <op> <othertype>,
            and apply any adaptations to the given operator.

            This method determines the type of a resulting binary expression
            given two source types and an operator.   For example, two
            :class:`_schema.Column` objects, both of the type
            :class:`.Integer`, will
            produce a :class:`.BinaryExpression` that also has the type
            :class:`.Integer` when compared via the addition (``+``) operator.
            However, using the addition operator with an :class:`.Integer`
            and a :class:`.Date` object will produce a :class:`.Date`, assuming
            "days delta" behavior by the database (in reality, most databases
            other than PostgreSQL don\'t accept this particular operation).

            The method returns a tuple of the form <operator>, <type>.
            The resulting operator and type will be those applied to the
            resulting :class:`.BinaryExpression` as the final operator and the
            right-hand side of the expression.

            Note that only a subset of operators make usage of
            :meth:`._adapt_expression`,
            including math operators and user-defined operators, but not
            boolean comparison or special SQL keywords like MATCH or BETWEEN.

            '''
            return (op, self.type)


    Comparator = <NODE:27>(Comparator, 'Comparator', ColumnOperators, Generic[_CT])
    hashable = True
    comparator_factory: '_ComparatorFactory[Any]' = Comparator
    sort_key_function: 'Optional[Callable[[Any], Any]]' = None
    should_evaluate_none: 'bool' = False
    _variant_mapping: 'util.immutabledict[str, TypeEngine[Any]]' = util.EMPTY_DICT
    
    def evaluates_none(self = None):
        '''Return a copy of this type which has the
        :attr:`.should_evaluate_none` flag set to True.

        E.g.::

                Table(
                    "some_table",
                    metadata,
                    Column(
                        String(50).evaluates_none(),
                        nullable=True,
                        server_default="no value",
                    ),
                )

        The ORM uses this flag to indicate that a positive value of ``None``
        is passed to the column in an INSERT statement, rather than omitting
        the column from the INSERT statement which has the effect of firing
        off column-level defaults.   It also allows for types which have
        special behavior associated with the Python None value to indicate
        that the value doesn\'t necessarily translate into SQL NULL; a
        prime example of this is a JSON type which may wish to persist the
        JSON value ``\'null\'``.

        In all cases, the actual NULL SQL value can be always be
        persisted in any column by using
        the :obj:`_expression.null` SQL construct in an INSERT statement
        or associated with an ORM-mapped attribute.

        .. note::

            The "evaluates none" flag does **not** apply to a value
            of ``None`` passed to :paramref:`_schema.Column.default` or
            :paramref:`_schema.Column.server_default`; in these cases,
            ``None``
            still means "no default".

        .. seealso::

            :ref:`session_forcing_null` - in the ORM documentation

            :paramref:`.postgresql.JSON.none_as_null` - PostgreSQL JSON
            interaction with this flag.

            :attr:`.TypeEngine.should_evaluate_none` - class-level flag

        '''
        typ = self.copy()
        typ.should_evaluate_none = True
        return typ

    
    def copy(self = None, **kw):
        return self.adapt(self.__class__)

    
    def copy_value(self = None, value = None):
        return value

    
    def literal_processor(self = None, dialect = None):
        '''Return a conversion function for processing literal values that are
        to be rendered directly without using binds.

        This function is used when the compiler makes use of the
        "literal_binds" flag, typically used in DDL generation as well
        as in certain scenarios where backends don\'t accept bound parameters.

        Returns a callable which will receive a literal Python value
        as the sole positional argument and will return a string representation
        to be rendered in a SQL statement.

        .. tip::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it\'s not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.literal_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.literal_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_literal_param`.

            .. seealso::

                :ref:`types_typedecorator`


        '''
        pass

    
    def bind_processor(self = None, dialect = None):
        """Return a conversion function for processing bind values.

        Returns a callable which will receive a bind parameter value
        as the sole positional argument and will return a value to
        send to the DB-API.

        If processing is not necessary, the method should return ``None``.

        .. tip::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.bind_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.bind_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_bind_param`.

            .. seealso::

                :ref:`types_typedecorator`


        :param dialect: Dialect instance in use.

        """
        pass

    
    def result_processor(self = None, dialect = None, coltype = None):
        """Return a conversion function for processing result row values.

        Returns a callable which will receive a result row column
        value as the sole positional argument and will return a value
        to return to the user.

        If processing is not necessary, the method should return ``None``.

        .. tip::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.result_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.result_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_result_value`.

            .. seealso::

                :ref:`types_typedecorator`

        :param dialect: Dialect instance in use.

        :param coltype: DBAPI coltype argument received in cursor.description.

        """
        pass

    
    def column_expression(self = None, colexpr = None):
        """Given a SELECT column expression, return a wrapping SQL expression.

        This is typically a SQL function that wraps a column expression
        as rendered in the columns clause of a SELECT statement.
        It is used for special data types that require
        columns to be wrapped in some special database function in order
        to coerce the value before being sent back to the application.
        It is the SQL analogue of the :meth:`.TypeEngine.result_processor`
        method.

        .. note:: The :func:`.TypeEngine.column_expression` method is applied
           only to the **outermost columns clause** of a SELECT statement, that
           is, the columns that are to be delivered directly into the returned
           result rows.  It does **not** apply to the columns clause inside
           of subqueries.  This necessarily avoids double conversions against
           the column and only runs the conversion when ready to be returned
           to the client.

        This method is called during the **SQL compilation** phase of a
        statement, when rendering a SQL string. It is **not** called
        against specific values.

        .. tip::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.column_expression`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.column_expression`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.column_expression`.

            .. seealso::

                :ref:`types_typedecorator`


        .. seealso::

            :ref:`types_sql_value_processing`

        """
        pass

    _has_column_expression = (lambda self = None: self.__class__.column_expression.__code__ is not TypeEngine.column_expression.__code__)()
    
    def bind_expression(self = None, bindvalue = None):
        """Given a bind value (i.e. a :class:`.BindParameter` instance),
        return a SQL expression in its place.

        This is typically a SQL function that wraps the existing bound
        parameter within the statement.  It is used for special data types
        that require literals being wrapped in some special database function
        in order to coerce an application-level value into a database-specific
        format.  It is the SQL analogue of the
        :meth:`.TypeEngine.bind_processor` method.

        This method is called during the **SQL compilation** phase of a
        statement, when rendering a SQL string. It is **not** called
        against specific values.

        Note that this method, when implemented, should always return
        the exact same structure, without any conditional logic, as it
        may be used in an executemany() call against an arbitrary number
        of bound parameter sets.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.bind_expression`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.bind_expression`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.bind_expression`.

            .. seealso::

                :ref:`types_typedecorator`

        .. seealso::

            :ref:`types_sql_value_processing`

        """
        pass

    _has_bind_expression = (lambda self = None: util.method_is_overridden(self, TypeEngine.bind_expression))()
    _to_instance = (lambda cls_or_self = None: to_instance(cls_or_self))()
    
    def compare_values(self = None, x = None, y = None):
        '''Compare two values for equality.'''
        return x == y

    
    def get_dbapi_type(self = None, dbapi = None):
        '''Return the corresponding type object from the underlying DB-API, if
        any.

        This can be useful for calling ``setinputsizes()``, for example.

        '''
        pass

    python_type = (lambda self = None: raise NotImplementedError())()
    
    def with_variant(self = None, type_ = None, *dialect_names):
        '''Produce a copy of this type object that will utilize the given
        type when applied to the dialect of the given name.

        e.g.::

            from sqlalchemy.types import String
            from sqlalchemy.dialects import mysql

            string_type = String()

            string_type = string_type.with_variant(
                mysql.VARCHAR(collation="foo"), "mysql", "mariadb"
            )

        The variant mapping indicates that when this type is
        interpreted by a specific dialect, it will instead be
        transmuted into the given type, rather than using the
        primary type.

        .. versionchanged:: 2.0 the :meth:`_types.TypeEngine.with_variant`
           method now works with a :class:`_types.TypeEngine` object "in
           place", returning a copy of the original type rather than returning
           a wrapping object; the ``Variant`` class is no longer used.

        :param type\\_: a :class:`.TypeEngine` that will be selected
         as a variant from the originating type, when a dialect
         of the given name is in use.
        :param \\*dialect_names: one or more base names of the dialect which
         uses this type. (i.e. ``\'postgresql\'``, ``\'mysql\'``, etc.)

         .. versionchanged:: 2.0 multiple dialect names can be specified
            for one variant.

        .. seealso::

            :ref:`types_with_variant` - illustrates the use of
            :meth:`_types.TypeEngine.with_variant`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _resolve_for_literal(self = None, value = None):
        '''adjust this type given a literal Python value that will be
        stored in a bound parameter.

        Used exclusively by _resolve_value_to_type().

        .. versionadded:: 1.4.30 or 2.0

        TODO: this should be part of public API

        .. seealso::

            :meth:`.TypeEngine._resolve_for_python_type`

        '''
        return self

    
    def _resolve_for_python_type(self = None, python_type = None, matched_on = None, matched_on_flattened = ('python_type', 'Type[Any]', 'matched_on', '_MatchedOnType', 'matched_on_flattened', 'Type[Any]', 'return', 'Optional[Self]')):
        """given a Python type (e.g. ``int``, ``str``, etc. ) return an
        instance of this :class:`.TypeEngine` that's appropriate for this type.

        An additional argument ``matched_on`` is passed, which indicates an
        entry from the ``__mro__`` of the given ``python_type`` that more
        specifically matches how the caller located this :class:`.TypeEngine`
        object.   Such as, if a lookup of some kind links the ``int`` Python
        type to the :class:`.Integer` SQL type, and the original object
        was some custom subclass of ``int`` such as ``MyInt(int)``, the
        arguments passed would be ``(MyInt, int)``.

        If the given Python type does not correspond to this
        :class:`.TypeEngine`, or the Python type is otherwise ambiguous, the
        method should return None.

        For simple cases, the method checks that the ``python_type``
        and ``matched_on`` types are the same (i.e. not a subclass), and
        returns self; for all other cases, it returns ``None``.

        The initial use case here is for the ORM to link user-defined
        Python standard library ``enum.Enum`` classes to the SQLAlchemy
        :class:`.Enum` SQL type when constructing ORM Declarative mappings.

        :param python_type: the Python type we want to use
        :param matched_on: the Python type that led us to choose this
         particular :class:`.TypeEngine` class, which would be a supertype
         of ``python_type``.   By default, the request is rejected if
         ``python_type`` doesn't match ``matched_on`` (None is returned).

        .. versionadded:: 2.0.0b4

        TODO: this should be part of public API

        .. seealso::

            :meth:`.TypeEngine._resolve_for_literal`

        """
        if python_type is not matched_on_flattened:
            return None

    
    def _with_collation(self = None, collation = None):
        '''set up error handling for the collate expression'''
        raise NotImplementedError('this datatype does not support collation')

    _type_affinity = (lambda self = None: typ = Nonefor t in self.__class__.__mro__:
if t is TypeEngine or TypeEngineMixin in t.__bases__:
None, typif None(t, TypeEngine):
passself.__class__)()
    _generic_type_affinity = (lambda self = None:
