# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: progress_bar.pyc (Python 3.11)

import math
from functools import lru_cache
from time import monotonic
from typing import Iterable, List, Optional
from color import Color, blend_rgb
from color_triplet import ColorTriplet
from console import Console, ConsoleOptions, RenderResult
from jupyter import JupyterMixin
from measure import Measurement
from segment import Segment
from style import Style, StyleType
PULSE_SIZE = 20

class ProgressBar(JupyterMixin):
    '''Renders a (progress) bar. Used by rich.progress.

    Args:
        total (float, optional): Number of steps in the bar. Defaults to 100. Set to None to render a pulsing animation.
        completed (float, optional): Number of steps completed. Defaults to 0.
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        pulse (bool, optional): Enable pulse effect. Defaults to False. Will pulse if a None total was passed.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        animation_time (Optional[float], optional): Time in seconds to use for animation, or None to use system time.
    '''
    
    def __init__(self, total, completed, width, pulse, style = None, complete_style = None, finished_style = None, pulse_style = (100, 0, None, False, 'bar.back', 'bar.complete', 'bar.finished', 'bar.pulse', None), animation_time = ('total', Optional[float], 'completed', float, 'width', Optional[int], 'pulse', bool, 'style', StyleType, 'complete_style', StyleType, 'finished_style', StyleType, 'pulse_style', StyleType, 'animation_time', Optional[float])):
        self.total = total
        self.completed = completed
        self.width = width
        self.pulse = pulse
        self.style = style
        self.complete_style = complete_style
        self.finished_style = finished_style
        self.pulse_style = pulse_style
        self.animation_time = animation_time
        self._pulse_segments = None

    
    def __repr__(self = None):
        return f'''<Bar {self.completed!r} of {self.total!r}>'''

    percentage_completed = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _get_pulse_segments = (lambda self, fore_style = None, back_style = None, color_system = lru_cache(maxsize = 16), no_color = (False,), ascii = ('fore_style', Style, 'back_style', Style, 'color_system', str, 'no_color', bool, 'ascii', bool, 'return', List[Segment]): bar = '-' if ascii else '━'segments = []if color_system not in ('standard', 'eight_bit', 'truecolor') or no_color:
segments += [
Segment(bar, fore_style)] * (PULSE_SIZE // 2)segments += [
Segment(' ' if no_color else bar, back_style)] * (PULSE_SIZE - PULSE_SIZE // 2)segmentsappend = None.appendfore_color = fore_style.color.get_truecolor() if fore_style.color else ColorTriplet(255, 0, 255)back_color = back_style.color.get_truecolor() if back_style.color else ColorTriplet(0, 0, 0)cos = math.cospi = math.pi_Segment = Segment_Style = Stylefrom_triplet = Color.from_tripletfor index in range(PULSE_SIZE):
position = index / PULSE_SIZEfade = 0.5 + cos(position * pi * 2) / 2color = blend_rgb(fore_color, back_color, cross_fade = fade)append(_Segment(bar, _Style(color = from_triplet(color))))segments)()
    
    def update(self = None, completed = None, total = None):
        '''Update progress with new values.

        Args:
            completed (float): Number of steps completed.
            total (float, optional): Total number of steps, or ``None`` to not change. Defaults to None.
        '''
        self.completed = completed
    # WARNING: Decompyle incomplete

    
    def _render_pulse(self = None, console = None, width = None, ascii = (False,)):
        '''Renders the pulse animation.

        Args:
            console (Console): Console instance.
            width (int): Width in characters of pulse animation.

        Returns:
            RenderResult: [description]

        Yields:
            Iterator[Segment]: Segments to render pulse
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete


if __name__ == '__main__':
    console = Console()
    bar = ProgressBar(width = 50, total = 100)
    import time
    console.show_cursor(False)
    for n in range(0, 101, 1):
        bar.update(n)
        console.print(bar)
        console.file.write('\r')
        time.sleep(0.05)
        console.show_cursor(True)
        console.print()
        return None
        return None
