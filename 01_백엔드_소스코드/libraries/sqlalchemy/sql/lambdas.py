# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lambdas.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as collections_abc
import inspect
import itertools
import operator
import threading
import types
from types import CodeType
from typing import Any
from typing import Callable
from typing import cast
from typing import List
from typing import MutableMapping
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import cache_key as _cache_key
from  import coercions
from  import elements
from  import roles
from  import schema
from  import visitors
from base import _clone
from base import Executable
from base import Options
from cache_key import CacheConst
from operators import ColumnOperators
from  import exc
from  import inspection
from  import util
from util.typing import Literal
if TYPE_CHECKING:
    from elements import BindParameter
    from elements import ClauseElement
    from roles import SQLRole
    from visitors import _CloneCallableType
_LambdaCacheType = MutableMapping[(Tuple[(Any, ...)], Union[('NonAnalyzedFunction', 'AnalyzedFunction')])]
_BoundParameterGetter = Callable[(..., Any)]
_closure_per_cache_key: '_LambdaCacheType' = util.LRUCache(1000)
_LambdaType = Callable[([], Any)]
_AnyLambdaType = Callable[(..., Any)]
_StmtLambdaType = Callable[([], Any)]
_E = TypeVar('_E', bound = Executable)
_StmtLambdaElementType = Callable[([
    _E], Any)]

class LambdaOptions(Options):
    enable_tracking = True
    track_closure_variables = True
    track_on: 'Optional[object]' = None
    global_track_bound_values = True
    track_bound_values = True
    lambda_cache: 'Optional[_LambdaCacheType]' = None


def lambda_stmt(lmb, enable_tracking, track_closure_variables = None, track_on = None, global_track_bound_values = None, track_bound_values = (True, True, None, True, True, None), lambda_cache = ('lmb', '_StmtLambdaType', 'enable_tracking', 'bool', 'track_closure_variables', 'bool', 'track_on', 'Optional[object]', 'global_track_bound_values', 'bool', 'track_bound_values', 'bool', 'lambda_cache', 'Optional[_LambdaCacheType]', 'return', 'StatementLambdaElement')):
    '''Produce a SQL statement that is cached as a lambda.

    The Python code object within the lambda is scanned for both Python
    literals that will become bound parameters as well as closure variables
    that refer to Core or ORM constructs that may vary.   The lambda itself
    will be invoked only once per particular set of constructs detected.

    E.g.::

        from sqlalchemy import lambda_stmt

        stmt = lambda_stmt(lambda: table.select())
        stmt += lambda s: s.where(table.c.id == 5)

        result = connection.execute(stmt)

    The object returned is an instance of :class:`_sql.StatementLambdaElement`.

    .. versionadded:: 1.4

    :param lmb: a Python function, typically a lambda, which takes no arguments
     and returns a SQL expression construct
    :param enable_tracking: when False, all scanning of the given lambda for
     changes in closure variables or bound parameters is disabled.  Use for
     a lambda that produces the identical results in all cases with no
     parameterization.
    :param track_closure_variables: when False, changes in closure variables
     within the lambda will not be scanned.   Use for a lambda where the
     state of its closure variables will never change the SQL structure
     returned by the lambda.
    :param track_bound_values: when False, bound parameter tracking will
     be disabled for the given lambda.  Use for a lambda that either does
     not produce any bound values, or where the initial bound values never
     change.
    :param global_track_bound_values: when False, bound parameter tracking
     will be disabled for the entire statement including additional links
     added via the :meth:`_sql.StatementLambdaElement.add_criteria` method.
    :param lambda_cache: a dictionary or other mapping-like object where
     information about the lambda\'s Python code as well as the tracked closure
     variables in the lambda itself will be stored.   Defaults
     to a global LRU cache.  This cache is independent of the "compiled_cache"
     used by the :class:`_engine.Connection` object.

    .. seealso::

        :ref:`engine_lambda_caching`


    '''
    return StatementLambdaElement(lmb, roles.StatementRole, LambdaOptions(enable_tracking = enable_tracking, track_on = track_on, track_closure_variables = track_closure_variables, global_track_bound_values = global_track_bound_values, track_bound_values = track_bound_values, lambda_cache = lambda_cache))


