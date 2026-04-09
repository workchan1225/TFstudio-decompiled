# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generator_core.pyc (Python 3.11)

'''
Core Implementations for Generator/BitGenerator Models.
'''
from llvmlite import ir
from numba.core import cgutils, types, config
from numba.core.extending import intrinsic, make_attribute_wrapper, models, overload, register_jitable, register_model
NumPyRngBitGeneratorModel = <NODE:12>()
_bit_gen_type = types.NumPyRandomBitGeneratorType('bit_generator')
NumPyRandomGeneratorTypeModel = <NODE:12>()
make_attribute_wrapper(types.NumPyRandomGeneratorType, 'bit_generator', 'bit_generator')

def _generate_next_binding(overloadable_function, return_type):
    '''
        Generate the overloads for "next_(some type)" functions.
    '''
    pass
# WARNING: Decompyle incomplete


def next_double(bitgen):
    return bitgen.ctypes.next_double(bitgen.ctypes.state)


def next_uint32(bitgen):
    return bitgen.ctypes.next_uint32(bitgen.ctypes.state)


def next_uint64(bitgen):
    return bitgen.ctypes.next_uint64(bitgen.ctypes.state)

if config.USE_LEGACY_TYPE_SYSTEM:
    _generate_next_binding(next_double, types.double)
    _generate_next_binding(next_uint32, types.uint32)
    _generate_next_binding(next_uint64, types.uint64)
    next_float = (lambda bitgen: types.float32(types.float32(next_uint32(bitgen) >> 8) * types.float32(1) / types.float32(1.67772e+07)))()
    return None
_generate_next_binding(next_double, types.np_double)
_generate_next_binding(next_uint32, types.np_uint32)
_generate_next_binding(next_uint64, types.np_uint64)
next_float = (lambda bitgen: types.np_float32(types.np_float32(next_uint32(bitgen) >> 8) * types.np_float32(1) / types.np_float32(1.67772e+07)))()
