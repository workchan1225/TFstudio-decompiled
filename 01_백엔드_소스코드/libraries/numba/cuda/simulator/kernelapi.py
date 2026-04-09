# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kernelapi.pyc (Python 3.11)

'''
Implements the cuda module as called from within an executing kernel
(@cuda.jit-decorated function).
'''
from contextlib import contextmanager
import sys
import threading
import traceback
from numba.core import types
import numpy as np
from numba.np import numpy_support
from vector_types import vector_types

class Dim3(object):
    '''
    Used to implement thread/block indices/dimensions
    '''
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    
    def __str__(self):
        return f'''({self.x!s}, {self.y!s}, {self.z!s})'''

    
    def __repr__(self):
        return f'''Dim3({self.x!s}, {self.y!s}, {self.z!s})'''

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



class GridGroup:
    '''
    Used to implement the grid group.
    '''
    
    def sync(self):
        threading.current_thread().syncthreads()



class FakeCUDACg:
    '''
    CUDA Cooperative Groups
    '''
    
    def this_grid(self):
        return GridGroup()



class FakeCUDALocal(object):
    '''
    CUDA Local arrays
    '''
    
    def array(self, shape, dtype):
        if isinstance(dtype, types.Type):
            dtype = numpy_support.as_dtype(dtype)
        return np.empty(shape, dtype)



class FakeCUDAConst(object):
    '''
    CUDA Const arrays
    '''
    
    def array_like(self, ary):
        return ary



class FakeCUDAShared(object):
    '''
    CUDA Shared arrays.

    Limitations: assumes that only one call to cuda.shared.array is on a line,
    and that that line is only executed once per thread. i.e.::

        a = cuda.shared.array(...); b = cuda.shared.array(...)

    will erroneously alias a and b, and::

        for i in range(10):
            sharedarrs[i] = cuda.shared.array(...)

    will alias all arrays created at that point (though it is not certain that
    this would be supported by Numba anyway).
    '''
    
    def __init__(self, dynshared_size):
        self._allocations = { }
        self._dynshared_size = dynshared_size
        self._dynshared = np.zeros(dynshared_size, dtype = np.byte)

    
    def array(self, shape, dtype):
        if isinstance(dtype, types.Type):
            dtype = numpy_support.as_dtype(dtype)
        if shape == 0:
            count = self._dynshared_size // dtype.itemsize
            return np.frombuffer(self._dynshared.data, dtype = dtype, count = count)
        stack = None.extract_stack(sys._getframe())
        caller = stack[-2][0:2]
        res = self._allocations.get(caller)
    # WARNING: Decompyle incomplete


addlock = threading.Lock()
sublock = threading.Lock()
andlock = threading.Lock()
orlock = threading.Lock()
xorlock = threading.Lock()
maxlock = threading.Lock()
minlock = threading.Lock()
compare_and_swaplock = threading.Lock()
caslock = threading.Lock()
inclock = threading.Lock()
declock = threading.Lock()
exchlock = threading.Lock()

class FakeCUDAAtomic(object):
    
    def add(self, array, index, val):
        addlock
        old = array[index]
        None(None, None)

    
    def sub(self, array, index, val):
        sublock
        old = array[index]
        None(None, None)

    
    def and_(self, array, index, val):
        andlock
        old = array[index]
        None(None, None)

    
    def or_(self, array, index, val):
        orlock
        old = array[index]
        None(None, None)

    
    def xor(self, array, index, val):
        xorlock
        old = array[index]
        None(None, None)

    
    def inc(self, array, index, val):
        inclock
        old = array[index]
        if old >= val:
            array[index] = 0
        
        None(None, None)

    
    def dec(self, array, index, val):
        declock
        old = array[index]
        if old == 0 or old > val:
            array[index] = val
        
        None(None, None)

    
    def exch(self, array, index, val):
        exchlock
        old = array[index]
        array[index] = val
        None(None, None)

    
    def max(self, array, index, val):
        maxlock
        old = array[index]
        array[index] = max(old, val)
        None(None, None)

    
    def min(self, array, index, val):
        minlock
        old = array[index]
        array[index] = min(old, val)
        None(None, None)

    
    def nanmax(self, array, index, val):
        maxlock
        old = array[index]
        array[index] = np.nanmax([
            array[index],
            val])
        None(None, None)

    
    def nanmin(self, array, index, val):
        minlock
        old = array[index]
        array[index] = np.nanmin([
            array[index],
            val])
        None(None, None)

    
    def compare_and_swap(self, array, old, val):
        compare_and_swaplock
        index = (0,) * array.ndim
        loaded = array[index]
        if loaded == old:
            array[index] = val
        None(None, None)
        return 
        with None:
            if not None, loaded:
                pass

    
    def cas(self, array, index, old, val):
        caslock
        loaded = array[index]
        if loaded == old:
            array[index] = val
        None(None, None)
        return 
        with None:
            if not None, loaded:
                pass



