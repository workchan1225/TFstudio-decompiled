# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backend_cffi.pyc (Python 3.11)

'''Python interface to the Zstandard (zstd) compression library.'''
from __future__ import absolute_import, unicode_literals
__all__ = [
    'BufferSegment',
    'BufferSegments',
    'BufferWithSegments',
    'BufferWithSegmentsCollection',
    'ZstdCompressionChunker',
    'ZstdCompressionDict',
    'ZstdCompressionObj',
    'ZstdCompressionParameters',
    'ZstdCompressionReader',
    'ZstdCompressionWriter',
    'ZstdCompressor',
    'ZstdDecompressionObj',
    'ZstdDecompressionReader',
    'ZstdDecompressionWriter',
    'ZstdDecompressor',
    'ZstdError',
    'FrameParameters',
    'backend_features',
    'estimate_decompression_context_size',
    'frame_content_size',
    'frame_header_size',
    'get_frame_parameters',
    'train_dictionary',
    'FLUSH_BLOCK',
    'FLUSH_FRAME',
    'COMPRESSOBJ_FLUSH_FINISH',
    'COMPRESSOBJ_FLUSH_BLOCK',
    'ZSTD_VERSION',
    'FRAME_HEADER',
    'CONTENTSIZE_UNKNOWN',
    'CONTENTSIZE_ERROR',
    'MAX_COMPRESSION_LEVEL',
    'COMPRESSION_RECOMMENDED_INPUT_SIZE',
    'COMPRESSION_RECOMMENDED_OUTPUT_SIZE',
    'DECOMPRESSION_RECOMMENDED_INPUT_SIZE',
    'DECOMPRESSION_RECOMMENDED_OUTPUT_SIZE',
    'MAGIC_NUMBER',
    'BLOCKSIZELOG_MAX',
    'BLOCKSIZE_MAX',
    'WINDOWLOG_MIN',
    'WINDOWLOG_MAX',
    'CHAINLOG_MIN',
    'CHAINLOG_MAX',
    'HASHLOG_MIN',
    'HASHLOG_MAX',
    'MINMATCH_MIN',
    'MINMATCH_MAX',
    'SEARCHLOG_MIN',
    'SEARCHLOG_MAX',
    'SEARCHLENGTH_MIN',
    'SEARCHLENGTH_MAX',
    'TARGETLENGTH_MIN',
    'TARGETLENGTH_MAX',
    'LDM_MINMATCH_MIN',
    'LDM_MINMATCH_MAX',
    'LDM_BUCKETSIZELOG_MAX',
    'STRATEGY_FAST',
    'STRATEGY_DFAST',
    'STRATEGY_GREEDY',
    'STRATEGY_LAZY',
    'STRATEGY_LAZY2',
    'STRATEGY_BTLAZY2',
    'STRATEGY_BTOPT',
    'STRATEGY_BTULTRA',
    'STRATEGY_BTULTRA2',
    'DICT_TYPE_AUTO',
    'DICT_TYPE_RAWCONTENT',
    'DICT_TYPE_FULLDICT',
    'FORMAT_ZSTD1',
    'FORMAT_ZSTD1_MAGICLESS']
import io
import os
from _cffi import ffi, lib
backend_features = set()
COMPRESSION_RECOMMENDED_INPUT_SIZE = lib.ZSTD_CStreamInSize()
COMPRESSION_RECOMMENDED_OUTPUT_SIZE = lib.ZSTD_CStreamOutSize()
DECOMPRESSION_RECOMMENDED_INPUT_SIZE = lib.ZSTD_DStreamInSize()
DECOMPRESSION_RECOMMENDED_OUTPUT_SIZE = lib.ZSTD_DStreamOutSize()
new_nonzero = ffi.new_allocator(should_clear_after_alloc = False)
MAX_COMPRESSION_LEVEL = lib.ZSTD_maxCLevel()
MAGIC_NUMBER = lib.ZSTD_MAGICNUMBER
FRAME_HEADER = b'(\xb5/\xfd'
CONTENTSIZE_UNKNOWN = lib.ZSTD_CONTENTSIZE_UNKNOWN
CONTENTSIZE_ERROR = lib.ZSTD_CONTENTSIZE_ERROR
ZSTD_VERSION = (lib.ZSTD_VERSION_MAJOR, lib.ZSTD_VERSION_MINOR, lib.ZSTD_VERSION_RELEASE)
BLOCKSIZELOG_MAX = lib.ZSTD_BLOCKSIZELOG_MAX
BLOCKSIZE_MAX = lib.ZSTD_BLOCKSIZE_MAX
WINDOWLOG_MIN = lib.ZSTD_WINDOWLOG_MIN
WINDOWLOG_MAX = lib.ZSTD_WINDOWLOG_MAX
CHAINLOG_MIN = lib.ZSTD_CHAINLOG_MIN
CHAINLOG_MAX = lib.ZSTD_CHAINLOG_MAX
HASHLOG_MIN = lib.ZSTD_HASHLOG_MIN
HASHLOG_MAX = lib.ZSTD_HASHLOG_MAX
MINMATCH_MIN = lib.ZSTD_MINMATCH_MIN
MINMATCH_MAX = lib.ZSTD_MINMATCH_MAX
SEARCHLOG_MIN = lib.ZSTD_SEARCHLOG_MIN
SEARCHLOG_MAX = lib.ZSTD_SEARCHLOG_MAX
SEARCHLENGTH_MIN = lib.ZSTD_MINMATCH_MIN
SEARCHLENGTH_MAX = lib.ZSTD_MINMATCH_MAX
TARGETLENGTH_MIN = lib.ZSTD_TARGETLENGTH_MIN
TARGETLENGTH_MAX = lib.ZSTD_TARGETLENGTH_MAX
LDM_MINMATCH_MIN = lib.ZSTD_LDM_MINMATCH_MIN
LDM_MINMATCH_MAX = lib.ZSTD_LDM_MINMATCH_MAX
LDM_BUCKETSIZELOG_MAX = lib.ZSTD_LDM_BUCKETSIZELOG_MAX
STRATEGY_FAST = lib.ZSTD_fast
STRATEGY_DFAST = lib.ZSTD_dfast
STRATEGY_GREEDY = lib.ZSTD_greedy
STRATEGY_LAZY = lib.ZSTD_lazy
STRATEGY_LAZY2 = lib.ZSTD_lazy2
STRATEGY_BTLAZY2 = lib.ZSTD_btlazy2
STRATEGY_BTOPT = lib.ZSTD_btopt
STRATEGY_BTULTRA = lib.ZSTD_btultra
STRATEGY_BTULTRA2 = lib.ZSTD_btultra2
DICT_TYPE_AUTO = lib.ZSTD_dct_auto
DICT_TYPE_RAWCONTENT = lib.ZSTD_dct_rawContent
DICT_TYPE_FULLDICT = lib.ZSTD_dct_fullDict
FORMAT_ZSTD1 = lib.ZSTD_f_zstd1
FORMAT_ZSTD1_MAGICLESS = lib.ZSTD_f_zstd1_magicless
FLUSH_BLOCK = 0
FLUSH_FRAME = 1
COMPRESSOBJ_FLUSH_FINISH = 0
COMPRESSOBJ_FLUSH_BLOCK = 1

def _cpu_count():
    
    try:
        if not os.cpu_count():
            return 0
        except AttributeError:
            pass
        
        try:
            return os.sysconf('SC_NPROCESSORS_ONLN')
        except (AttributeError, ValueError):
            pass

        return 0



class BufferSegment:
    '''Represents a segment within a ``BufferWithSegments``.

    This type is essentially a reference to N bytes within a
    ``BufferWithSegments``.

    The object conforms to the buffer protocol.
    '''
    offset = (lambda self: raise NotImplementedError())()
    
    def __len__(self):
        '''Obtain the length of the segment, in bytes.'''
        raise NotImplementedError()

    
    def tobytes(self):
        '''Obtain bytes copy of this segment.'''
        raise NotImplementedError()



class BufferSegments:
    '''Represents an array of ``(offset, length)`` integers.

    This type is effectively an index used by :py:class:`BufferWithSegments`.

    The array members are 64-bit unsigned integers using host/native bit order.

    Instances conform to the buffer protocol.
    '''
    pass


class BufferWithSegments:
    '''A memory buffer containing N discrete items of known lengths.

    This type is essentially a fixed size memory address and an array
    of 2-tuples of ``(offset, length)`` 64-bit unsigned native-endian
    integers defining the byte offset and length of each segment within
    the buffer.

    Instances behave like containers.

    Instances also conform to the buffer protocol. So a reference to the
    backing bytes can be obtained via ``memoryview(o)``. A *copy* of the
    backing bytes can be obtained via ``.tobytes()``.

    This type exists to facilitate operations against N>1 items without
    the overhead of Python object creation and management. Used with
    APIs like :py:meth:`ZstdDecompressor.multi_decompress_to_buffer`, it
    is possible to decompress many objects in parallel without the GIL
    held, leading to even better performance.
    '''
    size = (lambda self: raise NotImplementedError())()
    
    def __len__(self):
        raise NotImplementedError()

    
    def __getitem__(self, i):
        '''Obtains a segment within the buffer.

        The returned object references memory within this buffer.

        :param i:
           Integer index of segment to retrieve.
        :return:
           :py:class:`BufferSegment`
        '''
        raise NotImplementedError()

    
    def segments(self):
        '''Obtain the array of ``(offset, length)`` segments in the buffer.

        :return:
           :py:class:`BufferSegments`
        '''
        raise NotImplementedError()

    
    def tobytes(self):
        '''Obtain bytes copy of this instance.'''
        raise NotImplementedError()



class BufferWithSegmentsCollection:
    '''A virtual spanning view over multiple BufferWithSegments.

    Instances are constructed from 1 or more :py:class:`BufferWithSegments`
    instances. The resulting object behaves like an ordered sequence whose
    members are the segments within each ``BufferWithSegments``.

    If the object is composed of 2 ``BufferWithSegments`` instances with the
    first having 2 segments and the second have 3 segments, then ``b[0]``
    and ``b[1]`` access segments in the first object and ``b[2]``, ``b[3]``,
    and ``b[4]`` access segments from the second.
    '''
    
    def __len__(self):
        '''The number of segments within all ``BufferWithSegments``.'''
        raise NotImplementedError()

    
    def __getitem__(self, i):
        '''Obtain the ``BufferSegment`` at an offset.'''
        raise NotImplementedError()



