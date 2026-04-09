# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rref.pyc (Python 3.11)

from sympy.polys.domains import ZZ
from sympy.polys.matrices.sdm import SDM, sdm_irref, sdm_rref_den
from sympy.polys.matrices.ddm import DDM
from sympy.polys.matrices.dense import ddm_irref, ddm_irref_den

def _dm_rref(M = None, *, method):
    '''
    Compute the reduced row echelon form of a ``DomainMatrix``.

    This function is the implementation of :meth:`DomainMatrix.rref`.

    Chooses the best algorithm depending on the domain, shape, and sparsity of
    the matrix as well as things like the bit count in the case of :ref:`ZZ` or
    :ref:`QQ`. The result is returned over the field associated with the domain
    of the Matrix.

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.rref
        The ``DomainMatrix`` method that calls this function.
    sympy.polys.matrices.rref._dm_rref_den
        Alternative function for computing RREF with denominator.
    '''
    (method, use_fmt) = _dm_rref_choose_method(M, method, denominator = False)
    (M, old_fmt) = _dm_to_fmt(M, use_fmt)
    if method == 'GJ':
        Mf = _to_field(M)
        (M_rref, pivots) = _dm_rref_GJ(Mf)
    elif method == 'FF':
        (M_rref_f, den, pivots) = _dm_rref_den_FF(M)
        M_rref = _to_field(M_rref_f) / den
    elif method == 'CD':
        (_, Mr) = M.clear_denoms_rowwise(convert = True)
        (M_rref_f, den, pivots) = _dm_rref_den_FF(Mr)
        M_rref = _to_field(M_rref_f) / den
    else:
        raise ValueError(f'''Unknown method for rref: {method}''')
    (M_rref, _) = _dm_to_fmt(M_rref, old_fmt)
    return (M_rref, pivots)


def _dm_rref_den(M = None, *, keep_domain, method):
    '''
    Compute the reduced row echelon form of a ``DomainMatrix`` with denominator.

    This function is the implementation of :meth:`DomainMatrix.rref_den`.

    Chooses the best algorithm depending on the domain, shape, and sparsity of
    the matrix as well as things like the bit count in the case of :ref:`ZZ` or
    :ref:`QQ`. The result is returned over the same domain as the input matrix
    unless ``keep_domain=False`` in which case the result might be over an
    associated ring or field domain.

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.rref_den
        The ``DomainMatrix`` method that calls this function.
    sympy.polys.matrices.rref._dm_rref
        Alternative function for computing RREF without denominator.
    '''
    (method, use_fmt) = _dm_rref_choose_method(M, method, denominator = True)
    (M, old_fmt) = _dm_to_fmt(M, use_fmt)
    if method == 'FF':
        (M_rref, den, pivots) = _dm_rref_den_FF(M)
    elif method == 'GJ':
        (M_rref_f, pivots) = _dm_rref_GJ(_to_field(M))
        if keep_domain and M_rref_f.domain != M.domain:
            (_, M_rref) = M_rref_f.clear_denoms(convert = True)
            if pivots:
                den = M_rref[(0, pivots[0])].element
            else:
                den = M_rref.domain.one
        else:
            M_rref = M_rref_f
            den = M_rref.domain.one
    elif method == 'CD':
        (_, Mr) = M.clear_denoms_rowwise(convert = True)
        (M_rref_r, den, pivots) = _dm_rref_den_FF(Mr)
        if keep_domain and M_rref_r.domain != M.domain:
            M_rref = _to_field(M_rref_r) / den
            den = M.domain.one
        else:
            M_rref = M_rref_r
            if pivots:
                den = M_rref[(0, pivots[0])].element
            else:
                den = M_rref.domain.one
    else:
        raise ValueError(f'''Unknown method for rref: {method}''')
    (M_rref, _) = _dm_to_fmt(M_rref, old_fmt)
    return (M_rref, den, pivots)


def _dm_to_fmt(M, fmt):
    '''Convert a matrix to the given format and return the old format.'''
    old_fmt = M.rep.fmt
    if old_fmt == fmt:
        pass
    elif fmt == 'dense':
        M = M.to_dense()
    elif fmt == 'sparse':
        M = M.to_sparse()
    else:
        raise ValueError(f'''Unknown format: {fmt}''')
    return (M, old_fmt)


def _dm_rref_GJ(M):
    '''Compute RREF using Gauss-Jordan elimination with division.'''
    if M.rep.fmt == 'sparse':
        return _dm_rref_GJ_sparse(M)
    return None(M)


def _dm_rref_den_FF(M):
    '''Compute RREF using fraction-free Gauss-Jordan elimination.'''
    if M.rep.fmt == 'sparse':
        return _dm_rref_den_FF_sparse(M)
    return None(M)


def _dm_rref_GJ_sparse(M):
    '''Compute RREF using sparse Gauss-Jordan elimination with division.'''
    (M_rref_d, pivots, _) = sdm_irref(M.rep)
    M_rref_sdm = SDM(M_rref_d, M.shape, M.domain)
    pivots = tuple(pivots)
    return (M.from_rep(M_rref_sdm), pivots)


def _dm_rref_GJ_dense(M):
