# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: Image.pyc (Python 3.11)

from __future__ import annotations
import abc
import atexit
import builtins
import io
import logging
import math
import os
import re
import struct
import sys
import tempfile
import warnings
from collections.abc import MutableMapping
from enum import IntEnum
from typing import IO, Protocol, cast
from  import ExifTags, ImageMode, TiffTags, UnidentifiedImageError, __version__, _plugins
from _binary import i32le, o32be, o32le
from _deprecate import deprecate
from _util import DeferredError, is_path
ElementTree: 'ModuleType | None'

try:
    from defusedxml import ElementTree
except ImportError:
    ElementTree = None

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator, Sequence
    from types import ModuleType
    from typing import Any, Literal
logger = logging.getLogger(__name__)

class DecompressionBombWarning(RuntimeWarning):
    pass


class DecompressionBombError(Exception):
    pass

WARN_POSSIBLE_FORMATS: 'bool' = False
MAX_IMAGE_PIXELS: 'int | None' = int(89478485)

try:
    from  import _imaging as core
    if __version__ != getattr(core, 'PILLOW_VERSION', None):
        msg = f'''The _imaging extension was built for another version of Pillow or PIL:\nCore version: {getattr(core, 'PILLOW_VERSION', None)}\nPillow version: {__version__}'''
        raise ImportError(msg)
except ImportError:
    v = None
    if str(v).startswith('Module use of python'):
        warnings.warn('The _imaging extension was built for another version of Python.', RuntimeWarning)
    elif str(v).startswith('The _imaging extension'):
        warnings.warn(str(v), RuntimeWarning)
    raise 
    v = None
    del v


class Transpose(IntEnum):
    FLIP_LEFT_RIGHT = 0
    FLIP_TOP_BOTTOM = 1
    ROTATE_90 = 2
    ROTATE_180 = 3
    ROTATE_270 = 4
    TRANSPOSE = 5
    TRANSVERSE = 6


class Transform(IntEnum):
    AFFINE = 0
    EXTENT = 1
    PERSPECTIVE = 2
    QUAD = 3
    MESH = 4


class Resampling(IntEnum):
    NEAREST = 0
    BOX = 4
    BILINEAR = 2
    HAMMING = 5
    BICUBIC = 3
    LANCZOS = 1

_filters_support = {
    Resampling.LANCZOS: 3,
    Resampling.BICUBIC: 2,
    Resampling.HAMMING: 1,
    Resampling.BILINEAR: 1,
    Resampling.BOX: 0.5 }

class Dither(IntEnum):
    NONE = 0
    ORDERED = 1
    RASTERIZE = 2
    FLOYDSTEINBERG = 3


class Palette(IntEnum):
    WEB = 0
    ADAPTIVE = 1


class Quantize(IntEnum):
    MEDIANCUT = 0
    MAXCOVERAGE = 1
    FASTOCTREE = 2
    LIBIMAGEQUANT = 3

module = sys.modules[__name__]
for enum in (Transpose, Transform, Resampling, Dither, Palette, Quantize):
    for item in enum:
        setattr(module, item.name, item.value)
        if hasattr(core, 'DEFAULT_STRATEGY'):
            DEFAULT_STRATEGY = core.DEFAULT_STRATEGY
            FILTERED = core.FILTERED
            HUFFMAN_ONLY = core.HUFFMAN_ONLY
            RLE = core.RLE
            FIXED = core.FIXED
TYPE_CHECKING = False
if TYPE_CHECKING:
    import mmap
    from xml.etree.ElementTree import Element
    from IPython.lib.pretty import PrettyPrinter
    from  import ImageFile, ImageFilter, ImagePalette, ImageQt, TiffImagePlugin
    from _typing import CapsuleType, NumpyArray, StrOrBytesPath
ID: 'list[str]' = []
OPEN: 'dict[str, tuple[Callable[[IO[bytes], str | bytes], ImageFile.ImageFile], Callable[[bytes], bool | str] | None]]' = { }
MIME: 'dict[str, str]' = { }
SAVE: 'dict[str, Callable[[Image, IO[bytes], str | bytes], None]]' = { }
SAVE_ALL: 'dict[str, Callable[[Image, IO[bytes], str | bytes], None]]' = { }
EXTENSION: 'dict[str, str]' = { }
DECODERS: 'dict[str, type[ImageFile.PyDecoder]]' = { }
ENCODERS: 'dict[str, type[ImageFile.PyEncoder]]' = { }
_ENDIAN = '<' if sys.byteorder == 'little' else '>'

def _conv_type_shape(im = None):
    m = ImageMode.getmode(im.mode)
    shape = (im.height, im.width)
    extra = len(m.bands)
    if extra != 1:
        shape += (extra,)
    return (shape, m.typestr)

MODES = [
    '1',
    'CMYK',
    'F',
    'HSV',
    'I',
    'I;16',
    'I;16B',
    'I;16L',
    'I;16N',
    'L',
    'LA',
    'La',
    'LAB',
    'P',
    'PA',
    'RGB',
    'RGBA',
    'RGBa',
    'RGBX',
    'YCbCr']
_MAPMODES = ('L', 'P', 'RGBX', 'RGBA', 'CMYK', 'I;16', 'I;16L', 'I;16B')

