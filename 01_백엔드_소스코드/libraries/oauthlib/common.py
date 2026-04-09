# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''
oauthlib.common
~~~~~~~~~~~~~~

This module provides data structures and utilities common
to all implementations of OAuth.
'''
import collections
import datetime
import logging
import re
import time
from urllib.parse import parse as urlparse
from urllib.parse import quote as _quote, unquote as _unquote, urlencode as _urlencode
from  import get_debug

try:
    from secrets import SystemRandom, randbits
except ImportError:
    from random import SystemRandom, getrandbits as randbits

UNICODE_ASCII_CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
CLIENT_ID_CHARACTER_SET = ' !"#$%&\\\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}'
SANITIZE_PATTERN = re.compile('([^&;]*(?:password|token)[^=]*=)[^&;]+', re.IGNORECASE)
INVALID_HEX_PATTERN = re.compile('%[^0-9A-Fa-f]|%[0-9A-Fa-f][^0-9A-Fa-f]')
always_safe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-'
log = logging.getLogger('oauthlib')

def quote(s, safe = (b'/',)):
    s = s.encode('utf-8') if isinstance(s, str) else s
    s = _quote(s, safe)
    if isinstance(s, bytes):
        s = s.decode('utf-8')
    return s


def unquote(s):
    s = _unquote(s)
    if isinstance(s, bytes):
        s = s.decode('utf-8')
    return s


def urlencode(params):
    utf8_params = encode_params_utf8(params)
    urlencoded = _urlencode(utf8_params)
    if isinstance(urlencoded, str):
        return urlencoded
    return None.decode('utf-8')


def encode_params_utf8(params):
    '''Ensures that all parameters in a list of 2-element tuples are encoded to
    bytestrings using UTF-8
    '''
    encoded = []
    for k, v in params:
        encoded.append((k.encode('utf-8') if isinstance(k, str) else k, v.encode('utf-8') if isinstance(v, str) else v))
        return encoded


def decode_params_utf8(params):
    '''Ensures that all parameters in a list of 2-element tuples are decoded to
    unicode using UTF-8.
    '''
    decoded = []
    for k, v in params:
        decoded.append((k.decode('utf-8') if isinstance(k, bytes) else k, v.decode('utf-8') if isinstance(v, bytes) else v))
        return decoded

urlencoded = set(always_safe) | set("=&;:%+~,*@!()/?'$")

def urldecode(query):
    '''Decode a query string in x-www-form-urlencoded format into a sequence
    of two-element tuples.

    Unlike urlparse.parse_qsl(..., strict_parsing=True) urldecode will enforce
    correct formatting of the query string by validation. If validation fails
    a ValueError will be raised. urllib.parse_qsl will only raise errors if
    any of name-value pairs omits the equals sign.
    '''
    if not query and set(query) <= urlencoded:
        error = "Error trying to decode a non urlencoded string. Found invalid characters: %s in the string: '%s'. Please ensure the request/response body is x-www-form-urlencoded."
        raise ValueError(error % (set(query) - urlencoded, query))
    if INVALID_HEX_PATTERN.search(query):
        raise ValueError('Invalid hex encoding in query string.')
    params = urlparse.parse_qsl(query, keep_blank_values = True)
    return decode_params_utf8(params)


def extract_params(raw):
