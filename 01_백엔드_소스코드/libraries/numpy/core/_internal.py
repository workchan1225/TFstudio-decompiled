# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _internal.pyc (Python 3.11)

__doc__ = '\nA place for internal code\n\nSome things are more easily handled Python.\n\n'
import ast
import re
import sys
import warnings
from exceptions import DTypePromotionError
from multiarray import dtype, array, ndarray, promote_types

try:
    import ctypes
except ImportError:
    ctypes = None

IS_PYPY = sys.implementation.name == 'pypy'
if sys.byteorder == 'little':
    _nbo = '<'
else:
    _nbo = '>'

def _makenames_list(adict, align):
    allfields = []
    for fname, obj in adict.items():
        n = len(obj)
        if isinstance(obj, tuple) or n not in (2, 3):
            raise ValueError('entry not a 2- or 3- tuple')
        if n > 2 and obj[2] == fname:
            continue
        num = int(obj[1])
        if num < 0:
            raise ValueError('invalid offset.')
        format = dtype(obj[0], align = align)
        if n > 2:
            title = obj[2]
        else:
            title = None
        allfields.append((fname, format, num, title))
        allfields.sort(key = (lambda x: x[2]))
        names = allfields()
        formats = allfields()
        offsets = allfields()
        titles = allfields()
        return (names, formats, offsets, titles)


def _usefields(adict, align):
    
    try:
        names = adict[-1]
    except KeyError:
        names = None

# WARNING: Decompyle incomplete


def _array_descr(descriptor):
    pass
# WARNING: Decompyle incomplete


def _reconstruct(subtype, shape, dtype):
    return ndarray.__new__(subtype, shape, dtype)

format_re = re.compile('(?P<order1>[<>|=]?)(?P<repeats> *[(]?[ ,0-9]*[)]? *)(?P<order2>[<>|=]?)(?P<dtype>[A-Za-z0-9.?]*(?:\\[[a-zA-Z0-9,.]+\\])?)')
sep_re = re.compile('\\s*,\\s*')
space_re = re.compile('\\s+$')
_convorder = {
    '=': _nbo }

def _commastring(astr):
    startindex = 0
    result = []
# WARNING: Decompyle incomplete


class dummy_ctype:
    
    def __init__(self, cls):
        self._cls = cls

    
    def __mul__(self, other):
        return self

    
    def __call__(self, *other):
        return self._cls(other)

    
    def __eq__(self, other):
        return self._cls == other._cls

    
    def __ne__(self, other):
        return self._cls != other._cls



def _getintp_ctype():
    val = _getintp_ctype.cache
# WARNING: Decompyle incomplete

_getintp_ctype.cache = None

class _missing_ctypes:
    
    def cast(self, num, obj):
        return num.value

    
    class c_void_p:
        
        def __init__(self, ptr):
            self.value = ptr




