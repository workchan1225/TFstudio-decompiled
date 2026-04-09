# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reduction.pyc (Python 3.11)

'''
A library written in CUDA Python for generating reduction kernels
'''
from numba.np.numpy_support import from_dtype
_WARPSIZE = 32
_NUMWARPS = 4

def _gpu_reduce_factory(fn, nbtype):
    pass
# WARNING: Decompyle incomplete


class Reduce(object):
    '''Create a reduction object that reduces values using a given binary
    function. The binary function is compiled once and cached inside this
    object. Keeping this object alive will prevent re-compilation.
    '''
    _cache = { }
    
    def __init__(self, functor):
        '''
        :param functor: A function implementing a binary operation for
                        reduction. It will be compiled as a CUDA device
                        function using ``cuda.jit(device=True)``.
        '''
        self._functor = functor

    
    def _compile(self, dtype):
        key = (self._functor, dtype)
        if key in self._cache:
            kernel = self._cache[key]
        else:
            kernel = _gpu_reduce_factory(self._functor, from_dtype(dtype))
            self._cache[key] = kernel
        return kernel

    
    def __call__(self, arr, size, res, init, stream = (None, None, 0, 0)):
        '''Performs a full reduction.

        :param arr: A host or device array.
        :param size: Optional integer specifying the number of elements in
                    ``arr`` to reduce. If this parameter is not specified, the
                    entire array is reduced.
        :param res: Optional device array into which to write the reduction
                    result to. The result is written into the first element of
                    this array. If this parameter is specified, then no
                    communication of the reduction output takes place from the
                    device to the host.
        :param init: Optional initial value for the reduction, the type of which
                    must match ``arr.dtype``.
        :param stream: Optional CUDA stream in which to perform the reduction.
                    If no stream is specified, the default stream of 0 is
                    used.
        :return: If ``res`` is specified, ``None`` is returned. Otherwise, the
                result of the reduction is returned.
        '''
        cuda = cuda
        import numba
        if arr.ndim != 1:
            raise TypeError('only support 1D array')
    # WARNING: Decompyle incomplete
