# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: style.pyc (Python 3.11)

'''
Module for applying conditional formatting to DataFrames and Series.
'''
from __future__ import annotations
import copy
from functools import partial
import operator
from typing import TYPE_CHECKING, Concatenate, Self, overload
import numpy as np
from pandas._config import get_option
from pandas.compat._optional import import_optional_dependency
import pandas as pd
from pandas import IndexSlice, RangeIndex

common
from pandas.core.frame import DataFrame, Series
Series = Series
import pandas.core.common, core
from pandas.io.formats.format import save_to_buffer
jinja2 = import_optional_dependency('jinja2', extra = 'DataFrame.style requires jinja2.')
from pandas.io.formats.style_render import CSSProperties, CSSStyles, ExtFormatter, StylerRenderer, Subset, Tooltips, format_table_styles, maybe_convert_css_to_tuples, non_reducing_slice, refactor_levels
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Sequence
    from matplotlib.colors import Colormap
    from pandas._typing import Any, Axis, AxisInt, ExcelWriterMergeCells, FilePath, IndexLabel, IntervalClosedType, Level, P, QuantileInterpolation, Scalar, StorageOptions, T, WriteBuffer, WriteExcelBuffer
    from pandas import ExcelWriter
    from pandas.core.generic import NDFrame

class Styler(StylerRenderer):
    pass
# WARNING: Decompyle incomplete


def _validate_apply_axis_arg(arg = None, arg_name = None, dtype = None, data = ('arg', 'NDFrame | Sequence | np.ndarray', 'arg_name', 'str', 'dtype', 'Any | None', 'data', 'NDFrame', 'return', 'np.ndarray')):
    '''
    For the apply-type methods, ``axis=None`` creates ``data`` as DataFrame, and for
    ``axis=[1,0]`` it creates a Series. Where ``arg`` is expected as an element
    of some operator with ``data`` we must make sure that the two are compatible shapes,
    or raise.

    Parameters
    ----------
    arg : sequence, Series or DataFrame
        the user input arg
    arg_name : string
        name of the arg for use in error messages
    dtype : numpy dtype, optional
        forced numpy dtype if given
    data : Series or DataFrame
        underling subset of Styler data on which operations are performed

    Returns
    -------
    ndarray
    '''
    dtype = {
        'dtype': dtype } if dtype else { }
    if isinstance(arg, Series) and isinstance(data, DataFrame):
        raise ValueError(f'''\'{arg_name}\' is a Series but underlying data for operations is a DataFrame since \'axis=None\'''')
    if isinstance(arg, DataFrame) and isinstance(data, Series):
        raise ValueError(f'''\'{arg_name}\' is a DataFrame but underlying data for operations is a Series with \'axis in [0,1]\'''')
# WARNING: Decompyle incomplete


def _background_gradient(data, cmap, low, high, text_color_threshold = None, vmin = None, vmax = None, gmap = ('PuBu', 0, 0, 0.408, None, None, None, False), text_only = ('cmap', 'str | Colormap', 'low', 'float', 'high', 'float', 'text_color_threshold', 'float', 'vmin', 'float | None', 'vmax', 'float | None', 'gmap', 'Sequence | np.ndarray | DataFrame | Series | None', 'text_only', 'bool', 'return', 'list[str] | DataFrame')):
    '''
    Color background in a range according to the data or a gradient map
    '''
    pass
# WARNING: Decompyle incomplete


def _highlight_between(data = None, props = None, left = None, right = (None, None, True), inclusive = ('data', 'NDFrame', 'props', 'str', 'left', 'Scalar | Sequence | np.ndarray | NDFrame | None', 'right', 'Scalar | Sequence | np.ndarray | NDFrame | None', 'inclusive', 'bool | str', 'return', 'np.ndarray')):
    '''
    Return an array of css props based on condition of data values within given range.
    '''
    if not np.iterable(left) and isinstance(left, str):
        left = _validate_apply_axis_arg(left, 'left', None, data)
    if not np.iterable(right) and isinstance(right, str):
        right = _validate_apply_axis_arg(right, 'right', None, data)
    if inclusive == 'both':
        ops = (operator.ge, operator.le)
    elif inclusive == 'neither':
        ops = (operator.gt, operator.lt)
    elif inclusive == 'left':
        ops = (operator.ge, operator.lt)
    elif inclusive == 'right':
        ops = (operator.gt, operator.le)
    else:
        raise ValueError(f'''\'inclusive\' values can be \'both\', \'left\', \'right\', or \'neither\' got {inclusive}''')
# WARNING: Decompyle incomplete


def _highlight_value(data = None, op = None, props = None):
    '''
    Return an array of css strings based on the condition of values matching an op.
    '''
    value = getattr(data, op)(skipna = True)
    if isinstance(data, DataFrame):
        value = getattr(value, op)(skipna = True)
    cond = data == value
    cond = cond.where(pd.notna(cond), False)
    return np.where(cond, props, '')


def _bar(data, align, colors, cmap, width, height = None, vmin = None, vmax = None, base_css = ('data', 'NDFrame', 'align', 'str | float | Callable', 'colors', 'str | list | tuple', 'cmap', 'Any', 'width', 'float', 'height', 'float', 'vmin', 'float | None', 'vmax', 'float | None', 'base_css', 'str')):
    '''
    Draw bar chart in data cells using HTML CSS linear gradient.

    Parameters
    ----------
    data : Series or DataFrame
        Underling subset of Styler data on which operations are performed.
    align : str in {"left", "right", "mid", "zero", "mean"}, int, float, callable
        Method for how bars are structured or scalar value of centre point.
    colors : list-like of str
        Two listed colors as string in valid CSS.
    width : float in [0,1]
        The percentage of the cell, measured from left, where drawn bars will reside.
    height : float in [0,1]
        The percentage of the cell\'s height where drawn bars will reside, centrally
        aligned.
    vmin : float, optional
        Overwrite the minimum value of the window.
    vmax : float, optional
        Overwrite the maximum value of the window.
    base_css : str
        Additional CSS that is included in the cell before bars are drawn.
    '''
    pass
# WARNING: Decompyle incomplete
