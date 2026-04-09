# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: measure.pyc (Python 3.11)

from operator import itemgetter
from typing import TYPE_CHECKING, Callable, NamedTuple, Optional, Sequence
from  import errors
from protocol import is_renderable, rich_cast
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderableType

class Measurement(NamedTuple):
    maximum: int = 'Stores the minimum and maximum widths (in characters) required to render an object.'
    span = (lambda self = None: self.maximum - self.minimum)()
    
    def normalize(self = None):
        '''Get measurement that ensures that minimum <= maximum and minimum >= 0

        Returns:
            Measurement: A normalized measurement.
        '''
        (minimum, maximum) = self
        minimum = min(max(0, minimum), maximum)
        return Measurement(max(0, minimum), max(0, max(minimum, maximum)))

    
    def with_maximum(self = None, width = None):
        '''Get a RenderableWith where the widths are <= width.

        Args:
            width (int): Maximum desired width.

        Returns:
            Measurement: New Measurement object.
        '''
        (minimum, maximum) = self
        return Measurement(min(minimum, width), min(maximum, width))

    
    def with_minimum(self = None, width = None):
        '''Get a RenderableWith where the widths are >= width.

        Args:
            width (int): Minimum desired width.

        Returns:
            Measurement: New Measurement object.
        '''
        (minimum, maximum) = self
        width = max(0, width)
        return Measurement(max(minimum, width), max(maximum, width))

    
    def clamp(self = None, min_width = None, max_width = None):
        '''Clamp a measurement within the specified range.

        Args:
            min_width (int): Minimum desired width, or ``None`` for no minimum. Defaults to None.
            max_width (int): Maximum desired width, or ``None`` for no maximum. Defaults to None.

        Returns:
            Measurement: New Measurement object.
        '''
        measurement = self
    # WARNING: Decompyle incomplete

    get = (lambda cls = None, console = None, options = classmethod, renderable = ('console', 'Console', 'options', 'ConsoleOptions', 'renderable', 'RenderableType', 'return', 'Measurement'): _max_width = options.max_widthif _max_width < 1:
Measurement(0, 0)if None(renderable, str):
renderable = console.render_str(renderable, markup = options.markup, highlight = False)renderable = rich_cast(renderable)# WARNING: Decompyle incomplete
)()


def measure_renderables(console = None, options = None, renderables = None):
    '''Get a measurement that would fit a number of renderables.

    Args:
        console (~rich.console.Console): Console instance.
        options (~rich.console.ConsoleOptions): Console options.
        renderables (Iterable[RenderableType]): One or more renderable objects.

    Returns:
        Measurement: Measurement object containing range of character widths required to
            contain all given renderables.
    '''
    pass
# WARNING: Decompyle incomplete
