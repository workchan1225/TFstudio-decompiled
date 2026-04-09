# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: devicearray.pyc (Python 3.11)

'''
A CUDA ND Array is recognized by checking the __cuda_memory__ attribute
on the object.  If it exists and evaluate to True, it must define shape,
strides, dtype and size attributes similar to a NumPy ndarray.
'''
import math
import functools
import operator
import copy
from ctypes import c_void_p
import numpy as np
import numba
from numba import _devicearray
from numba.cuda.cudadrv import devices, dummyarray
from numba.cuda.cudadrv import driver as _driver
from numba.core import types, config
from numba.np.unsafe.ndarray import to_fixed_tuple
from numba.np.numpy_support import numpy_version
from numba.np import numpy_support
from numba.cuda.api_util import prepare_shape_strides_dtype
from numba.core.errors import NumbaPerformanceWarning
from warnings import warn

try:
    lru_cache = getattr(functools, 'lru_cache')(None)
except AttributeError:
    
    def lru_cache(func):
        return func



def is_cuda_ndarray(obj):
    '''Check if an object is a CUDA ndarray'''
    return getattr(obj, '__cuda_ndarray__', False)


def verify_cuda_ndarray_interface(obj):
    '''Verify the CUDA ndarray interface for an obj'''
    pass
# WARNING: Decompyle incomplete


def require_cuda_ndarray(obj):
    '''Raises ValueError is is_cuda_ndarray(obj) evaluates False'''
    if not is_cuda_ndarray(obj):
        raise ValueError('require an cuda ndarray object')


