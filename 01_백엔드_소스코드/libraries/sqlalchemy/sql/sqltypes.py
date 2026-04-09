# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sqltypes.pyc (Python 3.11)

'''SQL specific types.'''
from __future__ import annotations
from collections.abc import abc as collections_abc
import datetime as dt
import decimal
import enum
import json
import pickle
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from uuid import UUID as _python_UUID
from  import coercions
from  import elements
from  import operators
from  import roles
from  import type_api
from base import _NONE_NAME
from base import NO_ARG
from base import SchemaEventTarget
from cache_key import HasCacheKey
from elements import quoted_name
from elements import Slice
from elements import TypeCoerce as type_coerce
from type_api import Emulated
from type_api import NativeForEmulated
from type_api import to_instance
from type_api import TypeDecorator
from type_api import TypeEngine
from type_api import TypeEngineMixin
from type_api import Variant
from visitors import InternalTraversal
from  import event
from  import exc
from  import inspection
from  import util
from engine import processors
from util import langhelpers
from util import OrderedDict
from util import warn_deprecated
from util.typing import get_args
from util.typing import is_literal
from util.typing import is_pep695
from util.typing import Literal
if TYPE_CHECKING:
    from _typing import _ColumnExpressionArgument
    from _typing import _CreateDropBind
    from _typing import _TypeEngineArgument
    from elements import ColumnElement
    from operators import OperatorType
    from schema import MetaData
    from type_api import _BindProcessorType
    from type_api import _ComparatorFactory
    from type_api import _LiteralProcessorType
    from type_api import _MatchedOnType
    from type_api import _ResultProcessorType
    from engine.interfaces import Dialect
_T = TypeVar('_T', bound = 'Any')
_CT = TypeVar('_CT', bound = Any)
_TE = TypeVar('_TE', bound = 'TypeEngine[Any]')
_P = TypeVar('_P')

class HasExpressionLookup(TypeEngineMixin):
    '''Mixin expression adaptations based on lookup tables.

    These rules are currently used by the numeric, integer and date types
    which have detailed cross-expression coercion rules.

    '''
    _expression_adaptations = (lambda self: raise NotImplementedError())()
    
    def Comparator():
        '''HasExpressionLookup.Comparator'''
        __slots__ = ()
        _blank_dict = util.EMPTY_DICT
        
        def _adapt_expression(self = None, op = None, other_comparator = None):
            othertype = other_comparator.type._type_affinity
        # WARNING: Decompyle incomplete


    Comparator = <NODE:27>(Comparator, 'Comparator', TypeEngine.Comparator[_CT])
    comparator_factory: '_ComparatorFactory[Any]' = Comparator


class Concatenable(TypeEngineMixin):
    """A mixin that marks a type as supporting 'concatenation',
    typically strings."""
    
    def Comparator():
        '''Concatenable.Comparator'''
        pass
    # WARNING: Decompyle incomplete

    Comparator = <NODE:27>(Comparator, 'Comparator', TypeEngine.Comparator[_T])
    comparator_factory: '_ComparatorFactory[Any]' = Comparator


class Indexable(TypeEngineMixin):
    '''A mixin that marks a type as supporting indexing operations,
    such as array or JSON structures.

    '''
    
    def Comparator():
        '''Indexable.Comparator'''
        __slots__ = ()
        
        def _setup_getitem(self, index):
            raise NotImplementedError()

        
        def __getitem__(self, index):
            (adjusted_op, adjusted_right_expr, result_type) = self._setup_getitem(index)
            return self.operate(adjusted_op, adjusted_right_expr, result_type = result_type)


    Comparator = <NODE:27>(Comparator, 'Comparator', TypeEngine.Comparator[_T])
    comparator_factory: '_ComparatorFactory[Any]' = Comparator


