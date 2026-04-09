# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dummyarray.pyc (Python 3.11)

from collections import namedtuple
import itertools
import functools
import operator
import ctypes
import numpy as np
from numba import _helperlib
Extent = namedtuple('Extent', [
    'begin',
    'end'])
attempt_nocopy_reshape = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_long, np.ctypeslib.ndpointer(np.ctypeslib.c_intp, ndim = 1), np.ctypeslib.ndpointer(np.ctypeslib.c_intp, ndim = 1), ctypes.c_long, np.ctypeslib.ndpointer(np.ctypeslib.c_intp, ndim = 1), np.ctypeslib.ndpointer(np.ctypeslib.c_intp, ndim = 1), ctypes.c_long, ctypes.c_int)(_helperlib.c_helpers['attempt_nocopy_reshape'])

class Dim(object):
    '''A single dimension of the array

    Attributes
    ----------
    start:
        start offset
    stop:
        stop offset
    size:
        number of items
    stride:
        item stride
    '''
    __slots__ = ('start', 'stop', 'size', 'stride', 'single')
    
    def __init__(self, start, stop, size, stride, single):
        self.start = start
        self.stop = stop
        self.size = size
        self.stride = stride
        self.single = single
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, item):
        if isinstance(item, slice):
            (start, stop, step) = item.indices(self.size)
            stride = step * self.stride
            start = self.start + start * abs(self.stride)
            stop = self.start + stop * abs(self.stride)
            if stride == 0:
                size = 1
            else:
                size = _compute_size(start, stop, stride)
            ret = Dim(start = start, stop = stop, size = size, stride = stride, single = False)
            return ret
        sliced = self[item:item + 1] if None != -1 else self[-1:]
        if sliced.size != 1:
            raise IndexError
        return Dim(start = sliced.start, stop = sliced.stop, size = sliced.size, stride = sliced.stride, single = True)

    
    def get_offset(self, idx):
        return self.start + idx * self.stride

    
    def __repr__(self):
        strfmt = 'Dim(start=%s, stop=%s, size=%s, stride=%s)'
        return strfmt % (self.start, self.stop, self.size, self.stride)

    
    def normalize(self, base):
        return Dim(start = self.start - base, stop = self.stop - base, size = self.size, stride = self.stride, single = self.single)

    
    def copy(self, start, stop, size, stride, single = (None, None, None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def is_contiguous(self, itemsize):
        return self.stride == itemsize



def compute_index(indices, dims):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(indices, dims)())


class Element(object):
    is_array = False
    
    def __init__(self, extent):
        self.extent = extent

    
    def iter_contiguous_extent(self):
        pass
    # WARNING: Decompyle incomplete



class Array(object):
    '''A dummy numpy array-like object.  Consider it an array without the
    actual data, but offset from the base data pointer.

    Attributes
    ----------
    dims: tuple of Dim
        describing each dimension of the array

    ndim: int
        number of dimension

    shape: tuple of int
        size of each dimension

    strides: tuple of int
        stride of each dimension

    itemsize: int
        itemsize

    extent: (start, end)
        start and end offset containing the memory region
    '''
    is_array = True
    from_desc = (lambda cls, offset, shape, strides, itemsize: dims = []for ashape, astride in zip(shape, strides):
dim = Dim(offset, offset + ashape * astride, ashape, astride, single = False)dims.append(dim)offset = 0cls(dims, itemsize))()
    
    def __init__(self, dims, itemsize):
        self.dims = tuple(dims)
        self.ndim = len(self.dims)
        self.shape = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.dims())
        self.strides = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.dims())
        self.itemsize = itemsize
        self.size = functools.reduce(operator.mul, self.shape, 1)
        self.extent = self._compute_extent()
        self.flags = self._compute_layout()

    
    def _compute_layout(self):
        if not self.dims:
            return {
                'C_CONTIGUOUS': True,
                'F_CONTIGUOUS': True }
        if (lambda .0: [ dim.stride == 0 for dim in .0 ])(self.dims()):
            return {
                'C_CONTIGUOUS': False,
                'F_CONTIGUOUS': False }
        flags = {
            'C_CONTIGUOUS': None,
            'F_CONTIGUOUS': True }
        sd = self.itemsize
        for dim in reversed(self.dims):
            if dim.size == 0:
                
                return None, {
                    'C_CONTIGUOUS': True,
                    'F_CONTIGUOUS': True }
            if None.size != 1:
                if dim.stride != sd:
                    pass
                sd *= dim.size = False
            sd = self.itemsize
            for dim in self.dims:
                if dim.size != 1:
                    if dim.stride != sd:
                        flags['F_CONTIGUOUS'] = False
                        
                        return None, flags
                return flags

    
    def _compute_extent(self):
        firstidx = [
            0] * self.ndim
        lastidx = self.shape()
        start = compute_index(firstidx, self.dims)
        stop = compute_index(lastidx, self.dims) + self.itemsize
        stop = max(stop, start)
        return Extent(start, stop)

    
    def __repr__(self):
        return f'''<Array dims={self.dims!s} itemsize={self.itemsize!s}>'''

    
    def __getitem__(self, item):
        if not isinstance(item, tuple):
            item = [
                item]
        else:
            item = list(item)
        nitem = len(item)
        ndim = len(self.dims)
        if nitem > ndim:
            raise IndexError('%d extra indices given' % (nitem - ndim,))
    # WARNING: Decompyle incomplete

    is_c_contig = (lambda self: self.flags['C_CONTIGUOUS'])()
    is_f_contig = (lambda self: self.flags['F_CONTIGUOUS'])()
    
    def iter_contiguous_extent(self):
        ''' Generates extents
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def reshape(self, *newdims, **kws):
        oldnd = self.ndim
        newnd = len(newdims)
        if newdims == self.shape:
            return (self, None)
        order = None.pop('order', 'C')
        if kws:
            raise TypeError('unknown keyword arguments %s' % kws.keys())
        if order not in 'CFA':
            raise ValueError('order not C|F|A')
        unknownidx = -1
        knownsize = 1
        for i, dim in enumerate(newdims):
            if dim < 0:
                if unknownidx == -1:
                    unknownidx = i
                    continue
                raise ValueError('can only specify one unknown dimension')
            knownsize *= dim
            if unknownidx >= 0:
                if knownsize == 0 or self.size % knownsize != 0:
                    raise ValueError('cannot infer valid shape for unknown dimension')
                newdims = newdims[0:unknownidx] + (self.size // knownsize,) + newdims[unknownidx + 1:]
        newsize = functools.reduce(operator.mul, newdims, 1)
        if order == 'A':
            order = 'F' if self.is_f_contig else 'C'
        if newsize != self.size:
            raise ValueError('reshape changes the size of the array')
        if self.is_c_contig or self.is_f_contig:
            if order == 'C':
                newstrides = list(iter_strides_c_contig(self, newdims))
            elif order == 'F':
                newstrides = list(iter_strides_f_contig(self, newdims))
            else:
                raise AssertionError('unreachable')
        newstrides = np.empty(newnd, np.ctypeslib.c_intp)
        olddims = np.array(self.shape, dtype = np.ctypeslib.c_intp)
        oldstrides = np.array(self.strides, dtype = np.ctypeslib.c_intp)
        newdims = np.array(newdims, dtype = np.ctypeslib.c_intp)
        if not attempt_nocopy_reshape(oldnd, olddims, oldstrides, newnd, newdims, newstrides, self.itemsize, order == 'F'):
            raise NotImplementedError('reshape would require copy')
        ret = self.from_desc(self.extent.begin, shape = newdims, strides = newstrides, itemsize = self.itemsize)
        return (ret, list(self.iter_contiguous_extent()))

    
    def squeeze(self, axis = (None,)):
        newstrides = []
        newshape = []
    # WARNING: Decompyle incomplete

    
    def ravel(self, order = ('C',)):
        if order not in 'CFA':
            raise ValueError('order not C|F|A')
        if (order in 'CA' or self.is_c_contig or order in 'FA') and self.is_f_contig:
            newshape = (self.size,)
            newstrides = (self.itemsize,)
            arr = self.from_desc(self.extent.begin, newshape, newstrides, self.itemsize)
            return (arr, list(self.iter_contiguous_extent()))
        raise None('ravel on non-contiguous array')



def iter_strides_f_contig(arr, shape = (None,)):
    '''yields the f-contiguous strides
    '''
    pass
# WARNING: Decompyle incomplete


def iter_strides_c_contig(arr, shape = (None,)):
    '''yields the c-contiguous strides
    '''
    pass
# WARNING: Decompyle incomplete


def is_element_indexing(item, ndim):
    if isinstance(item, slice):
        return False
    if None(item, tuple):
        if not len(item) == ndim and (lambda .0: pass# WARNING: Decompyle incomplete
)(item()):
            return True
    return True
    return False


def _compute_size(start, stop, step):
    '''Algorithm adapted from cpython rangeobject.c
    '''
    if step > 0:
        lo = start
        hi = stop
    else:
        lo = stop
        hi = start
        step = -step
    if lo >= hi:
        return 0
    return (None - lo - 1) // step + 1
