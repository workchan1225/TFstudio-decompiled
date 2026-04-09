# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libintmath.pyc (Python 3.11)

'''
Utility functions for integer math.

TODO: rename, cleanup, perhaps move the gmpy wrapper code
here from settings.py

'''
import math
from bisect import bisect
from backend import xrange
from backend import BACKEND, gmpy, sage, sage_utils, MPZ, MPZ_ONE, MPZ_ZERO
small_trailing = [
    0] * 256
for j in range(1, 8):
    small_trailing[1 << j::1 << j + 1] = [
        j] * (1 << 7 - j)
    
    def giant_steps(start, target, n = (2,)):
        """
    Return a list of integers ~=

    [start, n*start, ..., target/n^2, target/n, target]

    but conservatively rounded so that the quotient between two
    successive elements is actually slightly less than n.

    With n = 2, this describes suitable precision steps for a
    quadratically convergent algorithm such as Newton's method;
    with n = 3 steps for cubic convergence (Halley's method), etc.

        >>> giant_steps(50,1000)
        [66, 128, 253, 502, 1000]
        >>> giant_steps(50,1000,4)
        [65, 252, 1000]

    """
        L = [
            target]
    # WARNING: Decompyle incomplete

    
    def rshift(x, n):
        '''For an integer x, calculate x >> n with the fastest (floor)
    rounding. Unlike the plain Python expression (x >> n), n is
    allowed to be negative, in which case a left shift is performed.'''
        if n >= 0:
            return x >> n
        return None << -n

    
    def lshift(x, n):
        '''For an integer x, calculate x << n. Unlike the plain Python
    expression (x << n), n is allowed to be negative, in which case a
    right shift with default (floor) rounding is performed.'''
        if n >= 0:
            return x << n
        return None >> -n

    if BACKEND == 'sage':
        import operator
        rshift = operator.rshift
        lshift = operator.lshift

def python_trailing(n):
    '''Count the number of trailing zero bits in abs(n).'''
    if not n:
        return 0
    low_byte = None & 255
    if low_byte:
        return small_trailing[low_byte]
    t = None
    n >>= 8
# WARNING: Decompyle incomplete

if BACKEND == 'gmpy':
    if gmpy.version() >= '2':
        
        def gmpy_trailing(n):
            '''Count the number of trailing zero bits in abs(n) using gmpy.'''
            if n:
                return MPZ(n).bit_scan1()

    else:
        
        def gmpy_trailing(n):
            '''Count the number of trailing zero bits in abs(n) using gmpy.'''
            if n:
                return MPZ(n).scan1()

powers = range(300)()

def python_bitcount(n):
    '''Calculate bit size of the nonnegative integer n.'''
    bc = bisect(powers, n)
    if bc != 300:
        return bc
    bc = None(math.log(n, 2)) - 4
    return bc + bctable[n >> bc]


def gmpy_bitcount(n):
    '''Calculate bit size of the nonnegative integer n.'''
    if n:
        return MPZ(n).numdigits(2)


def sage_trailing(n):
    return MPZ(n).trailing_zero_bits()

if BACKEND == 'gmpy':
    bitcount = gmpy_bitcount
    trailing = gmpy_trailing
elif BACKEND == 'sage':
    sage_bitcount = sage_utils.bitcount
    bitcount = sage_bitcount
    trailing = sage_trailing
else:
    bitcount = python_bitcount
    trailing = python_trailing
if BACKEND == 'gmpy' and 'bit_length' in dir(gmpy):
    bitcount = gmpy.bit_length
trailtable = range(256)()
bctable = range(1024)()

def bin_to_radix(x, xbits, base, bdigits):
    '''Changes radix of a fixed-point number; i.e., converts
    x * 2**xbits to floor(x * 10**bdigits).'''
    return x * MPZ(base) ** bdigits >> xbits

stddigits = '0123456789abcdefghijklmnopqrstuvwxyz'

def small_numeral(n, base, digits = (10, stddigits)):
    '''Return the string numeral of a positive integer in an arbitrary
    base. Most efficient for small input.'''
    if base == 10:
        return str(n)
    digs = None
# WARNING: Decompyle incomplete


def numeral_python(n, base, size, digits = (10, 0, stddigits)):
    """Represent the integer n as a string of digits in the given base.
    Recursive division is used to make this function about 3x faster
    than Python's str() for converting integers to decimal strings.

    The 'size' parameters specifies the number of digits in n; this
    number is only used to determine splitting points and need not be
    exact."""
    if n <= 0:
        if not n:
            return '0'
        return None + numeral(-n, base, size, digits)
    if None < 250:
        return small_numeral(n, base, digits)
    half = None // 2 + (size & 1)
    (A, B) = divmod(n, base ** half)
    ad = numeral(A, base, half, digits)
    bd = numeral(B, base, half, digits).rjust(half, '0')
    return ad + bd


