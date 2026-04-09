# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: urllib3\__init__.py

"""
Python HTTP library with thread-safe connection pooling, file post support, user friendly, and more
"""

from __future__ import annotations
import logging
import sys
import typing
import warnings
from logging import NullHandler
from  import exceptions
from _base_connection import _TYPE_BODY
from _collections import HTTPHeaderDict
from _version import __version__
from connectionpool import HTTPConnectionPool
from filepost import _TYPE_FIELDS
from poolmanager import PoolManager
from response import BaseHTTPResponse
from util.request import make_headers
from util.retry import Retry
from util.timeout import Timeout
import ssl
from contrib.emscripten import inject_into_urllib3

def add_stderr_logger(level):
    """
    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    """
    # 74           0 RESUME                   0
    # 85           2 LOAD_GLOBAL              1 (NULL + logging)
    # 14 LOAD_ATTR                1 (getLogger)
    # 24 LOAD_GLOBAL              4 (__name__)
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 STORE_FAST               1 (logger)
    # 86          52 LOAD_GLOBAL              1 (NULL + logging)
    # 64 LOAD_ATTR                3 (StreamHandler)
    # 74 PRECALL                  0
    # 78 CALL                     0
    # 88 STORE_FAST               2 (handler)
    # 87          90 LOAD_FAST                2 (handler)
    # 92 LOAD_METHOD              4 (setFormatter)
    # 114 LOAD_GLOBAL              1 (NULL + logging)
    # 126 LOAD_ATTR                5 (Formatter)
    # 136 LOAD_CONST               1 ('%(asctime)s %(levelname)s %(message)s')
    # 138 PRECALL                  1
    # 142 CALL                     1
    # 152 PRECALL                  1
    # 156 CALL                     1
    # 166 POP_TOP
    # 88         168 LOAD_FAST                1 (logger)
    # 170 LOAD_METHOD              6 (addHandler)
    # 192 LOAD_FAST                2 (handler)
    # 194 PRECALL                  1
    # 198 CALL                     1
    # 208 POP_TOP
    # 89         210 LOAD_FAST                1 (logger)
    # 212 LOAD_METHOD              7 (setLevel)
    # 234 LOAD_FAST                0 (level)
    # 236 PRECALL                  1
    # 240 CALL                     1
    # 250 POP_TOP
    # 90         252 LOAD_FAST                1 (logger)
    # 254 LOAD_METHOD              8 (debug)
    # 276 LOAD_CONST               2 ('Added a stderr logging handler to logger: %s')
    # 278 LOAD_GLOBAL              4 (__name__)
    # 290 PRECALL                  2
    # 294 CALL                     2
    # 304 POP_TOP
    # 91         306 LOAD_FAST                2 (handler)
    # 308 RETURN_VALUE

def disable_warnings(category):
    """
    Helper for quickly disabling all urllib3 warnings.
    """
    # 107           0 RESUME                   0
    # 111           2 LOAD_GLOBAL              1 (NULL + warnings)
    # 14 LOAD_ATTR                1 (simplefilter)
    # 24 LOAD_CONST               1 ('ignore')
    # 26 LOAD_FAST                0 (category)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_TOP
    # 44 LOAD_CONST               2 (None)
    # 46 RETURN_VALUE

def request(method, url, *, body, fields, headers, preload_content, decode_content, redirect, retries, timeout, json):
    """
    A convenience, top-level request method. It uses a module-global ``PoolManager`` instance.
    Therefore, its side effects could be shared across dependencies relying on it.
    To avoid side effects create a new ``PoolManager`` instance and use it instead.
    The method does not accept low-level ``**urlopen_kw`` keyword arguments.

    :param method:
        HTTP request method (such as GET, POST, PUT, etc.)

    :param url:
        The URL to perform the request on.

    :param body:
        Data to send in the request body, either :class:`str`, :class:`bytes`,
        an iterable of :class:`str`/:class:`bytes`, or a file-like object.

    :param fields:
        Data to encode and send in the request body.

    :param headers:
        Dictionary of custom headers to send, such as User-Agent,
        If-None-Match, etc.

    :param bool preload_content:
        If True, the response's body will be preloaded into memory.

    :param bool decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param redirect:
        If True, automatically handle redirects (status codes 301, 302,
        303, 307, 308). Each redirect counts as a retry. Disabling retries
        will disable redirect, too.

    :param retries:
        Configure the number of retries to allow before raising a
        :class:`~urllib3.exceptions.MaxRetryError` exception.

        If ``None`` (default) will retry 3 times, see ``Retry.DEFAULT``. Pass a
        :class:`~urllib3.util.retry.Retry` object for fine-grained control
        over different types of retries.
        Pass an integer number to retry connection errors that many times,
        but no other types of errors. Pass zero to never retry.

        If ``False``, then retries are disabled and any exception is raised
        immediately. Also, instead of raising a MaxRetryError on redirects,
        the redirect response will be returned.

    :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

    :param timeout:
        If specified, overrides the default timeout for this one
        request. It may be a float (in seconds) or an instance of
        :class:`urllib3.util.Timeout`.

    :param json:
        Data to encode and send as JSON with UTF-encoded in the request body.
        The ``"Content-Type"`` header will be set to ``"application/json"``
        unless specified otherwise.
    """
    # 117           0 RESUME                   0
    # 193           2 LOAD_GLOBAL              0 (_DEFAULT_POOL)
    # 14 LOAD_METHOD              1 (request)
    # 194          36 LOAD_FAST                0 (method)
    # 195          38 LOAD_FAST                1 (url)
    # 196          40 LOAD_FAST                2 (body)
    # 197          42 LOAD_FAST                3 (fields)
    # 198          44 LOAD_FAST                4 (headers)
    # 199          46 LOAD_FAST                5 (preload_content)
    # 200          48 LOAD_FAST                6 (decode_content)
    # 201          50 LOAD_FAST                7 (redirect)
    # 202          52 LOAD_FAST                8 (retries)
    # 203          54 LOAD_FAST                9 (timeout)
    # 204          56 LOAD_FAST               10 (json)
    # 193          58 KW_NAMES                 1
    # 60 PRECALL                 11
    # 64 CALL                    11
    # 74 RETURN_VALUE
