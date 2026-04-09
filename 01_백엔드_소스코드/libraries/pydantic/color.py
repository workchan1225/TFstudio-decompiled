# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color.pyc (Python 3.11)

__doc__ = 'Color definitions are used as per the CSS3\n[CSS Color Module Level 3](http://www.w3.org/TR/css3-color/#svg-color) specification.\n\nA few colors have multiple names referring to the sames colors, eg. `grey` and `gray` or `aqua` and `cyan`.\n\nIn these cases the _last_ color when sorted alphabetically takes preferences,\neg. `Color((0, 255, 255)).as_named() == \'cyan\'` because "cyan" comes after "aqua".\n\nWarning: Deprecated\n    The `Color` class is deprecated, use `pydantic_extra_types` instead.\n    See [`pydantic-extra-types.Color`](../usage/types/extra_types/color_types.md)\n    for more information.\n'
import math
import re
from colorsys import hls_to_rgb, rgb_to_hls
from typing import Any, Callable, Optional, Union, cast
from pydantic_core import CoreSchema, PydanticCustomError, core_schema
from typing_extensions import deprecated
from _internal import _repr
from _internal._schema_generation_shared import GetJsonSchemaHandler as _GetJsonSchemaHandler
from json_schema import JsonSchemaValue
from warnings import PydanticDeprecatedSince20
ColorTuple = Union[(tuple[(int, int, int)], tuple[(int, int, int, float)])]
ColorType = Union[(ColorTuple, str)]
HslColorTuple = Union[(tuple[(float, float, float)], tuple[(float, float, float, float)])]

class RGBA:
    '''Internal use only as a representation of a color.'''
    __slots__ = ('r', 'g', 'b', 'alpha', '_tuple')
    
    def __init__(self, r = None, g = None, b = None, alpha = ('r', float, 'g', float, 'b', float, 'alpha', Optional[float])):
        self.r = r
        self.g = g
        self.b = b
        self.alpha = alpha
        self._tuple = (r, g, b, alpha)

    
    def __getitem__(self = None, item = None):
        return self._tuple[item]


_r_255 = '(\\d{1,3}(?:\\.\\d+)?)'
_r_comma = '\\s*,\\s*'
_r_alpha = '(\\d(?:\\.\\d+)?|\\.\\d+|\\d{1,2}%)'
_r_h = '(-?\\d+(?:\\.\\d+)?|-?\\.\\d+)(deg|rad|turn)?'
_r_sl = '(\\d{1,3}(?:\\.\\d+)?)%'
r_hex_short = '\\s*(?:#|0x)?([0-9a-f])([0-9a-f])([0-9a-f])([0-9a-f])?\\s*'
r_hex_long = '\\s*(?:#|0x)?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})?\\s*'
r_rgb = f'''\\s*rgba?\\(\\s*{_r_255}{_r_comma}{_r_255}{_r_comma}{_r_255}(?:{_r_comma}{_r_alpha})?\\s*\\)\\s*'''
r_hsl = f'''\\s*hsla?\\(\\s*{_r_h}{_r_comma}{_r_sl}{_r_comma}{_r_sl}(?:{_r_comma}{_r_alpha})?\\s*\\)\\s*'''
r_rgb_v4_style = f'''\\s*rgba?\\(\\s*{_r_255}\\s+{_r_255}\\s+{_r_255}(?:\\s*/\\s*{_r_alpha})?\\s*\\)\\s*'''
r_hsl_v4_style = f'''\\s*hsla?\\(\\s*{_r_h}\\s+{_r_sl}\\s+{_r_sl}(?:\\s*/\\s*{_r_alpha})?\\s*\\)\\s*'''
repeat_colors = '0123456789abcdef'()
rads = 2 * math.pi
Color = <NODE:12>()

