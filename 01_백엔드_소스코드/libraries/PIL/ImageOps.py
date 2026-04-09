# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageOps.pyc (Python 3.11)

from __future__ import annotations
import functools
import operator
import re
from collections.abc import Sequence
from typing import Literal, Protocol, cast, overload
from  import ExifTags, Image, ImagePalette

def _border(border = None):
    if isinstance(border, tuple):
        if len(border) == 2:
            (left, top) = border
            (right, bottom) = border
        elif len(border) == 4:
            (left, top, right, bottom) = border
        else:
            left = border
            top = border
            right = border
            bottom = border
    return (left, top, right, bottom)


def _color(color = None, mode = None):
    if isinstance(color, str):
        ImageColor = ImageColor
        import 
        color = ImageColor.getcolor(color, mode)
    return color


def _lut(image = None, lut = None):
    if image.mode == 'P':
        msg = 'mode P support coming soon'
        raise NotImplementedError(msg)
    if image.mode in ('L', 'RGB'):
        if image.mode == 'RGB' and len(lut) == 256:
            lut = lut + lut + lut
        return image.point(lut)
    msg = f'''{image.mode}'''
    raise OSError(msg)


def autocontrast(image = None, cutoff = None, ignore = None, mask = (0, None, None, False), preserve_tone = ('image', 'Image.Image', 'cutoff', 'float | tuple[float, float]', 'ignore', 'int | Sequence[int] | None', 'mask', 'Image.Image | None', 'preserve_tone', 'bool', 'return', 'Image.Image')):
    '''
    Maximize (normalize) image contrast. This function calculates a
    histogram of the input image (or mask region), removes ``cutoff`` percent of the
    lightest and darkest pixels from the histogram, and remaps the image
    so that the darkest pixel becomes black (0), and the lightest
    becomes white (255).

    :param image: The image to process.
    :param cutoff: The percent to cut off from the histogram on the low and
                   high ends. Either a tuple of (low, high), or a single
                   number for both.
    :param ignore: The background pixel value (use None for no background).
    :param mask: Histogram used in contrast operation is computed using pixels
                 within the mask. If no mask is given the entire image is used
                 for histogram computation.
    :param preserve_tone: Preserve image tone in Photoshop-like style autocontrast.

                          .. versionadded:: 8.2.0

    :return: An image.
    '''
    if preserve_tone:
        histogram = image.convert('L').histogram(mask)
    else:
        histogram = image.histogram(mask)
    lut = []
# WARNING: Decompyle incomplete


def colorize(image, black, white = None, mid = None, blackpoint = None, whitepoint = (None, 0, 255, 127), midpoint = ('image', 'Image.Image', 'black', 'str | tuple[int, ...]', 'white', 'str | tuple[int, ...]', 'mid', 'str | int | tuple[int, ...] | None', 'blackpoint', 'int', 'whitepoint', 'int', 'midpoint', 'int', 'return', 'Image.Image')):
    '''
    Colorize grayscale image.
    This function calculates a color wedge which maps all black pixels in
    the source image to the first color and all white pixels to the
    second color. If ``mid`` is specified, it uses three-color mapping.
    The ``black`` and ``white`` arguments should be RGB tuples or color names;
    optionally you can use three-color mapping by also specifying ``mid``.
    Mapping positions for any of the colors can be specified
    (e.g. ``blackpoint``), where these parameters are the integer
    value corresponding to where the corresponding color should be mapped.
    These parameters must have logical order, such that
    ``blackpoint <= midpoint <= whitepoint`` (if ``mid`` is specified).

    :param image: The image to colorize.
    :param black: The color to use for black input pixels.
    :param white: The color to use for white input pixels.
    :param mid: The color to use for midtone input pixels.
    :param blackpoint: an int value [0, 255] for the black mapping.
    :param whitepoint: an int value [0, 255] for the white mapping.
    :param midpoint: an int value [0, 255] for the midtone mapping.
    :return: An image.
    '''
    pass
