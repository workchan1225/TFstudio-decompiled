# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: primetest.pyc (Python 3.11)

'''
Primality testing

'''
from itertools import count
from sympy.core.sympify import sympify
from sympy.external.gmpy import gmpy as _gmpy, gcd, jacobi, is_square as gmpy_is_square, bit_scan1, is_fermat_prp, is_euler_prp, is_selfridge_prp, is_strong_selfridge_prp, is_strong_bpsw_prp
from sympy.external.ntheory import _lucas_sequence
from sympy.utilities.misc import as_int, filldedent
MERSENNE_PRIME_EXPONENTS = (2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609, 57885161, 74207281, 77232917, 82589933)

def is_fermat_pseudoprime(n, a):
