# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: GifImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import itertools
import math
import os
import subprocess
from enum import IntEnum
from functools import cached_property
from typing import Any, NamedTuple, cast
from  import Image, ImageChops, ImageFile, ImageMath, ImageOps, ImagePalette, ImageSequence
from _binary import i16le as i16
from _binary import o8
from _binary import o16le as o16
from _util import DeferredError
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import IO, Literal
    from  import _imaging
    from _typing import Buffer

class LoadingStrategy(IntEnum):
    '''.. versionadded:: 9.1.0'''
    RGB_AFTER_FIRST = 0
    RGB_AFTER_DIFFERENT_PALETTE_ONLY = 1
    RGB_ALWAYS = 2

LOADING_STRATEGY = LoadingStrategy.RGB_AFTER_FIRST

def _accept(prefix = None):
    return prefix.startswith((b'GIF87a', b'GIF89a'))


class GifImageFile(ImageFile.ImageFile):
    pass
# WARNING: Decompyle incomplete

RAWMODE = {
    '1': 'L',
    'L': 'L',
    'P': 'P' }

def _normalize_mode(im = None):
    """
    Takes an image (or frame), returns an image in a mode that is appropriate
    for saving in a Gif.

    It may return the original image, or it may return an image converted to
    palette or 'L' mode.

    :param im: Image object
    :returns: Image object
    """
    if im.mode in RAWMODE:
        im.load()
        return im
# WARNING: Decompyle incomplete

_Palette = bytes | bytearray | list[int] | ImagePalette.ImagePalette

def _normalize_palette(im = None, palette = None, info = None):
    """
    Normalizes the palette for image.
      - Sets the palette to the incoming palette, if provided.
      - Ensures that there's a palette for L mode images
      - Optimizes the palette if necessary/desired.

    :param im: Image object
    :param palette: bytes object containing the source palette, or ....
    :param info: encoderinfo
    :returns: Image object
    """
    source_palette = None
    if palette:
        if isinstance(palette, (bytes, bytearray, list)):
            source_palette = bytearray(palette[:768])
        if isinstance(palette, ImagePalette.ImagePalette):
            source_palette = bytearray(palette.palette)
# WARNING: Decompyle incomplete


def _write_single_frame(im = None, fp = None, palette = None):
    im_out = _normalize_mode(im)
    for k, v in im_out.info.items():
        if isinstance(k, str):
            im.encoderinfo.setdefault(k, v)
        im_out = _normalize_palette(im_out, palette, im.encoderinfo)
        for s in _get_global_header(im_out, im.encoderinfo):
            fp.write(s)
            flags = 0
            if get_interlace(im):
                flags = flags | 64
    _write_local_header(fp, im, (0, 0), flags)
    im_out.encoderconfig = (8, get_interlace(im))
    ImageFile._save(im_out, fp, [
        ImageFile._Tile('gif', (0, 0) + im.size, 0, RAWMODE[im_out.mode])])
    fp.write(b'\x00')


def _getbbox(base_im = None, im_frame = None):
    palette_bytes = (base_im, im_frame)()
    if palette_bytes[0] != palette_bytes[1]:
        im_frame = im_frame.convert('RGBA')
        base_im = base_im.convert('RGBA')
    delta = ImageChops.subtract_modulo(im_frame, base_im)
    return (delta, delta.getbbox(alpha_only = False))


class _Frame(NamedTuple):
    encoderinfo: 'dict[str, Any]' = '_Frame'


def _write_multiple_frames(im = None, fp = None, palette = None):
    duration = im.encoderinfo.get('duration')
    disposal = im.encoderinfo.get('disposal', im.info.get('disposal'))
    im_frames = []
    previous_im = None
    frame_count = 0
    background_im = None
# WARNING: Decompyle incomplete


def _save_all(im = None, fp = None, filename = None):
    _save(im, fp, filename, save_all = True)


def _save(im = None, fp = None, filename = None, save_all = (False,)):
    if 'palette' in im.encoderinfo or 'palette' in im.info:
        palette = im.encoderinfo.get('palette', im.info.get('palette'))
    else:
        palette = None
        im.encoderinfo.setdefault('optimize', True)
    if not save_all or _write_multiple_frames(im, fp, palette):
        _write_single_frame(im, fp, palette)
    fp.write(b';')
    if hasattr(fp, 'flush'):
        fp.flush()
        return None


def get_interlace(im = None):
    interlace = im.encoderinfo.get('interlace', 1)
    if min(im.size) < 16:
        interlace = 0
    return interlace


