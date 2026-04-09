# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: align.pyc (Python 3.11)

from itertools import chain
from typing import TYPE_CHECKING, Iterable, Optional, Literal
from constrain import Constrain
from jupyter import JupyterMixin
from measure import Measurement
from segment import Segment
from style import StyleType
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType, RenderResult
AlignMethod = Literal[('left', 'center', 'right')]
VerticalAlignMethod = Literal[('top', 'middle', 'bottom')]

class Align(JupyterMixin):
    '''Align a renderable by adding spaces if necessary.

    Args:
        renderable (RenderableType): A console renderable.
        align (AlignMethod): One of "left", "center", or "right""
        style (StyleType, optional): An optional style to apply to the background.
        vertical (Optional[VerticalAlignMethod], optional): Optional vertical align, one of "top", "middle", or "bottom". Defaults to None.
        pad (bool, optional): Pad the right with spaces. Defaults to True.
        width (int, optional): Restrict contents to given width, or None to use default width. Defaults to None.
        height (int, optional): Set height of align renderable, or None to fit to contents. Defaults to None.

    Raises:
        ValueError: if ``align`` is not one of the expected values.

    Example:
        .. code-block:: python

            from rich.console import Console
            from rich.align import Align
            from rich.panel import Panel

            console = Console()
            # Create a panel 20 characters wide
            p = Panel("Hello, [b]World[/b]!", style="on green", width=20)

            # Renders the panel centered in the terminal
            console.print(Align(p, align="center"))
    '''
    
    def __init__(self = None, renderable = None, align = None, style = None, *, vertical, pad, width, height):
        if align not in ('left', 'center', 'right'):
            raise ValueError(f'''invalid value for align, expected "left", "center", or "right" (not {align!r})''')
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''Align({self.renderable!r}, {self.align!r})'''

    left = (lambda cls = None, renderable = None, style = None, *, vertical, pad, width: cls(renderable, 'left', style = style, vertical = vertical, pad = pad, width = width, height = height))()
    center = (lambda cls = None, renderable = None, style = None, *, vertical, pad, width: cls(renderable, 'center', style = style, vertical = vertical, pad = pad, width = width, height = height))()
    right = (lambda cls = None, renderable = None, style = None, *, vertical, pad, width: cls(renderable, 'right', style = style, vertical = vertical, pad = pad, width = width, height = height))()
    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        measurement = Measurement.get(console, options, self.renderable)
        return measurement



class VerticalCenter(JupyterMixin):
    '''Vertically aligns a renderable.

    Warn:
        This class is deprecated and may be removed in a future version. Use Align class with
        `vertical="middle"`.

    Args:
        renderable (RenderableType): A renderable object.
        style (StyleType, optional): An optional style to apply to the background. Defaults to None.
    '''
    
    def __init__(self = None, renderable = None, style = None):
        self.renderable = renderable
        self.style = style

    
    def __repr__(self = None):
        return f'''VerticalCenter({self.renderable!r})'''

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        measurement = Measurement.get(console, options, self.renderable)
        return measurement


if __name__ == '__main__':
    from rich.console import Console, Group
    from rich.highlighter import ReprHighlighter
    from rich.panel import Panel
    highlighter = ReprHighlighter()
    console = Console()
    panel = Panel(Group(Align.left(highlighter("align='left'")), Align.center(highlighter("align='center'")), Align.right(highlighter("align='right'"))), width = 60, style = 'on dark_blue', title = 'Align')
    console.print(Align.center(panel, vertical = 'middle', style = 'on red', height = console.height))
    return None
