# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: defchararray.pyc (Python 3.11)

'''
This module contains a set of functions for vectorized string
operations and methods.

.. note::
   The `chararray` class exists for backwards compatibility with
   Numarray, it is not recommended for new development. Starting from numpy
   1.4, if one needs arrays of strings, it is recommended to use arrays of
   `dtype` `object_`, `bytes_` or `str_`, and use the free functions
   in the `numpy.char` module for fast vectorized string operations.

Some methods will only be available if the corresponding string method is
available in your version of Python.

The preferred alias for `defchararray` is `numpy.char`.

'''
import functools
from _utils import set_module
from numerictypes import bytes_, str_, integer, int_, object_, bool_, character
from numeric import ndarray, compare_chararrays
from numeric import array as narray
from numpy.core.multiarray import _vec_string
from numpy.core import overrides
from numpy.compat import asbytes
import numpy
__all__ = [
    'equal',
    'not_equal',
    'greater_equal',
    'less_equal',
    'greater',
    'less',
    'str_len',
    'add',
    'multiply',
    'mod',
    'capitalize',
    'center',
    'count',
    'decode',
    'encode',
    'endswith',
    'expandtabs',
    'find',
    'index',
    'isalnum',
    'isalpha',
    'isdigit',
    'islower',
    'isspace',
    'istitle',
    'isupper',
    'join',
    'ljust',
    'lower',
    'lstrip',
    'partition',
    'replace',
    'rfind',
    'rindex',
    'rjust',
    'rpartition',
    'rsplit',
    'rstrip',
    'split',
    'splitlines',
    'startswith',
    'strip',
    'swapcase',
    'title',
    'translate',
    'upper',
    'zfill',
    'isnumeric',
    'isdecimal',
    'array',
    'asarray']
_globalvar = 0
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy.char')

def _is_unicode(arr):
    '''Returns True if arr is a string or a string array with a dtype that
    represents a unicode string, otherwise returns False.

    '''
    if isinstance(arr, str) or issubclass(numpy.asarray(arr).dtype.type, str):
        return True


def _to_bytes_or_str_array(result, output_dtype_like = (None,)):
    '''
    Helper function to cast a result back into an array
    with the appropriate dtype if an object array must be used
    as an intermediary.
    '''
    ret = numpy.asarray(result.tolist())
    dtype = getattr(output_dtype_like, 'dtype', None)
# WARNING: Decompyle incomplete


def _clean_args(*args):
    """
    Helper function for delegating arguments to Python string
    functions.

    Many of the Python string operations that have optional arguments
    do not use 'None' to indicate a default value.  In these cases,
    we need to remove all None arguments, and those following them.
    """
    newargs = []
# WARNING: Decompyle incomplete


def _get_num_chars(a):
    '''
    Helper function that returns the number of characters per field in
    a string or unicode array.  This is to abstract out the fact that
    for a unicode array this is itemsize / 4.
    '''
    if issubclass(a.dtype.type, str_):
        return a.itemsize // 4
    return None.itemsize


def _binary_op_dispatcher(x1, x2):
    return (x1, x2)

equal = (lambda x1, x2: compare_chararrays(x1, x2, '==', True))()
not_equal = (lambda x1, x2: compare_chararrays(x1, x2, '!=', True))()
greater_equal = (lambda x1, x2: compare_chararrays(x1, x2, '>=', True))()
less_equal = (lambda x1, x2: compare_chararrays(x1, x2, '<=', True))()
greater = (lambda x1, x2: compare_chararrays(x1, x2, '>', True))()
less = (lambda x1, x2: compare_chararrays(x1, x2, '<', True))()

def _unary_op_dispatcher(a):
    return (a,)

str_len = (lambda a: _vec_string(a, int_, '__len__'))()
add = (lambda x1, x2: arr1 = numpy.asarray(x1)arr2 = numpy.asarray(x2)out_size = _get_num_chars(arr1) + _get_num_chars(arr2)if type(arr1.dtype) != type(arr2.dtype):
raise TypeError(f'''np.char.add() requires both arrays of the same dtype kind, but got dtypes: \'{arr1.dtype}\' and \'{arr2.dtype}\' (the few cases where this used to work often lead to incorrect results).''')_vec_string(arr1, type(arr1.dtype)(out_size), '__add__', (arr2,)))()

