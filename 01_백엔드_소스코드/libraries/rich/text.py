# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text.pyc (Python 3.11)

import re
from functools import partial, reduce
from math import gcd
from operator import itemgetter
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterable, List, NamedTuple, Optional, Pattern, Tuple, Union
from _loop import loop_last
from _pick import pick_bool
from _wrap import divide_line
from align import AlignMethod
from cells import cell_len, set_cell_size
from containers import Lines
from control import strip_control_codes
from emoji import EmojiVariant
from jupyter import JupyterMixin
from measure import Measurement
from segment import Segment
from style import Style, StyleType
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, JustifyMethod, OverflowMethod
DEFAULT_JUSTIFY: 'JustifyMethod' = 'default'
DEFAULT_OVERFLOW: 'OverflowMethod' = 'fold'
_re_whitespace = re.compile('\\s+$')
TextType = Union[(str, 'Text')]
GetStyleCallable = Callable[([
    str], Optional[StyleType])]

class Span(NamedTuple):
    style: Union[(str, Style)] = 'A marked up region in some text.'
    
    def __repr__(self = None):
        return f'''Span({self.start}, {self.end}, {self.style!r})'''

    
    def __bool__(self = None):
        return self.end > self.start

    
    def split(self = None, offset = None):
        '''Split a span in to 2 from a given offset.'''
        if offset < self.start:
            return (self, None)
        if None >= self.end:
            return (self, None)
        (start, end, style) = None
        span1 = Span(start, min(end, offset), style)
        span2 = Span(span1.end, end, style)
        return (span1, span2)

    
    def move(self = None, offset = None):
        '''Move start and end by a given offset.

        Args:
            offset (int): Number of characters to add to start and end.

        Returns:
            TextSpan: A new TextSpan with adjusted position.
        '''
        (start, end, style) = self
        return Span(start + offset, end + offset, style)

    
    def right_crop(self = None, offset = None):
        '''Crop the span at the given offset.

        Args:
            offset (int): A value between start and end.

        Returns:
            Span: A new (possibly smaller) span.
        '''
        (start, end, style) = self
        if offset >= end:
            return self
        return None(start, min(offset, end), style)

    
    def extend(self = None, cells = None):
        '''Extend the span by the given number of cells.

        Args:
            cells (int): Additional space to add to end of span.

        Returns:
            Span: A span.
        '''
        if cells:
            (start, end, style) = self
            return Span(start, end + cells, style)



class Text(JupyterMixin):
    '''Text with color / style.

    Args:
        text (str, optional): Default unstyled text. Defaults to "".
        style (Union[str, Style], optional): Base style for text. Defaults to "".
        justify (str, optional): Justify method: "left", "center", "full", "right". Defaults to None.
        overflow (str, optional): Overflow method: "crop", "fold", "ellipsis". Defaults to None.
        no_wrap (bool, optional): Disable text wrapping, or None for default. Defaults to None.
        end (str, optional): Character to end text with. Defaults to "\\\\n".
        tab_size (int): Number of spaces per tab, or ``None`` to use ``console.tab_size``. Defaults to None.
        spans (List[Span], optional). A list of predefined style spans. Defaults to None.
    '''
    __slots__ = [
        '_text',
        'style',
        'justify',
        'overflow',
        'no_wrap',
        'end',
        'tab_size',
        '_spans',
        '_length']
    
    def __init__(self = None, text = None, style = None, *, justify, overflow, no_wrap, end, tab_size, spans):