class LambdaElement(elements.ClauseElement):
    '''A SQL construct where the state is stored as an un-invoked lambda.

    The :class:`_sql.LambdaElement` is produced transparently whenever
    passing lambda expressions into SQL constructs, such as::

        stmt = select(table).where(lambda: table.c.col == parameter)

    The :class:`_sql.LambdaElement` is the base of the
    :class:`_sql.StatementLambdaElement` which represents a full statement
    within a lambda.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`engine_lambda_caching`

    '''
    __visit_name__ = 'lambda_element'
    _is_lambda_element = True
    _traverse_internals = [
        ('_resolved', visitors.InternalTraversal.dp_clauseelement)]
    _resolved_bindparams: 'List[BindParameter[Any]]' = ()
    tracker_key: 'Tuple[CodeType, ...]' = None
    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self.fn.__code__!r})'''

    
    def __init__(self = None, fn = None, role = None, opts = (LambdaOptions, None), apply_propagate_attrs = ('fn', '_LambdaType', 'role', 'Type[SQLRole]', 'opts', 'Union[Type[LambdaOptions], LambdaOptions]', 'apply_propagate_attrs', 'Optional[ClauseElement]')):
        self.fn = fn
        self.role = role
        self.tracker_key = (fn.__code__,)
        self.opts = opts
    # WARNING: Decompyle incomplete

    
    def _retrieve_tracker_rec(self, fn, apply_propagate_attrs, opts):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self, key):
        return getattr(self._rec.expected_expr, key)

    _is_sequence = (lambda self: self._rec.is_sequence)()
    _select_iterable = (lambda self: if self._is_sequence:
(lambda .0: [ element._select_iterable for element in .0 ])(self._resolved())
        return None._resolved._select_iterable
)()
    _from_objects = (lambda self: if self._is_sequence:
(lambda .0: [ element._from_objects for element in .0 ])(self._resolved())
        return None._resolved._from_objects
)()
    
    def _param_dict(self):
        return self._resolved_bindparams()

    
    def _setup_binds_for_tracked_expr(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _copy_internals(self = property, clone = property, deferred_copy_internals = property, **kw):
        pass
    # WARNING: Decompyle incomplete

    _resolved = (lambda self: expr = self._rec.expected_exprif self._resolved_bindparams:
expr = self._setup_binds_for_tracked_expr(expr)expr)()
    
    def _gen_cache_key(self, anon_map, bindparams):
        if self.closure_cache_key is _cache_key.NO_CACHE:
            anon_map[_cache_key.NO_CACHE] = True
            return None
        cache_key = (None.fn.__code__, self.__class__) + self.closure_cache_key
        parent = self.parent_lambda
    # WARNING: Decompyle incomplete

    
    def _invoke_user_fn(self = None, fn = None, *arg):
        return fn()



class DeferredLambdaElement(LambdaElement):
    pass
# WARNING: Decompyle incomplete


class StatementLambdaElement(Executable, LambdaElement, roles.AllowsLambdaRole):
    '''Represent a composable SQL statement as a :class:`_sql.LambdaElement`.

    The :class:`_sql.StatementLambdaElement` is constructed using the
    :func:`_sql.lambda_stmt` function::


        from sqlalchemy import lambda_stmt

        stmt = lambda_stmt(lambda: select(table))

    Once constructed, additional criteria can be built onto the statement
    by adding subsequent lambdas, which accept the existing statement
    object as a single parameter::

        stmt += lambda s: s.where(table.c.col == parameter)

    .. versionadded:: 1.4

    .. seealso::

        :ref:`engine_lambda_caching`

    '''
    if TYPE_CHECKING:
        
        def __init__(self = None, fn = None, role = None, opts = (LambdaOptions, None), apply_propagate_attrs = ('fn', '_StmtLambdaType', 'role', 'Type[SQLRole]', 'opts', 'Union[Type[LambdaOptions], LambdaOptions]', 'apply_propagate_attrs', 'Optional[ClauseElement]')):
            pass

    
    def __add__(self = None, other = None):
        return self.add_criteria(other)

    
    def add_criteria(self, other = None, enable_tracking = None, track_on = None, track_closure_variables = (True, None, True, True), track_bound_values = ('other', '_StmtLambdaElementType[Any]', 'enable_tracking', 'bool', 'track_on', 'Optional[Any]', 'track_closure_variables', 'bool', 'track_bound_values', 'bool', 'return', 'StatementLambdaElement')):
        '''Add new criteria to this :class:`_sql.StatementLambdaElement`.

        E.g.::

            >>> def my_stmt(parameter):
            ...     stmt = lambda_stmt(
            ...         lambda: select(table.c.x, table.c.y),
            ...     )
            ...     stmt = stmt.add_criteria(lambda: table.c.x > parameter)
            ...     return stmt

        The :meth:`_sql.StatementLambdaElement.add_criteria` method is
        equivalent to using the Python addition operator to add a new
        lambda, except that additional arguments may be added including
        ``track_closure_values`` and ``track_on``::

            >>> def my_stmt(self, foo):
            ...     stmt = lambda_stmt(
            ...         lambda: select(func.max(foo.x, foo.y)),
            ...         track_closure_variables=False,
            ...     )
            ...     stmt = stmt.add_criteria(lambda: self.where_criteria, track_on=[self])
            ...     return stmt

        See :func:`_sql.lambda_stmt` for a description of the parameters
        accepted.

        '''
        opts = self.opts + dict(enable_tracking = enable_tracking, track_closure_variables = track_closure_variables, global_track_bound_values = self.opts.global_track_bound_values, track_on = track_on, track_bound_values = track_bound_values)
        return LinkedLambdaElement(other, parent_lambda = self, opts = opts)

    
    def _execute_on_connection(self, connection, distilled_params, execution_options):
        pass
    # WARNING: Decompyle incomplete

    _proxied = (lambda self = None: self._rec_expected_expr)()
    _with_options = (lambda self: self._proxied._with_options)()
    _effective_plugin_target = (lambda self: self._proxied._effective_plugin_target)()
    _execution_options = (lambda self: self._proxied._execution_options)()
    _all_selected_columns = (lambda self: self._proxied._all_selected_columns)()
    is_select = (lambda self: self._proxied.is_select)()
    is_update = (lambda self: self._proxied.is_update)()
    is_insert = (lambda self: self._proxied.is_insert)()
    is_text = (lambda self: self._proxied.is_text)()
    is_delete = (lambda self: self._proxied.is_delete)()
    is_dml = (lambda self: self._proxied.is_dml)()
    
    def spoil(self = property):
        '''Return a new :class:`.StatementLambdaElement` that will run
        all lambdas unconditionally each time.

        '''
        return NullLambdaStatement(self.fn())



class NullLambdaStatement(elements.ClauseElement, roles.AllowsLambdaRole):
    '''Provides the :class:`.StatementLambdaElement` API but does not
    cache or analyze lambdas.

    the lambdas are instead invoked immediately.

    The intended use is to isolate issues that may arise when using
    lambda statements.

    '''
    __visit_name__ = 'lambda_element'
    _is_lambda_element = True
    _traverse_internals = [
        ('_resolved', visitors.InternalTraversal.dp_clauseelement)]
    
    def __init__(self, statement):
        self._resolved = statement
        self._propagate_attrs = statement._propagate_attrs

    
    def __getattr__(self, key):
        return getattr(self._resolved, key)

    
    def __add__(self, other):
        statement = other(self._resolved)
        return NullLambdaStatement(statement)

    
    def add_criteria(self, other, **kw):
        statement = other(self._resolved)
        return NullLambdaStatement(statement)

    
    def _execute_on_connection(self, connection, distilled_params, execution_options):
        if self._resolved.supports_execution:
            return connection._execute_clauseelement(self, distilled_params, execution_options)
        raise None.ObjectNotExecutableError(self)



class LinkedLambdaElement(StatementLambdaElement):
    parent_lambda: 'StatementLambdaElement' = 'Represent subsequent links of a :class:`.StatementLambdaElement`.'
    
    def __init__(self = None, fn = None, parent_lambda = None, opts = ('fn', '_StmtLambdaElementType[Any]', 'parent_lambda', 'StatementLambdaElement', 'opts', 'Union[Type[LambdaOptions], LambdaOptions]')):
        self.opts = opts
        self.fn = fn
        self.parent_lambda = parent_lambda
        self.tracker_key = parent_lambda.tracker_key + (fn.__code__,)
        self._retrieve_tracker_rec(fn, self, opts)
        self._propagate_attrs = parent_lambda._propagate_attrs

    
    def _invoke_user_fn(self, fn, *arg):
        return fn(self.parent_lambda._resolved)



class AnalyzedCode:
    __slots__ = ('track_closure_variables', 'track_bound_values', 'bindparam_trackers', 'closure_trackers', 'build_py_wrappers')
    _fns: 'weakref.WeakKeyDictionary[CodeType, AnalyzedCode]' = weakref.WeakKeyDictionary()
    _generation_mutex = threading.RLock()
    get = (lambda cls, fn, lambda_element, lambda_kw: try:
cls._fns[fn.__code__]except KeyError:
passcls._generation_mutexif fn.__code__ in cls._fns:
None(None, None)# WARNING: Decompyle incomplete
)()
    
    def __init__(self, fn, lambda_element, opts):
        if inspect.ismethod(fn):
            raise exc.ArgumentError('Method %s may not be passed as a SQL expression' % fn)
        closure = fn.__closure__
        if opts.track_bound_values:
            self.track_bound_values = opts.global_track_bound_values
            enable_tracking = opts.enable_tracking
            track_on = opts.track_on
            track_closure_variables = opts.track_closure_variables
            if track_closure_variables:
                self.track_closure_variables = not track_on
                self.bindparam_trackers = []
                self.closure_trackers = []
                self.build_py_wrappers = []
                if enable_tracking:
                    if track_on:
                        self._init_track_on(track_on)
                    self._init_globals(fn)
                    if closure:
                        self._init_closure(fn)
        self._setup_additional_closure_trackers(fn, lambda_element, opts)

    
    def _init_track_on(self, track_on):
        pass
    # WARNING: Decompyle incomplete

    
    def _init_globals(self, fn):
        build_py_wrappers = self.build_py_wrappers
        bindparam_trackers = self.bindparam_trackers
        track_bound_values = self.track_bound_values
        for name in fn.__code__.co_names:
            if name not in fn.__globals__:
                continue
            _bound_value = self._roll_down_to_literal(fn.__globals__[name])
            if coercions._deep_is_literal(_bound_value):
                build_py_wrappers.append((name, None))
                if track_bound_values:
                    bindparam_trackers.append(self._bound_parameter_getter_func_globals(name))
            return None

    
    def _init_closure(self, fn):
        build_py_wrappers = self.build_py_wrappers
        closure = fn.__closure__
        track_bound_values = self.track_bound_values
        track_closure_variables = self.track_closure_variables
        bindparam_trackers = self.bindparam_trackers
        closure_trackers = self.closure_trackers
        for fv, cell in enumerate(zip(fn.__code__.co_freevars, closure)):
            _bound_value = self._roll_down_to_literal(cell.cell_contents)
            if coercions._deep_is_literal(_bound_value):
                build_py_wrappers.append((fv, closure_index))
                if track_bound_values:
                    bindparam_trackers.append(self._bound_parameter_getter_func_closure(fv, closure_index))
                continue
            if track_closure_variables:
                closure_trackers.append(self._cache_key_getter_closure_variable(fn, fv, closure_index, cell.cell_contents))
            return None

    
    def _setup_additional_closure_trackers(self, fn, lambda_element, opts):
        analyzed_function = AnalyzedFunction(self, lambda_element, None, fn)
        closure_trackers = self.closure_trackers
        for pywrapper in analyzed_function.closure_pywrappers:
            if not pywrapper._sa__has_param:
                closure_trackers.append(self._cache_key_getter_tracked_literal(fn, pywrapper))
            return None

    _roll_down_to_literal = (lambda cls, element: is_clause_element = hasattr(element, '__clause_element__')# WARNING: Decompyle incomplete
)()
    
    def _bound_parameter_getter_func_globals(self, name):
        '''Return a getter that will extend a list of bound parameters
        with new entries from the ``__globals__`` collection of a particular
        lambda.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _bound_parameter_getter_func_closure(self, name, closure_index):
        '''Return a getter that will extend a list of bound parameters
        with new entries from the ``__closure__`` collection of a particular
        lambda.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _cache_key_getter_track_on(self, idx, elem):
        '''Return a getter that will extend a cache key with new entries
        from the "track_on" parameter passed to a :class:`.LambdaElement`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _cache_key_getter_closure_variable(self, fn, variable_name, idx, cell_contents, use_clause_element, use_inspect = (False, False)):
        '''Return a getter that will extend a cache key with new entries
        from the ``__closure__`` collection of a particular lambda.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _raise_for_uncacheable_closure_variable(self, variable_name, fn, from_ = (None,)):
        raise exc.InvalidRequestError(f'''Closure variable named \'{variable_name!s}\' inside of lambda callable {fn.__code__!s} does not refer to a cacheable SQL element, and also does not appear to be serving as a SQL literal bound value based on the default SQL expression returned by the function.   This variable needs to remain outside the scope of a SQL-generating lambda so that a proper cache key may be generated from the lambda\'s state.  Evaluate this variable outside of the lambda, set track_on=[<elements>] to explicitly select closure elements to track, or set track_closure_variables=False to exclude closure variables from being part of the cache key.'''), from_

    
    def _cache_key_getter_tracked_literal(self, fn, pytracker):
        '''Return a getter that will extend a cache key with new entries
        from the ``__closure__`` collection of a particular lambda.

        this getter differs from _cache_key_getter_closure_variable
        in that these are detected after the function is run, and PyWrapper
        objects have recorded that a particular literal value is in fact
        not being interpreted as a bound parameter.

        '''
        elem = pytracker._sa__to_evaluate
        closure_index = pytracker._sa__closure_index
        variable_name = pytracker._sa__name
        return self._cache_key_getter_closure_variable(fn, variable_name, closure_index, elem)



