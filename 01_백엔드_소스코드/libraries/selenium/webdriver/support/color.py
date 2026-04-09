# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Sequence
from re import Match
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from typing import SupportsFloat, SupportsIndex, SupportsInt
    ParseableFloat = SupportsFloat | SupportsIndex | str | bytes | bytearray
    ParseableInt = SupportsInt | SupportsIndex | str | bytes
RGB_PATTERN = '^\\s*rgb\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*\\)\\s*$'
RGB_PCT_PATTERN = '^\\s*rgb\\(\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*,\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*,\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*\\)\\s*$'
RGBA_PATTERN = '^\\s*rgba\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})\\s*,\\s*(0|1|0\\.\\d+)\\s*\\)\\s*$'
RGBA_PCT_PATTERN = '^\\s*rgba\\(\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*,\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*,\\s*(\\d{1,3}|\\d{1,2}\\.\\d+)%\\s*,\\s*(0|1|0\\.\\d+)\\s*\\)\\s*$'
HEX_PATTERN = '#([A-Fa-f0-9]{2})([A-Fa-f0-9]{2})([A-Fa-f0-9]{2})'
HEX3_PATTERN = '#([A-Fa-f0-9])([A-Fa-f0-9])([A-Fa-f0-9])'
HSL_PATTERN = '^\\s*hsl\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})%\\s*,\\s*(\\d{1,3})%\\s*\\)\\s*$'
HSLA_PATTERN = '^\\s*hsla\\(\\s*(\\d{1,3})\\s*,\\s*(\\d{1,3})%\\s*,\\s*(\\d{1,3})%\\s*,\\s*(0|1|0\\.\\d+)\\s*\\)\\s*$'

class Color:
    '''Color conversion support class.

    Example:
    ::

        from selenium.webdriver.support.color import Color

        print(Color.from_string("#00ff33").rgba)
        print(Color.from_string("rgb(1, 255, 3)").hex)
        print(Color.from_string("blue").rgba)
    '''
    from_string = (lambda cls = None, str_ = None: pass# WARNING: Decompyle incomplete
)()
    _from_hsl = (lambda cls = None, h = None, s = classmethod, light = (1,), a = ('h', 'ParseableFloat', 's', 'ParseableFloat', 'light', 'ParseableFloat', 'a', 'ParseableFloat', 'return', 'Color'): h = float(h) / 360s = float(s) / 100_l = float(light) / 100if s == 0:
r = _lg = rb = relif _l < 0.5:
passluminocity2 = _l + s - _l * sluminocity1 = 2 * _l - luminocity2
def hue_to_rgb(lum1 = None, lum2 = None, hue = _l * (1 + s)):
if hue < 0:
hue += 1if hue > 1:
hue -= 1if hue < 0.166667:
lum1 + (lum2 - lum1) * 6 * hueif None < 0.5:
lum2if None < 0.666667:
lum1 + (lum2 - lum1) * (0.666667 - hue) * 6r = hue_to_rgb(luminocity1, luminocity2, h + 0.333333)g = hue_to_rgb(luminocity1, luminocity2, h)b = hue_to_rgb(luminocity1, luminocity2, h - 0.333333)cls(round(r * 255), round(g * 255), round(b * 255), a))()
    
    def __init__(self = None, red = None, green = None, blue = (1,), alpha = ('red', 'ParseableInt', 'green', 'ParseableInt', 'blue', 'ParseableInt', 'alpha', 'ParseableFloat', 'return', 'None')):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)
        if float(alpha) == 1:
            pass
        elif not float(alpha):
            self.alpha = float(alpha)(0)
            return None

    rgb = (lambda self = None: f'''rgb({self.red}, {self.green}, {self.blue})''')()
    rgba = (lambda self = None: f'''rgba({self.red}, {self.green}, {self.blue}, {self.alpha})''')()
    hex = (lambda self = None: f'''#{self.red:02x}{self.green:02x}{self.blue:02x}''')()
    
    def __eq__(self = None, other = None):
        if isinstance(other, Color):
            return self.rgba == other.rgba

    
    def __ne__(self = None, other = None):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not None

    
    def __hash__(self = None):
        return hash((self.red, self.green, self.blue, self.alpha))

    
    def __repr__(self = None):
        return f'''Color(red={self.red}, green={self.green}, blue={self.blue}, alpha={self.alpha})'''

    
    def __str__(self = None):
        return f'''Color: {self.rgba}'''


# WARNING: Decompyle incomplete