def String():
    '''String'''
    __doc__ = 'The base for all string and character types.\n\n    In SQL, corresponds to VARCHAR.\n\n    The `length` field is usually required when the `String` type is\n    used within a CREATE TABLE statement, as VARCHAR requires a length\n    on most databases.\n\n    '
    __visit_name__ = 'string'
    
    def __init__(self = None, length = None, collation = None):
        '''
        Create a string-holding type.

        :param length: optional, a length for the column for use in
          DDL and CAST expressions.  May be safely omitted if no ``CREATE
          TABLE`` will be issued.  Certain databases may require a
          ``length`` for use in DDL, and will raise an exception when
          the ``CREATE TABLE`` DDL is issued if a ``VARCHAR``
          with no length is included.  Whether the value is
          interpreted as bytes or characters is database specific.

        :param collation: Optional, a column-level collation for
          use in DDL and CAST expressions.  Renders using the
          COLLATE keyword supported by SQLite, MySQL, and PostgreSQL.
          E.g.:

          .. sourcecode:: pycon+sql

            >>> from sqlalchemy import cast, select, String
            >>> print(select(cast("some string", String(collation="utf8"))))
            {printsql}SELECT CAST(:param_1 AS VARCHAR COLLATE utf8) AS anon_1

          .. note::

            In most cases, the :class:`.Unicode` or :class:`.UnicodeText`
            datatypes should be used for a :class:`_schema.Column` that expects
            to store non-ascii data. These datatypes will ensure that the
            correct types are used on the database.

        '''
        self.length = length
        self.collation = collation

    
    def _with_collation(self, collation):
        new_type = self.copy()
        new_type.collation = collation
        return new_type

    
    def _resolve_for_literal(self, value):
        if value.isascii():
            return _STRING

    
    def literal_processor(self, dialect):
        pass
    # WARNING: Decompyle incomplete

    
    def bind_processor(self = None, dialect = None):
        pass

    
    def result_processor(self = None, dialect = None, coltype = None):
        pass

    python_type = (lambda self: str)()
    
    def get_dbapi_type(self, dbapi):
        return dbapi.STRING


String = <NODE:27>(String, 'String', Concatenable, TypeEngine[str])

class Text(String):
    '''A variably sized string type.

    In SQL, usually corresponds to CLOB or TEXT.  In general, TEXT objects
    do not have a length; while some databases will accept a length
    argument here, it will be rejected by others.

    '''
    __visit_name__ = 'text'


class Unicode(String):
    '''A variable length Unicode string type.

    The :class:`.Unicode` type is a :class:`.String` subclass that assumes
    input and output strings that may contain non-ASCII characters, and for
    some backends implies an underlying column type that is explicitly
    supporting of non-ASCII data, such as ``NVARCHAR`` on Oracle Database and
    SQL Server.  This will impact the output of ``CREATE TABLE`` statements and
    ``CAST`` functions at the dialect level.

    The character encoding used by the :class:`.Unicode` type that is used to
    transmit and receive data to the database is usually determined by the
    DBAPI itself. All modern DBAPIs accommodate non-ASCII strings but may have
    different methods of managing database encodings; if necessary, this
    encoding should be configured as detailed in the notes for the target DBAPI
    in the :ref:`dialect_toplevel` section.

    In modern SQLAlchemy, use of the :class:`.Unicode` datatype does not
    imply any encoding/decoding behavior within SQLAlchemy itself.  In Python
    3, all string objects are inherently Unicode capable, and SQLAlchemy
    does not produce bytestring objects nor does it accommodate a DBAPI that
    does not return Python Unicode objects in result sets for string values.

    .. warning:: Some database backends, particularly SQL Server with pyodbc,
       are known to have undesirable behaviors regarding data that is noted
       as being of ``NVARCHAR`` type as opposed to ``VARCHAR``, including
       datatype mismatch errors and non-use of indexes.  See the section
       on :meth:`.DialectEvents.do_setinputsizes` for background on working
       around unicode character issues for backends like SQL Server with
       pyodbc as well as cx_Oracle.

    .. seealso::

        :class:`.UnicodeText` - unlengthed textual counterpart
        to :class:`.Unicode`.

        :meth:`.DialectEvents.do_setinputsizes`

    '''
    __visit_name__ = 'unicode'


