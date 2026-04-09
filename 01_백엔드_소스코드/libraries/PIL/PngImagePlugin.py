# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PngImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import itertools
import logging
import re
import struct
import warnings
import zlib
from enum import IntEnum
from typing import IO, NamedTuple, cast
from  import Image, ImageChops, ImageFile, ImagePalette, ImageSequence
from _binary import i16be as i16
from _binary import i32be as i32
from _binary import o8
from _binary import o16be as o16
from _binary import o32be as o32
from _deprecate import deprecate
from _util import DeferredError
TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, NoReturn
    from  import _imaging
logger = logging.getLogger(__name__)
is_cid = re.compile(b'\\w\\w\\w\\w').match
_MAGIC = b'\x89PNG\r\n\x1a\n'
_MODES = {
    (1, 0): ('1', '1'),
    (2, 0): ('L', 'L;2'),
    (4, 0): ('L', 'L;4'),
    (8, 0): ('L', 'L'),
    (16, 0): ('I;16', 'I;16B'),
    (8, 2): ('RGB', 'RGB'),
    (16, 2): ('RGB', 'RGB;16B'),
    (1, 3): ('P', 'P;1'),
    (2, 3): ('P', 'P;2'),
    (4, 3): ('P', 'P;4'),
    (8, 3): ('P', 'P'),
    (8, 4): ('LA', 'LA'),
    (16, 4): ('RGBA', 'LA;16B'),
    (8, 6): ('RGBA', 'RGBA'),
    (16, 6): ('RGBA', 'RGBA;16B') }
_simple_palette = re.compile(b'^\xff*\x00\xff*$')
MAX_TEXT_CHUNK = ImageFile.SAFEBLOCK
MAX_TEXT_MEMORY = 64 * MAX_TEXT_CHUNK

class Disposal(IntEnum):
    OP_NONE = 0
    OP_BACKGROUND = 1
    OP_PREVIOUS = 2


class Blend(IntEnum):
    OP_SOURCE = 0
    OP_OVER = 1


def _safe_zlib_decompress(s = None):
    dobj = zlib.decompressobj()
    plaintext = dobj.decompress(s, MAX_TEXT_CHUNK)
    if dobj.unconsumed_tail:
        msg = 'Decompressed data too large for PngImagePlugin.MAX_TEXT_CHUNK'
        raise ValueError(msg)
    return plaintext


def _crc32(data = None, seed = None):
    return zlib.crc32(data, seed) & 0xFFFFFFFF


