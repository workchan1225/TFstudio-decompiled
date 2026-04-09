# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: httplib2\__init__.py

"""Small, fast HTTP client library for Python."""

import base64
import calendar
import copy
import email
import email.feedparser
from email import header
import email.message
import email.utils
import errno
from gettext import gettext
import gzip
from hashlib import md5
from hashlib import sha1
import hmac
import http.client
import io
import os
import random
import re
import socket
import ssl
import sys
import time
import urllib.parse
import zlib
import socks
from  import auth
import error
from iri2uri import iri2uri
from httplib2 import certs

def has_timeout(timeout):
    # 56           0 RESUME                   0
    # 57           2 LOAD_GLOBAL              1 (NULL + hasattr)
    # 14 LOAD_GLOBAL              2 (socket)
    # 26 LOAD_CONST               1 ('_GLOBAL_DEFAULT_TIMEOUT')
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE    18 (to 80)
    # 58          44 LOAD_FAST                0 (timeout)
    # 46 LOAD_CONST               0 (None)
    # 48 IS_OP                    1
    # 50 JUMP_IF_FALSE_OR_POP    13 (to 78)
    # 52 LOAD_FAST                0 (timeout)
    # 54 LOAD_GLOBAL              2 (socket)
    # 66 LOAD_ATTR                2 (_GLOBAL_DEFAULT_TIMEOUT)
    # 76 IS_OP                    1
    # >>   78 RETURN_VALUE
    # 59     >>   80 LOAD_FAST                0 (timeout)
    # 82 LOAD_CONST               0 (None)
    # 84 IS_OP                    1
    # 86 RETURN_VALUE

def _build_ssl_context(disable_ssl_certificate_validation, ca_certs, cert_file, key_file, maximum_version, minimum_version, key_password):
    # 140           0 RESUME                   0
    # 149           2 LOAD_GLOBAL              1 (NULL + hasattr)
    # 14 LOAD_GLOBAL              2 (ssl)
    # 26 LOAD_CONST               1 ('SSLContext')
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_TRUE    15 (to 74)
    # 150          44 LOAD_GLOBAL              5 (NULL + RuntimeError)
    # 56 LOAD_CONST               2 ('httplib2 requires Python 3.2+ for ssl.SSLContext')
    # 58 PRECALL                  1
    # 62 CALL                     1
    # 72 RAISE_VARARGS            1
    # 152     >>   74 LOAD_GLOBAL              3 (NULL + ssl)
    # 86 LOAD_ATTR                3 (SSLContext)
    # 96 LOAD_GLOBAL              8 (DEFAULT_TLS_VERSION)
    # 108 PRECALL                  1
    # 112 CALL                     1
    # 122 STORE_FAST               7 (context)
    # 155         124 LOAD_FAST                0 (disable_ssl_certificate_validation)
    # 126 POP_JUMP_FORWARD_IF_FALSE    24 (to 176)
    # 128 LOAD_GLOBAL              1 (NULL + hasattr)
    # 140 LOAD_FAST                7 (context)
    # 142 LOAD_CONST               3 ('check_hostname')
    # 144 PRECALL                  2
    # 148 CALL                     2
    # 158 POP_JUMP_FORWARD_IF_FALSE     8 (to 176)
    # 156         160 LOAD_FAST                0 (disable_ssl_certificate_validation)
    # 162 UNARY_NOT
    # 164 LOAD_FAST                7 (context)
    # 166 STORE_ATTR               5 (check_hostname)
    # 157     >>  176 LOAD_FAST                0 (disable_ssl_certificate_validation)
    # 178 POP_JUMP_FORWARD_IF_FALSE    12 (to 204)
    # 180 LOAD_GLOBAL              2 (ssl)
    # 192 LOAD_ATTR                6 (CERT_NONE)
    # 202 JUMP_FORWARD            11 (to 226)
    # >>  204 LOAD_GLOBAL              2 (ssl)
    # 216 LOAD_ATTR                7 (CERT_REQUIRED)
    # >>  226 LOAD_FAST                7 (context)
    # 228 STORE_ATTR               8 (verify_mode)
    # 161         238 LOAD_FAST                4 (maximum_version)
    # 240 POP_JUMP_FORWARD_IF_NONE    86 (to 414)
    # 162         242 LOAD_GLOBAL              1 (NULL + hasattr)
    # 254 LOAD_FAST                7 (context)
    # 256 LOAD_CONST               4 ('maximum_version')
    # 258 PRECALL                  2
    # 262 CALL                     2
    # 272 POP_JUMP_FORWARD_IF_FALSE    55 (to 384)
    # 163         274 LOAD_GLOBAL             19 (NULL + isinstance)
    # 286 LOAD_FAST                4 (maximum_version)
    # 288 LOAD_GLOBAL             20 (str)
    # 300 PRECALL                  2
    # 304 CALL                     2
    # 314 POP_JUMP_FORWARD_IF_FALSE    26 (to 368)
    # 164         316 LOAD_GLOBAL             23 (NULL + getattr)
    # 328 LOAD_GLOBAL              2 (ssl)
    # 340 LOAD_ATTR               12 (TLSVersion)
    # 350 LOAD_FAST                4 (maximum_version)
    # 352 PRECALL                  2
    # 356 CALL                     2
    # 366 STORE_FAST               4 (maximum_version)
    # 165     >>  368 LOAD_FAST                4 (maximum_version)
    # 370 LOAD_FAST                7 (context)
    # 372 STORE_ATTR              13 (maximum_version)
    # 382 JUMP_FORWARD            15 (to 414)
    # 167     >>  384 LOAD_GLOBAL              5 (NULL + RuntimeError)
    # 396 LOAD_CONST               5 ('setting tls_maximum_version requires Python 3.7 and OpenSSL 1.1 or newer')
    # 398 PRECALL                  1
    # 402 CALL                     1
    # 412 RAISE_VARARGS            1
    # 168     >>  414 LOAD_FAST                5 (minimum_version)
    # 416 POP_JUMP_FORWARD_IF_NONE    86 (to 590)
    # 169         418 LOAD_GLOBAL              1 (NULL + hasattr)
    # 430 LOAD_FAST                7 (context)
    # 432 LOAD_CONST               6 ('minimum_version')
    # 434 PRECALL                  2
    # 438 CALL                     2
    # 448 POP_JUMP_FORWARD_IF_FALSE    55 (to 560)
    # 170         450 LOAD_GLOBAL             19 (NULL + isinstance)
    # 462 LOAD_FAST                5 (minimum_version)
    # 464 LOAD_GLOBAL             20 (str)
    # 476 PRECALL                  2
    # 480 CALL                     2
    # 490 POP_JUMP_FORWARD_IF_FALSE    26 (to 544)
    # 171         492 LOAD_GLOBAL             23 (NULL + getattr)
    # 504 LOAD_GLOBAL              2 (ssl)
    # 516 LOAD_ATTR               12 (TLSVersion)
    # 526 LOAD_FAST                5 (minimum_version)
    # 528 PRECALL                  2
    # 532 CALL                     2
    # 542 STORE_FAST               5 (minimum_version)
    # 172     >>  544 LOAD_FAST                5 (minimum_version)
    # 546 LOAD_FAST                7 (context)
    # 548 STORE_ATTR              14 (minimum_version)
    # 558 JUMP_FORWARD            15 (to 590)
    # 174     >>  560 LOAD_GLOBAL              5 (NULL + RuntimeError)
    # 572 LOAD_CONST               7 ('setting tls_minimum_version requires Python 3.7 and OpenSSL 1.1 or newer')
    # 574 PRECALL                  1
    # 578 CALL                     1
    # 588 RAISE_VARARGS            1
    # 178     >>  590 LOAD_GLOBAL              1 (NULL + hasattr)
    # 602 LOAD_FAST                7 (context)
    # 604 LOAD_CONST               3 ('check_hostname')
    # 606 PRECALL                  2
    # 610 CALL                     2
    # 620 POP_JUMP_FORWARD_IF_FALSE     8 (to 638)
    # 179         622 LOAD_FAST                0 (disable_ssl_certificate_validation)
    # 624 UNARY_NOT
    # 626 LOAD_FAST                7 (context)
    # 628 STORE_ATTR               5 (check_hostname)
    # 181     >>  638 LOAD_FAST                0 (disable_ssl_certificate_validation)
    # 640 POP_JUMP_FORWARD_IF_TRUE    21 (to 684)
    # 182         642 LOAD_FAST                7 (context)
    # 644 LOAD_METHOD             15 (load_verify_locations)
    # 666 LOAD_FAST                1 (ca_certs)
    # 668 PRECALL                  1
    # 672 CALL                     1
    # 682 POP_TOP
    # 184     >>  684 LOAD_FAST                2 (cert_file)
    # 686 POP_JUMP_FORWARD_IF_FALSE    23 (to 734)
    # 185         688 LOAD_FAST                7 (context)
    # 690 LOAD_METHOD             16 (load_cert_chain)
    # 712 LOAD_FAST                2 (cert_file)
    # 714 LOAD_FAST                3 (key_file)
    # 716 LOAD_FAST                6 (key_password)
    # 718 PRECALL                  3
    # 722 CALL                     3
    # 732 POP_TOP
    # 187     >>  734 LOAD_FAST                7 (context)
    # 736 RETURN_VALUE

def _get_end2end_headers(response):
    # 0 MAKE_CELL                1 (hopbyhop)
    # 190           2 RESUME                   0
    # 191           4 LOAD_GLOBAL              1 (NULL + list)
    # 16 LOAD_GLOBAL              2 (HOP_BY_HOP)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 STORE_DEREF              1 (hopbyhop)
    # 192          44 LOAD_DEREF               1 (hopbyhop)
    # 46 LOAD_METHOD              2 (extend)
    # 68 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7E221F0, file "httplib2\__init__.py", line 192>)
    # 70 MAKE_FUNCTION            0
    # 72 LOAD_FAST                0 (response)
    # 74 LOAD_METHOD              3 (get)
    # 96 LOAD_CONST               2 ('connection')
    # 98 LOAD_CONST               3 ('')
    # 100 PRECALL                  2
    # 104 CALL                     2
    # 114 LOAD_METHOD              4 (split)
    # 136 LOAD_CONST               4 (',')
    # 138 PRECALL                  1
    # 142 CALL                     1
    # 152 GET_ITER
    # 154 PRECALL                  0
    # 158 CALL                     0
    # 168 PRECALL                  1
    # 172 CALL                     1
    # 182 POP_TOP
    # 193         184 LOAD_CLOSURE             1 (hopbyhop)
    # 186 BUILD_TUPLE              1
    # 188 LOAD_CONST               5 (<code object <listcomp> at 0x000001EBD7E34E30, file "httplib2\__init__.py", line 193>)
    # 190 MAKE_FUNCTION            8 (closure)
    # 192 LOAD_GLOBAL              1 (NULL + list)
    # 204 LOAD_FAST                0 (response)
    # 206 LOAD_METHOD              5 (keys)
    # 228 PRECALL                  0
    # 232 CALL                     0
    # 242 PRECALL                  1
    # 246 CALL                     1
    # 256 GET_ITER
    # 258 PRECALL                  0
    # 262 CALL                     0
    # 272 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E221F0, file "httplib2\__init__.py", line 192>:
    # 192           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                22 (to 52)
    # 8 STORE_FAST               1 (x)
    # 10 LOAD_FAST                1 (x)
    # 12 LOAD_METHOD              0 (strip)
    # 34 PRECALL                  0
    # 38 CALL                     0
    # 48 LIST_APPEND              2
    # 50 JUMP_BACKWARD           23 (to 6)
    # >>   52 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E34E30, file "httplib2\__init__.py", line 193>:
    # 0 COPY_FREE_VARS           1
    # 193           2 RESUME                   0
    # 4 BUILD_LIST               0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                 8 (to 26)
    # 10 STORE_FAST               1 (header)
    # 12 LOAD_FAST                1 (header)
    # 14 LOAD_DEREF               2 (hopbyhop)
    # 16 CONTAINS_OP              1
    # 18 POP_JUMP_BACKWARD_IF_FALSE     6 (to 8)
    # 20 LOAD_FAST                1 (header)
    # 22 LIST_APPEND              2
    # 24 JUMP_BACKWARD            9 (to 8)
    # >>   26 RETURN_VALUE

def _errno_from_exception(e):
    # 199           0 RESUME                   0
    # 201           2 LOAD_GLOBAL              1 (NULL + getattr)
    # 14 LOAD_FAST                0 (e)
    # 16 LOAD_CONST               1 ('errno')
    # 18 LOAD_GLOBAL              2 (_missing)
    # 30 PRECALL                  3
    # 34 CALL                     3
    # 44 STORE_FAST               1 (errno)
    # 202          46 LOAD_FAST                1 (errno)
    # 48 LOAD_GLOBAL              2 (_missing)
    # 60 IS_OP                    1
    # 62 POP_JUMP_FORWARD_IF_FALSE     2 (to 68)
    # 203          64 LOAD_FAST                1 (errno)
    # 66 RETURN_VALUE
    # 206     >>   68 LOAD_GLOBAL              1 (NULL + getattr)
    # 80 LOAD_FAST                0 (e)
    # 82 LOAD_CONST               2 ('args')
    # 84 LOAD_CONST               0 (None)
    # 86 PRECALL                  3
    # 90 CALL                     3
    # 100 STORE_FAST               2 (args)
    # 207         102 LOAD_FAST                2 (args)
    # 104 POP_JUMP_FORWARD_IF_FALSE    21 (to 148)
    # 208         106 LOAD_GLOBAL              5 (NULL + _errno_from_exception)
    # 118 LOAD_FAST                2 (args)
    # 120 LOAD_CONST               3 (0)
    # 122 BINARY_SUBSCR
    # 132 PRECALL                  1
    # 136 CALL                     1
    # 146 RETURN_VALUE
    # 212     >>  148 LOAD_GLOBAL              1 (NULL + getattr)
    # 160 LOAD_FAST                0 (e)
    # 162 LOAD_CONST               4 ('socket_err')
    # 164 LOAD_CONST               0 (None)
    # 166 PRECALL                  3
    # 170 CALL                     3
    # 180 STORE_FAST               3 (socket_err)
    # 213         182 LOAD_FAST                3 (socket_err)
    # 184 POP_JUMP_FORWARD_IF_FALSE    15 (to 216)
    # 214         186 LOAD_GLOBAL              5 (NULL + _errno_from_exception)
    # 198 LOAD_FAST                3 (socket_err)
    # 200 PRECALL                  1
    # 204 CALL                     1
    # 214 RETURN_VALUE
    # 216     >>  216 LOAD_CONST               0 (None)
    # 218 RETURN_VALUE

def parse_uri(uri):
    """Parses a URI using the regex given in Appendix B of RFC 3986.

        (scheme, authority, path, query, fragment) = parse_uri(uri)
    """
    # 222           0 RESUME                   0
    # 227           2 LOAD_GLOBAL              0 (URI)
    # 14 LOAD_METHOD              1 (match)
    # 36 LOAD_FAST                0 (uri)
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 LOAD_METHOD              2 (groups)
    # 74 PRECALL                  0
    # 78 CALL                     0
    # 88 STORE_FAST               1 (groups)
    # 228          90 LOAD_FAST                1 (groups)
    # 92 LOAD_CONST               1 (1)
    # 94 BINARY_SUBSCR
    # 104 LOAD_FAST                1 (groups)
    # 106 LOAD_CONST               2 (3)
    # 108 BINARY_SUBSCR
    # 118 LOAD_FAST                1 (groups)
    # 120 LOAD_CONST               3 (4)
    # 122 BINARY_SUBSCR
    # 132 LOAD_FAST                1 (groups)
    # 134 LOAD_CONST               4 (6)
    # 136 BINARY_SUBSCR
    # 146 LOAD_FAST                1 (groups)
    # 148 LOAD_CONST               5 (8)
    # 150 BINARY_SUBSCR
    # 160 BUILD_TUPLE              5
    # 162 RETURN_VALUE

def urlnorm(uri):
    # 231           0 RESUME                   0
    # 232           2 LOAD_GLOBAL              1 (NULL + parse_uri)
    # 14 LOAD_FAST                0 (uri)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 UNPACK_SEQUENCE          5
    # 34 STORE_FAST               1 (scheme)
    # 36 STORE_FAST               2 (authority)
    # 38 STORE_FAST               3 (path)
    # 40 STORE_FAST               4 (query)
    # 42 STORE_FAST               5 (fragment)
    # 233          44 LOAD_FAST                1 (scheme)
    # 46 POP_JUMP_FORWARD_IF_FALSE     2 (to 52)
    # 48 LOAD_FAST                2 (authority)
    # 50 POP_JUMP_FORWARD_IF_TRUE    18 (to 88)
    # 234     >>   52 LOAD_GLOBAL              3 (NULL + RelativeURIError)
    # 64 LOAD_CONST               1 ('Only absolute URIs are allowed. uri = %s')
    # 66 LOAD_FAST                0 (uri)
    # 68 BINARY_OP                6 (%)
    # 72 PRECALL                  1
    # 76 CALL                     1
    # 86 RAISE_VARARGS            1
    # 235     >>   88 LOAD_FAST                2 (authority)
    # 90 LOAD_METHOD              2 (lower)
    # 112 PRECALL                  0
    # 116 CALL                     0
    # 126 STORE_FAST               2 (authority)
    # 236         128 LOAD_FAST                1 (scheme)
    # 130 LOAD_METHOD              2 (lower)
    # 152 PRECALL                  0
    # 156 CALL                     0
    # 166 STORE_FAST               1 (scheme)
    # 237         168 LOAD_FAST                3 (path)
    # 170 POP_JUMP_FORWARD_IF_TRUE     2 (to 176)
    # 238         172 LOAD_CONST               2 ('/')
    # 174 STORE_FAST               3 (path)
    # 241     >>  176 LOAD_FAST                4 (query)
    # 178 POP_JUMP_FORWARD_IF_FALSE    23 (to 226)
    # 180 LOAD_CONST               3 ('?')
    # 182 LOAD_METHOD              3 (join)
    # 204 LOAD_FAST                3 (path)
    # 206 LOAD_FAST                4 (query)
    # 208 BUILD_LIST               2
    # 210 PRECALL                  1
    # 214 CALL                     1
    # 224 JUMP_IF_TRUE_OR_POP      1 (to 228)
    # >>  226 LOAD_FAST                3 (path)
    # >>  228 STORE_FAST               6 (request_uri)
    # 242         230 LOAD_FAST                1 (scheme)
    # 232 LOAD_METHOD              2 (lower)
    # 254 PRECALL                  0
    # 258 CALL                     0
    # 268 STORE_FAST               1 (scheme)
    # 243         270 LOAD_FAST                1 (scheme)
    # 272 LOAD_CONST               4 ('://')
    # 274 BINARY_OP                0 (+)
    # 278 LOAD_FAST                2 (authority)
    # 280 BINARY_OP                0 (+)
    # 284 LOAD_FAST                6 (request_uri)
    # 286 BINARY_OP                0 (+)
    # 290 STORE_FAST               7 (defrag_uri)
    # 244         292 LOAD_FAST                1 (scheme)
    # 294 LOAD_FAST                2 (authority)
    # 296 LOAD_FAST                6 (request_uri)
    # 298 LOAD_FAST                7 (defrag_uri)
    # 300 BUILD_TUPLE              4
    # 302 RETURN_VALUE

def safename(filename):
    """Return a filename suitable for the cache.
    Strips dangerous and common characters to create a filename we
    can use to store the cache in.
    """
    # 252           0 RESUME                   0
    # 257           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (filename)
    # 16 LOAD_GLOBAL              2 (bytes)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_FALSE    24 (to 92)
    # 258          44 LOAD_FAST                0 (filename)
    # 46 STORE_FAST               1 (filename_bytes)
    # 259          48 LOAD_FAST                0 (filename)
    # 50 LOAD_METHOD              2 (decode)
    # 72 LOAD_CONST               1 ('utf-8')
    # 74 PRECALL                  1
    # 78 CALL                     1
    # 88 STORE_FAST               0 (filename)
    # 90 JUMP_FORWARD            21 (to 134)
    # 261     >>   92 LOAD_FAST                0 (filename)
    # 94 LOAD_METHOD              3 (encode)
    # 116 LOAD_CONST               1 ('utf-8')
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 STORE_FAST               1 (filename_bytes)
    # 262     >>  134 LOAD_GLOBAL              9 (NULL + _md5)
    # 146 LOAD_FAST                1 (filename_bytes)
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 LOAD_METHOD              5 (hexdigest)
    # 184 PRECALL                  0
    # 188 CALL                     0
    # 198 STORE_FAST               2 (filemd5)
    # 263         200 LOAD_GLOBAL             12 (re_url_scheme)
    # 212 LOAD_METHOD              7 (sub)
    # 234 LOAD_CONST               2 ('')
    # 236 LOAD_FAST                0 (filename)
    # 238 PRECALL                  2
    # 242 CALL                     2
    # 252 STORE_FAST               0 (filename)
    # 264         254 LOAD_GLOBAL             16 (re_unsafe)
    # 266 LOAD_METHOD              7 (sub)
    # 288 LOAD_CONST               2 ('')
    # 290 LOAD_FAST                0 (filename)
    # 292 PRECALL                  2
    # 296 CALL                     2
    # 306 STORE_FAST               0 (filename)
    # 271         308 LOAD_FAST                0 (filename)
    # 310 LOAD_CONST               3 (None)
    # 312 LOAD_CONST               4 (90)
    # 314 BUILD_SLICE              2
    # 316 BINARY_SUBSCR
    # 326 STORE_FAST               0 (filename)
    # 273         328 LOAD_CONST               5 (',')
    # 330 LOAD_METHOD              9 (join)
    # 352 LOAD_FAST                0 (filename)
    # 354 LOAD_FAST                2 (filemd5)
    # 356 BUILD_TUPLE              2
    # 358 PRECALL                  1
    # 362 CALL                     1
    # 372 RETURN_VALUE

def _normalize_headers(headers):
    # 279           0 RESUME                   0
    # 280           2 LOAD_GLOBAL              1 (NULL + dict)
    # 281          14 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD716FB90, file "httplib2\__init__.py", line 281>)
    # 16 MAKE_FUNCTION            0
    # 283          18 LOAD_FAST                0 (headers)
    # 20 LOAD_METHOD              1 (items)
    # 42 PRECALL                  0
    # 46 CALL                     0
    # 281          56 GET_ITER
    # 58 PRECALL                  0
    # 62 CALL                     0
    # 280          72 PRECALL                  1
    # 76 CALL                     1
    # 86 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD716FB90, file "httplib2\__init__.py", line 281>:
    # 281           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                96 (to 200)
    # 283           8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (key)
    # 14 STORE_FAST               2 (value)
    # 282          16 LOAD_GLOBAL              1 (NULL + _convert_byte_str)
    # 28 LOAD_FAST                1 (key)
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 LOAD_METHOD              1 (lower)
    # 66 PRECALL                  0
    # 70 CALL                     0
    # 80 LOAD_GLOBAL              4 (NORMALIZE_SPACE)
    # 92 LOAD_METHOD              3 (sub)
    # 114 LOAD_GLOBAL              1 (NULL + _convert_byte_str)
    # 126 LOAD_FAST                2 (value)
    # 128 PRECALL                  1
    # 132 CALL                     1
    # 142 LOAD_CONST               0 (' ')
    # 144 PRECALL                  2
    # 148 CALL                     2
    # 158 LOAD_METHOD              4 (strip)
    # 180 PRECALL                  0
    # 184 CALL                     0
    # 194 BUILD_TUPLE              2
    # 281         196 LIST_APPEND              2
    # 198 JUMP_BACKWARD           97 (to 6)
    # >>  200 RETURN_VALUE

def _convert_byte_str(s):
    # 288           0 RESUME                   0
    # 289           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (s)
    # 16 LOAD_GLOBAL              2 (str)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_JUMP_FORWARD_IF_TRUE    16 (to 76)
    # 290          44 LOAD_GLOBAL              3 (NULL + str)
    # 56 LOAD_FAST                0 (s)
    # 58 LOAD_CONST               1 ('utf-8')
    # 60 PRECALL                  2
    # 64 CALL                     2
    # 74 RETURN_VALUE
    # 291     >>   76 LOAD_FAST                0 (s)
    # 78 RETURN_VALUE

def _parse_cache_control(headers):
    # 294           0 RESUME                   0
    # 295           2 BUILD_MAP                0
    # 4 STORE_FAST               1 (retval)
    # 296           6 LOAD_CONST               1 ('cache-control')
    # 8 LOAD_FAST                0 (headers)
    # 10 CONTAINS_OP              0
    # 12 POP_JUMP_FORWARD_IF_FALSE    69 (to 152)
    # 297          14 LOAD_FAST                0 (headers)
    # 16 LOAD_CONST               1 ('cache-control')
    # 18 BINARY_SUBSCR
    # 28 LOAD_METHOD              0 (split)
    # 50 LOAD_CONST               2 (',')
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               2 (parts)
    # 298          68 LOAD_CONST               3 (<code object <listcomp> at 0x000001EBD72CB730, file "httplib2\__init__.py", line 298>)
    # 70 MAKE_FUNCTION            0
    # 299          72 LOAD_FAST                2 (parts)
    # 298          74 GET_ITER
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 STORE_FAST               3 (parts_with_args)
    # 301          92 LOAD_CONST               4 (<code object <listcomp> at 0x000001EBD7183C90, file "httplib2\__init__.py", line 301>)
    # 94 MAKE_FUNCTION            0
    # 96 LOAD_FAST                2 (parts)
    # 98 GET_ITER
    # 100 PRECALL                  0
    # 104 CALL                     0
    # 114 STORE_FAST               4 (parts_wo_args)
    # 302         116 LOAD_GLOBAL              3 (NULL + dict)
    # 128 LOAD_FAST                3 (parts_with_args)
    # 130 LOAD_FAST                4 (parts_wo_args)
    # 132 BINARY_OP                0 (+)
    # 136 PRECALL                  1
    # 140 CALL                     1
    # 150 STORE_FAST               1 (retval)
    # 303     >>  152 LOAD_FAST                1 (retval)
    # 154 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD72CB730, file "httplib2\__init__.py", line 298>:
    # 298           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                72 (to 152)
    # 299           8 STORE_FAST               1 (part)
    # 10 LOAD_CONST               0 (-1)
    # 12 LOAD_FAST                1 (part)
    # 14 LOAD_METHOD              0 (find)
    # 36 LOAD_CONST               1 ('=')
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 COMPARE_OP               3 (!=)
    # 58 POP_JUMP_BACKWARD_IF_FALSE    27 (to 6)
    # 60 LOAD_GLOBAL              3 (NULL + tuple)
    # 72 LOAD_CONST               2 (<code object <listcomp> at 0x000001EBD7E0B1B0, file "httplib2\__init__.py", line 299>)
    # 74 MAKE_FUNCTION            0
    # 76 LOAD_FAST                1 (part)
    # 78 LOAD_METHOD              2 (split)
    # 100 LOAD_CONST               1 ('=')
    # 102 LOAD_CONST               3 (1)
    # 104 PRECALL                  2
    # 108 CALL                     2
    # 118 GET_ITER
    # 120 PRECALL                  0
    # 124 CALL                     0
    # 134 PRECALL                  1
    # 138 CALL                     1
    # 148 LIST_APPEND              2
    # 150 JUMP_BACKWARD           73 (to 6)
    # >>  152 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E0B1B0, file "httplib2\__init__.py", line 299>:
    # 299           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                40 (to 88)
    # 8 STORE_FAST               1 (x)
    # 10 LOAD_FAST                1 (x)
    # 12 LOAD_METHOD              0 (strip)
    # 34 PRECALL                  0
    # 38 CALL                     0
    # 48 LOAD_METHOD              1 (lower)
    # 70 PRECALL                  0
    # 74 CALL                     0
    # 84 LIST_APPEND              2
    # 86 JUMP_BACKWARD           41 (to 6)
    # >>   88 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7183C90, file "httplib2\__init__.py", line 301>:
    # 301           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                67 (to 142)
    # 8 STORE_FAST               1 (name)
    # 10 LOAD_CONST               0 (-1)
    # 12 LOAD_FAST                1 (name)
    # 14 LOAD_METHOD              0 (find)
    # 36 LOAD_CONST               1 ('=')
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 COMPARE_OP               2 (==)
    # 58 POP_JUMP_BACKWARD_IF_FALSE    27 (to 6)
    # 60 LOAD_FAST                1 (name)
    # 62 LOAD_METHOD              1 (strip)
    # 84 PRECALL                  0
    # 88 CALL                     0
    # 98 LOAD_METHOD              2 (lower)
    # 120 PRECALL                  0
    # 124 CALL                     0
    # 134 LOAD_CONST               2 (1)
    # 136 BUILD_TUPLE              2
    # 138 LIST_APPEND              2
    # 140 JUMP_BACKWARD           68 (to 6)
    # >>  142 RETURN_VALUE

def _entry_disposition(response_headers, request_headers):
    """Determine freshness from the Date, Expires and Cache-Control headers.

    We don't handle the following:

    1. Cache-Control: max-stale
    2. Age: headers are not used in the calculations.

    Not that this algorithm is simpler than you might think
    because we are operating as a private (non-shared) cache.
    This lets us ignore 's-maxage'. We can also ignore
    'proxy-invalidate' since we aren't a proxy.
    We will never return a stale document as
    fresh as a design decision, and thus the non-implementation
    of 'max-stale'. This also lets us safely ignore 'must-revalidate'
    since we operate as if every server has sent 'must-revalidate'.
    Since we are private we get to ignore both 'public' and
    'private' parameters. We also ignore 'no-transform' since
    we don't do any transformations.
    The 'no-store' parameter is handled at a higher level.
    So the only Cache-Control parameters we look at are:

    no-cache
    only-if-cached
    max-age
    min-fresh
    """
    # 313           0 RESUME                   0
    # 341           2 LOAD_CONST               1 ('STALE')
    # 4 STORE_FAST               2 (retval)
    # 342           6 LOAD_GLOBAL              1 (NULL + _parse_cache_control)
    # 18 LOAD_FAST                1 (request_headers)
    # 20 PRECALL                  1
    # 24 CALL                     1
    # 34 STORE_FAST               3 (cc)
    # 343          36 LOAD_GLOBAL              1 (NULL + _parse_cache_control)
    # 48 LOAD_FAST                0 (response_headers)
    # 50 PRECALL                  1
    # 54 CALL                     1
    # 64 STORE_FAST               4 (cc_response)
    # 345          66 LOAD_CONST               2 ('pragma')
    # 68 LOAD_FAST                1 (request_headers)
    # 70 CONTAINS_OP              0
    # 72 POP_JUMP_FORWARD_IF_FALSE    62 (to 198)
    # 74 LOAD_FAST                1 (request_headers)
    # 76 LOAD_CONST               2 ('pragma')
    # 78 BINARY_SUBSCR
    # 88 LOAD_METHOD              1 (lower)
    # 110 PRECALL                  0
    # 114 CALL                     0
    # 124 LOAD_METHOD              2 (find)
    # 146 LOAD_CONST               3 ('no-cache')
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 LOAD_CONST               4 (-1)
    # 164 COMPARE_OP               3 (!=)
    # 170 POP_JUMP_FORWARD_IF_FALSE    13 (to 198)
    # 346         172 LOAD_CONST               5 ('TRANSPARENT')
    # 174 STORE_FAST               2 (retval)
    # 347         176 LOAD_CONST               6 ('cache-control')
    # 178 LOAD_FAST                1 (request_headers)
    # 180 CONTAINS_OP              1
    # 182 POP_JUMP_FORWARD_IF_FALSE     5 (to 194)
    # 348         184 LOAD_CONST               3 ('no-cache')
    # 186 LOAD_FAST                1 (request_headers)
    # 188 LOAD_CONST               6 ('cache-control')
    # 190 STORE_SUBSCR
    # >>  194 EXTENDED_ARG             1
    # 196 JUMP_FORWARD           360 (to 918)
    # 349     >>  198 LOAD_CONST               3 ('no-cache')
    # 200 LOAD_FAST                3 (cc)
    # 202 CONTAINS_OP              0
    # 204 POP_JUMP_FORWARD_IF_FALSE     4 (to 214)
    # 350         206 LOAD_CONST               5 ('TRANSPARENT')
    # 208 STORE_FAST               2 (retval)
    # 210 EXTENDED_ARG             1
    # 212 JUMP_FORWARD           352 (to 918)
    # 351     >>  214 LOAD_CONST               3 ('no-cache')
    # 216 LOAD_FAST                4 (cc_response)
    # 218 CONTAINS_OP              0
    # 220 POP_JUMP_FORWARD_IF_FALSE     4 (to 230)
    # 352         222 LOAD_CONST               1 ('STALE')
    # 224 STORE_FAST               2 (retval)
    # 226 EXTENDED_ARG             1
    # 228 JUMP_FORWARD           344 (to 918)
    # 353     >>  230 LOAD_CONST               7 ('only-if-cached')
    # 232 LOAD_FAST                3 (cc)
    # 234 CONTAINS_OP              0
    # 236 POP_JUMP_FORWARD_IF_FALSE     4 (to 246)
    # 354         238 LOAD_CONST               8 ('FRESH')
    # 240 STORE_FAST               2 (retval)
    # 242 EXTENDED_ARG             1
    # 244 JUMP_FORWARD           336 (to 918)
    # 355     >>  246 LOAD_CONST               9 ('date')
    # 248 LOAD_FAST                0 (response_headers)
    # 250 CONTAINS_OP              0
    # 252 EXTENDED_ARG             1
    # 254 POP_JUMP_FORWARD_IF_FALSE   331 (to 918)
    # 356         256 LOAD_GLOBAL              7 (NULL + calendar)
    # 268 LOAD_ATTR                4 (timegm)
    # 278 LOAD_GLOBAL             10 (email)
    # 290 LOAD_ATTR                6 (utils)
    # 300 LOAD_METHOD              7 (parsedate_tz)
    # 322 LOAD_FAST                0 (response_headers)
    # 324 LOAD_CONST               9 ('date')
    # 326 BINARY_SUBSCR
    # 336 PRECALL                  1
    # 340 CALL                     1
    # 350 PRECALL                  1
    # 354 CALL                     1
    # 364 STORE_FAST               5 (date)
    # 357         366 LOAD_GLOBAL             17 (NULL + time)
    # 378 LOAD_ATTR                8 (time)
    # 388 PRECALL                  0
    # 392 CALL                     0
    # 402 STORE_FAST               6 (now)
    # 358         404 LOAD_GLOBAL             19 (NULL + max)
    # 416 LOAD_CONST              10 (0)
    # 418 LOAD_FAST                6 (now)
    # 420 LOAD_FAST                5 (date)
    # 422 BINARY_OP               10 (-)
    # 426 PRECALL                  2
    # 430 CALL                     2
    # 440 STORE_FAST               7 (current_age)
    # 359         442 LOAD_CONST              11 ('max-age')
    # 444 LOAD_FAST                4 (cc_response)
    # 446 CONTAINS_OP              0
    # 448 POP_JUMP_FORWARD_IF_FALSE    41 (to 532)
    # 360         450 NOP
    # 361         452 LOAD_GLOBAL             21 (NULL + int)
    # 464 LOAD_FAST                4 (cc_response)
    # 466 LOAD_CONST              11 ('max-age')
    # 468 BINARY_SUBSCR
    # 478 PRECALL                  1
    # 482 CALL                     1
    # 492 STORE_FAST               8 (freshness_lifetime)
    # 494 JUMP_FORWARD           108 (to 712)
    # >>  496 PUSH_EXC_INFO
    # 362         498 LOAD_GLOBAL             22 (ValueError)
    # 510 CHECK_EXC_MATCH
    # 512 POP_JUMP_FORWARD_IF_FALSE     5 (to 524)
    # 514 POP_TOP
    # 363         516 LOAD_CONST              10 (0)
    # 518 STORE_FAST               8 (freshness_lifetime)
    # 520 POP_EXCEPT
    # 522 JUMP_FORWARD            94 (to 712)
    # 362     >>  524 RERAISE                  0
    # >>  526 COPY                     3
    # 528 POP_EXCEPT
    # 530 RERAISE                  1
    # 364     >>  532 LOAD_CONST              12 ('expires')
    # 534 LOAD_FAST                0 (response_headers)
    # 536 CONTAINS_OP              0
    # 538 POP_JUMP_FORWARD_IF_FALSE    84 (to 708)
    # 365         540 LOAD_GLOBAL             10 (email)
    # 552 LOAD_ATTR                6 (utils)
    # 562 LOAD_METHOD              7 (parsedate_tz)
    # 584 LOAD_FAST                0 (response_headers)
    # 586 LOAD_CONST              12 ('expires')
    # 588 BINARY_SUBSCR
    # 598 PRECALL                  1
    # 602 CALL                     1
    # 612 STORE_FAST               9 (expires)
    # 366         614 LOAD_CONST              13 (None)
    # 616 LOAD_FAST                9 (expires)
    # 618 COMPARE_OP               2 (==)
    # 624 POP_JUMP_FORWARD_IF_FALSE     3 (to 632)
    # 367         626 LOAD_CONST              10 (0)
    # 628 STORE_FAST               8 (freshness_lifetime)
    # 630 JUMP_FORWARD            40 (to 712)
    # 369     >>  632 LOAD_GLOBAL             19 (NULL + max)
    # 644 LOAD_CONST              10 (0)
    # 646 LOAD_GLOBAL              7 (NULL + calendar)
    # 658 LOAD_ATTR                4 (timegm)
    # 668 LOAD_FAST                9 (expires)
    # 670 PRECALL                  1
    # 674 CALL                     1
    # 684 LOAD_FAST                5 (date)
    # 686 BINARY_OP               10 (-)
    # 690 PRECALL                  2
    # 694 CALL                     2
    # 704 STORE_FAST               8 (freshness_lifetime)
    # 706 JUMP_FORWARD             2 (to 712)
    # 371     >>  708 LOAD_CONST              10 (0)
    # 710 STORE_FAST               8 (freshness_lifetime)
    # 372     >>  712 LOAD_CONST              11 ('max-age')
    # 714 LOAD_FAST                3 (cc)
    # 716 CONTAINS_OP              0
    # 718 POP_JUMP_FORWARD_IF_FALSE    41 (to 802)
    # 373         720 NOP
    # 374         722 LOAD_GLOBAL             21 (NULL + int)
    # 734 LOAD_FAST                3 (cc)
    # 736 LOAD_CONST              11 ('max-age')
    # 738 BINARY_SUBSCR
    # 748 PRECALL                  1
    # 752 CALL                     1
    # 762 STORE_FAST               8 (freshness_lifetime)
    # 764 JUMP_FORWARD            18 (to 802)
    # >>  766 PUSH_EXC_INFO
    # 375         768 LOAD_GLOBAL             22 (ValueError)
    # 780 CHECK_EXC_MATCH
    # 782 POP_JUMP_FORWARD_IF_FALSE     5 (to 794)
    # 784 POP_TOP
    # 376         786 LOAD_CONST              10 (0)
    # 788 STORE_FAST               8 (freshness_lifetime)
    # 790 POP_EXCEPT
    # 792 JUMP_FORWARD             4 (to 802)
    # 375     >>  794 RERAISE                  0
    # >>  796 COPY                     3
    # 798 POP_EXCEPT
    # 800 RERAISE                  1
    # 377     >>  802 LOAD_CONST              14 ('min-fresh')
    # 804 LOAD_FAST                3 (cc)
    # 806 CONTAINS_OP              0
    # 808 POP_JUMP_FORWARD_IF_FALSE    46 (to 902)
    # 378         810 NOP
    # 379         812 LOAD_GLOBAL             21 (NULL + int)
    # 824 LOAD_FAST                3 (cc)
    # 826 LOAD_CONST              14 ('min-fresh')
    # 828 BINARY_SUBSCR
    # 838 PRECALL                  1
    # 842 CALL                     1
    # 852 STORE_FAST              10 (min_fresh)
    # 854 JUMP_FORWARD            18 (to 892)
    # >>  856 PUSH_EXC_INFO
    # 380         858 LOAD_GLOBAL             22 (ValueError)
    # 870 CHECK_EXC_MATCH
    # 872 POP_JUMP_FORWARD_IF_FALSE     5 (to 884)
    # 874 POP_TOP
    # 381         876 LOAD_CONST              10 (0)
    # 878 STORE_FAST              10 (min_fresh)
    # 880 POP_EXCEPT
    # 882 JUMP_FORWARD             4 (to 892)
    # 380     >>  884 RERAISE                  0
    # >>  886 COPY                     3
    # 888 POP_EXCEPT
    # 890 RERAISE                  1
    # 382     >>  892 LOAD_FAST                7 (current_age)
    # 894 LOAD_FAST               10 (min_fresh)
    # 896 BINARY_OP               13 (+=)
    # 900 STORE_FAST               7 (current_age)
    # 383     >>  902 LOAD_FAST                8 (freshness_lifetime)
    # 904 LOAD_FAST                7 (current_age)
    # 906 COMPARE_OP               4 (>)
    # 912 POP_JUMP_FORWARD_IF_FALSE     2 (to 918)
    # 384         914 LOAD_CONST               8 ('FRESH')
    # 916 STORE_FAST               2 (retval)
    # 385     >>  918 LOAD_FAST                2 (retval)
    # 920 RETURN_VALUE
    # ExceptionTable:
    # 452 to 492 -> 496 [0]
    # 496 to 518 -> 526 [1] lasti
    # 524 to 524 -> 526 [1] lasti
    # 722 to 762 -> 766 [0]
    # 766 to 788 -> 796 [1] lasti
    # 794 to 794 -> 796 [1] lasti
    # 812 to 852 -> 856 [0]
    # 856 to 878 -> 886 [1] lasti
    # 884 to 884 -> 886 [1] lasti

