# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_support.pyc (Python 3.11)

import collections
import ctypes
import re
import numpy as np
from numba.core import errors, types, config
from numba.core.typing.templates import signature
from numba.np import npdatetime_helpers
from numba.core.errors import TypingError
from numba.core.cgutils import is_nonelike
numpy_version = tuple(map(int, np.__version__.split('.')[:2]))
if config.USE_LEGACY_TYPE_SYSTEM:
    FROM_DTYPE = {
        np.dtype(object): types.pyobject,
        np.dtype('complex128'): types.complex128,
        np.dtype('complex64'): types.complex64,
        np.dtype('float16'): types.float16,
        np.dtype('float64'): types.float64,
        np.dtype('float32'): types.float32,
        np.dtype('uint64'): types.uint64,
        np.dtype('uint32'): types.uint32,
        np.dtype('uint16'): types.uint16,
        np.dtype('uint8'): types.uint8,
        np.dtype('int64'): types.int64,
        np.dtype('int32'): types.int32,
        np.dtype('int16'): types.int16,
        np.dtype('int8'): types.int8,
        np.dtype('bool'): types.boolean }
else:
    FROM_DTYPE = {
        np.dtype(object): types.pyobject,
        np.dtype('complex128'): types.np_complex128,
        np.dtype('complex64'): types.np_complex64,
        np.dtype('float16'): types.np_float16,
        np.dtype('float64'): types.np_float64,
        np.dtype('float32'): types.np_float32,
        np.dtype('uint64'): types.np_uint64,
        np.dtype('uint32'): types.np_uint32,
        np.dtype('uint16'): types.np_uint16,
        np.dtype('uint8'): types.np_uint8,
        np.dtype('int64'): types.np_int64,
        np.dtype('int32'): types.np_int32,
        np.dtype('int16'): types.np_int16,
        np.dtype('int8'): types.np_int8,
        np.dtype('bool'): types.np_bool_ }
re_typestr = re.compile('[<>=\\|]([a-z])(\\d+)?$', re.I)
re_datetimestr = re.compile('[<>=\\|]([mM])8?(\\[([a-z]+)\\])?$', re.I)
sizeof_unicode_char = np.dtype('U1').itemsize

def _from_str_dtype(dtype):
    m = re_typestr.match(dtype.str)
    if not m:
        raise errors.NumbaNotImplementedError(dtype)
    groups = m.groups()
    typecode = groups[0]
# WARNING: Decompyle incomplete


def _from_datetime_dtype(dtype):
    m = re_datetimestr.match(dtype.str)
    if not m:
        raise errors.NumbaNotImplementedError(dtype)
    groups = m.groups()
    typecode = groups[0]
    if not groups[2]:
        unit = ''
        if typecode == 'm':
            return types.NPTimedelta(unit)
        if None == 'M':
            return types.NPDatetime(unit)
        raise None.NumbaNotImplementedError(dtype)


def from_dtype(dtype):
    '''
    Return a Numba Type instance corresponding to the given Numpy *dtype*.
    NumbaNotImplementedError is raised on unsupported Numpy dtypes.
    '''
    if type(dtype) is type and issubclass(dtype, np.generic):
        dtype = np.dtype(dtype)
# WARNING: Decompyle incomplete

_as_dtype_letters = {
    types.UnicodeCharSeq: 'U',
    types.CharSeq: 'S',
    types.NPTimedelta: 'm8',
    types.NPDatetime: 'M8' }

def as_dtype(nbtype):
    '''
    Return a numpy dtype instance corresponding to the given Numba type.
    NumbaNotImplementedError is if no correspondence is known.
    '''
    nbtype = types.unliteral(nbtype)
    if isinstance(nbtype, (types.Complex, types.Integer, types.Float)):
        return np.dtype(str(nbtype))
    if None(nbtype, types.Boolean):
        return np.dtype('?')
    if None(nbtype, (types.NPDatetime, types.NPTimedelta)):
        letter = _as_dtype_letters[type(nbtype)]
        if nbtype.unit:
            return np.dtype(f'''{letter!s}[{nbtype.unit!s}]''')
        return None.dtype(letter)
    if None(nbtype, (types.CharSeq, types.UnicodeCharSeq)):
        letter = _as_dtype_letters[type(nbtype)]
        return np.dtype('%s%d' % (letter, nbtype.count))
    if None(nbtype, types.Record):
        return as_struct_dtype(nbtype)
    if None(nbtype, types.EnumMember):
        return as_dtype(nbtype.dtype)
    if None(nbtype, types.npytypes.DType):
        return as_dtype(nbtype.dtype)
    if None(nbtype, types.NumberClass):
        return as_dtype(nbtype.dtype)
    if None(nbtype, types.NestedArray):
        spec = (as_dtype(nbtype.dtype), tuple(nbtype.shape))
        return np.dtype(spec)
    if None(nbtype, types.PyObject):
        return np.dtype(object)
    msg = f'''{None} cannot be represented as a NumPy dtype'''
    raise errors.NumbaNotImplementedError(msg)


