# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctx_fp.pyc (Python 3.11)

from ctx_base import StandardBaseContext
import math
import cmath
from  import math2
from  import function_docs
from libmp import mpf_bernoulli, to_float, int_types
from  import libmp

class FPContext(StandardBaseContext):
    """
    Context for fast low-precision arithmetic (53-bit precision, giving at most
    about 15-digit accuracy), using Python's builtin float and complex.
    """
    
    def __init__(ctx):
        StandardBaseContext.__init__(ctx)
        ctx.loggamma = math2.loggamma
        ctx._bernoulli_cache = { }
        ctx.pretty = False
        ctx._init_aliases()

    
    _mpq = lambda cls, x: float(x[0]) / x[1]
    NoConvergence = libmp.NoConvergence
    
    def _get_prec(ctx):
        return 53

    
    def _set_prec(ctx, p):
        pass

    
    def _get_dps(ctx):
        return 15

    
    def _set_dps(ctx, p):
        pass

    _fixed_precision = True
    prec = property(_get_prec, _set_prec)
    dps = property(_get_dps, _set_dps)
    zero = 0
    one = 1
    eps = math2.EPS
    inf = math2.INF
    ninf = math2.NINF
    nan = math2.NAN
    j = (0+1j)
    _wrap_specfun = (lambda cls, name, f, wrap: pass# WARNING: Decompyle incomplete
)()
    
    def bernoulli(ctx, n):
        cache = ctx._bernoulli_cache
        if n in cache:
            return cache[n]
        cache[n] = None(mpf_bernoulli(n, 53, 'n'), strict = True)
        return cache[n]

    pi = math2.pi
    e = math2.e
    euler = math2.euler
    sqrt2 = 1.41421
    sqrt5 = 2.23607
    phi = 1.61803
    ln2 = 0.693147
    ln10 = 2.30259
    euler = 0.577216
    catalan = 0.915966
    khinchin = 2.68545
    apery = 1.20206
    glaisher = 1.28243
    absmin = abs
    absmax = abs
    
    def is_special(ctx, x):
        return x - x != 0

    
    def isnan(ctx, x):
        return x != x

    
    def isinf(ctx, x):
        return abs(x) == math2.INF

    
    def isnormal(ctx, x):
        if x:
            return x - x == 0

    
    def isnpint(ctx, x):
