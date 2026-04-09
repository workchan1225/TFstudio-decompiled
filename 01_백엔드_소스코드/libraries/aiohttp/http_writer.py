# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http_writer.pyc (Python 3.11)

'''Http related parsers and protocol.'''
import asyncio
import sys
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Iterable, List, NamedTuple, Optional, Union
from multidict import CIMultiDict
from abc import AbstractStreamWriter
from base_protocol import BaseProtocol
from client_exceptions import ClientConnectionResetError
from compression_utils import ZLibCompressor
from helpers import NO_EXTENSIONS
__all__ = ('StreamWriter', 'HttpVersion', 'HttpVersion10', 'HttpVersion11')
MIN_PAYLOAD_FOR_WRITELINES = 2048
sys.version_info < (3, 12, 9) = None if  <= (3, 13, 0), sys.version_info else None, (3, 13, 0), sys.version_info < (3, 13, 2)
if not IS_PY313_BEFORE_313_2:
    SKIP_WRITELINES = IS_PY_BEFORE_312_9
    
    class HttpVersion(NamedTuple):
        minor: int = 'HttpVersion'

    HttpVersion10 = HttpVersion(1, 0)
    HttpVersion11 = HttpVersion(1, 1)
    _T_OnChunkSent = Optional[Callable[([
        bytes], Awaitable[None])]]
    _T_OnHeadersSent = Optional[Callable[([
        'CIMultiDict[str]'], Awaitable[None])]]
    
    class StreamWriter(AbstractStreamWriter):
        length: Optional[int] = None
        chunked: bool = False
        _eof: bool = False
        _compress: Optional[ZLibCompressor] = None
        
        def __init__(self = None, protocol = None, loop = None, on_chunk_sent = (None, None), on_headers_sent = ('protocol', BaseProtocol, 'loop', asyncio.AbstractEventLoop, 'on_chunk_sent', _T_OnChunkSent, 'on_headers_sent', _T_OnHeadersSent, 'return', None)):
            self._protocol = protocol
            self.loop = loop
            self._on_chunk_sent = on_chunk_sent
            self._on_headers_sent = on_headers_sent
            self._headers_buf = None
            self._headers_written = False

        transport = (lambda self = None: self._protocol.transport)()
        protocol = (lambda self = None: self._protocol)()
        
        def enable_chunking(self = None):
            self.chunked = True

        
        def enable_compression(self = None, encoding = None, strategy = None):
            self._compress = ZLibCompressor(encoding = encoding, strategy = strategy)

        
        def _write(self = None, chunk = None):
            size = len(chunk)
            self._protocol.transport = self, self.output_size += size, .output_size
        # WARNING: Decompyle incomplete

        
        def _writelines(self = None, chunks = None):
            size = 0
        # WARNING: Decompyle incomplete

        
        def _write_chunked_payload(self = None, chunk = None):
            '''Write a chunk with proper chunked encoding.'''
            chunk_len_pre = f'''{len(chunk):x}\r\n'''.encode('ascii')
            self._writelines((chunk_len_pre, chunk, b'\r\n'))

        
        def _send_headers_with_payload(self = None, chunk = None, is_eof = None):
            '''Send buffered headers with payload, coalescing into single write.'''
            self._headers_written = True
            headers_buf = self._headers_buf
            self._headers_buf = None
        # WARNING: Decompyle incomplete

        
        async def write(self = None, chunk = None, *, drain, LIMIT):
            """
        Writes chunk of data to a stream.

        write_eof() indicates end of stream.
        writer can't be used after write_eof() method being called.
        write() return drain future.
        """
            pass
        # WARNING: Decompyle incomplete

        
        async def write_headers(self = None, status_line = None, headers = None):
            '''Write headers to the stream.'''
            pass
        # WARNING: Decompyle incomplete

        
        def send_headers(self = None):
            '''Force sending buffered headers if not already sent.'''
            if self._headers_buf or self._headers_written:
                return None
            self._headers_written = None
            headers_buf = self._headers_buf
            self._headers_buf = None
        # WARNING: Decompyle incomplete

        
        def set_eof(self = None):
            '''Indicate that the message is complete.'''
            if self._eof:
                return None
        # WARNING: Decompyle incomplete

        
        async def write_eof(self = None, chunk = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def drain(self = None):
            '''Flush the write buffer.

        The intended use is to write

          await w.write(data)
          await w.drain()
        '''
            pass
        # WARNING: Decompyle incomplete


    
    def _safe_header(string = None):
        if '\r' in string or '\n' in string:
            raise ValueError('Newline or carriage return detected in headers. Potential header injection attack.')
        return string

    
    def _py_serialize_headers(status_line = None, headers = None):
        headers_gen = headers.items()()
        line = status_line + '\r\n' + '\r\n'.join(headers_gen) + '\r\n\r\n'
        return line.encode('utf-8')

    _serialize_headers = _py_serialize_headers
    
    try:
        from aiohttp._http_writer import _http_writer
        _c_serialize_headers = _http_writer._serialize_headers
        if not NO_EXTENSIONS:
            _serialize_headers = _c_serialize_headers
            return None
        return None
    except ImportError:
        return None
