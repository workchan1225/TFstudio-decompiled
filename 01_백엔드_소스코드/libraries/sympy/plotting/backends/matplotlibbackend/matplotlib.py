# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matplotlib.pyc (Python 3.11)

from collections.abc import Callable
from sympy.core.basic import Basic
from sympy.external import import_module


base_backend
from sympy.printing.latex import latex
import sympy.plotting.backends.base_backend, plotting, backends

def _str_or_latex(label):
    if isinstance(label, Basic):
        return latex(label, mode = 'inline')
    return None(label)


def _matplotlib_list(interval_list):
    '''
    Returns lists for matplotlib ``fill`` command from a list of bounding
    rectangular intervals
    '''
    xlist = []
    ylist = []
    if len(interval_list):
        for intervals in interval_list:
            intervalx = intervals[0]
            intervaly = intervals[1]
            xlist.extend([
                intervalx.start,
                intervalx.start,
                intervalx.end,
                intervalx.end,
                None])
            ylist.extend([
                intervaly.start,
                intervaly.end,
                intervaly.end,
                intervaly.start,
                None])
    xlist.extend((None, None, None, None))
    ylist.extend((None, None, None, None))
    return (xlist, ylist)


class MatplotlibBackend(base_backend.Plot):
    pass
# WARNING: Decompyle incomplete
