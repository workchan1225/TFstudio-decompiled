# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _models.pyc (Python 3.11)

from __future__ import annotations
import codecs
import datetime
import email.message as email
import json as jsonlib
import re
import typing
import urllib.request as urllib
from collections.abc import Mapping
from http.cookiejar import Cookie, CookieJar
from _content import ByteStream, UnattachedStream, encode_request, encode_response
from _decoders import SUPPORTED_DECODERS, ByteChunker, ContentDecoder, IdentityDecoder, LineDecoder, MultiDecoder, TextChunker, TextDecoder
from _exceptions import CookieConflict, HTTPStatusError, RequestNotRead, ResponseNotRead, StreamClosed, StreamConsumed, request_context
from _multipart import get_multipart_boundary_from_content_type
from _status_codes import codes
from _types import AsyncByteStream, CookieTypes, HeaderTypes, QueryParamTypes, RequestContent, RequestData, RequestExtensions, RequestFiles, ResponseContent, ResponseExtensions, SyncByteStream
from _urls import URL
from _utils import to_bytes_or_str, to_str
__all__ = [
    'Cookies',
    'Headers',
    'Request',
    'Response']
SENSITIVE_HEADERS = {
    'authorization',
    'proxy-authorization'}

def _is_known_encoding(encoding = None):
    '''
    Return `True` if `encoding` is a known codec.
    '''
    
    try:
        codecs.lookup(encoding)
    except LookupError:
        return False

    return True


def _normalize_header_key(key = None, encoding = None):
    '''
    Coerce str/bytes into a strictly byte-wise HTTP header key.
    '''
    if isinstance(key, bytes):
        pass
    elif not encoding:
        return encoding('ascii')


def _normalize_header_value(value = None, encoding = None):
