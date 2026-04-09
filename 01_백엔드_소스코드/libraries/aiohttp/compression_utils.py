# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compression_utils.pyc (Python 3.11)

import asyncio
import sys
import zlib
from concurrent.futures import Executor
from typing import Any, Final, Optional, Protocol, TypedDict, cast
if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    from typing import Union
    Buffer = Union[(bytes, bytearray, 'memoryview[int]', 'memoryview[bytes]')]

try:
    import brotlicffi as brotli
    
    try:
        pass
    except ImportError:
        import brotli
        
        try:
            pass
        try:
            HAS_BROTLI = True
        except ImportError:
            HAS_BROTLI = False

        
        try:
            if sys.version_info >= (3, 14):
                from compression.zstd import ZstdDecompressor
            else:
                from backports.zstd import ZstdDecompressor
            HAS_ZSTD = True
        except ImportError:
            HAS_ZSTD = False

        MAX_SYNC_CHUNK_SIZE = 1024
        
        class ZLibCompressObjProtocol(Protocol):
            
            def compress(self = None, data = None):
                pass

            
            def flush(self = None, mode = None):
                pass


        
        class ZLibDecompressObjProtocol(Protocol):
            
            def decompress(self = None, data = None, max_length = None):
                pass

            
            def flush(self = None, length = None):
                pass

            eof = (lambda self = None: pass)()

        
        class ZLibBackendProtocol(Protocol):
            Z_FINISH: int = 'ZLibBackendProtocol'
            
            def compressobj(self, level, method = None, wbits = None, memLevel = None, strategy = (..., ..., ..., ..., ..., ...), zdict = ('level', int, 'method', int, 'wbits', int, 'memLevel', int, 'strategy', int, 'zdict', Optional[Buffer], 'return', ZLibCompressObjProtocol)):
                pass

            
            def decompressobj(self = None, wbits = None, zdict = None):
                pass

            
            def compress(self = None, data = None, level = None, wbits = (..., ...)):
                pass

            
            def decompress(self = None, data = None, wbits = None, bufsize = (..., ...)):
                pass


        
        def CompressObjArgs():
            '''CompressObjArgs'''
            level: int = 'CompressObjArgs'

        CompressObjArgs = <NODE:27>(CompressObjArgs, 'CompressObjArgs', TypedDict, total = False)
        
        class ZLibBackendWrapper:
            
            def __init__(self = None, _zlib_backend = None):
                self._zlib_backend = _zlib_backend

            name = (lambda self = None: getattr(self._zlib_backend, '__name__', 'undefined'))()
            MAX_WBITS = (lambda self = None: self._zlib_backend.MAX_WBITS)()
            Z_FULL_FLUSH = (lambda self = None: self._zlib_backend.Z_FULL_FLUSH)()
            Z_SYNC_FLUSH = (lambda self = None: self._zlib_backend.Z_SYNC_FLUSH)()
            Z_BEST_SPEED = (lambda self = None: self._zlib_backend.Z_BEST_SPEED)()
            Z_FINISH = (lambda self = None: self._zlib_backend.Z_FINISH)()
            
            def compressobj(self = None, *args, **kwargs):
                pass
            # WARNING: Decompyle incomplete

            
            def decompressobj(self = None, *args, **kwargs):
                pass
            # WARNING: Decompyle incomplete

            
            def compress(self = None, data = None, *args, **kwargs):
                pass
            # WARNING: Decompyle incomplete

            
            def decompress(self = None, data = None, *args, **kwargs):
                pass
            # WARNING: Decompyle incomplete

            
            def __getattr__(self = None, attrname = None):
                return getattr(self._zlib_backend, attrname)


        ZLibBackend: ZLibBackendWrapper = ZLibBackendWrapper(zlib)
        
        def set_zlib_backend(new_zlib_backend = None):
            ZLibBackend._zlib_backend = new_zlib_backend

        
        def encoding_to_mode(encoding = None, suppress_deflate_header = None):
            if encoding == 'gzip':
                return 16 + ZLibBackend.MAX_WBITS
            return -(ZLibBackend.MAX_WBITS) if None else ZLibBackend.MAX_WBITS

        
        class ZlibBaseHandler:
            
            def __init__(self = None, mode = None, executor = None, max_sync_chunk_size = (None, MAX_SYNC_CHUNK_SIZE)):
                self._mode = mode
                self._executor = executor
                self._max_sync_chunk_size = max_sync_chunk_size


        
        class ZLibCompressor(ZlibBaseHandler):
            pass
        # WARNING: Decompyle incomplete

        
        class ZLibDecompressor(ZlibBaseHandler):
            pass
        # WARNING: Decompyle incomplete

        
        class BrotliDecompressor:
            
            def __init__(self = None):
                if not HAS_BROTLI:
                    raise RuntimeError('The brotli decompression is not available. Please install `Brotli` module')
                self._obj = brotli.Decompressor()

            
            def decompress_sync(self = None, data = None):
                if hasattr(self._obj, 'decompress'):
                    return cast(bytes, self._obj.decompress(data))
                return None(bytes, self._obj.process(data))

            
            def flush(self = None):
                if hasattr(self._obj, 'flush'):
                    return cast(bytes, self._obj.flush())


        
        class ZSTDDecompressor:
            
            def __init__(self = None):
                if not HAS_ZSTD:
                    raise RuntimeError('The zstd decompression is not available. Please install `backports.zstd` module')
                self._obj = ZstdDecompressor()

            
            def decompress_sync(self = None, data = None):
                return self._obj.decompress(data)

            
            def flush(self = None):
                return b''


        return None