def parse_tuple(value = None):
    '''Parse a tuple or list to get RGBA values.

    Args:
        value: A tuple or list.

    Returns:
        An `RGBA` tuple parsed from the input tuple.

    Raises:
        PydanticCustomError: If tuple is not valid.
    '''
    if len(value) == 3:
        (r, g, b) = value()
        return RGBA(r, g, b, None)
    if None(value) == 4:
        (r, g, b) = value[:3]()
        return RGBA(r, g, b, parse_float_alpha(value[3]))
    raise None('color_error', 'value is not a valid color: tuples must have length 3 or 4')


def parse_str(value = None):
    '''Parse a string representing a color to an RGBA tuple.

    Possible formats for the input string include:

    * named color, see `COLORS_BY_NAME`
    * hex short eg. `<prefix>fff` (prefix can be `#`, `0x` or nothing)
    * hex long eg. `<prefix>ffffff` (prefix can be `#`, `0x` or nothing)
    * `rgb(<r>, <g>, <b>)`
    * `rgba(<r>, <g>, <b>, <a>)`

    Args:
        value: A string representing a color.

    Returns:
        An `RGBA` tuple parsed from the input string.

    Raises:
        ValueError: If the input string cannot be parsed to an RGBA tuple.
    '''
    value_lower = value.lower()
    
    try:
        (r, g, b) = COLORS_BY_NAME[value_lower]
        return ints_to_rgba(r, g, b, None)
    except KeyError:
        pass

    m = re.fullmatch(r_hex_short, value_lower)
# WARNING: Decompyle incomplete


def ints_to_rgba(r = None, g = None, b = None, alpha = (None,)):
    '''Converts integer or string values for RGB color and an optional alpha value to an `RGBA` object.

    Args:
        r: An integer or string representing the red color value.
        g: An integer or string representing the green color value.
        b: An integer or string representing the blue color value.
        alpha: A float representing the alpha value. Defaults to None.

    Returns:
        An instance of the `RGBA` class with the corresponding color and alpha values.
    '''
    return RGBA(parse_color_value(r), parse_color_value(g), parse_color_value(b), parse_float_alpha(alpha))


def parse_color_value(value = None, max_val = None):
    '''Parse the color value provided and return a number between 0 and 1.

    Args:
        value: An integer or string color value.
        max_val: Maximum range value. Defaults to 255.

    Raises:
        PydanticCustomError: If the value is not a valid color.

    Returns:
        A number between 0 and 1.
    '''
    
    try:
        color = float(value)
    except ValueError:
        raise PydanticCustomError('color_error', 'value is not a valid color: color values must be a valid number')

    if  <= 0, color or 0, color <= max_val:
        pass
    
    return color / max_val
    raise PydanticCustomError('color_error', 'value is not a valid color: color values must be in the range 0 to {max_val}', {
        'max_val': max_val })


def parse_float_alpha(value = None):
    """Parse an alpha value checking it's a valid float in the range 0 to 1.

    Args:
        value: The input value to parse.

    Returns:
        The parsed value as a float, or `None` if the value was None or equal 1.

    Raises:
        PydanticCustomError: If the input value cannot be successfully parsed as a float in the expected range.
    """
    pass
# WARNING: Decompyle incomplete


def parse_hsl(h = None, h_units = None, sat = None, light = (None,), alpha = ('h', str, 'h_units', str, 'sat', str, 'light', str, 'alpha', Optional[float], 'return', RGBA)):
    '''Parse raw hue, saturation, lightness, and alpha values and convert to RGBA.

    Args:
        h: The hue value.
        h_units: The unit for hue value.
        sat: The saturation value.
        light: The lightness value.
        alpha: Alpha value.

    Returns:
        An instance of `RGBA`.
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
    return RGBA(r, g, b, parse_float_alpha(alpha))


def float_to_255(c = None):
    '''Converts a float value between 0 and 1 (inclusive) to an integer between 0 and 255 (inclusive).

    Args:
        c: The float value to be converted. Must be between 0 and 1 (inclusive).

    Returns:
        The integer equivalent of the given float value rounded to the nearest whole number.

    Raises:
        ValueError: If the given float value is outside the acceptable range of 0 to 1 (inclusive).
    '''
    return int(round(c * 255))

# WARNING: Decompyle incomplete
