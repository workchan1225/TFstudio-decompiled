# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval.pyc (Python 3.11)

'''
Top level ``eval`` module.
'''
from __future__ import annotations
import tokenize
from typing import TYPE_CHECKING, Any
import warnings
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg
from pandas.core.dtypes.common import is_extension_array_dtype, is_string_dtype
from pandas.core.computation.engines import ENGINES
from pandas.core.computation.expr import PARSERS, Expr
from pandas.core.computation.parsing import tokenize_string
from pandas.core.computation.scope import ensure_scope
from pandas.core.generic import NDFrame
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from pandas.core.computation.ops import BinOp

def _check_engine(engine = None):
    """
    Make sure a valid engine is passed.

    Parameters
    ----------
    engine : str
        String to validate.

    Raises
    ------
    KeyError
      * If an invalid engine is passed.
    ImportError
      * If numexpr was requested but doesn't exist.

    Returns
    -------
    str
        Engine name.
    """
    NUMEXPR_INSTALLED = NUMEXPR_INSTALLED
    import pandas.core.computation.check
    USE_NUMEXPR = USE_NUMEXPR
    import pandas.core.computation.expressions
# WARNING: Decompyle incomplete


def _check_parser(parser = None):
    '''
    Make sure a valid parser is passed.

    Parameters
    ----------
    parser : str

    Raises
    ------
    KeyError
      * If an invalid parser is passed
    '''
    if parser not in PARSERS:
        raise KeyError(f'''Invalid parser \'{parser}\' passed, valid parsers are {PARSERS.keys()}''')


def _check_resolvers(resolvers = None):
    pass
# WARNING: Decompyle incomplete


def _check_expression(expr = None):
    '''
    Make sure an expression is not an empty string

    Parameters
    ----------
    expr : object
        An object that can be converted to a string

    Raises
    ------
    ValueError
      * If expr is an empty string
    '''
    if not expr:
        raise ValueError('expr cannot be an empty string')


def _convert_expression(expr = None):
    """
    Convert an object to an expression.

    This function converts an object to an expression (a unicode string) and
    checks to make sure it isn't empty after conversion. This is used to
    convert operators to their string representation for recursive calls to
    :func:`~pandas.eval`.

    Parameters
    ----------
    expr : object
        The object to be converted to a string.

    Returns
    -------
    str
        The string representation of an object.

    Raises
    ------
    ValueError
      * If the expression is empty.
    """
    s = pprint_thing(expr)
    _check_expression(s)
    return s


def _check_for_locals(expr = None, stack_level = None, parser = None):
    at_top_of_stack = stack_level == 0
    not_pandas_parser = parser != 'pandas'
    if not_pandas_parser:
        msg = "The '@' prefix is only supported by the pandas parser"
    elif at_top_of_stack:
        msg = "The '@' prefix is not allowed in top-level eval calls.\nplease refer to your variables by name without the '@' prefix."
    if at_top_of_stack or not_pandas_parser:
        for toknum, tokval in tokenize_string(expr):
            if toknum == tokenize.OP and tokval == '@':
                raise SyntaxError(msg)
            return None
            return None

eval = (lambda expr, parser, engine, local_dict, global_dict = None, resolvers = None, level = set_module('pandas'), target = ('pandas', None, None, None, (), 0, None, False), inplace = ('expr', 'str | BinOp', 'parser', 'str', 'engine', 'str | None', 'level', 'int', 'inplace', 'bool', 'return', 'Any'): inplace = validate_bool_kwarg(inplace, 'inplace')multi_line = len(exprs) > 1# WARNING: Decompyle incomplete
)()
