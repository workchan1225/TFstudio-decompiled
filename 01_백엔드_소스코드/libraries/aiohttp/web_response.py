# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_response.pyc (Python 3.11)

import asyncio
import collections.abc as collections
import datetime
import enum
import json
import math
import time
import warnings
from concurrent.futures import Executor
from http import HTTPStatus
from http.cookies import SimpleCookie
from typing import TYPE_CHECKING, Any, Dict, Iterator, MutableMapping, Optional, Union, cast
from multidict import CIMultiDict, istr
from  import hdrs, payload
from abc import AbstractStreamWriter
from compression_utils import ZLibCompressor
from helpers import ETAG_ANY, QUOTED_ETAG_RE, ETag, HeadersMixin, must_be_empty_body, parse_http_date, rfc822_formatted_time, sentinel, should_remove_content_length, validate_etag_value
from http import SERVER_SOFTWARE, HttpVersion10, HttpVersion11
from payload import Payload
from typedefs import JSONEncoder, LooseHeaders
REASON_PHRASES = HTTPStatus()
LARGE_BODY_SIZE = 1048576
__all__ = ('ContentCoding', 'StreamResponse', 'Response', 'json_response')

class ContentCoding(enum.Enum):
    deflate = 'deflate'
    gzip = 'gzip'
    identity = 'identity'

CONTENT_CODINGS = ContentCoding()

class StreamResponse(HeadersMixin, BaseClass):
    pass
# WARNING: Decompyle incomplete


class Response(StreamResponse):
    pass
# WARNING: Decompyle incomplete


def json_response(data = None, *, text, body, status, reason, headers, content_type, dumps):
    if data is not sentinel:
        if text or body:
            raise ValueError('only one of data, text, or body should be specified')
        text = dumps(data)
    return Response(text = text, body = body, status = status, reason = reason, headers = headers, content_type = content_type)
