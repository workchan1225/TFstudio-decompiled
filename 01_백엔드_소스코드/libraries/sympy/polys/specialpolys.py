# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: specialpolys.pyc (Python 3.11)

'''Functions for generating interesting polynomials, e.g. for benchmarking. '''
from sympy.core import Add, Mul, Symbol, sympify, Dummy, symbols
from sympy.core.containers import Tuple
from sympy.core.singleton import S
from sympy.ntheory import nextprime
from sympy.polys.densearith import dmp_add_term, dmp_neg, dmp_mul, dmp_sqr
from sympy.polys.densebasic import dmp_zero, dmp_one, dmp_ground, dup_from_raw_dict, dmp_raise, dup_random
from sympy.polys.domains import ZZ
from sympy.polys.factortools import dup_zz_cyclotomic_poly
from sympy.polys.polyclasses import DMP
from sympy.polys.polytools import Poly, PurePoly
from sympy.polys.polyutils import _analyze_gens
from sympy.utilities import subsets, public, filldedent
swinnerton_dyer_poly = (lambda n, x, polys = (None, False): if n <= 0:
raise ValueError('Cannot generate Swinnerton-Dyer polynomial of order %s' % n)# WARNING: Decompyle incomplete
)()
cyclotomic_poly = (lambda n, x, polys = (None, False): if n <= 0:
raise ValueError('Cannot generate cyclotomic polynomial of order %s' % n)poly = DMP(dup_zz_cyclotomic_poly(int(n), ZZ), ZZ)# WARNING: Decompyle incomplete
)()
symmetric_poly = (lambda n = public, *, polys: gens = _analyze_gens(gens)if not n < 0 and n > len(gens) or gens:
raise ValueError(f'''Cannot generate symmetric polynomial of order {n!s} for {gens!s}''')if not n:
poly = S.One# WARNING: Decompyle incomplete
)()
random_poly = (lambda x, n, inf, sup, domain, polys = (ZZ, False): poly = Poly(dup_random(n, inf, sup, domain), x, domain = domain)poly if polys else poly.as_expr())()
interpolating_poly = (lambda n, x, X, Y = ('x', 'y'): pass# WARNING: Decompyle incomplete
)()

def fateman_poly_F_1(n):
    """Fateman's GCD benchmark: trivial GCD """
    Y = range(n + 1)()
    y_1 = Y[1]
    y_0 = Y[0]
# WARNING: Decompyle incomplete


def dmp_fateman_poly_F_1(n, K):
    """Fateman's GCD benchmark: trivial GCD """
    u = [
        K(1),
        K(0)]
    for i in range(n):
        u = [
            dmp_one(i, K),
            u]
        v = [
            K(1),
            K(0),
            K(0)]
        for i in range(0, n):
            v = [
                dmp_one(i, K),
                dmp_zero(i),
                v]
            m = n - 1
            U = dmp_add_term(u, dmp_ground(K(1), m), 0, n, K)
            V = dmp_add_term(u, dmp_ground(K(2), m), 0, n, K)
            f = [
                [
                    -K(3),
                    K(0)],
                [],
                [
                    K(1),
                    K(0),
                    -K(1)]]
            W = dmp_add_term(v, dmp_ground(K(1), m), 0, n, K)
            Y = dmp_raise(f, m, 1, K)
            F = dmp_mul(U, V, n, K)
            G = dmp_mul(W, Y, n, K)
            H = dmp_one(n, K)
            return (F, G, H)


def fateman_poly_F_2(n):
    """Fateman's GCD benchmark: linearly dense quartic inputs """
    Y = range(n + 1)()
    y_0 = Y[0]
# WARNING: Decompyle incomplete


def dmp_fateman_poly_F_2(n, K):
    """Fateman's GCD benchmark: linearly dense quartic inputs """
    u = [
        K(1),
        K(0)]
    for i in range(n - 1):
        u = [
            dmp_one(i, K),
            u]
        m = n - 1
        v = dmp_add_term(u, dmp_ground(K(2), m - 1), 0, n, K)
        f = dmp_sqr([
            dmp_one(m, K),
            dmp_neg(v, m, K)], n, K)
        g = dmp_sqr([
            dmp_one(m, K),
            v], n, K)
        v = dmp_add_term(u, dmp_one(m - 1, K), 0, n, K)
        h = dmp_sqr([
            dmp_one(m, K),
            v], n, K)
        return (dmp_mul(f, h, n, K), dmp_mul(g, h, n, K), h)


def fateman_poly_F_3(n):
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
    pass
# WARNING: Decompyle incomplete


