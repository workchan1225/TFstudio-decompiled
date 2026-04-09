# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: palette.pyc (Python 3.11)

from math import sqrt
from functools import lru_cache
from typing import Sequence, Tuple, TYPE_CHECKING
from color_triplet import ColorTriplet
if TYPE_CHECKING:
    from rich.table import Table

class Palette:
    '''A palette of available colors.'''
    
    def __init__(self = None, colors = None):
        self._colors = colors

    
    def __getitem__(self = None, number = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich__(self = None):
        Color = Color
        import rich.color
        Style = Style
        import rich.style
        Text = Text
        import rich.text
        Table = Table
        import rich.table
        table = Table('index', 'RGB', 'Color', title = 'Palette', caption = f'''{len(self._colors)} colors''', highlight = True, caption_justify = 'right')
    # WARNING: Decompyle incomplete

    match = (lambda self = None, color = None: pass# WARNING: Decompyle incomplete
)()

if __name__ == '__main__':
    import colorsys
    from typing import Iterable
    from rich.color import Color
    from rich.console import Console, ConsoleOptions
    from rich.segment import Segment
    from rich.style import Style
    
    class ColorBox:
        
        def __rich_console__(self = None, console = None, options = None):
            pass
        # WARNING: Decompyle incomplete


    console = Console()
    console.print(ColorBox())
    return None
