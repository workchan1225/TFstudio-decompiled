# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cse_main.pyc (Python 3.11)

''' Tools for doing common subexpression elimination.
'''
from collections import defaultdict
from sympy.core import Basic, Mul, Add, Pow, sympify
from sympy.core.containers import Tuple, OrderedSet
from sympy.core.exprtools import factor_terms
from sympy.core.singleton import S
from sympy.core.sorting import ordered
from sympy.core.symbol import symbols, Symbol
from sympy.matrices import MatrixBase, Matrix, ImmutableMatrix, SparseMatrix, ImmutableSparseMatrix
from sympy.matrices.expressions import MatrixExpr, MatrixSymbol, MatMul, MatAdd, MatPow, Inverse
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.polys.rootoftools import RootOf
from sympy.utilities.iterables import numbered_symbols, sift, topological_sort, iterable
from  import cse_opts
basic_optimizations = [
    (cse_opts.sub_pre, cse_opts.sub_post),
    (factor_terms, None)]

def reps_toposort(r):
    """Sort replacements ``r`` so (k1, v1) appears before (k2, v2)
    if k2 is in v1's free symbols. This orders items in the
    way that cse returns its results (hence, in order to use the
    replacements in a substitution option it would make sense
    to reverse the order).

    Examples
    ========

    >>> from sympy.simplify.cse_main import reps_toposort
    >>> from sympy.abc import x, y
    >>> from sympy import Eq
    >>> for l, r in reps_toposort([(x, y + 1), (y, 2)]):
    ...     print(Eq(l, r))
    ...
    Eq(y, 2)
    Eq(x, y + 1)

    """
    pass
# WARNING: Decompyle incomplete


def cse_separate(r, e):
    """Move expressions that are in the form (symbol, expr) out of the
    expressions and sort them into the replacements using the reps_toposort.

    Examples
    ========

    >>> from sympy.simplify.cse_main import cse_separate
    >>> from sympy.abc import x, y, z
    >>> from sympy import cos, exp, cse, Eq, symbols
    >>> x0, x1 = symbols('x:2')
    >>> eq = (x + 1 + exp((x + 1)/(y + 1)) + cos(y + 1))
    >>> cse([eq, Eq(x, z + 1), z - 2], postprocess=cse_separate) in [
    ... [[(x0, y + 1), (x, z + 1), (x1, x + 1)],
    ...  [x1 + exp(x1/x0) + cos(x0), z - 2]],
    ... [[(x1, y + 1), (x, z + 1), (x0, x + 1)],
    ...  [x0 + exp(x0/x1) + cos(x1), z - 2]]]
    ...
    True
    """
    d = sift(e, (lambda w: if w.is_Equality:
passw.lhs.is_Symbol))
    r = (lambda .0: [ w.args for w in .0 ]) + d[True]()
    e = d[False]
    return [
        reps_toposort(r),
        e]


def cse_release_variables(r, e):
    '''
    Return tuples giving ``(a, b)`` where ``a`` is a symbol and ``b`` is
    either an expression or None. The value of None is used when a
    symbol is no longer needed for subsequent expressions.

    Use of such output can reduce the memory footprint of lambdified
    expressions that contain large, repeated subexpressions.

    Examples
    ========

    >>> from sympy import cse
    >>> from sympy.simplify.cse_main import cse_release_variables
    >>> from sympy.abc import x, y
    >>> eqs = [(x + y - 1)**2, x, x + y, (x + y)/(2*x + 1) + (x + y - 1)**2, (2*x + 1)**(x + y)]
    >>> defs, rvs = cse_release_variables(*cse(eqs))
    >>> for i in defs:
    ...   print(i)
    ...
    (x0, x + y)
    (x1, (x0 - 1)**2)
    (x2, 2*x + 1)
    (_3, x0/x2 + x1)
    (_4, x2**x0)
    (x2, None)
    (_0, x1)
    (x1, None)
    (_2, x0)
    (x0, None)
    (_1, x)
    >>> print(rvs)
    (_0, _1, _2, _3, _4)
    '''
    pass
# WARNING: Decompyle incomplete


def preprocess_for_cse(expr, optimizations):
    ''' Preprocess an expression to optimize for common subexpression
    elimination.

    Parameters
    ==========

    expr : SymPy expression
        The target expression to optimize.
    optimizations : list of (callable, callable) pairs
        The (preprocessor, postprocessor) pairs.

    Returns
    =======

    expr : SymPy expression
        The transformed expression.
    '''
    pass
# WARNING: Decompyle incomplete


def postprocess_for_cse(expr, optimizations):
    '''Postprocess an expression after common subexpression elimination to
    return the expression to canonical SymPy form.

    Parameters
    ==========

    expr : SymPy expression
        The target expression to transform.
    optimizations : list of (callable, callable) pairs, optional
        The (preprocessor, postprocessor) pairs.  The postprocessors will be
        applied in reversed order to undo the effects of the preprocessors
        correctly.

    Returns
    =======

    expr : SymPy expression
        The transformed expression.
    '''
    pass
