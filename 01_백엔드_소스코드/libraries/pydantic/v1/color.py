# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color.pyc (Python 3.11)

__doc__ = '\nColor definitions are  used as per CSS3 specification:\nhttp://www.w3.org/TR/css3-color/#svg-color\n\nA few colors have multiple names referring to the sames colors, eg. `grey` and `gray` or `aqua` and `cyan`.\n\nIn these cases the LAST color when sorted alphabetically takes preferences,\neg. Color((0, 255, 255)).as_named() == \'cyan\' because "cyan" comes after "aqua".\n'
import math
import re
from colorsys import hls_to_rgb, rgb_to_hls
from typing import TYPE_CHECKING, Any, Dict, Optional, Tuple, Union, cast
from pydantic.v1.errors import ColorError
from pydantic.v1.utils import Representation, almost_equal_floats
if TYPE_CHECKING:
    from pydantic.v1.typing import CallableGenerator, ReprArgs
ColorTuple = Union[(Tuple[(int, int, int)], Tuple[(int, int, int, float)])]
ColorType = Union[(ColorTuple, str)]
HslColorTuple = Union[(Tuple[(float, float, float)], Tuple[(float, float, float, float)])]

class RGBA:
    '''
    Internal use only as a representation of a color.
    '''
    __slots__ = ('r', 'g', 'b', 'alpha', '_tuple')
    
    def __init__(self, r = None, g = None, b = None, alpha = ('r', float, 'g', float, 'b', float, 'alpha', Optional[float])):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha
        self._tuple = (r, g, b, alpha)

    
    def __getitem__(self = None, item = None):
        return self._tuple[item]


r_hex_short = '\\s*(?:#|0x)?([0-9a-f])([0-9a-f])([0-9a-f])([0-9a-f])?\\s*'
r_hex_long = '\\s*(?:#|0x)?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})?\\s*'
_r_255 = '(\\d{1,3}(?:\\.\\d+)?)'
_r_comma = '\\s*,\\s*'
r_rgb = f'''\\s*rgb\\(\\s*{_r_255}{_r_comma}{_r_255}{_r_comma}{_r_255}\\)\\s*'''
_r_alpha = '(\\d(?:\\.\\d+)?|\\.\\d+|\\d{1,2}%)'
r_rgba = f'''\\s*rgba\\(\\s*{_r_255}{_r_comma}{_r_255}{_r_comma}{_r_255}{_r_comma}{_r_alpha}\\s*\\)\\s*'''
_r_h = '(-?\\d+(?:\\.\\d+)?|-?\\.\\d+)(deg|rad|turn)?'
_r_sl = '(\\d{1,3}(?:\\.\\d+)?)%'
r_hsl = f'''\\s*hsl\\(\\s*{_r_h}{_r_comma}{_r_sl}{_r_comma}{_r_sl}\\s*\\)\\s*'''
r_hsla = f'''\\s*hsl\\(\\s*{_r_h}{_r_comma}{_r_sl}{_r_comma}{_r_sl}{_r_comma}{_r_alpha}\\s*\\)\\s*'''
repeat_colors = '0123456789abcdef'()
rads = 2 * math.pi

class Color(Representation):
    __slots__ = ('_original', '_rgba')
    
    def __init__(self = None, value = None):
        self
        self
        if isinstance(value, (tuple, list)):
            self._rgba = parse_tuple(value)
        elif isinstance(value, str):
            self._rgba = parse_str(value)
        elif isinstance(value, Color):
            self._rgba = value._rgba
            value = value._original
        else:
            raise ColorError(reason = 'value must be a tuple, list or string')
        self._original = value

    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'color'))()
    
    def original(self = None):
        '''
        Original value passed to Color
        '''
        return self._original

    
    def as_named(self = None, *, fallback):
        pass
    # WARNING: Decompyle incomplete

    
    def as_hex(self = None):
        '''
        Hex string representing the color can be 3, 4, 6 or 8 characters depending on whether the string
        a "short" representation of the color is possible and whether there\'s an alpha channel.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def as_rgb(self = None):
        '''
        Color as an rgb(<r>, <g>, <b>) or rgba(<r>, <g>, <b>, <a>) string.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def as_rgb_tuple(self = None, *, alpha):
        """
        Color as an RGB or RGBA tuple; red, green and blue are in the range 0 to 255, alpha if included is
        in the range 0 to 1.

        :param alpha: whether to include the alpha channel, options are
          None - (default) include alpha only if it's set (e.g. not None)
          True - always include alpha,
          False - always omit alpha,
        """
        (r, g, b) = self._rgba[:3]()
    # WARNING: Decompyle incomplete

    
    def as_hsl(self = None):
        '''
        Color as an hsl(<h>, <s>, <l>) or hsl(<h>, <s>, <l>, <a>) string.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def as_hsl_tuple(self = None, *, alpha):
        """
        Color as an HSL or HSLA tuple, e.g. hue, saturation, lightness and optionally alpha; all elements are in
        the range 0 to 1.

        NOTE: this is HSL as used in HTML and most other places, not HLS as used in python's colorsys.

        :param alpha: whether to include the alpha channel, options are
          None - (default) include alpha only if it's set (e.g. not None)
          True - always include alpha,
          False - always omit alpha,
        """
        (h, l, s) = rgb_to_hls(self._rgba.r, self._rgba.g, self._rgba.b)
    # WARNING: Decompyle incomplete

    
    def _alpha_float(self = None):
        pass
    # WARNING: Decompyle incomplete

    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    
    def __str__(self = None):
        return self.as_named(fallback = True)

    
    def __repr_args__(self = None):
        return [
            (None, self.as_named(fallback = True))] + [
            ('rgb', self.as_rgb_tuple())]

    
    def __eq__(self = None, other = None):
        if isinstance(other, Color):
            pass
        return self.as_rgb_tuple() == other.as_rgb_tuple()

    
    def __hash__(self = None):
        return hash(self.as_rgb_tuple())



def parse_tuple(value = None):
    '''
    Parse a tuple or list as a color.
    '''
    if len(value) == 3:
        (r, g, b) = value()
        return RGBA(r, g, b, None)
    if None(value) == 4:
        (r, g, b) = value[:3]()
        return RGBA(r, g, b, parse_float_alpha(value[3]))
    raise None(reason = 'tuples must have length 3 or 4')


def parse_str(value = None):
    '''
    Parse a string to an RGBA tuple, trying the following formats (in this order):
    * named color, see COLORS_BY_NAME below
    * hex short eg. `<prefix>fff` (prefix can be `#`, `0x` or nothing)
    * hex long eg. `<prefix>ffffff` (prefix can be `#`, `0x` or nothing)
    * `rgb(<r>, <g>, <b>) `
    * `rgba(<r>, <g>, <b>, <a>)`
    '''
    value_lower = value.lower()
    
    try:
        (r, g, b) = COLORS_BY_NAME[value_lower]
        return ints_to_rgba(r, g, b, None)
    except KeyError:
        pass

    m = re.fullmatch(r_hex_short, value_lower)
# WARNING: Decompyle incomplete


def ints_to_rgba(r = None, g = None, b = None, alpha = ('r', Union[(int, str)], 'g', Union[(int, str)], 'b', Union[(int, str)], 'alpha', Optional[float], 'return', RGBA)):
    return RGBA(parse_color_value(r), parse_color_value(g), parse_color_value(b), parse_float_alpha(alpha))


def parse_color_value(value = None, max_val = None):
    """
    Parse a value checking it's a valid int in the range 0 to max_val and divide by max_val to give a number
    in the range 0 to 1
    """
    
    try:
        color = float(value)
    except ValueError:
        raise ColorError(reason = 'color values must be a valid number')

    if  <= 0, color or 0, color <= max_val:
        pass
    
    return color / max_val
    raise ColorError(reason = f'''color values must be in the range 0 to {max_val}''')


def parse_float_alpha(value = None):
    """
    Parse a value checking it's a valid float in the range 0 to 1
    """
    pass
# WARNING: Decompyle incomplete


def parse_hsl(h = None, h_units = None, sat = None, light = (None,), alpha = ('h', str, 'h_units', str, 'sat', str, 'light', str, 'alpha', Optional[float], 'return', RGBA)):
    '''
    Parse raw hue, saturation, lightness and alpha values and convert to RGBA.
    '''
    l_value = parse_color_value(light, 100)
    s_value = parse_color_value(sat, 100)
    h_value = float(h)
    if h_units in frozenset({None, 'deg'}):
        h_value = (h_value % 360) / 360
    elif h_units == 'rad':
        h_value = (h_value % rads) / rads
    else:
        h_value = h_value % 1
    (r, g, b) = hls_to_rgb(h_value, l_value, s_value)
    return RGBA(r, g, b, alpha)


def float_to_255(c = None):
    return int(round(c * 255))

# WARNING: Decompyle incomplete
