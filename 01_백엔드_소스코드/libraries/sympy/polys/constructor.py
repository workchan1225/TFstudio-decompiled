# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constructor.pyc (Python 3.11)

'''Tools for constructing domains for expressions. '''
from math import prod
from sympy.core import sympify
from sympy.core.evalf import pure_complex
from sympy.core.sorting import ordered
from sympy.polys.domains import ZZ, QQ, ZZ_I, QQ_I, EX
from sympy.polys.domains.complexfield import ComplexField
from sympy.polys.domains.realfield import RealField
from sympy.polys.polyoptions import build_options
from sympy.polys.polyutils import parallel_dict_from_basic
from sympy.utilities import public

def _construct_simple(coeffs, opt):
    '''Handle simple domains, e.g.: ZZ, QQ, RR and algebraic domains. '''
    pass
# WARNING: Decompyle incomplete


def _construct_algebraic(coeffs, opt):
    '''We know that coefficients are algebraic so construct the extension. '''
    pass
# WARNING: Decompyle incomplete


def _construct_composite(coeffs, opt):
    '''Handle composite domains, e.g.: ZZ[X], QQ[X], ZZ(X), QQ(X). '''
    denoms = []
    numers = []
# WARNING: Decompyle incomplete


def _construct_expression(coeffs, opt):
    '''The last resort case, i.e. use the expression domain. '''
    result = []
    domain = EX
    for coeff in coeffs:
        result.append(domain.from_sympy(coeff))
        return (domain, result)

construct_domain = (lambda obj: opt = build_options(args)# WARNING: Decompyle incomplete
)()
