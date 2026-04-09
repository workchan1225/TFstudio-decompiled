# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: records.pyc (Python 3.11)

"""
Record Arrays
=============
Record arrays expose the fields of structured arrays as properties.

Most commonly, ndarrays contain elements of a single type, e.g. floats,
integers, bools etc.  However, it is possible for elements to be combinations
of these using structured types, such as::

  >>> a = np.array([(1, 2.0), (1, 2.0)], dtype=[('x', np.int64), ('y', np.float64)])
  >>> a
  array([(1, 2.), (1, 2.)], dtype=[('x', '<i8'), ('y', '<f8')])

Here, each element consists of two fields: x (and int), and y (a float).
This is known as a structured array.  The different fields are analogous
to columns in a spread-sheet.  The different fields can be accessed as
one would a dictionary::

  >>> a['x']
  array([1, 1])

  >>> a['y']
  array([2., 2.])

Record arrays allow us to access fields as properties::

  >>> ar = np.rec.array(a)

  >>> ar.x
  array([1, 1])

  >>> ar.y
  array([2., 2.])

"""
import warnings
from collections import Counter
from contextlib import nullcontext
from _utils import set_module
from  import numeric as sb
from  import numerictypes as nt
from numpy.compat import os_fspath
from arrayprint import _get_legacy_print_mode
__all__ = [
    'record',
    'recarray',
    'format_parser',
    'fromarrays',
    'fromrecords',
    'fromstring',
    'fromfile',
    'array']
ndarray = sb.ndarray
_byteorderconv = {
    'b': '>',
    'l': '<',
    'n': '=',
    'B': '>',
    'L': '<',
    'N': '=',
    'S': 's',
    's': 's',
    '>': '>',
    '<': '<',
    '=': '=',
    '|': '|',
    'I': '|',
    'i': '|' }
numfmt = nt.sctypeDict

def find_duplicate(list):
    '''Find duplication in a list, return a list of duplicated elements'''
    return Counter(list).items()()

format_parser = <NODE:12>()

class record(nt.void):
    pass
# WARNING: Decompyle incomplete


class recarray(ndarray):
    pass
# WARNING: Decompyle incomplete


def _deprecate_shape_0_as_None(shape):
    if shape == 0:
        warnings.warn('Passing `shape=0` to have the shape be inferred is deprecated, and in future will be equivalent to `shape=(0,)`. To infer the shape and suppress this warning, pass `shape=None` instead.', FutureWarning, stacklevel = 3)
        return None

fromarrays = (lambda arrayList, dtype, shape, formats, names, titles, aligned, byteorder = (None, None, None, None, None, False, None): arrayList = arrayList()shape = _deprecate_shape_0_as_None(shape)# WARNING: Decompyle incomplete
)()
fromrecords = (lambda recList, dtype, shape, formats, names, titles, aligned, byteorder = (None, None, None, None, None, False, None): pass# WARNING: Decompyle incomplete
)()
fromstring = (lambda datastring, dtype, shape, offset, formats, names, titles, aligned, byteorder = (None, None, 0, None, None, None, False, None): pass# WARNING: Decompyle incomplete
)()

def get_remaining_size(fd):
    pos = fd.tell()
    
    try:
        fd.seek(0, 2)
        fd.seek(pos, 0)
        return fd.tell() - pos
    except:
        fd.seek(pos, 0)


fromfile = (lambda fd, dtype, shape, offset, formats, names, titles, aligned, byteorder = (None, None, 0, None, None, None, False, None): pass# WARNING: Decompyle incomplete
)()
array = (lambda obj, dtype, shape, offset, strides, formats, names, titles, aligned, byteorder, copy = (None, None, 0, None, None, None, None, False, None, True): pass# WARNING: Decompyle incomplete
)()
