# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: TgaImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import warnings
from typing import IO
from  import Image, ImageFile, ImagePalette
from _binary import i16le as i16
from _binary import o8
from _binary import o16le as o16
MODES = {
    (1, 8): 'P',
    (3, 1): '1',
    (3, 8): 'L',
    (3, 16): 'LA',
    (2, 16): 'BGRA;15Z',
    (2, 24): 'BGR',
    (2, 32): 'BGRA' }

class TgaImageFile(ImageFile.ImageFile):
    format = 'TGA'
    format_description = 'Targa'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def load_end(self = None):
        if self._flip_horizontally:
            self.im = self.im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            return None


SAVE = {
    '1': ('1', 1, 0, 3),
    'L': ('L', 8, 0, 3),
    'LA': ('LA', 16, 0, 3),
    'P': ('P', 8, 1, 1),
    'RGB': ('BGR', 24, 0, 2),
    'RGBA': ('BGRA', 32, 0, 2) }

def _save(im = None, fp = None, filename = None):
    
    try:
        (rawmode, bits, colormaptype, imagetype) = SAVE[im.mode]
    except KeyError:
        e = None
        msg = f'''cannot write mode {im.mode} as TGA'''
        raise OSError(msg), e
        e = None
        del e

    if 'rle' in im.encoderinfo:
        rle = im.encoderinfo['rle']
    else:
        compression = im.encoderinfo.get('compression', im.info.get('compression'))
        rle = compression == 'tga_rle'
    if rle:
        imagetype += 8
    id_section = im.encoderinfo.get('id_section', im.info.get('id_section', ''))
    id_len = len(id_section)
    if id_len > 255:
        id_len = 255
        id_section = id_section[:255]
        warnings.warn('id_section has been trimmed to 255 characters')
    if colormaptype:
        palette = im.im.getpalette('RGB', 'BGR')
        colormapentry = 24
        colormaplength = len(palette) // 3
    else:
        (colormaplength, colormapentry) = (0, 0)
    if im.mode in ('LA', 'RGBA'):
        flags = 8
    else:
        flags = 0
    orientation = im.encoderinfo.get('orientation', im.info.get('orientation', -1))
    if orientation > 0:
        flags = flags | 32
    fp.write(o8(id_len) + o8(colormaptype) + o8(imagetype) + o16(0) + o16(colormaplength) + o8(colormapentry) + o16(0) + o16(0) + o16(im.size[0]) + o16(im.size[1]) + o8(bits) + o8(flags))
    if id_section:
        fp.write(id_section)
    if colormaptype:
        fp.write(palette)
    if rle:
        ImageFile._save(im, fp, [
            ImageFile._Tile('tga_rle', (0, 0) + im.size, 0, (rawmode, orientation))])
    else:
        ImageFile._save(im, fp, [
            ImageFile._Tile('raw', (0, 0) + im.size, 0, (rawmode, 0, orientation))])
    fp.write(b'\x00\x00\x00\x00\x00\x00\x00\x00TRUEVISION-XFILE.\x00')

Image.register_open(TgaImageFile.format, TgaImageFile)
Image.register_save(TgaImageFile.format, _save)
Image.register_extensions(TgaImageFile.format, [
    '.tga',
    '.icb',
    '.vda',
    '.vst'])
Image.register_mime(TgaImageFile.format, 'image/x-tga')