class FakeCUDAFp16(object):
    
    def hadd(self, a, b):
        return a + b

    
    def hsub(self, a, b):
        return a - b

    
    def hmul(self, a, b):
        return a * b

    
    def hdiv(self, a, b):
        return a / b

    
    def hfma(self, a, b, c):
        return a * b + c

    
    def hneg(self, a):
        return -a

    
    def habs(self, a):
        return abs(a)

    
    def hsin(self, x):
        return np.sin(x, dtype = np.float16)

    
    def hcos(self, x):
        return np.cos(x, dtype = np.float16)

    
    def hlog(self, x):
        return np.log(x, dtype = np.float16)

    
    def hlog2(self, x):
        return np.log2(x, dtype = np.float16)

    
    def hlog10(self, x):
        return np.log10(x, dtype = np.float16)

    
    def hexp(self, x):
        return np.exp(x, dtype = np.float16)

    
    def hexp2(self, x):
        return np.exp2(x, dtype = np.float16)

    
    def hexp10(self, x):
        return np.float16(10 ** x)

    
    def hsqrt(self, x):
        return np.sqrt(x, dtype = np.float16)

    
    def hrsqrt(self, x):
        return np.float16(x ** -0.5)

    
    def hceil(self, x):
        return np.ceil(x, dtype = np.float16)

    
    def hfloor(self, x):
        return np.ceil(x, dtype = np.float16)

    
    def hrcp(self, x):
        return np.reciprocal(x, dtype = np.float16)

    
    def htrunc(self, x):
        return np.trunc(x, dtype = np.float16)

    
    def hrint(self, x):
        return np.rint(x, dtype = np.float16)

    
    def heq(self, a, b):
        return a == b

    
    def hne(self, a, b):
        return a != b

    
    def hge(self, a, b):
        return a >= b

    
    def hgt(self, a, b):
        return a > b

    
    def hle(self, a, b):
        return a <= b

    
    def hlt(self, a, b):
        return a < b

    
    def hmax(self, a, b):
        return max(a, b)

    
    def hmin(self, a, b):
        return min(a, b)



class FakeCUDAModule(object):
    '''
    An instance of this class will be injected into the __globals__ for an
    executing function in order to implement calls to cuda.*. This will fail to
    work correctly if the user code does::

        from numba import cuda as something_else

    In other words, the CUDA module must be called cuda.
    '''
    
    def __init__(self, grid_dim, block_dim, dynshared_size):
        pass
    # WARNING: Decompyle incomplete

    cg = (lambda self: self._cg)()
    local = (lambda self: self._local)()
    shared = (lambda self: self._shared)()
    const = (lambda self: self._const)()
    atomic = (lambda self: self._atomic)()
    fp16 = (lambda self: self._fp16)()
    threadIdx = (lambda self: threading.current_thread().threadIdx)()
    blockIdx = (lambda self: threading.current_thread().blockIdx)()
    warpsize = (lambda self: 32)()
    laneid = (lambda self: threading.current_thread().thread_id % 32)()
    
    def syncthreads(self):
        threading.current_thread().syncthreads()

    
    def threadfence(self):
        pass

    
    def threadfence_block(self):
        pass

    
    def threadfence_system(self):
        pass

    
    def syncthreads_count(self, val):
        return threading.current_thread().syncthreads_count(val)

    
    def syncthreads_and(self, val):
        return threading.current_thread().syncthreads_and(val)

    
    def syncthreads_or(self, val):
        return threading.current_thread().syncthreads_or(val)

    
    def popc(self, val):
        return bin(val).count('1')

    
    def fma(self, a, b, c):
        return a * b + c

    
    def cbrt(self, a):
        return a ** 0.333333

    
    def brev(self, val):
        return int('{:032b}'.format(val)[::-1], 2)

    
    def clz(self, val):
        s = '{:032b}'.format(val)
        return len(s) - len(s.lstrip('0'))

    
    def ffs(self, val):
        s = '{:032b}'.format(val)
        r = ((len(s) - len(s.rstrip('0'))) + 1) % 33
        return r

    
    def selp(self, a, b, c):
        return b if a else c

    
    def grid(self, n):
        bdim = self.blockDim
        bid = self.blockIdx
        tid = self.threadIdx
        x = bid.x * bdim.x + tid.x
        if n == 1:
            return x
        y = None.y * bdim.y + tid.y
        if n == 2:
            return (x, y)
        z = None.z * bdim.z + tid.z
        if n == 3:
            return (x, y, z)
        raise None('Global ID has 1-3 dimensions. %d requested' % n)

    
    def gridsize(self, n):
        bdim = self.blockDim
        gdim = self.gridDim
        x = bdim.x * gdim.x
        if n == 1:
            return x
        y = None.y * gdim.y
        if n == 2:
            return (x, y)
        z = None.z * gdim.z
        if n == 3:
            return (x, y, z)
        raise None('Global grid has 1-3 dimensions. %d requested' % n)


swapped_cuda_module = (lambda fn, fake_cuda_module: pass# WARNING: Decompyle incomplete
)()
