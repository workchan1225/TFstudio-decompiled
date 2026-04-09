# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _misc.pyc (Python 3.11)

from __future__ import annotations
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any
from pandas.util._decorators import set_module
from pandas.plotting._core import _get_plot_backend
if TYPE_CHECKING:
    from collections.abc import Generator, Mapping
    from matplotlib.axes import Axes
    from matplotlib.colors import Colormap
    from matplotlib.figure import Figure
    from matplotlib.table import Table
    import numpy as np
    from pandas import DataFrame, Series
table = (lambda ax = None, data = None: plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
register = (lambda : plot_backend = _get_plot_backend('matplotlib')plot_backend.register())()
deregister = (lambda : plot_backend = _get_plot_backend('matplotlib')plot_backend.deregister())()
scatter_matrix = (lambda frame, alpha, figsize, ax, grid, diagonal = None, marker = None, density_kwds = set_module('pandas.plotting'), hist_kwds = (0.5, None, None, False, 'hist', '.', None, None, 0.05), range_padding = ('frame', 'DataFrame', 'alpha', 'float', 'figsize', 'tuple[float, float] | None', 'ax', 'Axes | None', 'grid', 'bool', 'diagonal', 'str', 'marker', 'str', 'density_kwds', 'Mapping[str, Any] | None', 'hist_kwds', 'Mapping[str, Any] | None', 'range_padding', 'float', 'return', 'np.ndarray'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
radviz = (lambda frame = None, class_column = None, ax = set_module('pandas.plotting'), color = (None, None, None), colormap = ('frame', 'DataFrame', 'class_column', 'str', 'ax', 'Axes | None', 'color', 'list[str] | tuple[str, ...] | None', 'colormap', 'Colormap | str | None', 'return', 'Axes'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
andrews_curves = (lambda frame, class_column = None, ax = None, samples = set_module('pandas.plotting'), color = (None, 200, None, None), colormap = ('frame', 'DataFrame', 'class_column', 'str', 'ax', 'Axes | None', 'samples', 'int', 'color', 'list[str] | tuple[str, ...] | None', 'colormap', 'Colormap | str | None', 'return', 'Axes'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
bootstrap_plot = (lambda series = None, fig = None, size = set_module('pandas.plotting'), samples = (None, 50, 500): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
parallel_coordinates = (lambda frame, class_column, cols, ax, color, use_columns, xticks = None, colormap = None, axvlines = set_module('pandas.plotting'), axvlines_kwds = (None, None, None, False, None, None, True, None, False), sort_labels = ('frame', 'DataFrame', 'class_column', 'str', 'cols', 'list[str] | None', 'ax', 'Axes | None', 'color', 'list[str] | tuple[str, ...] | None', 'use_columns', 'bool', 'xticks', 'list | tuple | None', 'colormap', 'Colormap | str | None', 'axvlines', 'bool', 'axvlines_kwds', 'Mapping[str, Any] | None', 'sort_labels', 'bool', 'return', 'Axes'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
lag_plot = (lambda series = None, lag = None, ax = set_module('pandas.plotting'): plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()
autocorrelation_plot = (lambda series = None, ax = None: plot_backend = _get_plot_backend('matplotlib')# WARNING: Decompyle incomplete
)()

class _Options(dict):
    pass
# WARNING: Decompyle incomplete

plot_params = _Options()
plot_params.__module__ = 'pandas.plotting'
