# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quaternion.pyc (Python 3.11)

from sympy.core.numbers import Rational
from sympy.core.singleton import S
from sympy.core.relational import is_eq
from sympy.functions.elementary.complexes import conjugate, im, re, sign
from sympy.functions.elementary.exponential import exp, log as ln
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import acos, asin, atan2
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.simplify.trigsimp import trigsimp
from sympy.integrals.integrals import integrate
from sympy.matrices.dense import MutableDenseMatrix as Matrix
from sympy.core.sympify import sympify, _sympify
from sympy.core.expr import Expr
from sympy.core.logic import fuzzy_not, fuzzy_or
from sympy.utilities.misc import as_int
from mpmath.libmp.libmpf import prec_to_dps

def _check_norm(elements, norm):
    '''validate if input norm is consistent'''
    pass
# WARNING: Decompyle incomplete


def _is_extrinsic(seq):
    '''validate seq and return True if seq is lowercase and False if uppercase'''
    if type(seq) != str:
        raise ValueError('Expected seq to be a string.')
    if len(seq) != 3:
        raise ValueError('Expected 3 axes, got `{}`.'.format(seq))
    intrinsic = seq.isupper()
    extrinsic = seq.islower()
    if not intrinsic and extrinsic:
        raise ValueError('seq must either be fully uppercase (for extrinsic rotations), or fully lowercase, for intrinsic rotations).')
    (i, j, k) = seq.lower()
    if i == j or j == k:
        raise ValueError('Consecutive axes must be different')
    bad = set(seq) - set('xyzXYZ')
    if bad:
        raise ValueError("Expected axes from `seq` to be from ['x', 'y', 'z'] or ['X', 'Y', 'Z'], got {}".format(''.join(bad)))
    return extrinsic


class Quaternion(Expr):
    pass
# WARNING: Decompyle incomplete
