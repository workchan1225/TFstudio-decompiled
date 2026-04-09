# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hashing.pyc (Python 3.11)

'''
Hash implementations for Numba types
'''
import math
import numpy as np
import sys
import ctypes
import warnings
from collections import namedtuple
from llvmlite.binding import binding as ll
from llvmlite import ir
from numba import literal_unroll
from numba.core.extending import overload, overload_method, intrinsic, register_jitable
from numba.core import errors
from numba.core import types
from numba.core.unsafe.bytes import grab_byte, grab_uint64_t
from numba.cpython.randomimpl import const_int, get_next_int, get_next_int32, get_state_ptr
_hash_width = sys.hash_info.width
_Py_hash_t = getattr(types, 'int%s' % _hash_width)
_Py_uhash_t = getattr(types, 'uint%s' % _hash_width)
_PyHASH_INF = sys.hash_info.inf
_PyHASH_NAN = sys.hash_info.nan
_PyHASH_MODULUS = _Py_uhash_t(sys.hash_info.modulus)
_PyHASH_BITS = 31 if types.intp.bitwidth == 32 else 61
_PyHASH_MULTIPLIER = 1000003
_PyHASH_IMAG = _PyHASH_MULTIPLIER
_PyLong_SHIFT = sys.int_info.bits_per_digit
_Py_HASH_CUTOFF = sys.hash_info.cutoff
_Py_hashfunc_name = sys.hash_info.algorithm

def _defer_hash(hash_func):
    pass

ol_defer_hash = (lambda obj, hash_func: pass# WARNING: Decompyle incomplete
)()
hash_overload = (lambda obj: pass# WARNING: Decompyle incomplete
)()
process_return = (lambda val: asint = _Py_hash_t(val)if asint == int(-1):
asint = int(-2)asint)()
_Py_HashDouble = (lambda v: if not np.isfinite(v):
if np.isinf(v):
if v > 0:
_PyHASH_INF-Nonex = None()process_return(x)(m, e) = None.frexp(v)sign = 1if m < 0:
sign = -1m = -mx = 0# WARNING: Decompyle incomplete
)()
_fpext = (lambda tyctx, val: 
def impl(cgctx, builder, signature, args):
val = args[0]builder.fpext(val, ir.DoubleType())sig = types.float64(types.float32)(sig, impl))()
_prng_random_hash = (lambda tyctx: 
def impl(cgctx, builder, signature, args):
state_ptr = get_state_ptr(cgctx, builder, 'internal')bits = const_int(_hash_width)if _hash_width == 32:
value = get_next_int32(cgctx, builder, state_ptr)else:
value = get_next_int(cgctx, builder, state_ptr, bits, False)valuesig = _Py_hash_t()(sig, impl))()
_long_impl = (lambda val: _tmp_shift = 32 - _PyLong_SHIFTmask_shift = ~types.uint32(0) >> _tmp_shifti = 64 // _PyLong_SHIFT + 1x = 0p3 = _PyHASH_BITS - _PyLong_SHIFTfor idx in range(i - 1, -1, -1):
p1 = x << _PyLong_SHIFTp2 = p1 & _PyHASH_MODULUSp4 = x >> p3x = p2 | p4x += types.uint32(val >> idx * _PyLong_SHIFT & mask_shift)if x >= _PyHASH_MODULUS:
x -= _PyHASH_MODULUS_Py_hash_t(x))()
int_hash = (lambda val: pass# WARNING: Decompyle incomplete
)()()
float_hash = (lambda val: if val.bitwidth == 64:

def impl(val):
hashed = _Py_HashDouble(val)hashedelse:

def impl(val):
fpextended = np.float64(_fpext(val))hashed = _Py_HashDouble(fpextended)hashedimpl)()
complex_hash = (lambda val: 
def impl(val):
hashreal = hash(val.real)hashimag = hash(val.imag)combined = hashreal + _PyHASH_IMAG * hashimagprocess_return(combined)impl)()
_tuple_hash = (lambda tup: tl = len(tup)acc = _PyHASH_XXPRIME_5for x in literal_unroll(tup):
lane = hash(x)if lane == _Py_uhash_t(-1):
-1None += lane * _PyHASH_XXPRIME_2acc = _PyHASH_XXROTATE(acc)acc *= _PyHASH_XXPRIME_1acc += tl ^ _PyHASH_XXPRIME_5 ^ _Py_uhash_t(3527539)if acc == _Py_uhash_t(-1):
process_return(1546275796)None(acc))()
tuple_hash = (lambda val: 
def impl(val):
_tuple_hash(val)impl)()
from ctypes import c_size_t, c_ubyte, c_uint64, pythonapi, Structure, Union