def dmp_fateman_poly_F_3(n, K):
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
    u = dup_from_raw_dict({
        n + 1: K.one }, K)
    for i in range(0, n - 1):
        u = dmp_add_term([
            u], dmp_one(i, K), n + 1, i + 1, K)
        v = dmp_add_term(u, dmp_ground(K(2), n - 2), 0, n, K)
        f = dmp_sqr(dmp_add_term([
            dmp_neg(v, n - 1, K)], dmp_one(n - 1, K), n + 1, n, K), n, K)
        g = dmp_sqr(dmp_add_term([
            v], dmp_one(n - 1, K), n + 1, n, K), n, K)
        v = dmp_add_term(u, dmp_one(n - 2, K), 0, n - 1, K)
        h = dmp_sqr(dmp_add_term([
            v], dmp_one(n - 1, K), n + 1, n, K), n, K)
        return (dmp_mul(f, h, n, K), dmp_mul(g, h, n, K), h)

from sympy.polys.rings import ring

def _f_0():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return x ** 2 * y * z ** 2 + 2 * x ** 2 * y * z + 3 * x ** 2 * y + 2 * x ** 2 + 3 * x + 4 * y ** 2 * z ** 2 + 5 * y ** 2 * z + 6 * y ** 2 + y * z ** 2 + 2 * y * z + y + 1


def _f_1():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return x ** 3 * y * z + x ** 2 * y ** 2 * z ** 2 + x ** 2 * y ** 2 + 20 * x ** 2 * y * z + 30 * x ** 2 * y + x ** 2 * z ** 2 + 10 * x ** 2 * z + x * y ** 3 * z + 30 * x * y ** 2 * z + 20 * x * y ** 2 + x * y * z ** 3 + 10 * x * y * z ** 2 + x * y * z + 610 * x * y + 20 * x * z ** 2 + 230 * x * z + 300 * x + y ** 2 * z ** 2 + 10 * y ** 2 * z + 30 * y * z ** 2 + 320 * y * z + 200 * y + 600 * z + 6000


def _f_2():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return (((x ** 5 * y ** 3 + x ** 5 * y ** 2 * z + x ** 5 * y * z ** 2 + x ** 5 * z ** 3 + x ** 3 * y ** 2 + x ** 3 * y * z + 90 * x ** 3 * y + 90 * x ** 3 * z + x ** 2 * y ** 2 * z - 11 * x ** 2 * y ** 2) + x ** 2 * z ** 3 - 11 * x ** 2 * z ** 2) + y * z - 11 * y) + 90 * z - 990


def _f_3():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return x ** 5 * y ** 2 + x ** 4 * z ** 4 + x ** 4 + x ** 3 * y ** 3 * z + x ** 3 * z + x ** 2 * y ** 4 + x ** 2 * y ** 3 * z ** 3 + x ** 2 * y * z ** 5 + x ** 2 * y * z + x * y ** 2 * z ** 4 + x * y ** 2 + x * y * z ** 7 + x * y * z ** 3 + x * y * z ** 2 + y ** 2 * z + y * z ** 4


def _f_4():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return (((((((-x ** 9 * y ** 8 * z - x ** 8 * y ** 5 * z ** 3 - x ** 7 * y ** 12 * z ** 2 - 5 * x ** 7 * y ** 8 - x ** 6 * y ** 9 * z ** 4) + x ** 6 * y ** 7 * z ** 3 + 3 * x ** 6 * y ** 7 * z - 5 * x ** 6 * y ** 5 * z ** 2 - x ** 6 * y ** 4 * z ** 3) + x ** 5 * y ** 4 * z ** 5 + 3 * x ** 5 * y ** 4 * z ** 3 - x ** 5 * y * z ** 5) + x ** 4 * y ** 11 * z ** 4 + 3 * x ** 4 * y ** 11 * z ** 2 - x ** 4 * y ** 8 * z ** 4) + 5 * x ** 4 * y ** 7 * z ** 2 + 15 * x ** 4 * y ** 7 - 5 * x ** 4 * y ** 4 * z ** 2) + x ** 3 * y ** 8 * z ** 6 + 3 * x ** 3 * y ** 8 * z ** 4 - x ** 3 * y ** 5 * z ** 6) + 5 * x ** 3 * y ** 4 * z ** 4 + 15 * x ** 3 * y ** 4 * z ** 2 + x ** 3 * y ** 3 * z ** 5 + 3 * x ** 3 * y ** 3 * z ** 3 - 5 * x ** 3 * y * z ** 4) + x ** 2 * z ** 7 + 3 * x ** 2 * z ** 5 + x * y ** 7 * z ** 6 + 3 * x * y ** 7 * z ** 4 + 5 * x * y ** 3 * z ** 4 + 15 * x * y ** 3 * z ** 2 + y ** 4 * z ** 8 + 3 * y ** 4 * z ** 6 + 5 * z ** 6 + 15 * z ** 4