class ZstdError(Exception):
    pass


def _zstd_error(zresult):
    return ffi.string(lib.ZSTD_getErrorName(zresult)).decode('utf-8')


def _make_cctx_params(params):
    res = lib.ZSTD_createCCtxParams()
    if res == ffi.NULL:
        raise MemoryError()
    res = ffi.gc(res, lib.ZSTD_freeCCtxParams)
    attrs = [
        (lib.ZSTD_c_format, params.format),
        (lib.ZSTD_c_compressionLevel, params.compression_level),
        (lib.ZSTD_c_windowLog, params.window_log),
        (lib.ZSTD_c_hashLog, params.hash_log),
        (lib.ZSTD_c_chainLog, params.chain_log),
        (lib.ZSTD_c_searchLog, params.search_log),
        (lib.ZSTD_c_minMatch, params.min_match),
        (lib.ZSTD_c_targetLength, params.target_length),
        (lib.ZSTD_c_strategy, params.strategy),
        (lib.ZSTD_c_contentSizeFlag, params.write_content_size),
        (lib.ZSTD_c_checksumFlag, params.write_checksum),
        (lib.ZSTD_c_dictIDFlag, params.write_dict_id),
        (lib.ZSTD_c_nbWorkers, params.threads),
        (lib.ZSTD_c_jobSize, params.job_size),
        (lib.ZSTD_c_overlapLog, params.overlap_log),
        (lib.ZSTD_c_forceMaxWindow, params.force_max_window),
        (lib.ZSTD_c_enableLongDistanceMatching, params.enable_ldm),
        (lib.ZSTD_c_ldmHashLog, params.ldm_hash_log),
        (lib.ZSTD_c_ldmMinMatch, params.ldm_min_match),
        (lib.ZSTD_c_ldmBucketSizeLog, params.ldm_bucket_size_log),
        (lib.ZSTD_c_ldmHashRateLog, params.ldm_hash_rate_log)]
    for param, value in attrs:
        _set_compression_parameter(res, param, value)
        return res


class ZstdCompressionParameters(object):
    """Low-level zstd compression parameters.

    This type represents a collection of parameters to control how zstd
    compression is performed.

    Instances can be constructed from raw parameters or derived from a
    base set of defaults specified from a compression level (recommended)
    via :py:meth:`ZstdCompressionParameters.from_level`.

    >>> # Derive compression settings for compression level 7.
    >>> params = zstandard.ZstdCompressionParameters.from_level(7)

    >>> # With an input size of 1MB
    >>> params = zstandard.ZstdCompressionParameters.from_level(7, source_size=1048576)

    Using ``from_level()``, it is also possible to override individual compression
    parameters or to define additional settings that aren't automatically derived.
    e.g.:

    >>> params = zstandard.ZstdCompressionParameters.from_level(4, window_log=10)
    >>> params = zstandard.ZstdCompressionParameters.from_level(5, threads=4)

    Or you can define low-level compression settings directly:

    >>> params = zstandard.ZstdCompressionParameters(window_log=12, enable_ldm=True)

    Once a ``ZstdCompressionParameters`` instance is obtained, it can be used to
    configure a compressor:

    >>> cctx = zstandard.ZstdCompressor(compression_params=params)

    Some of these are very low-level settings. It may help to consult the official
    zstandard documentation for their behavior. Look for the ``ZSTD_p_*`` constants
    in ``zstd.h`` (https://github.com/facebook/zstd/blob/dev/lib/zstd.h).
    """
    from_level = (lambda level, source_size, dict_size = (0, 0): params = lib.ZSTD_getCParams(level, source_size, dict_size)args = {
'window_log': 'windowLog',
'chain_log': 'chainLog',
'hash_log': 'hashLog',
'search_log': 'searchLog',
'min_match': 'minMatch',
'target_length': 'targetLength',
'strategy': 'strategy' }# WARNING: Decompyle incomplete
)()
    
    def __init__(self, format, compression_level, window_log, hash_log, chain_log, search_log, min_match, target_length, strategy, write_content_size, write_checksum, write_dict_id, job_size, overlap_log, force_max_window, enable_ldm, ldm_hash_log, ldm_min_match, ldm_bucket_size_log, ldm_hash_rate_log, threads = (0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0)):
        params = lib.ZSTD_createCCtxParams()
        if params == ffi.NULL:
            raise MemoryError()
        params = ffi.gc(params, lib.ZSTD_freeCCtxParams)
        self._params = params
        if threads < 0:
            threads = _cpu_count()
        _set_compression_parameter(params, lib.ZSTD_c_nbWorkers, threads)
        _set_compression_parameter(params, lib.ZSTD_c_format, format)
        _set_compression_parameter(params, lib.ZSTD_c_compressionLevel, compression_level)
        _set_compression_parameter(params, lib.ZSTD_c_windowLog, window_log)
        _set_compression_parameter(params, lib.ZSTD_c_hashLog, hash_log)
        _set_compression_parameter(params, lib.ZSTD_c_chainLog, chain_log)
        _set_compression_parameter(params, lib.ZSTD_c_searchLog, search_log)
        _set_compression_parameter(params, lib.ZSTD_c_minMatch, min_match)
        _set_compression_parameter(params, lib.ZSTD_c_targetLength, target_length)
        if strategy == -1:
            strategy = 0
        _set_compression_parameter(params, lib.ZSTD_c_strategy, strategy)
        _set_compression_parameter(params, lib.ZSTD_c_contentSizeFlag, write_content_size)
        _set_compression_parameter(params, lib.ZSTD_c_checksumFlag, write_checksum)
        _set_compression_parameter(params, lib.ZSTD_c_dictIDFlag, write_dict_id)
        _set_compression_parameter(params, lib.ZSTD_c_jobSize, job_size)
        if overlap_log == -1:
            overlap_log = 0
        _set_compression_parameter(params, lib.ZSTD_c_overlapLog, overlap_log)
        _set_compression_parameter(params, lib.ZSTD_c_forceMaxWindow, force_max_window)
        _set_compression_parameter(params, lib.ZSTD_c_enableLongDistanceMatching, enable_ldm)
        _set_compression_parameter(params, lib.ZSTD_c_ldmHashLog, ldm_hash_log)
        _set_compression_parameter(params, lib.ZSTD_c_ldmMinMatch, ldm_min_match)
        _set_compression_parameter(params, lib.ZSTD_c_ldmBucketSizeLog, ldm_bucket_size_log)
        if ldm_hash_rate_log == -1:
            ldm_hash_rate_log = 0
        _set_compression_parameter(params, lib.ZSTD_c_ldmHashRateLog, ldm_hash_rate_log)

    format = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_format))()
    compression_level = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_compressionLevel))()
    window_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_windowLog))()
    hash_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_hashLog))()
    chain_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_chainLog))()
    search_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_searchLog))()
    min_match = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_minMatch))()
    target_length = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_targetLength))()
    strategy = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_strategy))()
    write_content_size = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_contentSizeFlag))()
    write_checksum = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_checksumFlag))()
    write_dict_id = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_dictIDFlag))()
    job_size = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_jobSize))()
    overlap_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_overlapLog))()
    force_max_window = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_forceMaxWindow))()
    enable_ldm = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_enableLongDistanceMatching))()
    ldm_hash_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_ldmHashLog))()
    ldm_min_match = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_ldmMinMatch))()
    ldm_bucket_size_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_ldmBucketSizeLog))()
    ldm_hash_rate_log = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_ldmHashRateLog))()
    threads = (lambda self: _get_compression_parameter(self._params, lib.ZSTD_c_nbWorkers))()
    
    def estimated_compression_context_size(self):
        '''Estimated size in bytes needed to compress with these parameters.'''
        return lib.ZSTD_estimateCCtxSize_usingCCtxParams(self._params)



