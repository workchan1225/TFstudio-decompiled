# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: devicearray.pyc (Python 3.11)

'''
The Device Array API is not implemented in the simulator. This module provides
stubs to allow tests to import correctly.
'''
from contextlib import contextmanager
from numba.np.numpy_support import numpy_version
import numpy as np
DeviceRecord = None
from_record_like = None
errmsg_contiguous_buffer = 'Array contains non-contiguous buffer and cannot be transferred as a single memory region. Please ensure contiguous buffer with numpy .ascontiguousarray()'

class FakeShape(tuple):
    pass
# WARNING: Decompyle incomplete


class FakeWithinKernelCUDAArray(object):
    """
    Created to emulate the behavior of arrays within kernels, where either
    array.item or array['item'] is valid (that is, give all structured
    arrays `numpy.recarray`-like semantics). This behaviour does not follow
    the semantics of Python and NumPy with non-jitted code, and will be
    deprecated and removed.
    """
    
    def __init__(self, item):
        pass
    # WARNING: Decompyle incomplete

    
    def __wrap_if_fake(self, item):
        if isinstance(item, FakeCUDAArray):
            return FakeWithinKernelCUDAArray(item)

    
    def __getattr__(self, attrname):
        
        try:
            if attrname in dir(self._item._ary):
                return self.__wrap_if_fake(getattr(self._item._ary, attrname))
            return None.__wrap_if_fake(self._item.__getitem__(attrname))
        except Exception:
            e = None
            if not isinstance(e, AttributeError):
                raise AttributeError(attrname), e
            e = None
            del e
            return None
            e = None
            del e


    
    def __setattr__(self, nm, val):
        self._item.__setitem__(nm, val)

    
    def __getitem__(self, idx):
        return self.__wrap_if_fake(self._item.__getitem__(idx))

    
    def __setitem__(self, idx, val):
        self._item.__setitem__(idx, val)

    
    def __len__(self):
        return len(self._item)

    
    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class FakeCUDAArray(object):
    '''
    Implements the interface of a DeviceArray/DeviceRecord, but mostly just
    wraps a NumPy array.
    '''
    __cuda_ndarray__ = True
    
    def __init__(self, ary, stream = (0,)):
        self._ary = ary
        self.stream = stream

    alloc_size = (lambda self: self._ary.nbytes)()
    nbytes = (lambda self: self._ary.nbytes)()
    
    def __getattr__(self, attrname):
        
        try:
            attr = getattr(self._ary, attrname)
            return attr
        except AttributeError:
            e = None
            msg = "Wrapped array has no attribute '%s'" % attrname
            raise AttributeError(msg), e
            e = None
            del e


    
    def bind(self, stream = (0,)):
        return FakeCUDAArray(self._ary, stream)

    T = (lambda self: self.transpose())()
    
    def transpose(self, axes = (None,)):
        return FakeCUDAArray(np.transpose(self._ary, axes = axes))

    
    def __getitem__(self, idx):
        ret = self._ary.__getitem__(idx)
        if type(ret) not in (np.ndarray, np.void):
            return ret
        return None(ret, stream = self.stream)

    
    def __setitem__(self, idx, val):
        return self._ary.__setitem__(idx, val)

    
    def copy_to_host(self, ary, stream = (None, 0)):
        pass
    # WARNING: Decompyle incomplete

    
    def copy_to_device(self, ary, stream = (0,)):
        '''
        Copy from the provided array into this array.

        This may be less forgiving than the CUDA Python implementation, which
        will copy data up to the length of the smallest of the two arrays,
        whereas this expects the size of the arrays to be equal.
        '''
        sentry_contiguous(self)
        ary_core = array_core(ary)
        self_core = array_core(self)
        if isinstance(ary, FakeCUDAArray):
            sentry_contiguous(ary)
            check_array_compatibility(self_core, ary_core)
        elif self_core.flags['C_CONTIGUOUS']:
            pass
        
        ary_core = ary_core('C', order = 'F', subok = True, copy = False if numpy_version < (2, 0) else None)
        check_array_compatibility(self_core, ary_core)
        np.copyto(self_core._ary, ary_core)

    shape = (lambda self: FakeShape(self._ary.shape))()
    
    def ravel(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def reshape(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def view(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def is_c_contiguous(self):
        return self._ary.flags.c_contiguous

    
    def is_f_contiguous(self):
        return self._ary.flags.f_contiguous

    
    def __str__(self):
        return str(self._ary)

    
    def __repr__(self):
        return repr(self._ary)

    
    def __len__(self):
        return len(self._ary)

    
    def __eq__(self, other):
        return FakeCUDAArray(self._ary == other)

    
    def __ne__(self, other):
        return FakeCUDAArray(self._ary != other)

    
    def __lt__(self, other):
        return FakeCUDAArray(self._ary < other)

    
    def __le__(self, other):
        return FakeCUDAArray(self._ary <= other)

    
    def __gt__(self, other):
        return FakeCUDAArray(self._ary > other)

    
    def __ge__(self, other):
        return FakeCUDAArray(self._ary >= other)

    
    def __add__(self, other):
        return FakeCUDAArray(self._ary + other)

    
    def __sub__(self, other):
        return FakeCUDAArray(self._ary - other)

    
    def __mul__(self, other):
        return FakeCUDAArray(self._ary * other)

    
    def __floordiv__(self, other):
        return FakeCUDAArray(self._ary // other)

    
    def __truediv__(self, other):
        return FakeCUDAArray(self._ary / other)

    
    def __mod__(self, other):
        return FakeCUDAArray(self._ary % other)

    
    def __pow__(self, other):
        return FakeCUDAArray(self._ary ** other)

    
    def split(self, section, stream = (0,)):
        return np.split(self._ary, range(section, len(self), section))()



def array_core(ary):
    '''
    Extract the repeated core of a broadcast array.

    Broadcast arrays are by definition non-contiguous due to repeated
    dimensions, i.e., dimensions with stride 0. In order to ascertain memory
    contiguity and copy the underlying data from such arrays, we must create
    a view without the repeated dimensions.

    '''
    if not ary.strides or ary.size:
        return ary
    core_index = None
    for stride in ary.strides:
        core_index.append(0 if stride == 0 else slice(None))
        return ary[tuple(core_index)]


def is_contiguous(ary):
    '''
    Returns True iff `ary` is C-style contiguous while ignoring
    broadcasted and 1-sized dimensions.
    As opposed to array_core(), it does not call require_context(),
    which can be quite expensive.
    '''
    size = ary.dtype.itemsize
    for shape, stride in zip(reversed(ary.shape), reversed(ary.strides)):
        if shape > 1 and stride != 0:
            if size != stride:
                return False
            None *= shape
        return True


def sentry_contiguous(ary):
    core = array_core(ary)
    if not core.flags['C_CONTIGUOUS'] or core.flags['F_CONTIGUOUS']:
        raise ValueError(errmsg_contiguous_buffer)
    return None


def check_array_compatibility(ary1, ary2):
    ary2sq = ary2.squeeze()
    ary1sq = ary1.squeeze()
    if ary1.dtype != ary2.dtype:
        raise TypeError(f'''incompatible dtype: {ary1.dtype!s} vs. {ary2.dtype!s}''')
    if ary1sq.shape != ary2sq.shape:
        raise ValueError(f'''incompatible shape: {ary1.shape!s} vs. {ary2.shape!s}''')
    if ary1sq.strides != ary2sq.strides:
        raise ValueError(f'''incompatible strides: {ary1.strides!s} vs. {ary2.strides!s}''')


def to_device(ary, stream, copy, to = (0, True, None)):
    ary = np.array(ary, copy = False if numpy_version < (2, 0) else None, subok = True)
    sentry_contiguous(ary)
# WARNING: Decompyle incomplete

pinned = (lambda arg: pass# WARNING: Decompyle incomplete
)()

def mapped_array(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def pinned_array(shape, dtype, strides, order = (np.float64, None, 'C')):
    return np.ndarray(shape = shape, strides = strides, dtype = dtype, order = order)


def managed_array(shape, dtype, strides, order = (np.float64, None, 'C')):
    return np.ndarray(shape = shape, strides = strides, dtype = dtype, order = order)


def device_array(*args, **kwargs):
    stream = kwargs.pop('stream') if 'stream' in kwargs else 0
# WARNING: Decompyle incomplete


def _contiguous_strides_like_array(ary):