def numeral_gmpy(n, base, size, digits = (10, 0, stddigits)):
    """Represent the integer n as a string of digits in the given base.
    Recursive division is used to make this function about 3x faster
    than Python's str() for converting integers to decimal strings.

    The 'size' parameters specifies the number of digits in n; this
    number is only used to determine splitting points and need not be
    exact."""
    if n < 0:
        return '-' + numeral(-n, base, size, digits)
    if None < 1500000:
        return gmpy.digits(n, base)
    half = None // 2 + (size & 1)
    (A, B) = divmod(n, MPZ(base) ** half)
    ad = numeral(A, base, half, digits)
    bd = numeral(B, base, half, digits).rjust(half, '0')
    return ad + bd

_1_800 = 1 << 800
_1_600 = 1 << 600
_1_400 = 1 << 400
_1_200 = 1 << 200
_1_100 = 0x10000000000000000000000000
_1_50 = 0x4000000000000

def isqrt_small_python(x):
    '''
    Correctly (floor) rounded integer square root, using
    division. Fast up to ~200 digits.
    '''
    if not x:
        return x
    if None < _1_800:
        if x < _1_50:
            return int(x ** 0.5)
        r = None(x ** 0.5 * 1) + 1
    else:
        bc = bitcount(x)
        n = bc // 2
        r = int((x >> 2 * n - 100) ** 0.5 + 2) << n - 50
    y = r + x // r >> 1
    if y >= r:
        return r
    r = None
    continue


def isqrt_fast_python(x):
    '''
    Fast approximate integer square root, computed using division-free
    Newton iteration for large x. For random integers the result is almost
    always correct (floor(sqrt(x))), but is 1 ulp too small with a roughly
    0.1% probability. If x is very close to an exact square, the answer is
    1 ulp wrong with high probability.

    With 0 guard bits, the largest error over a set of 10^5 random
    inputs of size 1-10^5 bits was 3 ulp. The use of 10 guard bits
    almost certainly guarantees a max 1 ulp error.
    '''
    if x < _1_800:
        y = int(x ** 0.5)
        if x >= _1_100:
            y = y + x // y >> 1
            if x >= _1_200:
                y = y + x // y >> 1
                if x >= _1_400:
                    y = y + x // y >> 1
        return y
    bc = None(x)
    guard_bits = 10
    x <<= 2 * guard_bits
    bc += 2 * guard_bits
    bc += bc & 1
    hbc = bc // 2
    startprec = min(50, hbc)
    r = int(2 ** (2 * startprec) * (x >> bc - 2 * startprec) ** -0.5)
    pp = startprec
    for p in giant_steps(startprec, hbc):
        r2 = r * r >> 2 * pp - p
        xr2 = (x >> bc - p) * r2 >> p
        r = r * ((3 << p) - xr2) >> pp + 1
        pp = p
        return r * (x >> hbc) >> p + guard_bits


def sqrtrem_python(x):
    '''Correctly rounded integer (floor) square root with remainder.'''
    if x < _1_600:
        y = isqrt_small_python(x)
        return (y, x - y * y)
    y = None(x) + 1
    rem = x - y * y
# WARNING: Decompyle incomplete


def isqrt_python(x):
    '''Integer square root with correct (floor) rounding.'''
    return sqrtrem_python(x)[0]


def sqrt_fixed(x, prec):
    return isqrt_fast(x << prec)

sqrt_fixed2 = sqrt_fixed
if BACKEND == 'gmpy':
    if gmpy.version() >= '2':
        isqrt_small = gmpy.isqrt
        isqrt_fast = gmpy.isqrt
        isqrt = gmpy.isqrt
        sqrtrem = gmpy.isqrt_rem
    else:
        isqrt_small = gmpy.sqrt
        isqrt_fast = gmpy.sqrt
        isqrt = gmpy.sqrt
        sqrtrem = gmpy.sqrtrem
elif BACKEND == 'sage':
    isqrt_small = getattr(sage_utils, 'isqrt', (lambda n: MPZ(n).isqrt()))
    isqrt_fast = getattr(sage_utils, 'isqrt', (lambda n: MPZ(n).isqrt()))
    isqrt = getattr(sage_utils, 'isqrt', (lambda n: MPZ(n).isqrt()))
    
    sqrtrem = lambda n: MPZ(n).sqrtrem()
else:
    isqrt_small = isqrt_small_python
    isqrt_fast = isqrt_fast_python
    isqrt = isqrt_python
    sqrtrem = sqrtrem_python

