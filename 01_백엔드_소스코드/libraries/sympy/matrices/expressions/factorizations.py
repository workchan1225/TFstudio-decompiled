# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: factorizations.pyc (Python 3.11)

from sympy.matrices.expressions import MatrixExpr
from sympy.assumptions.ask import Q

class Factorization(MatrixExpr):
    arg = property((lambda self: self.args[0]))
    shape = property((lambda self: self.arg.shape))


class LofLU(Factorization):
    predicates = (lambda self: (Q.lower_triangular,))()


class UofLU(Factorization):
    predicates = (lambda self: (Q.upper_triangular,))()


class LofCholesky(LofLU):
    pass


class UofCholesky(UofLU):
    pass


class QofQR(Factorization):
    predicates = (lambda self: (Q.orthogonal,))()


class RofQR(Factorization):
    predicates = (lambda self: (Q.upper_triangular,))()


class EigenVectors(Factorization):
    predicates = (lambda self: (Q.orthogonal,))()


class EigenValues(Factorization):
    predicates = (lambda self: (Q.diagonal,))()


class UofSVD(Factorization):
    predicates = (lambda self: (Q.orthogonal,))()


class SofSVD(Factorization):
    predicates = (lambda self: (Q.diagonal,))()


class VofSVD(Factorization):
    predicates = (lambda self: (Q.orthogonal,))()


def lu(expr):
    return (LofLU(expr), UofLU(expr))


def qr(expr):
    return (QofQR(expr), RofQR(expr))


def eig(expr):
    return (EigenValues(expr), EigenVectors(expr))


def svd(expr):
    return (UofSVD(expr), SofSVD(expr), VofSVD(expr))
