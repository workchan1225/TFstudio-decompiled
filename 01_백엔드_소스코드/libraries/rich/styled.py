# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: styled.pyc (Python 3.11)

from typing import TYPE_CHECKING
from measure import Measurement
from segment import Segment
from style import StyleType
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderResult, RenderableType

class Styled:
    '''Apply a style to a renderable.

    Args:
        renderable (RenderableType): Any renderable.
        style (StyleType): A style to apply across the entire renderable.
    '''
    
    def __init__(self = None, renderable = None, style = None):
        self.renderable = renderable
        self.style = style

    
    def __rich_console__(self = None, console = None, options = None):
        style = console.get_style(self.style)
        rendered_segments = console.render(self.renderable, options)
        segments = Segment.apply_style(rendered_segments, style)
        return segments

    
    def __rich_measure__(self = None, console = None, options = None):
        return Measurement.get(console, options, self.renderable)


if __name__ == '__main__':
    from rich import print
    from rich.panel import Panel
    panel = Styled(Panel('hello'), 'on blue')
    print(panel)
    return None
