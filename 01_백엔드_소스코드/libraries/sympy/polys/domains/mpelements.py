# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mpelements.pyc (Python 3.11)

'''Real and complex elements. '''
from sympy.external.gmpy import MPQ
from sympy.polys.domains.domainelement import DomainElement
from sympy.utilities import public
from mpmath.ctx_mp_python import PythonMPContext, _mpf, _mpc, _constant
from mpmath.libmp import MPZ_ONE, fzero, fone, finf, fninf, fnan, round_nearest, mpf_mul, repr_dps, int_types, from_int, from_float, from_str, to_rational
RealElement = <NODE:12>()
ComplexElement = <NODE:12>()
new = object.__new__
MPContext = <NODE:12>()
