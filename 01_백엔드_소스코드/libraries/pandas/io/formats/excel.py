# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: excel.pyc (Python 3.11)

'''
Utilities for conversion to writer-agnostic Excel representation.
'''
from __future__ import annotations
from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
import functools
import itertools
import re
from typing import TYPE_CHECKING, Any, cast
import warnings
import numpy as np
from pandas._libs.lib import is_list_like
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes import missing
from pandas.core.dtypes.common import is_float, is_scalar
from pandas import DataFrame, Index, MultiIndex, Period, PeriodIndex

common
from pandas.io.formats._color_data import CSS4_COLORS
import pandas.core.common, core
from pandas.io.formats.css import CSSResolver, CSSWarning
from pandas.io.formats.format import get_level_lengths
if TYPE_CHECKING:
    from pandas._typing import ExcelWriterMergeCells, FilePath, IndexLabel, StorageOptions, WriteExcelBuffer
    from pandas import ExcelWriter

class ExcelCell:
    __fields__ = ('row', 'col', 'val', 'style', 'mergestart', 'mergeend')
    __slots__ = __fields__
    
    def __init__(self, row, col = None, val = None, style = None, mergestart = (None, None, None), mergeend = ('row', 'int', 'col', 'int', 'mergestart', 'int | None', 'mergeend', 'int | None', 'return', 'None')):
        self.row = row
        self.col = col
        self.val = val
        self.style = style
        self.mergestart = mergestart
        self.mergeend = mergeend



class CssExcelCell(ExcelCell):
    pass
# WARNING: Decompyle incomplete


class CSSToExcelConverter:
    '''
    A callable for converting CSS declarations to ExcelWriter styles

    Supports parts of CSS 2.2, with minimal CSS 3.0 support (e.g. text-shadow),
    focusing on font styling, backgrounds, borders and alignment.

    Operates by first computing CSS styles in a fairly generic
    way (see :meth:`compute_css`) then determining Excel style
    properties from CSS properties (see :meth:`build_xlstyle`).

    Parameters
    ----------
    inherited : str, optional
        CSS declarations understood to be the containing scope for the
        CSS processed by :meth:`__call__`.
    '''
    NAMED_COLORS = CSS4_COLORS
    VERTICAL_MAP = {
        'top': 'top',
        'text-top': 'top',
        'middle': 'center',
        'baseline': 'bottom',
        'bottom': 'bottom',
        'text-bottom': 'bottom' }
    BOLD_MAP = {
        'bold': True,
        'bolder': True,
        '600': True,
        '700': True,
        '800': True,
        '900': True,
        'normal': False,
        'lighter': False,
        '100': False,
        '200': False,
        '300': False,
        '400': False,
        '500': False }
    ITALIC_MAP = {
        'normal': False,
        'italic': True,
        'oblique': True }
    FAMILY_MAP = {
        'serif': 1,
        'sans-serif': 2,
        'cursive': 4,
        'fantasy': 5 }
    inherited: 'dict[str, str] | None' = ('dashed', 'mediumDashDot', 'dashDotDot', 'hair', 'dotted', 'mediumDashDotDot', 'double', 'dashDot', 'slantDashDot', 'mediumDashed')()
    
    def __init__(self = None, inherited = None):
        pass
    # WARNING: Decompyle incomplete

    compute_css = CSSResolver()
    
    def __call__(self = None, declarations = None):
        '''
        Convert CSS declarations to ExcelWriter style.

        Parameters
        ----------
        declarations : str | frozenset[tuple[str, str]]
            CSS string or set of CSS declaration tuples.
            e.g. "font-weight: bold; background: blue" or
            {("font-weight", "bold"), ("background", "blue")}

        Returns
        -------
        xlstyle : dict
            A style as interpreted by ExcelWriter when found in
            ExcelCell.style.
        '''
        return self._call_cached(declarations)

    
    def _call_uncached(self = None, declarations = None):
        properties = self.compute_css(declarations, self.inherited)
        return self.build_xlstyle(properties)

    
    def build_xlstyle(self = None, props = None):
        pass
    # WARNING: Decompyle incomplete

    
    def build_alignment(self = None, props = None):
        return {
            'horizontal': props.get('text-align'),
            'vertical': self._get_vertical_alignment(props),
            'wrap_text': self._get_is_wrap_text(props) }

    
    def _get_vertical_alignment(self = None, props = None):
        vertical_align = props.get('vertical-align')
        if vertical_align:
            return self.VERTICAL_MAP.get(vertical_align)

    
    def _get_is_wrap_text(self = None, props = None):
        pass
    # WARNING: Decompyle incomplete

    
    def build_border(self = None, props = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _border_style(self = None, style = None, width = None, color = ('style', 'str | None', 'width', 'str | None', 'color', 'str | None', 'return', 'str | None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_width_name(self = None, width_input = None):
        width = self._width_to_float(width_input)
        if width < 1e-05:
            return None
        if None < 1.3:
            return 'thin'
        if None < 2.8:
            return 'medium'

    
    def _width_to_float(self = None, width = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _pt_to_float(self = None, pt_string = None):
        pass
    # WARNING: Decompyle incomplete

    
    def build_fill(self = None, props = None):
        fill_color = props.get('background-color')
        if fill_color not in (None, 'transparent', 'none'):
            return {
                'fgColor': self.color_to_excel(fill_color),
                'patternType': 'solid' }

    
    def build_number_format(self = None, props = None):
        fc = props.get('number-format')
        fc = fc.replace('§', ';') if isinstance(fc, str) else fc
        return {
            'format_code': fc }

    
    def build_font(self = None, props = None):
