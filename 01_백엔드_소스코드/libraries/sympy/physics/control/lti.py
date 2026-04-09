# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lti.pyc (Python 3.11)

from typing import Type
from sympy import Interval, numer, Rational, solveset
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.evalf import EvalfMixin
from sympy.core.expr import Expr
from sympy.core.function import expand
from sympy.core.logic import fuzzy_and
from sympy.core.mul import Mul
from sympy.core.numbers import I, pi, oo
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, Symbol
from sympy.functions import Abs
from sympy.core.sympify import sympify, _sympify
from sympy.matrices import Matrix, ImmutableMatrix, ImmutableDenseMatrix, eye, ShapeError, zeros
from sympy.functions.elementary.exponential import exp, log
from sympy.matrices.expressions import MatMul, MatAdd
from sympy.polys import Poly, rootof
from sympy.polys.polyroots import roots
from sympy.polys.polytools import cancel, degree
from sympy.series import limit
from sympy.utilities.misc import filldedent
from mpmath.libmp.libmpf import prec_to_dps
__all__ = [
    'TransferFunction',
    'Series',
    'MIMOSeries',
    'Parallel',
    'MIMOParallel',
    'Feedback',
    'MIMOFeedback',
    'TransferFunctionMatrix',
    'StateSpace',
    'gbt',
    'bilinear',
    'forward_diff',
    'backward_diff',
    'phase_margin',
    'gain_margin']

def _roots(poly, var):
    ''' like roots, but works on higher-order polynomials. '''
    pass
# WARNING: Decompyle incomplete


def gbt(tf, sample_per, alpha):
    '''
    Returns falling coefficients of H(z) from numerator and denominator.

    Explanation
    ===========

    Where H(z) is the corresponding discretized transfer function,
    discretized with the generalised bilinear transformation method.
    H(z) is obtained from the continuous transfer function H(s)
    by substituting $s(z) = \\frac{z-1}{T(\\alpha z + (1-\\alpha))}$ into H(s), where T is the
    sample period.
    Coefficients are falling, i.e. $H(z) = \\frac{az+b}{cz+d}$ is returned
    as [a, b], [c, d].

    Examples
    ========

    >>> from sympy.physics.control.lti import TransferFunction, gbt
    >>> from sympy.abc import s, L, R, T

    >>> tf = TransferFunction(1, s*L + R, s)
    >>> numZ, denZ = gbt(tf, T, 0.5)
    >>> numZ
    [T/(2*(L + R*T/2)), T/(2*(L + R*T/2))]
    >>> denZ
    [1, (-L + R*T/2)/(L + R*T/2)]

    >>> numZ, denZ = gbt(tf, T, 0)
    >>> numZ
    [T/L]
    >>> denZ
    [1, (-L + R*T)/L]

    >>> numZ, denZ = gbt(tf, T, 1)
    >>> numZ
    [T/(L + R*T), 0]
    >>> denZ
    [1, -L/(L + R*T)]

    >>> numZ, denZ = gbt(tf, T, 0.3)
    >>> numZ
    [3*T/(10*(L + 3*R*T/10)), 7*T/(10*(L + 3*R*T/10))]
    >>> denZ
    [1, (-L + 7*R*T/10)/(L + 3*R*T/10)]

    References
    ==========

    .. [1] https://www.polyu.edu.hk/ama/profile/gfzhang/Research/ZCC09_IJC.pdf
    '''
    pass
# WARNING: Decompyle incomplete


def bilinear(tf, sample_per):
    '''
    Returns falling coefficients of H(z) from numerator and denominator.

    Explanation
    ===========

    Where H(z) is the corresponding discretized transfer function,
    discretized with the bilinear transform method.
    H(z) is obtained from the continuous transfer function H(s)
    by substituting $s(z) = \\frac{2}{T}\\frac{z-1}{z+1}$ into H(s), where T is the
    sample period.
    Coefficients are falling, i.e. $H(z) = \\frac{az+b}{cz+d}$ is returned
    as [a, b], [c, d].

    Examples
    ========

    >>> from sympy.physics.control.lti import TransferFunction, bilinear
    >>> from sympy.abc import s, L, R, T

    >>> tf = TransferFunction(1, s*L + R, s)
    >>> numZ, denZ = bilinear(tf, T)
    >>> numZ
    [T/(2*(L + R*T/2)), T/(2*(L + R*T/2))]
    >>> denZ
    [1, (-L + R*T/2)/(L + R*T/2)]
    '''
    return gbt(tf, sample_per, S.Half)


