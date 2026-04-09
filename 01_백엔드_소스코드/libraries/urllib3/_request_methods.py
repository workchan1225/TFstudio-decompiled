# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _request_methods.pyc (Python 3.11)

from __future__ import annotations
import json as _json
import typing
from urllib.parse import urlencode
from _base_connection import _TYPE_BODY
from _collections import HTTPHeaderDict
from filepost import _TYPE_FIELDS, encode_multipart_formdata
from response import BaseHTTPResponse
__all__ = [
    'RequestMethods']
_TYPE_ENCODE_URL_FIELDS = typing.Union[(typing.Sequence[tuple[(str, typing.Union[(str, bytes)])]], typing.Mapping[(str, typing.Union[(str, bytes)])])]

class RequestMethods:
    '''
    Convenience mixin for classes who implement a :meth:`urlopen` method, such
    as :class:`urllib3.HTTPConnectionPool` and
    :class:`urllib3.PoolManager`.

    Provides behavior for making common types of HTTP request methods and
    decides which type of request field encoding to use.

    Specifically,

    :meth:`.request_encode_url` is for sending requests whose fields are
    encoded in the URL (such as GET, HEAD, DELETE).

    :meth:`.request_encode_body` is for sending requests whose fields are
    encoded in the *body* of the request using multipart or www-form-urlencoded
    (such as for POST, PUT, PATCH).

    :meth:`.request` is for making any kind of request, it will look up the
    appropriate encoding format and use one of the above two methods to make
    the request.

    Initializer parameters:

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.
    '''
    _encode_url_methods = {
        'GET',
        'HEAD',
        'DELETE',
        'OPTIONS'}
    
    def __init__(self = None, headers = None):
