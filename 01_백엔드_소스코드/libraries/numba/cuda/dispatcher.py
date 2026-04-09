# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dispatcher.pyc (Python 3.11)

import numpy as np
import os
import sys
import ctypes
import functools
from numba.core import config, serialize, sigutils, types, typing, utils
from numba.core.caching import Cache, CacheImpl
from numba.core.compiler_lock import global_compiler_lock
from numba.core.dispatcher import Dispatcher
from numba.core.errors import NumbaPerformanceWarning, NumbaValueError
from numba.core.typing.typeof import Purpose, typeof
from numba.cuda.api import get_current_device
from numba.cuda.args import wrap_arg
from numba.cuda.compiler import compile_cuda, CUDACompiler
from numba.cuda.cudadrv import driver
from numba.cuda.cudadrv.devices import get_context
from numba.cuda.descriptor import cuda_target
from numba.cuda.errors import missing_launch_config_msg, normalize_kernel_dimensions
from numba.cuda import types as cuda_types
from numba import cuda
from numba import _dispatcher
from warnings import warn
cuda_fp16_math_funcs = [
    'hsin',
    'hcos',
    'hlog',
    'hlog10',
    'hlog2',
    'hexp',
    'hexp10',
    'hexp2',
    'hsqrt',
    'hrsqrt',
    'hfloor',
    'hceil',
    'hrcp',
    'hrint',
    'htrunc',
    'hdiv']

class _Kernel(serialize.ReduceMixin):
    pass
# WARNING: Decompyle incomplete


class ForAll(object):
    
    def __init__(self, dispatcher, ntasks, tpb, stream, sharedmem):
        if ntasks < 0:
            raise ValueError("Can't create ForAll with negative task count: %s" % ntasks)
        self.dispatcher = dispatcher
        self.ntasks = ntasks
        self.thread_per_block = tpb
        self.stream = stream
        self.sharedmem = sharedmem

    
    def __call__(self, *args):
        if self.ntasks == 0:
            return None
        if None.dispatcher.specialized:
            specialized = self.dispatcher
    # WARNING: Decompyle incomplete

    
    def _compute_thread_per_block(self, dispatcher):
        tpb = self.thread_per_block
        if tpb != 0:
            return tpb
        ctx = None()
        kernel = next(iter(dispatcher.overloads.values()))
        kwargs = dict(func = kernel._codelibrary.get_cufunc(), b2d_func = 0, memsize = self.sharedmem, blocksizelimit = 1024)
    # WARNING: Decompyle incomplete



class _LaunchConfiguration:
    
    def __init__(self, dispatcher, griddim, blockdim, stream, sharedmem):
        self.dispatcher = dispatcher
        self.griddim = griddim
        self.blockdim = blockdim
        self.stream = stream
        self.sharedmem = sharedmem
        if config.CUDA_LOW_OCCUPANCY_WARNINGS:
            min_grid_size = 128
            grid_size = griddim[0] * griddim[1] * griddim[2]
            if grid_size < min_grid_size:
                msg = f'''Grid size {grid_size} will likely result in GPU under-utilization due to low occupancy.'''
                warn(NumbaPerformanceWarning(msg))
                return None
            return None

    
    def __call__(self, *args):
        return self.dispatcher.call(args, self.griddim, self.blockdim, self.stream, self.sharedmem)



class CUDACacheImpl(CacheImpl):
    
    def reduce(self, kernel):
        return kernel._reduce_states()

    
    def rebuild(self, target_context, payload):
        pass
    # WARNING: Decompyle incomplete

    
    def check_cachable(self, cres):
        return True



class CUDACache(Cache):
    pass
# WARNING: Decompyle incomplete


class CUDADispatcher(serialize.ReduceMixin, Dispatcher):
    pass
# WARNING: Decompyle incomplete