def forward_diff(tf, sample_per):
    '''
    Returns falling coefficients of H(z) from numerator and denominator.

    Explanation
    ===========

    Where H(z) is the corresponding discretized transfer function,
    discretized with the forward difference transform method.
    H(z) is obtained from the continuous transfer function H(s)
    by substituting $s(z) = \\frac{z-1}{T}$ into H(s), where T is the
    sample period.
    Coefficients are falling, i.e. $H(z) = \\frac{az+b}{cz+d}$ is returned
    as [a, b], [c, d].

    Examples
    ========

    >>> from sympy.physics.control.lti import TransferFunction, forward_diff
    >>> from sympy.abc import s, L, R, T

    >>> tf = TransferFunction(1, s*L + R, s)
    >>> numZ, denZ = forward_diff(tf, T)
    >>> numZ
    [T/L]
    >>> denZ
    [1, (-L + R*T)/L]
    '''
    return gbt(tf, sample_per, S.Zero)


def backward_diff(tf, sample_per):
    '''
    Returns falling coefficients of H(z) from numerator and denominator.

    Explanation
    ===========

    Where H(z) is the corresponding discretized transfer function,
    discretized with the backward difference transform method.
    H(z) is obtained from the continuous transfer function H(s)
    by substituting $s(z) =  \\frac{z-1}{Tz}$ into H(s), where T is the
    sample period.
    Coefficients are falling, i.e. $H(z) = \\frac{az+b}{cz+d}$ is returned
    as [a, b], [c, d].

    Examples
    ========

    >>> from sympy.physics.control.lti import TransferFunction, backward_diff
    >>> from sympy.abc import s, L, R, T

    >>> tf = TransferFunction(1, s*L + R, s)
    >>> numZ, denZ = backward_diff(tf, T)
    >>> numZ
    [T/(L + R*T), 0]
    >>> denZ
    [1, -L/(L + R*T)]
    '''
    return gbt(tf, sample_per, S.One)


def phase_margin(system):
    '''
    Returns the phase margin of a continuous time system.
    Only applicable to Transfer Functions which can generate valid bode plots.

    Raises
    ======

    NotImplementedError
        When time delay terms are present in the system.

    ValueError
        When a SISO LTI system is not passed.

        When more than one free symbol is present in the system.
        The only variable in the transfer function should be
        the variable of the Laplace transform.

    Examples
    ========

    >>> from sympy.physics.control import TransferFunction, phase_margin
    >>> from sympy.abc import s

    >>> tf = TransferFunction(1, s**3 + 2*s**2 + s, s)
    >>> phase_margin(tf)
    180*(-pi + atan((-1 + (-2*18**(1/3)/(9 + sqrt(93))**(1/3) + 12**(1/3)*(9 + sqrt(93))**(1/3))**2/36)/(-12**(1/3)*(9 + sqrt(93))**(1/3)/3 + 2*18**(1/3)/(3*(9 + sqrt(93))**(1/3)))))/pi + 180
    >>> phase_margin(tf).n()
    21.3863897518751

    >>> tf1 = TransferFunction(s**3, s**2 + 5*s, s)
    >>> phase_margin(tf1)
    -180 + 180*(atan(sqrt(2)*(-51/10 - sqrt(101)/10)*sqrt(1 + sqrt(101))/(2*(sqrt(101)/2 + 51/2))) + pi)/pi
    >>> phase_margin(tf1).n()
    -25.1783920627277

    >>> tf2 = TransferFunction(1, s + 1, s)
    >>> phase_margin(tf2)
    -180

    See Also
    ========

    gain_margin

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Phase_margin

    '''
    arg = arg
    import sympy.functions
    if not isinstance(system, SISOLinearTimeInvariant):
        raise ValueError('Margins are only applicable for SISO LTI systems.')
    _w = Dummy('w', real = True)
    repl = I * _w
    expr = system.to_expr()
    len_free_symbols = len(expr.free_symbols)
    if expr.has(exp):
        raise NotImplementedError('Margins for systems with Time delay terms are not supported.')
    if len_free_symbols > 1:
        raise ValueError('Extra degree of freedom found. Make sure that there are no free symbols in the dynamical system other than the variable of Laplace transform.')
    w_expr = expr.subs({
        system.var: repl })
    mag = 20 * log(Abs(w_expr), 10)
    mag_sol = list(solveset(mag, _w, Interval(0, oo, left_open = True)))
    if len(mag_sol) == 0:
        pm = S(-180)
    else:
        wcp = mag_sol[0]
        pm = ((arg(w_expr) * S(180) / pi).subs({
            _w: wcp }) + S(180)) % 360
    if pm >= 180:
        pm = pm - 360
    return pm


