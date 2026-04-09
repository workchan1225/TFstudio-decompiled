# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: series.pyc (Python 3.11)

from collections.abc import Callable
from sympy.calculus.util import continuous_domain
from sympy.concrete import Sum, Product
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.function import arity
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Symbol
from sympy.functions import atan2, zeta, frac, ceiling, floor, im
from sympy.core.relational import Equality, GreaterThan, LessThan, Relational, Ne
from sympy.core.sympify import sympify
from sympy.external import import_module
from sympy.logic.boolalg import BooleanFunction
from sympy.plotting.utils import _get_free_symbols, extract_solution
from sympy.printing.latex import latex
from sympy.printing.pycode import PythonCodePrinter
from sympy.printing.precedence import precedence
from sympy.sets.sets import Set, Interval, Union
from sympy.simplify.simplify import nsimplify
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.lambdify import lambdify
from intervalmath import interval
import warnings

class IntervalMathPrinter(PythonCodePrinter):
    '''A printer to be used inside `plot_implicit` when `adaptive=True`,
    in which case the interval arithmetic module is going to be used, which
    requires the following edits.
    '''
    
    def _print_And(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def _print_Or(self, expr):
        pass
    # WARNING: Decompyle incomplete



def _uniform_eval(f1 = None, f2 = {
    'modules': None,
    'force_real_eval': False,
    'has_sum': False }, *, modules, force_real_eval, has_sum, *args):
    '''
    Note: this is an experimental function, as such it is prone to changes.
    Please, do not use it in your code.
    '''
    pass
# WARNING: Decompyle incomplete


def _adaptive_eval(f, x):
    '''Evaluate f(x) with an adaptive algorithm. Post-process the result.
    If a symbolic expression is evaluated with SymPy, it might returns
    another symbolic expression, containing additions, ...
    Force evaluation to a float.

    Parameters
    ==========
    f : callable
    x : float
    '''
    np = import_module('numpy')
    y = f(x)
    if not isinstance(y, Expr) and y.is_Number:
        y = y.evalf()
    y = complex(y)
    if y.imag > 1e-08:
        return np.nan
    return None.real


def _get_wrapper_for_expr(ret):
    wrapper = '%s'
    if ret == 'real':
        wrapper = 're(%s)'
    elif ret == 'imag':
        wrapper = 'im(%s)'
    elif ret == 'abs':
        wrapper = 'abs(%s)'
    elif ret == 'arg':
        wrapper = 'arg(%s)'
    return wrapper


class BaseSeries:
    '''Base class for the data objects containing stuff to be plotted.

    Notes
    =====

    The backend should check if it supports the data series that is given.
    (e.g. TextBackend supports only LineOver1DRangeSeries).
    It is the backend responsibility to know how to use the class of
    data series that is given.

    Some data series classes are grouped (using a class attribute like is_2Dline)
    according to the api they present (based only on convention). The backend is
    not obliged to use that api (e.g. LineOver1DRangeSeries belongs to the
    is_2Dline group and presents the get_points method, but the
    TextBackend does not use the get_points method).

    BaseSeries
    '''
    is_2Dline = False
    is_3Dline = False
    is_3Dsurface = False
    is_contour = False
    is_implicit = False
    is_interactive = False
    is_parametric = False
    is_generic = False
    is_vector = False
    is_2Dvector = False
    is_3Dvector = False
    _N = 100
    
    def __init__(self, *args, **kwargs):
        kwargs = _set_discretization_points(kwargs.copy(), type(self))
        self.only_integers = kwargs.get('only_integers', False)
        self.modules = kwargs.get('modules', None)
        self.show_in_legend = kwargs.get('show_in_legend', True)
        self.colorbar = kwargs.get('colorbar', True)
        self.use_cm = kwargs.get('use_cm', False)
        self.is_polar = kwargs.get('is_polar', kwargs.get('polar', False))
        self.is_point = kwargs.get('is_point', kwargs.get('point', False))
        self._label = ''
        self._latex_label = ''
        self._ranges = []
        self._n = [
            int(kwargs.get('n1', self._N)),
            int(kwargs.get('n2', self._N)),
            int(kwargs.get('n3', self._N))]
        self._scales = [
            kwargs.get('xscale', 'linear'),
            kwargs.get('yscale', 'linear'),
            kwargs.get('zscale', 'linear')]
        self._params = kwargs.get('params', { })
        if not isinstance(self._params, dict):
            raise TypeError('`params` must be a dictionary mapping symbols to numeric values.')
        if len(self._params) > 0:
            self.is_interactive = True
        self.rendering_kw = kwargs.get('rendering_kw', { })
        self._tx = kwargs.get('tx', None)
        self._ty = kwargs.get('ty', None)
        self._tz = kwargs.get('tz', None)
        self._tp = kwargs.get('tp', None)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)((self._tx, self._ty, self._tz, self._tp)()):
            raise TypeError('`tx`, `ty`, `tz`, `tp` must be functions.')
        self._functions = []
        self._signature = []
        self._force_real_eval = kwargs.get('force_real_eval', None)
        self._discretized_domain = None
        self._interactive_ranges = False
        self._needs_to_be_int = []
        self.color_func = None
        self._eval_color_func_with_signature = False

    
    def _block_lambda_functions(self, *exprs):
        '''Some data series can be used to plot numerical functions, others
        cannot. Execute this method inside the `__init__` to prevent the
        processing of numerical functions.
        '''
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(exprs()):
            raise TypeError(type(self).__name__ + ' requires a symbolic expression.')

    
    def _check_fs(self):
        ''' Checks if there are enogh parameters and free symbols.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _create_lambda_func(self):
        """Create the lambda functions to be used by the uniform meshing
        strategy.

        Notes
        =====
        The old sympy.plotting used experimental_lambdify. It created one
        lambda function each time an evaluation was requested. If that failed,
        it went on to create a different lambda function and evaluated it,
        and so on.

        This new module changes strategy: it creates right away the default
        lambda function as well as the backup one. The reason is that the
        series could be interactive, hence the numerical function will be
        evaluated multiple times. So, let's create the functions just once.

        This approach works fine for the majority of cases, in which the
        symbolic expression is relatively short, hence the lambdification
        is fast. If the expression is very long, this approach takes twice
        the time to create the lambda functions. Be aware of that!
        """
        exprs = self.expr if hasattr(self.expr, '__iter__') else [
            self.expr]
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(exprs()):
            fs = _get_free_symbols(exprs)
            self._signature = sorted(fs, key = (lambda t: t.name))
            self._functions = []
            for e in exprs:
                self._functions.append([
                    lambdify(self._signature, e, modules = self.modules),
                    lambdify(self._signature, e, modules = 'sympy', dummify = True)])
        self._signature = (lambda .0: [ r[0] for r in .0 ])(self.ranges(), key = (lambda t: t.name))
        self._functions = exprs()
        if isinstance(self.color_func, Expr):
            self.color_func = lambdify(self._signature, self.color_func)
            self._eval_color_func_with_signature = True
            return None
        return (lambda .0: [ (e, None) for e in .0 ])

    
    def _update_range_value(self, t):
        '''If the value of a plotting range is a symbolic expression,
        substitute the parameters in order to get a numerical value.
        '''
        if not self._interactive_ranges:
            return complex(t)
        return None(t.subs(self.params))

    
    def _create_discretized_domain(self):
