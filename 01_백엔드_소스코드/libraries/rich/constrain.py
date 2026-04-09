# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constrain.pyc (Python 3.11)

from typing import Optional, TYPE_CHECKING
from jupyter import JupyterMixin
from measure import Measurement
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType, RenderResult

class Constrain(JupyterMixin):
    '''Constrain the width of a renderable to a given number of characters.

    Args:
        renderable (RenderableType): A renderable object.
        width (int, optional): The maximum width (in characters) to render. Defaults to 80.
    '''
    
    def __init__(self = None, renderable = None, width = None):
        self.renderable = renderable
        self.width = width

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete
