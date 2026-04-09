# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expr.pyc (Python 3.11)

__doc__ = '\n:func:`~pandas.eval` parsers.\n'
from __future__ import annotations
import ast
from functools import partial, reduce
from keyword import iskeyword
import tokenize
from typing import TYPE_CHECKING, ClassVar, TypeVar
import numpy as np
from pandas.errors import UndefinedVariableError
from pandas.core.dtypes.common import is_string_dtype

common
from pandas.core.computation.ops import ARITH_OPS_SYMS, BOOL_OPS_SYMS, CMP_OPS_SYMS, LOCAL_TAG, MATHOPS, REDUCTIONS, UNARY_OPS_SYMS, BinOp, Constant, FuncNode, Op, Term, UnaryOp, is_term
BOOL_OPS_SYMS = BOOL_OPS_SYMS
CMP_OPS_SYMS = CMP_OPS_SYMS
LOCAL_TAG = LOCAL_TAG
MATHOPS = MATHOPS
REDUCTIONS = REDUCTIONS
UNARY_OPS_SYMS = UNARY_OPS_SYMS
BinOp = BinOp
Constant = Constant
FuncNode = FuncNode
Op = Op
Term = Term
UnaryOp = UnaryOp
is_term = is_term
import pandas.core.common, core
from pandas.core.computation.parsing import clean_backtick_quoted_toks, tokenize_string
from pandas.core.computation.scope import Scope
from pandas.io.formats import printing
if TYPE_CHECKING:
    from collections.abc import Callable

def _rewrite_assign(tok = None):
    '''
    Rewrite the assignment operator for PyTables expressions that use ``=``
    as a substitute for ``==``.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tuple of int, str
        Either the input or token or the replacement values
    '''
    (toknum, tokval) = tok
    return (toknum, '==' if tokval == '=' else tokval)


def _replace_booleans(tok = None):
    '''
    Replace ``&`` with ``and`` and ``|`` with ``or`` so that bitwise
    precedence is changed to boolean precedence.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tuple of int, str
        Either the input or token or the replacement values
    '''
    (toknum, tokval) = tok
    if toknum == tokenize.OP:
        if tokval == '&':
            return (tokenize.NAME, 'and')
        if None == '|':
            return (tokenize.NAME, 'or')
        return (None, tokval)
    return (None, tokval)


def _replace_locals(tok = None):
    """
    Replace local variables with a syntactically valid name.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tuple of int, str
        Either the input or token or the replacement values

    Notes
    -----
    This is somewhat of a hack in that we rewrite a string such as ``'@a'`` as
    ``'__pd_eval_local_a'`` by telling the tokenizer that ``__pd_eval_local_``
    is a ``tokenize.OP`` and to replace the ``'@'`` symbol with it.
    """
    (toknum, tokval) = tok
    if toknum == tokenize.OP and tokval == '@':
        return (tokenize.OP, LOCAL_TAG)
    return (None, tokval)


def _compose2(f, g):
    '''
    Compose 2 callables.
    '''
    pass
# WARNING: Decompyle incomplete


def _compose(*funcs):
    '''
    Compose 2 or more callables.
    '''
    pass
# WARNING: Decompyle incomplete


def _preparse(source = None, f = None):
    '''
    Compose a collection of tokenization functions.

    Parameters
    ----------
    source : str
        A Python source code string
    f : callable
        This takes a tuple of (toknum, tokval) as its argument and returns a
        tuple with the same structure but possibly different elements. Defaults
        to the composition of ``_rewrite_assign``, ``_replace_booleans``, and
        ``_replace_locals``.

    Returns
    -------
    str
        Valid Python source code

    Notes
    -----
    The `f` parameter can be any callable that takes *and* returns input of the
    form ``(toknum, tokval)``, where ``toknum`` is one of the constants from
    the ``tokenize`` module and ``tokval`` is a string.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_type(t):
    '''
    Factory for a type checking function of type ``t`` or tuple of types.
    '''
    pass
# WARNING: Decompyle incomplete

_is_list = _is_type(list)
_is_str = _is_type(str)
_all_nodes = (lambda .0: pass# WARNING: Decompyle incomplete
)(dir(ast)()())

def _filter_nodes(superclass, all_nodes = (_all_nodes,)):
    '''
    Filter out AST nodes that are subclasses of ``superclass``.
    '''
    pass
# WARNING: Decompyle incomplete

_all_node_names = (lambda .0: pass# WARNING: Decompyle incomplete
)(_all_nodes())
_mod_nodes = _filter_nodes(ast.mod)
_stmt_nodes = _filter_nodes(ast.stmt)
_expr_nodes = _filter_nodes(ast.expr)
_expr_context_nodes = _filter_nodes(ast.expr_context)
_boolop_nodes = _filter_nodes(ast.boolop)
_operator_nodes = _filter_nodes(ast.operator)
_unary_op_nodes = _filter_nodes(ast.unaryop)
_cmp_op_nodes = _filter_nodes(ast.cmpop)
_comprehension_nodes = _filter_nodes(ast.comprehension)
_handler_nodes = _filter_nodes(ast.excepthandler)
_arguments_nodes = _filter_nodes(ast.arguments)
_keyword_nodes = _filter_nodes(ast.keyword)
_alias_nodes = _filter_nodes(ast.alias)
_hacked_nodes = frozenset([
    'Assign',
    'Module',
    'Expr'])
_unsupported_expr_nodes = frozenset([
    'Yield',
    'GeneratorExp',
    'IfExp',
    'DictComp',
    'SetComp',
    'Repr',
    'Lambda',
    'Set',
    'AST',
    'Is',
    'IsNot'])
_unsupported_nodes = (_stmt_nodes | _mod_nodes | _handler_nodes | _arguments_nodes | _keyword_nodes | _alias_nodes | _expr_context_nodes | _unsupported_expr_nodes) - _hacked_nodes
_base_supported_nodes = _all_node_names - _unsupported_nodes | _hacked_nodes
intersection = _unsupported_nodes & _base_supported_nodes
_msg = f'''cannot both support and not support {intersection}'''
# WARNING: Decompyle incomplete