# WARNING: Decompyle incomplete


def contain(image = None, size = None, method = None):
    '''
    Returns a resized version of the image, set to the maximum width and height
    within the requested size, while maintaining the original aspect ratio.

    :param image: The image to resize.
    :param size: The requested output size in pixels, given as a
                 (width, height) tuple.
    :param method: Resampling method to use. Default is
                   :py:attr:`~PIL.Image.Resampling.BICUBIC`.
                   See :ref:`concept-filters`.
    :return: An image.
    '''
    im_ratio = image.width / image.height
    dest_ratio = size[0] / size[1]
    if im_ratio != dest_ratio:
        if im_ratio > dest_ratio:
            new_height = round((image.height / image.width) * size[0])
            if new_height != size[1]:
                size = (size[0], new_height)
            else:
                new_width = round((image.width / image.height) * size[1])
                if new_width != size[0]:
                    size = (new_width, size[1])
    return image.resize(size, resample = method)


def cover(image = None, size = None, method = None):
    '''
    Returns a resized version of the image, so that the requested size is
    covered, while maintaining the original aspect ratio.

    :param image: The image to resize.
    :param size: The requested output size in pixels, given as a
                 (width, height) tuple.
    :param method: Resampling method to use. Default is
                   :py:attr:`~PIL.Image.Resampling.BICUBIC`.
                   See :ref:`concept-filters`.
    :return: An image.
    '''
    im_ratio = image.width / image.height
    dest_ratio = size[0] / size[1]
    if im_ratio != dest_ratio:
        if im_ratio < dest_ratio:
            new_height = round((image.height / image.width) * size[0])
            if new_height != size[1]:
                size = (size[0], new_height)
            else:
                new_width = round((image.width / image.height) * size[1])
                if new_width != size[0]:
                    size = (new_width, size[1])
    return image.resize(size, resample = method)


def pad(image = None, size = None, method = None, color = (Image.Resampling.BICUBIC, None, (0.5, 0.5)), centering = ('image', 'Image.Image', 'size', 'tuple[int, int]', 'method', 'int', 'color', 'str | int | tuple[int, ...] | None', 'centering', 'tuple[float, float]', 'return', 'Image.Image')):
    '''
    Returns a resized and padded version of the image, expanded to fill the
    requested aspect ratio and size.

    :param image: The image to resize and crop.
    :param size: The requested output size in pixels, given as a
                 (width, height) tuple.
    :param method: Resampling method to use. Default is
                   :py:attr:`~PIL.Image.Resampling.BICUBIC`.
                   See :ref:`concept-filters`.
    :param color: The background color of the padded image.
    :param centering: Control the position of the original image within the
                      padded version.

                          (0.5, 0.5) will keep the image centered
                          (0, 0) will keep the image aligned to the top left
                          (1, 1) will keep the image aligned to the bottom
                          right
    :return: An image.
    '''
    resized = contain(image, size, method)
    if resized.size == size:
        out = resized
# WARNING: Decompyle incomplete


def crop(image = None, border = None):
    '''
    Remove border from image.  The same amount of pixels are removed
    from all four sides.  This function works on all image modes.

    .. seealso:: :py:meth:`~PIL.Image.Image.crop`

    :param image: The image to crop.
    :param border: The number of pixels to remove.
    :return: An image.
    '''
    (left, top, right, bottom) = _border(border)
    return image.crop((left, top, image.size[0] - right, image.size[1] - bottom))


def scale(image = None, factor = None, resample = None):
    '''
    Returns a rescaled image by a specific factor given in parameter.
    A factor greater than 1 expands the image, between 0 and 1 contracts the
    image.

    :param image: The image to rescale.
    :param factor: The expansion factor, as a float.
    :param resample: Resampling method to use. Default is
                     :py:attr:`~PIL.Image.Resampling.BICUBIC`.
                     See :ref:`concept-filters`.
    :returns: An :py:class:`~PIL.Image.Image` object.
    '''
    if factor == 1:
        return image.copy()
    if None <= 0:
        msg = 'the factor must be greater than 0'
        raise ValueError(msg)
    size = (round(factor * image.width), round(factor * image.height))
    return image.resize(size, resample)


