# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from sympy.core.containers import Tuple
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import AppliedUndef
from sympy.core.relational import Relational
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify
from sympy.logic.boolalg import BooleanFunction
from sympy.sets.fancysets import ImageSet
from sympy.sets.sets import FiniteSet
from sympy.tensor.indexed import Indexed

def _get_free_symbols(exprs):
    '''Returns the free symbols of a symbolic expression.

    If the expression contains any of these elements, assume that they are
    the "free symbols" of the expression:

    * indexed objects
    * applied undefined function (useful for sympy.physics.mechanics module)
    '''
    if not isinstance(exprs, (list, tuple, set)):
        exprs = [
            exprs]
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(exprs()):
        return set()
# WARNING: Decompyle incomplete


def extract_solution(set_sol, n = (10,)):
    '''Extract numerical solutions from a set solution (computed by solveset,
    linsolve, nonlinsolve). Often, it is not trivial do get something useful
    out of them.

    Parameters
    ==========

    n : int, optional
        In order to replace ImageSet with FiniteSet, an iterator is created
        for each ImageSet contained in `set_sol`, starting from 0 up to `n`.
        Default value: 10.
    '''
    pass
# WARNING: Decompyle incomplete


def _plot_sympify(args):
    """This function recursively loop over the arguments passed to the plot
    functions: the sympify function will be applied to all arguments except
    those of type string/dict.

    Generally, users can provide the following arguments to a plot function:

    expr, range1 [tuple, opt], ..., label [str, opt], rendering_kw [dict, opt]

    `expr, range1, ...` can be sympified, whereas `label, rendering_kw` can't.
    In particular, whenever a special character like $, {, }, ... is used in
    the `label`, sympify will raise an error.
    """
    if isinstance(args, Expr):
        return args
    args = None(args)
# WARNING: Decompyle incomplete


def _create_ranges(exprs, ranges, npar, label, params = ('', None)):
    '''This function does two things:

    1. Check if the number of free symbols is in agreement with the type of
       plot chosen. For example, plot() requires 1 free symbol;
       plot3d() requires 2 free symbols.
    2. Sometime users create plots without providing ranges for the variables.
       Here we create the necessary ranges.

    Parameters
    ==========

    exprs : iterable
        The expressions from which to extract the free symbols
    ranges : iterable
        The limiting ranges provided by the user
    npar : int
        The number of free symbols required by the plot functions.
        For example,
        npar=1 for plot, npar=2 for plot3d, ...
    params : dict
        A dictionary mapping symbols to parameters for interactive plot.
    '''
    
    get_default_range = lambda symbol: Tuple(symbol, -10, 10)
    free_symbols = _get_free_symbols(exprs)
# WARNING: Decompyle incomplete


def _is_range(r):
