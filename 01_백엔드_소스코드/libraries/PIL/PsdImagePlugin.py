# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PsdImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
from functools import cached_property
from typing import IO
from  import Image, ImageFile, ImagePalette
from _binary import i8
from _binary import i16be as i16
from _binary import i32be as i32
from _binary import si16be as si16
from _binary import si32be as si32
from _util import DeferredError
MODES = {
    (0, 1): ('1', 1),
    (0, 8): ('L', 1),
    (1, 8): ('L', 1),
    (2, 8): ('P', 1),
    (3, 8): ('RGB', 3),
    (4, 8): ('CMYK', 4),
    (7, 8): ('L', 1),
    (8, 8): ('L', 1),
    (9, 8): ('LAB', 3) }

def _accept(prefix = None):
    return prefix.startswith(b'8BPS')


class PsdImageFile(ImageFile.ImageFile):
    format = 'PSD'
    format_description = 'Adobe Photoshop'
    _close_exclusive_fp_after_loading = False
    
    def _open(self = None):
        read = self.fp.read
        s = read(26)
        if _accept(s) or i16(s, 4) != 1:
            msg = 'not a PSD file'
            raise SyntaxError(msg)
        psd_bits = i16(s, 22)
        psd_channels = i16(s, 12)
        psd_mode = i16(s, 24)
        (mode, channels) = MODES[(psd_mode, psd_bits)]
        if channels > psd_channels:
            msg = 'not enough channels'
            raise OSError(msg)
        if mode == 'RGB' and psd_channels == 4:
            mode = 'RGBA'
            channels = 4
        self._mode = mode
        self._size = (i32(s, 18), i32(s, 14))
        size = i32(read(4))
        if size:
            data = read(size)
            if mode == 'P' and size == 768:
                self.palette = ImagePalette.raw('RGB;L', data)
        self.resources = []
        size = i32(read(4))
    # WARNING: Decompyle incomplete

    layers = (lambda self = None: layers = []# WARNING: Decompyle incomplete
)()
    n_frames = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    is_animated = (lambda self = None: len(self.layers) > 1)()
    
    def seek(self = None, layer = None):
        if not self._seek_check(layer):
            return None
        if None(self._fp, DeferredError):
            raise self._fp.ex
        (_, mode, _, tile) = self.layers[layer - 1]
        self._mode = mode
        self.tile = tile
        self.frame = layer
        self.fp = self._fp

    
    def tell(self = None):
        return self.frame



def _layerinfo(fp = None, ct_bytes = None):
    pass
# WARNING: Decompyle incomplete


def _maketile(file = None, mode = None, bbox = None, channels = ('file', 'IO[bytes]', 'mode', 'str', 'bbox', 'tuple[int, int, int, int]', 'channels', 'int', 'return', 'list[ImageFile._Tile]')):
    tiles = []
    read = file.read
    compression = i16(read(2))
    xsize = bbox[2] - bbox[0]
    ysize = bbox[3] - bbox[1]
    offset = file.tell()
    if compression == 0:
        for channel in range(channels):
            layer = mode[channel]
            if mode == 'CMYK':
                layer += ';I'
            tiles.append(ImageFile._Tile('raw', bbox, offset, layer))
            offset = offset + xsize * ysize
    if compression == 1:
        i = 0
        bytecount = read(channels * ysize * 2)
        offset = file.tell()
        for channel in range(channels):
            layer = mode[channel]
            if mode == 'CMYK':
                layer += ';I'
            tiles.append(ImageFile._Tile('packbits', bbox, offset, layer))
            for y in range(ysize):
                offset = offset + i16(bytecount, i)
                i += 2
                file.seek(offset)
                if offset & 1:
                    read(1)
    return tiles

Image.register_open(PsdImageFile.format, PsdImageFile, _accept)
Image.register_extension(PsdImageFile.format, '.psd')
Image.register_mime(PsdImageFile.format, 'image/vnd.adobe.photoshop')
