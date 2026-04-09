# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array_exprs.pyc (Python 3.11)

import ast
from collections import defaultdict, OrderedDict
import contextlib
import sys
from types import SimpleNamespace
import numpy as np
import operator
from numba.core import types, targetconfig, ir, rewrites, compiler
from numba.core.typing import npydecl
from numba.np.ufunc.dufunc import DUFunc

def _is_ufunc(func):
    return isinstance(func, (np.ufunc, DUFunc))

RewriteArrayExprs = <NODE:12>()
_unaryops = {
    operator.invert: ast.Invert,
    operator.neg: ast.USub,
    operator.pos: ast.UAdd }
_binops = {
    operator.floordiv: ast.FloorDiv,
    operator.pow: ast.Pow,
    operator.and_: ast.BitAnd,
    operator.lshift: ast.LShift,
    operator.xor: ast.BitXor,
    operator.rshift: ast.RShift,
    operator.or_: ast.BitOr,
    operator.mod: ast.Mod,
    operator.truediv: ast.Div,
    operator.mul: ast.Mult,
    operator.sub: ast.Sub,
    operator.add: ast.Add }
_cmpops = {
    operator.ge: ast.GtE,
    operator.gt: ast.Gt,
    operator.le: ast.LtE,
    operator.lt: ast.Lt,
    operator.ne: ast.NotEq,
    operator.eq: ast.Eq }

def _arr_expr_to_ast(expr):
    '''Build a Python expression AST from an array expression built by
    RewriteArrayExprs.
    '''
    pass
# WARNING: Decompyle incomplete

_legalize_parameter_names = (lambda var_list: pass# WARNING: Decompyle incomplete
)()

class _EraseInvalidLineRanges(ast.NodeTransformer):
    pass
# WARNING: Decompyle incomplete


def _fix_invalid_lineno_ranges(astree = rewrites.register_rewrite('after-inference')):
    '''Inplace fixes invalid lineno ranges.
    '''
    ast.fix_missing_locations(astree)
    _EraseInvalidLineRanges().visit(astree)
    ast.fix_missing_locations(astree)


def _lower_array_expr(lowerer, expr):
    '''Lower an array expression built by RewriteArrayExprs.
    '''
    pass
# WARNING: Decompyle incomplete
