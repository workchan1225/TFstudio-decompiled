# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matrices.pyc (Python 3.11)

'''Known matrices related to physics'''
from sympy.core.numbers import I
from sympy.matrices.dense import MutableDenseMatrix as Matrix
from sympy.utilities.decorator import deprecated

def msigma(i):
    '''Returns a Pauli matrix `\\sigma_i` with `i=1,2,3`.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pauli_matrices

    Examples
    ========

    >>> from sympy.physics.matrices import msigma
    >>> msigma(1)
    Matrix([
    [0, 1],
    [1, 0]])
    '''
    if i == 1:
        mat = ((0, 1), (1, 0))
    elif i == 2:
        mat = ((0, -I), (I, 0))
    elif i == 3:
        mat = ((1, 0), (0, -1))
    else:
        raise IndexError('Invalid Pauli index')
    return Matrix(mat)


def pat_matrix(m, dx, dy, dz):
    '''Returns the Parallel Axis Theorem matrix to translate the inertia
    matrix a distance of `(dx, dy, dz)` for a body of mass m.

    Examples
    ========

    To translate a body having a mass of 2 units a distance of 1 unit along
    the `x`-axis we get:

    >>> from sympy.physics.matrices import pat_matrix
    >>> pat_matrix(2, 1, 0, 0)
    Matrix([
    [0, 0, 0],
    [0, 2, 0],
    [0, 0, 2]])

    '''
    dxdy = -dx * dy
    dydz = -dy * dz
    dzdx = -dz * dx
    dxdx = dx ** 2
    dydy = dy ** 2
    dzdz = dz ** 2
    mat = ((dydy + dzdz, dxdy, dzdx), (dxdy, dxdx + dzdz, dydz), (dzdx, dydz, dydy + dxdx))
    return m * Matrix(mat)


def mgamma(mu, lower = (False,)):
    '''Returns a Dirac gamma matrix `\\gamma^\\mu` in the standard
    (Dirac) representation.

    Explanation
    ===========

    If you want `\\gamma_\\mu`, use ``gamma(mu, True)``.

    We use a convention:

    `\\gamma^5 = i \\cdot \\gamma^0 \\cdot \\gamma^1 \\cdot \\gamma^2 \\cdot \\gamma^3`

    `\\gamma_5 = i \\cdot \\gamma_0 \\cdot \\gamma_1 \\cdot \\gamma_2 \\cdot \\gamma_3 = - \\gamma^5`

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_matrices

    Examples
    ========

    >>> from sympy.physics.matrices import mgamma
    >>> mgamma(1)
    Matrix([
    [ 0,  0, 0, 1],
    [ 0,  0, 1, 0],
    [ 0, -1, 0, 0],
    [-1,  0, 0, 0]])
    '''
    if mu not in (0, 1, 2, 3, 5):
        raise IndexError('Invalid Dirac index')
    if mu == 0:
        mat = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1))
    elif mu == 1:
        mat = ((0, 0, 0, 1), (0, 0, 1, 0), (0, -1, 0, 0), (-1, 0, 0, 0))
    elif mu == 2:
        mat = ((0, 0, 0, -I), (0, 0, I, 0), (0, I, 0, 0), (-I, 0, 0, 0))
    elif mu == 3:
        mat = ((0, 0, 1, 0), (0, 0, 0, -1), (-1, 0, 0, 0), (0, 1, 0, 0))
    elif mu == 5:
        mat = ((0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0))
    m = Matrix(mat)
    if lower and mu in (1, 2, 3, 5):
        m = -m
    return m

minkowski_tensor = Matrix(((1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)))
mdft = (lambda n: DFT = DFTimport sympy.matrices.expressions.fourierDFT(n).as_mutable())()
