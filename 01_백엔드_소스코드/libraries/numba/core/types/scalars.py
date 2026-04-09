# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scalars.pyc (Python 3.11)

import enum
import numpy as np
from abstract import Dummy, Hashable, Literal, Number, Type
from functools import total_ordering, cached_property
from numba.core import utils
from numba.core.typeconv import Conversion
from numba.np import npdatetime_helpers

class Boolean(Hashable):
    
    def cast_python_value(self, value):
        return bool(value)



def parse_integer_bitwidth(name):
    for prefix in ('int', 'uint'):
        if name.startswith(prefix):
            bitwidth = int(name[len(prefix):])
        return bitwidth


def parse_integer_signed(name):
    signed = name.startswith('int')
    return signed

Integer = <NODE:12>()

class IntegerLiteral(Integer, Literal):
    
    def __init__(self, value):
        self._literal_init(value)
        name = 'Literal[int]({})'.format(value)
        basetype = self.literal_type
        Integer.__init__(self, name = name, bitwidth = basetype.bitwidth, signed = basetype.signed)

    
    def can_convert_to(self, typingctx, other):
        conv = typingctx.can_convert(self.literal_type, other)
    # WARNING: Decompyle incomplete


Literal.ctor_map[int] = IntegerLiteral

class BooleanLiteral(Boolean, Literal):
    
    def __init__(self, value):
        self._literal_init(value)
        name = 'Literal[bool]({})'.format(value)
        Boolean.__init__(self, name = name)

    
    def can_convert_to(self, typingctx, other):
        conv = typingctx.can_convert(self.literal_type, other)
    # WARNING: Decompyle incomplete


Literal.ctor_map[bool] = BooleanLiteral
Float = <NODE:12>()
Complex = <NODE:12>()

class _NPDatetimeBase(Type):
    pass
# WARNING: Decompyle incomplete

NPTimedelta = <NODE:12>()
NPDatetime = <NODE:12>()

class EnumClass(Dummy):
    pass
# WARNING: Decompyle incomplete


class IntEnumClass(EnumClass):
    '''
    Type class for IntEnum classes.
    '''
    basename = 'IntEnum class'
    member_type = (lambda self: IntEnumMember(self.instance_class, self.dtype))()


class EnumMember(Type):
    pass
# WARNING: Decompyle incomplete


class IntEnumMember(EnumMember):
    '''
    Type class for IntEnum members.
    '''
    basename = 'IntEnum'
    class_type_class = IntEnumClass
    
    def can_convert_to(self, typingctx, other):
        '''
        Convert IntEnum members to plain integers.
        '''
        if issubclass(self.instance_class, enum.IntEnum):
            conv = typingctx.can_convert(self.dtype, other)
            if conv:
                return max(conv, Conversion.safe)
            return None
