# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intrinsics.pyc (Python 3.11)

from llvmlite import ir
from numba import cuda, types
from numba.core import cgutils
from numba.core.errors import RequireLiteralValue, NumbaValueError
from numba.core.typing import signature
from numba.core.extending import overload_attribute
from numba.cuda import nvvmutils
from numba.cuda.extending import intrinsic

def _type_grid_function(ndim):
    val = ndim.literal_value
    if val == 1:
        restype = types.int64
    elif val in (2, 3):
        restype = types.UniTuple(types.int64, val)
    else:
        raise NumbaValueError('argument can only be 1, 2, 3')
    return signature(restype, types.int32)

grid = (lambda typingctx, ndim: if not isinstance(ndim, types.IntegerLiteral):
raise RequireLiteralValue(ndim)sig = _type_grid_function(ndim)
def codegen(context, builder, sig, args):
restype = sig.return_typeif restype == types.int64:
nvvmutils.get_global_id(builder, dim = 1)if None(restype, types.UniTuple):
ids = nvvmutils.get_global_id(builder, dim = restype.count)cgutils.pack_array(builder, ids)(sig, codegen))()
gridsize = (lambda typingctx, ndim: pass# WARNING: Decompyle incomplete
)()
_warpsize = (lambda typingctx: sig = signature(types.int32)
def codegen(context, builder, sig, args):
nvvmutils.call_sreg(builder, 'warpsize')(sig, codegen))()
cuda_warpsize = (lambda mod: 
def get(mod):
_warpsize()get)()
syncthreads = (lambda typingctx: sig = signature(types.none)
def codegen(context, builder, sig, args):
fname = 'llvm.nvvm.barrier0'lmod = builder.modulefnty = ir.FunctionType(ir.VoidType(), ())sync = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(sync, ())context.get_dummy_value()(sig, codegen))()

def _syncthreads_predicate(typingctx, predicate, fname):
    pass
# WARNING: Decompyle incomplete

syncthreads_count = (lambda typingctx, predicate: fname = 'llvm.nvvm.barrier0.popc'_syncthreads_predicate(typingctx, predicate, fname))()
syncthreads_and = (lambda typingctx, predicate: fname = 'llvm.nvvm.barrier0.and'_syncthreads_predicate(typingctx, predicate, fname))()
syncthreads_or = (lambda typingctx, predicate: fname = 'llvm.nvvm.barrier0.or'_syncthreads_predicate(typingctx, predicate, fname))()