class SupportsGetMesh(Protocol):
    '''
    An object that supports the ``getmesh`` method, taking an image as an
    argument, and returning a list of tuples. Each tuple contains two tuples,
    the source box as a tuple of 4 integers, and a tuple of 8 integers for the
    final quadrilateral, in order of top left, bottom left, bottom right, top
    right.
    '''
    
    def getmesh(self = None, image = None):
        pass



def deform(image = None, deformer = None, resample = None):
    '''
    Deform the image.

    :param image: The image to deform.
    :param deformer: A deformer object.  Any object that implements a
                    ``getmesh`` method can be used.
    :param resample: An optional resampling filter. Same values possible as
       in the PIL.Image.transform function.
    :return: An image.
    '''
    return image.transform(image.size, Image.Transform.MESH, deformer.getmesh(image), resample)


def equalize(image = None, mask = None):
    '''
    Equalize the image histogram. This function applies a non-linear
    mapping to the input image, in order to create a uniform
    distribution of grayscale values in the output image.

    :param image: The image to equalize.
    :param mask: An optional mask.  If given, only the pixels selected by
                 the mask are included in the analysis.
    :return: An image.
    '''
    if image.mode == 'P':
        image = image.convert('RGB')
    h = image.histogram(mask)
    lut = []
    for b in range(0, len(h), 256):
        histo = h[b:b + 256]()
        if len(histo) <= 1:
            lut.extend(list(range(256)))
            continue
        step = (functools.reduce(operator.add, histo) - histo[-1]) // 255
        if not step:
            lut.extend(list(range(256)))
            continue
        n = step // 2
        for i in range(256):
            lut.append(n // step)
            n = n + h[i + b]
            return _lut(image, lut)


def expand(image = None, border = None, fill = None):
    '''
    Add border to the image

    :param image: The image to expand.
    :param border: Border width, in pixels.
    :param fill: Pixel fill value (a color value).  Default is 0 (black).
    :return: An image.
    '''
    (left, top, right, bottom) = _border(border)
    width = left + image.size[0] + right
    height = top + image.size[1] + bottom
    color = _color(fill, image.mode)
    if image.palette:
        mode = image.palette.mode
        palette = ImagePalette.ImagePalette(mode, image.getpalette(mode))
        if isinstance(color, tuple):
            if len(color) == 3 or len(color) == 4:
                color = palette.getcolor(color)
            else:
                palette = None
    out = Image.new(image.mode, (width, height), color)
    if palette:
        out.putpalette(palette.palette, mode)
    out.paste(image, (left, top))
    return out


def fit(image = None, size = None, method = None, bleed = (Image.Resampling.BICUBIC, 0, (0.5, 0.5)), centering = ('image', 'Image.Image', 'size', 'tuple[int, int]', 'method', 'int', 'bleed', 'float', 'centering', 'tuple[float, float]', 'return', 'Image.Image')):
    '''
    Returns a resized and cropped version of the image, cropped to the
    requested aspect ratio and size.

    This function was contributed by Kevin Cazabon.

    :param image: The image to resize and crop.
    :param size: The requested output size in pixels, given as a
                 (width, height) tuple.
    :param method: Resampling method to use. Default is
                   :py:attr:`~PIL.Image.Resampling.BICUBIC`.
                   See :ref:`concept-filters`.
    :param bleed: Remove a border around the outside of the image from all
                  four edges. The value is a decimal percentage (use 0.01 for
                  one percent). The default value is 0 (no border).
                  Cannot be greater than or equal to 0.5.
    :param centering: Control the cropping position.  Use (0.5, 0.5) for
                      center cropping (e.g. if cropping the width, take 50% off
                      of the left side, and therefore 50% off the right side).
                      (0.0, 0.0) will crop from the top left corner (i.e. if
                      cropping the width, take all of the crop off of the right
                      side, and if cropping the height, take all of it off the
                      bottom).  (1.0, 0.0) will crop from the bottom left
                      corner, etc. (i.e. if cropping the width, take all of the
                      crop off the left side, and if cropping the height take
                      none from the top, and therefore all off the bottom).
    :return: An image.
    '''
    (centering_x, centering_y) = centering
    if not  <= 0, centering_x or 0, centering_x <= 1:
        pass
    
    if not  <= 0, centering_y or 0, centering_y <= 1:
        pass
    else:
        0.5
    if not  <= 0, bleed or 0, bleed < 0.5:
        pass
    else:
        0.5
    (bleed * image.size[0], bleed * image.size[1], bleed_pixels) = 0
    live_size = (image.size[0] - bleed_pixels[0] * 2, image.size[1] - bleed_pixels[1] * 2)
    live_size_ratio = live_size[0] / live_size[1]
    output_ratio = size[0] / size[1]
    if live_size_ratio == output_ratio:
        crop_width = live_size[0]
        crop_height = live_size[1]
    elif live_size_ratio >= output_ratio:
        crop_width = output_ratio * live_size[1]
        crop_height = live_size[1]
    else:
        crop_width = live_size[0]
        crop_height = live_size[0] / output_ratio
    crop_left = bleed_pixels[0] + (live_size[0] - crop_width) * centering_x
    crop_top = bleed_pixels[1] + (live_size[1] - crop_height) * centering_y
    crop = (crop_left, crop_top, crop_left + crop_width, crop_top + crop_height)
    return image.resize(size, method, box = crop)


def flip(image = None):
    '''
    Flip the image vertically (top to bottom).

    :param image: The image to flip.
    :return: An image.
    '''
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)