def _multiply_dispatcher(a, i):
    return (a,)

multiply = (lambda a, i: a_arr = numpy.asarray(a)i_arr = numpy.asarray(i)if not issubclass(i_arr.dtype.type, integer):
raise ValueError('Can only multiply by integers')out_size = _get_num_chars(a_arr) * max(int(i_arr.max()), 0)_vec_string(a_arr, type(a_arr.dtype)(out_size), '__mul__', (i_arr,)))()

def _mod_dispatcher(a, values):
    return (a, values)

mod = (lambda a, values: _to_bytes_or_str_array(_vec_string(a, object_, '__mod__', (values,)), a))()
capitalize = (lambda a: a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'capitalize'))()

def _center_dispatcher(a, width, fillchar = (None,)):
    return (a,)

center = (lambda a, width, fillchar = (' ',): a_arr = numpy.asarray(a)width_arr = numpy.asarray(width)size = int(numpy.max(width_arr.flat))if numpy.issubdtype(a_arr.dtype, numpy.bytes_):
fillchar = asbytes(fillchar)_vec_string(a_arr, type(a_arr.dtype)(size), 'center', (width_arr, fillchar)))()

def _count_dispatcher(a, sub, start, end = (None, None)):
    return (a,)

count = (lambda a, sub, start, end = (0, None): _vec_string(a, int_, 'count', [
sub,
start] + _clean_args(end)))()

def _code_dispatcher(a, encoding, errors = (None, None)):
    return (a,)

decode = (lambda a, encoding, errors = (None, None): _to_bytes_or_str_array(_vec_string(a, object_, 'decode', _clean_args(encoding, errors))))()
encode = (lambda a, encoding, errors = (None, None): _to_bytes_or_str_array(_vec_string(a, object_, 'encode', _clean_args(encoding, errors))))()

def _endswith_dispatcher(a, suffix, start, end = (None, None)):
    return (a,)

endswith = (lambda a, suffix, start, end = (0, None): _vec_string(a, bool_, 'endswith', [
suffix,
start] + _clean_args(end)))()

def _expandtabs_dispatcher(a, tabsize = (None,)):
    return (a,)

expandtabs = (lambda a, tabsize = (8,): _to_bytes_or_str_array(_vec_string(a, object_, 'expandtabs', (tabsize,)), a))()
find = (lambda a, sub, start, end = (0, None): _vec_string(a, int_, 'find', [
sub,
start] + _clean_args(end)))()
index = (lambda a, sub, start, end = (0, None): _vec_string(a, int_, 'index', [
sub,
start] + _clean_args(end)))()
isalnum = (lambda a: _vec_string(a, bool_, 'isalnum'))()
isalpha = (lambda a: _vec_string(a, bool_, 'isalpha'))()
isdigit = (lambda a: _vec_string(a, bool_, 'isdigit'))()
islower = (lambda a: _vec_string(a, bool_, 'islower'))()
isspace = (lambda a: _vec_string(a, bool_, 'isspace'))()
istitle = (lambda a: _vec_string(a, bool_, 'istitle'))()
isupper = (lambda a: _vec_string(a, bool_, 'isupper'))()

def _join_dispatcher(sep, seq):
    return (sep, seq)

join = (lambda sep, seq: _to_bytes_or_str_array(_vec_string(sep, object_, 'join', (seq,)), seq))()

def _just_dispatcher(a, width, fillchar = (None,)):
    return (a,)

ljust = (lambda a, width, fillchar = (' ',): a_arr = numpy.asarray(a)width_arr = numpy.asarray(width)size = int(numpy.max(width_arr.flat))if numpy.issubdtype(a_arr.dtype, numpy.bytes_):
fillchar = asbytes(fillchar)_vec_string(a_arr, type(a_arr.dtype)(size), 'ljust', (width_arr, fillchar)))()
lower = (lambda a: a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'lower'))()

def _strip_dispatcher(a, chars = (None,)):
    return (a,)