class NonAnalyzedFunction:
    __slots__ = ('expr',)
    closure_bindparams: 'Optional[List[BindParameter[Any]]]' = None
    bindparam_trackers: 'Optional[List[_BoundParameterGetter]]' = None
    expr: 'ClauseElement' = False
    
    def __init__(self = None, expr = None):
        self.expr = expr

    expected_expr = (lambda self = None: self.expr)()


class AnalyzedFunction:
    bindparam_trackers: 'Optional[List[_BoundParameterGetter]]' = ('analyzed_code', 'fn', 'closure_pywrappers', 'tracker_instrumented_fn', 'expr', 'bindparam_trackers', 'expected_expr', 'is_sequence', 'propagate_attrs', 'closure_bindparams')
    
    def __init__(self, analyzed_code, lambda_element, apply_propagate_attrs, fn):
        self.analyzed_code = analyzed_code
        self.fn = fn
        self.bindparam_trackers = analyzed_code.bindparam_trackers
        self._instrument_and_run_function(lambda_element)
        self._coerce_expression(lambda_element, apply_propagate_attrs)

    
    def _instrument_and_run_function(self, lambda_element):
        pass
    # WARNING: Decompyle incomplete

    
    def _coerce_expression(self, lambda_element, apply_propagate_attrs):
        """Run the tracker-generated expression through coercion rules.

        After the user-defined lambda has been invoked to produce a statement
        for re-use, run it through coercion rules to both check that it's the
        correct type of object and also to coerce it to its useful form.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _rewrite_code_obj(self, f, cell_values, globals_):
        '''Return a copy of f, with a new closure and new globals

        yes it works in pypy :P

        '''
        pass
    # WARNING: Decompyle incomplete



class PyWrapper(ColumnOperators):
    '''A wrapper object that is injected into the ``__globals__`` and
    ``__closure__`` of a Python function.

    When the function is instrumented with :class:`.PyWrapper` objects, it is
    then invoked just once in order to set up the wrappers.  We look through
    all the :class:`.PyWrapper` objects we made to find the ones that generated
    a :class:`.BindParameter` object, e.g. the expression system interpreted
    something as a literal.   Those positions in the globals/closure are then
    ones that we will look at, each time a new lambda comes in that refers to
    the same ``__code__`` object.   In this way, we keep a single version of
    the SQL expression that this lambda produced, without calling upon the
    Python function that created it more than once, unless its other closure
    variables have changed.   The expression is then transformed to have the
    new bound values embedded into it.

    '''
    
    def __init__(self, fn, name, to_evaluate, closure_index, getter, track_bound_values = (None, None, True)):
        self.fn = fn
        self._name = name
        self._to_evaluate = to_evaluate
        self._param = None
        self._has_param = False
        self._bind_paths = { }
        self._getter = getter
        self._closure_index = closure_index
        self.track_bound_values = track_bound_values

    
    def __call__(self, *arg, **kw):
        elem = object.__getattribute__(self, '_to_evaluate')
    # WARNING: Decompyle incomplete

    
    def operate(self, op, *other, **kwargs):
        elem = object.__getattribute__(self, '_py_wrapper_literal')()
    # WARNING: Decompyle incomplete

    
    def reverse_operate(self, op, other, **kwargs):
        elem = object.__getattribute__(self, '_py_wrapper_literal')()
    # WARNING: Decompyle incomplete

    
    def _extract_bound_parameters(self, starting_point, result_list):
        param = object.__getattribute__(self, '_param')
    # WARNING: Decompyle incomplete

    
    def _py_wrapper_literal(self, expr, operator = (None, None), **kw):
        param = object.__getattribute__(self, '_param')
        to_evaluate = object.__getattribute__(self, '_to_evaluate')
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        to_evaluate = object.__getattribute__(self, '_to_evaluate')
        return bool(to_evaluate)

    
    def __getattribute__(self, key):
        if key.startswith('_sa_'):
            return object.__getattribute__(self, key[4:])
        if None in ('__clause_element__', 'operate', 'reverse_operate', '_py_wrapper_literal', '__class__', '__dict__'):
            return object.__getattribute__(self, key)
        if None.startswith('__'):
            elem = object.__getattribute__(self, '_to_evaluate')
            return getattr(elem, key)
        return None._sa__add_getter(key, operator.attrgetter)

    
    def __iter__(self):
        elem = object.__getattribute__(self, '_to_evaluate')
        return iter(elem)

    
    def __getitem__(self, key):
        elem = object.__getattribute__(self, '_to_evaluate')
        if not hasattr(elem, '__getitem__'):
            raise AttributeError('__getitem__')
        if isinstance(key, PyWrapper):
            raise exc.InvalidRequestError('Dictionary keys / list indexes inside of a cached lambda must be Python literals only')
        return self._sa__add_getter(key, operator.itemgetter)

    
    def _add_getter(self, key, getter_fn):
        bind_paths = object.__getattribute__(self, '_bind_paths')
        bind_path_key = (key, getter_fn)
        if bind_path_key in bind_paths:
            return bind_paths[bind_path_key]
        getter = getter_fn(key)
        elem = object.__getattribute__(self, '_to_evaluate')
        value = getter(elem)
        rolled_down_value = AnalyzedCode._roll_down_to_literal(value)
        if coercions._deep_is_literal(rolled_down_value):
            wrapper = PyWrapper(self._sa_fn, key, value, getter = getter)
            bind_paths[bind_path_key] = wrapper
            return wrapper


insp = (lambda lmb: inspection.inspect(lmb._resolved))()