def _decompressContent(response, new_content):
    # 388           0 RESUME                   0
    # 389           2 LOAD_FAST                1 (new_content)
    # 4 STORE_FAST               2 (content)
    # 390           6 NOP
    # 391           8 LOAD_FAST                0 (response)
    # 10 LOAD_METHOD              0 (get)
    # 32 LOAD_CONST               1 ('content-encoding')
    # 34 LOAD_CONST               0 (None)
    # 36 PRECALL                  2
    # 40 CALL                     2
    # 50 STORE_FAST               3 (encoding)
    # 392          52 LOAD_FAST                3 (encoding)
    # 54 LOAD_CONST               2 (('gzip', 'deflate'))
    # 56 CONTAINS_OP              0
    # 58 POP_JUMP_FORWARD_IF_FALSE   207 (to 474)
    # 393          60 LOAD_FAST                3 (encoding)
    # 62 LOAD_CONST               3 ('gzip')
    # 64 COMPARE_OP               2 (==)
    # 70 POP_JUMP_FORWARD_IF_FALSE    57 (to 186)
    # 394          72 LOAD_GLOBAL              3 (NULL + gzip)
    # 84 LOAD_ATTR                2 (GzipFile)
    # 94 LOAD_GLOBAL              7 (NULL + io)
    # 106 LOAD_ATTR                4 (BytesIO)
    # 116 LOAD_FAST                1 (new_content)
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 KW_NAMES                 4
    # 134 PRECALL                  1
    # 138 CALL                     1
    # 148 LOAD_METHOD              5 (read)
    # 170 PRECALL                  0
    # 174 CALL                     0
    # 184 STORE_FAST               2 (content)
    # 395     >>  186 LOAD_FAST                3 (encoding)
    # 188 LOAD_CONST               5 ('deflate')
    # 190 COMPARE_OP               2 (==)
    # 196 POP_JUMP_FORWARD_IF_FALSE    93 (to 384)
    # 396         198 NOP
    # 397         200 LOAD_GLOBAL             13 (NULL + zlib)
    # 212 LOAD_ATTR                7 (decompress)
    # 222 LOAD_FAST                2 (content)
    # 224 LOAD_GLOBAL             12 (zlib)
    # 236 LOAD_ATTR                8 (MAX_WBITS)
    # 246 PRECALL                  2
    # 250 CALL                     2
    # 260 STORE_FAST               2 (content)
    # 262 JUMP_FORWARD            60 (to 384)
    # >>  264 PUSH_EXC_INFO
    # 398         266 LOAD_GLOBAL             18 (IOError)
    # 278 LOAD_GLOBAL             12 (zlib)
    # 290 LOAD_ATTR               10 (error)
    # 300 BUILD_TUPLE              2
    # 302 CHECK_EXC_MATCH
    # 304 POP_JUMP_FORWARD_IF_FALSE    35 (to 376)
    # 306 POP_TOP
    # 399         308 LOAD_GLOBAL             13 (NULL + zlib)
    # 320 LOAD_ATTR                7 (decompress)
    # 330 LOAD_FAST                2 (content)
    # 332 LOAD_GLOBAL             12 (zlib)
    # 344 LOAD_ATTR                8 (MAX_WBITS)
    # 354 UNARY_NEGATIVE
    # 356 PRECALL                  2
    # 360 CALL                     2
    # 370 STORE_FAST               2 (content)
    # 372 POP_EXCEPT
    # 374 JUMP_FORWARD             4 (to 384)
    # 398     >>  376 RERAISE                  0
    # >>  378 COPY                     3
    # 380 POP_EXCEPT
    # 382 RERAISE                  1
    # 400     >>  384 LOAD_GLOBAL             23 (NULL + str)
    # 396 LOAD_GLOBAL             25 (NULL + len)
    # 408 LOAD_FAST                2 (content)
    # 410 PRECALL                  1
    # 414 CALL                     1
    # 424 PRECALL                  1
    # 428 CALL                     1
    # 438 LOAD_FAST                0 (response)
    # 440 LOAD_CONST               6 ('content-length')
    # 442 STORE_SUBSCR
    # 402         446 LOAD_FAST                0 (response)
    # 448 LOAD_CONST               1 ('content-encoding')
    # 450 BINARY_SUBSCR
    # 460 LOAD_FAST                0 (response)
    # 462 LOAD_CONST               7 ('-content-encoding')
    # 464 STORE_SUBSCR
    # 403         468 LOAD_FAST                0 (response)
    # 470 LOAD_CONST               1 ('content-encoding')
    # 472 DELETE_SUBSCR
    # >>  474 JUMP_FORWARD            80 (to 636)
    # >>  476 PUSH_EXC_INFO
    # 404         478 LOAD_GLOBAL             18 (IOError)
    # 490 LOAD_GLOBAL             12 (zlib)
    # 502 LOAD_ATTR               10 (error)
    # 512 BUILD_TUPLE              2
    # 514 CHECK_EXC_MATCH
    # 516 POP_JUMP_FORWARD_IF_FALSE    55 (to 628)
    # 518 POP_TOP
    # 405         520 LOAD_CONST               8 ('')
    # 522 STORE_FAST               2 (content)
    # 406         524 LOAD_GLOBAL             27 (NULL + FailedToDecompressContent)
    # 407         536 LOAD_GLOBAL             29 (NULL + _)
    # 548 LOAD_CONST               9 ('Content purported to be compressed with %s but failed to decompress.')
    # 550 PRECALL                  1
    # 554 CALL                     1
    # 564 LOAD_FAST                0 (response)
    # 566 LOAD_METHOD              0 (get)
    # 588 LOAD_CONST               1 ('content-encoding')
    # 590 PRECALL                  1
    # 594 CALL                     1
    # 604 BINARY_OP                6 (%)
    # 408         608 LOAD_FAST                0 (response)
    # 409         610 LOAD_FAST                2 (content)
    # 406         612 PRECALL                  3
    # 616 CALL                     3
    # 626 RAISE_VARARGS            1
    # 404     >>  628 RERAISE                  0
    # >>  630 COPY                     3
    # 632 POP_EXCEPT
    # 634 RERAISE                  1
    # 411     >>  636 LOAD_FAST                2 (content)
    # 638 RETURN_VALUE
    # ExceptionTable:
    # 8 to 196 -> 476 [0]
    # 200 to 260 -> 264 [0]
    # 262 to 262 -> 476 [0]
    # 264 to 370 -> 378 [1] lasti
    # 372 to 374 -> 476 [0]
    # 376 to 376 -> 378 [1] lasti
    # 378 to 472 -> 476 [0]
    # 476 to 628 -> 630 [1] lasti

def _bind_write_headers(msg):
    # 0 MAKE_CELL                0 (msg)
    # 414           2 RESUME                   0
    # 415           4 LOAD_CLOSURE             0 (msg)
    # 6 BUILD_TUPLE              1
    # 8 LOAD_CONST               1 (<code object _write_headers at 0x000001EBD7596180, file "httplib2\__init__.py", line 415>)
    # 10 MAKE_FUNCTION            8 (closure)
    # 12 STORE_FAST               1 (_write_headers)
    # 428          14 LOAD_FAST                1 (_write_headers)
    # 16 RETURN_VALUE
    # Disassembly of <code object _write_headers at 0x000001EBD7596180, file "httplib2\__init__.py", line 415>:
    # 0 COPY_FREE_VARS           1
    # 415           2 RESUME                   0
    # 417           4 LOAD_DEREF               4 (msg)
    # 6 LOAD_METHOD              0 (items)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 GET_ITER
    # >>   44 FOR_ITER               174 (to 394)
    # 46 UNPACK_SEQUENCE          2
    # 50 STORE_FAST               1 (h)
    # 52 STORE_FAST               2 (v)
    # 418          54 LOAD_GLOBAL              3 (NULL + print)
    # 66 LOAD_CONST               1 ('%s:')
    # 68 LOAD_FAST                1 (h)
    # 70 BINARY_OP                6 (%)
    # 74 LOAD_CONST               2 (' ')
    # 76 LOAD_FAST                0 (self)
    # 78 LOAD_ATTR                2 (_fp)
    # 88 KW_NAMES                 3
    # 90 PRECALL                  3
    # 94 CALL                     3
    # 104 POP_TOP
    # 419         106 LOAD_GLOBAL              7 (NULL + isinstance)
    # 118 LOAD_FAST                2 (v)
    # 120 LOAD_GLOBAL              8 (header)
    # 132 LOAD_ATTR                5 (Header)
    # 142 PRECALL                  2
    # 146 CALL                     2
    # 156 POP_JUMP_FORWARD_IF_FALSE    48 (to 254)
    # 420         158 LOAD_GLOBAL              3 (NULL + print)
    # 170 LOAD_FAST                2 (v)
    # 172 LOAD_METHOD              6 (encode)
    # 194 LOAD_FAST                0 (self)
    # 196 LOAD_ATTR                7 (_maxheaderlen)
    # 206 KW_NAMES                 4
    # 208 PRECALL                  1
    # 212 CALL                     1
    # 222 LOAD_FAST                0 (self)
    # 224 LOAD_ATTR                2 (_fp)
    # 234 KW_NAMES                 5
    # 236 PRECALL                  2
    # 240 CALL                     2
    # 250 POP_TOP
    # 252 JUMP_BACKWARD          105 (to 44)
    # 423     >>  254 LOAD_GLOBAL              9 (NULL + header)
    # 266 LOAD_ATTR                5 (Header)
    # 276 LOAD_FAST                2 (v)
    # 278 LOAD_FAST                0 (self)
    # 280 LOAD_ATTR                7 (_maxheaderlen)
    # 290 LOAD_CONST               6 ('utf-8')
    # 292 LOAD_FAST                1 (h)
    # 294 KW_NAMES                 7
    # 296 PRECALL                  4
    # 300 CALL                     4
    # 310 STORE_FAST               3 (headers)
    # 424         312 LOAD_GLOBAL              3 (NULL + print)
    # 324 LOAD_FAST                3 (headers)
    # 326 LOAD_METHOD              6 (encode)
    # 348 PRECALL                  0
    # 352 CALL                     0
    # 362 LOAD_FAST                0 (self)
    # 364 LOAD_ATTR                2 (_fp)
    # 374 KW_NAMES                 5
    # 376 PRECALL                  2
    # 380 CALL                     2
    # 390 POP_TOP
    # 392 JUMP_BACKWARD          175 (to 44)
    # 426     >>  394 LOAD_GLOBAL              3 (NULL + print)
    # 406 LOAD_FAST                0 (self)
    # 408 LOAD_ATTR                2 (_fp)
    # 418 KW_NAMES                 5
    # 420 PRECALL                  1
    # 424 CALL                     1
    # 434 POP_TOP
    # 436 LOAD_CONST               0 (None)
    # 438 RETURN_VALUE

def _updateCache(request_headers, response_headers, content, cache, cachekey):
    # 431           0 RESUME                   0
    # 432           2 LOAD_FAST                4 (cachekey)
    # 4 EXTENDED_ARG             1
    # 6 POP_JUMP_FORWARD_IF_FALSE   463 (to 934)
    # 433           8 LOAD_GLOBAL              1 (NULL + _parse_cache_control)
    # 20 LOAD_FAST                0 (request_headers)
    # 22 PRECALL                  1
    # 26 CALL                     1
    # 36 STORE_FAST               5 (cc)
    # 434          38 LOAD_GLOBAL              1 (NULL + _parse_cache_control)
    # 50 LOAD_FAST                1 (response_headers)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               6 (cc_response)
    # 435          68 LOAD_CONST               1 ('no-store')
    # 70 LOAD_FAST                5 (cc)
    # 72 CONTAINS_OP              0
    # 74 POP_JUMP_FORWARD_IF_TRUE     4 (to 84)
    # 76 LOAD_CONST               1 ('no-store')
    # 78 LOAD_FAST                6 (cc_response)
    # 80 CONTAINS_OP              0
    # 82 POP_JUMP_FORWARD_IF_FALSE    23 (to 130)
    # 436     >>   84 LOAD_FAST                3 (cache)
    # 86 LOAD_METHOD              1 (delete)
    # 108 LOAD_FAST                4 (cachekey)
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 POP_TOP
    # 126 LOAD_CONST               0 (None)
    # 128 RETURN_VALUE
    # 438     >>  130 LOAD_GLOBAL              4 (email)
    # 142 LOAD_ATTR                3 (message)
    # 152 LOAD_METHOD              4 (Message)
    # 174 PRECALL                  0
    # 178 CALL                     0
    # 188 STORE_FAST               7 (info)
    # 439         190 LOAD_FAST                1 (response_headers)
    # 192 LOAD_METHOD              5 (items)
    # 214 PRECALL                  0
    # 218 CALL                     0
    # 228 GET_ITER
    # >>  230 FOR_ITER                14 (to 260)
    # 232 UNPACK_SEQUENCE          2
    # 236 STORE_FAST               8 (key)
    # 238 STORE_FAST               9 (value)
    # 440         240 LOAD_FAST                8 (key)
    # 242 LOAD_CONST               2 (('status', 'content-encoding', 'transfer-encoding'))
    # 244 CONTAINS_OP              1
    # 246 POP_JUMP_FORWARD_IF_FALSE     5 (to 258)
    # 441         248 LOAD_FAST                9 (value)
    # 250 LOAD_FAST                7 (info)
    # 252 LOAD_FAST                8 (key)
    # 254 STORE_SUBSCR
    # >>  258 JUMP_BACKWARD           15 (to 230)
    # 445     >>  260 LOAD_FAST                1 (response_headers)
    # 262 LOAD_METHOD              6 (get)
    # 284 LOAD_CONST               3 ('vary')
    # 286 LOAD_CONST               0 (None)
    # 288 PRECALL                  2
    # 292 CALL                     2
    # 302 STORE_FAST              10 (vary)
    # 446         304 LOAD_FAST               10 (vary)
    # 306 POP_JUMP_FORWARD_IF_FALSE    97 (to 502)
    # 447         308 LOAD_FAST               10 (vary)
    # 310 LOAD_METHOD              7 (lower)
    # 332 PRECALL                  0
    # 336 CALL                     0
    # 346 LOAD_METHOD              8 (replace)
    # 368 LOAD_CONST               4 (' ')
    # 370 LOAD_CONST               5 ('')
    # 372 PRECALL                  2
    # 376 CALL                     2
    # 386 LOAD_METHOD              9 (split)
    # 408 LOAD_CONST               6 (',')
    # 410 PRECALL                  1
    # 414 CALL                     1
    # 424 STORE_FAST              11 (vary_headers)
    # 448         426 LOAD_FAST               11 (vary_headers)
    # 428 GET_ITER
    # >>  430 FOR_ITER                35 (to 502)
    # 432 STORE_FAST              12 (header)
    # 449         434 LOAD_CONST               7 ('-varied-%s')
    # 436 LOAD_FAST               12 (header)
    # 438 BINARY_OP                6 (%)
    # 442 STORE_FAST               8 (key)
    # 450         444 NOP
    # 451         446 LOAD_FAST                0 (request_headers)
    # 448 LOAD_FAST               12 (header)
    # 450 BINARY_SUBSCR
    # 460 LOAD_FAST                7 (info)
    # 462 LOAD_FAST                8 (key)
    # 464 STORE_SUBSCR
    # 468 JUMP_BACKWARD           20 (to 430)
    # >>  470 PUSH_EXC_INFO
    # 452         472 LOAD_GLOBAL             20 (KeyError)
    # 484 CHECK_EXC_MATCH
    # 486 POP_JUMP_FORWARD_IF_FALSE     3 (to 494)
    # 488 POP_TOP
    # 453         490 POP_EXCEPT
    # 492 JUMP_BACKWARD           32 (to 430)
    # 452     >>  494 RERAISE                  0
    # >>  496 COPY                     3
    # 498 POP_EXCEPT
    # 500 RERAISE                  1
    # 455     >>  502 LOAD_FAST                1 (response_headers)
    # 504 LOAD_ATTR               11 (status)
    # 514 STORE_FAST              13 (status)
    # 456         516 LOAD_FAST               13 (status)
    # 518 LOAD_CONST               8 (304)
    # 520 COMPARE_OP               2 (==)
    # 526 POP_JUMP_FORWARD_IF_FALSE     2 (to 532)
    # 457         528 LOAD_CONST               9 (200)
    # 530 STORE_FAST              13 (status)
    # 459     >>  532 LOAD_CONST              10 ('status: %d\r\n')
    # 534 LOAD_FAST               13 (status)
    # 536 BINARY_OP                6 (%)
    # 540 STORE_FAST              14 (status_header)
    # 461         542 NOP
    # 462         544 LOAD_FAST                7 (info)
    # 546 LOAD_METHOD             12 (as_string)
    # 568 PRECALL                  0
    # 572 CALL                     0
    # 582 STORE_FAST              15 (header_str)
    # 584 JUMP_FORWARD            66 (to 718)
    # >>  586 PUSH_EXC_INFO
    # 463         588 LOAD_GLOBAL             26 (UnicodeEncodeError)
    # 600 CHECK_EXC_MATCH
    # 602 POP_JUMP_FORWARD_IF_FALSE    53 (to 710)
    # 604 POP_TOP
    # 464         606 LOAD_GLOBAL             29 (NULL + setattr)
    # 618 LOAD_FAST                7 (info)
    # 620 LOAD_CONST              11 ('_write_headers')
    # 622 LOAD_GLOBAL             31 (NULL + _bind_write_headers)
    # 634 LOAD_FAST                7 (info)
    # 636 PRECALL                  1
    # 640 CALL                     1
    # 650 PRECALL                  3
    # 654 CALL                     3
    # 664 POP_TOP
    # 465         666 LOAD_FAST                7 (info)
    # 668 LOAD_METHOD             12 (as_string)
    # 690 PRECALL                  0
    # 694 CALL                     0
    # 704 STORE_FAST              15 (header_str)
    # 706 POP_EXCEPT
    # 708 JUMP_FORWARD             4 (to 718)
    # 463     >>  710 RERAISE                  0
    # >>  712 COPY                     3
    # 714 POP_EXCEPT
    # 716 RERAISE                  1
    # 467     >>  718 LOAD_GLOBAL             33 (NULL + re)
    # 730 LOAD_ATTR               17 (sub)
    # 740 LOAD_CONST              12 ('\r(?!\n)|(?<!\r)\n')
    # 742 LOAD_CONST              13 ('\r\n')
    # 744 LOAD_FAST               15 (header_str)
    # 746 PRECALL                  3
    # 750 CALL                     3
    # 760 STORE_FAST              15 (header_str)
    # 468         762 LOAD_CONST              14 (b'')
    # 764 LOAD_METHOD             18 (join)
    # 786 LOAD_FAST               14 (status_header)
    # 788 LOAD_METHOD             19 (encode)
    # 810 LOAD_CONST              15 ('utf-8')
    # 812 PRECALL                  1
    # 816 CALL                     1
    # 826 LOAD_FAST               15 (header_str)
    # 828 LOAD_METHOD             19 (encode)
    # 850 LOAD_CONST              15 ('utf-8')
    # 852 PRECALL                  1
    # 856 CALL                     1
    # 866 LOAD_FAST                2 (content)
    # 868 BUILD_LIST               3
    # 870 PRECALL                  1
    # 874 CALL                     1
    # 884 STORE_FAST              16 (text)
    # 470         886 LOAD_FAST                3 (cache)
    # 888 LOAD_METHOD             20 (set)
    # 910 LOAD_FAST                4 (cachekey)
    # 912 LOAD_FAST               16 (text)
    # 914 PRECALL                  2
    # 918 CALL                     2
    # 928 POP_TOP
    # 930 LOAD_CONST               0 (None)
    # 932 RETURN_VALUE
    # 432     >>  934 LOAD_CONST               0 (None)
    # 936 RETURN_VALUE
    # ExceptionTable:
    # 446 to 466 -> 470 [1]
    # 470 to 488 -> 496 [2] lasti
    # 494 to 494 -> 496 [2] lasti
    # 544 to 582 -> 586 [0]
    # 586 to 704 -> 712 [1] lasti
    # 710 to 710 -> 712 [1] lasti

def _cnonce():
    # 473           0 RESUME                   0
    # 474           2 LOAD_GLOBAL              1 (NULL + _md5)
    # 475          14 LOAD_GLOBAL              3 (NULL + time)
    # 26 LOAD_ATTR                2 (ctime)
    # 36 PRECALL                  0
    # 40 CALL                     0
    # 50 FORMAT_VALUE             1 (str)
    # 52 LOAD_CONST               1 (':')
    # 54 LOAD_CONST               2 (<code object <listcomp> at 0x000001EBD7DDF930, file "httplib2\__init__.py", line 475>)
    # 56 MAKE_FUNCTION            0
    # 58 LOAD_GLOBAL              7 (NULL + range)
    # 70 LOAD_CONST               3 (20)
    # 72 PRECALL                  1
    # 76 CALL                     1
    # 86 GET_ITER
    # 88 PRECALL                  0
    # 92 CALL                     0
    # 102 FORMAT_VALUE             1 (str)
    # 104 BUILD_STRING             3
    # 106 LOAD_METHOD              4 (encode)
    # 128 LOAD_CONST               4 ('utf-8')
    # 130 PRECALL                  1
    # 134 CALL                     1
    # 474         144 PRECALL                  1
    # 148 CALL                     1
    # 476         158 LOAD_METHOD              5 (hexdigest)
    # 180 PRECALL                  0
    # 184 CALL                     0
    # 474         194 STORE_FAST               0 (dig)
    # 477         196 LOAD_FAST                0 (dig)
    # 198 LOAD_CONST               0 (None)
    # 200 LOAD_CONST               5 (16)
    # 202 BUILD_SLICE              2
    # 204 BINARY_SUBSCR
    # 214 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7DDF930, file "httplib2\__init__.py", line 475>:
    # 475           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                29 (to 66)
    # 8 STORE_FAST               1 (i)
    # 10 LOAD_CONST               0 ('0123456789')
    # 12 LOAD_GLOBAL              1 (NULL + random)
    # 24 LOAD_ATTR                1 (randrange)
    # 34 LOAD_CONST               1 (0)
    # 36 LOAD_CONST               2 (9)
    # 38 PRECALL                  2
    # 42 CALL                     2
    # 52 BINARY_SUBSCR
    # 62 LIST_APPEND              2
    # 64 JUMP_BACKWARD           30 (to 6)
    # >>   66 RETURN_VALUE

def _wsse_username_token(cnonce, iso_now, password):
    # 480           0 RESUME                   0
    # 482           2 LOAD_GLOBAL              1 (NULL + base64)
    # 14 LOAD_ATTR                1 (b64encode)
    # 24 LOAD_GLOBAL              5 (NULL + _sha)
    # 36 LOAD_FAST                0 (cnonce)
    # 38 FORMAT_VALUE             1 (str)
    # 40 LOAD_FAST                1 (iso_now)
    # 42 FORMAT_VALUE             1 (str)
    # 44 LOAD_FAST                2 (password)
    # 46 FORMAT_VALUE             1 (str)
    # 48 BUILD_STRING             3
    # 50 LOAD_METHOD              3 (encode)
    # 72 LOAD_CONST               1 ('utf-8')
    # 74 PRECALL                  1
    # 78 CALL                     1
    # 88 PRECALL                  1
    # 92 CALL                     1
    # 102 LOAD_METHOD              4 (digest)
    # 124 PRECALL                  0
    # 128 CALL                     0
    # 138 PRECALL                  1
    # 142 CALL                     1
    # 152 LOAD_METHOD              5 (strip)
    # 174 PRECALL                  0
    # 178 CALL                     0
    # 188 LOAD_METHOD              6 (decode)
    # 210 LOAD_CONST               1 ('utf-8')
    # 212 PRECALL                  1
    # 216 CALL                     1
    # 481         226 RETURN_VALUE

class Authentication:
    """Authentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 496           0 RESUME                   0
        # 497           2 LOAD_GLOBAL              1 (NULL + parse_uri)
        # 14 LOAD_FAST                3 (request_uri)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 UNPACK_SEQUENCE          5
        # 34 STORE_FAST               8 (scheme)
        # 36 STORE_FAST               9 (authority)
        # 38 STORE_FAST              10 (path)
        # 40 STORE_FAST              11 (query)
        # 42 STORE_FAST              12 (fragment)
        # 498          44 LOAD_FAST               10 (path)
        # 46 LOAD_FAST                0 (self)
        # 48 STORE_ATTR               1 (path)
        # 499          58 LOAD_FAST                2 (host)
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               2 (host)
        # 500          72 LOAD_FAST                1 (credentials)
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               3 (credentials)
        # 501          86 LOAD_FAST                7 (http)
        # 88 LOAD_FAST                0 (self)
        # 90 STORE_ATTR               4 (http)
        # 100 LOAD_CONST               0 (None)
        # 102 RETURN_VALUE

    def depth(self, request_uri):
        # 503           0 RESUME                   0
        # 504           2 LOAD_GLOBAL              1 (NULL + parse_uri)
        # 14 LOAD_FAST                1 (request_uri)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 UNPACK_SEQUENCE          5
        # 34 STORE_FAST               2 (scheme)
        # 36 STORE_FAST               3 (authority)
        # 38 STORE_FAST               4 (path)
        # 40 STORE_FAST               5 (query)
        # 42 STORE_FAST               6 (fragment)
        # 505          44 LOAD_FAST                1 (request_uri)
        # 46 LOAD_GLOBAL              3 (NULL + len)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_ATTR                2 (path)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 LOAD_CONST               0 (None)
        # 86 BUILD_SLICE              2
        # 88 BINARY_SUBSCR
        # 98 LOAD_METHOD              3 (count)
        # 120 LOAD_CONST               1 ('/')
        # 122 PRECALL                  1
        # 126 CALL                     1
        # 136 RETURN_VALUE

    def inscope(self, host, request_uri):
        # 507           0 RESUME                   0
        # 509           2 LOAD_GLOBAL              1 (NULL + parse_uri)
        # 14 LOAD_FAST                2 (request_uri)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 UNPACK_SEQUENCE          5
        # 34 STORE_FAST               3 (scheme)
        # 36 STORE_FAST               4 (authority)
        # 38 STORE_FAST               5 (path)
        # 40 STORE_FAST               6 (query)
        # 42 STORE_FAST               7 (fragment)
        # 510          44 LOAD_FAST                1 (host)
        # 46 LOAD_FAST                0 (self)
        # 48 LOAD_ATTR                1 (host)
        # 58 COMPARE_OP               2 (==)
        # 64 JUMP_IF_FALSE_OR_POP    25 (to 116)
        # 66 LOAD_FAST                5 (path)
        # 68 LOAD_METHOD              2 (startswith)
        # 90 LOAD_FAST                0 (self)
        # 92 LOAD_ATTR                3 (path)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # >>  116 RETURN_VALUE

    def request(self, method, request_uri, headers, content):
        """Modify the request headers to add the appropriate
        Authorization header. Over-rise this in sub-classes."""
        # 512           0 RESUME                   0
        # 515           2 LOAD_CONST               1 (None)
        # 4 RETURN_VALUE

    def response(self, response, content):
        """Gives us a chance to update with new nonces
        or such returned from the last authorized response.
        Over-rise this in sub-classes if necessary.

        Return TRUE is the request is to be retried, for
        example Digest may return stale=true.
        """
        # 517           0 RESUME                   0
        # 525           2 LOAD_CONST               1 (False)
        # 4 RETURN_VALUE

    def __eq__(self, auth):
        # 527           0 RESUME                   0
        # 528           2 LOAD_CONST               1 (False)
        # 4 RETURN_VALUE

    def __ne__(self, auth):
        # 530           0 RESUME                   0
        # 531           2 LOAD_CONST               1 (True)
        # 4 RETURN_VALUE

    def __lt__(self, auth):
        # 533           0 RESUME                   0
        # 534           2 LOAD_CONST               1 (True)
        # 4 RETURN_VALUE

    def __gt__(self, auth):
        # 536           0 RESUME                   0
        # 537           2 LOAD_CONST               1 (False)
        # 4 RETURN_VALUE

    def __le__(self, auth):
        # 539           0 RESUME                   0
        # 540           2 LOAD_CONST               1 (True)
        # 4 RETURN_VALUE

    def __ge__(self, auth):
        # 542           0 RESUME                   0
        # 543           2 LOAD_CONST               1 (False)
        # 4 RETURN_VALUE

    def __bool__(self):
        # 545           0 RESUME                   0
        # 546           2 LOAD_CONST               1 (True)
        # 4 RETURN_VALUE


class BasicAuthentication:
    """BasicAuthentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 550           0 RESUME                   0
        # 551           2 LOAD_GLOBAL              0 (Authentication)
        # 14 LOAD_METHOD              1 (__init__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_FAST                1 (credentials)
        # 40 LOAD_FAST                2 (host)
        # 42 LOAD_FAST                3 (request_uri)
        # 44 LOAD_FAST                4 (headers)
        # 46 LOAD_FAST                5 (response)
        # 48 LOAD_FAST                6 (content)
        # 50 LOAD_FAST                7 (http)
        # 52 PRECALL                  8
        # 56 CALL                     8
        # 66 POP_TOP
        # 68 LOAD_CONST               0 (None)
        # 70 RETURN_VALUE

    def request(self, method, request_uri, headers, content):
        """Modify the request headers to add the appropriate
        Authorization header."""
        # 553           0 RESUME                   0
        # 556           2 LOAD_CONST               1 ('Basic ')
        # 4 LOAD_GLOBAL              1 (NULL + base64)
        # 16 LOAD_ATTR                1 (b64encode)
        # 557          26 LOAD_CONST               2 ('%s:%s')
        # 28 LOAD_FAST                0 (self)
        # 30 LOAD_ATTR                2 (credentials)
        # 40 BINARY_OP                6 (%)
        # 44 LOAD_METHOD              3 (encode)
        # 66 LOAD_CONST               3 ('utf-8')
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 556          82 PRECALL                  1
        # 86 CALL                     1
        # 558          96 LOAD_METHOD              4 (strip)
        # 118 PRECALL                  0
        # 122 CALL                     0
        # 132 LOAD_METHOD              5 (decode)
        # 154 LOAD_CONST               3 ('utf-8')
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 556         170 BINARY_OP                0 (+)
        # 174 LOAD_FAST                3 (headers)
        # 176 LOAD_CONST               4 ('authorization')
        # 178 STORE_SUBSCR
        # 182 LOAD_CONST               5 (None)
        # 184 RETURN_VALUE