lstrip = (lambda a, chars = (None,): a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'lstrip', (chars,)))()

def _partition_dispatcher(a, sep):
    return (a,)

partition = (lambda a, sep: _to_bytes_or_str_array(_vec_string(a, object_, 'partition', (sep,)), a))()

def _replace_dispatcher(a, old, new, count = (None,)):
    return (a,)

replace = (lambda a, old, new, count = (None,): _to_bytes_or_str_array(_vec_string(a, object_, 'replace', [
old,
new] + _clean_args(count)), a))()
rfind = (lambda a, sub, start, end = (0, None): _vec_string(a, int_, 'rfind', [
sub,
start] + _clean_args(end)))()
rindex = (lambda a, sub, start, end = (0, None): _vec_string(a, int_, 'rindex', [
sub,
start] + _clean_args(end)))()
rjust = (lambda a, width, fillchar = (' ',): a_arr = numpy.asarray(a)width_arr = numpy.asarray(width)size = int(numpy.max(width_arr.flat))if numpy.issubdtype(a_arr.dtype, numpy.bytes_):
fillchar = asbytes(fillchar)_vec_string(a_arr, type(a_arr.dtype)(size), 'rjust', (width_arr, fillchar)))()
rpartition = (lambda a, sep: _to_bytes_or_str_array(_vec_string(a, object_, 'rpartition', (sep,)), a))()

def _split_dispatcher(a, sep, maxsplit = (None, None)):
    return (a,)

rsplit = (lambda a, sep, maxsplit = (None, None): _vec_string(a, object_, 'rsplit', [
sep] + _clean_args(maxsplit)))()

def _strip_dispatcher(a, chars = (None,)):
    return (a,)

rstrip = (lambda a, chars = (None,): a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'rstrip', (chars,)))()
split = (lambda a, sep, maxsplit = (None, None): _vec_string(a, object_, 'split', [
sep] + _clean_args(maxsplit)))()

def _splitlines_dispatcher(a, keepends = (None,)):
    return (a,)

splitlines = (lambda a, keepends = (None,): _vec_string(a, object_, 'splitlines', _clean_args(keepends)))()

def _startswith_dispatcher(a, prefix, start, end = (None, None)):
    return (a,)

startswith = (lambda a, prefix, start, end = (0, None): _vec_string(a, bool_, 'startswith', [
prefix,
start] + _clean_args(end)))()
strip = (lambda a, chars = (None,): a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'strip', _clean_args(chars)))()
swapcase = (lambda a: a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'swapcase'))()
title = (lambda a: a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'title'))()

def _translate_dispatcher(a, table, deletechars = (None,)):
    return (a,)

translate = (lambda a, table, deletechars = (None,): a_arr = numpy.asarray(a)if issubclass(a_arr.dtype.type, str_):
_vec_string(a_arr, a_arr.dtype, 'translate', (table,))None(a_arr, a_arr.dtype, 'translate', [
table] + _clean_args(deletechars)))()
upper = (lambda a: a_arr = numpy.asarray(a)_vec_string(a_arr, a_arr.dtype, 'upper'))()

def _zfill_dispatcher(a, width):
    return (a,)

zfill = (lambda a, width: a_arr = numpy.asarray(a)width_arr = numpy.asarray(width)size = int(numpy.max(width_arr.flat))_vec_string(a_arr, type(a_arr.dtype)(size), 'zfill', (width_arr,)))()
isnumeric = (lambda a: if not _is_unicode(a):
raise TypeError('isnumeric is only available for Unicode strings and arrays')_vec_string(a, bool_, 'isnumeric'))()
isdecimal = (lambda a: if not _is_unicode(a):
raise TypeError('isdecimal is only available for Unicode strings and arrays')_vec_string(a, bool_, 'isdecimal'))()
chararray = <NODE:12>()
array = (lambda obj, itemsize, copy, unicode, order = (None, True, None, None): pass# WARNING: Decompyle incomplete
)()
asarray = (lambda obj, itemsize, unicode, order = (None, None, None): array(obj, itemsize, copy = False, unicode = unicode, order = order))()
