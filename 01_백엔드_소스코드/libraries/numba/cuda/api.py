# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

'''
API that are reported to numba.cuda
'''
import contextlib
import os
import numpy as np
from cudadrv import devicearray, devices, driver
from numba.core import config
from numba.cuda.api_util import prepare_shape_strides_dtype
require_context = devices.require_context
current_context = devices.get_context
gpus = devices.gpus
from_cuda_array_interface = (lambda desc, owner, sync = (None, True): version = desc.get('version')# WARNING: Decompyle incomplete
)()

def as_cuda_array(obj, sync = (True,)):
    '''Create a DeviceNDArray from any object that implements
    the :ref:`cuda array interface <cuda-array-interface>`.

    A view of the underlying GPU buffer is created.  No copying of the data
    is done.  The resulting DeviceNDArray will acquire a reference from `obj`.

    If ``sync`` is ``True``, then the imported stream (if present) will be
    synchronized.
    '''
    if not is_cuda_array(obj):
        raise TypeError("*obj* doesn't implement the cuda array interface.")
    return from_cuda_array_interface(obj.__cuda_array_interface__, owner = obj, sync = sync)


def is_cuda_array(obj):
    '''Test if the object has defined the `__cuda_array_interface__` attribute.

    Does not verify the validity of the interface.
    '''
    return hasattr(obj, '__cuda_array_interface__')


def is_float16_supported():
    '''Whether 16-bit floats are supported.

    float16 is always supported in current versions of Numba - returns True.
    '''
    return True

to_device = (lambda obj, stream, copy, to = (0, True, None): pass# WARNING: Decompyle incomplete
)()
device_array = (lambda shape, dtype, strides, order, stream = (np.float64, None, 'C', 0): (shape, strides, dtype) = prepare_shape_strides_dtype(shape, strides, dtype, order)devicearray.DeviceNDArray(shape = shape, strides = strides, dtype = dtype, stream = stream))()
managed_array = (lambda shape, dtype, strides, order, stream, attach_global = (np.float64, None, 'C', 0, True): (shape, strides, dtype) = prepare_shape_strides_dtype(shape, strides, dtype, order)bytesize = driver.memory_size_from_info(shape, strides, dtype.itemsize)buffer = current_context().memallocmanaged(bytesize, attach_global = attach_global)npary = np.ndarray(shape = shape, strides = strides, dtype = dtype, order = order, buffer = buffer)managedview = np.ndarray.view(npary, type = devicearray.ManagedNDArray)managedview.device_setup(buffer, stream = stream)managedview)()
pinned_array = (lambda shape, dtype, strides, order = (np.float64, None, 'C'): (shape, strides, dtype) = prepare_shape_strides_dtype(shape, strides, dtype, order)bytesize = driver.memory_size_from_info(shape, strides, dtype.itemsize)buffer = current_context().memhostalloc(bytesize)np.ndarray(shape = shape, strides = strides, dtype = dtype, order = order, buffer = buffer))()
mapped_array = (lambda shape, dtype, strides, order, stream, portable, wc = (np.float64, None, 'C', 0, False, False): (shape, strides, dtype) = prepare_shape_strides_dtype(shape, strides, dtype, order)bytesize = driver.memory_size_from_info(shape, strides, dtype.itemsize)buffer = current_context().memhostalloc(bytesize, mapped = True)npary = np.ndarray(shape = shape, strides = strides, dtype = dtype, order = order, buffer = buffer)mappedview = np.ndarray.view(npary, type = devicearray.MappedNDArray)mappedview.device_setup(buffer, stream = stream)mappedview)()
open_ipc_array = (lambda handle, shape, dtype, strides, offset = (None, 0): pass# WARNING: Decompyle incomplete
)()()

def synchronize():
    '''Synchronize the current context.'''
    return current_context().synchronize()


def _contiguous_strides_like_array(ary):
