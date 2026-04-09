# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: appellseqs.pyc (Python 3.11)

'''
Efficient functions for generating Appell sequences.

An Appell sequence is a zero-indexed sequence of polynomials `p_i(x)`
satisfying `p_{i+1}\'(x)=(i+1)p_i(x)` for all `i`. This definition leads
to the following iterative algorithm:

.. math :: p_0(x) = c_0,\\ p_i(x) = i \\int_0^x p_{i-1}(t)\\,dt + c_i

The constant coefficients `c_i` are usually determined from the
just-evaluated integral and `i`.

Appell sequences satisfy the following identity from umbral calculus:

.. math :: p_n(x+y) = \\sum_{k=0}^n \\binom{n}{k} p_k(x) y^{n-k}

References
==========

.. [1] https://en.wikipedia.org/wiki/Appell_sequence
.. [2] Peter Luschny, "An introduction to the Bernoulli function",
       https://arxiv.org/abs/2009.06743
'''
from sympy.polys.densearith import dup_mul_ground, dup_sub_ground, dup_quo_ground
from sympy.polys.densetools import dup_eval, dup_integrate
from sympy.polys.domains import ZZ, QQ
from sympy.polys.polytools import named_poly
from sympy.utilities import public

def dup_bernoulli(n, K):
    '''Low-level implementation of Bernoulli polynomials.'''
    if n < 1:
        return [
            K.one]
    p = [
        None.one,
        K(-1, 2)]
    for i in range(2, n + 1):
        p = dup_integrate(dup_mul_ground(p, K(i), K), 1, K)
        if i % 2 == 0:
            p = dup_sub_ground(p, dup_eval(p, K(1, 2), K) * K(1 << i - 1, (1 << i) - 1), K)
        return p

bernoulli_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_bernoulli, QQ, 'Bernoulli polynomial', (x,), polys))()

def dup_bernoulli_c(n, K):
    '''Low-level implementation of central Bernoulli polynomials.'''
    p = [
        K.one]
    for i in range(1, n + 1):
        p = dup_integrate(dup_mul_ground(p, K(i), K), 1, K)
        if i % 2 == 0:
            p = dup_sub_ground(p, dup_eval(p, K.one, K) * K((1 << i - 1) - 1, (1 << i) - 1), K)
        return p

bernoulli_c_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_bernoulli_c, QQ, 'central Bernoulli polynomial', (x,), polys))()

def dup_genocchi(n, K):
    '''Low-level implementation of Genocchi polynomials.'''
    if n < 1:
        return [
            K.zero]
    p = [
        -(None.one)]
    for i in range(2, n + 1):
        p = dup_integrate(dup_mul_ground(p, K(i), K), 1, K)
        if i % 2 == 0:
            p = dup_sub_ground(p, dup_eval(p, K.one, K) // K(2), K)
        return p

genocchi_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_genocchi, ZZ, 'Genocchi polynomial', (x,), polys))()

def dup_euler(n, K):
    '''Low-level implementation of Euler polynomials.'''
    return dup_quo_ground(dup_genocchi(n + 1, ZZ), K(-n - 1), K)

euler_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_euler, QQ, 'Euler polynomial', (x,), polys))()

def dup_andre(n, K):
    '''Low-level implementation of Andre polynomials.'''
    p = [
        K.one]
    for i in range(1, n + 1):
        p = dup_integrate(dup_mul_ground(p, K(i), K), 1, K)
        if i % 2 == 0:
            p = dup_sub_ground(p, dup_eval(p, K.one, K), K)
        return p

andre_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_andre, ZZ, 'Andre polynomial', (x,), polys))()
