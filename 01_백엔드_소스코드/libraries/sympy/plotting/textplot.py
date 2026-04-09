# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: textplot.pyc (Python 3.11)

from sympy.core.numbers import Float
from sympy.core.symbol import Dummy
from sympy.utilities.lambdify import lambdify
import math

def is_valid(x):
    '''Check if a floating point number is valid'''
    pass
# WARNING: Decompyle incomplete


def rescale(y, W, H, mi, ma):
    '''Rescale the given array `y` to fit into the integer values
    between `0` and `H-1` for the values between ``mi`` and ``ma``.
    '''
    y_new = []
    norm = ma - mi
    offset = (ma + mi) / 2
    for x in range(W):
        if is_valid(y[x]):
            normalized = (y[x] - offset) / norm
            if not is_valid(normalized):
                y_new.append(None)
                continue
            rescaled = Float((normalized * H + H / 2) * (H - 1) / H).round()
            rescaled = int(rescaled)
            y_new.append(rescaled)
            continue
        y_new.append(None)
        return y_new


def linspace(start, stop, num):
    pass
# WARNING: Decompyle incomplete


def textplot_str(expr, a, b, W, H = (55, 21)):
    '''Generator for the lines of the plot'''
    pass
# WARNING: Decompyle incomplete


def textplot(expr, a, b, W, H = (55, 21)):
    """
    Print a crude ASCII art plot of the SymPy expression 'expr' (which
    should contain a single symbol, e.g. x or something else) over the
    interval [a, b].

    Examples
    ========

    >>> from sympy import Symbol, sin
    >>> from sympy.plotting import textplot
    >>> t = Symbol('t')
    >>> textplot(sin(t)*t, 0, 15)
     14 |                                                  ...
        |                                                     .
        |                                                 .
        |                                                      .
        |                                                .
        |                            ...
        |                           /   .               .
        |                          /
        |                         /      .
        |                        .        .            .
    1.5 |----.......--------------------------------------------
        |....       \\           .          .
        |            \\         /                      .
        |             ..      /             .
        |               \\    /                       .
        |                ....
        |                                    .
        |                                     .     .
        |
        |                                      .   .
    -11 |_______________________________________________________
         0                          7.5                        15
    """
    for line in textplot_str(expr, a, b, W, H):
        print(line)
        return None
