# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageDraw2.pyc (Python 3.11)

'''
(Experimental) WCK-style drawing interface operations

.. seealso:: :py:mod:`PIL.ImageDraw`
'''
from __future__ import annotations
from typing import Any, AnyStr, BinaryIO
from  import Image, ImageColor, ImageDraw, ImageFont, ImagePath
from _typing import Coords, StrOrBytesPath

class Pen:
    '''Stores an outline color and width.'''
    
    def __init__(self = None, color = None, width = None, opacity = (1, 255)):
        self.color = ImageColor.getrgb(color)
        self.width = width



class Brush:
    '''Stores a fill color'''
    
    def __init__(self = None, color = None, opacity = None):
        self.color = ImageColor.getrgb(color)



class Font:
    '''Stores a TrueType font and color'''
    
    def __init__(self = None, color = None, file = None, size = (12,)):
        self.color = ImageColor.getrgb(color)
        self.font = ImageFont.truetype(file, size)



class Draw:
    '''
    (Experimental) WCK-style drawing interface
    '''
    
    def __init__(self = None, image = None, size = None, color = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self = None):
        return self.image

    
    def render(self = None, op = None, xy = None, pen = (None,), brush = ('op', 'str', 'xy', 'Coords', 'pen', 'Pen | Brush | None', 'brush', 'Brush | Pen | None', 'kwargs', 'Any', 'return', 'None'), **kwargs):
        outline = None
        fill = None
        width = 1
        if isinstance(pen, Pen):
            outline = pen.color
            width = pen.width
        elif isinstance(brush, Pen):
            outline = brush.color
            width = brush.width
        if isinstance(brush, Brush):
            fill = brush.color
        elif isinstance(pen, Brush):
            fill = pen.color
        if self.transform:
            path = ImagePath.Path(xy)
            path.transform(self.transform)
            xy = path
        if op in ('arc', 'line'):
            kwargs.setdefault('fill', outline)
        else:
            kwargs.setdefault('fill', fill)
            kwargs.setdefault('outline', outline)
        if op == 'line':
            kwargs.setdefault('width', width)
    # WARNING: Decompyle incomplete

    
    def settransform(self = None, offset = None):
        '''Sets a transformation offset.'''
        (xoffset, yoffset) = offset
        self.transform = (1, 0, xoffset, 0, 1, yoffset)

    
    def arc(self, xy = None, pen = None, start = None, end = ('xy', 'Coords', 'pen', 'Pen | Brush | None', 'start', 'float', 'end', 'float', 'options', 'Any', 'return', 'None'), *options):
        '''
        Draws an arc (a portion of a circle outline) between the start and end
        angles, inside the given bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.arc`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def chord(self, xy = None, pen = None, start = None, end = ('xy', 'Coords', 'pen', 'Pen | Brush | None', 'start', 'float', 'end', 'float', 'options', 'Any', 'return', 'None'), *options):
        '''
        Same as :py:meth:`~PIL.ImageDraw2.Draw.arc`, but connects the end points
        with a straight line.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.chord`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def ellipse(self = None, xy = None, pen = None, *options):
        '''
        Draws an ellipse inside the given bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.ellipse`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def line(self = None, xy = None, pen = None, *options):
        '''
        Draws a line between the coordinates in the ``xy`` list.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.line`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def pieslice(self, xy = None, pen = None, start = None, end = ('xy', 'Coords', 'pen', 'Pen | Brush | None', 'start', 'float', 'end', 'float', 'options', 'Any', 'return', 'None'), *options):
        '''
        Same as arc, but also draws straight lines between the end points and the
        center of the bounding box.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.pieslice`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def polygon(self = None, xy = None, pen = None, *options):
        '''
        Draws a polygon.

        The polygon outline consists of straight lines between the given
        coordinates, plus a straight line between the last and the first
        coordinate.


        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.polygon`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def rectangle(self = None, xy = None, pen = None, *options):
        '''
        Draws a rectangle.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.rectangle`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def text(self = None, xy = None, text = None, font = ('xy', 'tuple[float, float]', 'text', 'AnyStr', 'font', 'Font', 'return', 'None')):
        '''
        Draws the string at the given position.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.text`
        '''
        if self.transform:
            path = ImagePath.Path(xy)
            path.transform(self.transform)
            xy = path
        self.draw.text(xy, text, font = font.font, fill = font.color)

    
    def textbbox(self = None, xy = None, text = None, font = ('xy', 'tuple[float, float]', 'text', 'AnyStr', 'font', 'Font', 'return', 'tuple[float, float, float, float]')):
        '''
        Returns bounding box (in pixels) of given text.

        :return: ``(left, top, right, bottom)`` bounding box

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.textbbox`
        '''
        if self.transform:
            path = ImagePath.Path(xy)
            path.transform(self.transform)
            xy = path
        return self.draw.textbbox(xy, text, font = font.font)

    
    def textlength(self = None, text = None, font = None):
        '''
        Returns length (in pixels) of given text.
        This is the amount by which following text should be offset.

        .. seealso:: :py:meth:`PIL.ImageDraw.ImageDraw.textlength`
        '''
        return self.draw.textlength(text, font = font.font)