def estimate_decompression_context_size():
    '''Estimate the memory size requirements for a decompressor instance.

    :return:
       Integer number of bytes.
    '''
    return lib.ZSTD_estimateDCtxSize()


def _set_compression_parameter(params, param, value):
    zresult = lib.ZSTD_CCtxParams_setParameter(params, param, value)
    if lib.ZSTD_isError(zresult):
        raise ZstdError('unable to set compression context parameter: %s' % _zstd_error(zresult))


def _get_compression_parameter(params, param):
    result = ffi.new('int *')
    zresult = lib.ZSTD_CCtxParams_getParameter(params, param, result)
    if lib.ZSTD_isError(zresult):
        raise ZstdError('unable to get compression context parameter: %s' % _zstd_error(zresult))
    return result[0]


class ZstdCompressionWriter(object):
    '''Writable compressing stream wrapper.

    ``ZstdCompressionWriter`` is a write-only stream interface for writing
    compressed data to another stream.

    This type conforms to the ``io.RawIOBase`` interface and should be usable
    by any type that operates against a *file-object* (``typing.BinaryIO``
    in Python type hinting speak). Only methods that involve writing will do
    useful things.

    As data is written to this stream (e.g. via ``write()``), that data
    is sent to the compressor. As compressed data becomes available from
    the compressor, it is sent to the underlying stream by calling its
    ``write()`` method.

    Both ``write()`` and ``flush()`` return the number of bytes written to the
    object\'s ``write()``. In many cases, small inputs do not accumulate enough
    data to cause a write and ``write()`` will return ``0``.

    Calling ``close()`` will mark the stream as closed and subsequent I/O
    operations will raise ``ValueError`` (per the documented behavior of
    ``io.RawIOBase``). ``close()`` will also call ``close()`` on the underlying
    stream if such a method exists and the instance was constructed with
    ``closefd=True``

    Instances are obtained by calling :py:meth:`ZstdCompressor.stream_writer`.

    Typically usage is as follows:

    >>> cctx = zstandard.ZstdCompressor(level=10)
    >>> compressor = cctx.stream_writer(fh)
    >>> compressor.write(b"chunk 0\\n")
    >>> compressor.write(b"chunk 1\\n")
    >>> compressor.flush()
    >>> # Receiver will be able to decode ``chunk 0\\nchunk 1\\n`` at this point.
    >>> # Receiver is also expecting more data in the zstd *frame*.
    >>>
    >>> compressor.write(b"chunk 2\\n")
    >>> compressor.flush(zstandard.FLUSH_FRAME)
    >>> # Receiver will be able to decode ``chunk 0\\nchunk 1\\nchunk 2``.
    >>> # Receiver is expecting no more data, as the zstd frame is closed.
    >>> # Any future calls to ``write()`` at this point will construct a new
    >>> # zstd frame.

    Instances can be used as context managers. Exiting the context manager is
    the equivalent of calling ``close()``, which is equivalent to calling
    ``flush(zstandard.FLUSH_FRAME)``:

    >>> cctx = zstandard.ZstdCompressor(level=10)
    >>> with cctx.stream_writer(fh) as compressor:
    ...     compressor.write(b\'chunk 0\')
    ...     compressor.write(b\'chunk 1\')
    ...     ...

    .. important::

       If ``flush(FLUSH_FRAME)`` is not called, emitted data doesn\'t
       constitute a full zstd *frame* and consumers of this data may complain
       about malformed input. It is recommended to use instances as a context
       manager to ensure *frames* are properly finished.

    If the size of the data being fed to this streaming compressor is known,
    you can declare it before compression begins:

    >>> cctx = zstandard.ZstdCompressor()
    >>> with cctx.stream_writer(fh, size=data_len) as compressor:
    ...     compressor.write(chunk0)
    ...     compressor.write(chunk1)
    ...     ...

    Declaring the size of the source data allows compression parameters to
    be tuned. And if ``write_content_size`` is used, it also results in the
    content size being written into the frame header of the output data.

    The size of chunks being ``write()`` to the destination can be specified:

    >>> cctx = zstandard.ZstdCompressor()
    >>> with cctx.stream_writer(fh, write_size=32768) as compressor:
    ...     ...

    To see how much memory is being used by the streaming compressor:

    >>> cctx = zstandard.ZstdCompressor()
    >>> with cctx.stream_writer(fh) as compressor:
    ...     ...
    ...     byte_size = compressor.memory_size()

    Thte total number of bytes written so far are exposed via ``tell()``:

    >>> cctx = zstandard.ZstdCompressor()
    >>> with cctx.stream_writer(fh) as compressor:
    ...     ...
    ...     total_written = compressor.tell()

    ``stream_writer()`` accepts a ``write_return_read`` boolean argument to
    control the return value of ``write()``. When ``False`` (the default),
    ``write()`` returns the number of bytes that were ``write()``\'en to the
    underlying object. When ``True``, ``write()`` returns the number of bytes
    read from the input that were subsequently written to the compressor.
    ``True`` is the *proper* behavior for ``write()`` as specified by the
    ``io.RawIOBase`` interface and will become the default value in a future
    release.
    '''
    
    def __init__(self, compressor, writer, source_size, write_size, write_return_read, closefd = (True,)):
        self._compressor = compressor
        self._writer = writer
        self._write_size = write_size
        self._write_return_read = bool(write_return_read)
        self._closefd = bool(closefd)
        self._entered = False
        self._closing = False
        self._closed = False
        self._bytes_compressed = 0
        self._dst_buffer = ffi.new('char[]', write_size)
        self._out_buffer = ffi.new('ZSTD_outBuffer *')
        self._out_buffer.dst = self._dst_buffer
        self._out_buffer.size = len(self._dst_buffer)
        self._out_buffer.pos = 0
        zresult = lib.ZSTD_CCtx_setPledgedSrcSize(compressor._cctx, source_size)
        if lib.ZSTD_isError(zresult):
            raise ZstdError('error setting source size: %s' % _zstd_error(zresult))

    
    def __enter__(self):
        if self._closed:
            raise ValueError('stream is closed')
        if self._entered:
            raise ZstdError('cannot __enter__ multiple times')
        self._entered = True
        return self

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._entered = False
        self.close()
        self._compressor = None
        return False

    
    def __iter__(self):
        raise io.UnsupportedOperation()

    
    def __next__(self):
        raise io.UnsupportedOperation()

    
    def memory_size(self):
        return lib.ZSTD_sizeof_CCtx(self._compressor._cctx)

    
    def fileno(self):
        f = getattr(self._writer, 'fileno', None)
        if f:
            return f()
        raise None('fileno not available on underlying writer')

    
    def close(self):
        if self._closed:
            return None
        
        try:
            self._closing = True
            self.flush(FLUSH_FRAME)
            self._closing = False
            self._closed = True
        except:
            self._closing = False
            self._closed = True

        f = getattr(self._writer, 'close', None)
        if self._closefd or f:
            f()
            return None
        return None

    closed = (lambda self: self._closed)()
    
    def isatty(self):
        return False

    
    def readable(self):
        return False

    
    def readline(self, size = (-1,)):
        raise io.UnsupportedOperation()

    
    def readlines(self, hint = (-1,)):
        raise io.UnsupportedOperation()

    
    def seek(self, offset, whence = (None,)):
        raise io.UnsupportedOperation()

    
    def seekable(self):
        return False

    
    def truncate(self, size = (None,)):
        raise io.UnsupportedOperation()

    
    def writable(self):
        return True

    
    def writelines(self, lines):
        raise NotImplementedError('writelines() is not yet implemented')

    
    def read(self, size = (-1,)):
        raise io.UnsupportedOperation()

    
    def readall(self):
        raise io.UnsupportedOperation()

    
    def readinto(self, b):
        raise io.UnsupportedOperation()

    
    def write(self, data):
        '''Send data to the compressor and possibly to the inner stream.'''
        if self._closed:
            raise ValueError('stream is closed')
        total_write = 0
        data_buffer = ffi.from_buffer(data)
        in_buffer = ffi.new('ZSTD_inBuffer *')
        in_buffer.src = data_buffer
        in_buffer.size = len(data_buffer)
        in_buffer.pos = 0
        out_buffer = self._out_buffer
        out_buffer.pos = 0
    # WARNING: Decompyle incomplete

    
    def flush(self, flush_mode = (FLUSH_BLOCK,)):
        """Evict data from compressor's internal state and write it to inner stream.

        Calling this method may result in 0 or more ``write()`` calls to the
        inner stream.

        This method will also call ``flush()`` on the inner stream, if such a
        method exists.

        :param flush_mode:
           How to flush the zstd compressor.

           ``zstandard.FLUSH_BLOCK`` will flush data already sent to the
           compressor but not emitted to the inner stream. The stream is still
           writable after calling this. This is the default behavior.

           See documentation for other ``zstandard.FLUSH_*`` constants for more
           flushing options.
        :return:
           Integer number of bytes written to the inner stream.
        """
        if flush_mode == FLUSH_BLOCK:
            flush = lib.ZSTD_e_flush
        elif flush_mode == FLUSH_FRAME:
            flush = lib.ZSTD_e_end
        else:
            raise ValueError('unknown flush_mode: %r' % flush_mode)
        if self._closed:
            raise ValueError('stream is closed')
        total_write = 0
        out_buffer = self._out_buffer
        out_buffer.pos = 0
        in_buffer = ffi.new('ZSTD_inBuffer *')
        in_buffer.src = ffi.NULL
        in_buffer.size = 0
        in_buffer.pos = 0
        zresult = lib.ZSTD_compressStream2(self._compressor._cctx, out_buffer, in_buffer, flush)
        if lib.ZSTD_isError(zresult):
            raise ZstdError('zstd compress error: %s' % _zstd_error(zresult))
        if out_buffer.pos:
            self._writer.write(ffi.buffer(out_buffer.dst, out_buffer.pos)[:])
            total_write += out_buffer.pos
            0 = self, self._bytes_compressed += out_buffer.pos, ._bytes_compressed
        if not zresult:
            pass
        
        f = getattr(self._writer, 'flush', None)
        if not f and self._closing:
            f()
        return total_write

    
    def tell(self):
        return self._bytes_compressed



