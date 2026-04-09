# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numbers.pyc (Python 3.11)

''' This module provides the unsafe things for targets/numbers.py
'''
from numba.core import types, errors
from numba.core.extending import intrinsic
from llvmlite import ir
viewer = (lambda tyctx, val, viewty: pass# WARNING: Decompyle incomplete
)()
trailing_zeros = (lambda typeingctx, src: if not isinstance(src, types.Integer):
msg = f'''trailing_zeros is only defined for integers, but value passed was \'{src}\'.'''raise errors.NumbaTypeError(msg)
def codegen(context, builder, signature, args):
(src,) = argsbuilder.cttz(src, ir.Constant(ir.IntType(1), 0))(src(src), codegen))()
leading_zeros = (lambda typeingctx, src: if not isinstance(src, types.Integer):
msg = f'''leading_zeros is only defined for integers, but value passed was \'{src}\'.'''raise errors.NumbaTypeError(msg)
def codegen(context, builder, signature, args):
(src,) = argsbuilder.ctlz(src, ir.Constant(ir.IntType(1), 0))(src(src), codegen))()
