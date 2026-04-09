# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

'''SQL function API, factories, and built-in functions.'''
from __future__ import annotations
import datetime
import decimal
from typing import Any
from typing import cast
from typing import Dict
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
from  import annotation
from  import coercions
from  import operators
from  import roles
from  import schema
from  import sqltypes
from  import type_api
from  import util as sqlutil
from _typing import is_table_value_type
from base import _entity_namespace
from base import ColumnCollection
from base import Executable
from base import Generative
from base import HasMemoized
from elements import _type_from_args
from elements import BinaryExpression
from elements import BindParameter
from elements import Cast
from elements import ClauseList
from elements import ColumnElement
from elements import Extract
from elements import FunctionFilter
from elements import Grouping
from elements import literal_column
from elements import NamedColumn
from elements import Over
from elements import WithinGroup
from selectable import FromClause
from selectable import Select
from selectable import TableValuedAlias
from sqltypes import TableValueType
from type_api import TypeEngine
from visitors import InternalTraversal
from  import util
if TYPE_CHECKING:
    from _typing import _ByArgument
    from _typing import _ColumnExpressionArgument
    from _typing import _ColumnExpressionOrLiteralArgument
    from _typing import _ColumnExpressionOrStrLabelArgument
    from _typing import _StarOrOne
    from _typing import _TypeEngineArgument
    from base import _EntityNamespace
    from elements import ClauseElement
    from elements import KeyedColumnElement
    from elements import TableValuedColumn
    from operators import OperatorType
    from engine.base import Connection
    from engine.cursor import CursorResult
    from engine.interfaces import _CoreMultiExecuteParams
    from engine.interfaces import CoreExecuteOptionsParameter
    from util.typing import Self
_T = TypeVar('_T', bound = Any)
_S = TypeVar('_S', bound = Any)
_registry: 'util.defaultdict[str, Dict[str, Type[Function[Any]]]]' = util.defaultdict(dict)

def register_function(identifier = None, fn = None, package = None):
    '''Associate a callable with a particular func. name.

    This is normally called by GenericFunction, but is also
    available by itself so that a non-Function construct
    can be associated with the :data:`.func` accessor (i.e.
    CAST, EXTRACT).

    '''
    reg = _registry[package]
    identifier = str(identifier).lower()
    if identifier in reg:
        util.warn("The GenericFunction '{}' is already registered and is going to be overridden.".format(identifier))
    reg[identifier] = fn


def FunctionElement():
    '''FunctionElement'''
    pass
# WARNING: Decompyle incomplete

FunctionElement = <NODE:27>(FunctionElement, 'FunctionElement', Executable, ColumnElement[_T], FromClause, Generative)

def FunctionAsBinary():
    '''FunctionAsBinary'''
    right_index: 'int' = [
        ('sql_function', InternalTraversal.dp_clauseelement),
        ('left_index', InternalTraversal.dp_plain_obj),
        ('right_index', InternalTraversal.dp_plain_obj),
        ('modifiers', InternalTraversal.dp_plain_dict)]
    
    def _gen_cache_key(self = None, anon_map = None, bindparams = None):
        return ColumnElement._gen_cache_key(self, anon_map, bindparams)

    
    def __init__(self = None, fn = None, left_index = None, right_index = ('fn', 'FunctionElement[Any]', 'left_index', 'int', 'right_index', 'int', 'return', 'None')):
        self.sql_function = fn
        self.left_index = left_index
        self.right_index = right_index
        self.operator = operators.function_as_comparison_op
        self.type = sqltypes.BOOLEANTYPE
        self.negate = None
        self._is_implicitly_boolean = True
        self.modifiers = util.immutabledict({ })

    left_expr = (lambda self = None: self.sql_function.clauses.clauses[self.left_index - 1])()
    left_expr = (lambda self = None, value = None: self.sql_function.clauses.clauses[self.left_index - 1] = value)()
    right_expr = (lambda self = None: self.sql_function.clauses.clauses[self.right_index - 1])()
    right_expr = (lambda self = None, value = None: self.sql_function.clauses.clauses[self.right_index - 1] = value)()
    if not TYPE_CHECKING:
        left = left_expr
        right = right_expr
        return None

FunctionAsBinary = <NODE:27>(FunctionAsBinary, 'FunctionAsBinary', BinaryExpression[Any])