def ifib(n, _cache = ({ },)):
    '''Computes the nth Fibonacci number as an integer, for
    integer n.'''
    if n < 0:
        return -1 ** (-n + 1) * ifib(-n)
    if None in _cache:
        return _cache[n]
    m = None
    (a, b, p, q) = (MPZ_ONE, MPZ_ZERO, MPZ_ZERO, MPZ_ONE)
# WARNING: Decompyle incomplete

MAX_FACTORIAL_CACHE = 1000

def ifac(n, memo = ({
    0: 1,
    1: 1 },)):
    '''Return n factorial (for integers n >= 0 only).'''
    f = memo.get(n)
    if f:
        return f
    k = None(memo)
    p = memo[k - 1]
    MAX = MAX_FACTORIAL_CACHE
# WARNING: Decompyle incomplete


def ifac2(n, memo_pair = ([
    {
        0: 1 },
    {
        1: 1 }],)):
    '''Return n!! (double factorial), integers n >= 0 only.'''
    memo = memo_pair[n & 1]
    f = memo.get(n)
    if f:
        return f
    k = None(memo)
    p = memo[k]
    MAX = MAX_FACTORIAL_CACHE
# WARNING: Decompyle incomplete

if BACKEND == 'gmpy':
    ifac = gmpy.fac
elif BACKEND == 'sage':
    
    ifac = lambda n: int(sage.factorial(n))
    ifib = sage.fibonacci

def list_primes(n):
    n = n + 1
    sieve = list(xrange(n))
    sieve[:2] = [
        0,
        0]
    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i ** 2, n, i):
                sieve[j] = 0
                return sieve()

if BACKEND == 'sage':
    
    def list_primes(n):
        return sage.primes(n + 1)()

small_odd_primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
small_odd_primes_set = set(small_odd_primes)

def isprime(n):
    '''
    Determines whether n is a prime number. A probabilistic test is
    performed if n is very large. No special trick is used for detecting
    perfect powers.

        >>> sum(list_primes(100000))
        454396537
        >>> sum(n*isprime(n) for n in range(100000))
        454396537

    '''
    pass
# WARNING: Decompyle incomplete


def moebius(n):
    '''
    Evaluates the Moebius function which is `mu(n) = (-1)^k` if `n`
    is a product of `k` distinct primes and `mu(n) = 0` otherwise.

    TODO: speed up using factorization
    '''
    pass
# WARNING: Decompyle incomplete


def gcd(*args):
    a = 0
# WARNING: Decompyle incomplete

MAX_EULER_CACHE = 500

def eulernum(m, _cache = ({
    0: MPZ_ONE },)):
    '''
    Computes the Euler numbers `E(n)`, which can be defined as
    coefficients of the Taylor expansion of `1/cosh x`:

    .. math ::

        \\frac{1}{\\cosh x} = \\sum_{n=0}^\\infty \\frac{E_n}{n!} x^n

    Example::

        >>> [int(eulernum(n)) for n in range(11)]
        [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
        >>> [int(eulernum(n)) for n in range(11)]   # test cache
        [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]

    '''
    if m & 1:
        return MPZ_ZERO
    f = None.get(m)
    if f:
        return f
    MAX = None
    n = m
    a = (0, 0, 1, 0, 0, 0)()
    for n in range(1, m + 1):
        for j in range(n + 1, -1, -2):
            a[j + 1] = (j - 1) * a[j] + (j + 1) * a[j + 2]
            a.append(0)
            suma = 0
            for k in range(n + 1, -1, -2):
                suma += a[k + 1]
                if n <= MAX:
                    _cache[n] = -1 ** (n // 2) * (suma // 2 ** n)
                if n == m:
                    
                    return (lambda .0: [ MPZ(_) for _ in .0 ]), -1 ** (n // 2) * suma // 2 ** n
                return None


def stirling1(n, k):
    '''
    Stirling number of the first kind.
    '''
    if n < 0 or k < 0:
        raise ValueError
    if k >= n:
        return MPZ(n == k)
    if None < 1:
        return MPZ_ZERO
    L = [
        None] * (k + 1)
    L[1] = MPZ_ONE
    for m in xrange(2, n + 1):
        for j in xrange(min(k, m), 0, -1):
            L[j] = (m - 1) * L[j] + L[j - 1]
            return -1 ** (n + k) * L[k]


def stirling2(n, k):
    '''
    Stirling number of the second kind.
    '''
    if n < 0 or k < 0:
        raise ValueError
    if k >= n:
        return MPZ(n == k)
    if None <= 1:
        return MPZ(k == 1)
    s = None
    t = MPZ_ONE
    for j in xrange(k + 1):
        if k + j & 1:
            s -= t * MPZ(j) ** n
        else:
            s += t * MPZ(j) ** n
        t = t * (k - j) // (j + 1)
        return s // ifac(k)
