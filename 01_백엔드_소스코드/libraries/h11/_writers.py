# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _writers.pyc (Python 3.11)

from typing import Any, Callable, Dict, List, Tuple, Type, Union
from _events import Data, EndOfMessage, Event, InformationalResponse, Request, Response
from _headers import Headers
from _state import CLIENT, IDLE, SEND_BODY, SEND_RESPONSE, SERVER
from _util import LocalProtocolError, Sentinel
__all__ = [
    'WRITERS']
Writer = Callable[([
    bytes], Any)]

def write_headers(headers = None, write = None):
    raw_items = headers._full_items
    for raw_name, name, value in raw_items:
        if name == b'host':
            write(b'%s: %s\r\n' % (raw_name, value))
        for raw_name, name, value in raw_items:
            if name != b'host':
                write(b'%s: %s\r\n' % (raw_name, value))
            write(b'\r\n')
            return None


def write_request(request = None, write = None):
    if request.http_version != b'1.1':
        raise LocalProtocolError('I only send HTTP/1.1')
    write(b'%s %s HTTP/1.1\r\n' % (request.method, request.target))
    write_headers(request.headers, write)


def write_any_response(response = None, write = None):
    if response.http_version != b'1.1':
        raise LocalProtocolError('I only send HTTP/1.1')
    status_bytes = str(response.status_code).encode('ascii')
    write(b'HTTP/1.1 %s %s\r\n' % (status_bytes, response.reason))
    write_headers(response.headers, write)


class BodyWriter:
    
    def __call__(self = None, event = None, write = None):
        if type(event) is Data:
            self.send_data(event.data, write)
            return None
        if None(event) is EndOfMessage:
            self.send_eom(event.headers, write)
            return None
        raise None

    
    def send_data(self = None, data = None, write = None):
        pass

    
    def send_eom(self = None, headers = None, write = None):
        pass



class ContentLengthWriter(BodyWriter):
    
    def __init__(self = None, length = None):
        self._length = length

    
    def send_data(self = None, data = None, write = None):
        if self._length < 0:
            raise LocalProtocolError('Too much data for declared Content-Length')
        write(data)

    
    def send_eom(self = None, headers = None, write = None):
        if self._length != 0:
            raise LocalProtocolError('Too little data for declared Content-Length')
        if headers:
            raise LocalProtocolError("Content-Length and trailers don't mix")



class ChunkedWriter(BodyWriter):
    
    def send_data(self = None, data = None, write = None):
        if not data:
            return None
        write(b'%x\r\n' % len(data))
        write(data)
        write(b'\r\n')

    
    def send_eom(self = None, headers = None, write = None):
        write(b'0\r\n')
        write_headers(headers, write)



class Http10Writer(BodyWriter):
    
    def send_data(self = None, data = None, write = None):
        write(data)

    
    def send_eom(self = None, headers = None, write = None):
        if headers:
            raise LocalProtocolError("can't send trailers to HTTP/1.0 client")


WritersType = Dict[(Union[(Tuple[(Type[Sentinel], Type[Sentinel])], Type[Sentinel])], Union[(Dict[(str, Type[BodyWriter])], Callable[([
    Union[(InformationalResponse, Response)],
    Writer], None)], Callable[([
    Request,
    Writer], None)])])]
WRITERS: WritersType = {
    SEND_BODY: {
        'chunked': ChunkedWriter,
        'content-length': ContentLengthWriter,
        'http/1.0': Http10Writer },
    (SERVER, SEND_RESPONSE): write_any_response,
    (SERVER, IDLE): write_any_response,
    (CLIENT, IDLE): write_request }
