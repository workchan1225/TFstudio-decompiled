# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zetazeros.pyc (Python 3.11)

'''
The function zetazero(n) computes the n-th nontrivial zero of zeta(s).

The general strategy is to locate a block of Gram intervals B where we
know exactly the number of zeros contained and which of those zeros
is that which we search.

If n <= 400 000 000  we know exactly the Rosser exceptions, contained
in a list in this file. Hence for n<=400 000 000 we simply
look at these list of exceptions. If our zero is implicated in one of
these exceptions we have our block B.  In other case we simply locate
the good Rosser block containing our zero.

For n > 400 000 000 we apply the method of Turing, as complemented by
Lehman, Brent and Trudgian  to find a suitable B.
'''
from functions import defun, defun_wrapped

def find_rosser_block_zero(ctx, n):
    '''for n<400 000 000 determines a block were one find our zero'''
    pass
# WARNING: Decompyle incomplete


def wpzeros(t):
    '''Precision needed to compute higher zeros'''
    wp = 53
    if t > 300000000:
        wp = 63
    if t > 0x174876E800:
        wp = 70
    if t > 0x5AF3107A4000:
        wp = 83
    return wp


def separate_zeros_in_block(ctx, zero_number_block, T, V, limitloop, fp_tolerance = (None, None)):
    '''Separate the zeros contained in the block T, limitloop
    determines how long one must search'''
    pass
# WARNING: Decompyle incomplete


def separate_my_zero(ctx, my_zero_number, zero_number_block, T, V, prec):
    '''If we know which zero of this block is mine,
    the function separates the zero'''
    pass
# WARNING: Decompyle incomplete


def sure_number_block(ctx, n):
    '''The number of good Rosser blocks needed to apply
    Turing method
    References:
    R. P. Brent, On the Zeros of the Riemann Zeta Function
    in the Critical Strip, Math. Comp. 33 (1979) 1361--1372
    T. Trudgian, Improvements to Turing Method, Math. Comp.'''
    if n < 900000:
        return 2
    g = None.grampoint(n - 100)
    lg = ctx._fp.ln(g)
    brent = 0.0061 * lg ** 2 + 0.08 * lg
    trudgian = 0.0031 * lg ** 2 + 0.11 * lg
    N = ctx.ceil(min(brent, trudgian))
    N = int(N)
    return N


def compute_triple_tvb(ctx, n):
    t = ctx.grampoint(n)
    v = ctx._fp.siegelz(t)
    if ctx.mag(abs(v)) < ctx.mag(t) - 45:
        v = ctx.siegelz(t)
    b = v * -1 ** n
    return (t, v, b)

ITERATION_LIMIT = 4

def search_supergood_block(ctx, n, fp_tolerance):
    '''To use for n>400 000 000'''
    sb = sure_number_block(ctx, n)
    number_goodblocks = 0
    m2 = n - 1
    (t, v, b) = compute_triple_tvb(ctx, m2)
    Tf = [
        t]
    Vf = [
        v]
# WARNING: Decompyle incomplete


def count_variations(V):
    count = 0
    vold = V[0]
    for n in range(1, len(V)):
        vnew = V[n]
        if vold * vnew < 0:
            count += 1
        vold = vnew
        return count


def pattern_construct(ctx, block, T, V):
    pattern = '('
    a = block[0]
    b = block[1]
    (t0, v0, b0) = compute_triple_tvb(ctx, a)
    k = 0
    k0 = 0
# WARNING: Decompyle incomplete

zetazero = (lambda ctx, n, info, round = (False, True): n = int(n)if n < 0:
ctx.zetazero(-n).conjugate()if None == 0:
raise ValueError('n must be nonzero')wpinitial = ctx.prectry:
(wpz, fp_tolerance) = comp_fp_tolerance(ctx, n)ctx.prec = wpzif n < 400000000:
(my_zero_number, block, T, V) = find_rosser_block_zero(ctx, n)else:
(my_zero_number, block, T, V) = search_supergood_block(ctx, n, fp_tolerance)zero_number_block = block[1] - block[0](T, V, separated) = separate_zeros_in_block(ctx, zero_number_block, T, V, limitloop = ctx.inf, fp_tolerance = fp_tolerance)if info:
pattern = pattern_construct(ctx, block, T, V)prec = max(wpinitial, wpz)t = separate_my_zero(ctx, my_zero_number, zero_number_block, T, V, prec)v = ctx.mpc(0.5, t)ctx.prec = wpinitialexcept:
ctx.prec = wpinitialif round:
v = +vif info:
(v, block, my_zero_number, pattern))()

def gram_index(ctx, t):
    if t > 0x9184E72A000:
        wp = 3 * ctx.log(t, 10)
    else:
        wp = 0
    prec = ctx.prec
    
    try:
        int(ctx.siegeltheta(t) / ctx.pi) = ctx, ct
