# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kernel.pyc (Python 3.11)

from contextlib import contextmanager
import functools
import sys
import threading
import numpy as np
from cudadrv.devicearray import FakeCUDAArray, FakeWithinKernelCUDAArray
from kernelapi import Dim3, FakeCUDAModule, swapped_cuda_module
from errors import normalize_kernel_dimensions
from args import wrap_arg, ArgHint
_kernel_context = None
_push_kernel_context = (lambda mod: pass# WARNING: Decompyle incomplete
)()

def _get_kernel_context():
    '''
    Get the current kernel context. This is usually done by a device function.
    '''
    return _kernel_context


class FakeOverload:
    '''
    Used only to provide the max_cooperative_grid_blocks method
    '''
    
    def max_cooperative_grid_blocks(self, blockdim):
        return 1



class FakeOverloadDict(dict):
    
    def __getitem__(self, key):
        return FakeOverload()



class FakeCUDAKernel(object):
    '''
    Wraps a @cuda.jit-ed function.
    '''
    
    def __init__(self, fn, device, fastmath, extensions, debug = (False, None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, configuration):
        pass
    # WARNING: Decompyle incomplete

    
    def bind(self):
        pass

    
    def specialize(self, *args):
        return self

    
    def forall(self, ntasks, tpb, stream, sharedmem = (0, 0, 0)):
        if ntasks < 0:
            raise ValueError("Can't create ForAll with negative task count: %s" % ntasks)
        return self[(ntasks, 1, stream, sharedmem)]

    overloads = (lambda self: FakeOverloadDict())()
    py_func = (lambda self: self.fn)()


class BlockThread(threading.Thread):
    pass
# WARNING: Decompyle incomplete


class BlockManager(object):
    '''
    Manages the execution of a thread block.

    When run() is called, all threads are started. Each thread executes until it
    hits syncthreads(), at which point it sets its own syncthreads_blocked to
    True so that the BlockManager knows it is blocked. It then waits on its
    syncthreads_event.

    The BlockManager polls threads to determine if they are blocked in
    syncthreads(). If it finds a blocked thread, it adds it to the set of
    blocked threads. When all threads are blocked, it unblocks all the threads.
    The thread are unblocked by setting their syncthreads_blocked back to False
    and setting their syncthreads_event.

    The polling continues until no threads are alive, when execution is
    complete.
    '''
    
    def __init__(self, f, grid_dim, block_dim, debug):
        self._grid_dim = grid_dim
        self._block_dim = block_dim
        self._f = f
        self._debug = debug
        self.block_state = np.zeros(block_dim, dtype = np.bool_)

    
    def run(self, grid_point, *args):
        pass
    # WARNING: Decompyle incomplete