class DigestAuthentication:
    """DigestAuthentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 565           0 RESUME                   0
        # 566           2 LOAD_GLOBAL              0 (Authentication)
        # 14 LOAD_METHOD              1 (__init__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_FAST                1 (credentials)
        # 40 LOAD_FAST                2 (host)
        # 42 LOAD_FAST                3 (request_uri)
        # 44 LOAD_FAST                4 (headers)
        # 46 LOAD_FAST                5 (response)
        # 48 LOAD_FAST                6 (content)
        # 50 LOAD_FAST                7 (http)
        # 52 PRECALL                  8
        # 56 CALL                     8
        # 66 POP_TOP
        # 567          68 LOAD_GLOBAL              5 (NULL + auth)
        # 80 LOAD_ATTR                3 (_parse_www_authenticate)
        # 90 LOAD_FAST                5 (response)
        # 92 LOAD_CONST               1 ('www-authenticate')
        # 94 PRECALL                  2
        # 98 CALL                     2
        # 108 LOAD_CONST               2 ('digest')
        # 110 BINARY_SUBSCR
        # 120 LOAD_FAST                0 (self)
        # 122 STORE_ATTR               4 (challenge)
        # 568         132 LOAD_FAST                0 (self)
        # 134 LOAD_ATTR                4 (challenge)
        # 144 LOAD_METHOD              5 (get)
        # 166 LOAD_CONST               3 ('qop')
        # 168 LOAD_CONST               4 ('auth')
        # 170 PRECALL                  2
        # 174 CALL                     2
        # 184 STORE_FAST               8 (qop)
        # 569         186 LOAD_CONST               4 ('auth')
        # 188 LOAD_CONST               5 (<code object <listcomp> at 0x000001EBD7E224C0, file "httplib2\__init__.py", line 569>)
        # 190 MAKE_FUNCTION            0
        # 192 LOAD_FAST                8 (qop)
        # 194 LOAD_METHOD              6 (split)
        # 216 PRECALL                  0
        # 220 CALL                     0
        # 230 GET_ITER
        # 232 PRECALL                  0
        # 236 CALL                     0
        # 246 CONTAINS_OP              0
        # 248 POP_JUMP_FORWARD_IF_FALSE     2 (to 254)
        # 250 LOAD_CONST               4 ('auth')
        # 252 JUMP_IF_TRUE_OR_POP      1 (to 256)
        # >>  254 LOAD_CONST               0 (None)
        # >>  256 LOAD_FAST                0 (self)
        # 258 LOAD_ATTR                4 (challenge)
        # 268 LOAD_CONST               3 ('qop')
        # 270 STORE_SUBSCR
        # 570         274 LOAD_FAST                0 (self)
        # 276 LOAD_ATTR                4 (challenge)
        # 286 LOAD_CONST               3 ('qop')
        # 288 BINARY_SUBSCR
        # 298 POP_JUMP_FORWARD_IF_NOT_NONE    31 (to 362)
        # 571         300 LOAD_GLOBAL             15 (NULL + UnimplementedDigestAuthOptionError)
        # 312 LOAD_GLOBAL             17 (NULL + _)
        # 324 LOAD_CONST               6 ('Unsupported value for qop: %s.')
        # 326 LOAD_FAST                8 (qop)
        # 328 BINARY_OP                6 (%)
        # 332 PRECALL                  1
        # 336 CALL                     1
        # 346 PRECALL                  1
        # 350 CALL                     1
        # 360 RAISE_VARARGS            1
        # 572     >>  362 LOAD_FAST                0 (self)
        # 364 LOAD_ATTR                4 (challenge)
        # 374 LOAD_METHOD              5 (get)
        # 396 LOAD_CONST               7 ('algorithm')
        # 398 LOAD_CONST               8 ('MD5')
        # 400 PRECALL                  2
        # 404 CALL                     2
        # 414 LOAD_METHOD              9 (upper)
        # 436 PRECALL                  0
        # 440 CALL                     0
        # 450 LOAD_FAST                0 (self)
        # 452 LOAD_ATTR                4 (challenge)
        # 462 LOAD_CONST               7 ('algorithm')
        # 464 STORE_SUBSCR
        # 573         468 LOAD_FAST                0 (self)
        # 470 LOAD_ATTR                4 (challenge)
        # 480 LOAD_CONST               7 ('algorithm')
        # 482 BINARY_SUBSCR
        # 492 LOAD_CONST               8 ('MD5')
        # 494 COMPARE_OP               3 (!=)
        # 500 POP_JUMP_FORWARD_IF_FALSE    42 (to 586)
        # 574         502 LOAD_GLOBAL             15 (NULL + UnimplementedDigestAuthOptionError)
        # 575         514 LOAD_GLOBAL             17 (NULL + _)
        # 526 LOAD_CONST               9 ('Unsupported value for algorithm: %s.')
        # 528 LOAD_FAST                0 (self)
        # 530 LOAD_ATTR                4 (challenge)
        # 540 LOAD_CONST               7 ('algorithm')
        # 542 BINARY_SUBSCR
        # 552 BINARY_OP                6 (%)
        # 556 PRECALL                  1
        # 560 CALL                     1
        # 574         570 PRECALL                  1
        # 574 CALL                     1
        # 584 RAISE_VARARGS            1
        # 577     >>  586 LOAD_CONST              10 ('')
        # 588 LOAD_METHOD             10 (join)
        # 610 LOAD_FAST                0 (self)
        # 612 LOAD_ATTR               11 (credentials)
        # 622 LOAD_CONST              11 (0)
        # 624 BINARY_SUBSCR
        # 634 LOAD_CONST              12 (':')
        # 636 LOAD_FAST                0 (self)
        # 638 LOAD_ATTR                4 (challenge)
        # 648 LOAD_CONST              13 ('realm')
        # 650 BINARY_SUBSCR
        # 660 LOAD_CONST              12 (':')
        # 662 LOAD_FAST                0 (self)
        # 664 LOAD_ATTR               11 (credentials)
        # 674 LOAD_CONST              14 (1)
        # 676 BINARY_SUBSCR
        # 686 BUILD_LIST               5
        # 688 PRECALL                  1
        # 692 CALL                     1
        # 702 LOAD_FAST                0 (self)
        # 704 STORE_ATTR              12 (A1)
        # 578         714 LOAD_CONST              14 (1)
        # 716 LOAD_FAST                0 (self)
        # 718 LOAD_ATTR                4 (challenge)
        # 728 LOAD_CONST              15 ('nc')
        # 730 STORE_SUBSCR
        # 734 LOAD_CONST               0 (None)
        # 736 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7E224C0, file "httplib2\__init__.py", line 569>:
        # 569           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                22 (to 52)
        # 8 STORE_FAST               1 (x)
        # 10 LOAD_FAST                1 (x)
        # 12 LOAD_METHOD              0 (strip)
        # 34 PRECALL                  0
        # 38 CALL                     0
        # 48 LIST_APPEND              2
        # 50 JUMP_BACKWARD           23 (to 6)
        # >>   52 RETURN_VALUE

    def request(self, method, request_uri, headers, content, cnonce):
        """Modify the request headers"""
        # 0 MAKE_CELL                9 (H)
        # 580           2 RESUME                   0
        # 582           4 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7E30880, file "httplib2\__init__.py", line 582>)
        # 6 MAKE_FUNCTION            0
        # 8 STORE_DEREF              9 (H)
        # 583          10 LOAD_CLOSURE             9 (H)
        # 12 BUILD_TUPLE              1
        # 14 LOAD_CONST               2 (<code object <lambda> at 0x000001EBD7E34FF0, file "httplib2\__init__.py", line 583>)
        # 16 MAKE_FUNCTION            8 (closure)
        # 18 STORE_FAST               6 (KD)
        # 584          20 LOAD_CONST               3 ('')
        # 22 LOAD_METHOD              0 (join)
        # 44 LOAD_FAST                1 (method)
        # 46 LOAD_CONST               4 (':')
        # 48 LOAD_FAST                2 (request_uri)
        # 50 BUILD_LIST               3
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 STORE_FAST               7 (A2)
        # 585          68 LOAD_FAST                5 (cnonce)
        # 70 JUMP_IF_TRUE_OR_POP     13 (to 98)
        # 72 LOAD_GLOBAL              3 (NULL + _cnonce)
        # 84 PRECALL                  0
        # 88 CALL                     0
        # >>   98 LOAD_FAST                0 (self)
        # 100 LOAD_ATTR                2 (challenge)
        # 110 LOAD_CONST               5 ('cnonce')
        # 112 STORE_SUBSCR
        # 586         116 LOAD_CONST               6 ('"%s"')
        # 118 PUSH_NULL
        # 120 LOAD_FAST                6 (KD)
        # 587         122 PUSH_NULL
        # 124 LOAD_DEREF               9 (H)
        # 126 LOAD_FAST                0 (self)
        # 128 LOAD_ATTR                3 (A1)
        # 138 PRECALL                  1
        # 142 CALL                     1
        # 590         152 LOAD_FAST                0 (self)
        # 154 LOAD_ATTR                2 (challenge)
        # 164 LOAD_CONST               7 ('nonce')
        # 166 BINARY_SUBSCR
        # 176 FORMAT_VALUE             1 (str)
        # 178 LOAD_CONST               4 (':')
        # 591         180 LOAD_CONST               8 ('%08x')
        # 182 LOAD_FAST                0 (self)
        # 184 LOAD_ATTR                2 (challenge)
        # 194 LOAD_CONST               9 ('nc')
        # 196 BINARY_SUBSCR
        # 206 BINARY_OP                6 (%)
        # 210 FORMAT_VALUE             1 (str)
        # 212 LOAD_CONST               4 (':')
        # 592         214 LOAD_FAST                0 (self)
        # 216 LOAD_ATTR                2 (challenge)
        # 226 LOAD_CONST               5 ('cnonce')
        # 228 BINARY_SUBSCR
        # 238 FORMAT_VALUE             1 (str)
        # 240 LOAD_CONST               4 (':')
        # 593         242 LOAD_FAST                0 (self)
        # 244 LOAD_ATTR                2 (challenge)
        # 254 LOAD_CONST              10 ('qop')
        # 256 BINARY_SUBSCR
        # 266 FORMAT_VALUE             1 (str)
        # 268 LOAD_CONST               4 (':')
        # 594         270 PUSH_NULL
        # 272 LOAD_DEREF               9 (H)
        # 274 LOAD_FAST                7 (A2)
        # 276 PRECALL                  1
        # 280 CALL                     1
        # 290 FORMAT_VALUE             1 (str)
        # 588         292 BUILD_STRING             9
        # 586         294 PRECALL                  2
        # 298 CALL                     2
        # 308 BINARY_OP                6 (%)
        # 312 STORE_FAST               8 (request_digest)
        # 598         314 LOAD_CONST              11 ('Digest username="%s", realm="%s", nonce="%s", uri="%s", algorithm=%s, response=%s, qop=%s, nc=%08x, cnonce="%s"')
        # 602         316 LOAD_FAST                0 (self)
        # 318 LOAD_ATTR                4 (credentials)
        # 328 LOAD_CONST              12 (0)
        # 330 BINARY_SUBSCR
        # 603         340 LOAD_FAST                0 (self)
        # 342 LOAD_ATTR                2 (challenge)
        # 352 LOAD_CONST              13 ('realm')
        # 354 BINARY_SUBSCR
        # 604         364 LOAD_FAST                0 (self)
        # 366 LOAD_ATTR                2 (challenge)
        # 376 LOAD_CONST               7 ('nonce')
        # 378 BINARY_SUBSCR
        # 605         388 LOAD_FAST                2 (request_uri)
        # 606         390 LOAD_FAST                0 (self)
        # 392 LOAD_ATTR                2 (challenge)
        # 402 LOAD_CONST              14 ('algorithm')
        # 404 BINARY_SUBSCR
        # 607         414 LOAD_FAST                8 (request_digest)
        # 608         416 LOAD_FAST                0 (self)
        # 418 LOAD_ATTR                2 (challenge)
        # 428 LOAD_CONST              10 ('qop')
        # 430 BINARY_SUBSCR
        # 609         440 LOAD_FAST                0 (self)
        # 442 LOAD_ATTR                2 (challenge)
        # 452 LOAD_CONST               9 ('nc')
        # 454 BINARY_SUBSCR
        # 610         464 LOAD_FAST                0 (self)
        # 466 LOAD_ATTR                2 (challenge)
        # 476 LOAD_CONST               5 ('cnonce')
        # 478 BINARY_SUBSCR
        # 601         488 BUILD_TUPLE              9
        # 597         490 BINARY_OP                6 (%)
        # 494 LOAD_FAST                3 (headers)
        # 496 LOAD_CONST              15 ('authorization')
        # 498 STORE_SUBSCR
        # 612         502 LOAD_FAST                0 (self)
        # 504 LOAD_ATTR                2 (challenge)
        # 514 LOAD_METHOD              5 (get)
        # 536 LOAD_CONST              16 ('opaque')
        # 538 PRECALL                  1
        # 542 CALL                     1
        # 552 POP_JUMP_FORWARD_IF_FALSE    30 (to 614)
        # 613         554 LOAD_FAST                3 (headers)
        # 556 LOAD_CONST              15 ('authorization')
        # 558 COPY                     2
        # 560 COPY                     2
        # 562 BINARY_SUBSCR
        # 572 LOAD_CONST              17 (', opaque="%s"')
        # 574 LOAD_FAST                0 (self)
        # 576 LOAD_ATTR                2 (challenge)
        # 586 LOAD_CONST              16 ('opaque')
        # 588 BINARY_SUBSCR
        # 598 BINARY_OP                6 (%)
        # 602 BINARY_OP               13 (+=)
        # 606 SWAP                     3
        # 608 SWAP                     2
        # 610 STORE_SUBSCR
        # 614     >>  614 LOAD_FAST                0 (self)
        # 616 LOAD_ATTR                2 (challenge)
        # 626 LOAD_CONST               9 ('nc')
        # 628 COPY                     2
        # 630 COPY                     2
        # 632 BINARY_SUBSCR
        # 642 LOAD_CONST              18 (1)
        # 644 BINARY_OP               13 (+=)
        # 648 SWAP                     3
        # 650 SWAP                     2
        # 652 STORE_SUBSCR
        # 656 LOAD_CONST              19 (None)
        # 658 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E30880, file "httplib2\__init__.py", line 582>:
        # 582           0 RESUME                   0
        # 2 LOAD_GLOBAL              1 (NULL + _md5)
        # 14 LOAD_FAST                0 (x)
        # 16 LOAD_METHOD              1 (encode)
        # 38 LOAD_CONST               1 ('utf-8')
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 PRECALL                  1
        # 58 CALL                     1
        # 68 LOAD_METHOD              2 (hexdigest)
        # 90 PRECALL                  0
        # 94 CALL                     0
        # 104 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E34FF0, file "httplib2\__init__.py", line 583>:
        # 0 COPY_FREE_VARS           1
        # 583           2 RESUME                   0
        # 4 PUSH_NULL
        # 6 LOAD_DEREF               2 (H)
        # 8 LOAD_FAST                0 (s)
        # 10 FORMAT_VALUE             1 (str)
        # 12 LOAD_CONST               1 (':')
        # 14 LOAD_FAST                1 (d)
        # 16 FORMAT_VALUE             1 (str)
        # 18 BUILD_STRING             3
        # 20 PRECALL                  1
        # 24 CALL                     1
        # 34 RETURN_VALUE

    def response(self, response, content):
        # 616           0 RESUME                   0
        # 617           2 LOAD_CONST               1 ('authentication-info')
        # 4 LOAD_FAST                1 (response)
        # 6 CONTAINS_OP              1
        # 8 POP_JUMP_FORWARD_IF_FALSE    95 (to 200)
        # 618          10 LOAD_GLOBAL              1 (NULL + auth)
        # 22 LOAD_ATTR                1 (_parse_www_authenticate)
        # 32 LOAD_FAST                1 (response)
        # 34 LOAD_CONST               2 ('www-authenticate')
        # 36 PRECALL                  2
        # 40 CALL                     2
        # 50 LOAD_METHOD              2 (get)
        # 72 LOAD_CONST               3 ('digest')
        # 74 BUILD_MAP                0
        # 76 PRECALL                  2
        # 80 CALL                     2
        # 90 STORE_FAST               3 (challenge)
        # 619          92 LOAD_CONST               4 ('true')
        # 94 LOAD_FAST                3 (challenge)
        # 96 LOAD_METHOD              2 (get)
        # 118 LOAD_CONST               5 ('stale')
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 COMPARE_OP               2 (==)
        # 140 POP_JUMP_FORWARD_IF_FALSE    28 (to 198)
        # 620         142 LOAD_FAST                3 (challenge)
        # 144 LOAD_CONST               6 ('nonce')
        # 146 BINARY_SUBSCR
        # 156 LOAD_FAST                0 (self)
        # 158 LOAD_ATTR                3 (challenge)
        # 168 LOAD_CONST               6 ('nonce')
        # 170 STORE_SUBSCR
        # 621         174 LOAD_CONST               7 (1)
        # 176 LOAD_FAST                0 (self)
        # 178 LOAD_ATTR                3 (challenge)
        # 188 LOAD_CONST               8 ('nc')
        # 190 STORE_SUBSCR
        # 622         194 LOAD_CONST               9 (True)
        # 196 RETURN_VALUE
        # 619     >>  198 JUMP_FORWARD            51 (to 302)
        # 624     >>  200 LOAD_GLOBAL              1 (NULL + auth)
        # 212 LOAD_ATTR                4 (_parse_authentication_info)
        # 222 LOAD_FAST                1 (response)
        # 224 LOAD_CONST               1 ('authentication-info')
        # 226 PRECALL                  2
        # 230 CALL                     2
        # 240 STORE_FAST               4 (updated_challenge)
        # 626         242 LOAD_CONST              10 ('nextnonce')
        # 244 LOAD_FAST                4 (updated_challenge)
        # 246 CONTAINS_OP              0
        # 248 POP_JUMP_FORWARD_IF_FALSE    26 (to 302)
        # 627         250 LOAD_FAST                4 (updated_challenge)
        # 252 LOAD_CONST              10 ('nextnonce')
        # 254 BINARY_SUBSCR
        # 264 LOAD_FAST                0 (self)
        # 266 LOAD_ATTR                3 (challenge)
        # 276 LOAD_CONST               6 ('nonce')
        # 278 STORE_SUBSCR
        # 628         282 LOAD_CONST               7 (1)
        # 284 LOAD_FAST                0 (self)
        # 286 LOAD_ATTR                3 (challenge)
        # 296 LOAD_CONST               8 ('nc')
        # 298 STORE_SUBSCR
        # 629     >>  302 LOAD_CONST              11 (False)
        # 304 RETURN_VALUE


class HmacDigestAuthentication:
    """HmacDigestAuthentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 637           0 RESUME                   0
        # 638           2 LOAD_GLOBAL              0 (Authentication)
        # 14 LOAD_METHOD              1 (__init__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_FAST                1 (credentials)
        # 40 LOAD_FAST                2 (host)
        # 42 LOAD_FAST                3 (request_uri)
        # 44 LOAD_FAST                4 (headers)
        # 46 LOAD_FAST                5 (response)
        # 48 LOAD_FAST                6 (content)
        # 50 LOAD_FAST                7 (http)
        # 52 PRECALL                  8
        # 56 CALL                     8
        # 66 POP_TOP
        # 639          68 LOAD_GLOBAL              5 (NULL + auth)
        # 80 LOAD_ATTR                3 (_parse_www_authenticate)
        # 90 LOAD_FAST                5 (response)
        # 92 LOAD_CONST               1 ('www-authenticate')
        # 94 PRECALL                  2
        # 98 CALL                     2
        # 108 STORE_FAST               8 (challenge)
        # 640         110 LOAD_FAST                8 (challenge)
        # 112 LOAD_CONST               2 ('hmacdigest')
        # 114 BINARY_SUBSCR
        # 124 LOAD_FAST                0 (self)
        # 126 STORE_ATTR               4 (challenge)
        # 642         136 LOAD_FAST                0 (self)
        # 138 LOAD_ATTR                4 (challenge)
        # 148 LOAD_METHOD              5 (get)
        # 170 LOAD_CONST               3 ('reason')
        # 172 LOAD_CONST               4 ('unauthorized')
        # 174 PRECALL                  2
        # 178 CALL                     2
        # 188 LOAD_FAST                0 (self)
        # 190 LOAD_ATTR                4 (challenge)
        # 200 LOAD_CONST               3 ('reason')
        # 202 STORE_SUBSCR
        # 643         206 LOAD_FAST                0 (self)
        # 208 LOAD_ATTR                4 (challenge)
        # 218 LOAD_CONST               3 ('reason')
        # 220 BINARY_SUBSCR
        # 230 LOAD_CONST               5 (('unauthorized', 'integrity'))
        # 232 CONTAINS_OP              1
        # 234 POP_JUMP_FORWARD_IF_FALSE    10 (to 256)
        # 644         236 LOAD_CONST               4 ('unauthorized')
        # 238 LOAD_FAST                0 (self)
        # 240 LOAD_ATTR                4 (challenge)
        # 250 LOAD_CONST               3 ('reason')
        # 252 STORE_SUBSCR
        # 645     >>  256 LOAD_FAST                0 (self)
        # 258 LOAD_ATTR                4 (challenge)
        # 268 LOAD_METHOD              5 (get)
        # 290 LOAD_CONST               6 ('salt')
        # 292 LOAD_CONST               7 ('')
        # 294 PRECALL                  2
        # 298 CALL                     2
        # 308 LOAD_FAST                0 (self)
        # 310 LOAD_ATTR                4 (challenge)
        # 320 LOAD_CONST               6 ('salt')
        # 322 STORE_SUBSCR
        # 646         326 LOAD_FAST                0 (self)
        # 328 LOAD_ATTR                4 (challenge)
        # 338 LOAD_METHOD              5 (get)
        # 360 LOAD_CONST               8 ('snonce')
        # 362 PRECALL                  1
        # 366 CALL                     1
        # 376 POP_JUMP_FORWARD_IF_TRUE    28 (to 434)
        # 647         378 LOAD_GLOBAL             13 (NULL + UnimplementedHmacDigestAuthOptionError)
        # 648         390 LOAD_GLOBAL             15 (NULL + _)
        # 402 LOAD_CONST               9 ("The challenge doesn't contain a server nonce, or this one is empty.")
        # 404 PRECALL                  1
        # 408 CALL                     1
        # 647         418 PRECALL                  1
        # 422 CALL                     1
        # 432 RAISE_VARARGS            1
        # 650     >>  434 LOAD_FAST                0 (self)
        # 436 LOAD_ATTR                4 (challenge)
        # 446 LOAD_METHOD              5 (get)
        # 468 LOAD_CONST              10 ('algorithm')
        # 470 LOAD_CONST              11 ('HMAC-SHA-1')
        # 472 PRECALL                  2
        # 476 CALL                     2
        # 486 LOAD_FAST                0 (self)
        # 488 LOAD_ATTR                4 (challenge)
        # 498 LOAD_CONST              10 ('algorithm')
        # 500 STORE_SUBSCR
        # 651         504 LOAD_FAST                0 (self)
        # 506 LOAD_ATTR                4 (challenge)
        # 516 LOAD_CONST              10 ('algorithm')
        # 518 BINARY_SUBSCR
        # 528 LOAD_CONST              12 (('HMAC-SHA-1', 'HMAC-MD5'))
        # 530 CONTAINS_OP              1
        # 532 POP_JUMP_FORWARD_IF_FALSE    42 (to 618)
        # 652         534 LOAD_GLOBAL             13 (NULL + UnimplementedHmacDigestAuthOptionError)
        # 653         546 LOAD_GLOBAL             15 (NULL + _)
        # 558 LOAD_CONST              13 ('Unsupported value for algorithm: %s.')
        # 560 LOAD_FAST                0 (self)
        # 562 LOAD_ATTR                4 (challenge)
        # 572 LOAD_CONST              10 ('algorithm')
        # 574 BINARY_SUBSCR
        # 584 BINARY_OP                6 (%)
        # 588 PRECALL                  1
        # 592 CALL                     1
        # 652         602 PRECALL                  1
        # 606 CALL                     1
        # 616 RAISE_VARARGS            1
        # 655     >>  618 LOAD_FAST                0 (self)
        # 620 LOAD_ATTR                4 (challenge)
        # 630 LOAD_METHOD              5 (get)
        # 652 LOAD_CONST              14 ('pw-algorithm')
        # 654 LOAD_CONST              15 ('SHA-1')
        # 656 PRECALL                  2
        # 660 CALL                     2
        # 670 LOAD_FAST                0 (self)
        # 672 LOAD_ATTR                4 (challenge)
        # 682 LOAD_CONST              14 ('pw-algorithm')
        # 684 STORE_SUBSCR
        # 656         688 LOAD_FAST                0 (self)
        # 690 LOAD_ATTR                4 (challenge)
        # 700 LOAD_CONST              14 ('pw-algorithm')
        # 702 BINARY_SUBSCR
        # 712 LOAD_CONST              16 (('SHA-1', 'MD5'))
        # 714 CONTAINS_OP              1
        # 716 POP_JUMP_FORWARD_IF_FALSE    42 (to 802)
        # 657         718 LOAD_GLOBAL             13 (NULL + UnimplementedHmacDigestAuthOptionError)
        # 658         730 LOAD_GLOBAL             15 (NULL + _)
        # 742 LOAD_CONST              17 ('Unsupported value for pw-algorithm: %s.')
        # 744 LOAD_FAST                0 (self)
        # 746 LOAD_ATTR                4 (challenge)
        # 756 LOAD_CONST              14 ('pw-algorithm')
        # 758 BINARY_SUBSCR
        # 768 BINARY_OP                6 (%)
        # 772 PRECALL                  1
        # 776 CALL                     1
        # 657         786 PRECALL                  1
        # 790 CALL                     1
        # 800 RAISE_VARARGS            1
        # 660     >>  802 LOAD_FAST                0 (self)
        # 804 LOAD_ATTR                4 (challenge)
        # 814 LOAD_CONST              10 ('algorithm')
        # 816 BINARY_SUBSCR
        # 826 LOAD_CONST              18 ('HMAC-MD5')
        # 828 COMPARE_OP               2 (==)
        # 834 POP_JUMP_FORWARD_IF_FALSE    13 (to 862)
        # 661         836 LOAD_GLOBAL             16 (_md5)
        # 848 LOAD_FAST                0 (self)
        # 850 STORE_ATTR               9 (hashmod)
        # 860 JUMP_FORWARD            12 (to 886)
        # 663     >>  862 LOAD_GLOBAL             20 (_sha)
        # 874 LOAD_FAST                0 (self)
        # 876 STORE_ATTR               9 (hashmod)
        # 664     >>  886 LOAD_FAST                0 (self)
        # 888 LOAD_ATTR                4 (challenge)
        # 898 LOAD_CONST              14 ('pw-algorithm')
        # 900 BINARY_SUBSCR
        # 910 LOAD_CONST              19 ('MD5')
        # 912 COMPARE_OP               2 (==)
        # 918 POP_JUMP_FORWARD_IF_FALSE    13 (to 946)
        # 665         920 LOAD_GLOBAL             16 (_md5)
        # 932 LOAD_FAST                0 (self)
        # 934 STORE_ATTR              11 (pwhashmod)
        # 944 JUMP_FORWARD            12 (to 970)
        # 667     >>  946 LOAD_GLOBAL             20 (_sha)
        # 958 LOAD_FAST                0 (self)
        # 960 STORE_ATTR              11 (pwhashmod)
        # 668     >>  970 LOAD_CONST               7 ('')
        # 972 LOAD_METHOD             12 (join)
        # 670         994 LOAD_FAST                0 (self)
        # 996 LOAD_ATTR               13 (credentials)
        # 1006 LOAD_CONST              20 (0)
        # 1008 BINARY_SUBSCR
        # 671        1018 LOAD_CONST              21 (':')
        # 672        1020 LOAD_FAST                0 (self)
        # 1022 LOAD_ATTR               11 (pwhashmod)
        # 1032 LOAD_METHOD             14 (new)
        # 1054 LOAD_CONST               7 ('')
        # 1056 LOAD_METHOD             12 (join)
        # 1078 LOAD_FAST                0 (self)
        # 1080 LOAD_ATTR               13 (credentials)
        # 1090 LOAD_CONST              22 (1)
        # 1092 BINARY_SUBSCR
        # 1102 LOAD_FAST                0 (self)
        # 1104 LOAD_ATTR                4 (challenge)
        # 1114 LOAD_CONST               6 ('salt')
        # 1116 BINARY_SUBSCR
        # 1126 BUILD_LIST               2
        # 1128 PRECALL                  1
        # 1132 CALL                     1
        # 1142 PRECALL                  1
        # 1146 CALL                     1
        # 1156 LOAD_METHOD             15 (hexdigest)
        # 1178 PRECALL                  0
        # 1182 CALL                     0
        # 1192 LOAD_METHOD             16 (lower)
        # 1214 PRECALL                  0
        # 1218 CALL                     0
        # 673        1228 LOAD_CONST              21 (':')
        # 674        1230 LOAD_FAST                0 (self)
        # 1232 LOAD_ATTR                4 (challenge)
        # 1242 LOAD_CONST              23 ('realm')
        # 1244 BINARY_SUBSCR
        # 669        1254 BUILD_LIST               5
        # 668        1256 PRECALL                  1
        # 1260 CALL                     1
        # 1270 LOAD_FAST                0 (self)
        # 1272 STORE_ATTR              17 (key)
        # 677        1282 LOAD_FAST                0 (self)
        # 1284 LOAD_ATTR               11 (pwhashmod)
        # 1294 LOAD_METHOD             14 (new)
        # 1316 LOAD_FAST                0 (self)
        # 1318 LOAD_ATTR               17 (key)
        # 1328 PRECALL                  1
        # 1332 CALL                     1
        # 1342 LOAD_METHOD             15 (hexdigest)
        # 1364 PRECALL                  0
        # 1368 CALL                     0
        # 1378 LOAD_METHOD             16 (lower)
        # 1400 PRECALL                  0
        # 1404 CALL                     0
        # 1414 LOAD_FAST                0 (self)
        # 1416 STORE_ATTR              17 (key)
        # 1426 LOAD_CONST               0 (None)
        # 1428 RETURN_VALUE

    def request(self, method, request_uri, headers, content):
        """Modify the request headers"""
        # 0 MAKE_CELL                3 (headers)
        # 679           2 RESUME                   0
        # 681           4 LOAD_GLOBAL              1 (NULL + _get_end2end_headers)
        # 16 LOAD_DEREF               3 (headers)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 STORE_FAST               5 (keys)
        # 682          34 LOAD_CONST               1 ('')
        # 36 LOAD_METHOD              1 (join)
        # 58 LOAD_CONST               2 (<code object <listcomp> at 0x000001EBD7DAD140, file "httplib2\__init__.py", line 682>)
        # 60 MAKE_FUNCTION            0
        # 62 LOAD_FAST                5 (keys)
        # 64 GET_ITER
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 STORE_FAST               6 (keylist)
        # 683          96 LOAD_CONST               1 ('')
        # 98 LOAD_METHOD              1 (join)
        # 120 LOAD_CLOSURE             3 (headers)
        # 122 BUILD_TUPLE              1
        # 124 LOAD_CONST               3 (<code object <listcomp> at 0x000001EBD7E35290, file "httplib2\__init__.py", line 683>)
        # 126 MAKE_FUNCTION            8 (closure)
        # 128 LOAD_FAST                5 (keys)
        # 130 GET_ITER
        # 132 PRECALL                  0
        # 136 CALL                     0
        # 146 PRECALL                  1
        # 150 CALL                     1
        # 160 STORE_FAST               7 (headers_val)
        # 684         162 LOAD_GLOBAL              5 (NULL + time)
        # 174 LOAD_ATTR                3 (strftime)
        # 184 LOAD_CONST               4 ('%Y-%m-%dT%H:%M:%SZ')
        # 186 LOAD_GLOBAL              5 (NULL + time)
        # 198 LOAD_ATTR                4 (gmtime)
        # 208 PRECALL                  0
        # 212 CALL                     0
        # 222 PRECALL                  2
        # 226 CALL                     2
        # 236 STORE_FAST               8 (created)
        # 685         238 LOAD_GLOBAL             11 (NULL + _cnonce)
        # 250 PRECALL                  0
        # 254 CALL                     0
        # 264 STORE_FAST               9 (cnonce)
        # 686         266 LOAD_FAST                1 (method)
        # 268 FORMAT_VALUE             1 (str)
        # 270 LOAD_CONST               5 (':')
        # 272 LOAD_FAST                2 (request_uri)
        # 274 FORMAT_VALUE             1 (str)
        # 276 LOAD_CONST               5 (':')
        # 278 LOAD_FAST                9 (cnonce)
        # 280 FORMAT_VALUE             1 (str)
        # 282 LOAD_CONST               5 (':')
        # 284 LOAD_FAST                0 (self)
        # 286 LOAD_ATTR                6 (challenge)
        # 296 LOAD_CONST               6 ('snonce')
        # 298 BINARY_SUBSCR
        # 308 FORMAT_VALUE             1 (str)
        # 310 LOAD_CONST               5 (':')
        # 312 LOAD_FAST                7 (headers_val)
        # 314 FORMAT_VALUE             1 (str)
        # 316 BUILD_STRING             9
        # 318 STORE_FAST              10 (request_digest)
        # 687         320 LOAD_GLOBAL             15 (NULL + hmac)
        # 332 LOAD_ATTR                8 (new)
        # 342 LOAD_FAST                0 (self)
        # 344 LOAD_ATTR                9 (key)
        # 354 LOAD_FAST               10 (request_digest)
        # 356 LOAD_FAST                0 (self)
        # 358 LOAD_ATTR               10 (hashmod)
        # 368 PRECALL                  3
        # 372 CALL                     3
        # 382 LOAD_METHOD             11 (hexdigest)
        # 404 PRECALL                  0
        # 408 CALL                     0
        # 418 LOAD_METHOD             12 (lower)
        # 440 PRECALL                  0
        # 444 CALL                     0
        # 454 STORE_FAST              10 (request_digest)
        # 456 LOAD_CONST               7 ('HMACDigest username="')
        # 693         458 LOAD_FAST                0 (self)
        # 460 LOAD_ATTR               13 (credentials)
        # 470 LOAD_CONST               8 (0)
        # 472 BINARY_SUBSCR
        # 482 FORMAT_VALUE             1 (str)
        # 484 LOAD_CONST               9 ('", realm="')
        # 694         486 LOAD_FAST                0 (self)
        # 488 LOAD_ATTR                6 (challenge)
        # 498 LOAD_CONST              10 ('realm')
        # 500 BINARY_SUBSCR
        # 510 FORMAT_VALUE             1 (str)
        # 512 LOAD_CONST              11 ('", snonce="')
        # 695         514 LOAD_FAST                0 (self)
        # 516 LOAD_ATTR                6 (challenge)
        # 526 LOAD_CONST               6 ('snonce')
        # 528 BINARY_SUBSCR
        # 538 FORMAT_VALUE             1 (str)
        # 540 LOAD_CONST              12 ('", cnonce="')
        # 696         542 LOAD_FAST                9 (cnonce)
        # 544 FORMAT_VALUE             1 (str)
        # 546 LOAD_CONST              13 ('", uri="')
        # 697         548 LOAD_FAST                2 (request_uri)
        # 550 FORMAT_VALUE             1 (str)
        # 552 LOAD_CONST              14 ('", created="')
        # 698         554 LOAD_FAST                8 (created)
        # 556 FORMAT_VALUE             1 (str)
        # 558 LOAD_CONST              15 ('", response="')
        # 699         560 LOAD_FAST               10 (request_digest)
        # 562 FORMAT_VALUE             1 (str)
        # 564 LOAD_CONST              16 ('", headers="')
        # 700         566 LOAD_FAST                6 (keylist)
        # 568 FORMAT_VALUE             1 (str)
        # 570 LOAD_CONST              17 ('"')
        # 688         572 BUILD_STRING            17
        # 574 LOAD_DEREF               3 (headers)
        # 576 LOAD_CONST              18 ('authorization')
        # 578 STORE_SUBSCR
        # 582 LOAD_CONST              19 (None)
        # 584 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7DAD140, file "httplib2\__init__.py", line 682>:
        # 682           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                 7 (to 22)
        # 8 STORE_FAST               1 (k)
        # 10 LOAD_CONST               0 ('%s ')
        # 12 LOAD_FAST                1 (k)
        # 14 BINARY_OP                6 (%)
        # 18 LIST_APPEND              2
        # 20 JUMP_BACKWARD            8 (to 6)
        # >>   22 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7E35290, file "httplib2\__init__.py", line 683>:
        # 0 COPY_FREE_VARS           1
        # 683           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                10 (to 30)
        # 10 STORE_FAST               1 (k)
        # 12 LOAD_DEREF               2 (headers)
        # 14 LOAD_FAST                1 (k)
        # 16 BINARY_SUBSCR
        # 26 LIST_APPEND              2
        # 28 JUMP_BACKWARD           11 (to 8)
        # >>   30 RETURN_VALUE

    def response(self, response, content):
        # 703           0 RESUME                   0
        # 704           2 LOAD_GLOBAL              1 (NULL + auth)
        # 14 LOAD_ATTR                1 (_parse_www_authenticate)
        # 24 LOAD_FAST                1 (response)
        # 26 LOAD_CONST               1 ('www-authenticate')
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 LOAD_METHOD              2 (get)
        # 64 LOAD_CONST               2 ('hmacdigest')
        # 66 BUILD_MAP                0
        # 68 PRECALL                  2
        # 72 CALL                     2
        # 82 STORE_FAST               3 (challenge)
        # 705          84 LOAD_FAST                3 (challenge)
        # 86 LOAD_METHOD              2 (get)
        # 108 LOAD_CONST               3 ('reason')
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 LOAD_CONST               4 (('integrity', 'stale'))
        # 126 CONTAINS_OP              0
        # 128 POP_JUMP_FORWARD_IF_FALSE     2 (to 134)
        # 706         130 LOAD_CONST               5 (True)
        # 132 RETURN_VALUE
        # 707     >>  134 LOAD_CONST               6 (False)
        # 136 RETURN_VALUE


