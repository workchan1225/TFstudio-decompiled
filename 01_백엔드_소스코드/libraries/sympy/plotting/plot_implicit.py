# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_implicit.pyc (Python 3.11)

"""Implicit plotting module for SymPy.

Explanation
===========

The module implements a data series called ImplicitSeries which is used by
``Plot`` class to plot implicit plots for different backends. The module,
by default, implements plotting using interval arithmetic. It switches to a
fall back algorithm if the expression cannot be plotted using interval arithmetic.
It is also possible to specify to use the fall back algorithm for all plots.

Boolean combinations of expressions cannot be plotted by the fall back
algorithm.

See Also
========

sympy.plotting.plot

References
==========

.. [1] Jeffrey Allen Tupper. Reliable Two-Dimensional Graphing Methods for
Mathematical Formulae with Two Free Variables.

.. [2] Jeffrey Allen Tupper. Graphing Equations with Generalized Interval
Arithmetic. Master's thesis. University of Toronto, 1996

"""
from sympy.core.containers import Tuple
from sympy.core.symbol import Dummy, Symbol
from sympy.polys.polyutils import _sort_gens
from sympy.plotting.series import ImplicitSeries, _set_discretization_points
from sympy.plotting.plot import plot_factory
from sympy.utilities.decorator import doctest_depends_on
from sympy.utilities.iterables import flatten
__doctest_requires__ = {
    'plot_implicit': [
        'matplotlib'] }
plot_implicit = (lambda expr, x_var, y_var, adaptive, depth, n, line_color, show = (None, None, True, 0, 300, 'blue', True): pass# WARNING: Decompyle incomplete
)()