def grayscale(image = None):
    '''
    Convert the image to grayscale.

    :param image: The image to convert.
    :return: An image.
    '''
    return image.convert('L')


def invert(image = None):
    '''
    Invert (negate) the image.

    :param image: The image to invert.
    :return: An image.
    '''
    lut = list(range(255, -1, -1))
    return image.point(lut) if image.mode == '1' else _lut(image, lut)


def mirror(image = None):
    '''
    Flip image horizontally (left to right).

    :param image: The image to mirror.
    :return: An image.
    '''
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)


def posterize(image = None, bits = None):
    '''
    Reduce the number of bits for each color channel.

    :param image: The image to posterize.
    :param bits: The number of bits to keep for each channel (1-8).
    :return: An image.
    '''
    pass
# WARNING: Decompyle incomplete


def solarize(image = None, threshold = None):
    '''
    Invert all pixel values above a threshold.

    :param image: The image to solarize.
    :param threshold: All pixels above this grayscale level are inverted.
    :return: An image.
    '''
    lut = []
    for i in range(256):
        if i < threshold:
            lut.append(i)
            continue
        lut.append(255 - i)
        return _lut(image, lut)

exif_transpose = (lambda image = None, *, in_place: pass)()
exif_transpose = (lambda image = None, *, in_place: pass)()

def exif_transpose(image = None, *, in_place):
    '''
    If an image has an EXIF Orientation tag, other than 1, transpose the image
    accordingly, and remove the orientation data.

    :param image: The image to transpose.
    :param in_place: Boolean. Keyword-only argument.
        If ``True``, the original image is modified in-place, and ``None`` is returned.
        If ``False`` (default), a new :py:class:`~PIL.Image.Image` object is returned
        with the transposition applied. If there is no transposition, a copy of the
        image will be returned.
    '''
    pass
# WARNING: Decompyle incomplete