def getmodebase(mode = None):
    '''
    Gets the "base" mode for given mode.  This function returns "L" for
    images that contain grayscale data, and "RGB" for images that
    contain color data.

    :param mode: Input mode.
    :returns: "L" or "RGB".
    :exception KeyError: If the input mode was not a standard mode.
    '''
    return ImageMode.getmode(mode).basemode


def getmodetype(mode = None):
    '''
    Gets the storage type mode.  Given a mode, this function returns a
    single-layer mode suitable for storing individual bands.

    :param mode: Input mode.
    :returns: "L", "I", or "F".
    :exception KeyError: If the input mode was not a standard mode.
    '''
    return ImageMode.getmode(mode).basetype


def getmodebandnames(mode = None):
    '''
    Gets a list of individual band names.  Given a mode, this function returns
    a tuple containing the names of individual bands (use
    :py:method:`~PIL.Image.getmodetype` to get the mode used to store each
    individual band.

    :param mode: Input mode.
    :returns: A tuple containing band names.  The length of the tuple
        gives the number of bands in an image of the given mode.
    :exception KeyError: If the input mode was not a standard mode.
    '''
    return ImageMode.getmode(mode).bands


def getmodebands(mode = None):
    '''
    Gets the number of individual bands for this mode.

    :param mode: Input mode.
    :returns: The number of bands in this mode.
    :exception KeyError: If the input mode was not a standard mode.
    '''
    return len(ImageMode.getmode(mode).bands)

_initialized = 0

def preinit():
    '''
    Explicitly loads BMP, GIF, JPEG, PPM and PPM file format drivers.

    It is called when opening or saving images.
    '''
    if _initialized >= 1:
        return None
# WARNING: Decompyle incomplete


def init():
    '''
    Explicitly initializes the Python Imaging Library. This function
    loads all available file format drivers.

    It is called when opening or saving images if :py:meth:`~preinit()` is
    insufficient, and by :py:meth:`~PIL.features.pilinfo`.
    '''
    global _initialized
    if _initialized >= 2:
        return False
    parent_name = None.rpartition('.')[0]
    for plugin in _plugins:
        logger.debug('Importing %s', plugin)
        __import__(f'''{parent_name}.{plugin}''', globals(), locals(), [])
        except ImportError:
            e = None
            logger.debug('Image: failed to import %s: %s', plugin, e)
            e = None
            del e
            continue
            e = None
            del e
        if OPEN or SAVE:
            _initialized = 2
            return True
        return None


def _getdecoder(mode = None, decoder_name = None, args = None, extra = ((),)):
    pass
# WARNING: Decompyle incomplete


def _getencoder(mode = None, encoder_name = None, args = None, extra = ((),)):
    pass
# WARNING: Decompyle incomplete


class ImagePointTransform:
    '''
    Used with :py:meth:`~PIL.Image.Image.point` for single band images with more than
    8 bits, this represents an affine transformation, where the value is multiplied by
    ``scale`` and ``offset`` is added.
    '''
    
    def __init__(self = None, scale = None, offset = None):
        self.scale = scale
        self.offset = offset

    
    def __neg__(self = None):
        return ImagePointTransform(-(self.scale), -(self.offset))

    
    def __add__(self = None, other = None):
        if isinstance(other, ImagePointTransform):
            return ImagePointTransform(self.scale + other.scale, self.offset + other.offset)
        return None(self.scale, self.offset + other)

    __radd__ = __add__
    
    def __sub__(self = None, other = None):
        return self + -other

    
    def __rsub__(self = None, other = None):
        return other + -self

    
    def __mul__(self = None, other = None):
        if isinstance(other, ImagePointTransform):
            return NotImplemented
        return None(self.scale * other, self.offset * other)

    __rmul__ = __mul__
    
    def __truediv__(self = None, other = None):
        if isinstance(other, ImagePointTransform):
            return NotImplemented
        return None(self.scale / other, self.offset / other)



def _getscaleoffset(expr = None):
    a = expr(ImagePointTransform(1, 0))
    return (a.scale, a.offset) if isinstance(a, ImagePointTransform) else (0, a)


class SupportsGetData(Protocol):
    
    def getdata(self = None):
        pass



class Image:
    """
    This class represents an image object.  To create
    :py:class:`~PIL.Image.Image` objects, use the appropriate factory
    functions.  There's hardly ever any reason to call the Image constructor
    directly.

    * :py:func:`~PIL.Image.open`
    * :py:func:`~PIL.Image.new`
    * :py:func:`~PIL.Image.frombytes`
    """
    format: 'str | None' = None
    format_description: 'str | None' = None
    _close_exclusive_fp_after_loading = True
    
    def __init__(self = None):
        self._im = None
        self._mode = ''
        self._size = (0, 0)
        self.palette = None
        self.info = { }
        self.readonly = 0
        self._exif = None

    im = (lambda self = None: if isinstance(self._im, DeferredError):
raise self._im.ex# WARNING: Decompyle incomplete
)()
    im = (lambda self = None, im = None: self._im = im)()
    width = (lambda self = None: self.size[0])()
    height = (lambda self = None: self.size[1])()
    size = (lambda self = None: self._size)()
    mode = (lambda self = None: self._mode)()
    readonly = (lambda self = None:
