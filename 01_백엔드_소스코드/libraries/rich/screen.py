# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: screen.pyc (Python 3.11)

from typing import Optional, TYPE_CHECKING
from segment import Segment
from style import StyleType
from _loop import loop_last
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderResult, RenderableType, Group

class Screen:
    renderable: 'RenderableType' = 'A renderable that fills the terminal screen and crops excess.\n\n    Args:\n        renderable (RenderableType): Child renderable.\n        style (StyleType, optional): Optional background style. Defaults to None.\n    '
    
    def __init__(self = None, *, style, application_mode, *renderables):
        Group = Group
        import rich.console
    # WARNING: Decompyle incomplete

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete
