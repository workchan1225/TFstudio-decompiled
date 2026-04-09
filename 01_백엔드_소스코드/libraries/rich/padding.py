# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: padding.pyc (Python 3.11)

from typing import TYPE_CHECKING, List, Optional, Tuple, Union
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType, RenderResult
from jupyter import JupyterMixin
from measure import Measurement
from segment import Segment
from style import Style
PaddingDimensions = Union[(int, Tuple[int], Tuple[(int, int)], Tuple[(int, int, int, int)])]

class Padding(JupyterMixin):
    '''Draw space around content.

    Example:
        >>> print(Padding("Hello", (2, 4), style="on blue"))

    Args:
        renderable (RenderableType): String or other renderable.
        pad (Union[int, Tuple[int]]): Padding for top, right, bottom, and left borders.
            May be specified with 1, 2, or 4 integers (CSS style).
        style (Union[str, Style], optional): Style for padding characters. Defaults to "none".
        expand (bool, optional): Expand padding to fit available width. Defaults to True.
    '''
    
    def __init__(self = None, renderable = None, pad = None, *, style, expand):
        self.renderable = renderable
        (self.top, self.right, self.bottom, self.left) = self.unpack(pad)
        self.style = style
        self.expand = expand

    indent = (lambda cls = None, renderable = None, level = classmethod: Padding(renderable, pad = (0, 0, 0, level), expand = False))()
    unpack = (lambda pad = None: if isinstance(pad, int):
(pad, pad, pad, pad)if None(pad) == 1:
_pad = pad[0](_pad, _pad, _pad, _pad)if None(pad) == 2:
(pad_top, pad_right) = pad(pad_top, pad_right, pad_top, pad_right)if None(pad) == 4:
(top, right, bottom, left) = pad(top, right, bottom, left)raise None(f'''1, 2 or 4 integers required for padding; {len(pad)} given'''))()
    
    def __repr__(self = None):
        return f'''Padding({self.renderable!r}, ({self.top},{self.right},{self.bottom},{self.left}))'''

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        max_width = options.max_width
        extra_width = self.left + self.right
        if max_width - extra_width < 1:
            return Measurement(max_width, max_width)
        (measure_min, measure_max) = None.get(console, options, self.renderable)
        measurement = Measurement(measure_min + extra_width, measure_max + extra_width)
        measurement = measurement.with_maximum(max_width)
        return measurement


if __name__ == '__main__':
    from rich import print
    print(Padding('Hello, World', (2, 4), style = 'on blue'))
    return None
