# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _endian.pyc (Python 3.11)

import sys
from ctypes import *
_array_type = type(Array)

def _other_endian(typ):
    """Return the type with the 'other' byte order.  Simple types like
    c_int and so on already have __ctype_be__ and __ctype_le__
    attributes which contain the types, for more complicated types
    arrays and structures are supported.
    """
    if hasattr(typ, _OTHER_ENDIAN):
        return getattr(typ, _OTHER_ENDIAN)
    if None(typ, _array_type):
        return _other_endian(typ._type_) * typ._length_
    if None(typ, (Structure, Union)):
        return typ
    raise None('This type does not support other endian: %s' % typ)


class _swapped_meta:
    pass
# WARNING: Decompyle incomplete


def _swapped_struct_meta():
    '''_swapped_struct_meta'''
    pass

_swapped_struct_meta = <NODE:27>(_swapped_struct_meta, '_swapped_struct_meta', _swapped_meta, type(Structure))

def _swapped_union_meta():
    '''_swapped_union_meta'''
    pass

_swapped_union_meta = <NODE:27>(_swapped_union_meta, '_swapped_union_meta', _swapped_meta, type(Union))
if sys.byteorder == 'little':
    _OTHER_ENDIAN = '__ctype_be__'
    LittleEndianStructure = Structure
    
    def BigEndianStructure():
        '''BigEndianStructure'''
        __doc__ = 'Structure with big endian byte order'
        __slots__ = ()
        _swappedbytes_ = None

    BigEndianStructure = <NODE:27>(BigEndianStructure, 'BigEndianStructure', Structure, metaclass = _swapped_struct_meta)
    LittleEndianUnion = Union
    
    def BigEndianUnion():
        '''BigEndianUnion'''
        __doc__ = 'Union with big endian byte order'
        __slots__ = ()
        _swappedbytes_ = None

    BigEndianUnion = <NODE:27>(BigEndianUnion, 'BigEndianUnion', Union, metaclass = _swapped_union_meta)
    return None
if None.byteorder == 'big':
    _OTHER_ENDIAN = '__ctype_le__'
    BigEndianStructure = Structure
    
    def LittleEndianStructure():
        '''LittleEndianStructure'''
        __doc__ = 'Structure with little endian byte order'
        __slots__ = ()
        _swappedbytes_ = None

    LittleEndianStructure = <NODE:27>(LittleEndianStructure, 'LittleEndianStructure', Structure, metaclass = _swapped_struct_meta)
    BigEndianUnion = Union
    
    def LittleEndianUnion():
        '''LittleEndianUnion'''
        __doc__ = 'Union with little endian byte order'
        __slots__ = ()
        _swappedbytes_ = None

    LittleEndianUnion = <NODE:27>(LittleEndianUnion, 'LittleEndianUnion', Union, metaclass = _swapped_union_meta)
    return None
raise RuntimeError('Invalid byteorder')
