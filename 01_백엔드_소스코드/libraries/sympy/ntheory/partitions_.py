# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: partitions_.pyc (Python 3.11)

from mpmath.libmp import fzero, from_int, from_rational, fone, fhalf, bitcount, to_int, mpf_mul, mpf_div, mpf_sub, mpf_add, mpf_sqrt, mpf_pi, mpf_cosh_sinh, mpf_cos, mpf_sin
from sympy.external.gmpy import gcd, legendre, jacobi
from residue_ntheory import _sqrt_mod_prime_power, is_quad_residue
from sympy.utilities.decorator import deprecated
from sympy.utilities.memoization import recurrence_memo
import math
from itertools import count

def _pre():
    global _factor, _totient
    maxn = 100000
    _factor = [
        0] * maxn
    _totient = [
        1] * maxn
    lim = int(maxn ** 0.5) + 5
    for i in range(2, lim):
        if _factor[i] == 0:
            for j in range(i * i, maxn, i):
                if _factor[j] == 0:
                    _factor[j] = i
                for i in range(2, maxn):
                    if _factor[i] == 0:
                        _factor[i] = i
                        _totient[i] = i - 1
                        continue
                    x = _factor[i]
                    y = i // x
                    if y % x == 0:
                        _totient[i] = _totient[y] * x
                        continue
                    _totient[i] = _totient[y] * (x - 1)
                    return None


def _a(n, k, prec):
    ''' Compute the inner sum in HRR formula [1]_

    References
    ==========

    .. [1] https://msp.org/pjm/1956/6-1/pjm-v6-n1-p18-p.pdf

    '''
    if k == 1:
        return fone
    k1 = None
    e = 0
    p = _factor[k]
# WARNING: Decompyle incomplete


def _d(n, j, prec, sq23pi, sqrt8):
    '''
    Compute the sinh term in the outer sum of the HRR formula.
    The constants sqrt(2/3*pi) and sqrt(8) must be precomputed.
    '''
    j = from_int(j)
    pi = mpf_pi(prec)
    a = mpf_div(sq23pi, j, prec)
    b = mpf_sub(from_int(n), from_rational(1, 24, prec), prec)
    c = mpf_sqrt(b, prec)
    (ch, sh) = mpf_cosh_sinh(mpf_mul(a, c), prec)
    D = mpf_div(mpf_sqrt(j, prec), mpf_mul(mpf_mul(sqrt8, b), pi), prec)
    E = mpf_sub(mpf_mul(a, ch), mpf_div(sh, c, prec), prec)
    return mpf_mul(D, E)

_partition_rec = (lambda n = None, prev = None: v = 0penta = 0for i in count():
penta += 3 * i + 1np = n - pentaif np < 0:
passelse:
s = prev[np]np -= i + 1if 0 <= np:
s += prev[np]v += -s if i % 2 else sv)()

def _partition(n = None):
    ''' Calculate the partition function P(n)

    Parameters
    ==========

    n : int

    '''
    pass
# WARNING: Decompyle incomplete

npartitions = (lambda n, verbose = (False,): func_partition = partitionimport sympy.functions.combinatorial.numbersfunc_partition(n))()