class FNV(Structure):
    _fields_ = [
        ('prefix', c_size_t),
        ('suffix', c_size_t)]


class SIPHASH(Structure):
    _fields_ = [
        ('k0', c_uint64),
        ('k1', c_uint64)]


class DJBX33A(Structure):
    _fields_ = [
        ('padding', c_ubyte * 16),
        ('suffix', c_size_t)]


class EXPAT(Structure):
    _fields_ = [
        ('padding', c_ubyte * 16),
        ('hashsalt', c_size_t)]


class _Py_HashSecret_t(Union):
    _fields_ = [
        ('uc', c_ubyte * 24),
        ('fnv', FNV),
        ('siphash', SIPHASH),
        ('djbx33a', DJBX33A),
        ('expat', EXPAT)]

_hashsecret_entry = namedtuple('_hashsecret_entry', [
    'symbol',
    'value'])

def _build_hashsecret():
    '''Read hash secret from the Python process

    Returns
    -------
    info : dict
        - keys are "djbx33a_suffix", "siphash_k0", siphash_k1".
        - values are the namedtuple[symbol:str, value:int]
    '''
    pass
# WARNING: Decompyle incomplete

_hashsecret = _build_hashsecret()
if _Py_hashfunc_name in ('siphash13', 'siphash24', 'fnv'):
    if _Py_hashfunc_name == 'fnv':
        msg = 'FNV hashing is not implemented in Numba. See PEP 456 https://www.python.org/dev/peps/pep-0456/ for rationale over not using FNV. Numba will continue to work, but hashes for built in types will be computed using siphash24. This will permit e.g. dictionaries to continue to behave as expected, however anything relying on the value of the hash opposed to hash as a derived property is likely to not work as expected.'
        warnings.warn(msg)
    _ROTATE = (lambda x, b: types.uint64(x << b | x >> types.uint64(64) - b))()
    _HALF_ROUND = (lambda a, b, c, d, s, t: a += bc += db = _ROTATE(b, s) ^ ad = _ROTATE(d, t) ^ ca = _ROTATE(a, 32)(a, b, c, d))()
    _SINGLE_ROUND = (lambda v0, v1, v2, v3: (v0, v1, v2, v3) = _HALF_ROUND(v0, v1, v2, v3, 13, 16)(v2, v1, v0, v3) = _HALF_ROUND(v2, v1, v0, v3, 17, 21)(v0, v1, v2, v3))()
    _DOUBLE_ROUND = (lambda v0, v1, v2, v3: (v0, v1, v2, v3) = _SINGLE_ROUND(v0, v1, v2, v3)(v0, v1, v2, v3) = _SINGLE_ROUND(v0, v1, v2, v3)(v0, v1, v2, v3))()
    
    def _gen_siphash(alg):
        pass
    # WARNING: Decompyle incomplete

    _siphash13 = _gen_siphash('siphash13')
    _siphash24 = _gen_siphash('siphash24')
    _siphasher = _siphash13 if _Py_hashfunc_name == 'siphash13' else _siphash24
else:
    msg = 'Unsupported hashing algorithm in use %s' % _Py_hashfunc_name
    raise ValueError(msg)
_inject_hashsecret_read = (lambda tyctx, name: pass# WARNING: Decompyle incomplete
)()

def _load_hashsecret(name):
    return _hashsecret[name].value

_impl_load_hashsecret = (lambda name: 
def imp(name):
_inject_hashsecret_read(name)imp)()
_Py_HashBytes = (lambda val, _len: if _len == 0:
process_return(0)if None < _Py_HASH_CUTOFF:
_hash = _Py_uhash_t(5381)for idx in range(_len):
_hash = (_hash << 5) + _hash + np.uint8(grab_byte(val, idx))_hash ^= _len_hash ^= _load_hashsecret('djbx33a_suffix')tmp = _siphasher(types.uint64(_load_hashsecret('siphash_k0')), types.uint64(_load_hashsecret('siphash_k1')), val, _len)_hash = process_return(tmp)process_return(_hash))()
unicode_hash = (lambda val: pass# WARNING: Decompyle incomplete
)()
