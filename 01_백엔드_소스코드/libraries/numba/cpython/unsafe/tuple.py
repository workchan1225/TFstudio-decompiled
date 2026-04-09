# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tuple.pyc (Python 3.11)

'''
This file provides internal compiler utilities that support certain special
operations with tuple and workarounds for limitations enforced in userland.
'''
from numba.core import types, typing, errors
from numba.core.cgutils import alloca_once
from numba.core.extending import intrinsic
tuple_setitem = (lambda typingctx, tup, idx, val: 
def codegen(context, builder, signature, args):
(tup, idx, val) = argsstack = alloca_once(builder, tup.type)builder.store(tup, stack)offptr = builder.gep(stack, [
idx.type(0),
idx], inbounds = True)builder.store(val, offptr)builder.load(stack)sig = tup(tup, idx, tup.dtype)(sig, codegen))()
build_full_slice_tuple = (lambda tyctx, sz: pass# WARNING: Decompyle incomplete
)()
unpack_single_tuple = (lambda tyctx, tup: if not isinstance(tup, types.BaseTuple):
msg = f'''Only tuples are supported when unpacking a single item, got type: {tup}'''raise errors.UnsupportedError(msg)sig = tup(tup)
def codegen(context, builder, signature, args):
args[0](sig, codegen))()
