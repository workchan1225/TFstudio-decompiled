# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libmpf.pyc (Python 3.11)

'''
Low-level functions for arbitrary-precision floating-point arithmetic.
'''
__docformat__ = 'plaintext'
import math
from bisect import bisect
import sys
getrandbits = None
from backend import MPZ, MPZ_TYPE, MPZ_ZERO, MPZ_ONE, MPZ_TWO, MPZ_FIVE, BACKEND, STRICT, HASH_MODULUS, HASH_BITS, gmpy, sage, sage_utils
from libintmath import giant_steps, trailtable, bctable, lshift, rshift, bitcount, trailing, sqrt_fixed, numeral, isqrt, isqrt_fast, sqrtrem, bin_to_radix
if BACKEND == 'sage':
    
    def to_pickable(x):
        (sign, man, exp, bc) = x
        return (sign, hex(man), exp, bc)

else:
    
    def to_pickable(x):
        (sign, man, exp, bc) = x
        return (sign, hex(man)[2:], exp, bc)


def from_pickable(x):
    (sign, man, exp, bc) = x
    return (sign, MPZ(man, 16), exp, bc)


class ComplexResult(ValueError):
    pass


try:
    intern
except NameError:
    
    intern = lambda x: x

round_nearest = intern('n')
round_floor = intern('f')
round_ceiling = intern('c')
round_up = intern('u')
round_down = intern('d')
round_fast = round_down

def prec_to_dps(n):
    '''Return number of accurate decimals that can be represented
    with a precision of n bits.'''
    return max(1, int(round(int(n) / 3.32193) - 1))


def dps_to_prec(n):
    '''Return the number of bits required to represent n decimals
    accurately.'''
    return max(1, int(round((int(n) + 1) * 3.32193)))


def repr_dps(n):
    '''Return the number of decimal digits required to represent
    a number with n-bit precision so that it can be uniquely
    reconstructed from the representation.'''
    dps = prec_to_dps(n)
    if dps == 15:
        return 17
    return None + 3

fzero = (0, MPZ_ZERO, 0, 0)
fnzero = (1, MPZ_ZERO, 0, 0)
fone = (0, MPZ_ONE, 0, 1)
fnone = (1, MPZ_ONE, 0, 1)
ftwo = (0, MPZ_ONE, 1, 1)
ften = (0, MPZ_FIVE, 1, 3)
fhalf = (0, MPZ_ONE, -1, 1)
fnan = (0, MPZ_ZERO, -123, -1)
finf = (0, MPZ_ZERO, -456, -2)
fninf = (1, MPZ_ZERO, -789, -3)
math_float_inf = float('inf')

def round_int(x, n, rnd):
