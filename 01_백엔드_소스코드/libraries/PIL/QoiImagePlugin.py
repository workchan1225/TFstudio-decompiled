# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: QoiImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import IO
from  import Image, ImageFile
from _binary import i32be as i32
from _binary import o8
from _binary import o32be as o32

def _accept(prefix = None):
    return prefix.startswith(b'qoif')


class QoiImageFile(ImageFile.ImageFile):
    format = 'QOI'
    format_description = 'Quite OK Image'
    
    def _open(self = None):
        if not _accept(self.fp.read(4)):
            msg = 'not a QOI file'
            raise SyntaxError(msg)
        self._size = (i32(self.fp.read(4)), i32(self.fp.read(4)))
        channels = self.fp.read(1)[0]
        self._mode = 'RGB' if channels == 3 else 'RGBA'
        self.fp.seek(1, os.SEEK_CUR)
        self.tile = [
            ImageFile._Tile('qoi', (0, 0) + self._size, self.fp.tell())]



class QoiDecoder(ImageFile.PyDecoder):
    _pulls_fd = True
    _previous_pixel: 'bytes | bytearray | None' = None
    _previously_seen_pixels: 'dict[int, bytes | bytearray]' = { }
    
    def _add_to_previous_pixels(self = None, value = None):
        self._previous_pixel = value
        (r, g, b, a) = value
        hash_value = (r * 3 + g * 5 + b * 7 + a * 11) % 64
        self._previously_seen_pixels[hash_value] = value

    
    def decode(self = None, buffer = None):
        pass
    # WARNING: Decompyle incomplete



def _save(im = None, fp = None, filename = None):
    if im.mode == 'RGB':
        channels = 3
    elif im.mode == 'RGBA':
        channels = 4
    else:
        msg = 'Unsupported QOI image mode'
        raise ValueError(msg)
    colorspace = 0 if im.encoderinfo.get('colorspace') == 'sRGB' else 1
    fp.write(b'qoif')
    fp.write(o32(im.size[0]))
    fp.write(o32(im.size[1]))
    fp.write(o8(channels))
    fp.write(o8(colorspace))
    ImageFile._save(im, fp, [
        ImageFile._Tile('qoi', (0, 0) + im.size)])


class QoiEncoder(ImageFile.PyEncoder):
    _pushes_fd = True
    _previous_pixel: 'tuple[int, int, int, int] | None' = None
    _previously_seen_pixels: 'dict[int, tuple[int, int, int, int]]' = { }
    _run = 0
    
    def _write_run(self = None):
        data = o8(192 | self._run - 1)
        self._run = 0
        return data

    
    def _delta(self = None, left = None, right = None):
        result = left - right & 255
        if result >= 128:
            result -= 256
        return result

    
    def encode(self = None, bufsize = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(QoiImageFile.format, QoiImageFile, _accept)
Image.register_decoder('qoi', QoiDecoder)
Image.register_extension(QoiImageFile.format, '.qoi')
Image.register_save(QoiImageFile.format, _save)
Image.register_encoder('qoi', QoiEncoder)
