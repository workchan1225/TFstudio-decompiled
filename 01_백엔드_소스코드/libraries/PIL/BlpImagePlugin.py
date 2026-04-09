# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: BlpImagePlugin.pyc (Python 3.11)

'''
Blizzard Mipmap Format (.blp)
Jerome Leclanche <jerome@leclan.ch>

The contents of this file are hereby released in the public domain (CC0)
Full text of the CC0 license:
  https://creativecommons.org/publicdomain/zero/1.0/

BLP1 files, used mostly in Warcraft III, are not fully supported.
All types of BLP2 files used in World of Warcraft are supported.

The BLP file structure consists of a header, up to 16 mipmaps of the
texture

Texture sizes must be powers of two, though the two dimensions do
not have to be equal; 512x256 is valid, but 512x200 is not.
The first mipmap (mipmap #0) is the full size image; each subsequent
mipmap halves both dimensions. The final mipmap should be 1x1.

BLP files come in many different flavours:
* JPEG-compressed (type == 0) - only supported for BLP1.
* RAW images (type == 1, encoding == 1). Each mipmap is stored as an
  array of 8-bit values, one per pixel, left to right, top to bottom.
  Each value is an index to the palette.
* DXT-compressed (type == 1, encoding == 2):
- DXT1 compression is used if alpha_encoding == 0.
  - An additional alpha bit is used if alpha_depth == 1.
  - DXT3 compression is used if alpha_encoding == 1.
  - DXT5 compression is used if alpha_encoding == 7.
'''
from __future__ import annotations
import abc
import os
import struct
from enum import IntEnum
from io import BytesIO
from typing import IO
from  import Image, ImageFile

class Format(IntEnum):
    JPEG = 0


class Encoding(IntEnum):
    UNCOMPRESSED = 1
    DXT = 2
    UNCOMPRESSED_RAW_BGRA = 3


class AlphaEncoding(IntEnum):
    DXT1 = 0
    DXT3 = 1
    DXT5 = 7


def unpack_565(i = None):
    return ((i >> 11 & 31) << 3, (i >> 5 & 63) << 2, (i & 31) << 3)


def decode_dxt1(data = None, alpha = None):
    '''
    input: one "row" of data (i.e. will produce 4*width pixels)
    '''
    blocks = len(data) // 8
    ret = (bytearray(), bytearray(), bytearray(), bytearray())
    for block_index in range(blocks):
        idx = block_index * 8
        (color0, color1, bits) = struct.unpack_from('<HHI', data, idx)
        (r0, g0, b0) = unpack_565(color0)
        (r1, g1, b1) = unpack_565(color1)
        for j in range(4):
            for i in range(4):
                control = bits & 3
                bits = bits >> 2
                a = 255
                if control == 0:
                    b = b0
                    g = g0
                    r = r0
                elif control == 1:
                    b = b1
                    g = g1
                    r = r1
                elif control == 2:
                    if color0 > color1:
                        r = (2 * r0 + r1) // 3
                        g = (2 * g0 + g1) // 3
                        b = (2 * b0 + b1) // 3
                    else:
                        r = (r0 + r1) // 2
                        g = (g0 + g1) // 2
                        b = (b0 + b1) // 2
                elif control == 3:
                    if color0 > color1:
                        r = (2 * r1 + r0) // 3
                        g = (2 * g1 + g0) // 3
                        b = (2 * b1 + b0) // 3
                    else:
                        (r, g, b, a) = (0, 0, 0, 0)
                if alpha:
                    ret[j].extend([
                        r,
                        g,
                        b,
                        a])
                    continue
                ret[j].extend([
                    r,
                    g,
                    b])
                return ret