def _write_local_header(fp = None, im = None, offset = None, flags = ('fp', 'IO[bytes]', 'im', 'Image.Image', 'offset', 'tuple[int, int]', 'flags', 'int', 'return', 'None')):
    
    try:
        transparency = im.encoderinfo['transparency']
    except KeyError:
        transparency = None

    if 'duration' in im.encoderinfo:
        duration = int(im.encoderinfo['duration'] / 10)
    else:
        duration = 0
    disposal = int(im.encoderinfo.get('disposal', 0))
# WARNING: Decompyle incomplete


def _save_netpbm(im = None, fp = None, filename = None):
    tempfile = im._dump()
# WARNING: Decompyle incomplete

_FORCE_OPTIMIZE = False

def _get_optimize(im = None, info = None):
    '''
    Palette optimization is a potentially expensive operation.

    This function determines if the palette should be optimized using
    some heuristics, then returns the list of palette entries in use.

    :param im: Image object
    :param info: encoderinfo
    :returns: list of indexes of palette entries in use, or None
    '''
    pass
# WARNING: Decompyle incomplete


def _get_color_table_size(palette_bytes = None):
    if not palette_bytes:
        return 0
    if None(palette_bytes) < 9:
        return 1
    return None.ceil(math.log(len(palette_bytes) // 3, 2)) - 1


def _get_header_palette(palette_bytes = None):
    '''
    Returns the palette, null padded to the next power of 2 (*3) bytes
    suitable for direct inclusion in the GIF header

    :param palette_bytes: Unpadded palette bytes, in RGBRGB form
    :returns: Null padded palette
    '''
    color_table_size = _get_color_table_size(palette_bytes)
    actual_target_size_diff = (2 << color_table_size) - len(palette_bytes) // 3
    if actual_target_size_diff > 0:
        palette_bytes += o8(0) * 3 * actual_target_size_diff
    return palette_bytes


def _get_palette_bytes(im = None):
    '''
    Gets the palette for inclusion in the gif header

    :param im: Image object
    :returns: Bytes, len<=768 suitable for inclusion in gif header
    '''
    pass
# WARNING: Decompyle incomplete


def _get_background(im = None, info_background = None):
    background = 0
# WARNING: Decompyle incomplete


def _get_global_header(im = None, info = None):
    '''Return a list of strings representing a GIF header'''
    version = b'87a'
# WARNING: Decompyle incomplete


def _write_frame_data(fp = None, im_frame = None, offset = None, params = ('fp', 'IO[bytes]', 'im_frame', 'Image.Image', 'offset', 'tuple[int, int]', 'params', 'dict[str, Any]', 'return', 'None')):
    
    try:
        im_frame.encoderinfo = params
        _write_local_header(fp, im_frame, offset, 0)
        ImageFile._save(im_frame, fp, [
            ImageFile._Tile('gif', (0, 0) + im_frame.size, 0, RAWMODE[im_frame.mode])])
        fp.write(b'\x00')
        del im_frame.encoderinfo
        return None
    except:
        del im_frame.encoderinfo



def getheader(im = None, palette = None, info = None):
    '''
    Legacy Method to get Gif data from image.

    Warning:: May modify image data.

    :param im: Image object
    :param palette: bytes object containing the source palette, or ....
    :param info: encoderinfo
    :returns: tuple of(list of header items, optimized palette)

    '''
    pass
# WARNING: Decompyle incomplete


def getdata(im = None, offset = None, **params):
    '''
    Legacy Method

    Return a list of strings representing this image.
    The first string is a local image header, the rest contains
    encoded image data.

    To specify duration, add the time in milliseconds,
    e.g. ``getdata(im_frame, duration=1000)``

    :param im: Image object
    :param offset: Tuple of (x, y) pixels. Defaults to (0, 0)
    :param \\**params: e.g. duration or other encoder info parameters
    :returns: List of bytes containing GIF encoded frame data

    '''
    BytesIO = BytesIO
    import io
    
    class Collector(BytesIO):
        data = []
        
        def write(self = None, data = None):
            self.data.append(data)
            return len(data)


    im.load()
    fp = Collector()
    _write_frame_data(fp, im, offset, params)
    return fp.data

Image.register_open(GifImageFile.format, GifImageFile, _accept)
Image.register_save(GifImageFile.format, _save)
Image.register_save_all(GifImageFile.format, _save_all)
Image.register_extension(GifImageFile.format, '.gif')
Image.register_mime(GifImageFile.format, 'image/gif')