def _f_5():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return ((((-x ** 3 - 3 * x ** 2 * y) + 3 * x ** 2 * z - 3 * x * y ** 2) + 6 * x * y * z - 3 * x * z ** 2 - y ** 3) + 3 * y ** 2 * z - 3 * y * z ** 2) + z ** 3


def _f_6():
    (R, x, y, z, t) = ring('x,y,z,t', ZZ)
    return (((2115 * x ** 4 * y + 45 * x ** 3 * z ** 3 * t ** 2 - 45 * x ** 3 * t ** 2 - 423 * x * y ** 4 - 47 * x * y ** 3) + 141 * x * y * z ** 3 + 94 * x * y * z * t - 9 * y ** 3 * z ** 3 * t ** 2) + 9 * y ** 3 * t ** 2 - y ** 2 * z ** 3 * t ** 2) + y ** 2 * t ** 2 + 3 * z ** 6 * t ** 2 + 2 * z ** 4 * t ** 3 - 3 * z ** 3 * t ** 2 - 2 * z * t ** 3


def _w_1():
    (R, x, y, z) = ring('x,y,z', ZZ)
    return ((((((((((((4 * x ** 6 * y ** 4 * z ** 2 + 4 * x ** 6 * y ** 3 * z ** 3 - 4 * x ** 6 * y ** 2 * z ** 4 - 4 * x ** 6 * y * z ** 5) + x ** 5 * y ** 4 * z ** 3 + 12 * x ** 5 * y ** 3 * z - x ** 5 * y ** 2 * z ** 5) + 12 * x ** 5 * y ** 2 * z ** 2 - 12 * x ** 5 * y * z ** 3 - 12 * x ** 5 * z ** 4) + 8 * x ** 4 * y ** 4 + 6 * x ** 4 * y ** 3 * z ** 2 + 8 * x ** 4 * y ** 3 * z - 4 * x ** 4 * y ** 2 * z ** 4) + 4 * x ** 4 * y ** 2 * z ** 3 - 8 * x ** 4 * y ** 2 * z ** 2 - 4 * x ** 4 * y * z ** 5 - 2 * x ** 4 * y * z ** 4 - 8 * x ** 4 * y * z ** 3) + 2 * x ** 3 * y ** 4 * z + x ** 3 * y ** 3 * z ** 3 - x ** 3 * y ** 2 * z ** 5 - 2 * x ** 3 * y ** 2 * z ** 3) + 9 * x ** 3 * y ** 2 * z - 12 * x ** 3 * y * z ** 3) + 12 * x ** 3 * y * z ** 2 - 12 * x ** 3 * z ** 4) + 3 * x ** 3 * z ** 3 + 6 * x ** 2 * y ** 3 - 6 * x ** 2 * y ** 2 * z ** 2) + 8 * x ** 2 * y ** 2 * z - 2 * x ** 2 * y * z ** 4 - 8 * x ** 2 * y * z ** 3) + 2 * x ** 2 * y * z ** 2 + 2 * x * y ** 3 * z - 2 * x * y ** 2 * z ** 3 - 3 * x * y * z) + 3 * x * z ** 3 - 2 * y ** 2) + 2 * y * z ** 2


def _w_2():
    (R, x, y) = ring('x,y', ZZ)
    return (((((24 * x ** 8 * y ** 3 + 48 * x ** 8 * y ** 2 + 24 * x ** 7 * y ** 5 - 72 * x ** 7 * y ** 2) + 25 * x ** 6 * y ** 4 + 2 * x ** 6 * y ** 3 + 4 * x ** 6 * y + 8 * x ** 6 + x ** 5 * y ** 6 + x ** 5 * y ** 3 - 12 * x ** 5) + x ** 4 * y ** 5 - x ** 4 * y ** 4 - 2 * x ** 4 * y ** 3) + 292 * x ** 4 * y ** 2 - x ** 3 * y ** 6) + 3 * x ** 3 * y ** 3 - x ** 2 * y ** 5) + 12 * x ** 2 * y ** 3 + 48 * x ** 2 - 12 * y ** 3


def f_polys():
    return (_f_0(), _f_1(), _f_2(), _f_3(), _f_4(), _f_5(), _f_6())


def w_polys():
    return (_w_1(), _w_2())
