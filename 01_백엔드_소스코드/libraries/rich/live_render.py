# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: live_render.pyc (Python 3.11)

from typing import Literal, Optional, Tuple
from _loop import loop_last
from console import Console, ConsoleOptions, RenderableType, RenderResult
from control import Control
from segment import ControlType, Segment
from style import StyleType
from text import Text
VerticalOverflowMethod = Literal[('crop', 'ellipsis', 'visible')]

class LiveRender:
    '''Creates a renderable that may be updated.

    Args:
        renderable (RenderableType): Any renderable object.
        style (StyleType, optional): An optional style to apply to the renderable. Defaults to "".
    '''
    
    def __init__(self = None, renderable = None, style = None, vertical_overflow = ('', 'ellipsis')):
        self.renderable = renderable
        self.style = style
        self.vertical_overflow = vertical_overflow
        self._shape = None

    last_render_height = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def set_renderable(self = None, renderable = None):
        '''Set a new renderable.

        Args:
            renderable (RenderableType): Any renderable object, including str.
        '''
        self.renderable = renderable

    
    def position_cursor(self = None):
        '''Get control codes to move cursor to beginning of live render.

        Returns:
            Control: A control instance that may be printed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def restore_cursor(self = None):
        '''Get control codes to clear the render and restore the cursor to its previous position.

        Returns:
            Control: A Control instance that may be printed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete
