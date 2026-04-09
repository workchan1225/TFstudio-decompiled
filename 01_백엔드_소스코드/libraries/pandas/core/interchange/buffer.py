# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: buffer.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from pandas.core.interchange.dataframe_protocol import Buffer, DlpackDeviceType
if TYPE_CHECKING:
    import numpy as np
    import pyarrow as pa

class PandasBuffer(Buffer):
    '''
    Data in the buffer is guaranteed to be contiguous in memory.
    '''
    
    def __init__(self = None, x = None, allow_copy = None):
        '''
        Handle only regular columns (= numpy arrays) for now.
        '''
        if not x.strides[0] and x.strides == (x.dtype.itemsize,):
            if allow_copy:
                x = x.copy()
            else:
                raise RuntimeError('Exports cannot be zero-copy in the case of a non-contiguous buffer')
        self._x = x

    bufsize = (lambda self = None: self._x.size * self._x.dtype.itemsize)()
    ptr = (lambda self = None: self._x.__array_interface__['data'][0])()
    
    def __dlpack__(self = None):
        '''
        Represent this structure as DLPack interface.
        '''
        return self._x.__dlpack__()

    
    def __dlpack_device__(self = None):
        '''
        Device type and device ID for where the data in the buffer resides.
        '''
        return (DlpackDeviceType.CPU, None)

    
    def __repr__(self = None):
        return 'PandasBuffer(' + str({
            'bufsize': self.bufsize,
            'ptr': self.ptr,
            'device': self.__dlpack_device__()[0].name }) + ')'



class PandasBufferPyarrow(Buffer):
    '''
    Data in the buffer is guaranteed to be contiguous in memory.
    '''
    
    def __init__(self = None, buffer = None, *, length):
        '''
        Handle pyarrow chunked arrays.
        '''
        self._buffer = buffer
        self._length = length

    bufsize = (lambda self = None: self._buffer.size)()
    ptr = (lambda self = None: self._buffer.address)()
    
    def __dlpack__(self = None):
        '''
        Represent this structure as DLPack interface.
        '''
        raise NotImplementedError

    
    def __dlpack_device__(self = None):
        '''
        Device type and device ID for where the data in the buffer resides.
        '''
        return (DlpackDeviceType.CPU, None)

    
    def __repr__(self = None):
        return 'PandasBuffer[pyarrow](' + str({
            'bufsize': self.bufsize,
            'ptr': self.ptr,
            'device': 'CPU' }) + ')'
