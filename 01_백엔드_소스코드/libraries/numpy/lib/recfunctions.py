# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: recfunctions.pyc (Python 3.11)

'''
Collection of utilities to manipulate structured arrays.

Most of these functions were initially implemented by John Hunter for
matplotlib.  They have been rewritten and extended for convenience.

'''
import itertools
import numpy as np
from numpy.ma import ma
from numpy import ndarray, recarray
from numpy.ma import MaskedArray
from numpy.ma.mrecords import MaskedRecords
from numpy.core.overrides import array_function_dispatch
from numpy.lib._iotools import _is_string_like
_check_fill_value = np.ma.core._check_fill_value
__all__ = [
    'append_fields',
    'apply_along_fields',
    'assign_fields_by_name',
    'drop_fields',
    'find_duplicates',
    'flatten_descr',
    'get_fieldstructure',
    'get_names',
    'get_names_flat',
    'join_by',
    'merge_arrays',
    'rec_append_fields',
    'rec_drop_fields',
    'rec_join',
    'recursive_fill_fields',
    'rename_fields',
    'repack_fields',
    'require_fields',
    'stack_arrays',
    'structured_to_unstructured',
    'unstructured_to_structured']

def _recursive_fill_fields_dispatcher(input, output):
    return (input, output)

recursive_fill_fields = (lambda input, output: newdtype = output.dtypefor field in newdtype.names:
current = input[field]except ValueError:
continue# WARNING: Decompyle incomplete
)()

def _get_fieldspec(dtype):
    """
    Produce a list of name/dtype pairs corresponding to the dtype fields

    Similar to dtype.descr, but the second item of each tuple is a dtype, not a
    string. As a result, this handles subarray dtypes

    Can be passed to the dtype constructor to reconstruct the dtype, noting that
    this (deliberately) discards field offsets.

    Examples
    --------
    >>> dt = np.dtype([(('a', 'A'), np.int64), ('b', np.double, 3)])
    >>> dt.descr
    [(('a', 'A'), '<i8'), ('b', '<f8', (3,))]
    >>> _get_fieldspec(dt)
    [(('a', 'A'), dtype('int64')), ('b', dtype(('<f8', (3,))))]

    """
    pass
# WARNING: Decompyle incomplete


def get_names(adtype):
    """
    Returns the field names of the input datatype as a tuple. Input datatype
    must have fields otherwise error is raised.

    Parameters
    ----------
    adtype : dtype
        Input datatype

    Examples
    --------
    >>> from numpy.lib import recfunctions as rfn
    >>> rfn.get_names(np.empty((1,), dtype=[('A', int)]).dtype)
    ('A',)
    >>> rfn.get_names(np.empty((1,), dtype=[('A',int), ('B', float)]).dtype)
    ('A', 'B')
    >>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
    >>> rfn.get_names(adtype)
    ('a', ('b', ('ba', 'bb')))
    """
    listnames = []
    names = adtype.names
# WARNING: Decompyle incomplete


def get_names_flat(adtype):
    """
    Returns the field names of the input datatype as a tuple. Input datatype
    must have fields otherwise error is raised.
    Nested structure are flattened beforehand.

    Parameters
    ----------
    adtype : dtype
        Input datatype

    Examples
    --------
    >>> from numpy.lib import recfunctions as rfn
    >>> rfn.get_names_flat(np.empty((1,), dtype=[('A', int)]).dtype) is None
    False
    >>> rfn.get_names_flat(np.empty((1,), dtype=[('A',int), ('B', str)]).dtype)
    ('A', 'B')
    >>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
    >>> rfn.get_names_flat(adtype)
    ('a', 'b', 'ba', 'bb')
    """
    listnames = []
    names = adtype.names
# WARNING: Decompyle incomplete


def flatten_descr(ndtype):
    """
    Flatten a structured data-type description.

    Examples
    --------
    >>> from numpy.lib import recfunctions as rfn
    >>> ndtype = np.dtype([('a', '<i4'), ('b', [('ba', '<f8'), ('bb', '<i4')])])
    >>> rfn.flatten_descr(ndtype)
    (('a', dtype('int32')), ('ba', dtype('float64')), ('bb', dtype('int32')))

    """
    names = ndtype.names
