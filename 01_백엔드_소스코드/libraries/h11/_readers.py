# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _readers.pyc (Python 3.11)

import re
from typing import Any, Callable, Dict, Iterable, NoReturn, Optional, Tuple, Type, Union
from _abnf import chunk_header, header_field, request_line, status_line
from _events import Data, EndOfMessage, InformationalResponse, Request, Response
from _receivebuffer import ReceiveBuffer
from _state import CLIENT, CLOSED, DONE, IDLE, MUST_CLOSE, SEND_BODY, SEND_RESPONSE, SERVER
from _util import LocalProtocolError, RemoteProtocolError, Sentinel, validate
__all__ = [
    'READERS']
header_field_re = re.compile(header_field.encode('ascii'))
obs_fold_re = re.compile(b'[ \\t]+')

def _obsolete_line_fold(lines = None):
    pass
# WARNING: Decompyle incomplete


def _decode_header_lines(lines = None):
    pass
# WARNING: Decompyle incomplete

request_line_re = re.compile(request_line.encode('ascii'))

def maybe_read_from_IDLE_client(buf = None):
    lines = buf.maybe_extract_lines()
# WARNING: Decompyle incomplete

status_line_re = re.compile(status_line.encode('ascii'))

def maybe_read_from_SEND_RESPONSE_server(buf = None):
    lines = buf.maybe_extract_lines()
# WARNING: Decompyle incomplete


class ContentLengthReader:
    
    def __init__(self = None, length = None):
        self._length = length
        self._remaining = length

    
    def __call__(self = None, buf = None):
        if self._remaining == 0:
            return EndOfMessage()
        data = None.maybe_extract_at_most(self._remaining)
    # WARNING: Decompyle incomplete

    
    def read_eof(self = None):
        raise RemoteProtocolError('peer closed connection without sending complete message body (received {} bytes, expected {})'.format(self._length - self._remaining, self._length))


chunk_header_re = re.compile(chunk_header.encode('ascii'))

class ChunkedReader:
    
    def __init__(self = None):
        self._bytes_in_chunk = 0
        self._bytes_to_discard = b''
        self._reading_trailer = False

    
    def __call__(self = None, buf = None):
        pass
    # WARNING: Decompyle incomplete

    
    def read_eof(self = None):
        raise RemoteProtocolError('peer closed connection without sending complete message body (incomplete chunked read)')



class Http10Reader:
    
    def __call__(self = None, buf = None):
        data = buf.maybe_extract_at_most(999999999)
    # WARNING: Decompyle incomplete

    
    def read_eof(self = None):
        return EndOfMessage()



def expect_nothing(buf = None):
    if buf:
        raise LocalProtocolError('Got data when expecting EOF')

ReadersType = Dict[(Union[(Type[Sentinel], Tuple[(Type[Sentinel], Type[Sentinel])])], Union[(Callable[(..., Any)], Dict[(str, Callable[(..., Any)])])])]
READERS: ReadersType = {
    SEND_BODY: {
        'chunked': ChunkedReader,
        'content-length': ContentLengthReader,
        'http/1.0': Http10Reader },
    (SERVER, CLOSED): expect_nothing,
    (SERVER, MUST_CLOSE): expect_nothing,
    (SERVER, DONE): expect_nothing,
    (CLIENT, CLOSED): expect_nothing,
    (CLIENT, MUST_CLOSE): expect_nothing,
    (CLIENT, DONE): expect_nothing,
    (SERVER, SEND_RESPONSE): maybe_read_from_SEND_RESPONSE_server,
    (SERVER, IDLE): maybe_read_from_SEND_RESPONSE_server,
    (CLIENT, IDLE): maybe_read_from_IDLE_client }
