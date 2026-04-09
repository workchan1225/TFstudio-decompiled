# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mathdecl.pyc (Python 3.11)

import math
import sys
from numba.core import types, utils
from numba.core.typing.templates import AttributeTemplate, ConcreteTemplate, signature, Registry
registry = Registry()
infer_global = registry.register_global
Math_unary = <NODE:12>()()()()()()()()()()()()()()()()()()()()()()()()()()
if sys.version_info >= (3, 11):
    Math_unary = infer_global(math.exp2)(Math_unary)
Math_atan2 = <NODE:12>()
Math_converter = <NODE:12>()
Math_floor_ceil = <NODE:12>()()
Math_copysign = <NODE:12>()
Math_hypot = <NODE:12>()
Math_nextafter = <NODE:12>()
Math_predicate = <NODE:12>()()
Math_isfinite = <NODE:12>()
Math_pow = <NODE:12>()
Math_gcd = <NODE:12>()
Math_frexp = <NODE:12>()
Math_ldexp = <NODE:12>()