def gain_margin(system):
    '''
    Returns the gain margin of a continuous time system.
    Only applicable to Transfer Functions which can generate valid bode plots.

    Raises
    ======

    NotImplementedError
        When time delay terms are present in the system.

    ValueError
        When a SISO LTI system is not passed.

        When more than one free symbol is present in the system.
        The only variable in the transfer function should be
        the variable of the Laplace transform.

    Examples
    ========

    >>> from sympy.physics.control import TransferFunction, gain_margin
    >>> from sympy.abc import s

    >>> tf = TransferFunction(1, s**3 + 2*s**2 + s, s)
    >>> gain_margin(tf)
    20*log(2)/log(10)
    >>> gain_margin(tf).n()
    6.02059991327962

    >>> tf1 = TransferFunction(s**3, s**2 + 5*s, s)
    >>> gain_margin(tf1)
    oo

    See Also
    ========

    phase_margin

    References
    ==========

    https://en.wikipedia.org/wiki/Bode_plot

    '''
    if not isinstance(system, SISOLinearTimeInvariant):
        raise ValueError('Margins are only applicable for SISO LTI systems.')
    _w = Dummy('w', real = True)
    repl = I * _w
    expr = system.to_expr()
    len_free_symbols = len(expr.free_symbols)
    if expr.has(exp):
        raise NotImplementedError('Margins for systems with Time delay terms are not supported.')
    if len_free_symbols > 1:
        raise ValueError('Extra degree of freedom found. Make sure that there are no free symbols in the dynamical system other than the variable of Laplace transform.')
    w_expr = expr.subs({
        system.var: repl })
    mag = 20 * log(Abs(w_expr), 10)
    phase = w_expr
    phase_sol = list(solveset(numer(phase.as_real_imag()[1].cancel()), _w, Interval(0, oo, left_open = True)))
    if len(phase_sol) == 0:
        gm = oo
    else:
        wcg = phase_sol[0]
        gm = -mag.subs({
            _w: wcg })
    return gm


class LinearTimeInvariant(EvalfMixin, Basic):
    pass
# WARNING: Decompyle incomplete


class SISOLinearTimeInvariant(LinearTimeInvariant):
    '''A common class for all the SISO Linear Time-Invariant Dynamical Systems.'''
    _is_SISO = True


class MIMOLinearTimeInvariant(LinearTimeInvariant):
    '''A common class for all the MIMO Linear Time-Invariant Dynamical Systems.'''
    _is_SISO = False

SISOLinearTimeInvariant._clstype = SISOLinearTimeInvariant
MIMOLinearTimeInvariant._clstype = MIMOLinearTimeInvariant

def _check_other_SISO(func):
    pass
# WARNING: Decompyle incomplete


def _check_other_MIMO(func):
    pass
# WARNING: Decompyle incomplete


class TransferFunction(SISOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


def _flatten_args(args, _cls):
    temp_args = []
    for arg in args:
        if isinstance(arg, _cls):
            temp_args.extend(arg.args)
            continue
        temp_args.append(arg)
        return tuple(temp_args)


def _dummify_args(_arg, var):
    dummy_dict = { }
    dummy_arg_list = []
    for arg in _arg:
        _s = Dummy()
        dummy_dict[_s] = var
        dummy_arg = arg.subs({
            var: _s })
        dummy_arg_list.append(dummy_arg)
        return (dummy_arg_list, dummy_dict)


class Series(SISOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


def _mat_mul_compatible(*args):
    '''To check whether shapes are compatible for matrix mul.'''
    pass
# WARNING: Decompyle incomplete


class MIMOSeries(MIMOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


class Parallel(SISOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


class MIMOParallel(MIMOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


class Feedback(TransferFunction):
    pass
# WARNING: Decompyle incomplete


def _is_invertible(a, b, sign):
    '''
    Checks whether a given pair of MIMO
    systems passed is invertible or not.
    '''
    _mat = eye(a.num_outputs) - sign * a.doit()._expr_mat * b.doit()._expr_mat
    _det = _mat.det()
    return _det != 0


class MIMOFeedback(MIMOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


def _to_TFM(mat, var):
    '''Private method to convert ImmutableMatrix to TransferFunctionMatrix efficiently'''
    pass
# WARNING: Decompyle incomplete


class TransferFunctionMatrix(MIMOLinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete


class StateSpace(LinearTimeInvariant):
    pass
# WARNING: Decompyle incomplete
