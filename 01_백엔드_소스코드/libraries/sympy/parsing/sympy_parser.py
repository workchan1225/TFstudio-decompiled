# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sympy_parser.pyc (Python 3.11)

'''Transform a string with Python-like source code into SymPy expression. '''
from tokenize import generate_tokens, untokenize, TokenError, NUMBER, STRING, NAME, OP, ENDMARKER, ERRORTOKEN, NEWLINE
from keyword import iskeyword
import ast
import unicodedata
from io import StringIO
import builtins
import types
from typing import Tuple as tTuple, Dict as tDict, Any, Callable, List, Optional, Union as tUnion
from sympy.assumptions.ask import AssumptionKeys
from sympy.core.basic import Basic
from sympy.core import Symbol
from sympy.core.function import Function
from sympy.utilities.misc import func_name
from sympy.functions.elementary.miscellaneous import Max, Min
null = ''
TOKEN = tTuple[(int, str)]
DICT = tDict[(str, Any)]
TRANS = Callable[([
    List[TOKEN],
    DICT,
    DICT], List[TOKEN])]

def _token_splittable(token_name = None):
    """
    Predicate for whether a token name can be split into multiple tokens.

    A token is splittable if it does not contain an underscore character and
    it is not the name of a Greek letter. This is used to implicitly convert
    expressions like 'xyz' into 'x*y*z'.
    """
    if '_' in token_name:
        return False
    
    try:
        return not unicodedata.lookup('GREEK SMALL LETTER ' + token_name)
    except KeyError:
        return 



def _token_callable(token = None, local_dict = None, global_dict = None, nextToken = (None,)):
