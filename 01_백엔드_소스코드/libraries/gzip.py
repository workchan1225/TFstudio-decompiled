# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gzip.pyc (Python 3.11)

"""Functions that read and write gzipped files.

The user of the file doesn't have to worry about the compression,
but random access is not allowed."""
import struct
import sys
import time
import os
import zlib
import builtins
import io
import _compression
__all__ = [
    'BadGzipFile',
    'GzipFile',
    'open',
    'compress',
    'decompress']
(FTEXT, FHCRC, FEXTRA, FNAME, FCOMMENT) = (1, 2, 4, 8, 16)
(READ, WRITE) = (1, 2)
_COMPRESS_LEVEL_FAST = 1
_COMPRESS_LEVEL_TRADEOFF = 6
_COMPRESS_LEVEL_BEST = 9

def open(filename, mode, compresslevel, encoding, errors, newline = ('rb', _COMPRESS_LEVEL_BEST, None, None, None)):
    '''Open a gzip-compressed file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
    "rb", and the default compresslevel is 9.

    For binary mode, this function is equivalent to the GzipFile constructor:
    GzipFile(filename, mode, compresslevel). In this case, the encoding, errors
    and newline arguments must not be provided.

    For text mode, a GzipFile object is created, and wrapped in an
    io.TextIOWrapper instance with the specified encoding, error handling
    behavior, and line ending(s).

    '''
    if 't' in mode:
        if 'b' in mode:
            raise ValueError(f'''Invalid mode: {mode!r}''')
# WARNING: Decompyle incomplete


def write32u(output, value):
    output.write(struct.pack('<L', value))


class _PaddedFile:
    """Minimal read-only file object that prepends a string to the contents
    of an actual file. Shouldn't be used outside of gzip.py, as it lacks
    essential functionality."""
    
    def __init__(self, f, prepend = (b'',)):
        self._buffer = prepend
        self._length = len(prepend)
        self.file = f
        self._read = 0

    
    def read(self, size):
        pass
    # WARNING: Decompyle incomplete

    
    def prepend(self, prepend = (b'',)):
        pass
    # WARNING: Decompyle incomplete

    
    def seek(self, off):
        self._read = None
        self._buffer = None
        return self.file.seek(off)

    
    def seekable(self):
        return True



class BadGzipFile(OSError):
    '''Exception raised in some cases for invalid gzip files.'''
    pass


