# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import annotations
import json
import typing as t
from http import HTTPStatus
from urllib.parse import urljoin
from _internal import _get_environ
from datastructures import Headers
from http import generate_etag
from http import http_date
from http import is_resource_modified
from http import parse_etags
from http import parse_range_header
from http import remove_entity_headers
from sansio.response import Response as _SansIOResponse
from urls import iri_to_uri
from utils import cached_property
from wsgi import _RangeWrapper
from wsgi import ClosingIterator
from wsgi import get_current_url
if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment
    from request import Request

def _iter_encoded(iterable = None):
    pass
# WARNING: Decompyle incomplete


class Response(_SansIOResponse):
    pass
# WARNING: Decompyle incomplete


class ResponseStream:
    '''A file descriptor like object used by :meth:`Response.stream` to
    represent the body of the stream. It directly pushes into the
    response iterable of the response object.
    '''
    mode = 'wb+'
    
    def __init__(self = None, response = None):
        self.response = response
        self.closed = False

    
    def write(self = None, value = None):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        self.response._ensure_sequence(mutable = True)
        self.response.response.append(value)
        self.response.headers.pop('Content-Length', None)
        return len(value)

    
    def writelines(self = None, seq = None):
        for item in seq:
            self.write(item)
            return None

    
    def close(self = None):
        self.closed = True

    
    def flush(self = None):
        if self.closed:
            raise ValueError('I/O operation on closed file')

    
    def isatty(self = None):
        if self.closed:
            raise ValueError('I/O operation on closed file')
        return False

    
    def tell(self = None):
        self.response._ensure_sequence()
        return sum(map(len, self.response.response))

    encoding = (lambda self = None: 'utf-8')()
