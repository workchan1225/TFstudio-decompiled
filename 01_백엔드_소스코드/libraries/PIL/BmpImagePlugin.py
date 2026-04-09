# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: BmpImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import IO, Any
from  import Image, ImageFile, ImagePalette
from _binary import i16le as i16
from _binary import i32le as i32
from _binary import o8
from _binary import o16le as o16
from _binary import o32le as o32
BIT2MODE = {
    1: ('P', 'P;1'),
    4: ('P', 'P;4'),
    8: ('P', 'P'),
    16: ('RGB', 'BGR;15'),
    24: ('RGB', 'BGR'),
    32: ('RGB', 'BGRX') }
USE_RAW_ALPHA = False

def _accept(prefix = None):
    return prefix.startswith(b'BM')


def _dib_accept(prefix = None):
    return i32(prefix) in (12, 40, 52, 56, 64, 108, 124)


class BmpImageFile(ImageFile.ImageFile):
    '''Image plugin for the Windows Bitmap format (BMP)'''
    format_description = 'Windows Bitmap'
    format = 'BMP'
    COMPRESSIONS = {
        'RAW': 0,
        'RLE8': 1,
        'RLE4': 2,
        'BITFIELDS': 3,
        'JPEG': 4,
        'PNG': 5 }
    for k, v in COMPRESSIONS.items():
        vars()[k] = v
        
        def _bitmap(self = None, header = None, offset = None):
            '''Read relevant info about the BMP'''
            seek = self.fp.seek
            read = self.fp.read
            if header:
                seek(header)
            file_info = {
                'header_size': i32(read(4)),
                'direction': -1 }
        # WARNING: Decompyle incomplete

        
        def _open(self = None):
            '''Open file, check magic number and read header'''
            head_data = self.fp.read(14)
            if not _accept(head_data):
                msg = 'Not a BMP file'
                raise SyntaxError(msg)
            offset = i32(head_data, 10)
            self._bitmap(offset = offset)

        return None


class BmpRleDecoder(ImageFile.PyDecoder):
    _pulls_fd = True
    
    def decode(self = None, buffer = None):
        pass
    # WARNING: Decompyle incomplete



class DibImageFile(BmpImageFile):
    format = 'DIB'
    format_description = 'Windows Bitmap'
    
    def _open(self = None):
        self._bitmap()


SAVE = {
    '1': ('1', 1, 2),
    'L': ('L', 8, 256),
    'P': ('P', 8, 256),
    'RGB': ('BGR', 24, 0),
    'RGBA': ('BGRA', 32, 0) }

def _dib_save(im = None, fp = None, filename = None):
    _save(im, fp, filename, False)


def _save(im = None, fp = None, filename = None, bitmap_header = (True,)):
    
    try:
        (rawmode, bits, colors) = SAVE[im.mode]
    except KeyError:
        e = None
        msg = f'''cannot write mode {im.mode} as BMP'''
        raise OSError(msg), e
        e = None
        del e

    info = im.encoderinfo
    dpi = info.get('dpi', (96, 96))
    ppm = (lambda .0: pass# WARNING: Decompyle incomplete
)(dpi())
    stride = (im.size[0] * bits + 7) // 8 + 3 & -4
    header = 40
    image = stride * im.size[1]
    if im.mode == '1':
        palette = (lambda .0: pass# WARNING: Decompyle incomplete
)((0, 255)())
    elif im.mode == 'L':
        palette = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(256)())
    elif im.mode == 'P':
        palette = im.im.getpalette('RGB', 'BGRX')
        colors = len(palette) // 4
    else:
        palette = None
    if bitmap_header:
        offset = 14 + header + colors * 4
        file_size = offset + image
        if file_size > 0xFFFFFFFF:
            msg = 'File size is too large for the BMP format'
            raise ValueError(msg)
        fp.write(b'BM' + o32(file_size) + o32(0) + o32(offset))
    fp.write(o32(header) + o32(im.size[0]) + o32(im.size[1]) + o16(1) + o16(bits) + o32(0) + o32(image) + o32(ppm[0]) + o32(ppm[1]) + o32(colors) + o32(colors))
    fp.write(b'\x00' * (header - 40))
    if palette:
        fp.write(palette)
    ImageFile._save(im, fp, [
        ImageFile._Tile('raw', (0, 0) + im.size, 0, (rawmode, stride, -1))])

Image.register_open(BmpImageFile.format, BmpImageFile, _accept)
Image.register_save(BmpImageFile.format, _save)
Image.register_extension(BmpImageFile.format, '.bmp')
Image.register_mime(BmpImageFile.format, 'image/bmp')
Image.register_decoder('bmp_rle', BmpRleDecoder)
Image.register_open(DibImageFile.format, DibImageFile, _dib_accept)
Image.register_save(DibImageFile.format, _dib_save)
Image.register_extension(DibImageFile.format, '.dib')
Image.register_mime(DibImageFile.format, 'image/bmp')
