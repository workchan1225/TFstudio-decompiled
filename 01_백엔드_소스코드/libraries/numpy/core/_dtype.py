# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dtype.pyc (Python 3.11)

'''
A place for code to be called from the implementation of np.dtype

String handling is much easier to do correctly in python.
'''
import numpy as np
_kind_to_stem = {
    'u': 'uint',
    'i': 'int',
    'c': 'complex',
    'f': 'float',
    'b': 'bool',
    'V': 'void',
    'O': 'object',
    'M': 'datetime',
    'm': 'timedelta',
    'S': 'bytes',
    'U': 'str' }

def _kind_name(dtype):
    
    try:
        return _kind_to_stem[dtype.kind]
    except KeyError:
        e = None
        raise RuntimeError('internal dtype error, unknown kind {!r}'.format(dtype.kind)), None
        e = None
        del e



def __str__(dtype):
    pass
# WARNING: Decompyle incomplete


def __repr__(dtype):
    arg_str = _construction_repr(dtype, include_align = False)
    if dtype.isalignedstruct:
        arg_str = arg_str + ', align=True'
    return 'dtype({})'.format(arg_str)


def _unpack_field(dtype, offset, title = (None,)):
    '''
    Helper function to normalize the items in dtype.fields.

    Call as:

    dtype, offset, title = _unpack_field(*dtype.fields[name])
    '''
    return (dtype, offset, title)


def _isunsized(dtype):
    return dtype.itemsize == 0


def _construction_repr(dtype, include_align, short = (False, False)):
    """
    Creates a string repr of the dtype, excluding the 'dtype()' part
    surrounding the object. This object may be a string, a list, or
    a dict depending on the nature of the dtype. This
    is the object passed as the first parameter to the dtype
    constructor, and if no additional constructor parameters are
    given, will reproduce the exact memory layout.

    Parameters
    ----------
    short : bool
        If true, this creates a shorter repr using 'kind' and 'itemsize', instead
        of the longer type name.

    include_align : bool
        If true, this includes the 'align=True' parameter
        inside the struct dtype construction dict when needed. Use this flag
        if you want a proper repr string without the 'dtype()' part around it.

        If false, this does not preserve the
        'align=True' parameter or sticky NPY_ALIGNED_STRUCT flag for
        struct arrays like the regular repr does, because the 'align'
        flag is not part of first dtype constructor parameter. This
        mode is intended for a full 'repr', where the 'align=True' is
        provided as the second parameter.
    """
    pass
# WARNING: Decompyle incomplete


def _scalar_str(dtype, short):
    byteorder = _byte_order_str(dtype)
    if dtype.type == np.bool_:
        if short:
            return "'?'"
        return None
    if None.type == np.object_:
        return "'O'"
    if None.type == np.bytes_:
        if _isunsized(dtype):
            return "'S'"
        return None % dtype.itemsize
    if None.type == np.str_:
        if _isunsized(dtype):
            return "'%sU'" % byteorder
        return None % (byteorder, dtype.itemsize / 4)
    if None(dtype.type, np.void):
        if _isunsized(dtype):
            return "'V'"
        return None % dtype.itemsize
    if None.type == np.datetime64:
        return f'''\'{byteorder!s}M8{_datetime_metadata_str(dtype)!s}\''''
    if None.type == np.timedelta64:
        return f'''\'{byteorder!s}m8{_datetime_metadata_str(dtype)!s}\''''
    if None.issubdtype(dtype, np.number):
        if short or dtype.byteorder not in ('=', '|'):
            return "'%s%c%d'" % (byteorder, dtype.kind, dtype.itemsize)
        return None % (_kind_name(dtype), 8 * dtype.itemsize)
    if None.isbuiltin == 2:
        return dtype.type.__name__
    raise None('Internal error: NumPy dtype unrecognized type number')


def _byte_order_str(dtype):
    """ Normalize byteorder to '<' or '>' """
    swapped = np.dtype(int).newbyteorder('S')
    native = swapped.newbyteorder('S')
    byteorder = dtype.byteorder
    if byteorder == '=':
        return native.byteorder
    if None == 'S':
        return swapped.byteorder
    if None == '|':
        return ''


def _datetime_metadata_str(dtype):
    (unit, count) = np.datetime_data(dtype)
    if unit == 'generic':
        return ''
    if None == 1:
        return '[{}]'.format(unit)
    return None.format(count, unit)


def _struct_dict_str(dtype, includealignedflag):
    names = dtype.names
    fld_dtypes = []
    offsets = []
    titles = []
# WARNING: Decompyle incomplete


def _aligned_offset(offset, alignment):
    return -(-offset // alignment) * alignment


def _is_packed(dtype):
    """
    Checks whether the structured data type in 'dtype'
    has a simple layout, where all the fields are in order,
    and follow each other with no alignment padding.

    When this returns true, the dtype can be reconstructed
    from a list of the field names and dtypes with no additional
    dtype parameters.

    Duplicates the C `is_dtype_struct_simple_unaligned_layout` function.
    """
    align = dtype.isalignedstruct
    max_alignment = 1
    total_offset = 0
# WARNING: Decompyle incomplete


def _struct_list_str(dtype):
    items = []
# WARNING: Decompyle incomplete


def _struct_str(dtype, include_align):
    if (include_align or dtype.isalignedstruct) and _is_packed(dtype):
        sub = _struct_list_str(dtype)
    else:
        sub = _struct_dict_str(dtype, include_align)
    if dtype.type != np.void:
        return '({t.__module__}.{t.__name__}, {f})'.format(t = dtype.type, f = sub)


def _subarray_str(dtype):
    (base, shape) = dtype.subdtype
    return '({}, {})'.format(_construction_repr(base, short = True), shape)


def _name_includes_bit_suffix(dtype):
    if dtype.type == np.object_:
        return False
    if None.type == np.bool_:
        return False
# WARNING: Decompyle incomplete


def _name_get(dtype):
    if dtype.isbuiltin == 2:
        return dtype.type.__name__
    if None.kind == '\x00':
        name = type(dtype).__name__
    elif issubclass(dtype.type, np.void):
        name = dtype.type.__name__
    else:
        name = _kind_name(dtype)
    if _name_includes_bit_suffix(dtype):
        name += '{}'.format(dtype.itemsize * 8)
    if dtype.type in (np.datetime64, np.timedelta64):
        name += _datetime_metadata_str(dtype)
    return name
