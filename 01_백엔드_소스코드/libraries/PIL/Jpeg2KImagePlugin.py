# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: Jpeg2KImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import os
import struct
from typing import cast
from  import Image, ImageFile, ImagePalette, _binary
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import IO

class BoxReader:
    '''
    A small helper class to read fields stored in JPEG2000 header boxes
    and to easily step into and read sub-boxes.
    '''
    
    def __init__(self = None, fp = None, length = None):
        self.fp = fp
        self.has_length = length >= 0
        self.length = length
        self.remaining_in_box = -1

    
    def _can_read(self = None, num_bytes = None):
        if self.has_length and self.fp.tell() + num_bytes > self.length:
            return False
        if None.remaining_in_box >= 0:
            return num_bytes <= self.remaining_in_box

    
    def _read_bytes(self = None, num_bytes = None):
        if not self._can_read(num_bytes):
            msg = 'Not enough data in header'
            raise SyntaxError(msg)
        data = self.fp.read(num_bytes)
        if len(data) < num_bytes:
            msg = f'''Expected to read {num_bytes} bytes but only got {len(data)}.'''
            raise OSError(msg)
        if self.remaining_in_box > 0:
            pass
        return data

    
    def read_fields(self = None, field_format = None):
        size = struct.calcsize(field_format)
        data = self._read_bytes(size)
        return struct.unpack(field_format, data)

    
    def read_boxes(self = None):
        size = self.remaining_in_box
        data = self._read_bytes(size)
        return BoxReader(io.BytesIO(data), size)

    
    def has_next_box(self = None):
        if self.has_length:
            return self.fp.tell() + self.remaining_in_box < self.length

    
    def next_box_type(self = None):
        if self.remaining_in_box > 0:
            self.fp.seek(self.remaining_in_box, os.SEEK_CUR)
        self.remaining_in_box = -1
        (lbox, tbox) = cast(tuple[(int, bytes)], self.read_fields('>I4s'))
        if lbox == 1:
            lbox = cast(int, self.read_fields('>Q')[0])
            hlen = 16
        else:
            hlen = 8
        if not lbox < hlen or self._can_read(lbox - hlen):
            msg = 'Invalid header length'
            raise SyntaxError(msg)
        self.remaining_in_box = lbox - hlen
        return tbox



def _parse_codestream(fp = None):
    '''Parse the JPEG 2000 codestream to extract the size and component
    count from the SIZ marker segment, returning a PIL (size, mode) tuple.'''
    hdr = fp.read(2)
    lsiz = _binary.i16be(hdr)
    siz = hdr + fp.read(lsiz - 2)
    (lsiz, rsiz, xsiz, ysiz, xosiz, yosiz, _, _, _, _, csiz) = struct.unpack_from('>HHIIIIIIIIH', siz)
    size = (xsiz - xosiz, ysiz - yosiz)
    if csiz == 1:
        ssiz = struct.unpack_from('>B', siz, 38)
        if (ssiz[0] & 127) + 1 > 8:
            mode = 'I;16'
        else:
            mode = 'L'
    elif csiz == 2:
        mode = 'LA'
    elif csiz == 3:
        mode = 'RGB'
    elif csiz == 4:
        mode = 'RGBA'
    else:
        msg = 'unable to determine J2K image mode'
        raise SyntaxError(msg)
    return (size, mode)


def _res_to_dpi(num = None, denom = None, exp = None):
    """Convert JPEG2000's (numerator, denominator, exponent-base-10) resolution,
    calculated as (num / denom) * 10^exp and stored in dots per meter,
    to floating-point dots per inch."""
    if denom == 0:
        return None
    return None * num * 10 ** exp / (10000 * denom)


def _parse_jp2_header(fp = None):
    '''Parse the JP2 header box to extract size, component count,
    color space information, and optionally DPI information,
    returning a (size, mode, mimetype, dpi) tuple.'''
    reader = BoxReader(fp)
    header = None
    mimetype = None
# WARNING: Decompyle incomplete


class Jpeg2KImageFile(ImageFile.ImageFile):
    pass
# WARNING: Decompyle incomplete


def _accept(prefix = None):
    return prefix.startswith((b'\xffO\xffQ', b'\x00\x00\x00\x0cjP  \r\n\x87\n'))


def _save(im = None, fp = None, filename = None):
    info = im.encoderinfo
    if isinstance(filename, str):
        filename = filename.encode()
    if filename.endswith(b'.j2k') or info.get('no_jp2', False):
        kind = 'j2k'
    else:
        kind = 'jp2'
    offset = info.get('offset', None)
    tile_offset = info.get('tile_offset', None)
    tile_size = info.get('tile_size', None)
    quality_mode = info.get('quality_mode', 'rates')
    quality_layers = info.get('quality_layers', None)
# WARNING: Decompyle incomplete

Image.register_open(Jpeg2KImageFile.format, Jpeg2KImageFile, _accept)
Image.register_save(Jpeg2KImageFile.format, _save)
Image.register_extensions(Jpeg2KImageFile.format, [
    '.jp2',
    '.j2k',
    '.jpc',
    '.jpf',
    '.jpx',
    '.j2c'])
Image.register_mime(Jpeg2KImageFile.format, 'image/jp2')