def decode_dxt3(data = None):
    '''
    input: one "row" of data (i.e. will produce 4*width pixels)
    '''
    blocks = len(data) // 16
    ret = (bytearray(), bytearray(), bytearray(), bytearray())
    for block_index in range(blocks):
        idx = block_index * 16
        block = data[idx:idx + 16]
        bits = struct.unpack_from('<8B', block)
        (color0, color1) = struct.unpack_from('<HH', block, 8)
        (code,) = struct.unpack_from('<I', block, 12)
        (r0, g0, b0) = unpack_565(color0)
        (r1, g1, b1) = unpack_565(color1)
        for j in range(4):
            high = False
            for i in range(4):
                alphacode_index = (4 * j + i) // 2
                a = bits[alphacode_index]
                if high:
                    high = False
                    a >>= 4
                else:
                    high = True
                    a &= 15
                a *= 17
                color_code = code >> 2 * (4 * j + i) & 3
                if color_code == 0:
                    b = b0
                    g = g0
                    r = r0
                elif color_code == 1:
                    b = b1
                    g = g1
                    r = r1
                elif color_code == 2:
                    r = (2 * r0 + r1) // 3
                    g = (2 * g0 + g1) // 3
                    b = (2 * b0 + b1) // 3
                elif color_code == 3:
                    r = (2 * r1 + r0) // 3
                    g = (2 * g1 + g0) // 3
                    b = (2 * b1 + b0) // 3
                ret[j].extend([
                    r,
                    g,
                    b,
                    a])
                return ret


def decode_dxt5(data = None):
    '''
    input: one "row" of data (i.e. will produce 4 * width pixels)
    '''
    blocks = len(data) // 16
    ret = (bytearray(), bytearray(), bytearray(), bytearray())
    for block_index in range(blocks):
        idx = block_index * 16
        block = data[idx:idx + 16]
        (a0, a1) = struct.unpack_from('<BB', block)
        bits = struct.unpack_from('<6B', block, 2)
        alphacode1 = bits[2] | bits[3] << 8 | bits[4] << 16 | bits[5] << 24
        alphacode2 = bits[0] | bits[1] << 8
        (color0, color1) = struct.unpack_from('<HH', block, 8)
        (code,) = struct.unpack_from('<I', block, 12)
        (r0, g0, b0) = unpack_565(color0)
        (r1, g1, b1) = unpack_565(color1)
        for j in range(4):
            for i in range(4):
                alphacode_index = 3 * (4 * j + i)
                if alphacode_index <= 12:
                    alphacode = alphacode2 >> alphacode_index & 7
                elif alphacode_index == 15:
                    alphacode = alphacode2 >> 15 | alphacode1 << 1 & 6
                else:
                    alphacode = alphacode1 >> alphacode_index - 16 & 7
                if alphacode == 0:
                    a = a0
                elif alphacode == 1:
                    a = a1
                elif a0 > a1:
                    a = ((8 - alphacode) * a0 + (alphacode - 1) * a1) // 7
                elif alphacode == 6:
                    a = 0
                elif alphacode == 7:
                    a = 255
                else:
                    a = ((6 - alphacode) * a0 + (alphacode - 1) * a1) // 5
                color_code = code >> 2 * (4 * j + i) & 3
                if color_code == 0:
                    b = b0
                    g = g0
                    r = r0
                elif color_code == 1:
                    b = b1
                    g = g1
                    r = r1
                elif color_code == 2:
                    r = (2 * r0 + r1) // 3
                    g = (2 * g0 + g1) // 3
                    b = (2 * b0 + b1) // 3
                elif color_code == 3:
                    r = (2 * r1 + r0) // 3
                    g = (2 * g1 + g0) // 3
                    b = (2 * b1 + b0) // 3
                ret[j].extend([
                    r,
                    g,
                    b,
                    a])
                return ret


class BLPFormatError(NotImplementedError):
    pass


def _accept(prefix = None):
    return prefix.startswith((b'BLP1', b'BLP2'))


class BlpImageFile(ImageFile.ImageFile):
    '''
    Blizzard Mipmap Format
    '''
    format = 'BLP'
    format_description = 'Blizzard Mipmap Format'
    
    def _open(self = None):
        self.magic = self.fp.read(4)
        if not _accept(self.magic):
            msg = f'''Bad BLP magic {repr(self.magic)}'''
            raise BLPFormatError(msg)
        compression = struct.unpack('<i', self.fp.read(4))[0]
        if self.magic == b'BLP1':
            alpha = struct.unpack('<I', self.fp.read(4))[0] != 0
        else:
            encoding = struct.unpack('<b', self.fp.read(1))[0]
            alpha = struct.unpack('<b', self.fp.read(1))[0] != 0
            alpha_encoding = struct.unpack('<b', self.fp.read(1))[0]
            self.fp.seek(1, os.SEEK_CUR)
        self._size = struct.unpack('<II', self.fp.read(8))
        if self.magic == b'BLP1':
            encoding = struct.unpack('<i', self.fp.read(4))[0]
            self.fp.seek(4, os.SEEK_CUR)
            args = (compression, encoding, alpha)
            offset = 28
        else:
            args = (compression, encoding, alpha, alpha_encoding)
            offset = 20
        decoder = self.magic.decode()
        self._mode = 'RGBA' if alpha else 'RGB'
        self.tile = [
            ImageFile._Tile(decoder, (0, 0) + self.size, offset, args)]