class ZstdCompressionObj(object):
    '''A compressor conforming to the API in Python\'s standard library.

    This type implements an API similar to compression types in Python\'s
    standard library such as ``zlib.compressobj`` and ``bz2.BZ2Compressor``.
    This enables existing code targeting the standard library API to swap
    in this type to achieve zstd compression.

    .. important::

       The design of this API is not ideal for optimal performance.

       The reason performance is not optimal is because the API is limited to
       returning a single buffer holding compressed data. When compressing
       data, we don\'t know how much data will be emitted. So in order to
       capture all this data in a single buffer, we need to perform buffer
       reallocations and/or extra memory copies. This can add significant
       overhead depending on the size or nature of the compressed data how
       much your application calls this type.

       If performance is critical, consider an API like
       :py:meth:`ZstdCompressor.stream_reader`,
       :py:meth:`ZstdCompressor.stream_writer`,
       :py:meth:`ZstdCompressor.chunker`, or
       :py:meth:`ZstdCompressor.read_to_iter`, which result in less overhead
       managing buffers.

    Instances are obtained by calling :py:meth:`ZstdCompressor.compressobj`.

    Here is how this API should be used:

    >>> cctx = zstandard.ZstdCompressor()
    >>> cobj = cctx.compressobj()
    >>> data = cobj.compress(b"raw input 0")
    >>> data = cobj.compress(b"raw input 1")
    >>> data = cobj.flush()

    Or to flush blocks:

    >>> cctx.zstandard.ZstdCompressor()
    >>> cobj = cctx.compressobj()
    >>> data = cobj.compress(b"chunk in first block")
    >>> data = cobj.flush(zstandard.COMPRESSOBJ_FLUSH_BLOCK)
    >>> data = cobj.compress(b"chunk in second block")
    >>> data = cobj.flush()

    For best performance results, keep input chunks under 256KB. This avoids
    extra allocations for a large output object.

    It is possible to declare the input size of the data that will be fed
    into the compressor:

    >>> cctx = zstandard.ZstdCompressor()
    >>> cobj = cctx.compressobj(size=6)
    >>> data = cobj.compress(b"foobar")
    >>> data = cobj.flush()
    '''
    
    def __init__(self, compressor, write_size = (COMPRESSION_RECOMMENDED_OUTPUT_SIZE,)):
        self._compressor = compressor
        self._out = ffi.new('ZSTD_outBuffer *')
        self._dst_buffer = ffi.new('char[]', write_size)
        self._out.dst = self._dst_buffer
        self._out.size = write_size
        self._out.pos = 0
        self._finished = False

    
    def compress(self, data):
        '''Send data to the compressor.

        This method receives bytes to feed to the compressor and returns
        bytes constituting zstd compressed data.

        The zstd compressor accumulates bytes and the returned bytes may be
        substantially smaller or larger than the size of the input data on
        any given call. The returned value may be the empty byte string
        (``b""``).

        :param data:
           Data to write to the compressor.
        :return:
           Compressed data.
        '''
        if self._finished:
            raise ZstdError('cannot call compress() after compressor finished')
        data_buffer = ffi.from_buffer(data)
        source = ffi.new('ZSTD_inBuffer *')
        source.src = data_buffer
        source.size = len(data_buffer)
        source.pos = 0
        chunks = []
    # WARNING: Decompyle incomplete

    
    def flush(self, flush_mode = (COMPRESSOBJ_FLUSH_FINISH,)):
        """Emit data accumulated in the compressor that hasn't been outputted yet.

        The ``flush_mode`` argument controls how to end the stream.

        ``zstandard.COMPRESSOBJ_FLUSH_FINISH`` (the default) ends the
        compression stream and finishes a zstd frame. Once this type of flush
        is performed, ``compress()`` and ``flush()`` can no longer be called.
        This type of flush **must** be called to end the compression context. If
        not called, the emitted data may be incomplete and may not be readable
        by a decompressor.

        ``zstandard.COMPRESSOBJ_FLUSH_BLOCK`` will flush a zstd block. This
        ensures that all data fed to this instance will have been omitted and
        can be decoded by a decompressor. Flushes of this type can be performed
        multiple times. The next call to ``compress()`` will begin a new zstd
        block.

        :param flush_mode:
           How to flush the zstd compressor.
        :return:
           Compressed data.
        """
        if flush_mode not in (COMPRESSOBJ_FLUSH_FINISH, COMPRESSOBJ_FLUSH_BLOCK):
            raise ValueError('flush mode not recognized')
        if self._finished:
            raise ZstdError('compressor object already finished')
        if flush_mode == COMPRESSOBJ_FLUSH_BLOCK:
            z_flush_mode = lib.ZSTD_e_flush
        elif flush_mode == COMPRESSOBJ_FLUSH_FINISH:
            z_flush_mode = lib.ZSTD_e_end
            self._finished = True
        else:
            raise ZstdError('unhandled flush mode')
    # WARNING: Decompyle incomplete



