# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageFile.pyc (Python 3.11)

from __future__ import annotations
import abc
import io
import itertools
import logging
import os
import struct
from typing import IO, Any, NamedTuple, cast
from  import ExifTags, Image
from _util import DeferredError, is_path
TYPE_CHECKING = False
if TYPE_CHECKING:
    from _typing import StrOrBytesPath
logger = logging.getLogger(__name__)
MAXBLOCK = 65536
SAFEBLOCK = 1048576
LOAD_TRUNCATED_IMAGES = False
ERRORS = {
    -1: 'image buffer overrun error',
    -2: 'decoding error',
    -3: 'unknown error',
    -8: 'bad configuration',
    -9: 'out of memory error' }

def _get_oserror(error = None, *, encoder):
    
    try:
        msg = Image.core.getcodecstatus(error)
    except AttributeError:
        msg = ERRORS.get(error)

    if not msg:
        msg = f'''{'encoder' if encoder else 'decoder'} error {error}'''
    msg += f''' when {'writing' if encoder else 'reading'} image file'''
    return OSError(msg)


def _tilesort(t = None):
    return t[2]


class _Tile(NamedTuple):
    extents: 'tuple[int, int, int, int] | None' = '_Tile'
    offset: 'int' = 0
    args: 'tuple[Any, ...] | str | None' = None


class ImageFile(Image.Image):
    pass
# WARNING: Decompyle incomplete


class StubHandler(abc.ABC):
    
    def open(self = None, im = None):
        pass

    load = (lambda self = None, im = None: pass)()


def StubImageFile():
    '''StubImageFile'''
    __doc__ = '\n    Base class for stub image loaders.\n\n    A stub loader is an image loader that can identify files of a\n    certain format, but relies on external code to load the file.\n    '
    _open = (lambda self = None: pass)()
    
    def load(self = None):
        loader = self._load()
    # WARNING: Decompyle incomplete

    _load = (lambda self = None: pass)()

StubImageFile = <NODE:27>(StubImageFile, 'StubImageFile', ImageFile, metaclass = abc.ABCMeta)