# WARNING: Decompyle incomplete


def _zip_dtype(seqarrays, flatten = (False,)):
    newdtype = []
    if flatten:
        for a in seqarrays:
            newdtype.extend(flatten_descr(a.dtype))
# WARNING: Decompyle incomplete


def _zip_descr(seqarrays, flatten = (False,)):
    '''
    Combine the dtype description of a series of arrays.

    Parameters
    ----------
    seqarrays : sequence of arrays
        Sequence of arrays
    flatten : {boolean}, optional
        Whether to collapse nested descriptions.
    '''
    return _zip_dtype(seqarrays, flatten = flatten).descr


def get_fieldstructure(adtype, lastname, parents = (None, None)):
    """
    Returns a dictionary with fields indexing lists of their parent fields.

    This function is used to simplify access to fields nested in other fields.

    Parameters
    ----------
    adtype : np.dtype
        Input datatype
    lastname : optional
        Last processed field name (used internally during recursion).
    parents : dictionary
        Dictionary of parent fields (used interbally during recursion).

    Examples
    --------
    >>> from numpy.lib import recfunctions as rfn
    >>> ndtype =  np.dtype([('A', int),
    ...                     ('B', [('BA', int),
    ...                            ('BB', [('BBA', int), ('BBB', int)])])])
    >>> rfn.get_fieldstructure(ndtype)
    ... # XXX: possible regression, order of BBA and BBB is swapped
    {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B'], 'BBA': ['B', 'BB'], 'BBB': ['B', 'BB']}

    """
    pass
# WARNING: Decompyle incomplete


def _izip_fields_flat(iterable):
    '''
    Returns an iterator of concatenated fields from a sequence of arrays,
    collapsing any nested structure.

    '''
    pass
# WARNING: Decompyle incomplete


def _izip_fields(iterable):
    '''
    Returns an iterator of concatenated fields from a sequence of arrays.

    '''
    pass
# WARNING: Decompyle incomplete


def _izip_records(seqarrays, fill_value, flatten = (None, True)):
    '''
    Returns an iterator of concatenated items from a sequence of arrays.

    Parameters
    ----------
    seqarrays : sequence of arrays
        Sequence of arrays.
    fill_value : {None, integer}
        Value used to pad shorter iterables.
    flatten : {True, False},
        Whether to
    '''
    pass
# WARNING: Decompyle incomplete


def _fix_output(output, usemask, asrecarray = (True, False)):
    '''
    Private function: return a recarray, a ndarray, a MaskedArray
    or a MaskedRecords depending on the input parameters
    '''
    if not isinstance(output, MaskedArray):
        usemask = False
    if usemask:
        if asrecarray:
            output = output.view(MaskedRecords)
        else:
            output = ma.filled(output)
            if asrecarray:
                output = output.view(recarray)
    return output


def _fix_defaults(output, defaults = (None,)):
    '''
    Update the fill_value and masked data of `output`
    from the default given in a dictionary defaults.
    '''
    names = output.dtype.names
    fill_value = output.fill_value
    mask = output.mask
    data = output.data
    if not defaults:
        for k, v in { }.items():
            if k in names:
                fill_value[k] = v
                data[k][mask[k]] = v
            return output


def _merge_arrays_dispatcher(seqarrays, fill_value, flatten, usemask, asrecarray = (None, None, None, None)):
    return seqarrays

merge_arrays = (lambda seqarrays, fill_value, flatten, usemask, asrecarray = (-1, False, False, False): if len(seqarrays) == 1:
seqarrays = np.asanyarray(seqarrays[0])# WARNING: Decompyle incomplete
)()

def _drop_fields_dispatcher(base, drop_names, usemask, asrecarray = (None, None)):
    return (base,)

drop_fields = (lambda base, drop_names, usemask, asrecarray = (True, False): pass# WARNING: Decompyle incomplete
)()

def _keep_fields(base, keep_names, usemask, asrecarray = (True, False)):
    '''
    Return a new array keeping only the fields in `keep_names`,
    and preserving the order of those fields.

    Parameters
    ----------
    base : array
        Input array
    keep_names : string or sequence
        String or sequence of strings corresponding to the names of the
        fields to keep. Order of the names will be preserved.
    usemask : {False, True}, optional
        Whether to return a masked array or not.
    asrecarray : string or sequence, optional
        Whether to return a recarray or a mrecarray (`asrecarray=True`) or
        a plain ndarray or masked array with flexible dtype. The default
        is False.
    '''
    pass
