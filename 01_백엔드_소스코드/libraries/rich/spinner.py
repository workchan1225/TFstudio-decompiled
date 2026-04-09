# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spinner.pyc (Python 3.11)

from typing import TYPE_CHECKING, List, Optional, Union, cast
from _spinners import SPINNERS
from measure import Measurement
from table import Table
from text import Text
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType, RenderResult
    from style import StyleType

class Spinner:
    '''A spinner animation.

    Args:
        name (str): Name of spinner (run python -m rich.spinner).
        text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
        style (StyleType, optional): Style for spinner animation. Defaults to None.
        speed (float, optional): Speed factor for animation. Defaults to 1.0.

    Raises:
        KeyError: If name isn\'t one of the supported spinner animations.
    '''
    
    def __init__(self = None, name = None, text = None, *, style, speed):
        
        try:
            spinner = SPINNERS[name]
        except KeyError:
            raise KeyError(f'''no spinner called {name!r}''')

        self.text = Text.from_markup(text) if isinstance(text, str) else text
        self.name = name
        self.frames = cast(List[str], spinner['frames'])[:]
        self.interval = cast(float, spinner['interval'])
        self.start_time = None
        self.style = style
        self.speed = speed
        self.frame_no_offset = 0
        self._update_speed = 0

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        text = self.render(0)
        return Measurement.get(console, options, text)

    
    def render(self = None, time = None):
        '''Render the spinner for a given time.

        Args:
            time (float): Time in seconds.

        Returns:
            RenderableType: A renderable containing animation frame.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def update(self = None, *, text, style, speed):
        '''Updates attributes of a spinner after it has been started.

        Args:
            text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
            style (StyleType, optional): Style for spinner animation. Defaults to None.
            speed (float, optional): Speed factor for animation. Defaults to None.
        '''
        if text:
            self.text = Text.from_markup(text) if isinstance(text, str) else text
        if style:
            self.style = style
        if speed:
            self._update_speed = speed
            return None


# WARNING: Decompyle incomplete