def ScalarFunctionColumn():
    '''ScalarFunctionColumn'''
    __visit_name__ = 'scalar_function_column'
    _traverse_internals = [
        ('name', InternalTraversal.dp_anon_name),
        ('type', InternalTraversal.dp_type),
        ('fn', InternalTraversal.dp_clauseelement)]
    is_literal = False
    table = None
    
    def __init__(self = None, fn = None, name = None, type_ = (None,)):
        self.fn = fn
        self.name = name
        self.type = type_api.to_instance(type_)


ScalarFunctionColumn = <NODE:27>(ScalarFunctionColumn, 'ScalarFunctionColumn', NamedColumn[_T])

class _FunctionGenerator:
    '''Generate SQL function expressions.

    :data:`.func` is a special object instance which generates SQL
    functions based on name-based attributes, e.g.:

    .. sourcecode:: pycon+sql

        >>> print(func.count(1))
        {printsql}count(:param_1)

    The returned object is an instance of :class:`.Function`, and  is a
    column-oriented SQL element like any other, and is used in that way:

    .. sourcecode:: pycon+sql

        >>> print(select(func.count(table.c.id)))
        {printsql}SELECT count(sometable.id) FROM sometable

    Any name can be given to :data:`.func`. If the function name is unknown to
    SQLAlchemy, it will be rendered exactly as is. For common SQL functions
    which SQLAlchemy is aware of, the name may be interpreted as a *generic
    function* which will be compiled appropriately to the target database:

    .. sourcecode:: pycon+sql

        >>> print(func.current_timestamp())
        {printsql}CURRENT_TIMESTAMP

    To call functions which are present in dot-separated packages,
    specify them in the same manner:

    .. sourcecode:: pycon+sql

        >>> print(func.stats.yield_curve(5, 10))
        {printsql}stats.yield_curve(:yield_curve_1, :yield_curve_2)

    SQLAlchemy can be made aware of the return type of functions to enable
    type-specific lexical and result-based behavior. For example, to ensure
    that a string-based function returns a Unicode value and is similarly
    treated as a string in expressions, specify
    :class:`~sqlalchemy.types.Unicode` as the type:

    .. sourcecode:: pycon+sql

        >>> print(
        ...     func.my_string("hi", type_=Unicode)
        ...     + " "
        ...     + func.my_string("there", type_=Unicode)
        ... )
        {printsql}my_string(:my_string_1) || :my_string_2 || my_string(:my_string_3)

    The object returned by a :data:`.func` call is usually an instance of
    :class:`.Function`.
    This object meets the "column" interface, including comparison and labeling
    functions.  The object can also be passed the :meth:`~.Connectable.execute`
    method of a :class:`_engine.Connection` or :class:`_engine.Engine`,
    where it will be
    wrapped inside of a SELECT statement first::

        print(connection.execute(func.current_timestamp()).scalar())

    In a few exception cases, the :data:`.func` accessor
    will redirect a name to a built-in expression such as :func:`.cast`
    or :func:`.extract`, as these names have well-known meaning
    but are not exactly the same as "functions" from a SQLAlchemy
    perspective.

    Functions which are interpreted as "generic" functions know how to
    calculate their return type automatically. For a listing of known generic
    functions, see :ref:`generic_functions`.

    .. note::

        The :data:`.func` construct has only limited support for calling
        standalone "stored procedures", especially those with special
        parameterization concerns.

        See the section :ref:`stored_procedures` for details on how to use
        the DBAPI-level ``callproc()`` method for fully traditional stored
        procedures.

    .. seealso::

        :ref:`tutorial_functions` - in the :ref:`unified_tutorial`

        :class:`.Function`

    '''
    
    def __init__(self = None, **opts):
        self._FunctionGenerator__names = []
        self.opts = opts

    
    def __getattr__(self = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    __call__ = (lambda self = None, *, type_: pass)()
    __call__ = (lambda self = None: pass)()
    
    def __call__(self = None, *c, **kwargs):
        o = self.opts.copy()
        o.update(kwargs)
        tokens = len(self._FunctionGenerator__names)
        if tokens == 2:
            (package, fname) = self._FunctionGenerator__names
        elif tokens == 1:
            fname = self._FunctionGenerator__names[0]
            package = '_default'
        else:
            package = None
    # WARNING: Decompyle incomplete

    if TYPE_CHECKING:
        aggregate_strings = (lambda self = None: pass)()
        ansifunction = (lambda self = None: pass)()
        array_agg = (lambda self = None, col = None: pass)()
        array_agg = (lambda self = None, col = None: pass)()
        array_agg = (lambda self = None, col = None: pass)()
        
        def array_agg(self = None, col = None, *args, **kwargs):
            pass

        cast = (lambda self = None: pass)()
        char_length = (lambda self = None: pass)()
        coalesce = (lambda self = None, col = None: pass)()
        coalesce = (lambda self = None, col = None: pass)()
        coalesce = (lambda self = None, col = None: pass)()
        
        def coalesce(self = None, col = None, *args, **kwargs):
            pass

        concat = (lambda self = None: pass)()
        count = (lambda self = None: pass)()
        cube = (lambda self = None: pass)()
        cume_dist = (lambda self = None: pass)()
        current_date = (lambda self = None: pass)()
        current_time = (lambda self = None: pass)()
        current_timestamp = (lambda self = None: pass)()
        current_user = (lambda self = None: pass)()
        dense_rank = (lambda self = None: pass)()
        extract = (lambda self = None: pass)()
        grouping_sets = (lambda self = None: pass)()
        localtime = (lambda self = None: pass)()
        localtimestamp = (lambda self = None: pass)()
        max = (lambda self = None, col = None: pass)()
        max = (lambda self = None, col = None: pass)()
        max = (lambda self = None, col = None: pass)()
        
        def max(self = None, col = None, *args, **kwargs):
            pass

        min = (lambda self = None, col = None: pass)()
        min = (lambda self = None, col = None: pass)()
        min = (lambda self = None, col = None: pass)()
        
        def min(self = None, col = None, *args, **kwargs):
            pass

        mode = (lambda self = None: pass)()
        next_value = (lambda self = None: pass)()
        now = (lambda self = None: pass)()
        orderedsetagg = (lambda self = None: pass)()
        percent_rank = (lambda self = None: pass)()
        percentile_cont = (lambda self = None: pass)()
        percentile_disc = (lambda self = None: pass)()
        random = (lambda self = None: pass)()
        rank = (lambda self = None: pass)()
        rollup = (lambda self = None: pass)()
        session_user = (lambda self = None: pass)()
        sum = (lambda self = None, col = None: pass)()
        sum = (lambda self = None, col = None: pass)()
        sum = (lambda self = None, col = None: pass)()
        
        def sum(self = None, col = None, *args, **kwargs):
            pass

        sysdate = (lambda self = None: pass)()
        user = (lambda self = None: pass)()
        return None

func = _FunctionGenerator()
func.__doc__ = _FunctionGenerator.__doc__
modifier = _FunctionGenerator(group = False)

def Function():
    '''Function'''
    __doc__ = 'Describe a named SQL function.\n\n    The :class:`.Function` object is typically generated from the\n    :data:`.func` generation object.\n\n\n    :param \\*clauses: list of column expressions that form the arguments\n     of the SQL function call.\n\n    :param type\\_: optional :class:`.TypeEngine` datatype object that will be\n     used as the return value of the column expression generated by this\n     function call.\n\n    :param packagenames: a string which indicates package prefix names\n     to be prepended to the function name when the SQL is generated.\n     The :data:`.func` generator creates these when it is called using\n     dotted format, e.g.::\n\n        func.mypackage.some_function(col1, col2)\n\n    .. seealso::\n\n        :ref:`tutorial_functions` - in the :ref:`unified_tutorial`\n\n        :data:`.func` - namespace which produces registered or ad-hoc\n        :class:`.Function` instances.\n\n        :class:`.GenericFunction` - allows creation of registered function\n        types.\n\n    '
    __visit_name__ = 'function'
    type: 'TypeEngine[_T]' = FunctionElement._traverse_internals + [
        ('packagenames', InternalTraversal.dp_plain_obj),
        ('name', InternalTraversal.dp_string),
        ('type', InternalTraversal.dp_type)]
    __init__ = (lambda self = None, name = None, *, type_, packagenames: pass)()
    __init__ = (lambda self = None, name = None, *, type_, packagenames: pass)()
    
    def __init__(self = None, name = None, *, type_, packagenames, *clauses):
        '''Construct a :class:`.Function`.

        The :data:`.func` construct is normally used to construct
        new :class:`.Function` instances.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _bind_param(self = None, operator = None, obj = None, type_ = (None, False), expanding = ('operator', 'OperatorType', 'obj', 'Any', 'type_', 'Optional[TypeEngine[_T]]', 'expanding', 'bool', 'kw', 'Any', 'return', 'BindParameter[_T]'), **kw):
        pass
    # WARNING: Decompyle incomplete


Function = <NODE:27>(Function, 'Function', FunctionElement[_T])

def GenericFunction():
    '''GenericFunction'''
    pass
# WARNING: Decompyle incomplete

GenericFunction = <NODE:27>(GenericFunction, 'GenericFunction', Function[_T])
register_function('cast', Cast)
register_function('extract', Extract)

def next_value():
    '''next_value'''
    __doc__ = "Represent the 'next value', given a :class:`.Sequence`\n    as its single argument.\n\n    Compiles into the appropriate function on each backend,\n    or will raise NotImplementedError if used on a backend\n    that does not provide support for sequences.\n\n    "
    type = sqltypes.Integer()
    name = 'next_value'
    _traverse_internals = [
        ('sequence', InternalTraversal.dp_named_ddl_element)]
    
    def __init__(self = None, seq = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare(self = None, other = None, **kw):
        if isinstance(other, next_value):
            pass
        return self.sequence.name == other.sequence.name

    _from_objects = (lambda self = None: [])()

next_value = <NODE:27>(next_value, 'next_value', GenericFunction[int])

def AnsiFunction():
    '''AnsiFunction'''
    __doc__ = 'Define a function in "ansi" format, which doesn\'t render parenthesis.'
    inherit_cache = True
    
    def __init__(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete


AnsiFunction = <NODE:27>(AnsiFunction, 'AnsiFunction', GenericFunction[_T])

def ReturnTypeFromArgs():
    '''ReturnTypeFromArgs'''
    pass
# WARNING: Decompyle incomplete

ReturnTypeFromArgs = <NODE:27>(ReturnTypeFromArgs, 'ReturnTypeFromArgs', GenericFunction[_T])

def coalesce():
    '''coalesce'''
    _has_args = True
    inherit_cache = True

coalesce = <NODE:27>(coalesce, 'coalesce', ReturnTypeFromArgs[_T])

def max():
    '''max'''
    __doc__ = 'The SQL MAX() aggregate function.'
    inherit_cache = True

max = <NODE:27>(max, 'max', ReturnTypeFromArgs[_T])

def min():
    '''min'''
    __doc__ = 'The SQL MIN() aggregate function.'
    inherit_cache = True

min = <NODE:27>(min, 'min', ReturnTypeFromArgs[_T])

def sum():
    '''sum'''
    __doc__ = 'The SQL SUM() aggregate function.'
    inherit_cache = True

sum = <NODE:27>(sum, 'sum', ReturnTypeFromArgs[_T])

def now():
    '''now'''
    __doc__ = 'The SQL now() datetime function.\n\n    SQLAlchemy dialects will usually render this particular function\n    in a backend-specific way, such as rendering it as ``CURRENT_TIMESTAMP``.\n\n    '
    type = sqltypes.DateTime()
    inherit_cache = True

now = <NODE:27>(now, 'now', GenericFunction[datetime.datetime])

def concat():
    '''concat'''
    __doc__ = 'The SQL CONCAT() function, which concatenates strings.\n\n    E.g.:\n\n    .. sourcecode:: pycon+sql\n\n        >>> print(select(func.concat("a", "b")))\n        {printsql}SELECT concat(:concat_2, :concat_3) AS concat_1\n\n    String concatenation in SQLAlchemy is more commonly available using the\n    Python ``+`` operator with string datatypes, which will render a\n    backend-specific concatenation operator, such as :\n\n    .. sourcecode:: pycon+sql\n\n        >>> print(select(literal("a") + "b"))\n        {printsql}SELECT :param_1 || :param_2 AS anon_1\n\n\n    '
    type = sqltypes.String()
    inherit_cache = True

concat = <NODE:27>(concat, 'concat', GenericFunction[str])

def char_length():
    '''char_length'''
    pass
# WARNING: Decompyle incomplete

char_length = <NODE:27>(char_length, 'char_length', GenericFunction[int])

def random():
    '''random'''
    __doc__ = 'The RANDOM() SQL function.'
    _has_args = True
    inherit_cache = True

random = <NODE:27>(random, 'random', GenericFunction[float])

def count():
    '''count'''
    pass
# WARNING: Decompyle incomplete

count = <NODE:27>(count, 'count', GenericFunction[int])

def current_date():
    '''current_date'''
    __doc__ = 'The CURRENT_DATE() SQL function.'
    type = sqltypes.Date()
    inherit_cache = True

current_date = <NODE:27>(current_date, 'current_date', AnsiFunction[datetime.date])

def current_time():
    '''current_time'''
    __doc__ = 'The CURRENT_TIME() SQL function.'
    type = sqltypes.Time()
    inherit_cache = True

current_time = <NODE:27>(current_time, 'current_time', AnsiFunction[datetime.time])

def current_timestamp():
    '''current_timestamp'''
    __doc__ = 'The CURRENT_TIMESTAMP() SQL function.'
    type = sqltypes.DateTime()
    inherit_cache = True

current_timestamp = <NODE:27>(current_timestamp, 'current_timestamp', AnsiFunction[datetime.datetime])

def current_user():
    '''current_user'''
    __doc__ = 'The CURRENT_USER() SQL function.'
    type = sqltypes.String()
    inherit_cache = True

current_user = <NODE:27>(current_user, 'current_user', AnsiFunction[str])

def localtime():
    '''localtime'''
    __doc__ = 'The localtime() SQL function.'
    type = sqltypes.DateTime()
    inherit_cache = True

localtime = <NODE:27>(localtime, 'localtime', AnsiFunction[datetime.datetime])

def localtimestamp():
    '''localtimestamp'''
    __doc__ = 'The localtimestamp() SQL function.'
    type = sqltypes.DateTime()
    inherit_cache = True

localtimestamp = <NODE:27>(localtimestamp, 'localtimestamp', AnsiFunction[datetime.datetime])

def session_user():
    '''session_user'''
    __doc__ = 'The SESSION_USER() SQL function.'
    type = sqltypes.String()
    inherit_cache = True

session_user = <NODE:27>(session_user, 'session_user', AnsiFunction[str])

def sysdate():
    '''sysdate'''
    __doc__ = 'The SYSDATE() SQL function.'
    type = sqltypes.DateTime()
    inherit_cache = True

sysdate = <NODE:27>(sysdate, 'sysdate', AnsiFunction[datetime.datetime])

def user():
    '''user'''
    __doc__ = 'The USER() SQL function.'
    type = sqltypes.String()
    inherit_cache = True

user = <NODE:27>(user, 'user', AnsiFunction[str])

def array_agg():
    '''array_agg'''
    pass
# WARNING: Decompyle incomplete

array_agg = <NODE:27>(array_agg, 'array_agg', ReturnTypeFromArgs[Sequence[_T]])

def OrderedSetAgg():
    '''OrderedSetAgg'''
    __doc__ = 'Define a function where the return type is based on the sort\n    expression type as defined by the expression passed to the\n    :meth:`.FunctionElement.within_group` method.'
    array_for_multi_clause = False
    inherit_cache = True
    
    def within_group_type(self = None, within_group = None):
        func_clauses = cast(ClauseList, self.clause_expr.element)
        order_by = sqlutil.unwrap_order_by(within_group.order_by)
        if self.array_for_multi_clause and len(func_clauses.clauses) > 1:
            return sqltypes.ARRAY(order_by[0].type)
        return None[0].type


OrderedSetAgg = <NODE:27>(OrderedSetAgg, 'OrderedSetAgg', GenericFunction[_T])

def mode():
    '''mode'''
    __doc__ = 'Implement the ``mode`` ordered-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is the same as the sort expression.\n\n    '
    inherit_cache = True

mode = <NODE:27>(mode, 'mode', OrderedSetAgg[_T])

def percentile_cont():
    '''percentile_cont'''
    __doc__ = "Implement the ``percentile_cont`` ordered-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is the same as the sort expression,\n    or if the arguments are an array, an :class:`_types.ARRAY` of the sort\n    expression's type.\n\n    "
    array_for_multi_clause = True
    inherit_cache = True

percentile_cont = <NODE:27>(percentile_cont, 'percentile_cont', OrderedSetAgg[_T])

def percentile_disc():
    '''percentile_disc'''
    __doc__ = "Implement the ``percentile_disc`` ordered-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is the same as the sort expression,\n    or if the arguments are an array, an :class:`_types.ARRAY` of the sort\n    expression's type.\n\n    "
    array_for_multi_clause = True
    inherit_cache = True

percentile_disc = <NODE:27>(percentile_disc, 'percentile_disc', OrderedSetAgg[_T])

def rank():
    '''rank'''
    __doc__ = 'Implement the ``rank`` hypothetical-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is :class:`.Integer`.\n\n    '
    type = sqltypes.Integer()
    inherit_cache = True

rank = <NODE:27>(rank, 'rank', GenericFunction[int])

def dense_rank():
    '''dense_rank'''
    __doc__ = 'Implement the ``dense_rank`` hypothetical-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is :class:`.Integer`.\n\n    '
    type = sqltypes.Integer()
    inherit_cache = True

dense_rank = <NODE:27>(dense_rank, 'dense_rank', GenericFunction[int])

def percent_rank():
    '''percent_rank'''
    __doc__ = 'Implement the ``percent_rank`` hypothetical-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is :class:`.Numeric`.\n\n    '
    type: 'sqltypes.Numeric[decimal.Decimal]' = sqltypes.Numeric()
    inherit_cache = True

percent_rank = <NODE:27>(percent_rank, 'percent_rank', GenericFunction[decimal.Decimal])

def cume_dist():
    '''cume_dist'''
    __doc__ = 'Implement the ``cume_dist`` hypothetical-set aggregate function.\n\n    This function must be used with the :meth:`.FunctionElement.within_group`\n    modifier to supply a sort expression to operate upon.\n\n    The return type of this function is :class:`.Numeric`.\n\n    '
    type: 'sqltypes.Numeric[decimal.Decimal]' = sqltypes.Numeric()
    inherit_cache = True

cume_dist = <NODE:27>(cume_dist, 'cume_dist', GenericFunction[decimal.Decimal])

def cube():
    '''cube'''
    __doc__ = 'Implement the ``CUBE`` grouping operation.\n\n    This function is used as part of the GROUP BY of a statement,\n    e.g. :meth:`_expression.Select.group_by`::\n\n        stmt = select(\n            func.sum(table.c.value), table.c.col_1, table.c.col_2\n        ).group_by(func.cube(table.c.col_1, table.c.col_2))\n\n    .. versionadded:: 1.2\n\n    '
    _has_args = True
    inherit_cache = True

cube = <NODE:27>(cube, 'cube', GenericFunction[_T])

def rollup():
    '''rollup'''
    __doc__ = 'Implement the ``ROLLUP`` grouping operation.\n\n    This function is used as part of the GROUP BY of a statement,\n    e.g. :meth:`_expression.Select.group_by`::\n\n        stmt = select(\n            func.sum(table.c.value), table.c.col_1, table.c.col_2\n        ).group_by(func.rollup(table.c.col_1, table.c.col_2))\n\n    .. versionadded:: 1.2\n\n    '
    _has_args = True
    inherit_cache = True

rollup = <NODE:27>(rollup, 'rollup', GenericFunction[_T])

def grouping_sets():
    '''grouping_sets'''
    __doc__ = 'Implement the ``GROUPING SETS`` grouping operation.\n\n    This function is used as part of the GROUP BY of a statement,\n    e.g. :meth:`_expression.Select.group_by`::\n\n        stmt = select(\n            func.sum(table.c.value), table.c.col_1, table.c.col_2\n        ).group_by(func.grouping_sets(table.c.col_1, table.c.col_2))\n\n    In order to group by multiple sets, use the :func:`.tuple_` construct::\n\n        from sqlalchemy import tuple_\n\n        stmt = select(\n            func.sum(table.c.value), table.c.col_1, table.c.col_2, table.c.col_3\n        ).group_by(\n            func.grouping_sets(\n                tuple_(table.c.col_1, table.c.col_2),\n                tuple_(table.c.value, table.c.col_3),\n            )\n        )\n\n    .. versionadded:: 1.2\n\n    '
    _has_args = True
    inherit_cache = True

grouping_sets = <NODE:27>(grouping_sets, 'grouping_sets', GenericFunction[_T])

def aggregate_strings():
    '''aggregate_strings'''
    pass
# WARNING: Decompyle incomplete

aggregate_strings = <NODE:27>(aggregate_strings, 'aggregate_strings', GenericFunction[str])
