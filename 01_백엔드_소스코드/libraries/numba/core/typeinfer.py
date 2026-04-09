# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typeinfer.pyc (Python 3.11)

'''
Type inference base on CPA.
The algorithm guarantees monotonic growth of type-sets for each variable.

Steps:
    1. seed initial types
    2. build constraints
    3. propagate constraints
    4. unify types

Constraint propagation is precise and does not regret (no backtracing).
Constraints push types forward following the dataflow.
'''
import logging
import operator
import contextlib
import itertools
from pprint import pprint
from collections import OrderedDict, defaultdict
from functools import reduce
from numba.core import types, utils, typing, ir, config
from numba.core.typing.templates import Signature
from numba.core.errors import TypingError, UntypedAttributeError, new_error_context, termcolor, UnsupportedError, ForceLiteralArg, CompilerError, NumbaValueError
from numba.core.funcdesc import qualifying_prefix
from numba.core.typeconv import Conversion
_logger = logging.getLogger(__name__)

class NOTSET:
    pass

_termcolor = termcolor()

class TypeVar(object):
    
    def __init__(self, context, var):
        self.context = context
        self.var = var
        self.type = None
        self.locked = False
        self.define_loc = None
        self.literal_value = NOTSET

    
    def add_type(self, tp, loc):
        pass
    # WARNING: Decompyle incomplete

    
    def lock(self, tp, loc, literal_value = (NOTSET,)):
        pass
    # WARNING: Decompyle incomplete

    
    def union(self, other, loc):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