# WARNING: Decompyle incomplete


def _rec_drop_fields_dispatcher(base, drop_names):
    return (base,)

rec_drop_fields = (lambda base, drop_names: drop_fields(base, drop_names, usemask = False, asrecarray = True))()

def _rename_fields_dispatcher(base, namemapper):
    return (base,)

rename_fields = (lambda base, namemapper: pass# WARNING: Decompyle incomplete
)()

def _append_fields_dispatcher(base, names, data, dtypes, fill_value, usemask, asrecarray = (None, None, None, None)):
    pass
# WARNING: Decompyle incomplete

append_fields = (lambda base, names, data, dtypes, fill_value, usemask, asrecarray = (None, -1, True, False): if isinstance(names, (tuple, list)):
if len(names) != len(data):
msg = 'The number of arrays does not match the number of names'raise ValueError(msg)elif isinstance(names, str):
names = [
names]data = [
data]# WARNING: Decompyle incomplete
)()

def _rec_append_fields_dispatcher(base, names, data, dtypes = (None,)):
    pass
# WARNING: Decompyle incomplete

rec_append_fields = (lambda base, names, data, dtypes = (None,): append_fields(base, names, data = data, dtypes = dtypes, asrecarray = True, usemask = False))()

def _repack_fields_dispatcher(a, align, recurse = (None, None)):
    return (a,)

repack_fields = (lambda a, align, recurse = (False, False): if not isinstance(a, np.dtype):
dt = repack_fields(a.dtype, align = align, recurse = recurse)a.astype(dt, copy = False)# WARNING: Decompyle incomplete
)()

def _get_fields_and_offsets(dt, offset = (0,)):
    '''
    Returns a flat list of (dtype, count, offset) tuples of all the
    scalar fields in the dtype "dt", including nested fields, in left
    to right order.
    '''
    pass
# WARNING: Decompyle incomplete


def _common_stride(offsets, counts, itemsize):
    '''
    Returns the stride between the fields, or None if the stride is not
    constant. The values in "counts" designate the lengths of
    subarrays. Subarrays are treated as many contiguous fields, with
    always positive stride.
    '''
    if len(offsets) <= 1:
        return itemsize
    negative = None[1] < offsets[0]
    if negative:
        it = zip(reversed(offsets), reversed(counts))
    else:
        it = zip(offsets, counts)
    prev_offset = None
    stride = None
# WARNING: Decompyle incomplete


def _structured_to_unstructured_dispatcher(arr, dtype, copy, casting = (None, None, None)):
    return (arr,)

structured_to_unstructured = (lambda arr, dtype, copy, casting = (None, False, 'unsafe'): pass# WARNING: Decompyle incomplete
)()

def _unstructured_to_structured_dispatcher(arr, dtype, names, align, copy, casting = (None, None, None, None, None)):
    return (arr,)

unstructured_to_structured = (lambda arr, dtype, names, align, copy, casting = (None, None, False, False, 'unsafe'): pass# WARNING: Decompyle incomplete
)()

def _apply_along_fields_dispatcher(func, arr):
    return (arr,)

apply_along_fields = (lambda func, arr: pass# WARNING: Decompyle incomplete
)()

def _assign_fields_by_name_dispatcher(dst, src, zero_unassigned = (None,)):
    return (dst, src)

assign_fields_by_name = (lambda dst, src, zero_unassigned = (True,): pass# WARNING: Decompyle incomplete
)()

def _require_fields_dispatcher(array, required_dtype):
    return (array,)

require_fields = (lambda array, required_dtype: out = np.empty(array.shape, dtype = required_dtype)assign_fields_by_name(out, array)out)()

def _stack_arrays_dispatcher(arrays, defaults, usemask, asrecarray, autoconvert = (None, None, None, None)):
    return arrays

stack_arrays = (lambda arrays, defaults, usemask, asrecarray, autoconvert = (None, True, False, False):