class UnicodeText(Text):
    '''An unbounded-length Unicode string type.

    See :class:`.Unicode` for details on the unicode
    behavior of this object.

    Like :class:`.Unicode`, usage the :class:`.UnicodeText` type implies a
    unicode-capable type being used on the backend, such as
    ``NCLOB``, ``NTEXT``.

    '''
    __visit_name__ = 'unicode_text'


def Integer():
    '''Integer'''
    __doc__ = 'A type for ``int`` integers.'
    __visit_name__ = 'integer'
    if TYPE_CHECKING:
        _type_affinity = (lambda self = None: pass)()
    
    def get_dbapi_type(self, dbapi):
        return dbapi.NUMBER

    python_type = (lambda self: int)()
    
    def _resolve_for_literal(self, value):
        if value.bit_length() >= 32:
            return _BIGINTEGER

    
    def literal_processor(self, dialect):
        
        def process(value):
            return str(int(value))

        return process

    _expression_adaptations = (lambda self: {
operators.sub: {
Numeric: Numeric,
Integer: self.__class__ },
operators.floordiv: {
Numeric: Numeric,
Integer: self.__class__ },
operators.truediv: {
Numeric: Numeric,
Integer: Numeric },
operators.mul: {
Numeric: Numeric,
Integer: self.__class__,
Interval: Interval },
operators.add: {
Numeric: Numeric,
Integer: self.__class__,
Date: Date } })()

Integer = <NODE:27>(Integer, 'Integer', HasExpressionLookup, TypeEngine[int])

class SmallInteger(Integer):
    '''A type for smaller ``int`` integers.

    Typically generates a ``SMALLINT`` in DDL, and otherwise acts like
    a normal :class:`.Integer` on the Python side.

    '''
    __visit_name__ = 'small_integer'


class BigInteger(Integer):
    '''A type for bigger ``int`` integers.

    Typically generates a ``BIGINT`` in DDL, and otherwise acts like
    a normal :class:`.Integer` on the Python side.

    '''
    __visit_name__ = 'big_integer'

_N = TypeVar('_N', bound = Union[(decimal.Decimal, float)])