class ChunkStream:
    
    def __init__(self = None, fp = None):
        self.fp = fp
        self.queue = []

    
    def read(self = None):
        '''Fetch a new chunk. Returns header information.'''
        cid = None
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *args):
        self.close()

    
    def close(self = None):
        self.queue = None
        self.fp = None

    
    def push(self = None, cid = None, pos = None, length = ('cid', 'bytes', 'pos', 'int', 'length', 'int', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def call(self = None, cid = None, pos = None, length = ('cid', 'bytes', 'pos', 'int', 'length', 'int', 'return', 'bytes')):
        '''Call the appropriate chunk handler'''
        logger.debug('STREAM %r %s %s', cid, pos, length)
        return getattr(self, f'''chunk_{cid.decode('ascii')}''')(pos, length)

    
    def crc(self = None, cid = None, data = None):
        '''Read and verify checksum'''
        if ImageFile.LOAD_TRUNCATED_IMAGES and cid[0] >> 5 & 1:
            self.crc_skip(cid, data)
            return None
    # WARNING: Decompyle incomplete

    
    def crc_skip(self = None, cid = None, data = None):
        '''Read checksum'''
        pass
    # WARNING: Decompyle incomplete

    
    def verify(self = None, endchunk = None):
        cids = []
    # WARNING: Decompyle incomplete



class iTXt(str):
    tkey: 'str | bytes | None' = '\n    Subclass of string to allow iTXt chunks to look like strings while\n    keeping their extra information\n\n    '
    __new__ = (lambda cls = None, text = None, lang = staticmethod, tkey = (None, None): self = str.__new__(cls, text)self.lang = langself.tkey = tkeyself)()


class PngInfo:
    '''
    PNG chunk container (for use with save(pnginfo=))

    '''
    
    def __init__(self = None):
        self.chunks = []

    
    def add(self = None, cid = None, data = None, after_idat = (False,)):
        '''Appends an arbitrary chunk. Use with caution.

        :param cid: a byte string, 4 bytes long.
        :param data: a byte string of the encoded data
        :param after_idat: for use with private chunks. Whether the chunk
                           should be written after IDAT

        '''
        self.chunks.append((cid, data, after_idat))

    
    def add_itxt(self, key = None, value = None, lang = None, tkey = ('', '', False), zip = ('key', 'str | bytes', 'value', 'str | bytes', 'lang', 'str | bytes', 'tkey', 'str | bytes', 'zip', 'bool', 'return', 'None')):
        '''Appends an iTXt chunk.

        :param key: latin-1 encodable text key name
        :param value: value for this key
        :param lang: language code
        :param tkey: UTF-8 version of the key name
        :param zip: compression flag

        '''
        if not isinstance(key, bytes):
            key = key.encode('latin-1', 'strict')
        if not isinstance(value, bytes):
            value = value.encode('utf-8', 'strict')
        if not isinstance(lang, bytes):
            lang = lang.encode('utf-8', 'strict')
        if not isinstance(tkey, bytes):
            tkey = tkey.encode('utf-8', 'strict')
        if zip:
            self.add(b'iTXt', key + b'\x00\x01\x00' + lang + b'\x00' + tkey + b'\x00' + zlib.compress(value))
            return None
        None.add(b'iTXt', key + b'\x00\x00\x00' + lang + b'\x00' + tkey + b'\x00' + value)

    
    def add_text(self = None, key = None, value = None, zip = (False,)):
        '''Appends a text chunk.

        :param key: latin-1 encodable text key name
        :param value: value for this key, text or an
           :py:class:`PIL.PngImagePlugin.iTXt` instance
        :param zip: compression flag

        '''
        pass
    # WARNING: Decompyle incomplete



class _RewindState(NamedTuple):
    seq_num: 'int | None' = '_RewindState'


class PngStream(ChunkStream):
    pass
# WARNING: Decompyle incomplete


def _accept(prefix = None):
    return prefix.startswith(_MAGIC)


class PngImageFile(ImageFile.ImageFile):
    pass
# WARNING: Decompyle incomplete

_OUTMODES = {
    '1': ('1', b'\x01', b'\x00'),
    'L;1': ('L;1', b'\x01', b'\x00'),
    'L;2': ('L;2', b'\x02', b'\x00'),
    'L;4': ('L;4', b'\x04', b'\x00'),
    'L': ('L', b'\x08', b'\x00'),
    'LA': ('LA', b'\x08', b'\x04'),
    'I': ('I;16B', b'\x10', b'\x00'),
    'I;16': ('I;16B', b'\x10', b'\x00'),
    'I;16B': ('I;16B', b'\x10', b'\x00'),
    'P;1': ('P;1', b'\x01', b'\x03'),
    'P;2': ('P;2', b'\x02', b'\x03'),
    'P;4': ('P;4', b'\x04', b'\x03'),
    'P': ('P', b'\x08', b'\x03'),
    'RGB': ('RGB', b'\x08', b'\x02'),
    'RGBA': ('RGBA', b'\x08', b'\x06') }

def putchunk(fp = None, cid = None, *data):
    '''Write a PNG chunk (including CRC field)'''
    byte_data = b''.join(data)
    fp.write(o32(len(byte_data)) + cid)
    fp.write(byte_data)
    crc = _crc32(byte_data, _crc32(cid))
    fp.write(o32(crc))


class _idat:
    
    def __init__(self = None, fp = None, chunk = None):
        self.fp = fp
        self.chunk = chunk

    
    def write(self = None, data = None):
        self.chunk(self.fp, b'IDAT', data)



class _fdat:
    
    def __init__(self = None, fp = None, chunk = None, seq_num = ('fp', 'IO[bytes]', 'chunk', 'Callable[..., None]', 'seq_num', 'int', 'return', 'None')):
        self.fp = fp
        self.chunk = chunk
        self.seq_num = seq_num

    
    def write(self = None, data = None):
        self.chunk(self.fp, b'fdAT', o32(self.seq_num), data)



class _Frame(NamedTuple):
    encoderinfo: 'dict[str, Any]' = '_Frame'


def _write_multiple_frames(im, fp, chunk, mode = None, rawmode = None, default_image = None, append_images = ('im', 'Image.Image', 'fp', 'IO[bytes]', 'chunk', 'Callable[..., None]', 'mode', 'str', 'rawmode', 'str', 'default_image', 'Image.Image | None', 'append_images', 'list[Image.Image]', 'return', 'Image.Image | None')):
    duration = im.encoderinfo.get('duration')
    loop = im.encoderinfo.get('loop', im.info.get('loop', 0))
    disposal = im.encoderinfo.get('disposal', im.info.get('disposal', Disposal.OP_NONE))
    blend = im.encoderinfo.get('blend', im.info.get('blend', Blend.OP_SOURCE))
    if default_image:
        chain = itertools.chain(append_images)
    else:
        chain = itertools.chain([
            im], append_images)
    im_frames = []
    frame_count = 0
# WARNING: Decompyle incomplete


def _save_all(im = None, fp = None, filename = None):
    _save(im, fp, filename, save_all = True)


def _save(im = None, fp = None, filename = None, chunk = (putchunk, False), save_all = ('im', 'Image.Image', 'fp', 'IO[bytes]', 'filename', 'str | bytes', 'chunk', 'Callable[..., None]', 'save_all', 'bool', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def getchunks(im = None, **params):
    '''Return a list of PNG chunks representing this image.'''
    pass
# WARNING: Decompyle incomplete

Image.register_open(PngImageFile.format, PngImageFile, _accept)
Image.register_save(PngImageFile.format, _save)
Image.register_save_all(PngImageFile.format, _save_all)
Image.register_extensions(PngImageFile.format, [
    '.png',
    '.apng'])
Image.register_mime(PngImageFile.format, 'image/png')