def as_struct_dtype(rec):
    '''Convert Numba Record type to NumPy structured dtype
    '''
    pass
# WARNING: Decompyle incomplete


def _check_struct_alignment(rec, fields):
    '''Check alignment compatibility with Numpy'''
    pass
# WARNING: Decompyle incomplete


def map_arrayscalar_type(val):
    if isinstance(val, np.generic):
        dtype = val.dtype
    else:
        
        try:
            dtype = np.dtype(type(val))
        except TypeError:
            raise errors.NumbaNotImplementedError('no corresponding numpy dtype for %r' % type(val))

        return from_dtype(dtype)


def is_array(val):
    return isinstance(val, np.ndarray)


def map_layout(val):
    if val.flags['C_CONTIGUOUS']:
        layout = 'C'
    elif val.flags['F_CONTIGUOUS']:
        layout = 'F'
    else:
        layout = 'A'
    return layout


def select_array_wrapper(inputs):
    """
    Given the array-compatible input types to an operation (e.g. ufunc),
    select the appropriate input for wrapping the operation output,
    according to each input's __array_priority__.

    An index into *inputs* is returned.
    """
    max_prio = float('-inf')
    selected_index = None
# WARNING: Decompyle incomplete


def resolve_output_type(context, inputs, formal_output):
    """
    Given the array-compatible input types to an operation (e.g. ufunc),
    and the operation's formal output type (a types.Array instance),
    resolve the actual output type using the typing *context*.

    This uses a mechanism compatible with Numpy's __array_priority__ /
    __array_wrap__.
    """
    selected_input = inputs[select_array_wrapper(inputs)]
    args = (selected_input, formal_output)
    sig = context.resolve_function_type('__array_wrap__', args, { })
# WARNING: Decompyle incomplete


def supported_ufunc_loop(ufunc, loop):
    """Return whether the *loop* for the *ufunc* is supported -in nopython-.

    *loop* should be a UFuncLoopSpec instance, and *ufunc* a numpy ufunc.

    For ufuncs implemented using the ufunc_db, it is supported if the ufunc_db
    contains a lowering definition for 'loop' in the 'ufunc' entry.

    For other ufuncs, it is type based. The loop will be considered valid if it
    only contains the following letter types: '?bBhHiIlLqQfd'. Note this is
    legacy and when implementing new ufuncs the ufunc_db should be preferred,
    as it allows for a more fine-grained incremental support.
    """
    pass
# WARNING: Decompyle incomplete


def UFuncLoopSpec():
    '''UFuncLoopSpec'''
    __doc__ = '\n    An object describing a ufunc loop\'s inner types.  Properties:\n    - inputs: the inputs\' Numba types\n    - outputs: the outputs\' Numba types\n    - ufunc_sig: the string representing the ufunc\'s type signature, in\n      Numpy format (e.g. "ii->i")\n    '
    __slots__ = ()
    numpy_inputs = (lambda self: self.inputs())()
    numpy_outputs = (lambda self: self.outputs())()

UFuncLoopSpec = <NODE:27>(UFuncLoopSpec, 'UFuncLoopSpec', collections.namedtuple('_UFuncLoopSpec', ('inputs', 'outputs', 'ufunc_sig')))

def _ufunc_loop_sig(out_tys, in_tys):
    pass
# WARNING: Decompyle incomplete