def Numeric():
    '''Numeric'''
    __doc__ = 'Base for non-integer numeric types, such as\n    ``NUMERIC``, ``FLOAT``, ``DECIMAL``, and other variants.\n\n    The :class:`.Numeric` datatype when used directly will render DDL\n    corresponding to precision numerics if available, such as\n    ``NUMERIC(precision, scale)``.  The :class:`.Float` subclass will\n    attempt to render a floating-point datatype such as ``FLOAT(precision)``.\n\n    :class:`.Numeric` returns Python ``decimal.Decimal`` objects by default,\n    based on the default value of ``True`` for the\n    :paramref:`.Numeric.asdecimal` parameter.  If this parameter is set to\n    False, returned values are coerced to Python ``float`` objects.\n\n    The :class:`.Float` subtype, being more specific to floating point,\n    defaults the :paramref:`.Float.asdecimal` flag to False so that the\n    default Python datatype is ``float``.\n\n    .. note::\n\n        When using a :class:`.Numeric` datatype against a database type that\n        returns Python floating point values to the driver, the accuracy of the\n        decimal conversion indicated by :paramref:`.Numeric.asdecimal` may be\n        limited.   The behavior of specific numeric/floating point datatypes\n        is a product of the SQL datatype in use, the Python :term:`DBAPI`\n        in use, as well as strategies that may be present within\n        the SQLAlchemy dialect in use.   Users requiring specific precision/\n        scale are encouraged to experiment with the available datatypes\n        in order to determine the best results.\n\n    '
    __visit_name__ = 'numeric'
    if TYPE_CHECKING:
        _type_affinity = (lambda self = None: pass)()
    _default_decimal_return_scale = 10
    __init__ = (lambda self = None, precision = None, scale = overload, decimal_return_scale = (..., ..., ..., ...), asdecimal = ('self', 'Numeric[decimal.Decimal]', 'precision', 'Optional[int]', 'scale', 'Optional[int]', 'decimal_return_scale', 'Optional[int]', 'asdecimal', 'Literal[True]'): pass)()
    __init__ = (lambda self = None, precision = None, scale = overload, decimal_return_scale = (..., ..., ..., ...), asdecimal = ('self', 'Numeric[float]', 'precision', 'Optional[int]', 'scale', 'Optional[int]', 'decimal_return_scale', 'Optional[int]', 'asdecimal', 'Literal[False]'): pass)()
    
    def __init__(self = None, precision = None, scale = None, decimal_return_scale = (None, None, None, True), asdecimal = ('precision', 'Optional[int]', 'scale', 'Optional[int]', 'decimal_return_scale', 'Optional[int]', 'asdecimal', 'bool')):
        '''
        Construct a Numeric.

        :param precision: the numeric precision for use in DDL ``CREATE
          TABLE``.

        :param scale: the numeric scale for use in DDL ``CREATE TABLE``.

        :param asdecimal: default True.  Return whether or not
          values should be sent as Python Decimal objects, or
          as floats.   Different DBAPIs send one or the other based on
          datatypes - the Numeric type will ensure that return values
          are one or the other across DBAPIs consistently.

        :param decimal_return_scale: Default scale to use when converting
         from floats to Python decimals.  Floating point values will typically
         be much longer due to decimal inaccuracy, and most floating point
         database types don\'t have a notion of "scale", so by default the
         float type looks for the first ten decimal places when converting.
         Specifying this value will override that length.  Types which
         do include an explicit ".scale" value, such as the base
         :class:`.Numeric` as well as the MySQL float types, will use the
         value of ".scale" as the default for decimal_return_scale, if not
         otherwise specified.

        When using the ``Numeric`` type, care should be taken to ensure
        that the asdecimal setting is appropriate for the DBAPI in use -
        when Numeric applies a conversion from Decimal->float or float->
        Decimal, this conversion incurs an additional performance overhead
        for all result columns received.

        DBAPIs that return Decimal natively (e.g. psycopg2) will have
        better accuracy and higher performance with a setting of ``True``,
        as the native translation to Decimal reduces the amount of floating-
        point issues at play, and the Numeric type itself doesn\'t need
        to apply any further conversions.  However, another DBAPI which
        returns floats natively *will* incur an additional conversion
        overhead, and is still subject to floating point data loss - in
        which case ``asdecimal=False`` will at least remove the extra
        conversion overhead.

        '''
        self.precision = precision
        self.scale = scale
        self.decimal_return_scale = decimal_return_scale
        self.asdecimal = asdecimal

    _effective_decimal_return_scale = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def get_dbapi_type(self, dbapi):
        return dbapi.NUMBER

    
    def literal_processor(self, dialect):
        
        def process(value):
            return str(value)

        return process

    python_type = (lambda self: if self.asdecimal:
decimal.Decimal)()
    
    def bind_processor(self, dialect):
        if dialect.supports_native_decimal:
            return None
        return None.to_float

    
    def result_processor(self, dialect, coltype):
        pass
    # WARNING: Decompyle incomplete

    _expression_adaptations = (lambda self: {
operators.sub: {
Integer: self.__class__,
Numeric: self.__class__ },
operators.add: {
Integer: self.__class__,
Numeric: self.__class__ },
operators.truediv: {
Integer: self.__class__,
Numeric: self.__class__ },
operators.mul: {
Integer: self.__class__,
Numeric: self.__class__,
Interval: Interval } })()

