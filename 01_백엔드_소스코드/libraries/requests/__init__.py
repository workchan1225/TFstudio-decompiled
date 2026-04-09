# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: requests\__init__.py

"""
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
"""

import warnings
import urllib3
from exceptions import RequestsDependencyWarning
from charset_normalizer import __version__
from chardet import __version__
import ssl
from urllib3.contrib import pyopenssl
from cryptography import __version__
from urllib3.exceptions import DependencyWarning
import logging
from logging import NullHandler
from  import packages
from __version__ import __author__
from api import delete
from exceptions import ConnectionError
from models import PreparedRequest
from sessions import Session
from status_codes import codes

def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version):
    # 58           0 RESUME                   0
    # 59           2 LOAD_FAST                0 (urllib3_version)
    # 4 LOAD_METHOD              0 (split)
    # 26 LOAD_CONST               1 ('.')
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 STORE_FAST               0 (urllib3_version)
    # 60          44 LOAD_FAST                0 (urllib3_version)
    # 46 LOAD_CONST               2 ('dev')
    # 48 BUILD_LIST               1
    # 50 COMPARE_OP               3 (!=)
    # 56 POP_JUMP_FORWARD_IF_TRUE     2 (to 62)
    # 58 LOAD_ASSERTION_ERROR
    # 60 RAISE_VARARGS            1
    # 63     >>   62 LOAD_GLOBAL              3 (NULL + len)
    # 74 LOAD_FAST                0 (urllib3_version)
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 LOAD_CONST               3 (2)
    # 92 COMPARE_OP               2 (==)
    # 98 POP_JUMP_FORWARD_IF_FALSE    21 (to 142)
    # 64         100 LOAD_FAST                0 (urllib3_version)
    # 102 LOAD_METHOD              2 (append)
    # 124 LOAD_CONST               4 ('0')
    # 126 PRECALL                  1
    # 130 CALL                     1
    # 140 POP_TOP
    # 67     >>  142 LOAD_FAST                0 (urllib3_version)
    # 144 UNPACK_SEQUENCE          3
    # 148 STORE_FAST               3 (major)
    # 150 STORE_FAST               4 (minor)
    # 152 STORE_FAST               5 (patch)
    # 68         154 LOAD_GLOBAL              7 (NULL + int)
    # 166 LOAD_FAST                3 (major)
    # 168 PRECALL                  1
    # 172 CALL                     1
    # 182 LOAD_GLOBAL              7 (NULL + int)
    # 194 LOAD_FAST                4 (minor)
    # 196 PRECALL                  1
    # 200 CALL                     1
    # 210 LOAD_GLOBAL              7 (NULL + int)
    # 222 LOAD_FAST                5 (patch)
    # 224 PRECALL                  1
    # 228 CALL                     1
    # 238 STORE_FAST               5 (patch)
    # 240 STORE_FAST               4 (minor)
    # 242 STORE_FAST               3 (major)
    # 70         244 LOAD_FAST                3 (major)
    # 246 LOAD_CONST               5 (1)
    # 248 COMPARE_OP               5 (>=)
    # 254 POP_JUMP_FORWARD_IF_TRUE     2 (to 260)
    # 256 LOAD_ASSERTION_ERROR
    # 258 RAISE_VARARGS            1
    # 71     >>  260 LOAD_FAST                3 (major)
    # 262 LOAD_CONST               5 (1)
    # 264 COMPARE_OP               2 (==)
    # 270 POP_JUMP_FORWARD_IF_FALSE     8 (to 288)
    # 72         272 LOAD_FAST                4 (minor)
    # 274 LOAD_CONST               6 (21)
    # 276 COMPARE_OP               5 (>=)
    # 282 POP_JUMP_FORWARD_IF_TRUE     2 (to 288)
    # 284 LOAD_ASSERTION_ERROR
    # 286 RAISE_VARARGS            1
    # 75     >>  288 LOAD_FAST                1 (chardet_version)
    # 290 POP_JUMP_FORWARD_IF_FALSE    95 (to 482)
    # 76         292 PUSH_NULL
    # 294 LOAD_FAST                1 (chardet_version)
    # 296 LOAD_ATTR                0 (split)
    # 306 LOAD_CONST               1 ('.')
    # 308 PRECALL                  1
    # 312 CALL                     1
    # 322 LOAD_CONST               0 (None)
    # 324 LOAD_CONST               7 (3)
    # 326 BUILD_SLICE              2
    # 328 BINARY_SUBSCR
    # 338 UNPACK_SEQUENCE          3
    # 342 STORE_FAST               3 (major)
    # 344 STORE_FAST               4 (minor)
    # 346 STORE_FAST               5 (patch)
    # 77         348 LOAD_GLOBAL              7 (NULL + int)
    # 360 LOAD_FAST                3 (major)
    # 362 PRECALL                  1
    # 366 CALL                     1
    # 376 LOAD_GLOBAL              7 (NULL + int)
    # 388 LOAD_FAST                4 (minor)
    # 390 PRECALL                  1
    # 394 CALL                     1
    # 404 LOAD_GLOBAL              7 (NULL + int)
    # 416 LOAD_FAST                5 (patch)
    # 418 PRECALL                  1
    # 422 CALL                     1
    # 432 STORE_FAST               5 (patch)
    # 434 STORE_FAST               4 (minor)
    # 436 STORE_FAST               3 (major)
    # 79         438 LOAD_CONST               8 ((3, 0, 2))
    # 440 LOAD_FAST                3 (major)
    # 442 LOAD_FAST                4 (minor)
    # 444 LOAD_FAST                5 (patch)
    # 446 BUILD_TUPLE              3
    # 448 SWAP                     2
    # 450 COPY                     2
    # 452 COMPARE_OP               1 (<=)
    # 458 POP_JUMP_FORWARD_IF_FALSE     6 (to 472)
    # 460 LOAD_CONST               9 ((6, 0, 0))
    # 462 COMPARE_OP               0 (<)
    # 468 POP_JUMP_FORWARD_IF_TRUE     4 (to 478)
    # 470 JUMP_FORWARD             1 (to 474)
    # >>  472 POP_TOP
    # >>  474 LOAD_ASSERTION_ERROR
    # 476 RAISE_VARARGS            1
    # >>  478 LOAD_CONST               0 (None)
    # 480 RETURN_VALUE
    # 80     >>  482 LOAD_FAST                2 (charset_normalizer_version)
    # 484 POP_JUMP_FORWARD_IF_FALSE    95 (to 676)
    # 81         486 PUSH_NULL
    # 488 LOAD_FAST                2 (charset_normalizer_version)
    # 490 LOAD_ATTR                0 (split)
    # 500 LOAD_CONST               1 ('.')
    # 502 PRECALL                  1
    # 506 CALL                     1
    # 516 LOAD_CONST               0 (None)
    # 518 LOAD_CONST               7 (3)
    # 520 BUILD_SLICE              2
    # 522 BINARY_SUBSCR
    # 532 UNPACK_SEQUENCE          3
    # 536 STORE_FAST               3 (major)
    # 538 STORE_FAST               4 (minor)
    # 540 STORE_FAST               5 (patch)
    # 82         542 LOAD_GLOBAL              7 (NULL + int)
    # 554 LOAD_FAST                3 (major)
    # 556 PRECALL                  1
    # 560 CALL                     1
    # 570 LOAD_GLOBAL              7 (NULL + int)
    # 582 LOAD_FAST                4 (minor)
    # 584 PRECALL                  1
    # 588 CALL                     1
    # 598 LOAD_GLOBAL              7 (NULL + int)
    # 610 LOAD_FAST                5 (patch)
    # 612 PRECALL                  1
    # 616 CALL                     1
    # 626 STORE_FAST               5 (patch)
    # 628 STORE_FAST               4 (minor)
    # 630 STORE_FAST               3 (major)
    # 84         632 LOAD_CONST              10 ((2, 0, 0))
    # 634 LOAD_FAST                3 (major)
    # 636 LOAD_FAST                4 (minor)
    # 638 LOAD_FAST                5 (patch)
    # 640 BUILD_TUPLE              3
    # 642 SWAP                     2
    # 644 COPY                     2
    # 646 COMPARE_OP               1 (<=)
    # 652 POP_JUMP_FORWARD_IF_FALSE     6 (to 666)
    # 654 LOAD_CONST              11 ((4, 0, 0))
    # 656 COMPARE_OP               0 (<)
    # 662 POP_JUMP_FORWARD_IF_TRUE     4 (to 672)
    # 664 JUMP_FORWARD             1 (to 668)
    # >>  666 POP_TOP
    # >>  668 LOAD_ASSERTION_ERROR
    # 670 RAISE_VARARGS            1
    # >>  672 LOAD_CONST               0 (None)
    # 674 RETURN_VALUE
    # 86     >>  676 LOAD_GLOBAL              9 (NULL + Exception)
    # 688 LOAD_CONST              12 ('You need either charset_normalizer or chardet installed')
    # 690 PRECALL                  1
    # 694 CALL                     1
    # 704 RAISE_VARARGS            1