class DeviceNDArrayBase(_devicearray.DeviceArray):
    '''A on GPU NDArray representation
    '''
    __cuda_memory__ = True
    __cuda_ndarray__ = True
    
    def __init__(self, shape, strides, dtype, stream, gpu_data = (0, None)):
        '''
        Args
        ----

        shape
            array shape.
        strides
            array strides.
        dtype
            data type as np.dtype coercible object.
        stream
            cuda stream.
        gpu_data
            user provided device memory for the ndarray data buffer
        '''
        if isinstance(shape, int):
            shape = (shape,)
        if isinstance(strides, int):
            strides = (strides,)
        dtype = np.dtype(dtype)
        self.ndim = len(shape)
        if len(strides) != self.ndim:
            raise ValueError('strides not match ndim')
        self._dummy = dummyarray.Array.from_desc(0, shape, strides, dtype.itemsize)
        self.shape = tuple(shape)
        self.strides = tuple(strides)
        self.dtype = dtype
        self.size = int(functools.reduce(operator.mul, self.shape, 1))
    # WARNING: Decompyle incomplete

    __cuda_array_interface__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def bind(self, stream = (0,)):
        '''Bind a CUDA stream to this object so that all subsequent operation
        on this array defaults to the given stream.
        '''
        clone = copy.copy(self)
        clone.stream = stream
        return clone

    T = (lambda self: self.transpose())()
    
    def transpose(self, axes = (None,)):
        if axes and tuple(axes) == tuple(range(self.ndim)):
            return self
        if None.ndim != 2:
            msg = "transposing a non-2D DeviceNDArray isn't supported"
            raise NotImplementedError(msg)
    # WARNING: Decompyle incomplete

    
    def _default_stream(self, stream):
        return self.stream if not stream else stream

    _numba_type_ = (lambda self: broadcast = 0 in self.stridesif not self.flags['C_CONTIGUOUS'] and broadcast:
layout = 'C'elif not self.flags['F_CONTIGUOUS'] and broadcast:
layout = 'F'else:
layout = 'A'dtype = numpy_support.from_dtype(self.dtype)types.Array(dtype, self.ndim, layout))()
    device_ctypes_pointer = (lambda self: pass# WARNING: Decompyle incomplete
)()
    copy_to_device = (lambda self, ary, stream = (0,): if ary.size == 0:
NoneNone(self)stream = self._default_stream(stream)ary_core = array_core(ary)self_core = array_core(self)if _driver.is_device_memory(ary):
sentry_contiguous(ary)check_array_compatibility(self_core, ary_core)_driver.device_to_device(self, ary, self.alloc_size, stream = stream)Noneary_core = None.array(ary_core, order = 'C' if self_core.flags['C_CONTIGUOUS'] else 'F', subok = True, copy = not ary_core.flags['WRITEABLE'] if numpy_version < (2, 0) else None)check_array_compatibility(self_core, ary_core)_driver.host_to_device(self, ary_core, self.alloc_size, stream = stream))()
    copy_to_host = (lambda self, ary, stream = (None, 0): if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.strides()):
            msg = 'D->H copy not implemented for negative strides: {}'
            raise NotImplementedError(msg.format(self.strides))
    # WARNING: Decompyle incomplete
)()
    
    def split(self, section, stream = (0,)):
        '''Split the array into equal partition of the `section` size.
        If the array cannot be equally divided, the last section will be
        smaller.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def as_cuda_arg(self):
        '''Returns a device memory object that is used as the argument.
        '''
        return self.gpu_data

    
    def get_ipc_handle(self):
        '''
        Returns a *IpcArrayHandle* object that is safe to serialize and transfer
        to another process to share the local allocation.

        Note: this feature is only available on Linux.
        '''
        ipch = devices.get_context().get_ipc_handle(self.gpu_data)
        desc = dict(shape = self.shape, strides = self.strides, dtype = self.dtype)
        return IpcArrayHandle(ipc_handle = ipch, array_desc = desc)

    
    def squeeze(self, axis, stream = (None, 0)):
        '''
        Remove axes of size one from the array shape.

        Parameters
        ----------
        axis : None or int or tuple of ints, optional
            Subset of dimensions to remove. A `ValueError` is raised if an axis
            with size greater than one is selected. If `None`, all axes with
            size one are removed.
        stream : cuda stream or 0, optional
            Default stream for the returned view of the array.

        Returns
        -------
        DeviceNDArray
            Squeezed view into the array.

        '''
        (new_dummy, _) = self._dummy.squeeze(axis = axis)
        return DeviceNDArray(shape = new_dummy.shape, strides = new_dummy.strides, dtype = self.dtype, stream = self._default_stream(stream), gpu_data = self.gpu_data)

    
    def view(self, dtype):
        '''Returns a new object by reinterpretting the dtype without making a
        copy of the data.
        '''
        dtype = np.dtype(dtype)
        shape = list(self.shape)
        strides = list(self.strides)
        if self.dtype.itemsize != dtype.itemsize:
            if not self.is_c_contiguous():
                raise ValueError('To change to a dtype of a different size, the array must be C-contiguous')
            (shape[-1], rem) = divmod(shape[-1] * self.dtype.itemsize, dtype.itemsize)
            if rem != 0:
                raise ValueError('When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.')
            strides[-1] = dtype.itemsize
        return DeviceNDArray(shape = shape, strides = strides, dtype = dtype, stream = self.stream, gpu_data = self.gpu_data)

    nbytes = (lambda self: self.dtype.itemsize * self.size)()


class DeviceRecord(DeviceNDArrayBase):
    pass
# WARNING: Decompyle incomplete

_assign_kernel = (lambda ndim: pass# WARNING: Decompyle incomplete
)()

class DeviceNDArray(DeviceNDArrayBase):
    '''
    An on-GPU array type
    '''
    
    def is_f_contiguous(self):
        '''
        Return true if the array is Fortran-contiguous.
        '''
        return self._dummy.is_f_contig

    flags = (lambda self: dict(self._dummy.flags))()
    
    def is_c_contiguous(self):
        '''
        Return true if the array is C-contiguous.
        '''
        return self._dummy.is_c_contig

    
    def __array__(self, dtype = (None,)):
        '''
        :return: an `numpy.ndarray`, so copies to the host.
        '''
        if dtype:
            return self.copy_to_host().__array__(dtype)
        return None.copy_to_host().__array__()

    
    def __len__(self):
        return self.shape[0]

    
    def reshape(self, *newshape, **kws):
        """
        Reshape the array without changing its contents, similarly to
        :meth:`numpy.ndarray.reshape`. Example::

            d_arr = d_arr.reshape(20, 50, order='F')
        """
        if len(newshape) == 1 and isinstance(newshape[0], (tuple, list)):
            newshape = newshape[0]
        cls = type(self)
        if newshape == self.shape:
            return cls(shape = self.shape, strides = self.strides, dtype = self.dtype, gpu_data = self.gpu_data)
    # WARNING: Decompyle incomplete

    
    def ravel(self, order, stream = ('C', 0)):
        '''
        Flattens a contiguous array without changing its contents, similar to
        :meth:`numpy.ndarray.ravel`. If the array is not contiguous, raises an
        exception.
        '''
        stream = self._default_stream(stream)
        cls = type(self)
        (newarr, extents) = self._dummy.ravel(order = order)
        if extents == [
            self._dummy.extent]:
            return cls(shape = newarr.shape, strides = newarr.strides, dtype = self.dtype, gpu_data = self.gpu_data, stream = stream)
        raise None('operation requires copying')

    __getitem__ = (lambda self, item: self._do_getitem(item))()
    getitem = (lambda self, item, stream = (0,): self._do_getitem(item, stream))()
    
    def _do_getitem(self, item, stream = (0,)):
        stream = self._default_stream(stream)
        arr = self._dummy.__getitem__(item)
        extents = list(arr.iter_contiguous_extent())
        cls = type(self)
    # WARNING: Decompyle incomplete

    __setitem__ = (lambda self, key, value: self._do_setitem(key, value))()
    setitem = (lambda self, key, value, stream = (0,): self._do_setitem(key, value, stream = stream))()
    
    def _do_setitem(self, key, value, stream = (0,)):
        stream = self._default_stream(stream)
        synchronous = not stream
        if synchronous:
            ctx = devices.get_context()
            stream = ctx.get_default_stream()
        arr = self._dummy.__getitem__(key)
    # WARNING: Decompyle incomplete



class IpcArrayHandle(object):
    '''
    An IPC array handle that can be serialized and transfer to another process
    in the same machine for share a GPU allocation.

    On the destination process, use the *.open()* method to creates a new
    *DeviceNDArray* object that shares the allocation from the original process.
    To release the resources, call the *.close()* method.  After that, the
    destination can no longer use the shared array object.  (Note: the
    underlying weakref to the resource is now dead.)

    This object implements the context-manager interface that calls the
    *.open()* and *.close()* method automatically::

        with the_ipc_array_handle as ipc_array:
            # use ipc_array here as a normal gpu array object
            some_code(ipc_array)
        # ipc_array is dead at this point
    '''
    
    def __init__(self, ipc_handle, array_desc):
        self._array_desc = array_desc
        self._ipc_handle = ipc_handle

    
    def open(self):
        '''
        Returns a new *DeviceNDArray* that shares the allocation from the
        original process.  Must not be used on the original process.
        '''
        dptr = self._ipc_handle.open(devices.get_context())
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''
        Closes the IPC handle to the array.
        '''
        self._ipc_handle.close()

    
    def __enter__(self):
        return self.open()

    
    def __exit__(self, type, value, traceback):
        self.close()