Numeric = <NODE:27>(Numeric, 'Numeric', HasExpressionLookup, TypeEngine[_N])

def Float():
    '''Float'''
    __doc__ = "Type representing floating point types, such as ``FLOAT`` or ``REAL``.\n\n    This type returns Python ``float`` objects by default, unless the\n    :paramref:`.Float.asdecimal` flag is set to ``True``, in which case they\n    are coerced to ``decimal.Decimal`` objects.\n\n    When a :paramref:`.Float.precision` is not provided in a\n    :class:`_types.Float` type some backend may compile this type as\n    an 8 bytes / 64 bit float datatype. To use a 4 bytes / 32 bit float\n    datatype a precision <= 24 can usually be provided or the\n    :class:`_types.REAL` type can be used.\n    This is known to be the case in the PostgreSQL and MSSQL dialects\n    that render the type as ``FLOAT`` that's in both an alias of\n    ``DOUBLE PRECISION``. Other third party dialects may have similar\n    behavior.\n    "
    __visit_name__ = 'float'
    if not TYPE_CHECKING:
        scale = None
    __init__ = (lambda self = None, precision = None, asdecimal = overload, decimal_return_scale = (..., ..., ...): pass)()
    __init__ = (lambda self = None, precision = None, asdecimal = overload, decimal_return_scale = (..., ..., ...): pass)()
    
    def __init__(self = None, precision = None, asdecimal = None, decimal_return_scale = (None, False, None)):
        '''
        Construct a Float.

        :param precision: the numeric precision for use in DDL ``CREATE
           TABLE``. Backends **should** attempt to ensure this precision
           indicates a number of digits for the generic
           :class:`_sqltypes.Float` datatype.

           .. note:: For the Oracle Database backend, the
              :paramref:`_sqltypes.Float.precision` parameter is not accepted
              when rendering DDL, as Oracle Database does not support float precision
              specified as a number of decimal places. Instead, use the
              Oracle Database-specific :class:`_oracle.FLOAT` datatype and specify the
              :paramref:`_oracle.FLOAT.binary_precision` parameter. This is new
              in version 2.0 of SQLAlchemy.

              To create a database agnostic :class:`_types.Float` that
              separately specifies binary precision for Oracle Database, use
              :meth:`_types.TypeEngine.with_variant` as follows::

                    from sqlalchemy import Column
                    from sqlalchemy import Float
                    from sqlalchemy.dialects import oracle

                    Column(
                        "float_data",
                        Float(5).with_variant(oracle.FLOAT(binary_precision=16), "oracle"),
                    )

        :param asdecimal: the same flag as that of :class:`.Numeric`, but
          defaults to ``False``.   Note that setting this flag to ``True``
          results in floating point conversion.

        :param decimal_return_scale: Default scale to use when converting
         from floats to Python decimals.  Floating point values will typically
         be much longer due to decimal inaccuracy, and most floating point
         database types don\'t have a notion of "scale", so by default the
         float type looks for the first ten decimal places when converting.
         Specifying this value will override that length.  Note that the
         MySQL float types, which do include "scale", will use "scale"
         as the default for decimal_return_scale, if not otherwise specified.

        '''
        self.precision = precision
        self.asdecimal = asdecimal
        self.decimal_return_scale = decimal_return_scale

    
    def result_processor(self, dialect, coltype):
        if self.asdecimal:
            return processors.to_decimal_processor_factory(decimal.Decimal, self._effective_decimal_return_scale)
        if None.supports_native_decimal:
            return processors.to_float


Float = <NODE:27>(Float, 'Float', Numeric[_N])

def Double():
    '''Double'''
    __doc__ = 'A type for double ``FLOAT`` floating point types.\n\n    Typically generates a ``DOUBLE`` or ``DOUBLE_PRECISION`` in DDL,\n    and otherwise acts like a normal :class:`.Float` on the Python\n    side.\n\n    .. versionadded:: 2.0\n\n    '
    __visit_name__ = 'double'

