# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parametricregion.pyc (Python 3.11)

from functools import singledispatch
from sympy.core.numbers import pi
from sympy.functions.elementary.trigonometric import tan
from sympy.simplify import trigsimp
from sympy.core import Basic, Tuple
from sympy.core.symbol import _symbol
from sympy.solvers import solve
from sympy.geometry import Point, Segment, Curve, Ellipse, Polygon
from sympy.vector import ImplicitRegion

class ParametricRegion(Basic):
    pass
# WARNING: Decompyle incomplete

parametric_region_list = (lambda reg: raise ValueError('SymPy cannot determine parametric representation of the region.'))()
_ = (lambda obj: [
ParametricRegion(obj.args)])()
_ = (lambda obj: definition = obj.arbitrary_point(obj.parameter).argsbounds = obj.limits[
ParametricRegion(definition, bounds)])()
_ = (lambda obj, parameter = ('t',): definition = obj.arbitrary_point(parameter).argst = _symbol(parameter, real = True)bounds = (t, 0, 2 * pi)[
ParametricRegion(definition, bounds)])()
_ = (lambda obj, parameter = ('t',): t = _symbol(parameter, real = True)definition = obj.arbitrary_point(t).argsfor i in range(0, 3):
lower_bound = solve(definition[i] - obj.points[0].args[i], t)upper_bound = solve(definition[i] - obj.points[1].args[i], t)if len(lower_bound) == 1 and len(upper_bound) == 1:
bounds = (t, lower_bound[0], upper_bound[0])definition_tuple = obj.arbitrary_point(parameter).args[
ParametricRegion(definition_tuple, bounds)])()
_ = (lambda obj, parameter = ('t',): pass# WARNING: Decompyle incomplete
)()
_ = (lambda obj, parameters = (('t', 's'),): pass# WARNING: Decompyle incomplete
)()
