# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyfuncs.pyc (Python 3.11)

'''High-level polynomials manipulation functions. '''
from sympy.core import S, Basic, symbols, Dummy
from sympy.polys.polyerrors import PolificationFailed, ComputationFailed, MultivariatePolynomialError, OptionError
from sympy.polys.polyoptions import allowed_flags, build_options
from sympy.polys.polytools import poly_from_expr, Poly
from sympy.polys.specialpolys import symmetric_poly, interpolating_poly
from sympy.polys.rings import sring
from sympy.utilities import numbered_symbols, take, public
symmetrize = (lambda F: pass# WARNING: Decompyle incomplete
)()
horner = (lambda f: allowed_flags(args, [])# WARNING: Decompyle incomplete
)()
interpolate = (lambda data, x: n = len(data)# WARNING: Decompyle incomplete
)()
rational_interpolate = (lambda data, degnum, X = (symbols('x'),): pass# WARNING: Decompyle incomplete
)()
viete = (lambda f, roots = (None,): allowed_flags(args, [])if isinstance(roots, Basic):
roots = Nonegens = (roots,) + gens# WARNING: Decompyle incomplete
)()