class GzipFile(_compression.BaseStream):
    '''The GzipFile class simulates most of the methods of a file object with
    the exception of the truncate() method.

    This class only supports opening files in binary mode. If you need to open a
    compressed file in text mode, use the gzip.open() function.

    '''
    myfileobj = None
    
    def __init__(self, filename, mode, compresslevel, fileobj, mtime = (None, None, _COMPRESS_LEVEL_BEST, None, None)):
        """Constructor for the GzipFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is based on fileobj, which can be a regular
        file, an io.BytesIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.

        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may include the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.

        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
        'xb' depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
        'wb', 'a' and 'ab', and 'x' and 'xb'.

        The compresslevel argument is an integer from 0 to 9 controlling the
        level of compression; 1 is fastest and produces the least compression,
        and 9 is slowest and produces the most compression. 0 is no compression
        at all. The default is 9.

        The mtime argument is an optional numeric timestamp to be written
        to the last modification time field in the stream when compressing.
        If omitted or None, the current time is used.

        """
        if mode:
            if 't' in mode or 'U' in mode:
                raise ValueError('Invalid mode: {!r}'.format(mode))
        if mode and 'b' not in mode:
            mode += 'b'
    # WARNING: Decompyle incomplete

    filename = (lambda self: import warningswarnings.warn('use the name attribute', DeprecationWarning, 2)if self.mode == WRITE and self.name[-3:] != '.gz':
self.name + '.gz'None.name)()
    mtime = (lambda self: self._buffer.raw._last_mtime)()
    
    def __repr__(self):
        s = repr(self.fileobj)
        return '<gzip ' + s[1:-1] + ' ' + hex(id(self)) + '>'

    
    def _init_write(self, filename):
        self.name = filename
        self.crc = zlib.crc32(b'')
        self.size = 0
        self.writebuf = []
        self.bufsize = 0
        self.offset = 0

    
    def _write_gzip_header(self, compresslevel):
        self.fileobj.write(b'\x1f\x8b')
        self.fileobj.write(b'\x08')
        
        try:
            fname = os.path.basename(self.name)
            if not isinstance(fname, bytes):
                fname = fname.encode('latin-1')
            if fname.endswith(b'.gz'):
                fname = fname[:-3]
            else:
                except UnicodeEncodeError:
                    fname = b''
                flags = 0
                if fname:
                    flags = FNAME

        self.fileobj.write(chr(flags).encode('latin-1'))
        mtime = self._write_mtime
    # WARNING: Decompyle incomplete

    
    def write(self, data):
        self._check_not_closed()
        if self.mode != WRITE:
            import errno
            raise OSError(errno.EBADF, 'write() on read-only GzipFile object')
    # WARNING: Decompyle incomplete

    
    def read(self, size = (-1,)):
        self._check_not_closed()
        if self.mode != READ:
            import errno
            raise OSError(errno.EBADF, 'read() on write-only GzipFile object')
        return self._buffer.read(size)

    
    def read1(self, size = (-1,)):
        """Implements BufferedIOBase.read1()

        Reads up to a buffer's worth of data if size is negative."""
        self._check_not_closed()
        if self.mode != READ:
            import errno
            raise OSError(errno.EBADF, 'read1() on write-only GzipFile object')
        if size < 0:
            size = io.DEFAULT_BUFFER_SIZE
        return self._buffer.read1(size)

    
    def peek(self, n):
        self._check_not_closed()
        if self.mode != READ:
            import errno
            raise OSError(errno.EBADF, 'peek() on write-only GzipFile object')
        return self._buffer.peek(n)

    closed = (lambda self: self.fileobj is None)()
    
    def close(self):
        fileobj = self.fileobj
    # WARNING: Decompyle incomplete

    
    def flush(self, zlib_mode = (zlib.Z_SYNC_FLUSH,)):
        self._check_not_closed()
        if self.mode == WRITE:
            self.fileobj.write(self.compress.flush(zlib_mode))
            self.fileobj.flush()
            return None

    
    def fileno(self):
        """Invoke the underlying file object's fileno() method.

        This will raise AttributeError if the underlying file object
        doesn't support fileno().
        """
        return self.fileobj.fileno()

    
    def rewind(self):
        '''Return the uncompressed stream file position indicator to the
        beginning of the file'''
        if self.mode != READ:
            raise OSError("Can't rewind in write mode")
        self._buffer.seek(0)

    
    def readable(self):
        return self.mode == READ

    
    def writable(self):
        return self.mode == WRITE

    
    def seekable(self):
        return True

    
    def seek(self, offset, whence = (io.SEEK_SET,)):
        if self.mode == WRITE:
            if whence != io.SEEK_SET:
                if whence == io.SEEK_CUR:
                    offset = self.offset + offset
                else:
                    raise ValueError('Seek from end not supported')
            if offset < self.offset:
                raise OSError('Negative seek in write mode')
            count = offset - self.offset
            chunk = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            for i in range(count // 1024):
                self.write(chunk)
                self.write(b'\x00' * (count % 1024))
        if self.mode == READ:
            self._check_not_closed()
            return self._buffer.seek(offset, whence)
        return None.offset

    
    def readline(self, size = (-1,)):
        self._check_not_closed()
        return self._buffer.readline(size)



def _read_exact(fp, n):
    '''Read exactly *n* bytes from `fp`

    This method is required because fp may be unbuffered,
    i.e. return short reads.
    '''
    data = fp.read(n)
# WARNING: Decompyle incomplete


def _read_gzip_header(fp):
    '''Read a gzip header from `fp` and progress to the end of the header.

    Returns last mtime if header was present or None otherwise.
    '''
    magic = fp.read(2)
    if magic == b'':
        return None
    if None != b'\x1f\x8b':
        raise BadGzipFile('Not a gzipped file (%r)' % magic)
    (method, flag, last_mtime) = struct.unpack('<BBIxx', _read_exact(fp, 8))
    if method != 8:
        raise BadGzipFile('Unknown compression method')
    if flag & FEXTRA:
        (extra_len,) = struct.unpack('<H', _read_exact(fp, 2))
        _read_exact(fp, extra_len)
    if flag & FNAME:
        s = fp.read(1)
        if s or s == b'\x00':
            pass
        
    if flag & FCOMMENT:
        s = fp.read(1)
        if s or s == b'\x00':
            pass
        
    if flag & FHCRC:
        _read_exact(fp, 2)
    return last_mtime


class _GzipReader(_compression.DecompressReader):
    pass
# WARNING: Decompyle incomplete


def _create_simple_gzip_header(compresslevel = None, mtime = None):
    '''
    Write a simple gzip header with no extra fields.
    :param compresslevel: Compresslevel used to determine the xfl bytes.
    :param mtime: The mtime (must support conversion to a 32-bit integer).
    :return: A bytes object representing the gzip header.
    '''
    pass
# WARNING: Decompyle incomplete


def compress(data = None, compresslevel = (_COMPRESS_LEVEL_BEST,), *, mtime):
    '''Compress data in one shot and return the compressed string.

    compresslevel sets the compression level in range of 0-9.
    mtime can be used to set the modification time. The modification time is
    set to the current time by default.
    '''
    if mtime == 0:
        return zlib.compress(data, level = compresslevel, wbits = 31)
    header = None(compresslevel, mtime)
    trailer = struct.pack('<LL', zlib.crc32(data), len(data) & 0xFFFFFFFF)
    return header + zlib.compress(data, level = compresslevel, wbits = -15) + trailer


def decompress(data):
    '''Decompress a gzip compressed string in one shot.
    Return the decompressed string.
    '''
    decompressed_members = []
    fp = io.BytesIO(data)
# WARNING: Decompyle incomplete


def main():
    ArgumentParser = ArgumentParser
    import argparse
    parser = ArgumentParser(description = 'A simple command line interface for the gzip module: act like gzip, but do not delete the input file.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--fast', action = 'store_true', help = 'compress faster')
    group.add_argument('--best', action = 'store_true', help = 'compress better')
    group.add_argument('-d', '--decompress', action = 'store_true', help = 'act like gunzip instead of gzip')
    parser.add_argument('args', nargs = '*', default = [
        '-'], metavar = 'file')
    args = parser.parse_args()
    compresslevel = _COMPRESS_LEVEL_TRADEOFF
    if args.fast:
        compresslevel = _COMPRESS_LEVEL_FAST
    elif args.best:
        compresslevel = _COMPRESS_LEVEL_BEST
    for arg in args.args:
        if args.decompress:
            if arg == '-':
                f = GzipFile(filename = '', mode = 'rb', fileobj = sys.stdin.buffer)
                g = sys.stdout.buffer
            elif arg[-3:] != '.gz':
                sys.exit(f'''filename doesn\'t end in .gz: {arg!r}''')
            f = open(arg, 'rb')
            g = builtins.open(arg[:-3], 'wb')
        elif arg == '-':
            f = sys.stdin.buffer
            g = GzipFile(filename = '', mode = 'wb', fileobj = sys.stdout.buffer, compresslevel = compresslevel)
        else:
            f = builtins.open(arg, 'rb')
            g = open(arg + '.gz', 'wb')
        chunk = f.read(io.DEFAULT_BUFFER_SIZE)
        if not chunk:
            pass
        else:
            g.write(chunk)
        if g is not sys.stdout.buffer:
            g.close()
        if f is not sys.stdin.buffer:
            f.close()
        return None

if __name__ == '__main__':
    main()
    return None