class _BLPBaseDecoder(ImageFile.PyDecoder, abc.ABC):
    _pulls_fd = True
    
    def decode(self = None, buffer = None):
        
        try:
            self._read_header()
            self._load()
        except struct.error:
            e = None
            msg = 'Truncated BLP file'
            raise OSError(msg), e
            e = None
            del e

        return (-1, 0)

    _load = (lambda self = None: pass)()
    
    def _read_header(self = None):
        self._offsets = struct.unpack('<16I', self._safe_read(64))
        self._lengths = struct.unpack('<16I', self._safe_read(64))

    
    def _safe_read(self = None, length = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _read_palette(self = None):
        ret = []
        for i in range(256):
            (b, g, r, a) = struct.unpack('<4B', self._safe_read(4))
        except struct.error:
            pass
        except:
            ret.append((b, g, r, a))
            continue
        return ret

    
    def _read_bgra(self = None, palette = None, alpha = None):
        data = bytearray()
        _data = BytesIO(self._safe_read(self._lengths[0]))
        
        try:
            (offset,) = struct.unpack('<B', _data.read(1))
        except struct.error:
            pass
        except:
            (b, g, r, a) = palette[offset]
            d = (r, g, b)
            if alpha:
                d += (a,)
            data.extend(d)
            continue

        return data



class BLP1Decoder(_BLPBaseDecoder):
    
    def _load(self = None):
        (self._compression, self._encoding, alpha) = self.args
        if self._compression == Format.JPEG:
            self._decode_jpeg_stream()
            return None
        if None._compression == 1:
            if self._encoding in (4, 5):
                palette = self._read_palette()
                data = self._read_bgra(palette, alpha)
                self.set_as_raw(data)
                return None
            msg = f'''{repr(self._encoding)}'''
            raise BLPFormatError(msg)
        msg = f'''Unsupported BLP compression {repr(self._encoding)}'''
        raise BLPFormatError(msg)

    
    def _decode_jpeg_stream(self = None):
        JpegImageFile = JpegImageFile
        import JpegImagePlugin
        (jpeg_header_size,) = struct.unpack('<I', self._safe_read(4))
        jpeg_header = self._safe_read(jpeg_header_size)
    # WARNING: Decompyle incomplete



class BLP2Decoder(_BLPBaseDecoder):
    
    def _load(self = None):
        (self._compression, self._encoding, alpha, self._alpha_encoding) = self.args
        palette = self._read_palette()
    # WARNING: Decompyle incomplete



class BLPEncoder(ImageFile.PyEncoder):
    _pushes_fd = True
    
    def _write_palette(self = None):
        data = b''
    # WARNING: Decompyle incomplete

    
    def encode(self = None, bufsize = None):
        palette_data = self._write_palette()
        offset = 148 + len(palette_data)
    # WARNING: Decompyle incomplete



def _save(im = None, fp = None, filename = None):
    if im.mode != 'P':
        msg = 'Unsupported BLP image mode'
        raise ValueError(msg)
    magic = b'BLP1' if im.encoderinfo.get('blp_version') == 'BLP1' else b'BLP2'
    fp.write(magic)
# WARNING: Decompyle incomplete

Image.register_open(BlpImageFile.format, BlpImageFile, _accept)
Image.register_extension(BlpImageFile.format, '.blp')
Image.register_decoder('BLP1', BLP1Decoder)
Image.register_decoder('BLP2', BLP2Decoder)
Image.register_save(BlpImageFile.format, _save)
Image.register_encoder('BLP', BLPEncoder)