class WsseAuthentication:
    """WsseAuthentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 719           0 RESUME                   0
        # 720           2 LOAD_GLOBAL              0 (Authentication)
        # 14 LOAD_METHOD              1 (__init__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_FAST                1 (credentials)
        # 40 LOAD_FAST                2 (host)
        # 42 LOAD_FAST                3 (request_uri)
        # 44 LOAD_FAST                4 (headers)
        # 46 LOAD_FAST                5 (response)
        # 48 LOAD_FAST                6 (content)
        # 50 LOAD_FAST                7 (http)
        # 52 PRECALL                  8
        # 56 CALL                     8
        # 66 POP_TOP
        # 68 LOAD_CONST               0 (None)
        # 70 RETURN_VALUE

    def request(self, method, request_uri, headers, content):
        """Modify the request headers to add the appropriate
        Authorization header."""
        # 722           0 RESUME                   0
        # 725           2 LOAD_CONST               1 ('WSSE profile="UsernameToken"')
        # 4 LOAD_FAST                3 (headers)
        # 6 LOAD_CONST               2 ('authorization')
        # 8 STORE_SUBSCR
        # 726          12 LOAD_GLOBAL              1 (NULL + time)
        # 24 LOAD_ATTR                1 (strftime)
        # 34 LOAD_CONST               3 ('%Y-%m-%dT%H:%M:%SZ')
        # 36 LOAD_GLOBAL              1 (NULL + time)
        # 48 LOAD_ATTR                2 (gmtime)
        # 58 PRECALL                  0
        # 62 CALL                     0
        # 72 PRECALL                  2
        # 76 CALL                     2
        # 86 STORE_FAST               5 (iso_now)
        # 727          88 LOAD_GLOBAL              7 (NULL + _cnonce)
        # 100 PRECALL                  0
        # 104 CALL                     0
        # 114 STORE_FAST               6 (cnonce)
        # 728         116 LOAD_GLOBAL              9 (NULL + _wsse_username_token)
        # 128 LOAD_FAST                6 (cnonce)
        # 130 LOAD_FAST                5 (iso_now)
        # 132 LOAD_FAST                0 (self)
        # 134 LOAD_ATTR                5 (credentials)
        # 144 LOAD_CONST               4 (1)
        # 146 BINARY_SUBSCR
        # 156 PRECALL                  3
        # 160 CALL                     3
        # 170 STORE_FAST               7 (password_digest)
        # 172 LOAD_CONST               5 ('UsernameToken Username="')
        # 730         174 LOAD_FAST                0 (self)
        # 176 LOAD_ATTR                5 (credentials)
        # 186 LOAD_CONST               6 (0)
        # 188 BINARY_SUBSCR
        # 198 FORMAT_VALUE             1 (str)
        # 200 LOAD_CONST               7 ('", PasswordDigest="')
        # 731         202 LOAD_FAST                7 (password_digest)
        # 204 FORMAT_VALUE             1 (str)
        # 206 LOAD_CONST               8 ('", Nonce="')
        # 732         208 LOAD_FAST                6 (cnonce)
        # 210 FORMAT_VALUE             1 (str)
        # 212 LOAD_CONST               9 ('", Created="')
        # 733         214 LOAD_FAST                5 (iso_now)
        # 216 FORMAT_VALUE             1 (str)
        # 218 LOAD_CONST              10 ('"')
        # 729         220 BUILD_STRING             9
        # 222 LOAD_FAST                3 (headers)
        # 224 LOAD_CONST              11 ('X-WSSE')
        # 226 STORE_SUBSCR
        # 230 LOAD_CONST              12 (None)
        # 232 RETURN_VALUE


class GoogleLoginAuthentication:
    """GoogleLoginAuthentication"""
    def __init__(self, credentials, host, request_uri, headers, response, content, http):
        # 738           0 RESUME                   0
        # 739           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (('urlencode',))
        # 6 IMPORT_NAME              0 (urllib.parse)
        # 8 IMPORT_FROM              1 (urlencode)
        # 10 STORE_FAST               8 (urlencode)
        # 12 POP_TOP
        # 741          14 LOAD_GLOBAL              4 (Authentication)
        # 26 LOAD_METHOD              3 (__init__)
        # 48 LOAD_FAST                0 (self)
        # 50 LOAD_FAST                1 (credentials)
        # 52 LOAD_FAST                2 (host)
        # 54 LOAD_FAST                3 (request_uri)
        # 56 LOAD_FAST                4 (headers)
        # 58 LOAD_FAST                5 (response)
        # 60 LOAD_FAST                6 (content)
        # 62 LOAD_FAST                7 (http)
        # 64 PRECALL                  8
        # 68 CALL                     8
        # 78 POP_TOP
        # 742          80 PUSH_NULL
        # 82 LOAD_FAST                9 (auth)
        # 84 LOAD_ATTR                4 (_parse_www_authenticate)
        # 94 LOAD_FAST                5 (response)
        # 96 LOAD_CONST               3 ('www-authenticate')
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 STORE_FAST              10 (challenge)
        # 743         114 LOAD_FAST               10 (challenge)
        # 116 LOAD_CONST               4 ('googlelogin')
        # 118 BINARY_SUBSCR
        # 128 LOAD_METHOD              5 (get)
        # 150 LOAD_CONST               5 ('service')
        # 152 LOAD_CONST               6 ('xapi')
        # 154 PRECALL                  2
        # 158 CALL                     2
        # 168 STORE_FAST              11 (service)
        # 746         170 LOAD_FAST               11 (service)
        # 172 LOAD_CONST               6 ('xapi')
        # 174 COMPARE_OP               2 (==)
        # 180 POP_JUMP_FORWARD_IF_FALSE    27 (to 236)
        # 182 LOAD_FAST                3 (request_uri)
        # 184 LOAD_METHOD              6 (find)
        # 206 LOAD_CONST               7 ('calendar')
        # 208 PRECALL                  1
        # 212 CALL                     1
        # 222 LOAD_CONST               1 (0)
        # 224 COMPARE_OP               4 (>)
        # 230 POP_JUMP_FORWARD_IF_FALSE     2 (to 236)
        # 747         232 LOAD_CONST               8 ('cl')
        # 234 STORE_FAST              11 (service)
        # 752     >>  236 LOAD_GLOBAL             15 (NULL + dict)
        # 248 LOAD_FAST                1 (credentials)
        # 250 LOAD_CONST               1 (0)
        # 252 BINARY_SUBSCR
        # 262 LOAD_FAST                1 (credentials)
        # 264 LOAD_CONST               9 (1)
        # 266 BINARY_SUBSCR
        # 276 LOAD_FAST               11 (service)
        # 278 LOAD_FAST                4 (headers)
        # 280 LOAD_CONST              10 ('user-agent')
        # 282 BINARY_SUBSCR
        # 292 KW_NAMES                11
        # 294 PRECALL                  4
        # 298 CALL                     4
        # 308 STORE_FAST               9 (auth)
        # 753         310 LOAD_FAST                0 (self)
        # 312 LOAD_ATTR                8 (http)
        # 322 LOAD_METHOD              9 (request)
        # 754         344 LOAD_CONST              12 ('https://www.google.com/accounts/ClientLogin')
        # 755         346 LOAD_CONST              13 ('POST')
        # 756         348 PUSH_NULL
        # 350 LOAD_FAST                8 (urlencode)
        # 352 LOAD_FAST                9 (auth)
        # 354 PRECALL                  1
        # 358 CALL                     1
        # 757         368 LOAD_CONST              14 ('Content-Type')
        # 370 LOAD_CONST              15 ('application/x-www-form-urlencoded')
        # 372 BUILD_MAP                1
        # 753         374 KW_NAMES                16
        # 376 PRECALL                  4
        # 380 CALL                     4
        # 390 UNPACK_SEQUENCE          2
        # 394 STORE_FAST              12 (resp)
        # 396 STORE_FAST               6 (content)
        # 759         398 LOAD_FAST                6 (content)
        # 400 LOAD_METHOD             10 (split)
        # 422 LOAD_CONST              17 ('\n')
        # 424 PRECALL                  1
        # 428 CALL                     1
        # 438 STORE_FAST              13 (lines)
        # 760         440 LOAD_GLOBAL             15 (NULL + dict)
        # 452 LOAD_CONST              18 (<code object <listcomp> at 0x000001EBD7DCBBB0, file "httplib2\__init__.py", line 760>)
        # 454 MAKE_FUNCTION            0
        # 456 LOAD_FAST               13 (lines)
        # 458 GET_ITER
        # 460 PRECALL                  0
        # 464 CALL                     0
        # 474 PRECALL                  1
        # 478 CALL                     1
        # 488 STORE_FAST              14 (d)
        # 761         490 LOAD_FAST               12 (resp)
        # 492 LOAD_ATTR               11 (status)
        # 502 LOAD_CONST              19 (403)
        # 504 COMPARE_OP               2 (==)
        # 510 POP_JUMP_FORWARD_IF_FALSE     9 (to 530)
        # 762         512 LOAD_CONST              20 ('')
        # 514 LOAD_FAST                0 (self)
        # 516 STORE_ATTR              12 (Auth)
        # 526 LOAD_CONST               0 (None)
        # 528 RETURN_VALUE
        # 764     >>  530 LOAD_FAST               14 (d)
        # 532 LOAD_CONST              21 ('Auth')
        # 534 BINARY_SUBSCR
        # 544 LOAD_FAST                0 (self)
        # 546 STORE_ATTR              12 (Auth)
        # 556 LOAD_CONST               0 (None)
        # 558 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7DCBBB0, file "httplib2\__init__.py", line 760>:
        # 760           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                39 (to 86)
        # 8 STORE_FAST               1 (line)
        # 10 LOAD_FAST                1 (line)
        # 12 POP_JUMP_BACKWARD_IF_FALSE     4 (to 6)
        # 14 LOAD_GLOBAL              1 (NULL + tuple)
        # 26 LOAD_FAST                1 (line)
        # 28 LOAD_METHOD              1 (split)
        # 50 LOAD_CONST               0 ('=')
        # 52 LOAD_CONST               1 (1)
        # 54 PRECALL                  2
        # 58 CALL                     2
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 LIST_APPEND              2
        # 84 JUMP_BACKWARD           40 (to 6)
        # >>   86 RETURN_VALUE

    def request(self, method, request_uri, headers, content):
        """Modify the request headers to add the appropriate
        Authorization header."""
        # 766           0 RESUME                   0
        # 769           2 LOAD_CONST               1 ('GoogleLogin Auth=')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (Auth)
        # 16 BINARY_OP                0 (+)
        # 20 LOAD_FAST                3 (headers)
        # 22 LOAD_CONST               2 ('authorization')
        # 24 STORE_SUBSCR
        # 28 LOAD_CONST               3 (None)
        # 30 RETURN_VALUE


class FileCache:
    """FileCache"""
    def __init__(self, cache, safe):
        # 789           0 RESUME                   0
        # 790           2 LOAD_FAST                1 (cache)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (cache)
        # 791          16 LOAD_FAST                2 (safe)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (safe)
        # 792          30 LOAD_GLOBAL              4 (os)
        # 42 LOAD_ATTR                3 (path)
        # 52 LOAD_METHOD              4 (exists)
        # 74 LOAD_FAST                1 (cache)
        # 76 PRECALL                  1
        # 80 CALL                     1
        # 90 POP_JUMP_FORWARD_IF_TRUE    27 (to 146)
        # 793          92 LOAD_GLOBAL              5 (NULL + os)
        # 104 LOAD_ATTR                5 (makedirs)
        # 114 LOAD_FAST                0 (self)
        # 116 LOAD_ATTR                0 (cache)
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 POP_TOP
        # 142 LOAD_CONST               0 (None)
        # 144 RETURN_VALUE
        # 792     >>  146 LOAD_CONST               0 (None)
        # 148 RETURN_VALUE

    def get(self, key):
        # 795           0 RESUME                   0
        # 796           2 LOAD_CONST               0 (None)
        # 4 STORE_FAST               2 (retval)
        # 797           6 LOAD_GLOBAL              0 (os)
        # 18 LOAD_ATTR                1 (path)
        # 28 LOAD_METHOD              2 (join)
        # 50 LOAD_FAST                0 (self)
        # 52 LOAD_ATTR                3 (cache)
        # 62 LOAD_FAST                0 (self)
        # 64 LOAD_METHOD              4 (safe)
        # 86 LOAD_FAST                1 (key)
        # 88 PRECALL                  1
        # 92 CALL                     1
        # 102 PRECALL                  2
        # 106 CALL                     2
        # 116 STORE_FAST               3 (cacheFullPath)
        # 798         118 NOP
        # 799         120 LOAD_GLOBAL             11 (NULL + open)
        # 132 LOAD_FAST                3 (cacheFullPath)
        # 134 LOAD_CONST               1 ('rb')
        # 136 PRECALL                  2
        # 140 CALL                     2
        # 150 STORE_FAST               4 (f)
        # 800         152 LOAD_FAST                4 (f)
        # 154 LOAD_METHOD              6 (read)
        # 176 PRECALL                  0
        # 180 CALL                     0
        # 190 STORE_FAST               2 (retval)
        # 801         192 LOAD_FAST                4 (f)
        # 194 LOAD_METHOD              7 (close)
        # 216 PRECALL                  0
        # 220 CALL                     0
        # 230 POP_TOP
        # 232 JUMP_FORWARD            16 (to 266)
        # >>  234 PUSH_EXC_INFO
        # 802         236 LOAD_GLOBAL             16 (IOError)
        # 248 CHECK_EXC_MATCH
        # 250 POP_JUMP_FORWARD_IF_FALSE     3 (to 258)
        # 252 POP_TOP
        # 803         254 POP_EXCEPT
        # 256 JUMP_FORWARD             4 (to 266)
        # 802     >>  258 RERAISE                  0
        # >>  260 COPY                     3
        # 262 POP_EXCEPT
        # 264 RERAISE                  1
        # 804     >>  266 LOAD_FAST                2 (retval)
        # 268 RETURN_VALUE
        # ExceptionTable:
        # 120 to 230 -> 234 [0]
        # 234 to 252 -> 260 [1] lasti
        # 258 to 258 -> 260 [1] lasti

    def set(self, key, value):
        # 806           0 RESUME                   0
        # 807           2 LOAD_GLOBAL              0 (os)
        # 14 LOAD_ATTR                1 (path)
        # 24 LOAD_METHOD              2 (join)
        # 46 LOAD_FAST                0 (self)
        # 48 LOAD_ATTR                3 (cache)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              4 (safe)
        # 82 LOAD_FAST                1 (key)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 STORE_FAST               3 (cacheFullPath)
        # 808         114 LOAD_GLOBAL             11 (NULL + open)
        # 126 LOAD_FAST                3 (cacheFullPath)
        # 128 LOAD_CONST               1 ('wb')
        # 130 PRECALL                  2
        # 134 CALL                     2
        # 144 STORE_FAST               4 (f)
        # 809         146 LOAD_FAST                4 (f)
        # 148 LOAD_METHOD              6 (write)
        # 170 LOAD_FAST                2 (value)
        # 172 PRECALL                  1
        # 176 CALL                     1
        # 186 POP_TOP
        # 810         188 LOAD_FAST                4 (f)
        # 190 LOAD_METHOD              7 (close)
        # 212 PRECALL                  0
        # 216 CALL                     0
        # 226 POP_TOP
        # 228 LOAD_CONST               0 (None)
        # 230 RETURN_VALUE

    def delete(self, key):
        # 812           0 RESUME                   0
        # 813           2 LOAD_GLOBAL              0 (os)
        # 14 LOAD_ATTR                1 (path)
        # 24 LOAD_METHOD              2 (join)
        # 46 LOAD_FAST                0 (self)
        # 48 LOAD_ATTR                3 (cache)
        # 58 LOAD_FAST                0 (self)
        # 60 LOAD_METHOD              4 (safe)
        # 82 LOAD_FAST                1 (key)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 STORE_FAST               2 (cacheFullPath)
        # 814         114 LOAD_GLOBAL              0 (os)
        # 126 LOAD_ATTR                1 (path)
        # 136 LOAD_METHOD              5 (exists)
        # 158 LOAD_FAST                2 (cacheFullPath)
        # 160 PRECALL                  1
        # 164 CALL                     1
        # 174 POP_JUMP_FORWARD_IF_FALSE    22 (to 220)
        # 815         176 LOAD_GLOBAL              1 (NULL + os)
        # 188 LOAD_ATTR                6 (remove)
        # 198 LOAD_FAST                2 (cacheFullPath)
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 POP_TOP
        # 216 LOAD_CONST               0 (None)
        # 218 RETURN_VALUE
        # 814     >>  220 LOAD_CONST               0 (None)
        # 222 RETURN_VALUE


class Credentials:
    """Credentials"""
    def __init__(self):
        # 819           0 RESUME                   0
        # 820           2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (credentials)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def add(self, name, password, domain):
        # 822           0 RESUME                   0
        # 823           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (credentials)
        # 14 LOAD_METHOD              1 (append)
        # 36 LOAD_FAST                3 (domain)
        # 38 LOAD_METHOD              2 (lower)
        # 60 PRECALL                  0
        # 64 CALL                     0
        # 74 LOAD_FAST                1 (name)
        # 76 LOAD_FAST                2 (password)
        # 78 BUILD_TUPLE              3
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 POP_TOP
        # 96 LOAD_CONST               0 (None)
        # 98 RETURN_VALUE

    def clear(self):
        # 825           0 RESUME                   0
        # 826           2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (credentials)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def iter(self, domain):
        # 828           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 829           6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (credentials)
        # 18 GET_ITER
        # >>   20 FOR_ITER                24 (to 70)
        # 22 UNPACK_SEQUENCE          3
        # 26 STORE_FAST               2 (cdomain)
        # 28 STORE_FAST               3 (name)
        # 30 STORE_FAST               4 (password)
        # 830          32 LOAD_FAST                2 (cdomain)
        # 34 LOAD_CONST               1 ('')
        # 36 COMPARE_OP               2 (==)
        # 42 POP_JUMP_FORWARD_IF_TRUE     6 (to 56)
        # 44 LOAD_FAST                1 (domain)
        # 46 LOAD_FAST                2 (cdomain)
        # 48 COMPARE_OP               2 (==)
        # 54 POP_JUMP_FORWARD_IF_FALSE     6 (to 68)
        # 831     >>   56 LOAD_FAST                3 (name)
        # 58 LOAD_FAST                4 (password)
        # 60 BUILD_TUPLE              2
        # 62 YIELD_VALUE
        # 64 RESUME                   1
        # 66 POP_TOP
        # >>   68 JUMP_BACKWARD           25 (to 20)
        # 829     >>   70 LOAD_CONST               0 (None)
        # 72 RETURN_VALUE


class KeyCerts:
    """KeyCerts"""
    def add(self, key, cert, domain, password):
        # 838           0 RESUME                   0
        # 839           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (credentials)
        # 14 LOAD_METHOD              1 (append)
        # 36 LOAD_FAST                3 (domain)
        # 38 LOAD_METHOD              2 (lower)
        # 60 PRECALL                  0
        # 64 CALL                     0
        # 74 LOAD_FAST                1 (key)
        # 76 LOAD_FAST                2 (cert)
        # 78 LOAD_FAST                4 (password)
        # 80 BUILD_TUPLE              4
        # 82 PRECALL                  1
        # 86 CALL                     1
        # 96 POP_TOP
        # 98 LOAD_CONST               0 (None)
        # 100 RETURN_VALUE

    def iter(self, domain):
        # 841           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 842           6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (credentials)
        # 18 GET_ITER
        # >>   20 FOR_ITER                26 (to 74)
        # 22 UNPACK_SEQUENCE          4
        # 26 STORE_FAST               2 (cdomain)
        # 28 STORE_FAST               3 (key)
        # 30 STORE_FAST               4 (cert)
        # 32 STORE_FAST               5 (password)
        # 843          34 LOAD_FAST                2 (cdomain)
        # 36 LOAD_CONST               1 ('')
        # 38 COMPARE_OP               2 (==)
        # 44 POP_JUMP_FORWARD_IF_TRUE     6 (to 58)
        # 46 LOAD_FAST                1 (domain)
        # 48 LOAD_FAST                2 (cdomain)
        # 50 COMPARE_OP               2 (==)
        # 56 POP_JUMP_FORWARD_IF_FALSE     7 (to 72)
        # 844     >>   58 LOAD_FAST                3 (key)
        # 60 LOAD_FAST                4 (cert)
        # 62 LOAD_FAST                5 (password)
        # 64 BUILD_TUPLE              3
        # 66 YIELD_VALUE
        # 68 RESUME                   1
        # 70 POP_TOP
        # >>   72 JUMP_BACKWARD           27 (to 20)
        # 842     >>   74 LOAD_CONST               0 (None)
        # 76 RETURN_VALUE


class AllHosts:
    """AllHosts"""

class ProxyInfo:
    """ProxyInfo"""
    def __init__(self, proxy_type, proxy_host, proxy_port, proxy_rdns, proxy_user, proxy_pass, proxy_headers):
        """Args:

          proxy_type: The type of proxy server.  This must be set to one of
          socks.PROXY_TYPE_XXX constants.  For example:  p =
          ProxyInfo(proxy_type=socks.PROXY_TYPE_HTTP, proxy_host='localhost',
          proxy_port=8000)
          proxy_host: The hostname or IP address of the proxy server.
          proxy_port: The port that the proxy server is running on.
          proxy_rdns: If True (default), DNS queries will not be performed
          locally, and instead, handed to the proxy to resolve.  This is useful
          if the network does not allow resolution of non-local names. In
          httplib2 0.9 and earlier, this defaulted to False.
          proxy_user: The username used to authenticate with the proxy server.
          proxy_pass: The password used to authenticate with the proxy server.
          proxy_headers: Additional or modified headers for the proxy connect
          request.
        """
        # 856           0 RESUME                   0
        # 876           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                5 (proxy_user)
        # 16 LOAD_GLOBAL              2 (bytes)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_FALSE    20 (to 84)
        # 877          44 LOAD_FAST                5 (proxy_user)
        # 46 LOAD_METHOD              2 (decode)
        # 68 PRECALL                  0
        # 72 CALL                     0
        # 82 STORE_FAST               5 (proxy_user)
        # 878     >>   84 LOAD_GLOBAL              1 (NULL + isinstance)
        # 96 LOAD_FAST                6 (proxy_pass)
        # 98 LOAD_GLOBAL              2 (bytes)
        # 110 PRECALL                  2
        # 114 CALL                     2
        # 124 POP_JUMP_FORWARD_IF_FALSE    20 (to 166)
        # 879         126 LOAD_FAST                6 (proxy_pass)
        # 128 LOAD_METHOD              2 (decode)
        # 150 PRECALL                  0
        # 154 CALL                     0
        # 164 STORE_FAST               6 (proxy_pass)
        # 889     >>  166 LOAD_FAST                1 (proxy_type)
        # 890         168 LOAD_FAST                2 (proxy_host)
        # 891         170 LOAD_FAST                3 (proxy_port)
        # 892         172 LOAD_FAST                4 (proxy_rdns)
        # 893         174 LOAD_FAST                5 (proxy_user)
        # 894         176 LOAD_FAST                6 (proxy_pass)
        # 895         178 LOAD_FAST                7 (proxy_headers)
        # 888         180 BUILD_TUPLE              7
        # 880         182 UNPACK_SEQUENCE          7
        # 881         186 LOAD_FAST                0 (self)
        # 188 STORE_ATTR               3 (proxy_type)
        # 882         198 LOAD_FAST                0 (self)
        # 200 STORE_ATTR               4 (proxy_host)
        # 883         210 LOAD_FAST                0 (self)
        # 212 STORE_ATTR               5 (proxy_port)
        # 884         222 LOAD_FAST                0 (self)
        # 224 STORE_ATTR               6 (proxy_rdns)
        # 885         234 LOAD_FAST                0 (self)
        # 236 STORE_ATTR               7 (proxy_user)
        # 886         246 LOAD_FAST                0 (self)
        # 248 STORE_ATTR               8 (proxy_pass)
        # 887         258 LOAD_FAST                0 (self)
        # 260 STORE_ATTR               9 (proxy_headers)
        # 270 LOAD_CONST               1 (None)
        # 272 RETURN_VALUE

    def astuple(self):
        # 898           0 RESUME                   0
        # 900           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (proxy_type)
        # 901          14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (proxy_host)
        # 902          26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (proxy_port)
        # 903          38 LOAD_FAST                0 (self)
        # 40 LOAD_ATTR                3 (proxy_rdns)
        # 904          50 LOAD_FAST                0 (self)
        # 52 LOAD_ATTR                4 (proxy_user)
        # 905          62 LOAD_FAST                0 (self)
        # 64 LOAD_ATTR                5 (proxy_pass)
        # 906          74 LOAD_FAST                0 (self)
        # 76 LOAD_ATTR                6 (proxy_headers)
        # 899          86 BUILD_TUPLE              7
        # 88 RETURN_VALUE

    def isgood(self):
        # 909           0 RESUME                   0
        # 910           2 LOAD_GLOBAL              0 (socks)
        # 14 JUMP_IF_FALSE_OR_POP    21 (to 58)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                1 (proxy_host)
        # 28 LOAD_CONST               0 (None)
        # 30 COMPARE_OP               3 (!=)
        # 36 JUMP_IF_FALSE_OR_POP    10 (to 58)
        # 38 LOAD_FAST                0 (self)
        # 40 LOAD_ATTR                2 (proxy_port)
        # 50 LOAD_CONST               0 (None)
        # 52 COMPARE_OP               3 (!=)
        # >>   58 RETURN_VALUE

    def applies_to(self, hostname):
        # 912           0 RESUME                   0
        # 913           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (bypass_host)
        # 26 LOAD_FAST                1 (hostname)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 UNARY_NOT
        # 44 RETURN_VALUE

    def bypass_host(self, hostname):
        """Has this host been excluded from the proxy config"""
        # 915           0 RESUME                   0
        # 917           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (bypass_hosts)
        # 14 LOAD_GLOBAL              2 (AllHosts)
        # 26 IS_OP                    0
        # 28 POP_JUMP_FORWARD_IF_FALSE     2 (to 34)
        # 918          30 LOAD_CONST               1 (True)
        # 32 RETURN_VALUE
        # 920     >>   34 LOAD_CONST               2 ('.')
        # 36 LOAD_FAST                1 (hostname)
        # 38 LOAD_METHOD              2 (lstrip)
        # 60 LOAD_CONST               2 ('.')
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 BINARY_OP                0 (+)
        # 80 STORE_FAST               1 (hostname)
        # 921          82 LOAD_FAST                0 (self)
        # 84 LOAD_ATTR                0 (bypass_hosts)
        # 94 GET_ITER
        # >>   96 FOR_ITER                59 (to 216)
        # 98 STORE_FAST               2 (skip_name)
        # 923         100 LOAD_FAST                2 (skip_name)
        # 102 LOAD_METHOD              3 (startswith)
        # 124 LOAD_CONST               2 ('.')
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 POP_JUMP_FORWARD_IF_FALSE    24 (to 190)
        # 142 LOAD_FAST                1 (hostname)
        # 144 LOAD_METHOD              4 (endswith)
        # 166 LOAD_FAST                2 (skip_name)
        # 168 PRECALL                  1
        # 172 CALL                     1
        # 182 POP_JUMP_FORWARD_IF_FALSE     3 (to 190)
        # 924         184 POP_TOP
        # 186 LOAD_CONST               1 (True)
        # 188 RETURN_VALUE
        # 926     >>  190 LOAD_FAST                1 (hostname)
        # 192 LOAD_CONST               2 ('.')
        # 194 LOAD_FAST                2 (skip_name)
        # 196 BINARY_OP                0 (+)
        # 200 COMPARE_OP               2 (==)
        # 206 POP_JUMP_FORWARD_IF_FALSE     3 (to 214)
        # 927         208 POP_TOP
        # 210 LOAD_CONST               1 (True)
        # 212 RETURN_VALUE
        # 926     >>  214 JUMP_BACKWARD           60 (to 96)
        # 928     >>  216 LOAD_CONST               3 (False)
        # 218 RETURN_VALUE

    def __repr__(self):
        # 930           0 RESUME                   0
        # 932           2 LOAD_CONST               1 ('<ProxyInfo type={p.proxy_type} host:port={p.proxy_host}:{p.proxy_port} rdns={p.proxy_rdns} user={p.proxy_user} headers={p.proxy_headers}>')
        # 935           4 LOAD_METHOD              0 (format)
        # 26 LOAD_FAST                0 (self)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 931          44 RETURN_VALUE


def proxy_info_from_environment(method):
    """Read proxy info from the environment variables.
    """
    # 938           0 RESUME                   0
    # 941           2 LOAD_FAST                0 (method)
    # 4 LOAD_CONST               1 (('http', 'https'))
    # 6 CONTAINS_OP              1
    # 8 POP_JUMP_FORWARD_IF_FALSE     2 (to 14)
    # 942          10 LOAD_CONST               2 (None)
    # 12 RETURN_VALUE
    # 944     >>   14 LOAD_FAST                0 (method)
    # 16 LOAD_CONST               3 ('_proxy')
    # 18 BINARY_OP                0 (+)
    # 22 STORE_FAST               1 (env_var)
    # 945          24 LOAD_GLOBAL              0 (os)
    # 36 LOAD_ATTR                1 (environ)
    # 46 LOAD_METHOD              2 (get)
    # 68 LOAD_FAST                1 (env_var)
    # 70 LOAD_GLOBAL              0 (os)
    # 82 LOAD_ATTR                1 (environ)
    # 92 LOAD_METHOD              2 (get)
    # 114 LOAD_FAST                1 (env_var)
    # 116 LOAD_METHOD              3 (upper)
    # 138 PRECALL                  0
    # 142 CALL                     0
    # 152 PRECALL                  1
    # 156 CALL                     1
    # 166 PRECALL                  2
    # 170 CALL                     2
    # 180 STORE_FAST               2 (url)
    # 946         182 LOAD_FAST                2 (url)
    # 184 POP_JUMP_FORWARD_IF_TRUE     2 (to 190)
    # 947         186 LOAD_CONST               2 (None)
    # 188 RETURN_VALUE
    # 948     >>  190 LOAD_GLOBAL              9 (NULL + proxy_info_from_url)
    # 202 LOAD_FAST                2 (url)
    # 204 LOAD_FAST                0 (method)
    # 206 LOAD_CONST               2 (None)
    # 208 KW_NAMES                 4
    # 210 PRECALL                  3
    # 214 CALL                     3
    # 224 RETURN_VALUE

def proxy_info_from_url(url, method, noproxy):
    """Construct a ProxyInfo from a URL (such as http_proxy env var)
    """
    # 951           0 RESUME                   0
    # 954           2 LOAD_GLOBAL              0 (urllib)
    # 14 LOAD_ATTR                1 (parse)
    # 24 LOAD_METHOD              2 (urlparse)
    # 46 LOAD_FAST                0 (url)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               0 (url)
    # 956          64 LOAD_CONST               1 (3)
    # 66 STORE_FAST               3 (proxy_type)
    # 957          68 LOAD_FAST                0 (url)
    # 70 LOAD_ATTR                3 (scheme)
    # 80 LOAD_CONST               2 ('socks4')
    # 82 COMPARE_OP               2 (==)
    # 88 POP_JUMP_FORWARD_IF_FALSE     3 (to 96)
    # 958          90 LOAD_CONST               3 (1)
    # 92 STORE_FAST               3 (proxy_type)
    # 94 JUMP_FORWARD            24 (to 144)
    # 959     >>   96 LOAD_FAST                0 (url)
    # 98 LOAD_ATTR                3 (scheme)
    # 108 LOAD_CONST               4 ('socks5')
    # 110 COMPARE_OP               2 (==)
    # 116 POP_JUMP_FORWARD_IF_TRUE    11 (to 140)
    # 118 LOAD_FAST                0 (url)
    # 120 LOAD_ATTR                3 (scheme)
    # 130 LOAD_CONST               5 ('socks')
    # 132 COMPARE_OP               2 (==)
    # 138 POP_JUMP_FORWARD_IF_FALSE     2 (to 144)
    # 960     >>  140 LOAD_CONST               6 (2)
    # 142 STORE_FAST               3 (proxy_type)
    # 961     >>  144 LOAD_GLOBAL              9 (NULL + ProxyInfo)
    # 962         156 LOAD_FAST                3 (proxy_type)
    # 963         158 LOAD_FAST                0 (url)
    # 160 LOAD_ATTR                5 (hostname)
    # 964         170 LOAD_FAST                0 (url)
    # 172 LOAD_ATTR                6 (port)
    # 182 JUMP_IF_TRUE_OR_POP     22 (to 228)
    # 184 LOAD_GLOBAL             15 (NULL + dict)
    # 196 LOAD_CONST               7 (443)
    # 198 LOAD_CONST               8 (80)
    # 200 KW_NAMES                 9
    # 202 PRECALL                  2
    # 206 CALL                     2
    # 216 LOAD_FAST                1 (method)
    # 218 BINARY_SUBSCR
    # 965     >>  228 LOAD_FAST                0 (url)
    # 230 LOAD_ATTR                8 (username)
    # 240 JUMP_IF_TRUE_OR_POP      1 (to 244)
    # 242 LOAD_CONST              10 (None)
    # 966     >>  244 LOAD_FAST                0 (url)
    # 246 LOAD_ATTR                9 (password)
    # 256 JUMP_IF_TRUE_OR_POP      1 (to 260)
    # 258 LOAD_CONST              10 (None)
    # 967     >>  260 LOAD_CONST              10 (None)
    # 961         262 KW_NAMES                11
    # 264 PRECALL                  6
    # 268 CALL                     6
    # 278 STORE_FAST               4 (pi)
    # 970         280 BUILD_LIST               0
    # 282 STORE_FAST               5 (bypass_hosts)
    # 972         284 LOAD_FAST                2 (noproxy)
    # 286 POP_JUMP_FORWARD_IF_NOT_NONE    62 (to 412)
    # 973         288 LOAD_GLOBAL             20 (os)
    # 300 LOAD_ATTR               11 (environ)
    # 310 LOAD_METHOD             12 (get)
    # 332 LOAD_CONST              12 ('no_proxy')
    # 334 LOAD_GLOBAL             20 (os)
    # 346 LOAD_ATTR               11 (environ)
    # 356 LOAD_METHOD             12 (get)
    # 378 LOAD_CONST              13 ('NO_PROXY')
    # 380 LOAD_CONST              14 ('')
    # 382 PRECALL                  2
    # 386 CALL                     2
    # 396 PRECALL                  2
    # 400 CALL                     2
    # 410 STORE_FAST               2 (noproxy)
    # 975     >>  412 LOAD_FAST                2 (noproxy)
    # 414 LOAD_CONST              15 ('*')
    # 416 COMPARE_OP               2 (==)
    # 422 POP_JUMP_FORWARD_IF_FALSE     8 (to 440)
    # 976         424 LOAD_GLOBAL             26 (AllHosts)
    # 436 STORE_FAST               5 (bypass_hosts)
    # 438 JUMP_FORWARD            75 (to 590)
    # 977     >>  440 LOAD_FAST                2 (noproxy)
    # 442 LOAD_METHOD             14 (strip)
    # 464 PRECALL                  0
    # 468 CALL                     0
    # 478 POP_JUMP_FORWARD_IF_FALSE    55 (to 590)
    # 978         480 LOAD_FAST                2 (noproxy)
    # 482 LOAD_METHOD             15 (split)
    # 504 LOAD_CONST              16 (',')
    # 506 PRECALL                  1
    # 510 CALL                     1
    # 520 STORE_FAST               5 (bypass_hosts)
    # 979         522 LOAD_GLOBAL             33 (NULL + tuple)
    # 534 LOAD_GLOBAL             35 (NULL + filter)
    # 546 LOAD_GLOBAL             36 (bool)
    # 558 LOAD_FAST                5 (bypass_hosts)
    # 560 PRECALL                  2
    # 564 CALL                     2
    # 574 PRECALL                  1
    # 578 CALL                     1
    # 588 STORE_FAST               5 (bypass_hosts)
    # 981     >>  590 LOAD_FAST                5 (bypass_hosts)
    # 592 LOAD_FAST                4 (pi)
    # 594 STORE_ATTR              19 (bypass_hosts)
    # 982         604 LOAD_FAST                4 (pi)
    # 606 RETURN_VALUE

class HTTPConnectionWithTimeout:
    """HTTPConnectionWithTimeout"""
    def __init__(self, host, port, timeout, proxy_info):
        # 996           0 RESUME                   0
        # 997           2 LOAD_GLOBAL              0 (http)
        # 14 LOAD_ATTR                1 (client)
        # 24 LOAD_ATTR                2 (HTTPConnection)
        # 34 LOAD_METHOD              3 (__init__)
        # 56 LOAD_FAST                0 (self)
        # 58 LOAD_FAST                1 (host)
        # 60 LOAD_FAST                2 (port)
        # 62 LOAD_FAST                3 (timeout)
        # 64 KW_NAMES                 1
        # 66 PRECALL                  4
        # 70 CALL                     4
        # 80 POP_TOP
        # 999          82 LOAD_FAST                4 (proxy_info)
        # 84 LOAD_FAST                0 (self)
        # 86 STORE_ATTR               4 (proxy_info)
        # 1000          96 LOAD_FAST                4 (proxy_info)
        # 98 POP_JUMP_FORWARD_IF_FALSE    39 (to 178)
        # 100 LOAD_GLOBAL             11 (NULL + isinstance)
        # 112 LOAD_FAST                4 (proxy_info)
        # 114 LOAD_GLOBAL             12 (ProxyInfo)
        # 126 PRECALL                  2
        # 130 CALL                     2
        # 140 POP_JUMP_FORWARD_IF_TRUE    20 (to 182)
        # 1001         142 PUSH_NULL
        # 144 LOAD_FAST                4 (proxy_info)
        # 146 LOAD_CONST               2 ('http')
        # 148 PRECALL                  1
        # 152 CALL                     1
        # 162 LOAD_FAST                0 (self)
        # 164 STORE_ATTR               4 (proxy_info)
        # 174 LOAD_CONST               0 (None)
        # 176 RETURN_VALUE
        # 1000     >>  178 LOAD_CONST               0 (None)
        # 180 RETURN_VALUE
        # >>  182 LOAD_CONST               0 (None)
        # 184 RETURN_VALUE

    def connect(self):
        """Connect to the host and port specified in __init__."""
        # 1003           0 RESUME                   0
        # 1005           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (proxy_info)
        # 14 POP_JUMP_FORWARD_IF_FALSE    22 (to 60)
        # 16 LOAD_GLOBAL              2 (socks)
        # 28 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 60)
        # 1006          30 LOAD_GLOBAL              5 (NULL + ProxiesUnavailableError)
        # 42 LOAD_CONST               2 ('Proxy support missing but proxy use was requested!')
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 RAISE_VARARGS            1
        # 1007     >>   60 LOAD_FAST                0 (self)
        # 62 LOAD_ATTR                0 (proxy_info)
        # 72 POP_JUMP_FORWARD_IF_FALSE    96 (to 266)
        # 74 LOAD_FAST                0 (self)
        # 76 LOAD_ATTR                0 (proxy_info)
        # 86 LOAD_METHOD              3 (isgood)
        # 108 PRECALL                  0
        # 112 CALL                     0
        # 122 POP_JUMP_FORWARD_IF_FALSE    71 (to 266)
        # 124 LOAD_FAST                0 (self)
        # 126 LOAD_ATTR                0 (proxy_info)
        # 136 LOAD_METHOD              4 (applies_to)
        # 158 LOAD_FAST                0 (self)
        # 160 LOAD_ATTR                5 (host)
        # 170 PRECALL                  1
        # 174 CALL                     1
        # 184 POP_JUMP_FORWARD_IF_FALSE    40 (to 266)
        # 1008         186 LOAD_CONST               3 (True)
        # 188 STORE_FAST               1 (use_proxy)
        # 1017         190 LOAD_FAST                0 (self)
        # 192 LOAD_ATTR                0 (proxy_info)
        # 202 LOAD_METHOD              6 (astuple)
        # 224 PRECALL                  0
        # 228 CALL                     0
        # 1009         238 UNPACK_SEQUENCE          7
        # 1010         242 STORE_FAST               2 (proxy_type)
        # 1011         244 STORE_FAST               3 (proxy_host)
        # 1012         246 STORE_FAST               4 (proxy_port)
        # 1013         248 STORE_FAST               5 (proxy_rdns)
        # 1014         250 STORE_FAST               6 (proxy_user)
        # 1015         252 STORE_FAST               7 (proxy_pass)
        # 1016         254 STORE_FAST               8 (proxy_headers)
        # 1019         256 LOAD_FAST                3 (proxy_host)
        # 258 STORE_FAST               9 (host)
        # 1020         260 LOAD_FAST                4 (proxy_port)
        # 262 STORE_FAST              10 (port)
        # 264 JUMP_FORWARD            18 (to 302)
        # 1022     >>  266 LOAD_CONST               4 (False)
        # 268 STORE_FAST               1 (use_proxy)
        # 1024         270 LOAD_FAST                0 (self)
        # 272 LOAD_ATTR                5 (host)
        # 282 STORE_FAST               9 (host)
        # 1025         284 LOAD_FAST                0 (self)
        # 286 LOAD_ATTR                7 (port)
        # 296 STORE_FAST              10 (port)
        # 1026         298 LOAD_CONST               1 (None)
        # 300 STORE_FAST               2 (proxy_type)
        # 1028     >>  302 LOAD_CONST               1 (None)
        # 304 STORE_FAST              11 (socket_err)
        # 1030         306 LOAD_GLOBAL             17 (NULL + socket)
        # 318 LOAD_ATTR                9 (getaddrinfo)
        # 328 LOAD_FAST                9 (host)
        # 330 LOAD_FAST               10 (port)
        # 332 LOAD_CONST               5 (0)
        # 334 LOAD_GLOBAL             16 (socket)
        # 346 LOAD_ATTR               10 (SOCK_STREAM)
        # 356 PRECALL                  4
        # 360 CALL                     4
        # 370 GET_ITER
        # >>  372 EXTENDED_ARG             2
        # 374 FOR_ITER               540 (to 1456)
        # 376 STORE_FAST              12 (res)
        # 1031         378 LOAD_FAST               12 (res)
        # 380 UNPACK_SEQUENCE          5
        # 384 STORE_FAST              13 (af)
        # 386 STORE_FAST              14 (socktype)
        # 388 STORE_FAST              15 (proto)
        # 390 STORE_FAST              16 (canonname)
        # 392 STORE_FAST              17 (sa)
        # 1032         394 NOP
        # 1033         396 LOAD_FAST                1 (use_proxy)
        # 398 POP_JUMP_FORWARD_IF_FALSE    59 (to 518)
        # 1034         400 LOAD_GLOBAL              3 (NULL + socks)
        # 412 LOAD_ATTR               11 (socksocket)
        # 422 LOAD_FAST               13 (af)
        # 424 LOAD_FAST               14 (socktype)
        # 426 LOAD_FAST               15 (proto)
        # 428 PRECALL                  3
        # 432 CALL                     3
        # 442 LOAD_FAST                0 (self)
        # 444 STORE_ATTR              12 (sock)
        # 1035         454 LOAD_FAST                0 (self)
        # 456 LOAD_ATTR               12 (sock)
        # 466 LOAD_METHOD             13 (setproxy)
        # 1036         488 LOAD_FAST                2 (proxy_type)
        # 490 LOAD_FAST                3 (proxy_host)
        # 492 LOAD_FAST                4 (proxy_port)
        # 494 LOAD_FAST                5 (proxy_rdns)
        # 496 LOAD_FAST                6 (proxy_user)
        # 498 LOAD_FAST                7 (proxy_pass)
        # 1035         500 PRECALL                  6
        # 504 CALL                     6
        # 514 POP_TOP
        # 516 JUMP_FORWARD            75 (to 668)
        # 1039     >>  518 LOAD_GLOBAL             17 (NULL + socket)
        # 530 LOAD_ATTR                8 (socket)
        # 540 LOAD_FAST               13 (af)
        # 542 LOAD_FAST               14 (socktype)
        # 544 LOAD_FAST               15 (proto)
        # 546 PRECALL                  3
        # 550 CALL                     3
        # 560 LOAD_FAST                0 (self)
        # 562 STORE_ATTR              12 (sock)
        # 1040         572 LOAD_FAST                0 (self)
        # 574 LOAD_ATTR               12 (sock)
        # 584 LOAD_METHOD             14 (setsockopt)
        # 606 LOAD_GLOBAL             16 (socket)
        # 618 LOAD_ATTR               15 (IPPROTO_TCP)
        # 628 LOAD_GLOBAL             16 (socket)
        # 640 LOAD_ATTR               16 (TCP_NODELAY)
        # 650 LOAD_CONST               6 (1)
        # 652 PRECALL                  3
        # 656 CALL                     3
        # 666 POP_TOP
        # 1041     >>  668 LOAD_GLOBAL             35 (NULL + has_timeout)
        # 680 LOAD_FAST                0 (self)
        # 682 LOAD_ATTR               18 (timeout)
        # 692 PRECALL                  1
        # 696 CALL                     1
        # 706 POP_JUMP_FORWARD_IF_FALSE    31 (to 770)
        # 1042         708 LOAD_FAST                0 (self)
        # 710 LOAD_ATTR               12 (sock)
        # 720 LOAD_METHOD             19 (settimeout)
        # 742 LOAD_FAST                0 (self)
        # 744 LOAD_ATTR               18 (timeout)
        # 754 PRECALL                  1
        # 758 CALL                     1
        # 768 POP_TOP
        # 1043     >>  770 LOAD_FAST                0 (self)
        # 772 LOAD_ATTR               20 (debuglevel)
        # 782 LOAD_CONST               5 (0)
        # 784 COMPARE_OP               4 (>)
        # 790 POP_JUMP_FORWARD_IF_FALSE   100 (to 992)
        # 1044         792 LOAD_GLOBAL             43 (NULL + print)
        # 804 LOAD_CONST               7 ('connect: ({0}, {1}) ************')
        # 806 LOAD_METHOD             22 (format)
        # 828 LOAD_FAST                0 (self)
        # 830 LOAD_ATTR                5 (host)
        # 840 LOAD_FAST                0 (self)
        # 842 LOAD_ATTR                7 (port)
        # 852 PRECALL                  2
        # 856 CALL                     2
        # 866 PRECALL                  1
        # 870 CALL                     1
        # 880 POP_TOP
        # 1045         882 LOAD_FAST                1 (use_proxy)
        # 884 POP_JUMP_FORWARD_IF_FALSE    53 (to 992)
        # 1046         886 LOAD_GLOBAL             43 (NULL + print)
        # 1047         898 LOAD_CONST               8 ('proxy: {0} ************')
        # 900 LOAD_METHOD             22 (format)
        # 1048         922 LOAD_GLOBAL             47 (NULL + str)
        # 934 LOAD_FAST                3 (proxy_host)
        # 936 LOAD_FAST                4 (proxy_port)
        # 938 LOAD_FAST                5 (proxy_rdns)
        # 940 LOAD_FAST                6 (proxy_user)
        # 942 LOAD_FAST                7 (proxy_pass)
        # 944 LOAD_FAST                8 (proxy_headers)
        # 946 BUILD_TUPLE              6
        # 948 PRECALL                  1
        # 952 CALL                     1
        # 1047         962 PRECALL                  1
        # 966 CALL                     1
        # 1046         976 PRECALL                  1
        # 980 CALL                     1
        # 990 POP_TOP
        # 1052     >>  992 LOAD_FAST                0 (self)
        # 994 LOAD_ATTR               12 (sock)
        # 1004 LOAD_METHOD             24 (connect)
        # 1026 LOAD_FAST                0 (self)
        # 1028 LOAD_ATTR                5 (host)
        # 1038 LOAD_FAST                0 (self)
        # 1040 LOAD_ATTR                7 (port)
        # 1050 BUILD_TUPLE              2
        # 1052 LOAD_FAST               17 (sa)
        # 1054 LOAD_CONST               9 (2)
        # 1056 LOAD_CONST               1 (None)
        # 1058 BUILD_SLICE              2
        # 1060 BINARY_SUBSCR
        # 1070 BINARY_OP                0 (+)
        # 1074 PRECALL                  1
        # 1078 CALL                     1
        # 1088 POP_TOP
        # 1090 JUMP_FORWARD           181 (to 1454)
        # >> 1092 PUSH_EXC_INFO
        # 1053        1094 LOAD_GLOBAL             16 (socket)
        # 1106 LOAD_ATTR               25 (error)
        # 1116 CHECK_EXC_MATCH
        # 1118 POP_JUMP_FORWARD_IF_FALSE   163 (to 1446)
        # 1120 STORE_FAST              18 (e)
        # 1054        1122 LOAD_FAST               18 (e)
        # 1124 STORE_FAST              11 (socket_err)
        # 1055        1126 LOAD_FAST                0 (self)
        # 1128 LOAD_ATTR               20 (debuglevel)
        # 1138 LOAD_CONST               5 (0)
        # 1140 COMPARE_OP               4 (>)
        # 1146 POP_JUMP_FORWARD_IF_FALSE   100 (to 1348)
        # 1056        1148 LOAD_GLOBAL             43 (NULL + print)
        # 1160 LOAD_CONST              10 ('connect fail: ({0}, {1})')
        # 1162 LOAD_METHOD             22 (format)
        # 1184 LOAD_FAST                0 (self)
        # 1186 LOAD_ATTR                5 (host)
        # 1196 LOAD_FAST                0 (self)
        # 1198 LOAD_ATTR                7 (port)
        # 1208 PRECALL                  2
        # 1212 CALL                     2
        # 1222 PRECALL                  1
        # 1226 CALL                     1
        # 1236 POP_TOP
        # 1057        1238 LOAD_FAST                1 (use_proxy)
        # 1240 POP_JUMP_FORWARD_IF_FALSE    53 (to 1348)
        # 1058        1242 LOAD_GLOBAL             43 (NULL + print)
        # 1059        1254 LOAD_CONST              11 ('proxy: {0}')
        # 1256 LOAD_METHOD             22 (format)
        # 1060        1278 LOAD_GLOBAL             47 (NULL + str)
        # 1290 LOAD_FAST                3 (proxy_host)
        # 1292 LOAD_FAST                4 (proxy_port)
        # 1294 LOAD_FAST                5 (proxy_rdns)
        # 1296 LOAD_FAST                6 (proxy_user)
        # 1298 LOAD_FAST                7 (proxy_pass)
        # 1300 LOAD_FAST                8 (proxy_headers)
        # 1302 BUILD_TUPLE              6
        # 1304 PRECALL                  1
        # 1308 CALL                     1
        # 1059        1318 PRECALL                  1
        # 1322 CALL                     1
        # 1058        1332 PRECALL                  1
        # 1336 CALL                     1
        # 1346 POP_TOP
        # 1063     >> 1348 LOAD_FAST                0 (self)
        # 1350 LOAD_ATTR               12 (sock)
        # 1360 POP_JUMP_FORWARD_IF_FALSE    25 (to 1412)
        # 1064        1362 LOAD_FAST                0 (self)
        # 1364 LOAD_ATTR               12 (sock)
        # 1374 LOAD_METHOD             26 (close)
        # 1396 PRECALL                  0
        # 1400 CALL                     0
        # 1410 POP_TOP
        # 1065     >> 1412 LOAD_CONST               1 (None)
        # 1414 LOAD_FAST                0 (self)
        # 1416 STORE_ATTR              12 (sock)
        # 1066        1426 POP_EXCEPT
        # 1428 LOAD_CONST               1 (None)
        # 1430 STORE_FAST              18 (e)
        # 1432 DELETE_FAST             18 (e)
        # 1434 EXTENDED_ARG             2
        # 1436 JUMP_BACKWARD          533 (to 372)
        # >> 1438 LOAD_CONST               1 (None)
        # 1440 STORE_FAST              18 (e)
        # 1442 DELETE_FAST             18 (e)
        # 1444 RERAISE                  1
        # 1053     >> 1446 RERAISE                  0
        # >> 1448 COPY                     3
        # 1450 POP_EXCEPT
        # 1452 RERAISE                  1
        # 1067     >> 1454 POP_TOP
        # 1068     >> 1456 LOAD_FAST                0 (self)
        # 1458 LOAD_ATTR               12 (sock)
        # 1468 POP_JUMP_FORWARD_IF_TRUE     2 (to 1474)
        # 1069        1470 LOAD_FAST               11 (socket_err)
        # 1472 RAISE_VARARGS            1
        # 1068     >> 1474 LOAD_CONST               1 (None)
        # 1476 RETURN_VALUE
        # ExceptionTable:
        # 396 to 1088 -> 1092 [1]
        # 1092 to 1120 -> 1448 [2] lasti
        # 1122 to 1424 -> 1438 [2] lasti
        # 1438 to 1446 -> 1448 [2] lasti


class HTTPSConnectionWithTimeout:
    """HTTPSConnectionWithTimeout"""
    def __init__(self, host, port, key_file, cert_file, timeout, proxy_info, ca_certs, disable_ssl_certificate_validation, tls_maximum_version, tls_minimum_version, key_password):
        # 0 COPY_FREE_VARS           1
        # 1081           2 RESUME                   0
        # 1096           4 LOAD_FAST                8 (disable_ssl_certificate_validation)
        # 6 LOAD_FAST                0 (self)
        # 8 STORE_ATTR               0 (disable_ssl_certificate_validation)
        # 1097          18 LOAD_FAST                7 (ca_certs)
        # 20 POP_JUMP_FORWARD_IF_FALSE     2 (to 26)
        # 22 LOAD_FAST                7 (ca_certs)
        # 24 JUMP_FORWARD             6 (to 38)
        # >>   26 LOAD_GLOBAL              2 (CA_CERTS)
        # >>   38 LOAD_FAST                0 (self)
        # 40 STORE_ATTR               2 (ca_certs)
        # 1099          50 LOAD_FAST                6 (proxy_info)
        # 52 LOAD_FAST                0 (self)
        # 54 STORE_ATTR               3 (proxy_info)
        # 1100          64 LOAD_FAST                6 (proxy_info)
        # 66 POP_JUMP_FORWARD_IF_FALSE    37 (to 142)
        # 68 LOAD_GLOBAL              9 (NULL + isinstance)
        # 80 LOAD_FAST                6 (proxy_info)
        # 82 LOAD_GLOBAL             10 (ProxyInfo)
        # 94 PRECALL                  2
        # 98 CALL                     2
        # 108 POP_JUMP_FORWARD_IF_TRUE    16 (to 142)
        # 1101         110 PUSH_NULL
        # 112 LOAD_FAST                6 (proxy_info)
        # 114 LOAD_CONST               1 ('https')
        # 116 PRECALL                  1
        # 120 CALL                     1
        # 130 LOAD_FAST                0 (self)
        # 132 STORE_ATTR               3 (proxy_info)
        # 1103     >>  142 LOAD_GLOBAL             13 (NULL + _build_ssl_context)
        # 1104         154 LOAD_FAST                0 (self)
        # 156 LOAD_ATTR                0 (disable_ssl_certificate_validation)
        # 1105         166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                2 (ca_certs)
        # 1106         178 LOAD_FAST                4 (cert_file)
        # 1107         180 LOAD_FAST                3 (key_file)
        # 1108         182 LOAD_FAST                9 (tls_maximum_version)
        # 1109         184 LOAD_FAST               10 (tls_minimum_version)
        # 1110         186 LOAD_FAST               11 (key_password)
        # 1103         188 KW_NAMES                 2
        # 190 PRECALL                  7
        # 194 CALL                     7
        # 204 STORE_FAST              12 (context)
        # 1112         206 LOAD_GLOBAL             15 (NULL + super)
        # 218 LOAD_GLOBAL             16 (HTTPSConnectionWithTimeout)
        # 230 LOAD_FAST                0 (self)
        # 232 PRECALL                  2
        # 236 CALL                     2
        # 246 LOAD_METHOD              9 (__init__)
        # 1113         268 LOAD_FAST                1 (host)
        # 270 LOAD_FAST                2 (port)
        # 272 LOAD_FAST                5 (timeout)
        # 274 LOAD_FAST               12 (context)
        # 1112         276 KW_NAMES                 3
        # 278 PRECALL                  4
        # 282 CALL                     4
        # 292 POP_TOP
        # 1115         294 LOAD_FAST                3 (key_file)
        # 296 LOAD_FAST                0 (self)
        # 298 STORE_ATTR              10 (key_file)
        # 1116         308 LOAD_FAST                4 (cert_file)
        # 310 LOAD_FAST                0 (self)
        # 312 STORE_ATTR              11 (cert_file)
        # 1117         322 LOAD_FAST               11 (key_password)
        # 324 LOAD_FAST                0 (self)
        # 326 STORE_ATTR              12 (key_password)
        # 336 LOAD_CONST               0 (None)
        # 338 RETURN_VALUE

    def connect(self):
        """Connect to a host on a given (SSL) port."""
        # 1119           0 RESUME                   0
        # 1121           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (proxy_info)
        # 14 POP_JUMP_FORWARD_IF_FALSE    96 (to 208)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                0 (proxy_info)
        # 28 LOAD_METHOD              1 (isgood)
        # 50 PRECALL                  0
        # 54 CALL                     0
        # 64 POP_JUMP_FORWARD_IF_FALSE    71 (to 208)
        # 66 LOAD_FAST                0 (self)
        # 68 LOAD_ATTR                0 (proxy_info)
        # 78 LOAD_METHOD              2 (applies_to)
        # 100 LOAD_FAST                0 (self)
        # 102 LOAD_ATTR                3 (host)
        # 112 PRECALL                  1
        # 116 CALL                     1
        # 126 POP_JUMP_FORWARD_IF_FALSE    40 (to 208)
        # 1122         128 LOAD_CONST               1 (True)
        # 130 STORE_FAST               1 (use_proxy)
        # 1131         132 LOAD_FAST                0 (self)
        # 134 LOAD_ATTR                0 (proxy_info)
        # 144 LOAD_METHOD              4 (astuple)
        # 166 PRECALL                  0
        # 170 CALL                     0
        # 1123         180 UNPACK_SEQUENCE          7
        # 1124         184 STORE_FAST               2 (proxy_type)
        # 1125         186 STORE_FAST               3 (proxy_host)
        # 1126         188 STORE_FAST               4 (proxy_port)
        # 1127         190 STORE_FAST               5 (proxy_rdns)
        # 1128         192 STORE_FAST               6 (proxy_user)
        # 1129         194 STORE_FAST               7 (proxy_pass)
        # 1130         196 STORE_FAST               8 (proxy_headers)
        # 1133         198 LOAD_FAST                3 (proxy_host)
        # 200 STORE_FAST               9 (host)
        # 1134         202 LOAD_FAST                4 (proxy_port)
        # 204 STORE_FAST              10 (port)
        # 206 JUMP_FORWARD            20 (to 248)
        # 1136     >>  208 LOAD_CONST               2 (False)
        # 210 STORE_FAST               1 (use_proxy)
        # 1138         212 LOAD_FAST                0 (self)
        # 214 LOAD_ATTR                3 (host)
        # 224 STORE_FAST               9 (host)
        # 1139         226 LOAD_FAST                0 (self)
        # 228 LOAD_ATTR                5 (port)
        # 238 STORE_FAST              10 (port)
        # 1140         240 LOAD_CONST               3 (None)
        # 242 STORE_FAST               2 (proxy_type)
        # 1141         244 LOAD_CONST               3 (None)
        # 246 STORE_FAST               8 (proxy_headers)
        # 1143     >>  248 LOAD_CONST               3 (None)
        # 250 STORE_FAST              11 (socket_err)
        # 1145         252 LOAD_GLOBAL             13 (NULL + socket)
        # 264 LOAD_ATTR                7 (getaddrinfo)
        # 274 LOAD_FAST                9 (host)
        # 276 LOAD_FAST               10 (port)
        # 278 LOAD_CONST               4 (0)
        # 280 LOAD_GLOBAL             12 (socket)
        # 292 LOAD_ATTR                8 (SOCK_STREAM)
        # 302 PRECALL                  4
        # 306 CALL                     4
        # 316 STORE_FAST              12 (address_info)
        # 1146         318 LOAD_FAST               12 (address_info)
        # 320 GET_ITER
        # >>  322 EXTENDED_ARG             3
        # 324 FOR_ITER               810 (to 1946)
        # 326 UNPACK_SEQUENCE          5
        # 330 STORE_FAST              13 (family)
        # 332 STORE_FAST              14 (socktype)
        # 334 STORE_FAST              15 (proto)
        # 336 STORE_FAST              16 (canonname)
        # 338 STORE_FAST              17 (sockaddr)
        # 1147         340 NOP
        # 1148         342 LOAD_FAST                1 (use_proxy)
        # 344 POP_JUMP_FORWARD_IF_FALSE    49 (to 444)
        # 1149         346 LOAD_GLOBAL             19 (NULL + socks)
        # 358 LOAD_ATTR               10 (socksocket)
        # 368 LOAD_FAST               13 (family)
        # 370 LOAD_FAST               14 (socktype)
        # 372 LOAD_FAST               15 (proto)
        # 374 PRECALL                  3
        # 378 CALL                     3
        # 388 STORE_FAST              18 (sock)
        # 1151         390 LOAD_FAST               18 (sock)
        # 392 LOAD_METHOD             11 (setproxy)
        # 1152         414 LOAD_FAST                2 (proxy_type)
        # 416 LOAD_FAST                3 (proxy_host)
        # 418 LOAD_FAST                4 (proxy_port)
        # 420 LOAD_FAST                5 (proxy_rdns)
        # 422 LOAD_FAST                6 (proxy_user)
        # 424 LOAD_FAST                7 (proxy_pass)
        # 1151         426 PRECALL                  6
        # 430 CALL                     6
        # 440 POP_TOP
        # 442 JUMP_FORWARD            65 (to 574)
        # 1155     >>  444 LOAD_GLOBAL             13 (NULL + socket)
        # 456 LOAD_ATTR                6 (socket)
        # 466 LOAD_FAST               13 (family)
        # 468 LOAD_FAST               14 (socktype)
        # 470 LOAD_FAST               15 (proto)
        # 472 PRECALL                  3
        # 476 CALL                     3
        # 486 STORE_FAST              18 (sock)
        # 1156         488 LOAD_FAST               18 (sock)
        # 490 LOAD_METHOD             12 (setsockopt)
        # 512 LOAD_GLOBAL             12 (socket)
        # 524 LOAD_ATTR               13 (IPPROTO_TCP)
        # 534 LOAD_GLOBAL             12 (socket)
        # 546 LOAD_ATTR               14 (TCP_NODELAY)
        # 556 LOAD_CONST               5 (1)
        # 558 PRECALL                  3
        # 562 CALL                     3
        # 572 POP_TOP
        # 1157     >>  574 LOAD_GLOBAL             31 (NULL + has_timeout)
        # 586 LOAD_FAST                0 (self)
        # 588 LOAD_ATTR               16 (timeout)
        # 598 PRECALL                  1
        # 602 CALL                     1
        # 612 POP_JUMP_FORWARD_IF_FALSE    26 (to 666)
        # 1158         614 LOAD_FAST               18 (sock)
        # 616 LOAD_METHOD             17 (settimeout)
        # 638 LOAD_FAST                0 (self)
        # 640 LOAD_ATTR               16 (timeout)
        # 650 PRECALL                  1
        # 654 CALL                     1
        # 664 POP_TOP
        # 1159     >>  666 LOAD_FAST               18 (sock)
        # 668 LOAD_METHOD             18 (connect)
        # 690 LOAD_FAST                0 (self)
        # 692 LOAD_ATTR                3 (host)
        # 702 LOAD_FAST                0 (self)
        # 704 LOAD_ATTR                5 (port)
        # 714 BUILD_TUPLE              2
        # 716 PRECALL                  1
        # 720 CALL                     1
        # 730 POP_TOP
        # 1161         732 LOAD_FAST                0 (self)
        # 734 LOAD_ATTR               19 (_context)
        # 744 LOAD_METHOD             20 (wrap_socket)
        # 766 LOAD_FAST               18 (sock)
        # 768 LOAD_FAST                0 (self)
        # 770 LOAD_ATTR                3 (host)
        # 780 KW_NAMES                 6
        # 782 PRECALL                  2
        # 786 CALL                     2
        # 796 LOAD_FAST                0 (self)
        # 798 STORE_ATTR              21 (sock)
        # 1164         808 LOAD_GLOBAL             45 (NULL + hasattr)
        # 820 LOAD_FAST                0 (self)
        # 822 LOAD_ATTR               19 (_context)
        # 832 LOAD_CONST               7 ('check_hostname')
        # 834 PRECALL                  2
        # 838 CALL                     2
        # 848 POP_JUMP_FORWARD_IF_TRUE   134 (to 1118)
        # 850 LOAD_FAST                0 (self)
        # 852 LOAD_ATTR               23 (disable_ssl_certificate_validation)
        # 862 POP_JUMP_FORWARD_IF_TRUE   127 (to 1118)
        # 1165         864 NOP
        # 1166         866 LOAD_GLOBAL             49 (NULL + ssl)
        # 878 LOAD_ATTR               25 (match_hostname)
        # 888 LOAD_FAST                0 (self)
        # 890 LOAD_ATTR               21 (sock)
        # 900 LOAD_METHOD             26 (getpeercert)
        # 922 PRECALL                  0
        # 926 CALL                     0
        # 936 LOAD_FAST                0 (self)
        # 938 LOAD_ATTR                3 (host)
        # 948 PRECALL                  2
        # 952 CALL                     2
        # 962 POP_TOP
        # 964 JUMP_FORWARD            76 (to 1118)
        # >>  966 PUSH_EXC_INFO
        # 1167         968 LOAD_GLOBAL             54 (Exception)
        # 980 CHECK_EXC_MATCH
        # 982 POP_JUMP_FORWARD_IF_FALSE    63 (to 1110)
        # 984 POP_TOP
        # 1168         986 LOAD_FAST                0 (self)
        # 988 LOAD_ATTR               21 (sock)
        # 998 LOAD_METHOD             28 (shutdown)
        # 1020 LOAD_GLOBAL             12 (socket)
        # 1032 LOAD_ATTR               29 (SHUT_RDWR)
        # 1042 PRECALL                  1
        # 1046 CALL                     1
        # 1056 POP_TOP
        # 1169        1058 LOAD_FAST                0 (self)
        # 1060 LOAD_ATTR               21 (sock)
        # 1070 LOAD_METHOD             30 (close)
        # 1092 PRECALL                  0
        # 1096 CALL                     0
        # 1106 POP_TOP
        # 1170        1108 RAISE_VARARGS            0
        # 1167     >> 1110 RERAISE                  0
        # >> 1112 COPY                     3
        # 1114 POP_EXCEPT
        # 1116 RERAISE                  1
        # 1172     >> 1118 LOAD_FAST                0 (self)
        # 1120 LOAD_ATTR               31 (debuglevel)
        # 1130 LOAD_CONST               4 (0)
        # 1132 COMPARE_OP               4 (>)
        # 1138 POP_JUMP_FORWARD_IF_FALSE   100 (to 1340)
        # 1173        1140 LOAD_GLOBAL             65 (NULL + print)
        # 1152 LOAD_CONST               8 ('connect: ({0}, {1})')
        # 1154 LOAD_METHOD             33 (format)
        # 1176 LOAD_FAST                0 (self)
        # 1178 LOAD_ATTR                3 (host)
        # 1188 LOAD_FAST                0 (self)
        # 1190 LOAD_ATTR                5 (port)
        # 1200 PRECALL                  2
        # 1204 CALL                     2
        # 1214 PRECALL                  1
        # 1218 CALL                     1
        # 1228 POP_TOP
        # 1174        1230 LOAD_FAST                1 (use_proxy)
        # 1232 POP_JUMP_FORWARD_IF_FALSE    53 (to 1340)
        # 1175        1234 LOAD_GLOBAL             65 (NULL + print)
        # 1176        1246 LOAD_CONST               9 ('proxy: {0}')
        # 1248 LOAD_METHOD             33 (format)
        # 1177        1270 LOAD_GLOBAL             69 (NULL + str)
        # 1282 LOAD_FAST                3 (proxy_host)
        # 1284 LOAD_FAST                4 (proxy_port)
        # 1286 LOAD_FAST                5 (proxy_rdns)
        # 1288 LOAD_FAST                6 (proxy_user)
        # 1290 LOAD_FAST                7 (proxy_pass)
        # 1292 LOAD_FAST                8 (proxy_headers)
        # 1294 BUILD_TUPLE              6
        # 1296 PRECALL                  1
        # 1300 CALL                     1
        # 1176        1310 PRECALL                  1
        # 1314 CALL                     1
        # 1175        1324 PRECALL                  1
        # 1328 CALL                     1
        # 1338 POP_TOP
        # >> 1340 EXTENDED_ARG             1
        # 1342 JUMP_FORWARD           300 (to 1944)
        # >> 1344 PUSH_EXC_INFO
        # 1180        1346 LOAD_GLOBAL             48 (ssl)
        # 1358 LOAD_ATTR               35 (SSLError)
        # 1368 LOAD_GLOBAL             48 (ssl)
        # 1380 LOAD_ATTR               36 (CertificateError)
        # 1390 BUILD_TUPLE              2
        # 1392 CHECK_EXC_MATCH
        # 1394 POP_JUMP_FORWARD_IF_FALSE    67 (to 1530)
        # 1396 STORE_FAST              19 (e)
        # 1181        1398 LOAD_FAST               18 (sock)
        # 1400 POP_JUMP_FORWARD_IF_FALSE    20 (to 1442)
        # 1182        1402 LOAD_FAST               18 (sock)
        # 1404 LOAD_METHOD             30 (close)
        # 1426 PRECALL                  0
        # 1430 CALL                     0
        # 1440 POP_TOP
        # 1183     >> 1442 LOAD_FAST                0 (self)
        # 1444 LOAD_ATTR               21 (sock)
        # 1454 POP_JUMP_FORWARD_IF_FALSE    25 (to 1506)
        # 1184        1456 LOAD_FAST                0 (self)
        # 1458 LOAD_ATTR               21 (sock)
        # 1468 LOAD_METHOD             30 (close)
        # 1490 PRECALL                  0
        # 1494 CALL                     0
        # 1504 POP_TOP
        # 1185     >> 1506 LOAD_CONST               3 (None)
        # 1508 LOAD_FAST                0 (self)
        # 1510 STORE_ATTR              21 (sock)
        # 1186        1520 RAISE_VARARGS            0
        # >> 1522 LOAD_CONST               3 (None)
        # 1524 STORE_FAST              19 (e)
        # 1526 DELETE_FAST             19 (e)
        # 1528 RERAISE                  1
        # 1187     >> 1530 LOAD_GLOBAL             12 (socket)
        # 1542 LOAD_ATTR               16 (timeout)
        # 1552 LOAD_GLOBAL             12 (socket)
        # 1564 LOAD_ATTR               37 (gaierror)
        # 1574 BUILD_TUPLE              2
        # 1576 CHECK_EXC_MATCH
        # 1578 POP_JUMP_FORWARD_IF_FALSE     2 (to 1584)
        # 1580 POP_TOP
        # 1188        1582 RAISE_VARARGS            0
        # 1189     >> 1584 LOAD_GLOBAL             12 (socket)
        # 1596 LOAD_ATTR               38 (error)
        # 1606 CHECK_EXC_MATCH
        # 1608 POP_JUMP_FORWARD_IF_FALSE   163 (to 1936)
        # 1610 STORE_FAST              19 (e)
        # 1190        1612 LOAD_FAST               19 (e)
        # 1614 STORE_FAST              11 (socket_err)
        # 1191        1616 LOAD_FAST                0 (self)
        # 1618 LOAD_ATTR               31 (debuglevel)
        # 1628 LOAD_CONST               4 (0)
        # 1630 COMPARE_OP               4 (>)
        # 1636 POP_JUMP_FORWARD_IF_FALSE   100 (to 1838)
        # 1192        1638 LOAD_GLOBAL             65 (NULL + print)
        # 1650 LOAD_CONST              10 ('connect fail: ({0}, {1})')
        # 1652 LOAD_METHOD             33 (format)
        # 1674 LOAD_FAST                0 (self)
        # 1676 LOAD_ATTR                3 (host)
        # 1686 LOAD_FAST                0 (self)
        # 1688 LOAD_ATTR                5 (port)
        # 1698 PRECALL                  2
        # 1702 CALL                     2
        # 1712 PRECALL                  1
        # 1716 CALL                     1
        # 1726 POP_TOP
        # 1193        1728 LOAD_FAST                1 (use_proxy)
        # 1730 POP_JUMP_FORWARD_IF_FALSE    53 (to 1838)
        # 1194        1732 LOAD_GLOBAL             65 (NULL + print)
        # 1195        1744 LOAD_CONST               9 ('proxy: {0}')
        # 1746 LOAD_METHOD             33 (format)
        # 1196        1768 LOAD_GLOBAL             69 (NULL + str)
        # 1780 LOAD_FAST                3 (proxy_host)
        # 1782 LOAD_FAST                4 (proxy_port)
        # 1784 LOAD_FAST                5 (proxy_rdns)
        # 1786 LOAD_FAST                6 (proxy_user)
        # 1788 LOAD_FAST                7 (proxy_pass)
        # 1790 LOAD_FAST                8 (proxy_headers)
        # 1792 BUILD_TUPLE              6
        # 1794 PRECALL                  1
        # 1798 CALL                     1
        # 1195        1808 PRECALL                  1
        # 1812 CALL                     1
        # 1194        1822 PRECALL                  1
        # 1826 CALL                     1
        # 1836 POP_TOP
        # 1199     >> 1838 LOAD_FAST                0 (self)
        # 1840 LOAD_ATTR               21 (sock)
        # 1850 POP_JUMP_FORWARD_IF_FALSE    25 (to 1902)
        # 1200        1852 LOAD_FAST                0 (self)
        # 1854 LOAD_ATTR               21 (sock)
        # 1864 LOAD_METHOD             30 (close)
        # 1886 PRECALL                  0
        # 1890 CALL                     0
        # 1900 POP_TOP
        # 1201     >> 1902 LOAD_CONST               3 (None)
        # 1904 LOAD_FAST                0 (self)
        # 1906 STORE_ATTR              21 (sock)
        # 1202        1916 POP_EXCEPT
        # 1918 LOAD_CONST               3 (None)
        # 1920 STORE_FAST              19 (e)
        # 1922 DELETE_FAST             19 (e)
        # 1924 EXTENDED_ARG             3
        # 1926 JUMP_BACKWARD          803 (to 322)
        # >> 1928 LOAD_CONST               3 (None)
        # 1930 STORE_FAST              19 (e)
        # 1932 DELETE_FAST             19 (e)
        # 1934 RERAISE                  1
        # 1189     >> 1936 RERAISE                  0
        # >> 1938 COPY                     3
        # 1940 POP_EXCEPT
        # 1942 RERAISE                  1
        # 1203     >> 1944 POP_TOP
        # 1204     >> 1946 LOAD_FAST                0 (self)
        # 1948 LOAD_ATTR               21 (sock)
        # 1958 POP_JUMP_FORWARD_IF_TRUE     2 (to 1964)
        # 1205        1960 LOAD_FAST               11 (socket_err)
        # 1962 RAISE_VARARGS            1
        # 1204     >> 1964 LOAD_CONST               3 (None)
        # 1966 RETURN_VALUE
        # ExceptionTable:
        # 342 to 862 -> 1344 [1]
        # 866 to 962 -> 966 [1]
        # 964 to 964 -> 1344 [1]
        # 966 to 1110 -> 1112 [2] lasti
        # 1112 to 1338 -> 1344 [1]
        # 1344 to 1396 -> 1938 [2] lasti
        # 1398 to 1520 -> 1522 [2] lasti
        # 1522 to 1610 -> 1938 [2] lasti
        # 1612 to 1914 -> 1928 [2] lasti
        # 1928 to 1936 -> 1938 [2] lasti


class Http:
    """Http"""
    def __init__(self, cache, timeout, proxy_info, ca_certs, disable_ssl_certificate_validation, tls_maximum_version, tls_minimum_version):
        """If 'cache' is a string then it is used as a directory name for
        a disk cache. Otherwise it must be an object that supports the
        same interface as FileCache.

        All timeouts are in seconds. If None is passed for timeout
        then Python's default timeout for sockets will be used. See
        for example the docs of socket.setdefaulttimeout():
        http://docs.python.org/library/socket.html#socket.setdefaulttimeout

        `proxy_info` may be:
          - a callable that takes the http scheme ('http' or 'https') and
            returns a ProxyInfo instance per request. By default, uses
            proxy_info_from_environment.
          - a ProxyInfo instance (static proxy config).
          - None (proxy disabled).

        ca_certs is the path of a file containing root CA certificates for SSL
        server certificate validation.  By default, a CA cert file bundled with
        httplib2 is used.

        If disable_ssl_certificate_validation is true, SSL cert validation will
        not be performed.

        tls_maximum_version / tls_minimum_version require Python 3.7+ /
        OpenSSL 1.1.0g+. A value of "TLSv1_3" requires OpenSSL 1.1.1+.
        """
        # 1229           0 RESUME                   0
        # 1265           2 LOAD_FAST                3 (proxy_info)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (proxy_info)
        # 1266          16 LOAD_FAST                4 (ca_certs)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (ca_certs)
        # 1267          30 LOAD_FAST                5 (disable_ssl_certificate_validation)
        # 32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               2 (disable_ssl_certificate_validation)
        # 1268          44 LOAD_FAST                6 (tls_maximum_version)
        # 46 LOAD_FAST                0 (self)
        # 48 STORE_ATTR               3 (tls_maximum_version)
        # 1269          58 LOAD_FAST                7 (tls_minimum_version)
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               4 (tls_minimum_version)
        # 1271          72 BUILD_MAP                0
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               5 (connections)
        # 1274          86 LOAD_FAST                1 (cache)
        # 88 POP_JUMP_FORWARD_IF_FALSE    42 (to 174)
        # 90 LOAD_GLOBAL             13 (NULL + isinstance)
        # 102 LOAD_FAST                1 (cache)
        # 104 LOAD_GLOBAL             14 (str)
        # 116 PRECALL                  2
        # 120 CALL                     2
        # 130 POP_JUMP_FORWARD_IF_FALSE    21 (to 174)
        # 1275         132 LOAD_GLOBAL             17 (NULL + FileCache)
        # 144 LOAD_FAST                1 (cache)
        # 146 PRECALL                  1
        # 150 CALL                     1
        # 160 LOAD_FAST                0 (self)
        # 162 STORE_ATTR               9 (cache)
        # 172 JUMP_FORWARD             7 (to 188)
        # 1277     >>  174 LOAD_FAST                1 (cache)
        # 176 LOAD_FAST                0 (self)
        # 178 STORE_ATTR               9 (cache)
        # 1280     >>  188 LOAD_GLOBAL             21 (NULL + Credentials)
        # 200 PRECALL                  0
        # 204 CALL                     0
        # 214 LOAD_FAST                0 (self)
        # 216 STORE_ATTR              11 (credentials)
        # 1283         226 LOAD_GLOBAL             25 (NULL + KeyCerts)
        # 238 PRECALL                  0
        # 242 CALL                     0
        # 252 LOAD_FAST                0 (self)
        # 254 STORE_ATTR              13 (certificates)
        # 1286         264 BUILD_LIST               0
        # 266 LOAD_FAST                0 (self)
        # 268 STORE_ATTR              14 (authorizations)
        # 1289         278 LOAD_CONST               1 (True)
        # 280 LOAD_FAST                0 (self)
        # 282 STORE_ATTR              15 (follow_redirects)
        # 1291         292 LOAD_GLOBAL             32 (REDIRECT_CODES)
        # 304 LOAD_FAST                0 (self)
        # 306 STORE_ATTR              17 (redirect_codes)
        # 1295         316 LOAD_CONST               2 ('PUT')
        # 318 LOAD_CONST               3 ('PATCH')
        # 320 BUILD_LIST               2
        # 322 LOAD_FAST                0 (self)
        # 324 STORE_ATTR              18 (optimistic_concurrency_methods)
        # 1297         334 LOAD_GLOBAL             39 (NULL + list)
        # 346 LOAD_GLOBAL             40 (SAFE_METHODS)
        # 358 PRECALL                  1
        # 362 CALL                     1
        # 372 LOAD_FAST                0 (self)
        # 374 STORE_ATTR              21 (safe_methods)
        # 1301         384 LOAD_CONST               4 (False)
        # 386 LOAD_FAST                0 (self)
        # 388 STORE_ATTR              22 (follow_all_redirects)
        # 1303         398 LOAD_CONST               4 (False)
        # 400 LOAD_FAST                0 (self)
        # 402 STORE_ATTR              23 (ignore_etag)
        # 1305         412 LOAD_CONST               4 (False)
        # 414 LOAD_FAST                0 (self)
        # 416 STORE_ATTR              24 (force_exception_to_status_code)
        # 1307         426 LOAD_FAST                2 (timeout)
        # 428 LOAD_FAST                0 (self)
        # 430 STORE_ATTR              25 (timeout)
        # 1310         440 LOAD_CONST               4 (False)
        # 442 LOAD_FAST                0 (self)
        # 444 STORE_ATTR              26 (forward_authorization_headers)
        # 454 LOAD_CONST               5 (None)
        # 456 RETURN_VALUE

    def close(self):
        """Close persistent connections, clear sensitive data.
        Not thread-safe, requires external synchronization against concurrent requests.
        """
        # 1312           0 RESUME                   0
        # 1316           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (connections)
        # 14 BUILD_MAP                0
        # 16 SWAP                     2
        # 18 STORE_FAST               1 (existing)
        # 20 LOAD_FAST                0 (self)
        # 22 STORE_ATTR               0 (connections)
        # 1317          32 LOAD_FAST                1 (existing)
        # 34 LOAD_METHOD              1 (items)
        # 56 PRECALL                  0
        # 60 CALL                     0
        # 70 GET_ITER
        # >>   72 FOR_ITER                25 (to 124)
        # 74 UNPACK_SEQUENCE          2
        # 78 STORE_FAST               2 (_)
        # 80 STORE_FAST               3 (c)
        # 1318          82 LOAD_FAST                3 (c)
        # 84 LOAD_METHOD              2 (close)
        # 106 PRECALL                  0
        # 110 CALL                     0
        # 120 POP_TOP
        # 122 JUMP_BACKWARD           26 (to 72)
        # 1319     >>  124 LOAD_FAST                0 (self)
        # 126 LOAD_ATTR                3 (certificates)
        # 136 LOAD_METHOD              4 (clear)
        # 158 PRECALL                  0
        # 162 CALL                     0
        # 172 POP_TOP
        # 1320         174 LOAD_FAST                0 (self)
        # 176 LOAD_METHOD              5 (clear_credentials)
        # 198 PRECALL                  0
        # 202 CALL                     0
        # 212 POP_TOP
        # 214 LOAD_CONST               1 (None)
        # 216 RETURN_VALUE

    def __getstate__(self):
        # 1322           0 RESUME                   0
        # 1323           2 LOAD_GLOBAL              1 (NULL + copy)
        # 14 LOAD_ATTR                0 (copy)
        # 24 LOAD_FAST                0 (self)
        # 26 LOAD_ATTR                1 (__dict__)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 STORE_FAST               1 (state_dict)
        # 1326          52 LOAD_CONST               1 ('request')
        # 54 LOAD_FAST                1 (state_dict)
        # 56 CONTAINS_OP              0
        # 58 POP_JUMP_FORWARD_IF_FALSE     3 (to 66)
        # 1327          60 LOAD_FAST                1 (state_dict)
        # 62 LOAD_CONST               1 ('request')
        # 64 DELETE_SUBSCR
        # 1328     >>   66 LOAD_CONST               2 ('connections')
        # 68 LOAD_FAST                1 (state_dict)
        # 70 CONTAINS_OP              0
        # 72 POP_JUMP_FORWARD_IF_FALSE     3 (to 80)
        # 1329          74 LOAD_FAST                1 (state_dict)
        # 76 LOAD_CONST               2 ('connections')
        # 78 DELETE_SUBSCR
        # 1330     >>   80 LOAD_FAST                1 (state_dict)
        # 82 RETURN_VALUE

    def __setstate__(self, state):
        # 1332           0 RESUME                   0
        # 1333           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__dict__)
        # 14 LOAD_METHOD              1 (update)
        # 36 LOAD_FAST                1 (state)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 POP_TOP
        # 1334          54 BUILD_MAP                0
        # 56 LOAD_FAST                0 (self)
        # 58 STORE_ATTR               2 (connections)
        # 68 LOAD_CONST               0 (None)
        # 70 RETURN_VALUE

    def _auth_from_challenge(self, host, request_uri, headers, response, content):
        """A generator that creates Authorization objects
           that can be applied to requests.
        """
        # 1336           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 1340           6 LOAD_GLOBAL              1 (NULL + auth)
        # 18 LOAD_ATTR                1 (_parse_www_authenticate)
        # 28 LOAD_FAST                4 (response)
        # 30 LOAD_CONST               1 ('www-authenticate')
        # 32 PRECALL                  2
        # 36 CALL                     2
        # 46 STORE_FAST               6 (challenges)
        # 1341          48 LOAD_FAST                0 (self)
        # 50 LOAD_ATTR                2 (credentials)
        # 60 LOAD_METHOD              3 (iter)
        # 82 LOAD_FAST                1 (host)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 GET_ITER
        # >>  100 FOR_ITER                45 (to 192)
        # 102 STORE_FAST               7 (cred)
        # 1342         104 LOAD_GLOBAL              8 (AUTH_SCHEME_ORDER)
        # 116 GET_ITER
        # >>  118 FOR_ITER                35 (to 190)
        # 120 STORE_FAST               8 (scheme)
        # 1343         122 LOAD_FAST                8 (scheme)
        # 124 LOAD_FAST                6 (challenges)
        # 126 CONTAINS_OP              0
        # 128 POP_JUMP_FORWARD_IF_FALSE    29 (to 188)
        # 1344         130 LOAD_GLOBAL             11 (NULL + AUTH_SCHEME_CLASSES)
        # 142 LOAD_FAST                8 (scheme)
        # 144 BINARY_SUBSCR
        # 154 LOAD_FAST                7 (cred)
        # 156 LOAD_FAST                1 (host)
        # 158 LOAD_FAST                2 (request_uri)
        # 160 LOAD_FAST                3 (headers)
        # 162 LOAD_FAST                4 (response)
        # 164 LOAD_FAST                5 (content)
        # 166 LOAD_FAST                0 (self)
        # 168 PRECALL                  7
        # 172 CALL                     7
        # 182 YIELD_VALUE
        # 184 RESUME                   1
        # 186 POP_TOP
        # >>  188 JUMP_BACKWARD           36 (to 118)
        # 1342     >>  190 JUMP_BACKWARD           46 (to 100)
        # 1341     >>  192 LOAD_CONST               2 (None)
        # 194 RETURN_VALUE

    def add_credentials(self, name, password, domain):
        """Add a name and password that will be used
        any time a request requires authentication."""
        # 1346           0 RESUME                   0
        # 1349           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (credentials)
        # 14 LOAD_METHOD              1 (add)
        # 36 LOAD_FAST                1 (name)
        # 38 LOAD_FAST                2 (password)
        # 40 LOAD_FAST                3 (domain)
        # 42 PRECALL                  3
        # 46 CALL                     3
        # 56 POP_TOP
        # 58 LOAD_CONST               1 (None)
        # 60 RETURN_VALUE

    def add_certificate(self, key, cert, domain, password):
        """Add a key and cert that will be used
        any time a request requires authentication."""
        # 1351           0 RESUME                   0
        # 1354           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (certificates)
        # 14 LOAD_METHOD              1 (add)
        # 36 LOAD_FAST                1 (key)
        # 38 LOAD_FAST                2 (cert)
        # 40 LOAD_FAST                3 (domain)
        # 42 LOAD_FAST                4 (password)
        # 44 PRECALL                  4
        # 48 CALL                     4
        # 58 POP_TOP
        # 60 LOAD_CONST               1 (None)
        # 62 RETURN_VALUE

    def clear_credentials(self):
        """Remove all the names and passwords
        that are used for authentication"""
        # 1356           0 RESUME                   0
        # 1359           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (credentials)
        # 14 LOAD_METHOD              1 (clear)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 1360          52 BUILD_LIST               0
        # 54 LOAD_FAST                0 (self)
        # 56 STORE_ATTR               2 (authorizations)
        # 66 LOAD_CONST               1 (None)
        # 68 RETURN_VALUE

    def _conn_request(self, conn, request_uri, method, body, headers):
        # 1362           0 RESUME                   0
        # 1363           2 LOAD_CONST               1 (0)
        # 4 STORE_FAST               6 (i)
        # 1364           6 LOAD_CONST               2 (False)
        # 8 STORE_FAST               7 (seen_bad_status_line)
        # 1365     >>   10 LOAD_FAST                6 (i)
        # 12 LOAD_GLOBAL              0 (RETRIES)
        # 24 COMPARE_OP               0 (<)
        # 30 EXTENDED_ARG             2
        # 32 POP_JUMP_FORWARD_IF_FALSE   737 (to 1508)
        # 1366          34 LOAD_FAST                6 (i)
        # 36 LOAD_CONST               3 (1)
        # 38 BINARY_OP               13 (+=)
        # 42 STORE_FAST               6 (i)
        # 1367          44 NOP
        # 1368          46 LOAD_FAST                1 (conn)
        # 48 LOAD_ATTR                1 (sock)
        # 58 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 100)
        # 1369          60 LOAD_FAST                1 (conn)
        # 62 LOAD_METHOD              2 (connect)
        # 84 PRECALL                  0
        # 88 CALL                     0
        # 98 POP_TOP
        # 1370     >>  100 LOAD_FAST                1 (conn)
        # 102 LOAD_METHOD              3 (request)
        # 124 LOAD_FAST                3 (method)
        # 126 LOAD_FAST                2 (request_uri)
        # 128 LOAD_FAST                4 (body)
        # 130 LOAD_FAST                5 (headers)
        # 132 PRECALL                  4
        # 136 CALL                     4
        # 146 POP_TOP
        # 148 EXTENDED_ARG             1
        # 150 JUMP_FORWARD           336 (to 824)
        # >>  152 PUSH_EXC_INFO
        # 1371         154 LOAD_GLOBAL              8 (socket)
        # 166 LOAD_ATTR                5 (timeout)
        # 176 CHECK_EXC_MATCH
        # 178 POP_JUMP_FORWARD_IF_FALSE    22 (to 224)
        # 180 POP_TOP
        # 1372         182 LOAD_FAST                1 (conn)
        # 184 LOAD_METHOD              6 (close)
        # 206 PRECALL                  0
        # 210 CALL                     0
        # 220 POP_TOP
        # 1373         222 RAISE_VARARGS            0
        # 1374     >>  224 LOAD_GLOBAL              8 (socket)
        # 236 LOAD_ATTR                7 (gaierror)
        # 246 CHECK_EXC_MATCH
        # 248 POP_JUMP_FORWARD_IF_FALSE    44 (to 338)
        # 250 POP_TOP
        # 1375         252 LOAD_FAST                1 (conn)
        # 254 LOAD_METHOD              6 (close)
        # 276 PRECALL                  0
        # 280 CALL                     0
        # 290 POP_TOP
        # 1376         292 LOAD_GLOBAL             17 (NULL + ServerNotFoundError)
        # 304 LOAD_CONST               4 ('Unable to find the server at %s')
        # 306 LOAD_FAST                1 (conn)
        # 308 LOAD_ATTR                9 (host)
        # 318 BINARY_OP                6 (%)
        # 322 PRECALL                  1
        # 326 CALL                     1
        # 336 RAISE_VARARGS            1
        # 1377     >>  338 LOAD_GLOBAL              8 (socket)
        # 350 LOAD_ATTR               10 (error)
        # 360 CHECK_EXC_MATCH
        # 362 POP_JUMP_FORWARD_IF_FALSE    63 (to 490)
        # 364 STORE_FAST               8 (e)
        # 1378         366 LOAD_GLOBAL             23 (NULL + _errno_from_exception)
        # 378 LOAD_FAST                8 (e)
        # 380 PRECALL                  1
        # 384 CALL                     1
        # 394 STORE_FAST               9 (errno_)
        # 1379         396 LOAD_FAST                9 (errno_)
        # 398 LOAD_GLOBAL             24 (errno)
        # 410 LOAD_ATTR               13 (ENETUNREACH)
        # 420 LOAD_GLOBAL             24 (errno)
        # 432 LOAD_ATTR               14 (EADDRNOTAVAIL)
        # 442 BUILD_TUPLE              2
        # 444 CONTAINS_OP              0
        # 446 POP_JUMP_FORWARD_IF_FALSE    16 (to 480)
        # 448 LOAD_FAST                6 (i)
        # 450 LOAD_GLOBAL              0 (RETRIES)
        # 462 COMPARE_OP               0 (<)
        # 468 POP_JUMP_FORWARD_IF_FALSE     5 (to 480)
        # 1380         470 POP_EXCEPT
        # 472 LOAD_CONST               0 (None)
        # 474 STORE_FAST               8 (e)
        # 476 DELETE_FAST              8 (e)
        # 478 JUMP_BACKWARD          235 (to 10)
        # 1381     >>  480 RAISE_VARARGS            0
        # >>  482 LOAD_CONST               0 (None)
        # 484 STORE_FAST               8 (e)
        # 486 DELETE_FAST              8 (e)
        # 488 RERAISE                  1
        # 1382     >>  490 LOAD_GLOBAL             30 (http)
        # 502 LOAD_ATTR               16 (client)
        # 512 LOAD_ATTR               17 (HTTPException)
        # 522 CHECK_EXC_MATCH
        # 524 POP_JUMP_FORWARD_IF_FALSE   145 (to 816)
        # 526 POP_TOP
        # 1383         528 LOAD_FAST                1 (conn)
        # 530 LOAD_ATTR                1 (sock)
        # 540 POP_JUMP_FORWARD_IF_NOT_NONE    78 (to 698)
        # 1384         542 LOAD_FAST                6 (i)
        # 544 LOAD_GLOBAL              0 (RETRIES)
        # 556 LOAD_CONST               3 (1)
        # 558 BINARY_OP               10 (-)
        # 562 COMPARE_OP               0 (<)
        # 568 POP_JUMP_FORWARD_IF_FALSE    43 (to 656)
        # 1385         570 LOAD_FAST                1 (conn)
        # 572 LOAD_METHOD              6 (close)
        # 594 PRECALL                  0
        # 598 CALL                     0
        # 608 POP_TOP
        # 1386         610 LOAD_FAST                1 (conn)
        # 612 LOAD_METHOD              2 (connect)
        # 634 PRECALL                  0
        # 638 CALL                     0
        # 648 POP_TOP
        # 1387         650 POP_EXCEPT
        # 652 EXTENDED_ARG             1
        # 654 JUMP_BACKWARD          323 (to 10)
        # 1389     >>  656 LOAD_FAST                1 (conn)
        # 658 LOAD_METHOD              6 (close)
        # 680 PRECALL                  0
        # 684 CALL                     0
        # 694 POP_TOP
        # 1390         696 RAISE_VARARGS            0
        # 1391     >>  698 LOAD_FAST                6 (i)
        # 700 LOAD_GLOBAL              0 (RETRIES)
        # 712 LOAD_CONST               3 (1)
        # 714 BINARY_OP               10 (-)
        # 718 COMPARE_OP               0 (<)
        # 724 POP_JUMP_FORWARD_IF_FALSE    43 (to 812)
        # 1392         726 LOAD_FAST                1 (conn)
        # 728 LOAD_METHOD              6 (close)
        # 750 PRECALL                  0
        # 754 CALL                     0
        # 764 POP_TOP
        # 1393         766 LOAD_FAST                1 (conn)
        # 768 LOAD_METHOD              2 (connect)
        # 790 PRECALL                  0
        # 794 CALL                     0
        # 804 POP_TOP
        # 1394         806 POP_EXCEPT
        # 808 EXTENDED_ARG             1
        # 810 JUMP_BACKWARD          401 (to 10)
        # 1397     >>  812 POP_EXCEPT
        # 814 JUMP_FORWARD             4 (to 824)
        # 1382     >>  816 RERAISE                  0
        # >>  818 COPY                     3
        # 820 POP_EXCEPT
        # 822 RERAISE                  1
        # 1398     >>  824 NOP
        # 1399         826 LOAD_FAST                1 (conn)
        # 828 LOAD_METHOD             18 (getresponse)
        # 850 PRECALL                  0
        # 854 CALL                     0
        # 864 STORE_FAST              10 (response)
        # 1424         866 LOAD_CONST               5 (b'')
        # 868 STORE_FAST              11 (content)
        # 1425         870 LOAD_FAST                3 (method)
        # 872 LOAD_CONST               6 ('HEAD')
        # 874 COMPARE_OP               2 (==)
        # 880 POP_JUMP_FORWARD_IF_FALSE    21 (to 924)
        # 1426         882 LOAD_FAST                1 (conn)
        # 884 LOAD_METHOD              6 (close)
        # 906 PRECALL                  0
        # 910 CALL                     0
        # 920 POP_TOP
        # 922 JUMP_FORWARD            20 (to 964)
        # 1428     >>  924 LOAD_FAST               10 (response)
        # 926 LOAD_METHOD             19 (read)
        # 948 PRECALL                  0
        # 952 CALL                     0
        # 962 STORE_FAST              11 (content)
        # 1429     >>  964 LOAD_GLOBAL             41 (NULL + Response)
        # 976 LOAD_FAST               10 (response)
        # 978 PRECALL                  1
        # 982 CALL                     1
        # 992 STORE_FAST              10 (response)
        # 1430         994 LOAD_FAST                3 (method)
        # 996 LOAD_CONST               6 ('HEAD')
        # 998 COMPARE_OP               3 (!=)
        # 1004 POP_JUMP_FORWARD_IF_FALSE    16 (to 1038)
        # 1431        1006 LOAD_GLOBAL             43 (NULL + _decompressContent)
        # 1018 LOAD_FAST               10 (response)
        # 1020 LOAD_FAST               11 (content)
        # 1022 PRECALL                  2
        # 1026 CALL                     2
        # 1036 STORE_FAST              11 (content)
        # >> 1038 JUMP_FORWARD           233 (to 1506)
        # >> 1040 PUSH_EXC_INFO
        # 1400        1042 LOAD_GLOBAL             30 (http)
        # 1054 LOAD_ATTR               16 (client)
        # 1064 LOAD_ATTR               22 (BadStatusLine)
        # 1074 LOAD_GLOBAL             30 (http)
        # 1086 LOAD_ATTR               16 (client)
        # 1096 LOAD_ATTR               23 (ResponseNotReady)
        # 1106 BUILD_TUPLE              2
        # 1108 CHECK_EXC_MATCH
        # 1110 POP_JUMP_FORWARD_IF_FALSE    77 (to 1266)
        # 1112 POP_TOP
        # 1404        1114 LOAD_FAST                7 (seen_bad_status_line)
        # 1116 POP_JUMP_FORWARD_IF_TRUE    53 (to 1224)
        # 1118 LOAD_FAST                6 (i)
        # 1120 LOAD_CONST               3 (1)
        # 1122 COMPARE_OP               2 (==)
        # 1128 POP_JUMP_FORWARD_IF_FALSE    47 (to 1224)
        # 1405        1130 LOAD_CONST               1 (0)
        # 1132 STORE_FAST               6 (i)
        # 1406        1134 LOAD_CONST               7 (True)
        # 1136 STORE_FAST               7 (seen_bad_status_line)
        # 1407        1138 LOAD_FAST                1 (conn)
        # 1140 LOAD_METHOD              6 (close)
        # 1162 PRECALL                  0
        # 1166 CALL                     0
        # 1176 POP_TOP
        # 1408        1178 LOAD_FAST                1 (conn)
        # 1180 LOAD_METHOD              2 (connect)
        # 1202 PRECALL                  0
        # 1206 CALL                     0
        # 1216 POP_TOP
        # 1409        1218 POP_EXCEPT
        # 1220 EXTENDED_ARG             2
        # 1222 JUMP_BACKWARD          607 (to 10)
        # 1411     >> 1224 LOAD_FAST                1 (conn)
        # 1226 LOAD_METHOD              6 (close)
        # 1248 PRECALL                  0
        # 1252 CALL                     0
        # 1262 POP_TOP
        # 1412        1264 RAISE_VARARGS            0
        # 1413     >> 1266 LOAD_GLOBAL              8 (socket)
        # 1278 LOAD_ATTR                5 (timeout)
        # 1288 CHECK_EXC_MATCH
        # 1290 POP_JUMP_FORWARD_IF_FALSE     2 (to 1296)
        # 1292 POP_TOP
        # 1414        1294 RAISE_VARARGS            0
        # 1415     >> 1296 LOAD_GLOBAL              8 (socket)
        # 1308 LOAD_ATTR               10 (error)
        # 1318 LOAD_GLOBAL             30 (http)
        # 1330 LOAD_ATTR               16 (client)
        # 1340 LOAD_ATTR               17 (HTTPException)
        # 1350 BUILD_TUPLE              2
        # 1352 CHECK_EXC_MATCH
        # 1354 POP_JUMP_FORWARD_IF_FALSE    71 (to 1498)
        # 1356 POP_TOP
        # 1416        1358 LOAD_FAST                1 (conn)
        # 1360 LOAD_METHOD              6 (close)
        # 1382 PRECALL                  0
        # 1386 CALL                     0
        # 1396 POP_TOP
        # 1417        1398 LOAD_FAST                6 (i)
        # 1400 LOAD_CONST               1 (0)
        # 1402 COMPARE_OP               2 (==)
        # 1408 POP_JUMP_FORWARD_IF_FALSE    43 (to 1496)
        # 1418        1410 LOAD_FAST                1 (conn)
        # 1412 LOAD_METHOD              6 (close)
        # 1434 PRECALL                  0
        # 1438 CALL                     0
        # 1448 POP_TOP
        # 1419        1450 LOAD_FAST                1 (conn)
        # 1452 LOAD_METHOD              2 (connect)
        # 1474 PRECALL                  0
        # 1478 CALL                     0
        # 1488 POP_TOP
        # 1420        1490 POP_EXCEPT
        # 1492 EXTENDED_ARG             2
        # 1494 JUMP_BACKWARD          743 (to 10)
        # 1422     >> 1496 RAISE_VARARGS            0
        # 1415     >> 1498 RERAISE                  0
        # >> 1500 COPY                     3
        # 1502 POP_EXCEPT
        # 1504 RERAISE                  1
        # 1433     >> 1506 NOP
        # 1434     >> 1508 LOAD_FAST               10 (response)
        # 1510 LOAD_FAST               11 (content)
        # 1512 BUILD_TUPLE              2
        # 1514 RETURN_VALUE
        # ExceptionTable:
        # 46 to 146 -> 152 [0]
        # 152 to 364 -> 818 [1] lasti
        # 366 to 468 -> 482 [1] lasti
        # 480 to 480 -> 482 [1] lasti
        # 482 to 648 -> 818 [1] lasti
        # 656 to 804 -> 818 [1] lasti
        # 816 to 816 -> 818 [1] lasti
        # 826 to 864 -> 1040 [0]
        # 1040 to 1216 -> 1500 [1] lasti
        # 1224 to 1488 -> 1500 [1] lasti
        # 1496 to 1498 -> 1500 [1] lasti

    def _request(self, conn, host, absolute_uri, request_uri, method, body, headers, redirections, cachekey):
        """Do the actual request using the connection object
        and also follow one level of redirects if necessary"""
        # 0 MAKE_CELL                2 (host)
        # 2 MAKE_CELL                4 (request_uri)
        # 1436           4 RESUME                   0
        # 1442           6 LOAD_CLOSURE             2 (host)
        # 8 LOAD_CLOSURE             4 (request_uri)
        # 10 BUILD_TUPLE              2
        # 12 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7E28470, file "httplib2\__init__.py", line 1442>)
        # 14 MAKE_FUNCTION            8 (closure)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                0 (authorizations)
        # 28 GET_ITER
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 STORE_FAST              10 (auths)
        # 1443          46 LOAD_FAST               10 (auths)
        # 48 POP_JUMP_FORWARD_IF_FALSE    27 (to 104)
        # 50 LOAD_GLOBAL              3 (NULL + sorted)
        # 62 LOAD_FAST               10 (auths)
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 LOAD_CONST               2 (0)
        # 80 BINARY_SUBSCR
        # 90 LOAD_CONST               3 (1)
        # 92 BINARY_SUBSCR
        # 102 JUMP_IF_TRUE_OR_POP      1 (to 106)
        # >>  104 LOAD_CONST               4 (None)
        # >>  106 STORE_FAST              11 (auth)
        # 1444         108 LOAD_FAST               11 (auth)
        # 110 POP_JUMP_FORWARD_IF_FALSE    19 (to 150)
        # 1445         112 PUSH_NULL
        # 114 LOAD_FAST               11 (auth)
        # 116 LOAD_ATTR                2 (request)
        # 126 LOAD_FAST                5 (method)
        # 128 LOAD_DEREF               4 (request_uri)
        # 130 LOAD_FAST                7 (headers)
        # 132 LOAD_FAST                6 (body)
        # 134 PRECALL                  4
        # 138 CALL                     4
        # 148 POP_TOP
        # 1447     >>  150 LOAD_FAST                0 (self)
        # 152 LOAD_METHOD              3 (_conn_request)
        # 174 LOAD_FAST                1 (conn)
        # 176 LOAD_DEREF               4 (request_uri)
        # 178 LOAD_FAST                5 (method)
        # 180 LOAD_FAST                6 (body)
        # 182 LOAD_FAST                7 (headers)
        # 184 PRECALL                  5
        # 188 CALL                     5
        # 198 UNPACK_SEQUENCE          2
        # 202 STORE_FAST              12 (response)
        # 204 STORE_FAST              13 (content)
        # 1449         206 LOAD_FAST               11 (auth)
        # 208 POP_JUMP_FORWARD_IF_FALSE    71 (to 352)
        # 1450         210 PUSH_NULL
        # 212 LOAD_FAST               11 (auth)
        # 214 LOAD_ATTR                4 (response)
        # 224 LOAD_FAST               12 (response)
        # 226 LOAD_FAST                6 (body)
        # 228 PRECALL                  2
        # 232 CALL                     2
        # 242 POP_JUMP_FORWARD_IF_FALSE    54 (to 352)
        # 1451         244 PUSH_NULL
        # 246 LOAD_FAST               11 (auth)
        # 248 LOAD_ATTR                2 (request)
        # 258 LOAD_FAST                5 (method)
        # 260 LOAD_DEREF               4 (request_uri)
        # 262 LOAD_FAST                7 (headers)
        # 264 LOAD_FAST                6 (body)
        # 266 PRECALL                  4
        # 270 CALL                     4
        # 280 POP_TOP
        # 1452         282 LOAD_FAST                0 (self)
        # 284 LOAD_METHOD              3 (_conn_request)
        # 306 LOAD_FAST                1 (conn)
        # 308 LOAD_DEREF               4 (request_uri)
        # 310 LOAD_FAST                5 (method)
        # 312 LOAD_FAST                6 (body)
        # 314 LOAD_FAST                7 (headers)
        # 316 PRECALL                  5
        # 320 CALL                     5
        # 330 UNPACK_SEQUENCE          2
        # 334 STORE_FAST              12 (response)
        # 336 STORE_FAST              13 (content)
        # 1453         338 LOAD_CONST               3 (1)
        # 340 LOAD_FAST               12 (response)
        # 342 STORE_ATTR               5 (_stale_digest)
        # 1455     >>  352 LOAD_FAST               12 (response)
        # 354 LOAD_ATTR                6 (status)
        # 364 LOAD_CONST               5 (401)
        # 366 COMPARE_OP               2 (==)
        # 372 POP_JUMP_FORWARD_IF_FALSE   141 (to 656)
        # 1456         374 LOAD_FAST                0 (self)
        # 376 LOAD_METHOD              7 (_auth_from_challenge)
        # 398 LOAD_DEREF               2 (host)
        # 400 LOAD_DEREF               4 (request_uri)
        # 402 LOAD_FAST                7 (headers)
        # 404 LOAD_FAST               12 (response)
        # 406 LOAD_FAST               13 (content)
        # 408 PRECALL                  5
        # 412 CALL                     5
        # 422 GET_ITER
        # >>  424 FOR_ITER               115 (to 656)
        # 426 STORE_FAST              14 (authorization)
        # 1457         428 LOAD_FAST               14 (authorization)
        # 430 LOAD_METHOD              2 (request)
        # 452 LOAD_FAST                5 (method)
        # 454 LOAD_DEREF               4 (request_uri)
        # 456 LOAD_FAST                7 (headers)
        # 458 LOAD_FAST                6 (body)
        # 460 PRECALL                  4
        # 464 CALL                     4
        # 474 POP_TOP
        # 1458         476 LOAD_FAST                0 (self)
        # 478 LOAD_METHOD              3 (_conn_request)
        # 500 LOAD_FAST                1 (conn)
        # 502 LOAD_DEREF               4 (request_uri)
        # 504 LOAD_FAST                5 (method)
        # 506 LOAD_FAST                6 (body)
        # 508 LOAD_FAST                7 (headers)
        # 510 PRECALL                  5
        # 514 CALL                     5
        # 524 UNPACK_SEQUENCE          2
        # 528 STORE_FAST              12 (response)
        # 530 STORE_FAST              13 (content)
        # 1459         532 LOAD_FAST               12 (response)
        # 534 LOAD_ATTR                6 (status)
        # 544 LOAD_CONST               5 (401)
        # 546 COMPARE_OP               3 (!=)
        # 552 POP_JUMP_FORWARD_IF_FALSE    50 (to 654)
        # 1460         554 LOAD_FAST                0 (self)
        # 556 LOAD_ATTR                0 (authorizations)
        # 566 LOAD_METHOD              8 (append)
        # 588 LOAD_FAST               14 (authorization)
        # 590 PRECALL                  1
        # 594 CALL                     1
        # 604 POP_TOP
        # 1461         606 LOAD_FAST               14 (authorization)
        # 608 LOAD_METHOD              4 (response)
        # 630 LOAD_FAST               12 (response)
        # 632 LOAD_FAST                6 (body)
        # 634 PRECALL                  2
        # 638 CALL                     2
        # 648 POP_TOP
        # 1462         650 POP_TOP
        # 652 JUMP_FORWARD             1 (to 656)
        # 1459     >>  654 JUMP_BACKWARD          116 (to 424)
        # 1464     >>  656 LOAD_FAST                0 (self)
        # 658 LOAD_ATTR                9 (follow_all_redirects)
        # 668 POP_JUMP_FORWARD_IF_TRUE    19 (to 708)
        # 670 LOAD_FAST                5 (method)
        # 672 LOAD_FAST                0 (self)
        # 674 LOAD_ATTR               10 (safe_methods)
        # 684 CONTAINS_OP              0
        # 686 POP_JUMP_FORWARD_IF_TRUE    10 (to 708)
        # 688 LOAD_FAST               12 (response)
        # 690 LOAD_ATTR                6 (status)
        # 700 LOAD_CONST               6 ((303, 308))
        # 702 CONTAINS_OP              0
        # 704 EXTENDED_ARG             1
        # 706 POP_JUMP_FORWARD_IF_FALSE   412 (to 1532)
        # 1465     >>  708 LOAD_FAST                0 (self)
        # 710 LOAD_ATTR               11 (follow_redirects)
        # 720 EXTENDED_ARG             1
        # 722 POP_JUMP_FORWARD_IF_FALSE   353 (to 1430)
        # 724 LOAD_FAST               12 (response)
        # 726 LOAD_ATTR                6 (status)
        # 736 LOAD_FAST                0 (self)
        # 738 LOAD_ATTR               12 (redirect_codes)
        # 748 CONTAINS_OP              0
        # 750 EXTENDED_ARG             1
        # 752 POP_JUMP_FORWARD_IF_FALSE   338 (to 1430)
        # 1468         754 LOAD_FAST                8 (redirections)
        # 756 EXTENDED_ARG             1
        # 758 POP_JUMP_FORWARD_IF_FALSE   318 (to 1396)
        # 1469         760 LOAD_CONST               7 ('location')
        # 762 LOAD_FAST               12 (response)
        # 764 CONTAINS_OP              1
        # 766 POP_JUMP_FORWARD_IF_FALSE    41 (to 850)
        # 768 LOAD_FAST               12 (response)
        # 770 LOAD_ATTR                6 (status)
        # 780 LOAD_CONST               8 (300)
        # 782 COMPARE_OP               3 (!=)
        # 788 POP_JUMP_FORWARD_IF_FALSE    30 (to 850)
        # 1470         790 LOAD_GLOBAL             27 (NULL + RedirectMissingLocation)
        # 1471         802 LOAD_GLOBAL             29 (NULL + _)
        # 814 LOAD_CONST               9 ('Redirected but the response is missing a Location: header.')
        # 816 PRECALL                  1
        # 820 CALL                     1
        # 830 LOAD_FAST               12 (response)
        # 832 LOAD_FAST               13 (content)
        # 1470         834 PRECALL                  3
        # 838 CALL                     3
        # 848 RAISE_VARARGS            1
        # 1474     >>  850 LOAD_CONST               7 ('location')
        # 852 LOAD_FAST               12 (response)
        # 854 CONTAINS_OP              0
        # 856 POP_JUMP_FORWARD_IF_FALSE    70 (to 998)
        # 1475         858 LOAD_FAST               12 (response)
        # 860 LOAD_CONST               7 ('location')
        # 862 BINARY_SUBSCR
        # 872 STORE_FAST              15 (location)
        # 1476         874 LOAD_GLOBAL             31 (NULL + parse_uri)
        # 886 LOAD_FAST               15 (location)
        # 888 PRECALL                  1
        # 892 CALL                     1
        # 902 UNPACK_SEQUENCE          5
        # 906 STORE_FAST              16 (scheme)
        # 908 STORE_FAST              17 (authority)
        # 910 STORE_FAST              18 (path)
        # 912 STORE_FAST              19 (query)
        # 914 STORE_FAST              20 (fragment)
        # 1477         916 LOAD_FAST               17 (authority)
        # 918 LOAD_CONST               4 (None)
        # 920 COMPARE_OP               2 (==)
        # 926 POP_JUMP_FORWARD_IF_FALSE    35 (to 998)
        # 1478         928 LOAD_GLOBAL             32 (urllib)
        # 940 LOAD_ATTR               17 (parse)
        # 950 LOAD_METHOD             18 (urljoin)
        # 972 LOAD_FAST                3 (absolute_uri)
        # 974 LOAD_FAST               15 (location)
        # 976 PRECALL                  2
        # 980 CALL                     2
        # 990 LOAD_FAST               12 (response)
        # 992 LOAD_CONST               7 ('location')
        # 994 STORE_SUBSCR
        # 1479     >>  998 LOAD_FAST               12 (response)
        # 1000 LOAD_ATTR                6 (status)
        # 1010 LOAD_CONST              10 (308)
        # 1012 COMPARE_OP               2 (==)
        # 1018 POP_JUMP_FORWARD_IF_TRUE    20 (to 1060)
        # 1020 LOAD_FAST               12 (response)
        # 1022 LOAD_ATTR                6 (status)
        # 1032 LOAD_CONST              11 (301)
        # 1034 COMPARE_OP               2 (==)
        # 1040 POP_JUMP_FORWARD_IF_FALSE    53 (to 1148)
        # 1042 LOAD_FAST                5 (method)
        # 1044 LOAD_FAST                0 (self)
        # 1046 LOAD_ATTR               10 (safe_methods)
        # 1056 CONTAINS_OP              0
        # 1058 POP_JUMP_FORWARD_IF_FALSE    44 (to 1148)
        # 1480     >> 1060 LOAD_FAST               12 (response)
        # 1062 LOAD_CONST               7 ('location')
        # 1064 BINARY_SUBSCR
        # 1074 LOAD_FAST               12 (response)
        # 1076 LOAD_CONST              12 ('-x-permanent-redirect-url')
        # 1078 STORE_SUBSCR
        # 1481        1082 LOAD_CONST              13 ('content-location')
        # 1084 LOAD_FAST               12 (response)
        # 1086 CONTAINS_OP              1
        # 1088 POP_JUMP_FORWARD_IF_FALSE     5 (to 1100)
        # 1482        1090 LOAD_FAST                3 (absolute_uri)
        # 1092 LOAD_FAST               12 (response)
        # 1094 LOAD_CONST              13 ('content-location')
        # 1096 STORE_SUBSCR
        # 1483     >> 1100 LOAD_GLOBAL             39 (NULL + _updateCache)
        # 1112 LOAD_FAST                7 (headers)
        # 1114 LOAD_FAST               12 (response)
        # 1116 LOAD_FAST               13 (content)
        # 1118 LOAD_FAST                0 (self)
        # 1120 LOAD_ATTR               20 (cache)
        # 1130 LOAD_FAST                9 (cachekey)
        # 1132 PRECALL                  5
        # 1136 CALL                     5
        # 1146 POP_TOP
        # 1484     >> 1148 LOAD_CONST              14 ('if-none-match')
        # 1150 LOAD_FAST                7 (headers)
        # 1152 CONTAINS_OP              0
        # 1154 POP_JUMP_FORWARD_IF_FALSE     3 (to 1162)
        # 1485        1156 LOAD_FAST                7 (headers)
        # 1158 LOAD_CONST              14 ('if-none-match')
        # 1160 DELETE_SUBSCR
        # 1486     >> 1162 LOAD_CONST              15 ('if-modified-since')
        # 1164 LOAD_FAST                7 (headers)
        # 1166 CONTAINS_OP              0
        # 1168 POP_JUMP_FORWARD_IF_FALSE     3 (to 1176)
        # 1487        1170 LOAD_FAST                7 (headers)
        # 1172 LOAD_CONST              15 ('if-modified-since')
        # 1174 DELETE_SUBSCR
        # 1488     >> 1176 LOAD_CONST              16 ('authorization')
        # 1178 LOAD_FAST                7 (headers)
        # 1180 CONTAINS_OP              0
        # 1182 POP_JUMP_FORWARD_IF_FALSE    10 (to 1204)
        # 1184 LOAD_FAST                0 (self)
        # 1186 LOAD_ATTR               21 (forward_authorization_headers)
        # 1196 POP_JUMP_FORWARD_IF_TRUE     3 (to 1204)
        # 1489        1198 LOAD_FAST                7 (headers)
        # 1200 LOAD_CONST              16 ('authorization')
        # 1202 DELETE_SUBSCR
        # 1490     >> 1204 LOAD_CONST               7 ('location')
        # 1206 LOAD_FAST               12 (response)
        # 1208 CONTAINS_OP              0
        # 1210 POP_JUMP_FORWARD_IF_FALSE    91 (to 1394)
        # 1491        1212 LOAD_FAST               12 (response)
        # 1214 LOAD_CONST               7 ('location')
        # 1216 BINARY_SUBSCR
        # 1226 STORE_FAST              15 (location)
        # 1492        1228 LOAD_GLOBAL             45 (NULL + copy)
        # 1240 LOAD_ATTR               23 (deepcopy)
        # 1250 LOAD_FAST               12 (response)
        # 1252 PRECALL                  1
        # 1256 CALL                     1
        # 1266 STORE_FAST              21 (old_response)
        # 1493        1268 LOAD_CONST              13 ('content-location')
        # 1270 LOAD_FAST               21 (old_response)
        # 1272 CONTAINS_OP              1
        # 1274 POP_JUMP_FORWARD_IF_FALSE     5 (to 1286)
        # 1494        1276 LOAD_FAST                3 (absolute_uri)
        # 1278 LOAD_FAST               21 (old_response)
        # 1280 LOAD_CONST              13 ('content-location')
        # 1282 STORE_SUBSCR
        # 1495     >> 1286 LOAD_FAST                5 (method)
        # 1288 STORE_FAST              22 (redirect_method)
        # 1496        1290 LOAD_FAST               12 (response)
        # 1292 LOAD_ATTR                6 (status)
        # 1302 LOAD_CONST              17 ((302, 303))
        # 1304 CONTAINS_OP              0
        # 1306 POP_JUMP_FORWARD_IF_FALSE     4 (to 1316)
        # 1497        1308 LOAD_CONST              18 ('GET')
        # 1310 STORE_FAST              22 (redirect_method)
        # 1498        1312 LOAD_CONST               4 (None)
        # 1314 STORE_FAST               6 (body)
        # 1499     >> 1316 LOAD_FAST                0 (self)
        # 1318 LOAD_METHOD              2 (request)
        # 1500        1340 LOAD_FAST               15 (location)
        # 1342 LOAD_FAST               22 (redirect_method)
        # 1344 LOAD_FAST                6 (body)
        # 1346 LOAD_FAST                7 (headers)
        # 1348 LOAD_FAST                8 (redirections)
        # 1350 LOAD_CONST               3 (1)
        # 1352 BINARY_OP               10 (-)
        # 1499        1356 KW_NAMES                19
        # 1358 PRECALL                  5
        # 1362 CALL                     5
        # 1372 UNPACK_SEQUENCE          2
        # 1376 STORE_FAST              12 (response)
        # 1378 STORE_FAST              13 (content)
        # 1502        1380 LOAD_FAST               21 (old_response)
        # 1382 LOAD_FAST               12 (response)
        # 1384 STORE_ATTR              24 (previous)
        # >> 1394 JUMP_FORWARD            68 (to 1532)
        # 1504     >> 1396 LOAD_GLOBAL             51 (NULL + RedirectLimit)
        # 1505        1408 LOAD_CONST              20 ('Redirected more times than redirection_limit allows.')
        # 1410 LOAD_FAST               12 (response)
        # 1412 LOAD_FAST               13 (content)
        # 1504        1414 PRECALL                  3
        # 1418 CALL                     3
        # 1428 RAISE_VARARGS            1
        # 1507     >> 1430 LOAD_FAST               12 (response)
        # 1432 LOAD_ATTR                6 (status)
        # 1442 LOAD_CONST              21 ((200, 203))
        # 1444 CONTAINS_OP              0
        # 1446 POP_JUMP_FORWARD_IF_FALSE    42 (to 1532)
        # 1448 LOAD_FAST                5 (method)
        # 1450 LOAD_FAST                0 (self)
        # 1452 LOAD_ATTR               10 (safe_methods)
        # 1462 CONTAINS_OP              0
        # 1464 POP_JUMP_FORWARD_IF_FALSE    33 (to 1532)
        # 1509        1466 LOAD_CONST              13 ('content-location')
        # 1468 LOAD_FAST               12 (response)
        # 1470 CONTAINS_OP              1
        # 1472 POP_JUMP_FORWARD_IF_FALSE     5 (to 1484)
        # 1510        1474 LOAD_FAST                3 (absolute_uri)
        # 1476 LOAD_FAST               12 (response)
        # 1478 LOAD_CONST              13 ('content-location')
        # 1480 STORE_SUBSCR
        # 1511     >> 1484 LOAD_GLOBAL             39 (NULL + _updateCache)
        # 1496 LOAD_FAST                7 (headers)
        # 1498 LOAD_FAST               12 (response)
        # 1500 LOAD_FAST               13 (content)
        # 1502 LOAD_FAST                0 (self)
        # 1504 LOAD_ATTR               20 (cache)
        # 1514 LOAD_FAST                9 (cachekey)
        # 1516 PRECALL                  5
        # 1520 CALL                     5
        # 1530 POP_TOP
        # 1513     >> 1532 LOAD_FAST               12 (response)
        # 1534 LOAD_FAST               13 (content)
        # 1536 BUILD_TUPLE              2
        # 1538 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7E28470, file "httplib2\__init__.py", line 1442>:
        # 0 COPY_FREE_VARS           2
        # 1442           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                37 (to 84)
        # 10 STORE_FAST               1 (auth)
        # 12 PUSH_NULL
        # 14 LOAD_FAST                1 (auth)
        # 16 LOAD_ATTR                0 (inscope)
        # 26 LOAD_DEREF               2 (host)
        # 28 LOAD_DEREF               3 (request_uri)
        # 30 PRECALL                  2
        # 34 CALL                     2
        # 44 POP_JUMP_BACKWARD_IF_FALSE    19 (to 8)
        # 46 PUSH_NULL
        # 48 LOAD_FAST                1 (auth)
        # 50 LOAD_ATTR                1 (depth)
        # 60 LOAD_DEREF               3 (request_uri)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 LOAD_FAST                1 (auth)
        # 78 BUILD_TUPLE              2
        # 80 LIST_APPEND              2
        # 82 JUMP_BACKWARD           38 (to 8)
        # >>   84 RETURN_VALUE

    def _normalize_headers(self, headers):
        # 1515           0 RESUME                   0
        # 1516           2 LOAD_GLOBAL              1 (NULL + _normalize_headers)
        # 14 LOAD_FAST                1 (headers)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 RETURN_VALUE

    def request(self, uri, method, body, headers, redirections, connection_type):
        """ Performs a single HTTP request.