class _ctypes:
    
    def __init__(self, array, ptr = (None,)):
        self._arr = array
        if ctypes:
            self._ctypes = ctypes
            self._data = self._ctypes.c_void_p(ptr)
        else:
            self._ctypes = _missing_ctypes()
            self._data = self._ctypes.c_void_p(ptr)
            self._data._objects = array
        if self._arr.ndim == 0:
            self._zerod = True
            return None
        self._zerod = None

    
    def data_as(self, obj):
        '''
        Return the data pointer cast to a particular c-types object.
        For example, calling ``self._as_parameter_`` is equivalent to
        ``self.data_as(ctypes.c_void_p)``. Perhaps you want to use the data as a
        pointer to a ctypes array of floating-point data:
        ``self.data_as(ctypes.POINTER(ctypes.c_double))``.

        The returned pointer will keep a reference to the array.
        '''
        ptr = self._ctypes.cast(self._data, obj)
        ptr._arr = self._arr
        return ptr

    
    def shape_as(self, obj):
        '''
        Return the shape tuple as an array of some other c-types
        type. For example: ``self.shape_as(ctypes.c_short)``.
        '''
        if self._zerod:
            return None
    # WARNING: Decompyle incomplete

    
    def strides_as(self, obj):
        '''
        Return the strides tuple as an array of some other
        c-types type. For example: ``self.strides_as(ctypes.c_longlong)``.
        '''
        if self._zerod:
            return None
    # WARNING: Decompyle incomplete

    data = (lambda self: self._data.value)()
    shape = (lambda self: self.shape_as(_getintp_ctype()))()
    strides = (lambda self: self.strides_as(_getintp_ctype()))()
    _as_parameter_ = (lambda self: self.data_as(ctypes.c_void_p))()
    
    def get_data(self):
        '''Deprecated getter for the `_ctypes.data` property.

        .. deprecated:: 1.21
        '''
        warnings.warn('"get_data" is deprecated. Use "data" instead', DeprecationWarning, stacklevel = 2)
        return self.data

    
    def get_shape(self):
        '''Deprecated getter for the `_ctypes.shape` property.

        .. deprecated:: 1.21
        '''
        warnings.warn('"get_shape" is deprecated. Use "shape" instead', DeprecationWarning, stacklevel = 2)
        return self.shape

    
    def get_strides(self):
        '''Deprecated getter for the `_ctypes.strides` property.

        .. deprecated:: 1.21
        '''
        warnings.warn('"get_strides" is deprecated. Use "strides" instead', DeprecationWarning, stacklevel = 2)
        return self.strides

    
    def get_as_parameter(self):
        '''Deprecated getter for the `_ctypes._as_parameter_` property.

        .. deprecated:: 1.21
        '''
        warnings.warn('"get_as_parameter" is deprecated. Use "_as_parameter_" instead', DeprecationWarning, stacklevel = 2)
        return self._as_parameter_



def _newnames(datatype, order):
    '''
    Given a datatype and an order object, return a new names tuple, with the
    order indicated
    '''
    oldnames = datatype.names
    nameslist = list(oldnames)
    if isinstance(order, str):
        order = [
            order]
    seen = set()
    if isinstance(order, (list, tuple)):
        for name in order:
            nameslist.remove(name)
        except ValueError:
            if name in seen:
                raise ValueError(f'''duplicate field name: {name}'''), None
            raise ValueError(f'''unknown field name: {name}'''), None
        seen.add(name)
        continue
        return tuple(list(order) + nameslist)
    raise ValueError(f'''unsupported order value: {order}''')


def _copy_fields(ary):
    '''Return copy of structured array with padding between fields removed.

    Parameters
    ----------
    ary : ndarray
       Structured array from which to remove padding bytes

    Returns
    -------
    ary_copy : ndarray
       Copy of ary with padding bytes removed
    '''
    pass
# WARNING: Decompyle incomplete


def _promote_fields(dt1, dt2):
    ''' Perform type promotion for two structured dtypes.

    Parameters
    ----------
    dt1 : structured dtype
        First dtype.
    dt2 : structured dtype
        Second dtype.

    Returns
    -------
    out : dtype
        The promoted dtype

    Notes
    -----
    If one of the inputs is aligned, the result will be.  The titles of
    both descriptors must match (point to the same field).
    '''
    pass
# WARNING: Decompyle incomplete


def _getfield_is_safe(oldtype, newtype, offset):
    ''' Checks safety of getfield for object arrays.

    As in _view_is_safe, we need to check that memory containing objects is not
    reinterpreted as a non-object datatype and vice versa.

    Parameters
    ----------
    oldtype : data-type
        Data type of the original ndarray.
    newtype : data-type
        Data type of the field being accessed by ndarray.getfield
    offset : int
        Offset of the field being accessed by ndarray.getfield

    Raises
    ------
    TypeError
        If the field access is invalid

    '''
    pass
# WARNING: Decompyle incomplete


def _view_is_safe(oldtype, newtype):
    ''' Checks safety of a view involving object arrays, for example when
    doing::

        np.zeros(10, dtype=oldtype).view(newtype)

    Parameters
    ----------
    oldtype : data-type
        Data type of original ndarray
    newtype : data-type
        Data type of the view

    Raises
    ------
    TypeError
        If the new type is incompatible with the old type.

    '''
    if oldtype == newtype:
        return None
    if None.hasobject or oldtype.hasobject:
        raise TypeError('Cannot change data-type for object array.')

# WARNING: Decompyle incomplete
