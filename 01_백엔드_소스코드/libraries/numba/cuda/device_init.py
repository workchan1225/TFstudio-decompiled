# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: device_init.pyc (Python 3.11)

import sys
from numba.cuda import cg
from stubs import threadIdx, blockIdx, blockDim, gridDim, laneid, warpsize, syncwarp, shared, local, const, atomic, shfl_sync_intrinsic, vote_sync_intrinsic, match_any_sync, match_all_sync, threadfence_block, threadfence_system, threadfence, selp, popc, brev, clz, ffs, fma, cbrt, activemask, lanemask_lt, nanosleep, fp16, _vector_type_stubs
from intrinsics import grid, gridsize, syncthreads, syncthreads_and, syncthreads_count, syncthreads_or
from cudadrv.error import CudaSupportError
from numba.cuda.cudadrv.driver import BaseCUDAMemoryManager, HostOnlyCUDAMemoryManager, GetIpcHandleMixin, MemoryPointer, MappedMemory, PinnedMemory, MemoryInfo, IpcHandle, set_memory_manager
from numba.cuda.cudadrv.runtime import runtime
from cudadrv import nvvm
from numba.cuda import initialize
from errors import KernelRuntimeError
from decorators import jit, declare_device
from api import *
from api import _auto_device
from args import In, Out, InOut
from intrinsic_wrapper import all_sync, any_sync, eq_sync, ballot_sync, shfl_sync, shfl_up_sync, shfl_down_sync, shfl_xor_sync
from kernels import reduction
reduce = reduction.Reduce
Reduce = reduction.Reduce
for vector_type_stub in _vector_type_stubs:
    setattr(sys.modules[__name__], vector_type_stub.__name__, vector_type_stub)
    for alias in vector_type_stub.aliases:
        setattr(sys.modules[__name__], alias, vector_type_stub)
        del vector_type_stub
        del _vector_type_stubs
        
        def is_available():