class Parser:
    '''
    Incremental image parser.  This class implements the standard
    feed/close consumer interface.
    '''
    incremental = None
    image: 'Image.Image | None' = None
    data: 'bytes | None' = None
    decoder: 'Image.core.ImagingDecoder | PyDecoder | None' = None
    offset = 0
    finished = 0
    
    def reset(self = None):
        """
        (Consumer) Reset the parser.  Note that you can only call this
        method immediately after you've created a parser; parser
        instances cannot be reused.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def feed(self = None, data = None):
        '''
        (Consumer) Feed data to the parser.

        :param data: A string buffer.
        :exception OSError: If the parser failed to parse the image file.
        '''
        if self.finished:
            return None
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *args):
        self.close()

    
    def close(self = None):
        '''
        (Consumer) Close the stream.

        :returns: An image object.
        :exception OSError: If the parser failed to parse the image file either
                            because it cannot be identified or cannot be
                            decoded.
        '''
        if self.decoder:
            self.feed(b'')
            self.data = None
            self.decoder = None
            if not self.finished:
                msg = 'image was incomplete'
                raise OSError(msg)
        if not self.image:
            msg = 'cannot parse this image'
            raise OSError(msg)
        None(None, None)



def _save(im = None, fp = None, tile = None, bufsize = (0,)):
    '''Helper to save image based on tile list

    :param im: Image object.
    :param fp: File object.
    :param tile: Tile list.
    :param bufsize: Optional buffer size
    '''
    im.load()
    if not hasattr(im, 'encoderconfig'):
        im.encoderconfig = ()
    tile.sort(key = _tilesort)
    bufsize = max(MAXBLOCK, bufsize, im.size[0] * 4)
    
    try:
        fh = fp.fileno()
        fp.flush()
        _encode_tile(im, fp, tile, bufsize, fh)
    except (AttributeError, io.UnsupportedOperation):
        exc = None
        _encode_tile(im, fp, tile, bufsize, None, exc)
        exc = None
        del exc
    except:
        exc = None
        del exc

    if hasattr(fp, 'flush'):
        fp.flush()
        return None


def _encode_tile(im, fp = None, tile = None, bufsize = None, fh = (None,), exc = ('im', 'Image.Image', 'fp', 'IO[bytes]', 'tile', 'list[_Tile]', 'bufsize', 'int', 'fh', 'int | None', 'exc', 'BaseException | None', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def _safe_read(fp = None, size = None):
    """
    Reads large blocks in a safe way.  Unlike fp.read(n), this function
    doesn't trust the user.  If the requested size is larger than
    SAFEBLOCK, the file is read block by block.

    :param fp: File handle.  Must implement a <b>read</b> method.
    :param size: Number of bytes to read.
    :returns: A string containing <i>size</i> bytes of data.

    Raises an OSError if the file is truncated and the read cannot be completed

    """
    if size <= 0:
        return b''
    if None <= SAFEBLOCK:
        data = fp.read(size)
        if len(data) < size:
            msg = 'Truncated File Read'
            raise OSError(msg)
        return data
    blocks = None
    remaining_size = size
# WARNING: Decompyle incomplete


class PyCodecState:
    
    def __init__(self = None):
        self.xsize = 0
        self.ysize = 0
        self.xoff = 0
        self.yoff = 0

    
    def extents(self = None):
        return (self.xoff, self.yoff, self.xoff + self.xsize, self.yoff + self.ysize)



class PyCodec:
    fd: 'IO[bytes] | None' = 'PyCodec'
    
    def __init__(self = None, mode = None, *args):
        self.im = None
        self.state = PyCodecState()
        self.fd = None
        self.mode = mode
        self.init(args)

    
    def init(self = None, args = None):
        '''
        Override to perform codec specific initialization

        :param args: Tuple of arg items from the tile entry
        :returns: None
        '''
        self.args = args

    
    def cleanup(self = None):
        '''
        Override to perform codec specific cleanup

        :returns: None
        '''
        pass

    
    def setfd(self = None, fd = None):
        '''
        Called from ImageFile to set the Python file-like object

        :param fd: A Python file-like object
        :returns: None
        '''
        self.fd = fd

    
    def setimage(self = None, im = None, extents = None):
        '''
        Called from ImageFile to set the core output image for the codec

        :param im: A core image object
        :param extents: a 4 tuple of (x0, y0, x1, y1) defining the rectangle
            for this tile
        :returns: None
        '''
        self.im = im
        if extents:
            (x0, y0, x1, y1) = extents
        else:
            (x0, y0, x1, y1) = (0, 0, 0, 0)
        if x0 == 0 and x1 == 0:
            (self.state.xsize, self.state.ysize) = self.im.size
        else:
            self.state.xoff = x0
            self.state.yoff = y0
            self.state.xsize = x1 - x0
            self.state.ysize = y1 - y0
        if self.state.xsize <= 0 or self.state.ysize <= 0:
            msg = 'Size cannot be negative'
            raise ValueError(msg)
        if self.state.xsize + self.state.xoff > self.im.size[0] or self.state.ysize + self.state.yoff > self.im.size[1]:
            msg = 'Tile cannot extend outside image'
            raise ValueError(msg)



class PyDecoder(PyCodec):
    '''
    Python implementation of a format decoder. Override this class and
    add the decoding logic in the :meth:`decode` method.

    See :ref:`Writing Your Own File Codec in Python<file-codecs-py>`
    '''
    _pulls_fd = False
    pulls_fd = (lambda self = None: self._pulls_fd)()
    
    def decode(self = None, buffer = None):
        '''
        Override to perform the decoding process.

        :param buffer: A bytes object with the data to be decoded.
        :returns: A tuple of ``(bytes consumed, errcode)``.
            If finished with decoding return -1 for the bytes consumed.
            Err codes are from :data:`.ImageFile.ERRORS`.
        '''
        msg = 'unavailable in base decoder'
        raise NotImplementedError(msg)

    
    def set_as_raw(self = None, data = None, rawmode = None, extra = (None, ())):
        '''
        Convenience method to set the internal image from a stream of raw data

        :param data: Bytes to be set
        :param rawmode: The rawmode to be used for the decoder.
            If not specified, it will default to the mode of the image
        :param extra: Extra arguments for the decoder.
        :returns: None
        '''
        if not rawmode:
            rawmode = self.mode
        d = Image._getdecoder(self.mode, 'raw', rawmode, extra)
    # WARNING: Decompyle incomplete



class PyEncoder(PyCodec):
    '''
    Python implementation of a format encoder. Override this class and
    add the decoding logic in the :meth:`encode` method.

    See :ref:`Writing Your Own File Codec in Python<file-codecs-py>`
    '''
    _pushes_fd = False
    pushes_fd = (lambda self = None: self._pushes_fd)()
    
    def encode(self = None, bufsize = None):
        '''
        Override to perform the encoding process.

        :param bufsize: Buffer size.
        :returns: A tuple of ``(bytes encoded, errcode, bytes)``.
            If finished with encoding return 1 for the error code.
            Err codes are from :data:`.ImageFile.ERRORS`.
        '''
        msg = 'unavailable in base encoder'
        raise NotImplementedError(msg)

    
    def encode_to_pyfd(self = None):
        '''
        If ``pushes_fd`` is ``True``, then this method will be used,
        and ``encode()`` will only be called once.

        :returns: A tuple of ``(bytes consumed, errcode)``.
            Err codes are from :data:`.ImageFile.ERRORS`.
        '''
        if not self.pushes_fd:
            return (0, -8)
        (bytes_consumed, errcode, data) = None.encode(0)
    # WARNING: Decompyle incomplete

    
    def encode_to_file(self = None, fh = None, bufsize = None):
        '''
        :param fh: File handle.
        :param bufsize: Buffer size.

        :returns: If finished successfully, return 0.
            Otherwise, return an error code. Err codes are from
            :data:`.ImageFile.ERRORS`.
        '''
        errcode = 0
    # WARNING: Decompyle incomplete
