# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pylowering.pyc (Python 3.11)

__doc__ = '\nLowering implementation for object mode.\n'
import builtins
import operator
import inspect
from functools import cached_property
import llvmlite.ir as llvmlite
from numba.core import types, utils, ir, generators, cgutils
from numba.core.errors import ForbiddenConstruct, LoweringError, NumbaNotImplementedError
from numba.core.lowering import BaseLower
_unsupported_builtins = set([
    locals])

class _Undefined:
    '''
    A sentinel value for undefined variable created by Expr.undef.
    '''
    
    def __repr__(self):
        return '<undefined>'


_UNDEFINED = _Undefined()
# WARNING: Decompyle incomplete