class ZstdCompressionChunker(object):
    """Compress data to uniformly sized chunks.

    This type allows you to iteratively feed chunks of data into a compressor
    and produce output chunks of uniform size.

    ``compress()``, ``flush()``, and ``finish()`` all return an iterator of
    ``bytes`` instances holding compressed data. The iterator may be empty.
    Callers MUST iterate through all elements of the returned iterator before
    performing another operation on the object or else the compressor's
    internal state may become confused. This can result in an exception being
    raised or malformed data being emitted.

    All chunks emitted by ``compress()`` will have a length of the configured
    chunk size.

    ``flush()`` and ``finish()`` may return a final chunk smaller than
    the configured chunk size.

    Instances are obtained by calling :py:meth:`ZstdCompressor.chunker`.

    Here is how the API should be used:

    >>> cctx = zstandard.ZstdCompressor()
    >>> chunker = cctx.chunker(chunk_size=32768)
    >>>
    >>> with open(path, 'rb') as fh:
    ...     while True:
    ...         in_chunk = fh.read(32768)
    ...         if not in_chunk:
    ...             break
    ...
    ...         for out_chunk in chunker.compress(in_chunk):
    ...             # Do something with output chunk of size 32768.
    ...
    ...     for out_chunk in chunker.finish():
    ...         # Do something with output chunks that finalize the zstd frame.

    This compressor type is often a better alternative to
    :py:class:`ZstdCompressor.compressobj` because it has better performance
    properties.

    ``compressobj()`` will emit output data as it is available. This results
    in a *stream* of output chunks of varying sizes. The consistency of the
    output chunk size with ``chunker()`` is more appropriate for many usages,
    such as sending compressed data to a socket.

    ``compressobj()`` may also perform extra memory reallocations in order
    to dynamically adjust the sizes of the output chunks. Since ``chunker()``
    output chunks are all the same size (except for flushed or final chunks),
    there is less memory allocation/copying overhead.
    """
    
    def __init__(self, compressor, chunk_size):
        self._compressor = compressor
        self._out = ffi.new('ZSTD_outBuffer *')
        self._dst_buffer = ffi.new('char[]', chunk_size)
        self._out.dst = self._dst_buffer
        self._out.size = chunk_size
        self._out.pos = 0
        self._in = ffi.new('ZSTD_inBuffer *')
        self._in.src = ffi.NULL
        self._in.size = 0
        self._in.pos = 0
        self._finished = False

    
    def compress(self, data):
        '''Feed new input data into the compressor.

        :param data:
           Data to feed to compressor.
        :return:
           Iterator of ``bytes`` representing chunks of compressed data.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self):
        '''Flushes all data currently in the compressor.

        :return:
           Iterator of ``bytes`` of compressed data.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def finish(self):
        '''Signals the end of input data.

        No new data can be compressed after this method is called.

        This method will flush buffered data and finish the zstd frame.

        :return:
           Iterator of ``bytes`` of compressed data.
        '''
        pass
    # WARNING: Decompyle incomplete



