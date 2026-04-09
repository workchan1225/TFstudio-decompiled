# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: css.pyc (Python 3.11)

'''
Utilities for interpreting CSS from Stylers for formatting non-HTML outputs.
'''
from __future__ import annotations
import re
from typing import TYPE_CHECKING
import warnings
from pandas.errors import CSSWarning
from pandas.util._exceptions import find_stack_level
if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterable, Iterator

def _side_expander(prop_fmt = None):
    """
    Wrapper to expand shorthand property into top, right, bottom, left properties

    Parameters
    ----------
    side : str
        The border side to expand into properties

    Returns
    -------
        function: Return to call when a 'border(-{side}): {value}' string is encountered
    """
    pass
# WARNING: Decompyle incomplete


def _border_expander(side = None):
    """
    Wrapper to expand 'border' property into border color, style, and width properties

    Parameters
    ----------
    side : str
        The border side to expand into properties

    Returns
    -------
        function: Return to call when a 'border(-{side}): {value}' string is encountered
    """
    pass
# WARNING: Decompyle incomplete


class CSSResolver:
    __module__ = __name__
    __qualname__ = 'CSSResolver'
    __doc__ = '\n    A callable for parsing and resolving CSS to atomic properties.\n    '
    UNIT_RATIOS = {
        'pt': ('pt', 1),
        'em': ('em', 1),
        'rem': ('pt', 12),
        'ex': ('em', 0.5),
        'px': ('pt', 0.75),
        'pc': ('pt', 12),
        'in': ('pt', 72),
        'cm': ('in', 0.393701),
        'mm': ('in', 0.0393701),
        'q': ('mm', 0.25),
        '!!default': ('em', 0) }
    FONT_SIZE_RATIOS = UNIT_RATIOS.copy()
    FONT_SIZE_RATIOS.update({
        '%': ('em', 0.01),
        'xx-small': ('rem', 0.5),
        'x-small': ('rem', 0.625),
        'small': ('rem', 0.8),
        'medium': ('rem', 1),
        'large': ('rem', 1.125),
        'x-large': ('rem', 1.5),
        'xx-large': ('rem', 2),
        'smaller': ('em', 0.833333),
        'larger': ('em', 1.2),
        '!!default': ('em', 1) })
    MARGIN_RATIOS = UNIT_RATIOS.copy()
    MARGIN_RATIOS.update({
        'none': ('pt', 0) })
    BORDER_WIDTH_RATIOS = UNIT_RATIOS.copy()
    BORDER_WIDTH_RATIOS.update({
        'none': ('pt', 0),
        'thick': ('px', 4),
        'medium': ('px', 2),
        'thin': ('px', 1) })
    BORDER_STYLES = [
        'none',
        'hidden',
        'dotted',
        'dashed',
        'solid',
        'double',
        'groove',
        'ridge',
        'inset',
        'outset',
        'mediumdashdot',
        'dashdotdot',
        'hair',
        'mediumdashdotdot',
        'dashdot',
        'slantdashdot',
        'mediumdashed']
    SIDE_SHORTHANDS = {
        1: [
            0,
            0,
            0,
            0],
        2: [
            0,
            1,
            0,
            1],
        3: [
            0,
            1,
            2,
            1],
        4: [
            0,
            1,
            2,
            3] }
    SIDES = ('top', 'right', 'bottom', 'left')
# WARNING: Decompyle incomplete
