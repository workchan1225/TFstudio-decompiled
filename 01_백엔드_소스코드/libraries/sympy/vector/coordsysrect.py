# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coordsysrect.pyc (Python 3.11)

from collections.abc import Callable
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core import S, Dummy, Lambda
from sympy.core.symbol import Str
from sympy.core.symbol import symbols
from sympy.matrices.immutable import ImmutableDenseMatrix as Matrix
from sympy.matrices.matrixbase import MatrixBase
from sympy.solvers import solve
from sympy.vector.scalar import BaseScalar
from sympy.core.containers import Tuple
from sympy.core.function import diff
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import acos, atan2, cos, sin
from sympy.matrices.dense import eye
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.simplify.simplify import simplify
from sympy.simplify.trigsimp import trigsimp
import sympy.vector as sympy
from sympy.vector.orienters import Orienter, AxisOrienter, BodyOrienter, SpaceOrienter, QuaternionOrienter

class CoordSys3D(Basic):
    pass
# WARNING: Decompyle incomplete


def _check_strings(arg_name, arg):
    errorstr = arg_name + ' must be an iterable of 3 string-types'
    if len(arg) != 3:
        raise ValueError(errorstr)
    for s in arg:
        if not isinstance(s, str):
            raise TypeError(errorstr)
        return None

from sympy.vector.vector import BaseVector