The 'uri' is the URI of the HTTP resource and can begin
with either 'http' or 'https'. The value of 'uri' must be an absolute URI.

The 'method' is the HTTP method to perform, such as GET, POST, DELETE, etc.
There is no restriction on the methods allowed.

The 'body' is the entity body to be sent with the request. It is a string
object.

Any extra headers that are to be sent with the request should be provided in the
'headers' dictionary.

The maximum number of redirect to follow before raising an
exception is 'redirections. The default is 5.

The return value is a tuple of (response, content), the first
being and instance of the 'Response' class, the second being
a string that contains the response entity body.
        """
        # 1522           0 RESUME                   0
        # 1545           2 LOAD_CONST               1 ('')
        # 4 STORE_FAST               7 (conn_key)
        # 1547           6 NOP
        # 1548           8 LOAD_FAST                4 (headers)
        # 10 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 18)
        # 1549          12 BUILD_MAP                0
        # 14 STORE_FAST               4 (headers)
        # 16 JUMP_FORWARD            21 (to 60)
        # 1551     >>   18 LOAD_FAST                0 (self)
        # 20 LOAD_METHOD              0 (_normalize_headers)
        # 42 LOAD_FAST                4 (headers)
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 STORE_FAST               4 (headers)
        # 1553     >>   60 LOAD_CONST               3 ('user-agent')
        # 62 LOAD_FAST                4 (headers)
        # 64 CONTAINS_OP              1
        # 66 POP_JUMP_FORWARD_IF_FALSE    13 (to 94)
        # 1554          68 LOAD_CONST               4 ('Python-httplib2/%s (gzip)')
        # 70 LOAD_GLOBAL              2 (__version__)
        # 82 BINARY_OP                6 (%)
        # 86 LOAD_FAST                4 (headers)
        # 88 LOAD_CONST               3 ('user-agent')
        # 90 STORE_SUBSCR
        # 1556     >>   94 LOAD_GLOBAL              5 (NULL + iri2uri)
        # 106 LOAD_FAST                1 (uri)
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 STORE_FAST               1 (uri)
        # 1559         124 LOAD_FAST                1 (uri)
        # 126 LOAD_METHOD              3 (replace)
        # 148 LOAD_CONST               5 (' ')
        # 150 LOAD_CONST               6 ('%20')
        # 152 PRECALL                  2
        # 156 CALL                     2
        # 166 LOAD_METHOD              3 (replace)
        # 188 LOAD_CONST               7 ('\r')
        # 190 LOAD_CONST               8 ('%0D')
        # 192 PRECALL                  2
        # 196 CALL                     2
        # 206 LOAD_METHOD              3 (replace)
        # 228 LOAD_CONST               9 ('\n')
        # 230 LOAD_CONST              10 ('%0A')
        # 232 PRECALL                  2
        # 236 CALL                     2
        # 246 STORE_FAST               1 (uri)
        # 1561         248 LOAD_GLOBAL              9 (NULL + urlnorm)
        # 260 LOAD_FAST                1 (uri)
        # 262 PRECALL                  1
        # 266 CALL                     1
        # 276 UNPACK_SEQUENCE          4
        # 280 STORE_FAST               8 (scheme)
        # 282 STORE_FAST               9 (authority)
        # 284 STORE_FAST              10 (request_uri)
        # 286 STORE_FAST              11 (defrag_uri)
        # 1563         288 LOAD_FAST                8 (scheme)
        # 290 LOAD_CONST              11 (':')
        # 292 BINARY_OP                0 (+)
        # 296 LOAD_FAST                9 (authority)
        # 298 BINARY_OP                0 (+)
        # 302 STORE_FAST               7 (conn_key)
        # 1564         304 LOAD_FAST                0 (self)
        # 306 LOAD_ATTR                5 (connections)
        # 316 LOAD_METHOD              6 (get)
        # 338 LOAD_FAST                7 (conn_key)
        # 340 PRECALL                  1
        # 344 CALL                     1
        # 354 STORE_FAST              12 (conn)
        # 1565         356 LOAD_FAST               12 (conn)
        # 358 EXTENDED_ARG             1
        # 360 POP_JUMP_FORWARD_IF_NOT_NONE   294 (to 950)
        # 1566         362 LOAD_FAST                6 (connection_type)
        # 364 POP_JUMP_FORWARD_IF_TRUE    13 (to 392)
        # 1567         366 LOAD_GLOBAL             14 (SCHEME_TO_CONNECTION)
        # 378 LOAD_FAST                8 (scheme)
        # 380 BINARY_SUBSCR
        # 390 STORE_FAST               6 (connection_type)
        # 1568     >>  392 LOAD_GLOBAL             17 (NULL + list)
        # 404 LOAD_FAST                0 (self)
        # 406 LOAD_ATTR                9 (certificates)
        # 416 LOAD_METHOD             10 (iter)
        # 438 LOAD_FAST                9 (authority)
        # 440 PRECALL                  1
        # 444 CALL                     1
        # 454 PRECALL                  1
        # 458 CALL                     1
        # 468 STORE_FAST              13 (certs)
        # 1569         470 LOAD_GLOBAL             23 (NULL + issubclass)
        # 482 LOAD_FAST                6 (connection_type)
        # 484 LOAD_GLOBAL             24 (HTTPSConnectionWithTimeout)
        # 496 PRECALL                  2
        # 500 CALL                     2
        # 510 POP_JUMP_FORWARD_IF_FALSE   159 (to 830)
        # 1570         512 LOAD_FAST               13 (certs)
        # 514 POP_JUMP_FORWARD_IF_FALSE    98 (to 712)
        # 1571         516 PUSH_NULL
        # 518 LOAD_FAST                6 (connection_type)
        # 1572         520 LOAD_FAST                9 (authority)
        # 1573         522 LOAD_FAST               13 (certs)
        # 524 LOAD_CONST              12 (0)
        # 526 BINARY_SUBSCR
        # 536 LOAD_CONST              12 (0)
        # 538 BINARY_SUBSCR
        # 1574         548 LOAD_FAST               13 (certs)
        # 550 LOAD_CONST              12 (0)
        # 552 BINARY_SUBSCR
        # 562 LOAD_CONST              13 (1)
        # 564 BINARY_SUBSCR
        # 1575         574 LOAD_FAST                0 (self)
        # 576 LOAD_ATTR               13 (timeout)
        # 1576         586 LOAD_FAST                0 (self)
        # 588 LOAD_ATTR               14 (proxy_info)
        # 1577         598 LOAD_FAST                0 (self)
        # 600 LOAD_ATTR               15 (ca_certs)
        # 1578         610 LOAD_FAST                0 (self)
        # 612 LOAD_ATTR               16 (disable_ssl_certificate_validation)
        # 1579         622 LOAD_FAST                0 (self)
        # 624 LOAD_ATTR               17 (tls_maximum_version)
        # 1580         634 LOAD_FAST                0 (self)
        # 636 LOAD_ATTR               18 (tls_minimum_version)
        # 1581         646 LOAD_FAST               13 (certs)
        # 648 LOAD_CONST              12 (0)
        # 650 BINARY_SUBSCR
        # 660 LOAD_CONST              14 (2)
        # 662 BINARY_SUBSCR
        # 1571         672 KW_NAMES                15
        # 674 PRECALL                 10
        # 678 CALL                    10
        # 688 COPY                     1
        # 690 STORE_FAST              12 (conn)
        # 692 LOAD_FAST                0 (self)
        # 694 LOAD_ATTR                5 (connections)
        # 704 LOAD_FAST                7 (conn_key)
        # 706 STORE_SUBSCR
        # 710 JUMP_FORWARD            93 (to 898)
        # 1584     >>  712 PUSH_NULL
        # 714 LOAD_FAST                6 (connection_type)
        # 1585         716 LOAD_FAST                9 (authority)
        # 1586         718 LOAD_FAST                0 (self)
        # 720 LOAD_ATTR               13 (timeout)
        # 1587         730 LOAD_FAST                0 (self)
        # 732 LOAD_ATTR               14 (proxy_info)
        # 1588         742 LOAD_FAST                0 (self)
        # 744 LOAD_ATTR               15 (ca_certs)
        # 1589         754 LOAD_FAST                0 (self)
        # 756 LOAD_ATTR               16 (disable_ssl_certificate_validation)
        # 1590         766 LOAD_FAST                0 (self)
        # 768 LOAD_ATTR               17 (tls_maximum_version)
        # 1591         778 LOAD_FAST                0 (self)
        # 780 LOAD_ATTR               18 (tls_minimum_version)
        # 1584         790 KW_NAMES                16
        # 792 PRECALL                  7
        # 796 CALL                     7
        # 806 COPY                     1
        # 808 STORE_FAST              12 (conn)
        # 810 LOAD_FAST                0 (self)
        # 812 LOAD_ATTR                5 (connections)
        # 822 LOAD_FAST                7 (conn_key)
        # 824 STORE_SUBSCR
        # 828 JUMP_FORWARD            34 (to 898)
        # 1594     >>  830 PUSH_NULL
        # 832 LOAD_FAST                6 (connection_type)
        # 1595         834 LOAD_FAST                9 (authority)
        # 836 LOAD_FAST                0 (self)
        # 838 LOAD_ATTR               13 (timeout)
        # 848 LOAD_FAST                0 (self)
        # 850 LOAD_ATTR               14 (proxy_info)
        # 1594         860 KW_NAMES                17
        # 862 PRECALL                  3
        # 866 CALL                     3
        # 876 COPY                     1
        # 878 STORE_FAST              12 (conn)
        # 880 LOAD_FAST                0 (self)
        # 882 LOAD_ATTR                5 (connections)
        # 892 LOAD_FAST                7 (conn_key)
        # 894 STORE_SUBSCR
        # 1597     >>  898 LOAD_FAST               12 (conn)
        # 900 LOAD_METHOD             19 (set_debuglevel)
        # 922 LOAD_GLOBAL             40 (debuglevel)
        # 934 PRECALL                  1
        # 938 CALL                     1
        # 948 POP_TOP
        # 1599     >>  950 LOAD_CONST              18 ('range')
        # 952 LOAD_FAST                4 (headers)
        # 954 CONTAINS_OP              1
        # 956 POP_JUMP_FORWARD_IF_FALSE     9 (to 976)
        # 958 LOAD_CONST              19 ('accept-encoding')
        # 960 LOAD_FAST                4 (headers)
        # 962 CONTAINS_OP              1
        # 964 POP_JUMP_FORWARD_IF_FALSE     5 (to 976)
        # 1600         966 LOAD_CONST              20 ('gzip, deflate')
        # 968 LOAD_FAST                4 (headers)
        # 970 LOAD_CONST              19 ('accept-encoding')
        # 972 STORE_SUBSCR
        # 1602     >>  976 LOAD_GLOBAL             42 (email)
        # 988 LOAD_ATTR               22 (message)
        # 998 LOAD_METHOD             23 (Message)
        # 1020 PRECALL                  0
        # 1024 CALL                     0
        # 1034 STORE_FAST              14 (info)
        # 1603        1036 LOAD_CONST               2 (None)
        # 1038 STORE_FAST              15 (cachekey)
        # 1604        1040 LOAD_CONST               2 (None)
        # 1042 STORE_FAST              16 (cached_value)
        # 1605        1044 LOAD_FAST                0 (self)
        # 1046 LOAD_ATTR               24 (cache)
        # 1056 EXTENDED_ARG             1
        # 1058 POP_JUMP_FORWARD_IF_FALSE   262 (to 1584)
        # 1606        1060 LOAD_FAST               11 (defrag_uri)
        # 1062 STORE_FAST              15 (cachekey)
        # 1607        1064 LOAD_FAST                0 (self)
        # 1066 LOAD_ATTR               24 (cache)
        # 1076 LOAD_METHOD              6 (get)
        # 1098 LOAD_FAST               15 (cachekey)
        # 1100 PRECALL                  1
        # 1104 CALL                     1
        # 1114 STORE_FAST              16 (cached_value)
        # 1608        1116 LOAD_FAST               16 (cached_value)
        # 1118 POP_JUMP_FORWARD_IF_FALSE   232 (to 1584)
        # 1609        1120 NOP
        # 1610        1122 LOAD_FAST               16 (cached_value)
        # 1124 LOAD_METHOD             25 (split)
        # 1146 LOAD_CONST              21 (b'\r\n\r\n')
        # 1148 LOAD_CONST              13 (1)
        # 1150 PRECALL                  2
        # 1154 CALL                     2
        # 1164 UNPACK_SEQUENCE          2
        # 1168 STORE_FAST              14 (info)
        # 1170 STORE_FAST              17 (content)
        # 1611        1172 LOAD_GLOBAL             43 (NULL + email)
        # 1184 LOAD_ATTR               26 (message_from_bytes)
        # 1194 LOAD_FAST               14 (info)
        # 1196 PRECALL                  1
        # 1200 CALL                     1
        # 1210 STORE_FAST              14 (info)
        # 1612        1212 LOAD_FAST               14 (info)
        # 1214 LOAD_METHOD             27 (items)
        # 1236 PRECALL                  0
        # 1240 CALL                     0
        # 1250 GET_ITER
        # >> 1252 FOR_ITER               111 (to 1476)
        # 1254 UNPACK_SEQUENCE          2
        # 1258 STORE_FAST              18 (k)
        # 1260 STORE_FAST              19 (v)
        # 1613        1262 LOAD_FAST               19 (v)
        # 1264 LOAD_METHOD             28 (startswith)
        # 1286 LOAD_CONST              22 ('=?')
        # 1288 PRECALL                  1
        # 1292 CALL                     1
        # 1302 POP_JUMP_FORWARD_IF_FALSE    85 (to 1474)
        # 1304 LOAD_FAST               19 (v)
        # 1306 LOAD_METHOD             29 (endswith)
        # 1328 LOAD_CONST              23 ('?=')
        # 1330 PRECALL                  1
        # 1334 CALL                     1
        # 1344 POP_JUMP_FORWARD_IF_FALSE    64 (to 1474)
        # 1614        1346 LOAD_FAST               14 (info)
        # 1348 LOAD_METHOD             30 (replace_header)
        # 1370 LOAD_FAST               18 (k)
        # 1372 LOAD_GLOBAL             63 (NULL + str)
        # 1384 LOAD_GLOBAL             42 (email)
        # 1396 LOAD_ATTR               32 (header)
        # 1406 LOAD_METHOD             33 (decode_header)
        # 1428 LOAD_FAST               19 (v)
        # 1430 PRECALL                  1
        # 1434 CALL                     1
        # 1444 LOAD_CONST              12 (0)
        # 1446 BINARY_SUBSCR
        # 1456 CALL_FUNCTION_EX         0
        # 1458 PRECALL                  2
        # 1462 CALL                     2
        # 1472 POP_TOP
        # >> 1474 JUMP_BACKWARD          112 (to 1252)
        # 1612     >> 1476 JUMP_FORWARD            53 (to 1584)
        # >> 1478 PUSH_EXC_INFO
        # 1615        1480 LOAD_GLOBAL             68 (IndexError)
        # 1492 LOAD_GLOBAL             70 (ValueError)
        # 1504 BUILD_TUPLE              2
        # 1506 CHECK_EXC_MATCH
        # 1508 POP_JUMP_FORWARD_IF_FALSE    33 (to 1576)
        # 1510 POP_TOP
        # 1616        1512 LOAD_FAST                0 (self)
        # 1514 LOAD_ATTR               24 (cache)
        # 1524 LOAD_METHOD             36 (delete)
        # 1546 LOAD_FAST               15 (cachekey)
        # 1548 PRECALL                  1
        # 1552 CALL                     1
        # 1562 POP_TOP
        # 1617        1564 LOAD_CONST               2 (None)
        # 1566 STORE_FAST              15 (cachekey)
        # 1618        1568 LOAD_CONST               2 (None)
        # 1570 STORE_FAST              16 (cached_value)
        # 1572 POP_EXCEPT
        # 1574 JUMP_FORWARD             4 (to 1584)
        # 1615     >> 1576 RERAISE                  0
        # >> 1578 COPY                     3
        # 1580 POP_EXCEPT
        # 1582 RERAISE                  1
        # 1621     >> 1584 LOAD_FAST                2 (method)
        # 1586 LOAD_FAST                0 (self)
        # 1588 LOAD_ATTR               37 (optimistic_concurrency_methods)
        # 1598 CONTAINS_OP              0
        # 1600 POP_JUMP_FORWARD_IF_FALSE    33 (to 1668)
        # 1622        1602 LOAD_FAST                0 (self)
        # 1604 LOAD_ATTR               24 (cache)
        # 1621        1614 POP_JUMP_FORWARD_IF_FALSE    26 (to 1668)
        # 1623        1616 LOAD_CONST              24 ('etag')
        # 1618 LOAD_FAST               14 (info)
        # 1620 CONTAINS_OP              0
        # 1622 POP_JUMP_FORWARD_IF_FALSE    22 (to 1668)
        # 1624        1624 LOAD_FAST                0 (self)
        # 1626 LOAD_ATTR               38 (ignore_etag)
        # 1623        1636 POP_JUMP_FORWARD_IF_TRUE    15 (to 1668)
        # 1625        1638 LOAD_CONST              25 ('if-match')
        # 1640 LOAD_FAST                4 (headers)
        # 1642 CONTAINS_OP              1
        # 1644 POP_JUMP_FORWARD_IF_FALSE    11 (to 1668)
        # 1628        1646 LOAD_FAST               14 (info)
        # 1648 LOAD_CONST              24 ('etag')
        # 1650 BINARY_SUBSCR
        # 1660 LOAD_FAST                4 (headers)
        # 1662 LOAD_CONST              25 ('if-match')
        # 1664 STORE_SUBSCR
        # 1633     >> 1668 LOAD_FAST                0 (self)
        # 1670 LOAD_ATTR               24 (cache)
        # 1680 POP_JUMP_FORWARD_IF_FALSE    37 (to 1756)
        # 1682 LOAD_FAST               15 (cachekey)
        # 1684 POP_JUMP_FORWARD_IF_FALSE    35 (to 1756)
        # 1686 LOAD_FAST                2 (method)
        # 1688 LOAD_FAST                0 (self)
        # 1690 LOAD_ATTR               39 (safe_methods)
        # 1700 CONTAINS_OP              1
        # 1702 POP_JUMP_FORWARD_IF_FALSE    26 (to 1756)
        # 1634        1704 LOAD_FAST                0 (self)
        # 1706 LOAD_ATTR               24 (cache)
        # 1716 LOAD_METHOD             36 (delete)
        # 1738 LOAD_FAST               15 (cachekey)
        # 1740 PRECALL                  1
        # 1744 CALL                     1
        # 1754 POP_TOP
        # 1638     >> 1756 LOAD_FAST                2 (method)
        # 1758 LOAD_FAST                0 (self)
        # 1760 LOAD_ATTR               39 (safe_methods)
        # 1770 CONTAINS_OP              0
        # 1772 POP_JUMP_FORWARD_IF_FALSE   119 (to 2012)
        # 1774 LOAD_CONST              26 ('vary')
        # 1776 LOAD_FAST               14 (info)
        # 1778 CONTAINS_OP              0
        # 1780 POP_JUMP_FORWARD_IF_FALSE   115 (to 2012)
        # 1639        1782 LOAD_FAST               14 (info)
        # 1784 LOAD_CONST              26 ('vary')
        # 1786 BINARY_SUBSCR
        # 1796 STORE_FAST              20 (vary)
        # 1640        1798 LOAD_FAST               20 (vary)
        # 1800 LOAD_METHOD             40 (lower)
        # 1822 PRECALL                  0
        # 1826 CALL                     0
        # 1836 LOAD_METHOD              3 (replace)
        # 1858 LOAD_CONST               5 (' ')
        # 1860 LOAD_CONST               1 ('')
        # 1862 PRECALL                  2
        # 1866 CALL                     2
        # 1876 LOAD_METHOD             25 (split)
        # 1898 LOAD_CONST              27 (',')
        # 1900 PRECALL                  1
        # 1904 CALL                     1
        # 1914 STORE_FAST              21 (vary_headers)
        # 1641        1916 LOAD_FAST               21 (vary_headers)
        # 1918 GET_ITER
        # >> 1920 FOR_ITER                45 (to 2012)
        # 1922 STORE_FAST              22 (header)
        # 1642        1924 LOAD_CONST              28 ('-varied-%s')
        # 1926 LOAD_FAST               22 (header)
        # 1928 BINARY_OP                6 (%)
        # 1932 STORE_FAST              23 (key)
        # 1643        1934 LOAD_FAST               14 (info)
        # 1936 LOAD_FAST               23 (key)
        # 1938 BINARY_SUBSCR
        # 1948 STORE_FAST              24 (value)
        # 1644        1950 LOAD_FAST                4 (headers)
        # 1952 LOAD_METHOD              6 (get)
        # 1974 LOAD_FAST               22 (header)
        # 1976 LOAD_CONST               2 (None)
        # 1978 PRECALL                  2
        # 1982 CALL                     2
        # 1992 LOAD_FAST               24 (value)
        # 1994 COMPARE_OP               3 (!=)
        # 2000 POP_JUMP_FORWARD_IF_FALSE     4 (to 2010)
        # 1645        2002 LOAD_CONST               2 (None)
        # 2004 STORE_FAST              16 (cached_value)
        # 1646        2006 POP_TOP
        # 2008 JUMP_FORWARD             1 (to 2012)
        # 1644     >> 2010 JUMP_BACKWARD           46 (to 1920)
        # 1649     >> 2012 LOAD_FAST                0 (self)
        # 2014 LOAD_ATTR               24 (cache)
        # 1648        2024 EXTENDED_ARG             1
        # 2026 POP_JUMP_FORWARD_IF_FALSE   453 (to 2934)
        # 1650        2028 LOAD_FAST               16 (cached_value)
        # 1648        2030 EXTENDED_ARG             1
        # 2032 POP_JUMP_FORWARD_IF_FALSE   450 (to 2934)
        # 1651        2034 LOAD_FAST                2 (method)
        # 2036 LOAD_FAST                0 (self)
        # 2038 LOAD_ATTR               39 (safe_methods)
        # 2048 CONTAINS_OP              0
        # 2050 POP_JUMP_FORWARD_IF_TRUE    13 (to 2078)
        # 2052 LOAD_FAST               14 (info)
        # 2054 LOAD_CONST              29 ('status')
        # 2056 BINARY_SUBSCR
        # 2066 LOAD_CONST              30 ('308')
        # 2068 COMPARE_OP               2 (==)
        # 2074 EXTENDED_ARG             1
        # 2076 POP_JUMP_FORWARD_IF_FALSE   428 (to 2934)
        # 1652     >> 2078 LOAD_CONST              18 ('range')
        # 2080 LOAD_FAST                4 (headers)
        # 2082 CONTAINS_OP              1
        # 2084 EXTENDED_ARG             1
        # 2086 POP_JUMP_FORWARD_IF_FALSE   423 (to 2934)
        # 1654        2088 LOAD_FAST                2 (method)
        # 2090 STORE_FAST              25 (redirect_method)
        # 1655        2092 LOAD_FAST               14 (info)
        # 2094 LOAD_CONST              29 ('status')
        # 2096 BINARY_SUBSCR
        # 2106 LOAD_CONST              31 (('307', '308'))
        # 2108 CONTAINS_OP              1
        # 2110 POP_JUMP_FORWARD_IF_FALSE     2 (to 2116)
        # 1656        2112 LOAD_CONST              32 ('GET')
        # 2114 STORE_FAST              25 (redirect_method)
        # 1657     >> 2116 LOAD_CONST              33 ('-x-permanent-redirect-url')
        # 2118 LOAD_FAST               14 (info)
        # 2120 CONTAINS_OP              0
        # 2122 POP_JUMP_FORWARD_IF_FALSE    93 (to 2310)
        # 1659        2124 LOAD_FAST                5 (redirections)
        # 2126 LOAD_CONST              12 (0)
        # 2128 COMPARE_OP               1 (<=)
        # 2134 POP_JUMP_FORWARD_IF_FALSE    17 (to 2170)
        # 1660        2136 LOAD_GLOBAL             83 (NULL + RedirectLimit)
        # 1661        2148 LOAD_CONST              34 ('Redirected more times than redirection_limit allows.')
        # 2150 BUILD_MAP                0
        # 2152 LOAD_CONST               1 ('')
        # 1660        2154 PRECALL                  3
        # 2158 CALL                     3
        # 2168 RAISE_VARARGS            1
        # 1663     >> 2170 LOAD_FAST                0 (self)
        # 2172 LOAD_METHOD             42 (request)
        # 1664        2194 LOAD_FAST               14 (info)
        # 2196 LOAD_CONST              33 ('-x-permanent-redirect-url')
        # 2198 BINARY_SUBSCR
        # 1665        2208 LOAD_FAST               25 (redirect_method)
        # 1666        2210 LOAD_FAST                4 (headers)
        # 1667        2212 LOAD_FAST                5 (redirections)
        # 2214 LOAD_CONST              13 (1)
        # 2216 BINARY_OP               10 (-)
        # 1663        2220 KW_NAMES                35
        # 2222 PRECALL                  4
        # 2226 CALL                     4
        # 2236 UNPACK_SEQUENCE          2
        # 2240 STORE_FAST              26 (response)
        # 2242 STORE_FAST              27 (new_content)
        # 1669        2244 LOAD_GLOBAL             87 (NULL + Response)
        # 2256 LOAD_FAST               14 (info)
        # 2258 PRECALL                  1
        # 2262 CALL                     1
        # 2272 LOAD_FAST               26 (response)
        # 2274 STORE_ATTR              44 (previous)
        # 1670        2284 LOAD_CONST              36 (True)
        # 2286 LOAD_FAST               26 (response)
        # 2288 LOAD_ATTR               44 (previous)
        # 2298 STORE_ATTR              45 (fromcache)
        # 2308 JUMP_FORWARD           139 (to 2588)
        # 1680     >> 2310 LOAD_GLOBAL             93 (NULL + _entry_disposition)
        # 2322 LOAD_FAST               14 (info)
        # 2324 LOAD_FAST                4 (headers)
        # 2326 PRECALL                  2
        # 2330 CALL                     2
        # 2340 STORE_FAST              28 (entry_disposition)
        # 1682        2342 LOAD_FAST               28 (entry_disposition)
        # 2344 LOAD_CONST              37 ('FRESH')
        # 2346 COMPARE_OP               2 (==)
        # 2352 POP_JUMP_FORWARD_IF_FALSE    26 (to 2406)
        # 1683        2354 LOAD_GLOBAL             87 (NULL + Response)
        # 2366 LOAD_FAST               14 (info)
        # 2368 PRECALL                  1
        # 2372 CALL                     1
        # 2382 STORE_FAST              26 (response)
        # 1684        2384 LOAD_CONST              36 (True)
        # 2386 LOAD_FAST               26 (response)
        # 2388 STORE_ATTR              45 (fromcache)
        # 1685        2398 LOAD_FAST               26 (response)
        # 2400 LOAD_FAST               17 (content)
        # 2402 BUILD_TUPLE              2
        # 2404 RETURN_VALUE
        # 1687     >> 2406 LOAD_FAST               28 (entry_disposition)
        # 2408 LOAD_CONST              38 ('STALE')
        # 2410 COMPARE_OP               2 (==)
        # 2416 POP_JUMP_FORWARD_IF_FALSE    46 (to 2510)
        # 1688        2418 LOAD_CONST              24 ('etag')
        # 2420 LOAD_FAST               14 (info)
        # 2422 CONTAINS_OP              0
        # 2424 POP_JUMP_FORWARD_IF_FALSE    22 (to 2470)
        # 2426 LOAD_FAST                0 (self)
        # 2428 LOAD_ATTR               38 (ignore_etag)
        # 2438 POP_JUMP_FORWARD_IF_TRUE    15 (to 2470)
        # 2440 LOAD_CONST              39 ('if-none-match')
        # 2442 LOAD_FAST                4 (headers)
        # 2444 CONTAINS_OP              1
        # 2446 POP_JUMP_FORWARD_IF_FALSE    11 (to 2470)
        # 1689        2448 LOAD_FAST               14 (info)
        # 2450 LOAD_CONST              24 ('etag')
        # 2452 BINARY_SUBSCR
        # 2462 LOAD_FAST                4 (headers)
        # 2464 LOAD_CONST              39 ('if-none-match')
        # 2466 STORE_SUBSCR
        # 1690     >> 2470 LOAD_CONST              40 ('last-modified')
        # 2472 LOAD_FAST               14 (info)
        # 2474 CONTAINS_OP              0
        # 2476 POP_JUMP_FORWARD_IF_FALSE    15 (to 2508)
        # 2478 LOAD_CONST              40 ('last-modified')
        # 2480 LOAD_FAST                4 (headers)
        # 2482 CONTAINS_OP              1
        # 2484 POP_JUMP_FORWARD_IF_FALSE    11 (to 2508)
        # 1691        2486 LOAD_FAST               14 (info)
        # 2488 LOAD_CONST              40 ('last-modified')
        # 2490 BINARY_SUBSCR
        # 2500 LOAD_FAST                4 (headers)
        # 2502 LOAD_CONST              41 ('if-modified-since')
        # 2504 STORE_SUBSCR
        # >> 2508 JUMP_FORWARD             7 (to 2524)
        # 1692     >> 2510 LOAD_FAST               28 (entry_disposition)
        # 2512 LOAD_CONST              42 ('TRANSPARENT')
        # 2514 COMPARE_OP               2 (==)
        # 2520 POP_JUMP_FORWARD_IF_FALSE     1 (to 2524)
        # 1693        2522 NOP
        # 1695     >> 2524 LOAD_FAST                0 (self)
        # 2526 LOAD_METHOD             47 (_request)
        # 1696        2548 LOAD_FAST               12 (conn)
        # 2550 LOAD_FAST                9 (authority)
        # 2552 LOAD_FAST                1 (uri)
        # 2554 LOAD_FAST               10 (request_uri)
        # 2556 LOAD_FAST                2 (method)
        # 2558 LOAD_FAST                3 (body)
        # 2560 LOAD_FAST                4 (headers)
        # 2562 LOAD_FAST                5 (redirections)
        # 2564 LOAD_FAST               15 (cachekey)
        # 1695        2566 PRECALL                  9
        # 2570 CALL                     9
        # 2580 UNPACK_SEQUENCE          2
        # 2584 STORE_FAST              26 (response)
        # 2586 STORE_FAST              27 (new_content)
        # 1699     >> 2588 LOAD_FAST               26 (response)
        # 2590 LOAD_ATTR               48 (status)
        # 2600 LOAD_CONST              43 (304)
        # 2602 COMPARE_OP               2 (==)
        # 2608 POP_JUMP_FORWARD_IF_FALSE   119 (to 2848)
        # 2610 LOAD_FAST                2 (method)
        # 2612 LOAD_CONST              32 ('GET')
        # 2614 COMPARE_OP               2 (==)
        # 2620 POP_JUMP_FORWARD_IF_FALSE   113 (to 2848)
        # 1705        2622 LOAD_GLOBAL             99 (NULL + _get_end2end_headers)
        # 2634 LOAD_FAST               26 (response)
        # 2636 PRECALL                  1
        # 2640 CALL                     1
        # 2650 GET_ITER
        # >> 2652 FOR_ITER                13 (to 2680)
        # 2654 STORE_FAST              23 (key)
        # 1706        2656 LOAD_FAST               26 (response)
        # 2658 LOAD_FAST               23 (key)
        # 2660 BINARY_SUBSCR
        # 2670 LOAD_FAST               14 (info)
        # 2672 LOAD_FAST               23 (key)
        # 2674 STORE_SUBSCR
        # 2678 JUMP_BACKWARD           14 (to 2652)
        # 1707     >> 2680 LOAD_GLOBAL             87 (NULL + Response)
        # 2692 LOAD_FAST               14 (info)
        # 2694 PRECALL                  1
        # 2698 CALL                     1
        # 2708 STORE_FAST              29 (merged_response)
        # 1708        2710 LOAD_GLOBAL            101 (NULL + hasattr)
        # 2722 LOAD_FAST               26 (response)
        # 2724 LOAD_CONST              44 ('_stale_digest')
        # 2726 PRECALL                  2
        # 2730 CALL                     2
        # 2740 POP_JUMP_FORWARD_IF_FALSE    12 (to 2766)
        # 1709        2742 LOAD_FAST               26 (response)
        # 2744 LOAD_ATTR               51 (_stale_digest)
        # 2754 LOAD_FAST               29 (merged_response)
        # 2756 STORE_ATTR              51 (_stale_digest)
        # 1710     >> 2766 LOAD_GLOBAL            105 (NULL + _updateCache)
        # 2778 LOAD_FAST                4 (headers)
        # 2780 LOAD_FAST               29 (merged_response)
        # 2782 LOAD_FAST               17 (content)
        # 2784 LOAD_FAST                0 (self)
        # 2786 LOAD_ATTR               24 (cache)
        # 2796 LOAD_FAST               15 (cachekey)
        # 2798 PRECALL                  5
        # 2802 CALL                     5
        # 2812 POP_TOP
        # 1711        2814 LOAD_FAST               29 (merged_response)
        # 2816 STORE_FAST              26 (response)
        # 1712        2818 LOAD_CONST              45 (200)
        # 2820 LOAD_FAST               26 (response)
        # 2822 STORE_ATTR              48 (status)
        # 1713        2832 LOAD_CONST              36 (True)
        # 2834 LOAD_FAST               26 (response)
        # 2836 STORE_ATTR              45 (fromcache)
        # 2846 JUMP_FORWARD           117 (to 3082)
        # 1715     >> 2848 LOAD_FAST               26 (response)
        # 2850 LOAD_ATTR               48 (status)
        # 2860 LOAD_CONST              45 (200)
        # 2862 COMPARE_OP               2 (==)
        # 2868 POP_JUMP_FORWARD_IF_FALSE     3 (to 2876)
        # 1716        2870 LOAD_FAST               27 (new_content)
        # 2872 STORE_FAST              17 (content)
        # 2874 JUMP_FORWARD           103 (to 3082)
        # 1718     >> 2876 LOAD_FAST                0 (self)
        # 2878 LOAD_ATTR               24 (cache)
        # 2888 LOAD_METHOD             36 (delete)
        # 2910 LOAD_FAST               15 (cachekey)
        # 2912 PRECALL                  1
        # 2916 CALL                     1
        # 2926 POP_TOP
        # 1719        2928 LOAD_FAST               27 (new_content)
        # 2930 STORE_FAST              17 (content)
        # 2932 JUMP_FORWARD            74 (to 3082)
        # 1721     >> 2934 LOAD_GLOBAL            107 (NULL + _parse_cache_control)
        # 2946 LOAD_FAST                4 (headers)
        # 2948 PRECALL                  1
        # 2952 CALL                     1
        # 2962 STORE_FAST              30 (cc)
        # 1722        2964 LOAD_CONST              46 ('only-if-cached')
        # 2966 LOAD_FAST               30 (cc)
        # 2968 CONTAINS_OP              0
        # 2970 POP_JUMP_FORWARD_IF_FALSE    23 (to 3018)
        # 1723        2972 LOAD_CONST              47 ('504')
        # 2974 LOAD_FAST               14 (info)
        # 2976 LOAD_CONST              29 ('status')
        # 2978 STORE_SUBSCR
        # 1724        2982 LOAD_GLOBAL             87 (NULL + Response)
        # 2994 LOAD_FAST               14 (info)
        # 2996 PRECALL                  1
        # 3000 CALL                     1
        # 3010 STORE_FAST              26 (response)
        # 1725        3012 LOAD_CONST              48 (b'')
        # 3014 STORE_FAST              17 (content)
        # 3016 JUMP_FORWARD            32 (to 3082)
        # 1727     >> 3018 LOAD_FAST                0 (self)
        # 3020 LOAD_METHOD             47 (_request)
        # 1728        3042 LOAD_FAST               12 (conn)
        # 3044 LOAD_FAST                9 (authority)
        # 3046 LOAD_FAST                1 (uri)
        # 3048 LOAD_FAST               10 (request_uri)
        # 3050 LOAD_FAST                2 (method)
        # 3052 LOAD_FAST                3 (body)
        # 3054 LOAD_FAST                4 (headers)
        # 3056 LOAD_FAST                5 (redirections)
        # 3058 LOAD_FAST               15 (cachekey)
        # 1727        3060 PRECALL                  9
        # 3064 CALL                     9
        # 3074 UNPACK_SEQUENCE          2
        # 3078 STORE_FAST              26 (response)
        # 3080 STORE_FAST              17 (content)
        # >> 3082 EXTENDED_ARG             1
        # 3084 JUMP_FORWARD           314 (to 3714)
        # >> 3086 PUSH_EXC_INFO
        # 1730        3088 LOAD_GLOBAL            108 (Exception)
        # 3100 CHECK_EXC_MATCH
        # 3102 EXTENDED_ARG             1
        # 3104 POP_JUMP_FORWARD_IF_FALSE   300 (to 3706)
        # 3106 STORE_FAST              31 (e)
        # 1731        3108 LOAD_GLOBAL            111 (NULL + isinstance)
        # 3120 LOAD_FAST               31 (e)
        # 3122 LOAD_GLOBAL            112 (socket)
        # 3134 LOAD_ATTR               13 (timeout)
        # 3144 PRECALL                  2
        # 3148 CALL                     2
        # 3158 STORE_FAST              32 (is_timeout)
        # 1732        3160 LOAD_FAST               32 (is_timeout)
        # 3162 POP_JUMP_FORWARD_IF_FALSE    49 (to 3262)
        # 1733        3164 LOAD_FAST                0 (self)
        # 3166 LOAD_ATTR                5 (connections)
        # 3176 LOAD_METHOD             57 (pop)
        # 3198 LOAD_FAST                7 (conn_key)
        # 3200 LOAD_CONST               2 (None)
        # 3202 PRECALL                  2
        # 3206 CALL                     2
        # 3216 STORE_FAST              12 (conn)
        # 1734        3218 LOAD_FAST               12 (conn)
        # 3220 POP_JUMP_FORWARD_IF_FALSE    20 (to 3262)
        # 1735        3222 LOAD_FAST               12 (conn)
        # 3224 LOAD_METHOD             58 (close)
        # 3246 PRECALL                  0
        # 3250 CALL                     0
        # 3260 POP_TOP
        # 1737     >> 3262 LOAD_FAST                0 (self)
        # 3264 LOAD_ATTR               59 (force_exception_to_status_code)
        # 3274 POP_JUMP_FORWARD_IF_FALSE   205 (to 3686)
        # 1738        3276 LOAD_GLOBAL            111 (NULL + isinstance)
        # 3288 LOAD_FAST               31 (e)
        # 3290 LOAD_GLOBAL            120 (HttpLib2ErrorWithResponse)
        # 3302 PRECALL                  2
        # 3306 CALL                     2
        # 3316 POP_JUMP_FORWARD_IF_FALSE    42 (to 3402)
        # 1739        3318 LOAD_FAST               31 (e)
        # 3320 LOAD_ATTR               61 (response)
        # 3330 STORE_FAST              26 (response)
        # 1740        3332 LOAD_FAST               31 (e)
        # 3334 LOAD_ATTR               62 (content)
        # 3344 STORE_FAST              17 (content)
        # 1741        3346 LOAD_CONST              49 (500)
        # 3348 LOAD_FAST               26 (response)
        # 3350 STORE_ATTR              48 (status)
        # 1742        3360 LOAD_GLOBAL             63 (NULL + str)
        # 3372 LOAD_FAST               31 (e)
        # 3374 PRECALL                  1
        # 3378 CALL                     1
        # 3388 LOAD_FAST               26 (response)
        # 3390 STORE_ATTR              63 (reason)
        # 3400 JUMP_FORWARD           143 (to 3688)
        # 1743     >> 3402 LOAD_GLOBAL            111 (NULL + isinstance)
        # 3414 LOAD_FAST               31 (e)
        # 3416 LOAD_GLOBAL            112 (socket)
        # 3428 LOAD_ATTR               13 (timeout)
        # 3438 PRECALL                  2
        # 3442 CALL                     2
        # 3452 POP_JUMP_FORWARD_IF_FALSE    42 (to 3538)
        # 1744        3454 LOAD_CONST              50 (b'Request Timeout')
        # 3456 STORE_FAST              17 (content)
        # 1745        3458 LOAD_GLOBAL             87 (NULL + Response)
        # 3470 LOAD_CONST              51 ('text/plain')
        # 3472 LOAD_CONST              52 ('408')
        # 3474 LOAD_GLOBAL            129 (NULL + len)
        # 3486 LOAD_FAST               17 (content)
        # 3488 PRECALL                  1
        # 3492 CALL                     1
        # 3502 LOAD_CONST              53 (('content-type', 'status', 'content-length'))
        # 3504 BUILD_CONST_KEY_MAP      3
        # 3506 PRECALL                  1
        # 3510 CALL                     1
        # 3520 STORE_FAST              26 (response)
        # 1746        3522 LOAD_CONST              54 ('Request Timeout')
        # 3524 LOAD_FAST               26 (response)
        # 3526 STORE_ATTR              63 (reason)
        # 3536 JUMP_FORWARD            75 (to 3688)
        # 1748     >> 3538 LOAD_GLOBAL             63 (NULL + str)
        # 3550 LOAD_FAST               31 (e)
        # 3552 PRECALL                  1
        # 3556 CALL                     1
        # 3566 LOAD_METHOD             65 (encode)
        # 3588 LOAD_CONST              55 ('utf-8')
        # 3590 PRECALL                  1
        # 3594 CALL                     1
        # 3604 STORE_FAST              17 (content)
        # 1749        3606 LOAD_GLOBAL             87 (NULL + Response)
        # 3618 LOAD_CONST              51 ('text/plain')
        # 3620 LOAD_CONST              56 ('400')
        # 3622 LOAD_GLOBAL            129 (NULL + len)
        # 3634 LOAD_FAST               17 (content)
        # 3636 PRECALL                  1
        # 3640 CALL                     1
        # 3650 LOAD_CONST              53 (('content-type', 'status', 'content-length'))
        # 3652 BUILD_CONST_KEY_MAP      3
        # 3654 PRECALL                  1
        # 3658 CALL                     1
        # 3668 STORE_FAST              26 (response)
        # 1750        3670 LOAD_CONST              57 ('Bad Request')
        # 3672 LOAD_FAST               26 (response)
        # 3674 STORE_ATTR              63 (reason)
        # 3684 JUMP_FORWARD             1 (to 3688)
        # 1752     >> 3686 RAISE_VARARGS            0
        # >> 3688 POP_EXCEPT
        # 3690 LOAD_CONST               2 (None)
        # 3692 STORE_FAST              31 (e)
        # 3694 DELETE_FAST             31 (e)
        # 3696 JUMP_FORWARD             8 (to 3714)
        # >> 3698 LOAD_CONST               2 (None)
        # 3700 STORE_FAST              31 (e)
        # 3702 DELETE_FAST             31 (e)
        # 3704 RERAISE                  1
        # 1730     >> 3706 RERAISE                  0
        # >> 3708 COPY                     3
        # 3710 POP_EXCEPT
        # 3712 RERAISE                  1
        # 1754     >> 3714 LOAD_FAST               26 (response)
        # 3716 LOAD_FAST               17 (content)
        # 3718 BUILD_TUPLE              2
        # 3720 RETURN_VALUE
        # ExceptionTable:
        # 8 to 1118 -> 3086 [0]
        # 1122 to 1474 -> 1478 [0]
        # 1476 to 1476 -> 3086 [0]
        # 1478 to 1570 -> 1578 [1] lasti
        # 1572 to 1574 -> 3086 [0]
        # 1576 to 1576 -> 1578 [1] lasti
        # 1578 to 2402 -> 3086 [0]
        # 2406 to 3080 -> 3086 [0]
        # 3086 to 3106 -> 3708 [1] lasti
        # 3108 to 3686 -> 3698 [1] lasti
        # 3698 to 3706 -> 3708 [1] lasti


class Response:
    """Response"""
    def __init__(self, info):
        # 1775           0 RESUME                   0
        # 1778           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (info)
        # 16 LOAD_GLOBAL              2 (http)
        # 28 LOAD_ATTR                2 (client)
        # 38 LOAD_ATTR                3 (HTTPResponse)
        # 48 PRECALL                  2
        # 52 CALL                     2
        # 62 POP_JUMP_FORWARD_IF_FALSE   158 (to 380)
        # 1779          64 LOAD_FAST                1 (info)
        # 66 LOAD_METHOD              4 (getheaders)
        # 88 PRECALL                  0
        # 92 CALL                     0
        # 102 GET_ITER
        # >>  104 FOR_ITER                76 (to 258)
        # 106 UNPACK_SEQUENCE          2
        # 110 STORE_FAST               2 (key)
        # 112 STORE_FAST               3 (value)
        # 1780         114 LOAD_FAST                2 (key)
        # 116 LOAD_METHOD              5 (lower)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 STORE_FAST               2 (key)
        # 1781         154 LOAD_FAST                0 (self)
        # 156 LOAD_METHOD              6 (get)
        # 178 LOAD_FAST                2 (key)
        # 180 PRECALL                  1
        # 184 CALL                     1
        # 194 STORE_FAST               4 (prev)
        # 1782         196 LOAD_FAST                4 (prev)
        # 198 POP_JUMP_FORWARD_IF_NONE    23 (to 246)
        # 1783         200 LOAD_CONST               1 (', ')
        # 202 LOAD_METHOD              7 (join)
        # 224 LOAD_FAST                4 (prev)
        # 226 LOAD_FAST                3 (value)
        # 228 BUILD_TUPLE              2
        # 230 PRECALL                  1
        # 234 CALL                     1
        # 244 STORE_FAST               3 (value)
        # 1784     >>  246 LOAD_FAST                3 (value)
        # 248 LOAD_FAST                0 (self)
        # 250 LOAD_FAST                2 (key)
        # 252 STORE_SUBSCR
        # 256 JUMP_BACKWARD           77 (to 104)
        # 1785     >>  258 LOAD_FAST                1 (info)
        # 260 LOAD_ATTR                8 (status)
        # 270 LOAD_FAST                0 (self)
        # 272 STORE_ATTR               8 (status)
        # 1786         282 LOAD_GLOBAL             19 (NULL + str)
        # 294 LOAD_FAST                0 (self)
        # 296 LOAD_ATTR                8 (status)
        # 306 PRECALL                  1
        # 310 CALL                     1
        # 320 LOAD_FAST                0 (self)
        # 322 LOAD_CONST               2 ('status')
        # 324 STORE_SUBSCR
        # 1787         328 LOAD_FAST                1 (info)
        # 330 LOAD_ATTR               10 (reason)
        # 340 LOAD_FAST                0 (self)
        # 342 STORE_ATTR              10 (reason)
        # 1788         352 LOAD_FAST                1 (info)
        # 354 LOAD_ATTR               11 (version)
        # 364 LOAD_FAST                0 (self)
        # 366 STORE_ATTR              11 (version)
        # 376 LOAD_CONST               0 (None)
        # 378 RETURN_VALUE
        # 1789     >>  380 LOAD_GLOBAL              1 (NULL + isinstance)
        # 392 LOAD_FAST                1 (info)
        # 394 LOAD_GLOBAL             24 (email)
        # 406 LOAD_ATTR               13 (message)
        # 416 LOAD_ATTR               14 (Message)
        # 426 PRECALL                  2
        # 430 CALL                     2
        # 440 POP_JUMP_FORWARD_IF_FALSE    90 (to 622)
        # 1790         442 LOAD_GLOBAL             31 (NULL + list)
        # 454 LOAD_FAST                1 (info)
        # 456 LOAD_METHOD             16 (items)
        # 478 PRECALL                  0
        # 482 CALL                     0
        # 492 PRECALL                  1
        # 496 CALL                     1
        # 506 GET_ITER
        # >>  508 FOR_ITER                28 (to 566)
        # 510 UNPACK_SEQUENCE          2
        # 514 STORE_FAST               2 (key)
        # 516 STORE_FAST               3 (value)
        # 1791         518 LOAD_FAST                3 (value)
        # 520 LOAD_FAST                0 (self)
        # 522 LOAD_FAST                2 (key)
        # 524 LOAD_METHOD              5 (lower)
        # 546 PRECALL                  0
        # 550 CALL                     0
        # 560 STORE_SUBSCR
        # 564 JUMP_BACKWARD           29 (to 508)
        # 1792     >>  566 LOAD_GLOBAL             35 (NULL + int)
        # 578 LOAD_FAST                0 (self)
        # 580 LOAD_CONST               2 ('status')
        # 582 BINARY_SUBSCR
        # 592 PRECALL                  1
        # 596 CALL                     1
        # 606 LOAD_FAST                0 (self)
        # 608 STORE_ATTR               8 (status)
        # 618 LOAD_CONST               0 (None)
        # 620 RETURN_VALUE
        # 1794     >>  622 LOAD_FAST                1 (info)
        # 624 LOAD_METHOD             16 (items)
        # 646 PRECALL                  0
        # 650 CALL                     0
        # 660 GET_ITER
        # >>  662 FOR_ITER                28 (to 720)
        # 664 UNPACK_SEQUENCE          2
        # 668 STORE_FAST               2 (key)
        # 670 STORE_FAST               3 (value)
        # 1795         672 LOAD_FAST                3 (value)
        # 674 LOAD_FAST                0 (self)
        # 676 LOAD_FAST                2 (key)
        # 678 LOAD_METHOD              5 (lower)
        # 700 PRECALL                  0
        # 704 CALL                     0
        # 714 STORE_SUBSCR
        # 718 JUMP_BACKWARD           29 (to 662)
        # 1796     >>  720 LOAD_GLOBAL             35 (NULL + int)
        # 732 LOAD_FAST                0 (self)
        # 734 LOAD_METHOD              6 (get)
        # 756 LOAD_CONST               2 ('status')
        # 758 LOAD_FAST                0 (self)
        # 760 LOAD_ATTR                8 (status)
        # 770 PRECALL                  2
        # 774 CALL                     2
        # 784 PRECALL                  1
        # 788 CALL                     1
        # 798 LOAD_FAST                0 (self)
        # 800 STORE_ATTR               8 (status)
        # 810 LOAD_CONST               0 (None)
        # 812 RETURN_VALUE

    def __getattr__(self, name):
        # 1798           0 RESUME                   0
        # 1799           2 LOAD_FAST                1 (name)
        # 4 LOAD_CONST               1 ('dict')
        # 6 COMPARE_OP               2 (==)
        # 12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
        # 1800          14 LOAD_FAST                0 (self)
        # 16 RETURN_VALUE
        # 1802     >>   18 LOAD_GLOBAL              1 (NULL + AttributeError)
        # 30 LOAD_FAST                1 (name)
        # 32 PRECALL                  1
        # 36 CALL                     1
        # 46 RAISE_VARARGS            1