# WARNING: Decompyle incomplete


class FuncArgTracker:
    '''
    A class which manages a mapping from functions to arguments and an inverse
    mapping from arguments to functions.
    '''
    
    def __init__(self, funcs):
        self.value_numbers = { }
        self.value_number_to_value = []
        self.arg_to_funcset = []
        self.func_to_argset = []
        for func_i, func in enumerate(funcs):
            func_argset = OrderedSet()
            for func_arg in func.args:
                arg_number = self.get_or_add_value_number(func_arg)
                func_argset.add(arg_number)
                self.arg_to_funcset[arg_number].add(func_i)
                self.func_to_argset.append(func_argset)
                return None

    
    def get_args_in_value_order(self, argset):
        '''
        Return the list of arguments in sorted order according to their value
        numbers.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_or_add_value_number(self, value):
        '''
        Return the value number for the given argument.
        '''
        nvalues = len(self.value_numbers)
        value_number = self.value_numbers.setdefault(value, nvalues)
        if value_number == nvalues:
            self.value_number_to_value.append(value)
            self.arg_to_funcset.append(OrderedSet())
        return value_number

    
    def stop_arg_tracking(self, func_i):
        '''
        Remove the function func_i from the argument to function mapping.
        '''
        for arg in self.func_to_argset[func_i]:
            self.arg_to_funcset[arg].remove(func_i)
            return None

    
    def get_common_arg_candidates(self, argset, min_func_i = (0,)):
        '''Return a dict whose keys are function numbers. The entries of the dict are
        the number of arguments said function has in common with
        ``argset``. Entries have at least 2 items in common.  All keys have
        value at least ``min_func_i``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_subset_candidates(self, argset, restrict_to_funcset = (None,)):
        '''
        Return a set of functions each of which whose argument list contains
        ``argset``, optionally filtered only to contain functions in
        ``restrict_to_funcset``.
        '''
        iarg = iter(argset)
        indices = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.arg_to_funcset[next(iarg)]())
    # WARNING: Decompyle incomplete

    
    def update_func_argset(self, func_i, new_argset):
        '''
        Update a function with a new set of arguments.
        '''
        new_args = OrderedSet(new_argset)
        old_args = self.func_to_argset[func_i]
        for deleted_arg in old_args - new_args:
            self.arg_to_funcset[deleted_arg].remove(func_i)
            for added_arg in new_args - old_args:
                self.arg_to_funcset[added_arg].add(func_i)
                self.func_to_argset[func_i].clear()
                self.func_to_argset[func_i].update(new_args)
                return None



class Unevaluated:
    
    def __init__(self, func, args):
        self.func = func
        self.args = args

    
    def __str__(self):
        return self.func(', '.join, (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()))

    
    def as_unevaluated_basic(self):
        pass
    # WARNING: Decompyle incomplete

    free_symbols = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __repr__ = __str__


def match_common_args(func_class, funcs, opt_subs):
    '''
    Recognize and extract common subexpressions of function arguments within a
    set of function calls. For instance, for the following function calls::

        x + z + y
        sin(x + y)

    this will extract a common subexpression of `x + y`::

        w = x + y
        w + z
        sin(w)

    The function we work with is assumed to be associative and commutative.

    Parameters
    ==========

    func_class: class
        The function class (e.g. Add, Mul)
    funcs: list of functions
        A list of function calls.
    opt_subs: dict
        A dictionary of substitutions which this function may update.
    '''
    pass
# WARNING: Decompyle incomplete


def opt_cse(exprs, order = ('canonical',)):
    """Find optimization opportunities in Adds, Muls, Pows and negative
    coefficient Muls.

    Parameters
    ==========

    exprs : list of SymPy expressions
        The expressions to optimize.
    order : string, 'none' or 'canonical'
        The order by which Mul and Add arguments are processed. For large
        expressions where speed is a concern, use the setting order='none'.

    Returns
    =======

    opt_subs : dictionary of expression substitutions
        The expression substitutions which can be useful to optimize CSE.

    Examples
    ========

    >>> from sympy.simplify.cse_main import opt_cse
    >>> from sympy.abc import x
    >>> opt_subs = opt_cse([x**-2])
    >>> k, v = list(opt_subs.keys())[0], list(opt_subs.values())[0]
    >>> print((k, v.as_unevaluated_basic()))
    (x**(-2), 1/(x**2))
    """
    pass
# WARNING: Decompyle incomplete


def tree_cse(exprs, symbols, opt_subs, order, ignore = (None, 'canonical', ())):
    """Perform raw CSE on expression tree, taking opt_subs into account.

    Parameters
    ==========

    exprs : list of SymPy expressions
        The expressions to reduce.
    symbols : infinite iterator yielding unique Symbols
        The symbols used to label the common subexpressions which are pulled
        out.
    opt_subs : dictionary of expression substitutions
        The expressions to be substituted before any CSE action is performed.
    order : string, 'none' or 'canonical'
        The order by which Mul and Add arguments are processed. For large
        expressions where speed is a concern, use the setting order='none'.
    ignore : iterable of Symbols
        Substitutions containing any Symbol from ``ignore`` will be ignored.
    """
    pass