def ufunc_can_cast(from_, to, has_mixed_inputs, casting = ('safe',)):
    '''
    A variant of np.can_cast() that can allow casting any integer to
    any real or complex type, in case the operation has mixed-kind
    inputs.

    For example we want `np.power(float32, int32)` to be computed using
    SP arithmetic and return `float32`.
    However, `np.sqrt(int32)` should use DP arithmetic and return `float64`.
    '''
    from_ = np.dtype(from_)
    to = np.dtype(to)
    if has_mixed_inputs and from_.kind in 'iu' and to.kind in 'cf':
        return True
    return None.can_cast(from_, to, casting)


def ufunc_find_matching_loop(ufunc, arg_types):
    '''Find the appropriate loop to be used for a ufunc based on the types
    of the operands

    ufunc        - The ufunc we want to check
    arg_types    - The tuple of arguments to the ufunc, including any
                   explicit output(s).
    return value - A UFuncLoopSpec identifying the loop, or None
                   if no matching loop is found.
    '''
    input_types = arg_types[:ufunc.nin]
    output_types = arg_types[ufunc.nin:]
# WARNING: Decompyle incomplete


def _is_aligned_struct(struct):
    return struct.isalignedstruct


def from_struct_dtype(dtype):
    '''Convert a NumPy structured dtype to Numba Record type
    '''
    if dtype.hasobject:
        msg = 'dtypes that contain object are not supported.'
        raise errors.NumbaNotImplementedError(msg)
    fields = []
    for name, info in dtype.fields.items():
        (elemdtype, offset) = info[:2]
        title = info[2] if len(info) == 3 else None
        ty = from_dtype(elemdtype)
        infos = {
            'type': ty,
            'offset': offset,
            'title': title }
        fields.append((name, infos))
        size = dtype.itemsize
        aligned = _is_aligned_struct(dtype)
        return types.Record(fields, size, aligned)


def _get_bytes_buffer(ptr, nbytes):
    '''
    Get a ctypes array of *nbytes* starting at *ptr*.
    '''
    if isinstance(ptr, ctypes.c_void_p):
        ptr = ptr.value
    arrty = ctypes.c_byte * nbytes
    return arrty.from_address(ptr)


def _get_array_from_ptr(ptr, nbytes, dtype):
    return np.frombuffer(_get_bytes_buffer(ptr, nbytes), dtype)


def carray(ptr, shape, dtype = (None,)):
    """
    Return a Numpy array view over the data pointed to by *ptr* with the
    given *shape*, in C order.  If *dtype* is given, it is used as the
    array's dtype, otherwise the array's dtype is inferred from *ptr*'s type.
    """
    from_ctypes = from_ctypes
    import numba.core.typing.ctypes_utils
    
    try:
        ptr = ptr._as_parameter_
    except AttributeError:
        pass

# WARNING: Decompyle incomplete


def farray(ptr, shape, dtype = (None,)):
    """
    Return a Numpy array view over the data pointed to by *ptr* with the
    given *shape*, in Fortran order.  If *dtype* is given, it is used as the
    array's dtype, otherwise the array's dtype is inferred from *ptr*'s type.
    """
    if not isinstance(shape, int):
        shape = shape[::-1]
    return carray(ptr, shape, dtype).T


def is_contiguous(dims, strides, itemsize):
    '''Is the given shape, strides, and itemsize of C layout?

    Note: The code is usable as a numba-compiled function
    '''
    nd = len(dims)
    innerax = nd - 1
# WARNING: Decompyle incomplete


def is_fortran(dims, strides, itemsize):
    '''Is the given shape, strides, and itemsize of F layout?

    Note: The code is usable as a numba-compiled function
    '''
    nd = len(dims)
    firstax = 0
# WARNING: Decompyle incomplete


def type_can_asarray(arr):
    """ Returns True if the type of 'arr' is supported by the Numba `np.asarray`
    implementation, False otherwise.
    """
    ok = (types.Array, types.Sequence, types.Tuple, types.StringLiteral, types.Number, types.Boolean, types.containers.ListType)
    return isinstance(arr, ok)


def type_is_scalar(typ):
    """ Returns True if the type of 'typ' is a scalar type, according to
    NumPy rules. False otherwise.
    https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types
    """
    ok = (types.Boolean, types.Number, types.UnicodeType, types.StringLiteral, types.NPTimedelta, types.NPDatetime)
    return isinstance(typ, ok)


def check_is_integer(v, name):
    '''Raises TypingError if the value is not an integer.'''
    if not isinstance(v, (int, types.Integer)):
        raise TypingError('{} must be an integer'.format(name))


def lt_floats(a, b):