def _check_cryptography(cryptography_version):
    # 89           0 RESUME                   0
    # 91           2 NOP
    # 92           4 LOAD_GLOBAL              1 (NULL + list)
    # 16 LOAD_GLOBAL              3 (NULL + map)
    # 28 LOAD_GLOBAL              4 (int)
    # 40 PUSH_NULL
    # 42 LOAD_FAST                0 (cryptography_version)
    # 44 LOAD_ATTR                3 (split)
    # 54 LOAD_CONST               1 ('.')
    # 56 PRECALL                  1
    # 60 CALL                     1
    # 70 PRECALL                  2
    # 74 CALL                     2
    # 84 PRECALL                  1
    # 88 CALL                     1
    # 98 STORE_FAST               0 (cryptography_version)
    # 100 JUMP_FORWARD            17 (to 136)
    # >>  102 PUSH_EXC_INFO
    # 93         104 LOAD_GLOBAL              8 (ValueError)
    # 116 CHECK_EXC_MATCH
    # 118 POP_JUMP_FORWARD_IF_FALSE     4 (to 128)
    # 120 POP_TOP
    # 94         122 POP_EXCEPT
    # 124 LOAD_CONST               0 (None)
    # 126 RETURN_VALUE
    # 93     >>  128 RERAISE                  0
    # >>  130 COPY                     3
    # 132 POP_EXCEPT
    # 134 RERAISE                  1
    # 96     >>  136 LOAD_FAST                0 (cryptography_version)
    # 138 BUILD_LIST               0
    # 140 LOAD_CONST               2 ((1, 3, 4))
    # 142 LIST_EXTEND              1
    # 144 COMPARE_OP               0 (<)
    # 150 POP_JUMP_FORWARD_IF_FALSE    49 (to 250)
    # 97         152 LOAD_CONST               3 ('Old version of cryptography ({}) may cause slowdown.')
    # 154 LOAD_METHOD              5 (format)
    # 98         176 LOAD_FAST                0 (cryptography_version)
    # 97         178 PRECALL                  1
    # 182 CALL                     1
    # 192 STORE_FAST               1 (warning)
    # 100         194 LOAD_GLOBAL             13 (NULL + warnings)
    # 206 LOAD_ATTR                7 (warn)
    # 216 LOAD_FAST                1 (warning)
    # 218 LOAD_GLOBAL             16 (RequestsDependencyWarning)
    # 230 PRECALL                  2
    # 234 CALL                     2
    # 244 POP_TOP
    # 246 LOAD_CONST               0 (None)
    # 248 RETURN_VALUE
    # 96     >>  250 LOAD_CONST               0 (None)
    # 252 RETURN_VALUE
    # ExceptionTable:
    # 4 to 98 -> 102 [0]
    # 102 to 120 -> 130 [1] lasti
    # 128 to 128 -> 130 [1] lasti
