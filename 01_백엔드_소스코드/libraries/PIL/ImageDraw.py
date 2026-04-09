# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageDraw.pyc (Python 3.11)

from __future__ import annotations
import math
import struct
from collections.abc import Sequence
from typing import cast
from  import Image, ImageColor, ImageText
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType
    from typing import Any, AnyStr
    from  import ImageDraw2, ImageFont
    from _typing import Coords, _Ink
Outline: 'Callable[[], Image.core._Outline]' = Image.core.outline

class ImageDraw:
    font: 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None' = None
    
    def __init__(self = None, im = None, mode = None):
        '''
        Create a drawing instance.

        :param im: The image to draw in.
        :param mode: Optional mode to use for color values.  For RGB
           images, this argument can be RGB or RGBA (to blend the
           drawing into the image).  For all other modes, this argument
           must be the same as the image mode.  If omitted, the mode
           defaults to the mode of the image.
        '''
        im._ensure_mutable()
        blend = 0
    # WARNING: Decompyle incomplete

    
    def getfont(self = None):
        '''
        Get the current default font.

        To set the default font for this ImageDraw instance::

            from PIL import ImageDraw, ImageFont
            draw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")

        To set the default font for all future ImageDraw instances::

            from PIL import ImageDraw, ImageFont
            ImageDraw.ImageDraw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")

        If the current default font is ``None``,
        it is initialized with ``ImageFont.load_default()``.

        :returns: An image font.'''
        if not self.font:
            ImageFont = ImageFont
            import 
            self.font = ImageFont.load_default()
        return self.font

    
    def _getfont(self = None, font_size = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _getink(self = None, ink = None, fill = None):
        result_ink = None
        result_fill = None
    # WARNING: Decompyle incomplete

    
    def arc(self, xy = None, start = None, end = None, fill = (None, 1), width = ('xy', 'Coords', 'start', 'float', 'end', 'float', 'fill', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw an arc.'''
        (ink, fill) = self._getink(fill)
    # WARNING: Decompyle incomplete

    
    def bitmap(self = None, xy = None, bitmap = None, fill = (None,)):
        '''Draw a bitmap.'''
        bitmap.load()
        (ink, fill) = self._getink(fill)
    # WARNING: Decompyle incomplete

    
    def chord(self, xy, start = None, end = None, fill = None, outline = (None, None, 1), width = ('xy', 'Coords', 'start', 'float', 'end', 'float', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a chord.'''
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def ellipse(self = None, xy = None, fill = None, outline = (None, None, 1), width = ('xy', 'Coords', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw an ellipse.'''
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def circle(self, xy = None, radius = None, fill = None, outline = (None, None, 1), width = ('xy', 'Sequence[float]', 'radius', 'float', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a circle given center coordinates and a radius.'''
        ellipse_xy = (xy[0] - radius, xy[1] - radius, xy[0] + radius, xy[1] + radius)
        self.ellipse(ellipse_xy, fill, outline, width)

    
    def line(self = None, xy = None, fill = None, width = (None, 0, None), joint = ('xy', 'Coords', 'fill', '_Ink | None', 'width', 'int', 'joint', 'str | None', 'return', 'None')):
        '''Draw a line, or a connected sequence of line segments.'''
        pass
    # WARNING: Decompyle incomplete

    
    def shape(self = None, shape = None, fill = None, outline = (None, None)):
        '''(Experimental) Draw a shape.'''
        shape.close()
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def pieslice(self, xy, start = None, end = None, fill = None, outline = (None, None, 1), width = ('xy', 'Coords', 'start', 'float', 'end', 'float', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a pieslice.'''
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def point(self = None, xy = None, fill = None):
        '''Draw one or more individual pixels.'''
        (ink, fill) = self._getink(fill)
    # WARNING: Decompyle incomplete

    
    def polygon(self = None, xy = None, fill = None, outline = (None, None, 1), width = ('xy', 'Coords', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a polygon.'''
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def regular_polygon(self, bounding_circle, n_sides = None, rotation = None, fill = None, outline = (0, None, None, 1), width = ('bounding_circle', 'Sequence[Sequence[float] | float]', 'n_sides', 'int', 'rotation', 'float', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a regular polygon.'''
        xy = _compute_regular_polygon_vertices(bounding_circle, n_sides, rotation)
        self.polygon(xy, fill, outline, width)

    
    def rectangle(self = None, xy = None, fill = None, outline = (None, None, 1), width = ('xy', 'Coords', 'fill', '_Ink | None', 'outline', '_Ink | None', 'width', 'int', 'return', 'None')):
        '''Draw a rectangle.'''
        (ink, fill_ink) = self._getink(outline, fill)
    # WARNING: Decompyle incomplete

    
    def rounded_rectangle(self = None, xy = None, radius = None, fill = None, outline = (0, None, None, 1), width = {
        'corners': None }, *, corners):
        '''Draw a rounded rectangle.'''
        pass
    # WARNING: Decompyle incomplete

    
    def text(self, xy, text, fill, font, anchor, spacing, align, direction, features = None, language = None, stroke_width = None, stroke_fill = (None, None, None, 4, 'left', None, None, None, 0, None, False), embedded_color = ('xy', 'tuple[float, float]', 'text', 'AnyStr | ImageText.Text', 'fill', '_Ink | None', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'anchor', 'str | None', 'spacing', 'float', 'align', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'stroke_fill', '_Ink | None', 'embedded_color', 'bool', 'args', 'Any', 'kwargs', 'Any', 'return', 'None'), *args, **kwargs):
        '''Draw text.'''
        pass
    # WARNING: Decompyle incomplete

    
    def multiline_text(self, xy, text, fill, font, anchor, spacing, align = None, direction = None, features = None, language = None, stroke_width = (None, None, None, 4, 'left', None, None, None, 0, None, False), stroke_fill = {
        'font_size': None }, embedded_color = ('xy', 'tuple[float, float]', 'text', 'AnyStr', 'fill', '_Ink | None', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'anchor', 'str | None', 'spacing', 'float', 'align', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'stroke_fill', '_Ink | None', 'embedded_color', 'bool', 'font_size', 'float | None', 'return', 'None'), *, font_size):
        return self.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color, font_size = font_size)

    
    def textlength(self = None, text = None, font = None, direction = None, features = (None, None, None, None, False), language = {
        'font_size': None }, embedded_color = ('text', 'AnyStr', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'embedded_color', 'bool', 'font_size', 'float | None', 'return', 'float'), *, font_size):
        '''Get the length of a given string, in pixels with 1/64 precision.'''
        pass
    # WARNING: Decompyle incomplete

    
    def textbbox(self, xy, text, font, anchor, spacing = None, align = None, direction = None, features = None, language = (None, None, 4, 'left', None, None, None, 0, False), stroke_width = {
        'font_size': None }, embedded_color = ('xy', 'tuple[float, float]', 'text', 'AnyStr', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'anchor', 'str | None', 'spacing', 'float', 'align', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'embedded_color', 'bool', 'font_size', 'float | None', 'return', 'tuple[float, float, float, float]'), *, font_size):
        '''Get the bounding box of a given string, in pixels.'''
        pass
    # WARNING: Decompyle incomplete

    
    def multiline_textbbox(self, xy, text, font, anchor, spacing = None, align = None, direction = None, features = None, language = (None, None, 4, 'left', None, None, None, 0, False), stroke_width = {
        'font_size': None }, embedded_color = ('xy', 'tuple[float, float]', 'text', 'AnyStr', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'anchor', 'str | None', 'spacing', 'float', 'align', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'embedded_color', 'bool', 'font_size', 'float | None', 'return', 'tuple[float, float, float, float]'), *, font_size):
        return self.textbbox(xy, text, font, anchor, spacing, align, direction, features, language, stroke_width, embedded_color, font_size = font_size)



def Draw(im = None, mode = None):
    '''
    A simple 2D drawing interface for PIL images.

    :param im: The image to draw in.
    :param mode: Optional mode to use for color values.  For RGB
       images, this argument can be RGB or RGBA (to blend the
       drawing into the image).  For all other modes, this argument
       must be the same as the image mode.  If omitted, the mode
       defaults to the mode of the image.
    '''
    
    try:
        return getattr(im, 'getdraw')(mode)
    except AttributeError:
        return 



def getdraw(im = None):
    '''
    :param im: The image to draw in.
    :returns: A (drawing context, drawing resource factory) tuple.
    '''
    ImageDraw2 = ImageDraw2
    import 
# WARNING: Decompyle incomplete


def floodfill(image = None, xy = None, value = None, border = (None, 0), thresh = ('image', 'Image.Image', 'xy', 'tuple[int, int]', 'value', 'float | tuple[int, ...]', 'border', 'float | tuple[int, ...] | None', 'thresh', 'float', 'return', 'None')):
    """
    .. warning:: This method is experimental.

    Fills a bounded region with a given color.

    :param image: Target image.
    :param xy: Seed position (a 2-item coordinate tuple). See
        :ref:`coordinate-system`.
    :param value: Fill color.
    :param border: Optional border value.  If given, the region consists of
        pixels with a color different from the border color.  If not given,
        the region consists of pixels having the same color as the seed
        pixel.
    :param thresh: Optional threshold value which specifies a maximum
        tolerable difference of a pixel value from the 'background' in
        order for it to be replaced. Useful for filling regions of
        non-homogeneous, but similar, colors.
    """
    pixel = image.load()
# WARNING: Decompyle incomplete


def _compute_regular_polygon_vertices(bounding_circle = None, n_sides = None, rotation = None):
    '''
    Generate a list of vertices for a 2D regular polygon.

    :param bounding_circle: The bounding circle is a sequence defined
        by a point and radius. The polygon is inscribed in this circle.
        (e.g. ``bounding_circle=(x, y, r)`` or ``((x, y), r)``)
    :param n_sides: Number of sides
        (e.g. ``n_sides=3`` for a triangle, ``6`` for a hexagon)
    :param rotation: Apply an arbitrary rotation to the polygon
        (e.g. ``rotation=90``, applies a 90 degree rotation)
    :return: List of regular polygon vertices
        (e.g. ``[(25, 50), (50, 50), (50, 25), (25, 25)]``)

    How are the vertices computed?
    1. Compute the following variables
        - theta: Angle between the apothem & the nearest polygon vertex
        - side_length: Length of each polygon edge
        - centroid: Center of bounding circle (1st, 2nd elements of bounding_circle)
        - polygon_radius: Polygon radius (last element of bounding_circle)
        - angles: Location of each polygon vertex in polar grid
            (e.g. A square with 0 degree rotation => [225.0, 315.0, 45.0, 135.0])

    2. For each angle in angles, get the polygon vertex at that angle
        The vertex is computed using the equation below.
            X= xcos(φ) + ysin(φ)
            Y= −xsin(φ) + ycos(φ)

        Note:
            φ = angle in degrees
            x = 0
            y = polygon_radius

        The formula above assumes rotation around the origin.
        In our case, we are rotating around the centroid.
        To account for this, we use the formula below
            X = xcos(φ) + ysin(φ) + centroid_x
            Y = −xsin(φ) + ycos(φ) + centroid_y
    '''
    pass
# WARNING: Decompyle incomplete


def _color_diff(color1 = None, color2 = None):
    '''
    Uses 1-norm distance to calculate difference between two values.
    '''
    pass
# WARNING: Decompyle incomplete