# WARNING: Decompyle incomplete


def cse(exprs, symbols, optimizations, postprocess, order, ignore, list = (None, None, None, 'canonical', (), True)):
    ''' Perform common subexpression elimination on an expression.

    Parameters
    ==========

    exprs : list of SymPy expressions, or a single SymPy expression
        The expressions to reduce.
    symbols : infinite iterator yielding unique Symbols
        The symbols used to label the common subexpressions which are pulled
        out. The ``numbered_symbols`` generator is useful. The default is a
        stream of symbols of the form "x0", "x1", etc. This must be an
        infinite iterator.
    optimizations : list of (callable, callable) pairs
        The (preprocessor, postprocessor) pairs of external optimization
        functions. Optionally \'basic\' can be passed for a set of predefined
        basic optimizations. Such \'basic\' optimizations were used by default
        in old implementation, however they can be really slow on larger
        expressions. Now, no pre or post optimizations are made by default.
    postprocess : a function which accepts the two return values of cse and
        returns the desired form of output from cse, e.g. if you want the
        replacements reversed the function might be the following lambda:
        lambda r, e: return reversed(r), e
    order : string, \'none\' or \'canonical\'
        The order by which Mul and Add arguments are processed. If set to
        \'canonical\', arguments will be canonically ordered. If set to \'none\',
        ordering will be faster but dependent on expressions hashes, thus
        machine dependent and variable. For large expressions where speed is a
        concern, use the setting order=\'none\'.
    ignore : iterable of Symbols
        Substitutions containing any Symbol from ``ignore`` will be ignored.
    list : bool, (default True)
        Returns expression in list or else with same type as input (when False).

    Returns
    =======

    replacements : list of (Symbol, expression) pairs
        All of the common subexpressions that were replaced. Subexpressions
        earlier in this list might show up in subexpressions later in this
        list.
    reduced_exprs : list of SymPy expressions
        The reduced expressions with all of the replacements above.

    Examples
    ========

    >>> from sympy import cse, SparseMatrix
    >>> from sympy.abc import x, y, z, w
    >>> cse(((w + x + y + z)*(w + y + z))/(w + x)**3)
    ([(x0, y + z), (x1, w + x)], [(w + x0)*(x0 + x1)/x1**3])


    List of expressions with recursive substitutions:

    >>> m = SparseMatrix([x + y, x + y + z])
    >>> cse([(x+y)**2, x + y + z, y + z, x + z + y, m])
    ([(x0, x + y), (x1, x0 + z)], [x0**2, x1, y + z, x1, Matrix([
    [x0],
    [x1]])])

    Note: the type and mutability of input matrices is retained.

    >>> isinstance(_[1][-1], SparseMatrix)
    True

    The user may disallow substitutions containing certain symbols:

    >>> cse([y**2*(x + 1), 3*y**2*(x + 1)], ignore=(y,))
    ([(x0, x + 1)], [x0*y**2, 3*x0*y**2])

    The default return value for the reduced expression(s) is a list, even if there is only
    one expression. The `list` flag preserves the type of the input in the output:

    >>> cse(x)
    ([], [x])
    >>> cse(x, list=False)
    ([], x)
    '''
    pass
# WARNING: Decompyle incomplete


def _cse_homogeneous(exprs, **kwargs):
    """
    Same as ``cse`` but the ``reduced_exprs`` are returned
    with the same type as ``exprs`` or a sympified version of the same.

    Parameters
    ==========

    exprs : an Expr, iterable of Expr or dictionary with Expr values
        the expressions in which repeated subexpressions will be identified
    kwargs : additional arguments for the ``cse`` function

    Returns
    =======

    replacements : list of (Symbol, expression) pairs
        All of the common subexpressions that were replaced. Subexpressions
        earlier in this list might show up in subexpressions later in this
        list.
    reduced_exprs : list of SymPy expressions
        The reduced expressions with all of the replacements above.

    Examples
    ========

    >>> from sympy.simplify.cse_main import cse
    >>> from sympy import cos, Tuple, Matrix
    >>> from sympy.abc import x
    >>> output = lambda x: type(cse(x, list=False)[1])
    >>> output(1)
    <class 'sympy.core.numbers.One'>
    >>> output('cos(x)')
    <class 'str'>
    >>> output(cos(x))
    cos
    >>> output(Tuple(1, x))
    <class 'sympy.core.containers.Tuple'>
    >>> output(Matrix([[1,0], [0,1]]))
    <class 'sympy.matrices.dense.MutableDenseMatrix'>
    >>> output([1, x])
    <class 'list'>
    >>> output((1, x))
    <class 'tuple'>
    >>> output({1, x})
    <class 'set'>
    """
    pass
# WARNING: Decompyle incomplete