class ZstdCompressionReader(object):
    """Readable compressing stream wrapper.

    ``ZstdCompressionReader`` is a read-only stream interface for obtaining
    compressed data from a source.

    This type conforms to the ``io.RawIOBase`` interface and should be usable
    by any type that operates against a *file-object* (``typing.BinaryIO``
    in Python type hinting speak).

    Instances are neither writable nor seekable (even if the underlying
    source is seekable). ``readline()`` and ``readlines()`` are not implemented
    because they don't make sense for compressed data. ``tell()`` returns the
    number of compressed bytes emitted so far.

    Instances are obtained by calling :py:meth:`ZstdCompressor.stream_reader`.

    In this example, we open a file for reading and then wrap that file
    handle with a stream from which compressed data can be ``read()``.

    >>> with open(path, 'rb') as fh:
    ...     cctx = zstandard.ZstdCompressor()
    ...     reader = cctx.stream_reader(fh)
    ...     while True:
    ...         chunk = reader.read(16384)
    ...         if not chunk:
    ...             break
    ...
    ...         # Do something with compressed chunk.

    Instances can also be used as context managers:

    >>> with open(path, 'rb') as fh:
    ...     cctx = zstandard.ZstdCompressor()
    ...     with cctx.stream_reader(fh) as reader:
    ...         while True:
    ...             chunk = reader.read(16384)
    ...             if not chunk:
    ...                 break
    ...
    ...             # Do something with compressed chunk.

    When the context manager exits or ``close()`` is called, the stream is
    closed, underlying resources are released, and future operations against
    the compression stream will fail.

    ``stream_reader()`` accepts a ``size`` argument specifying how large the
    input stream is. This is used to adjust compression parameters so they are
    tailored to the source size. e.g.

    >>> with open(path, 'rb') as fh:
    ...     cctx = zstandard.ZstdCompressor()
    ...     with cctx.stream_reader(fh, size=os.stat(path).st_size) as reader:
    ...         ...

    If the ``source`` is a stream, you can specify how large ``read()``
    requests to that stream should be via the ``read_size`` argument.
    It defaults to ``zstandard.COMPRESSION_RECOMMENDED_INPUT_SIZE``. e.g.

    >>> with open(path, 'rb') as fh:
    ...     cctx = zstandard.ZstdCompressor()
    ...     # Will perform fh.read(8192) when obtaining data to feed into the
    ...     # compressor.
    ...     with cctx.stream_reader(fh, read_size=8192) as reader:
    ...         ...
    """
    
    def __init__(self, compressor, source, read_size, closefd = (True,)):
        self._compressor = compressor
        self._source = source
        self._read_size = read_size
        self._closefd = closefd
        self._entered = False
        self._closed = False
        self._bytes_compressed = 0
        self._finished_input = False
        self._finished_output = False
        self._in_buffer = ffi.new('ZSTD_inBuffer *')
        self._source_buffer = None

    
    def __enter__(self):
        if self._entered:
            raise ValueError('cannot __enter__ multiple times')
        if self._closed:
            raise ValueError('stream is closed')
        self._entered = True
        return self

    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._entered = False
        self._compressor = None
        self.close()
        self._source = None
        return False

    
    def readable(self):
        return True

    
    def writable(self):
        return False

    
    def seekable(self):
        return False

    
    def readline(self):
        raise io.UnsupportedOperation()

    
    def readlines(self):
        raise io.UnsupportedOperation()

    
    def write(self, data):
        raise OSError('stream is not writable')

    
    def writelines(self, ignored):
        raise OSError('stream is not writable')

    
    def isatty(self):
        return False

    
    def flush(self):
        pass

    
    def close(self):
        if self._closed:
            return None
        self._closed = None
        f = getattr(self._source, 'close', None)
        if self._closefd or f:
            f()
            return None
        return None

    closed = (lambda self: self._closed)()
    
    def tell(self):
        return self._bytes_compressed

    
    def readall(self):
        chunks = []
        chunk = self.read(1048576)
        if not chunk:
            pass
        else:
            chunks.append(chunk)
        return b''.join(chunks)

    
    def __iter__(self):
        raise io.UnsupportedOperation()

    
    def __next__(self):
        raise io.UnsupportedOperation()

    next = __next__
    
    def _read_input(self):
        if self._finished_input:
            return None
        if None(self._source, 'read'):
            data = self._source.read(self._read_size)
            if not data:
                self._finished_input = True
                return None
            self._source_buffer = None.from_buffer(data)
            self._in_buffer.src = self._source_buffer
            self._in_buffer.size = len(self._source_buffer)
            self._in_buffer.pos = 0
            return None
        self._source_buffer = None.from_buffer(self._source)
        self._in_buffer.src = self._source_buffer
        self._in_buffer.size = len(self._source_buffer)
        self._in_buffer.pos = 0

    
    def _compress_into_buffer(self, out_buffer):