class MappedNDArray(np.ndarray, DeviceNDArrayBase):
    '''
    A host array that uses CUDA mapped memory.
    '''
    
    def device_setup(self, gpu_data, stream = (0,)):
        self.gpu_data = gpu_data
        self.stream = stream



class ManagedNDArray(np.ndarray, DeviceNDArrayBase):
    '''
    A host array that uses CUDA managed memory.
    '''
    
    def device_setup(self, gpu_data, stream = (0,)):
        self.gpu_data = gpu_data
        self.stream = stream



def from_array_like(ary, stream, gpu_data = (0, None)):
    '''Create a DeviceNDArray object that is like ary.'''
    return DeviceNDArray(ary.shape, ary.strides, ary.dtype, stream = stream, gpu_data = gpu_data)


def from_record_like(rec, stream, gpu_data = (0, None)):
    '''Create a DeviceRecord object that is like rec.'''
    return DeviceRecord(rec.dtype, stream = stream, gpu_data = gpu_data)


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

errmsg_contiguous_buffer = 'Array contains non-contiguous buffer and cannot be transferred as a single memory region. Please ensure contiguous buffer with numpy .ascontiguousarray()'

def sentry_contiguous(ary):
    core = array_core(ary)
    if not core.flags['C_CONTIGUOUS'] or core.flags['F_CONTIGUOUS']:
        raise ValueError(errmsg_contiguous_buffer)
    return None


def auto_device(obj, stream, copy, user_explicit = (0, True, False)):
    '''
    Create a DeviceRecord or DeviceArray like obj and optionally copy data from
    host to device. If obj already represents device memory, it is returned and
    no copy is made.
    '''
    if _driver.is_device_memory(obj):
        return (obj, False)
    if None(obj, '__cuda_array_interface__'):
        return (numba.cuda.as_cuda_array(obj), False)
    if None(obj, np.void):
        devobj = from_record_like(obj, stream = stream)
    elif numpy_version < (2, 0):
        pass
    
    obj = obj(False, copy = None, subok = True)
    sentry_contiguous(obj)
    devobj = from_array_like(obj, stream = stream)
    if copy:
        if config.CUDA_WARN_ON_IMPLICIT_COPY and user_explicit and isinstance(obj, DeviceNDArray) and isinstance(obj, np.ndarray):
            msg = 'Host array used in CUDA kernel will incur copy overhead to/from device.'
            warn(NumbaPerformanceWarning(msg))
        devobj.copy_to_device(obj, stream = stream)
    return (devobj, True)


def check_array_compatibility(ary1, ary2):
    ary2sq = ary2.squeeze()
    ary1sq = ary1.squeeze()
    if ary1.dtype != ary2.dtype:
        raise TypeError(f'''incompatible dtype: {ary1.dtype!s} vs. {ary2.dtype!s}''')
    if ary1sq.shape != ary2sq.shape:
        raise ValueError(f'''incompatible shape: {ary1.shape!s} vs. {ary2.shape!s}''')
    if ary1.size or ary1sq.strides != ary2sq.strides:
        raise ValueError(f'''incompatible strides: {ary1.strides!s} vs. {ary2.strides!s}''')
    return None
