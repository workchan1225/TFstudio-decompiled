# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _core.pyc (Python 3.11)

from __future__ import annotations
import importlib
from typing import TYPE_CHECKING, Literal
from pandas._config import get_option
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_integer, is_list_like
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.base import PandasObject
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Sequence
    import types
    from matplotlib.axes import Axes
    import numpy as np
    from pandas._typing import IndexLabel
    from pandas import DataFrame, Index, Series
    from pandas.core.groupby.generic import DataFrameGroupBy

def holds_integer(column = None):
    return column.dtype.kind in 'iu'

hist_series = (lambda self, by, ax, grid, xlabelsize, xrot, ylabelsize, yrot = None, figsize = None, bins = set_module('pandas.plotting'), backend = (None, None, True, None, None, None, None, None, 10, None, False), legend = ('self', 'Series', 'grid', 'bool', 'xlabelsize', 'int | None', 'xrot', 'float | None', 'ylabelsize', 'int | None', 'yrot', 'float | None', 'figsize', 'tuple[int, int] | None', 'bins', 'int | Sequence[int]', 'backend', 'str | None', 'legend', 'bool'): plot_backend = _get_plot_backend(backend)# WARNING: Decompyle incomplete
)()
hist_frame = (lambda data, column, by, grid, xlabelsize, xrot, ylabelsize, yrot, ax, sharex, sharey, figsize = None, layout = None, bins = set_module('pandas.plotting'), backend = (None, None, True, None, None, None, None, None, False, False, None, None, 10, None, False), legend = ('data', 'DataFrame', 'column', 'IndexLabel | None', 'grid', 'bool', 'xlabelsize', 'int | None', 'xrot', 'float | None', 'ylabelsize', 'int | None', 'yrot', 'float | None', 'sharex', 'bool', 'sharey', 'bool', 'figsize', 'tuple[int, int] | None', 'layout', 'tuple[int, int] | None', 'bins', 'int | Sequence[int]', 'backend', 'str | None', 'legend', 'bool'): plot_backend = _get_plot_backend(backend)# WARNING: Decompyle incomplete
)()
boxplot = (lambda data, column, by, ax, fontsize, rot = None, grid = None, figsize = set_module('pandas.plotting'), layout = (None, None, None, None, 0, True, None, None, None), return_type = ('data', 'DataFrame', 'column', 'str | list[str] | None', 'by', 'str | list[str] | None', 'ax', 'Axes | None', 'fontsize', 'float | str | None', 'rot', 'int', 'grid', 'bool', 'figsize', 'tuple[float, float] | None', 'layout', 'tuple[int, int] | None', 'return_type', 'str | None'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
boxplot_frame = (lambda self, column, by, ax, fontsize, rot, grid = None, figsize = None, layout = set_module('pandas.plotting'), return_type = (None, None, None, None, 0, True, None, None, None, None), backend = ('self', 'DataFrame', 'fontsize', 'int | None', 'rot', 'int', 'grid', 'bool', 'figsize', 'tuple[float, float] | None'): plot_backend = _get_plot_backend(backend)# WARNING: Decompyle incomplete
)()
boxplot_frame_groupby = (lambda grouped, subplots, column, fontsize, rot, grid, ax, figsize = None, layout = None, sharex = set_module('pandas.plotting'), sharey = (True, None, None, 0, True, None, None, None, False, True, None), backend = ('grouped', 'DataFrameGroupBy', 'subplots', 'bool', 'fontsize', 'int | None', 'rot', 'int', 'grid', 'bool', 'figsize', 'tuple[float, float] | None', 'sharex', 'bool', 'sharey', 'bool'): plot_backend = _get_plot_backend(backend)# WARNING: Decompyle incomplete
)()
PlotAccessor = <NODE:12>()
_backends: 'dict[str, types.ModuleType]' = { }

def _load_backend(backend = None):
    '''
    Load a pandas plotting backend.

    Parameters
    ----------
    backend : str
        The identifier for the backend. Either an entrypoint item registered
        with importlib.metadata, "matplotlib", or a module name.

    Returns
    -------
    types.ModuleType
        The imported backend.
    '''
    entry_points = entry_points
    import importlib.metadata
    if backend == 'matplotlib':
        
        try:
            module = importlib.import_module('pandas.plotting._matplotlib')
        except ImportError:
            raise ImportError('matplotlib is required for plotting when the default backend "matplotlib" is selected.'), None

        return module
    found_backend = False
    eps = entry_points()
    key = 'pandas_plotting_backends'
    if hasattr(eps, 'select'):
        entry = eps.select(group = key)
    else:
        entry = eps.get(key, ())
    for entry_point in entry:
        found_backend = entry_point.name == backend
        if found_backend:
            module = entry_point.load()
        
        if not found_backend:
            
            try:
                module = importlib.import_module(backend)
                found_backend = True
            except ImportError:
                pass

            if found_backend and hasattr(module, 'plot'):
                return module
            raise None(f'''Could not find plotting backend \'{backend}\'. Ensure that you\'ve installed the package providing the \'{backend}\' entrypoint, or that the package has a top-level `.plot` method.''')


def _get_plot_backend(backend = None):
    '''
    Return the plotting backend to use (e.g. `pandas.plotting._matplotlib`).

    The plotting system of pandas uses matplotlib by default, but the idea here
    is that it can also work with other third-party backends. This function
    returns the module which provides a top-level `.plot` method that will
    actually do the plotting. The backend is specified from a string, which
    either comes from the keyword argument `backend`, or, if not specified, from
    the option `pandas.options.plotting.backend`. All the rest of the code in
    this file uses the backend specified there for the plotting.

    The backend is imported lazily, as matplotlib is a soft dependency, and
    pandas can be used without it being installed.

    Notes
    -----
    Modifies `_backends` with imported backend as a side effect.
    '''
    if not backend:
        pass
    backend_str = get_option('plotting.backend')
    if backend_str in _backends:
        return _backends[backend_str]
    module = None(backend_str)
    _backends[backend_str] = module
    return module