Double = <NODE:27>(Double, 'Double', Float[_N])

class _RenderISO8601NoT:
    
    def _literal_processor_datetime(self, dialect):
        return self._literal_processor_portion(dialect, None)

    
    def _literal_processor_date(self, dialect):
        return self._literal_processor_portion(dialect, 0)

    
    def _literal_processor_time(self, dialect):
        return self._literal_processor_portion(dialect, -1)

    
    def _literal_processor_portion(self, dialect, _portion = (None,)):
        pass
    # WARNING: Decompyle incomplete



def DateTime():
    '''DateTime'''
    __doc__ = 'A type for ``datetime.datetime()`` objects.\n\n    Date and time types return objects from the Python ``datetime``\n    module.  Most DBAPIs have built in support for the datetime\n    module, with the noted exception of SQLite.  In the case of\n    SQLite, date and time types are stored as strings which are then\n    converted back to datetime objects when rows are returned.\n\n    For the time representation within the datetime type, some\n    backends include additional options, such as timezone support and\n    fractional seconds support.  For fractional seconds, use the\n    dialect-specific datatype, such as :class:`.mysql.TIME`.  For\n    timezone support, use at least the :class:`_types.TIMESTAMP` datatype,\n    if not the dialect-specific datatype object.\n\n    '
    __visit_name__ = 'datetime'
    
    def __init__(self = None, timezone = None):
        '''Construct a new :class:`.DateTime`.

        :param timezone: boolean.  Indicates that the datetime type should
         enable timezone support, if available on the
         **base date/time-holding type only**.   It is recommended
         to make use of the :class:`_types.TIMESTAMP` datatype directly when
         using this flag, as some databases include separate generic
         date/time-holding types distinct from the timezone-capable
         TIMESTAMP datatype, such as Oracle Database.


        '''
        self.timezone = timezone

    
    def get_dbapi_type(self, dbapi):
        return dbapi.DATETIME

    
    def _resolve_for_literal(self, value):
        with_timezone = value.tzinfo is not None
        if not with_timezone and self.timezone:
            return DATETIME_TIMEZONE

    
    def literal_processor(self, dialect):
        return self._literal_processor_datetime(dialect)

    python_type = (lambda self: dt.datetime)()
    _expression_adaptations = (lambda self: {
operators.sub: {
DateTime: Interval,
Interval: self.__class__ },
operators.add: {
Interval: self.__class__ } })()

DateTime = <NODE:27>(DateTime, 'DateTime', _RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.datetime])

def Date():
    '''Date'''
    __doc__ = 'A type for ``datetime.date()`` objects.'
    __visit_name__ = 'date'
    
    def get_dbapi_type(self, dbapi):
        return dbapi.DATETIME

    python_type = (lambda self: dt.date)()
    
    def literal_processor(self, dialect):
        return self._literal_processor_date(dialect)

    _expression_adaptations = (lambda self: {
operators.sub: {
DateTime: Interval,
Interval: DateTime,
Date: Integer,
Integer: self.__class__ },
operators.add: {
Time: DateTime,
Interval: DateTime,
Integer: self.__class__ } })()

Date = <NODE:27>(Date, 'Date', _RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.date])

def Time():
    '''Time'''
    __doc__ = 'A type for ``datetime.time()`` objects.'
    __visit_name__ = 'time'
    
    def __init__(self = None, timezone = None):
        self.timezone = timezone

    
    def get_dbapi_type(self, dbapi):
        return dbapi.DATETIME

    python_type = (lambda self: dt.time)()
    
    def _resolve_for_literal(self, value):
        with_timezone = value.tzinfo is not None
        if not with_timezone and self.timezone:
            return TIME_TIMEZONE

    _expression_adaptations = (lambda self: {
operators.sub: {
Interval: self.__class__,
Time: Interval },
operators.add: {
Interval: self.__class__,
Date: DateTime } })()
    
    def literal_processor(self, dialect):
        return self._literal_processor_time(dialect)


Time = <NODE:27>(Time, 'Time', _RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.time])

def _Binary():
    '''_Binary'''
    pass
# WARNING: Decompyle incomplete

_Binary = <NODE:27>(_Binary, '_Binary', TypeEngine[bytes])

class LargeBinary(_Binary):
    '''A type for large binary byte data.

    The :class:`.LargeBinary` type corresponds to a large and/or unlengthed
    binary type for the target platform, such as BLOB on MySQL and BYTEA for
    PostgreSQL.  It also handles the necessary conversions for the DBAPI.

    '''
    __visit_name__ = 'large_binary'
    
    def __init__(self = None, length = None):
        '''
        Construct a LargeBinary type.

        :param length: optional, a length for the column for use in
          DDL statements, for those binary types that accept a length,
          such as the MySQL BLOB type.

        '''
        _Binary.__init__(self, length = length)



class SchemaType(TypeEngineMixin, SchemaEventTarget):
    pass
# WARNING: Decompyle incomplete

_EnumTupleArg = Union[(Sequence[enum.Enum], Sequence[str])]

def Enum():
    '''Enum'''
    pass
# WARNING: Decompyle incomplete

Enum = <NODE:27>(Enum, 'Enum', String, SchemaType, Emulated, TypeEngine[Union[(str, enum.Enum)]])

def PickleType():
    '''PickleType'''
    pass
# WARNING: Decompyle incomplete

PickleType = <NODE:27>(PickleType, 'PickleType', TypeDecorator[object])

def Boolean():
    '''Boolean'''
    __doc__ = 'A bool datatype.\n\n    :class:`.Boolean` typically uses BOOLEAN or SMALLINT on the DDL side,\n    and on the Python side deals in ``True`` or ``False``.\n\n    The :class:`.Boolean` datatype currently has two levels of assertion\n    that the values persisted are simple true/false values.  For all\n    backends, only the Python values ``None``, ``True``, ``False``, ``1``\n    or ``0`` are accepted as parameter values.   For those backends that\n    don\'t support a "native boolean" datatype, an option exists to\n    also create a CHECK constraint on the target column\n\n    .. versionchanged:: 1.2 the :class:`.Boolean` datatype now asserts that\n       incoming Python values are already in pure boolean form.\n\n\n    '
    __visit_name__ = 'boolean'
    native = True
    
    def __init__(self = None, create_constraint = None, name = None, _create_events = (False, None, True, None), _adapted_from = ('create_constraint', 'bool', 'name', 'Optional[str]', '_create_events', 'bool', '_adapted_from', 'Optional[SchemaType]')):
        '''Construct a Boolean.

        :param create_constraint: defaults to False.  If the boolean
          is generated as an int/smallint, also create a CHECK constraint
          on the table that ensures 1 or 0 as a value.

          .. note:: it is strongly recommended that the CHECK constraint
             have an explicit name in order to support schema-management
             concerns.  This can be established either by setting the
             :paramref:`.Boolean.name` parameter or by setting up an
             appropriate naming convention; see
             :ref:`constraint_naming_conventions` for background.

          .. versionchanged:: 1.4 - this flag now defaults to False, meaning
             no CHECK constraint is generated for a non-native enumerated
             type.

        :param name: if a CHECK constraint is generated, specify
          the name of the constraint.

        '''
        self.create_constraint = create_constraint
        self.name = name
        self._create_events = _create_events
        if _adapted_from:
            self.dispatch = self.dispatch._join(_adapted_from.dispatch)
            return None

    
    def copy(self, **kw):
        return self.adapt(cast('Type[TypeEngine[Any]]', self.__class__), _create_events = True)

    
    def _should_create_constraint(self, compiler, **kw):
