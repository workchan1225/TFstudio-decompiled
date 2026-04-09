# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: _pytest\_py\path.py

"""local path implementation."""

from __future__ import annotations
import atexit
from collections.abc import Callable
from contextlib import contextmanager
import fnmatch
import importlib.util
import io
import os
from os.path import abspath
from os.path import dirname
from os.path import exists
from os.path import isabs
from os.path import isdir
from os.path import isfile
from os.path import islink
from os.path import normpath
import posixpath
from stat import S_ISDIR
from stat import S_ISLNK
from stat import S_ISREG
import sys
from typing import Any
from typing import cast
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
import uuid
import warnings
from  import error

class Checkers:
    """Checkers"""
    def __init__(self, path):
        # 44           0 RESUME                   0
        # 45           2 LOAD_FAST                1 (path)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (path)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def dotfile(self):
        # 47           0 RESUME                   0
        # 48           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_ATTR                1 (basename)
        # 24 LOAD_METHOD              2 (startswith)
        # 46 LOAD_CONST               1 ('.')
        # 48 PRECALL                  1
        # 52 CALL                     1
        # 62 RETURN_VALUE

    def ext(self, arg):
        # 50           0 RESUME                   0
        # 51           2 LOAD_FAST                1 (arg)
        # 4 LOAD_METHOD              0 (startswith)
        # 26 LOAD_CONST               1 ('.')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 POP_JUMP_FORWARD_IF_TRUE     5 (to 54)
        # 52          44 LOAD_CONST               1 ('.')
        # 46 LOAD_FAST                1 (arg)
        # 48 BINARY_OP                0 (+)
        # 52 STORE_FAST               1 (arg)
        # 53     >>   54 LOAD_FAST                0 (self)
        # 56 LOAD_ATTR                1 (path)
        # 66 LOAD_ATTR                2 (ext)
        # 76 LOAD_FAST                1 (arg)
        # 78 COMPARE_OP               2 (==)
        # 84 RETURN_VALUE

    def basename(self, arg):
        # 55           0 RESUME                   0
        # 56           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_ATTR                1 (basename)
        # 24 LOAD_FAST                1 (arg)
        # 26 COMPARE_OP               2 (==)
        # 32 RETURN_VALUE

    def basestarts(self, arg):
        # 58           0 RESUME                   0
        # 59           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_ATTR                1 (basename)
        # 24 LOAD_METHOD              2 (startswith)
        # 46 LOAD_FAST                1 (arg)
        # 48 PRECALL                  1
        # 52 CALL                     1
        # 62 RETURN_VALUE

    def relto(self, arg):
        # 61           0 RESUME                   0
        # 62           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_METHOD              1 (relto)
        # 36 LOAD_FAST                1 (arg)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 RETURN_VALUE

    def fnmatch(self, arg):
        # 64           0 RESUME                   0
        # 65           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_METHOD              1 (fnmatch)
        # 36 LOAD_FAST                1 (arg)
        # 38 PRECALL                  1
        # 42 CALL                     1
        # 52 RETURN_VALUE

    def endswith(self, arg):
        # 67           0 RESUME                   0
        # 68           2 LOAD_GLOBAL              1 (NULL + str)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (path)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 LOAD_METHOD              2 (endswith)
        # 62 LOAD_FAST                1 (arg)
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 RETURN_VALUE

    def _evaluate(self, kw):
        # 70           0 RESUME                   0
        # 71           2 LOAD_CONST               1 (2)
        # 4 LOAD_CONST               2 (('getrawcode',))
        # 6 IMPORT_NAME              0 (_code.source)
        # 8 IMPORT_FROM              1 (getrawcode)
        # 10 STORE_FAST               2 (getrawcode)
        # 12 POP_TOP
        # 73          14 LOAD_FAST                1 (kw)
        # 16 LOAD_METHOD              2 (items)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 GET_ITER
        # >>   54 EXTENDED_ARG             1
        # 56 FOR_ITER               334 (to 726)
        # 58 UNPACK_SEQUENCE          2
        # 62 STORE_FAST               3 (name)
        # 64 STORE_FAST               4 (value)
        # 74          66 LOAD_CONST               3 (False)
        # 68 STORE_FAST               5 (invert)
        # 75          70 LOAD_CONST               0 (None)
        # 72 STORE_FAST               6 (meth)
        # 76          74 NOP
        # 77          76 LOAD_GLOBAL              7 (NULL + getattr)
        # 88 LOAD_FAST                0 (self)
        # 90 LOAD_FAST                3 (name)
        # 92 PRECALL                  2
        # 96 CALL                     2
        # 106 STORE_FAST               6 (meth)
        # 108 JUMP_FORWARD            74 (to 258)
        # >>  110 PUSH_EXC_INFO
        # 78         112 LOAD_GLOBAL              8 (AttributeError)
        # 124 CHECK_EXC_MATCH
        # 126 POP_JUMP_FORWARD_IF_FALSE    61 (to 250)
        # 128 POP_TOP
        # 79         130 LOAD_FAST                3 (name)
        # 132 LOAD_CONST               0 (None)
        # 134 LOAD_CONST               4 (3)
        # 136 BUILD_SLICE              2
        # 138 BINARY_SUBSCR
        # 148 LOAD_CONST               5 ('not')
        # 150 COMPARE_OP               2 (==)
        # 156 POP_JUMP_FORWARD_IF_FALSE    44 (to 246)
        # 80         158 LOAD_CONST               6 (True)
        # 160 STORE_FAST               5 (invert)
        # 81         162 NOP
        # 82         164 LOAD_GLOBAL              7 (NULL + getattr)
        # 176 LOAD_FAST                0 (self)
        # 178 LOAD_FAST                3 (name)
        # 180 LOAD_CONST               4 (3)
        # 182 LOAD_CONST               0 (None)
        # 184 BUILD_SLICE              2
        # 186 BINARY_SUBSCR
        # 196 PRECALL                  2
        # 200 CALL                     2
        # 210 STORE_FAST               6 (meth)
        # 212 JUMP_FORWARD            16 (to 246)
        # >>  214 PUSH_EXC_INFO
        # 83         216 LOAD_GLOBAL              8 (AttributeError)
        # 228 CHECK_EXC_MATCH
        # 230 POP_JUMP_FORWARD_IF_FALSE     3 (to 238)
        # 232 POP_TOP
        # 84         234 POP_EXCEPT
        # 236 JUMP_FORWARD             4 (to 246)
        # 83     >>  238 RERAISE                  0
        # >>  240 COPY                     3
        # 242 POP_EXCEPT
        # 244 RERAISE                  1
        # >>  246 POP_EXCEPT
        # 248 JUMP_FORWARD             4 (to 258)
        # 78     >>  250 RERAISE                  0
        # >>  252 COPY                     3
        # 254 POP_EXCEPT
        # 256 RERAISE                  1
        # 85     >>  258 LOAD_FAST                6 (meth)
        # 260 POP_JUMP_FORWARD_IF_NOT_NONE    26 (to 314)
        # 86         262 LOAD_GLOBAL             11 (NULL + TypeError)
        # 274 LOAD_CONST               7 ('no ')
        # 276 LOAD_FAST                3 (name)
        # 278 FORMAT_VALUE             2 (repr)
        # 280 LOAD_CONST               8 (' checker available for ')
        # 282 LOAD_FAST                0 (self)
        # 284 LOAD_ATTR                6 (path)
        # 294 FORMAT_VALUE             2 (repr)
        # 296 BUILD_STRING             4
        # 298 PRECALL                  1
        # 302 CALL                     1
        # 312 RAISE_VARARGS            1
        # 87     >>  314 NOP
        # 88         316 PUSH_NULL
        # 318 LOAD_FAST                2 (getrawcode)
        # 320 LOAD_FAST                6 (meth)
        # 322 PRECALL                  1
        # 326 CALL                     1
        # 336 LOAD_ATTR                7 (co_argcount)
        # 346 LOAD_CONST               9 (1)
        # 348 COMPARE_OP               4 (>)
        # 354 POP_JUMP_FORWARD_IF_FALSE    19 (to 394)
        # 89         356 PUSH_NULL
        # 358 LOAD_FAST                6 (meth)
        # 360 LOAD_FAST                4 (value)
        # 362 PRECALL                  1
        # 366 CALL                     1
        # 376 UNARY_NOT
        # 378 LOAD_FAST                5 (invert)
        # 380 BINARY_OP               12 (^)
        # 384 POP_JUMP_FORWARD_IF_FALSE     3 (to 392)
        # 90         386 POP_TOP
        # 388 LOAD_CONST               3 (False)
        # 390 RETURN_VALUE
        # 89     >>  392 JUMP_FORWARD            45 (to 484)
        # 92     >>  394 LOAD_GLOBAL             17 (NULL + bool)
        # 406 LOAD_FAST                4 (value)
        # 408 PRECALL                  1
        # 412 CALL                     1
        # 422 LOAD_GLOBAL             17 (NULL + bool)
        # 434 PUSH_NULL
        # 436 LOAD_FAST                6 (meth)
        # 438 PRECALL                  0
        # 442 CALL                     0
        # 452 PRECALL                  1
        # 456 CALL                     1
        # 466 BINARY_OP               12 (^)
        # 470 LOAD_FAST                5 (invert)
        # 472 BINARY_OP               12 (^)
        # 476 POP_JUMP_FORWARD_IF_FALSE     3 (to 484)
        # 93         478 POP_TOP
        # 480 LOAD_CONST               3 (False)
        # 482 RETURN_VALUE
        # >>  484 JUMP_BACKWARD          216 (to 54)
        # >>  486 PUSH_EXC_INFO
        # 94         488 LOAD_GLOBAL             18 (error)
        # 500 LOAD_ATTR               10 (ENOENT)
        # 510 LOAD_GLOBAL             18 (error)
        # 522 LOAD_ATTR               11 (ENOTDIR)
        # 532 LOAD_GLOBAL             18 (error)
        # 544 LOAD_ATTR               12 (EBUSY)
        # 554 BUILD_TUPLE              3
        # 556 CHECK_EXC_MATCH
        # 558 POP_JUMP_FORWARD_IF_FALSE    79 (to 718)
        # 560 POP_TOP
        # 98         562 LOAD_FAST                0 (self)
        # 564 LOAD_ATTR               13 (_depend_on_existence)
        # 574 GET_ITER
        # >>  576 FOR_ITER                67 (to 712)
        # 578 STORE_FAST               3 (name)
        # 99         580 LOAD_FAST                3 (name)
        # 582 LOAD_FAST                1 (kw)
        # 584 CONTAINS_OP              0
        # 586 POP_JUMP_FORWARD_IF_FALSE    26 (to 640)
        # 100         588 LOAD_FAST                1 (kw)
        # 590 LOAD_METHOD             14 (get)
        # 612 LOAD_FAST                3 (name)
        # 614 PRECALL                  1
        # 618 CALL                     1
        # 628 POP_JUMP_FORWARD_IF_FALSE     5 (to 640)
        # 101         630 POP_TOP
        # 632 POP_EXCEPT
        # 634 POP_TOP
        # 636 LOAD_CONST               3 (False)
        # 638 RETURN_VALUE
        # 102     >>  640 LOAD_CONST               5 ('not')
        # 642 LOAD_FAST                3 (name)
        # 644 BINARY_OP                0 (+)
        # 648 STORE_FAST               3 (name)
        # 103         650 LOAD_FAST                3 (name)
        # 652 LOAD_FAST                1 (kw)
        # 654 CONTAINS_OP              0
        # 656 POP_JUMP_FORWARD_IF_FALSE    26 (to 710)
        # 104         658 LOAD_FAST                1 (kw)
        # 660 LOAD_METHOD             14 (get)
        # 682 LOAD_FAST                3 (name)
        # 684 PRECALL                  1
        # 688 CALL                     1
        # 698 POP_JUMP_FORWARD_IF_TRUE     5 (to 710)
        # 105         700 POP_TOP
        # 702 POP_EXCEPT
        # 704 POP_TOP
        # 706 LOAD_CONST               3 (False)
        # 708 RETURN_VALUE
        # >>  710 JUMP_BACKWARD           68 (to 576)
        # 98     >>  712 POP_EXCEPT
        # 714 EXTENDED_ARG             1
        # 716 JUMP_BACKWARD          332 (to 54)
        # 94     >>  718 RERAISE                  0
        # >>  720 COPY                     3
        # 722 POP_EXCEPT
        # 724 RERAISE                  1
        # 106     >>  726 LOAD_CONST               6 (True)
        # 728 RETURN_VALUE
        # ExceptionTable:
        # 76 to 106 -> 110 [1]
        # 110 to 160 -> 252 [2] lasti
        # 164 to 210 -> 214 [2]
        # 212 to 212 -> 252 [2] lasti
        # 214 to 232 -> 240 [3] lasti
        # 234 to 236 -> 252 [2] lasti
        # 238 to 238 -> 240 [3] lasti
        # 240 to 244 -> 252 [2] lasti
        # 250 to 250 -> 252 [2] lasti
        # 316 to 384 -> 486 [1]
        # 392 to 476 -> 486 [1]
        # 486 to 630 -> 720 [2] lasti
        # 640 to 700 -> 720 [2] lasti
        # 710 to 710 -> 720 [2] lasti
        # 718 to 718 -> 720 [2] lasti

    def _stat(self):
        # 110           0 RESUME                   0
        # 111           2 NOP
        # 112           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_statcache)
        # 16 RETURN_VALUE
        # >>   18 PUSH_EXC_INFO
        # 113          20 LOAD_GLOBAL              2 (AttributeError)
        # 32 CHECK_EXC_MATCH
        # 34 POP_JUMP_FORWARD_IF_FALSE    93 (to 222)
        # 36 POP_TOP
        # 114          38 NOP
        # 115          40 LOAD_FAST                0 (self)
        # 42 LOAD_ATTR                2 (path)
        # 52 LOAD_METHOD              3 (stat)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 88 LOAD_FAST                0 (self)
        # 90 STORE_ATTR               0 (_statcache)
        # 100 JUMP_FORWARD            51 (to 204)
        # >>  102 PUSH_EXC_INFO
        # 116         104 LOAD_GLOBAL              8 (error)
        # 116 LOAD_ATTR                5 (ELOOP)
        # 126 CHECK_EXC_MATCH
        # 128 POP_JUMP_FORWARD_IF_FALSE    33 (to 196)
        # 130 POP_TOP
        # 117         132 LOAD_FAST                0 (self)
        # 134 LOAD_ATTR                2 (path)
        # 144 LOAD_METHOD              6 (lstat)
        # 166 PRECALL                  0
        # 170 CALL                     0
        # 180 LOAD_FAST                0 (self)
        # 182 STORE_ATTR               0 (_statcache)
        # 192 POP_EXCEPT
        # 194 JUMP_FORWARD             4 (to 204)
        # 116     >>  196 RERAISE                  0
        # >>  198 COPY                     3
        # 200 POP_EXCEPT
        # 202 RERAISE                  1
        # 118     >>  204 LOAD_FAST                0 (self)
        # 206 LOAD_ATTR                0 (_statcache)
        # 216 SWAP                     2
        # 218 POP_EXCEPT
        # 220 RETURN_VALUE
        # 113     >>  222 RERAISE                  0
        # >>  224 COPY                     3
        # 226 POP_EXCEPT
        # 228 RERAISE                  1
        # ExceptionTable:
        # 4 to 14 -> 18 [0]
        # 18 to 36 -> 224 [1] lasti
        # 40 to 98 -> 102 [1]
        # 100 to 100 -> 224 [1] lasti
        # 102 to 190 -> 198 [2] lasti
        # 192 to 194 -> 224 [1] lasti
        # 196 to 196 -> 198 [2] lasti
        # 198 to 216 -> 224 [1] lasti
        # 222 to 222 -> 224 [1] lasti

    def dir(self):
        # 120           0 RESUME                   0
        # 121           2 LOAD_GLOBAL              1 (NULL + S_ISDIR)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_METHOD              1 (_stat)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_ATTR                2 (mode)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 RETURN_VALUE

    def file(self):
        # 123           0 RESUME                   0
        # 124           2 LOAD_GLOBAL              1 (NULL + S_ISREG)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_METHOD              1 (_stat)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_ATTR                2 (mode)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 RETURN_VALUE

    def exists(self):
        # 126           0 RESUME                   0
        # 127           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_stat)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 RETURN_VALUE

    def link(self):
        # 129           0 RESUME                   0
        # 130           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_METHOD              1 (lstat)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 STORE_FAST               1 (st)
        # 131          52 LOAD_GLOBAL              5 (NULL + S_ISLNK)
        # 64 LOAD_FAST                1 (st)
        # 66 LOAD_ATTR                3 (mode)
        # 76 PRECALL                  1
        # 80 CALL                     1
        # 90 RETURN_VALUE


class NeverRaised:
    """NeverRaised"""

class Visitor:
    """Visitor"""
    def __init__(self, fil, rec, ignore, bf, sort):
        # 139           0 RESUME                   0
        # 140           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (fil)
        # 16 LOAD_GLOBAL              2 (str)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_FALSE    15 (to 74)
        # 141          44 LOAD_GLOBAL              5 (NULL + FNMatcher)
        # 56 LOAD_FAST                1 (fil)
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 STORE_FAST               1 (fil)
        # 142     >>   74 LOAD_GLOBAL              1 (NULL + isinstance)
        # 86 LOAD_FAST                2 (rec)
        # 88 LOAD_GLOBAL              2 (str)
        # 100 PRECALL                  2
        # 104 CALL                     2
        # 114 POP_JUMP_FORWARD_IF_FALSE    21 (to 158)
        # 143         116 LOAD_GLOBAL              5 (NULL + FNMatcher)
        # 128 LOAD_FAST                2 (rec)
        # 130 PRECALL                  1
        # 134 CALL                     1
        # 144 LOAD_FAST                0 (self)
        # 146 STORE_ATTR               3 (rec)
        # 156 JUMP_FORWARD            34 (to 226)
        # 144     >>  158 LOAD_GLOBAL              9 (NULL + hasattr)
        # 170 LOAD_FAST                2 (rec)
        # 172 LOAD_CONST               1 ('__call__')
        # 174 PRECALL                  2
        # 178 CALL                     2
        # 188 POP_JUMP_FORWARD_IF_TRUE    11 (to 212)
        # 190 LOAD_FAST                2 (rec)
        # 192 POP_JUMP_FORWARD_IF_FALSE     9 (to 212)
        # 145         194 LOAD_CONST               2 (<code object <lambda> at 0x000001EBD7EFEA30, file "_pytest\_py\path.py", line 145>)
        # 196 MAKE_FUNCTION            0
        # 198 LOAD_FAST                0 (self)
        # 200 STORE_ATTR               3 (rec)
        # 210 JUMP_FORWARD             7 (to 226)
        # 147     >>  212 LOAD_FAST                2 (rec)
        # 214 LOAD_FAST                0 (self)
        # 216 STORE_ATTR               3 (rec)
        # 148     >>  226 LOAD_FAST                1 (fil)
        # 228 LOAD_FAST                0 (self)
        # 230 STORE_ATTR               5 (fil)
        # 149         240 LOAD_FAST                3 (ignore)
        # 242 LOAD_FAST                0 (self)
        # 244 STORE_ATTR               6 (ignore)
        # 150         254 LOAD_FAST                4 (bf)
        # 256 LOAD_FAST                0 (self)
        # 258 STORE_ATTR               7 (breadthfirst)
        # 151         268 LOAD_FAST                5 (sort)
        # 270 POP_JUMP_FORWARD_IF_FALSE    45 (to 362)
        # 272 LOAD_GLOBAL             17 (NULL + cast)
        # 284 LOAD_GLOBAL             18 (Callable)
        # 296 LOAD_GLOBAL             20 (Any)
        # 308 BUILD_LIST               1
        # 310 LOAD_GLOBAL             20 (Any)
        # 322 BUILD_TUPLE              2
        # 324 BINARY_SUBSCR
        # 334 LOAD_GLOBAL             22 (sorted)
        # 346 PRECALL                  2
        # 350 CALL                     2
        # 360 JUMP_FORWARD             2 (to 366)
        # >>  362 LOAD_CONST               3 (<code object <lambda> at 0x000001EBD7EFEAF0, file "_pytest\_py\path.py", line 151>)
        # 364 MAKE_FUNCTION            0
        # >>  366 LOAD_FAST                0 (self)
        # 368 STORE_ATTR              12 (optsort)
        # 378 LOAD_CONST               0 (None)
        # 380 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7EFEA30, file "_pytest\_py\path.py", line 145>:
        # 145           0 RESUME                   0
        # 2 LOAD_CONST               1 (True)
        # 4 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7EFEAF0, file "_pytest\_py\path.py", line 151>:
        # 151           0 RESUME                   0
        # 2 LOAD_FAST                0 (x)
        # 4 RETURN_VALUE

    def gen(self, path):
        # 0 MAKE_CELL                6 (rec)
        # 153           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 154           8 NOP
        # 155          10 LOAD_FAST                1 (path)
        # 12 LOAD_METHOD              0 (listdir)
        # 34 PRECALL                  0
        # 38 CALL                     0
        # 48 STORE_FAST               2 (entries)
        # 50 JUMP_FORWARD            17 (to 86)
        # >>   52 PUSH_EXC_INFO
        # 156          54 LOAD_FAST                0 (self)
        # 56 LOAD_ATTR                1 (ignore)
        # 66 CHECK_EXC_MATCH
        # 68 POP_JUMP_FORWARD_IF_FALSE     4 (to 78)
        # 70 POP_TOP
        # 157          72 POP_EXCEPT
        # 74 LOAD_CONST               0 (None)
        # 76 RETURN_VALUE
        # 156     >>   78 RERAISE                  0
        # >>   80 COPY                     3
        # 82 POP_EXCEPT
        # 84 RERAISE                  1
        # 158     >>   86 LOAD_FAST                0 (self)
        # 88 LOAD_ATTR                2 (rec)
        # 98 STORE_DEREF              6 (rec)
        # 159         100 LOAD_FAST                0 (self)
        # 102 LOAD_METHOD              3 (optsort)
        # 160         124 LOAD_CLOSURE             6 (rec)
        # 126 BUILD_TUPLE              1
        # 128 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7E48270, file "_pytest\_py\path.py", line 160>)
        # 130 MAKE_FUNCTION            8 (closure)
        # 132 LOAD_FAST                2 (entries)
        # 134 GET_ITER
        # 136 PRECALL                  0
        # 140 CALL                     0
        # 159         150 PRECALL                  1
        # 154 CALL                     1
        # 164 STORE_FAST               3 (dirs)
        # 162         166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                4 (breadthfirst)
        # 178 POP_JUMP_FORWARD_IF_TRUE    32 (to 244)
        # 163         180 LOAD_FAST                3 (dirs)
        # 182 GET_ITER
        # >>  184 FOR_ITER                29 (to 244)
        # 186 STORE_FAST               4 (subdir)
        # 164         188 LOAD_FAST                0 (self)
        # 190 LOAD_METHOD              5 (gen)
        # 212 LOAD_FAST                4 (subdir)
        # 214 PRECALL                  1
        # 218 CALL                     1
        # 228 GET_YIELD_FROM_ITER
        # 230 LOAD_CONST               0 (None)
        # >>  232 SEND                     3 (to 240)
        # 234 YIELD_VALUE
        # 236 RESUME                   2
        # 238 JUMP_BACKWARD_NO_INTERRUPT     4 (to 232)
        # >>  240 POP_TOP
        # 242 JUMP_BACKWARD           30 (to 184)
        # 165     >>  244 LOAD_FAST                0 (self)
        # 246 LOAD_METHOD              3 (optsort)
        # 268 LOAD_FAST                2 (entries)
        # 270 PRECALL                  1
        # 274 CALL                     1
        # 284 GET_ITER
        # >>  286 FOR_ITER                34 (to 356)
        # 288 STORE_FAST               5 (p)
        # 166         290 LOAD_FAST                0 (self)
        # 292 LOAD_ATTR                6 (fil)
        # 302 POP_JUMP_FORWARD_IF_NONE    21 (to 346)
        # 304 LOAD_FAST                0 (self)
        # 306 LOAD_METHOD              6 (fil)
        # 328 LOAD_FAST                5 (p)
        # 330 PRECALL                  1
        # 334 CALL                     1
        # 344 POP_JUMP_FORWARD_IF_FALSE     4 (to 354)
        # 167     >>  346 LOAD_FAST                5 (p)
        # 348 YIELD_VALUE
        # 350 RESUME                   1
        # 352 POP_TOP
        # >>  354 JUMP_BACKWARD           35 (to 286)
        # 168     >>  356 LOAD_FAST                0 (self)
        # 358 LOAD_ATTR                4 (breadthfirst)
        # 368 POP_JUMP_FORWARD_IF_FALSE    32 (to 434)
        # 169         370 LOAD_FAST                3 (dirs)
        # 372 GET_ITER
        # >>  374 FOR_ITER                31 (to 438)
        # 376 STORE_FAST               4 (subdir)
        # 170         378 LOAD_FAST                0 (self)
        # 380 LOAD_METHOD              5 (gen)
        # 402 LOAD_FAST                4 (subdir)
        # 404 PRECALL                  1
        # 408 CALL                     1
        # 418 GET_YIELD_FROM_ITER
        # 420 LOAD_CONST               0 (None)
        # >>  422 SEND                     3 (to 430)
        # 424 YIELD_VALUE
        # 426 RESUME                   2
        # 428 JUMP_BACKWARD_NO_INTERRUPT     4 (to 422)
        # >>  430 POP_TOP
        # 432 JUMP_BACKWARD           30 (to 374)
        # 168     >>  434 LOAD_CONST               0 (None)
        # 436 RETURN_VALUE
        # 169     >>  438 LOAD_CONST               0 (None)
        # 440 RETURN_VALUE
        # ExceptionTable:
        # 10 to 48 -> 52 [0]
        # 52 to 70 -> 80 [1] lasti
        # 78 to 78 -> 80 [1] lasti
        # Disassembly of <code object <listcomp> at 0x000001EBD7E48270, file "_pytest\_py\path.py", line 160>:
        # 0 COPY_FREE_VARS           1
        # 160           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                39 (to 88)
        # 10 STORE_FAST               1 (p)
        # 12 LOAD_FAST                1 (p)
        # 14 LOAD_METHOD              0 (check)
        # 36 LOAD_CONST               0 (1)
        # 38 KW_NAMES                 1
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 POP_JUMP_BACKWARD_IF_FALSE    24 (to 8)
        # 56 LOAD_DEREF               2 (rec)
        # 58 POP_JUMP_FORWARD_IF_NONE    11 (to 82)
        # 60 PUSH_NULL
        # 62 LOAD_DEREF               2 (rec)
        # 64 LOAD_FAST                1 (p)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 POP_JUMP_BACKWARD_IF_FALSE    37 (to 8)
        # >>   82 LOAD_FAST                1 (p)
        # 84 LIST_APPEND              2
        # 86 JUMP_BACKWARD           40 (to 8)
        # >>   88 RETURN_VALUE


class FNMatcher:
    """FNMatcher"""
    def __init__(self, pattern):
        # 174           0 RESUME                   0
        # 175           2 LOAD_FAST                1 (pattern)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (pattern)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def __call__(self, path):
        # 177           0 RESUME                   0
        # 178           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (pattern)
        # 14 STORE_FAST               2 (pattern)
        # 181          16 LOAD_FAST                2 (pattern)
        # 18 LOAD_METHOD              1 (find)
        # 40 LOAD_FAST                1 (path)
        # 42 LOAD_ATTR                2 (sep)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 LOAD_CONST               1 (-1)
        # 68 COMPARE_OP               2 (==)
        # 74 POP_JUMP_FORWARD_IF_FALSE    79 (to 234)
        # 182          76 LOAD_GLOBAL              6 (iswin32)
        # 181          88 POP_JUMP_FORWARD_IF_FALSE    72 (to 234)
        # 183          90 LOAD_FAST                2 (pattern)
        # 92 LOAD_METHOD              1 (find)
        # 114 LOAD_GLOBAL              8 (posixpath)
        # 126 LOAD_ATTR                2 (sep)
        # 136 PRECALL                  1
        # 140 CALL                     1
        # 150 LOAD_CONST               1 (-1)
        # 152 COMPARE_OP               3 (!=)
        # 158 POP_JUMP_FORWARD_IF_FALSE    37 (to 234)
        # 188         160 LOAD_FAST                2 (pattern)
        # 162 LOAD_METHOD              5 (replace)
        # 184 LOAD_GLOBAL              8 (posixpath)
        # 196 LOAD_ATTR                2 (sep)
        # 206 LOAD_FAST                1 (path)
        # 208 LOAD_ATTR                2 (sep)
        # 218 PRECALL                  2
        # 222 CALL                     2
        # 232 STORE_FAST               2 (pattern)
        # 190     >>  234 LOAD_FAST                2 (pattern)
        # 236 LOAD_METHOD              1 (find)
        # 258 LOAD_FAST                1 (path)
        # 260 LOAD_ATTR                2 (sep)
        # 270 PRECALL                  1
        # 274 CALL                     1
        # 284 LOAD_CONST               1 (-1)
        # 286 COMPARE_OP               2 (==)
        # 292 POP_JUMP_FORWARD_IF_FALSE     8 (to 310)
        # 191         294 LOAD_FAST                1 (path)
        # 296 LOAD_ATTR                6 (basename)
        # 306 STORE_FAST               3 (name)
        # 308 JUMP_FORWARD            59 (to 428)
        # 193     >>  310 LOAD_GLOBAL             15 (NULL + str)
        # 322 LOAD_FAST                1 (path)
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 STORE_FAST               3 (name)
        # 194         340 LOAD_GLOBAL             16 (os)
        # 352 LOAD_ATTR                9 (path)
        # 362 LOAD_METHOD             10 (isabs)
        # 384 LOAD_FAST                2 (pattern)
        # 386 PRECALL                  1
        # 390 CALL                     1
        # 400 POP_JUMP_FORWARD_IF_TRUE    13 (to 428)
        # 195         402 LOAD_CONST               2 ('*')
        # 404 LOAD_FAST                1 (path)
        # 406 LOAD_ATTR                2 (sep)
        # 416 BINARY_OP                0 (+)
        # 420 LOAD_FAST                2 (pattern)
        # 422 BINARY_OP                0 (+)
        # 426 STORE_FAST               2 (pattern)
        # 196     >>  428 LOAD_GLOBAL             23 (NULL + fnmatch)
        # 440 LOAD_ATTR               11 (fnmatch)
        # 450 LOAD_FAST                3 (name)
        # 452 LOAD_FAST                2 (pattern)
        # 454 PRECALL                  2
        # 458 CALL                     2
        # 468 RETURN_VALUE


def map_as_list(func, iter):
    # 199           0 RESUME                   0
    # 200           2 LOAD_GLOBAL              1 (NULL + list)
    # 14 LOAD_GLOBAL              3 (NULL + map)
    # 26 LOAD_FAST                0 (func)
    # 28 LOAD_FAST                1 (iter)
    # 30 PRECALL                  2
    # 34 CALL                     2
    # 44 PRECALL                  1
    # 48 CALL                     1
    # 58 RETURN_VALUE

class Stat:
    """Stat"""
    def size(self):
        # 206           0 RESUME                   0
        # 207           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def mtime(self):
        # 209           0 RESUME                   0
        # 210           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def __getattr__(self, name):
        # 212           0 RESUME                   0
        # 213           2 LOAD_GLOBAL              1 (NULL + getattr)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (_osstatresult)
        # 26 LOAD_CONST               1 ('st_')
        # 28 LOAD_FAST                1 (name)
        # 30 BINARY_OP                0 (+)
        # 34 PRECALL                  2
        # 38 CALL                     2
        # 48 RETURN_VALUE

    def __init__(self, path, osstatresult):
        # 215           0 RESUME                   0
        # 216           2 LOAD_FAST                1 (path)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (path)
        # 217          16 LOAD_FAST                2 (osstatresult)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (_osstatresult)
        # 30 LOAD_CONST               0 (None)
        # 32 RETURN_VALUE

    def owner(self):
        # 219           0 RESUME                   0
        # 221           2 LOAD_GLOBAL              0 (iswin32)
        # 14 POP_JUMP_FORWARD_IF_FALSE    15 (to 46)
        # 222          16 LOAD_GLOBAL              3 (NULL + NotImplementedError)
        # 28 LOAD_CONST               1 ('XXX win32')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 223     >>   46 LOAD_CONST               2 (0)
        # 48 LOAD_CONST               0 (None)
        # 50 IMPORT_NAME              2 (pwd)
        # 52 STORE_FAST               1 (pwd)
        # 225          54 LOAD_GLOBAL              7 (NULL + error)
        # 66 LOAD_ATTR                4 (checked_call)
        # 76 LOAD_FAST                1 (pwd)
        # 78 LOAD_ATTR                5 (getpwuid)
        # 88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                6 (uid)
        # 100 PRECALL                  2
        # 104 CALL                     2
        # 114 STORE_FAST               2 (entry)
        # 226         116 LOAD_FAST                2 (entry)
        # 118 LOAD_CONST               2 (0)
        # 120 BINARY_SUBSCR
        # 130 RETURN_VALUE

    def group(self):
        """Return group name of file."""
        # 228           0 RESUME                   0
        # 231           2 LOAD_GLOBAL              0 (iswin32)
        # 14 POP_JUMP_FORWARD_IF_FALSE    15 (to 46)
        # 232          16 LOAD_GLOBAL              3 (NULL + NotImplementedError)
        # 28 LOAD_CONST               1 ('XXX win32')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 233     >>   46 LOAD_CONST               2 (0)
        # 48 LOAD_CONST               3 (None)
        # 50 IMPORT_NAME              2 (grp)
        # 52 STORE_FAST               1 (grp)
        # 235          54 LOAD_GLOBAL              7 (NULL + error)
        # 66 LOAD_ATTR                4 (checked_call)
        # 76 LOAD_FAST                1 (grp)
        # 78 LOAD_ATTR                5 (getgrgid)
        # 88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                6 (gid)
        # 100 PRECALL                  2
        # 104 CALL                     2
        # 114 STORE_FAST               2 (entry)
        # 236         116 LOAD_FAST                2 (entry)
        # 118 LOAD_CONST               2 (0)
        # 120 BINARY_SUBSCR
        # 130 RETURN_VALUE

    def isdir(self):
        # 238           0 RESUME                   0
        # 239           2 LOAD_GLOBAL              1 (NULL + S_ISDIR)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (_osstatresult)
        # 26 LOAD_ATTR                2 (st_mode)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 RETURN_VALUE

    def isfile(self):
        # 241           0 RESUME                   0
        # 242           2 LOAD_GLOBAL              1 (NULL + S_ISREG)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (_osstatresult)
        # 26 LOAD_ATTR                2 (st_mode)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 RETURN_VALUE

    def islink(self):
        # 244           0 RESUME                   0
        # 245           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (path)
        # 14 LOAD_METHOD              1 (lstat)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 POP_TOP
        # 246          52 LOAD_GLOBAL              5 (NULL + S_ISLNK)
        # 64 LOAD_FAST                0 (self)
        # 66 LOAD_ATTR                3 (_osstatresult)
        # 76 LOAD_ATTR                4 (st_mode)
        # 86 PRECALL                  1
        # 90 CALL                     1
        # 100 RETURN_VALUE


def getuserid(user):
    # 249           0 RESUME                   0
    # 250           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               0 (None)
    # 6 IMPORT_NAME              0 (pwd)
    # 8 STORE_FAST               1 (pwd)
    # 252          10 LOAD_GLOBAL              3 (NULL + isinstance)
    # 22 LOAD_FAST                0 (user)
    # 24 LOAD_GLOBAL              4 (int)
    # 36 PRECALL                  2
    # 40 CALL                     2
    # 50 POP_JUMP_FORWARD_IF_TRUE    27 (to 106)
    # 253          52 LOAD_FAST                1 (pwd)
    # 54 LOAD_METHOD              3 (getpwnam)
    # 76 LOAD_FAST                0 (user)
    # 78 PRECALL                  1
    # 82 CALL                     1
    # 92 LOAD_CONST               2 (2)
    # 94 BINARY_SUBSCR
    # 104 STORE_FAST               0 (user)
    # 254     >>  106 LOAD_FAST                0 (user)
    # 108 RETURN_VALUE

def getgroupid(group):
    # 257           0 RESUME                   0
    # 258           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               0 (None)
    # 6 IMPORT_NAME              0 (grp)
    # 8 STORE_FAST               1 (grp)
    # 260          10 LOAD_GLOBAL              3 (NULL + isinstance)
    # 22 LOAD_FAST                0 (group)
    # 24 LOAD_GLOBAL              4 (int)
    # 36 PRECALL                  2
    # 40 CALL                     2
    # 50 POP_JUMP_FORWARD_IF_TRUE    27 (to 106)
    # 261          52 LOAD_FAST                1 (grp)
    # 54 LOAD_METHOD              3 (getgrnam)
    # 76 LOAD_FAST                0 (group)
    # 78 PRECALL                  1
    # 82 CALL                     1
    # 92 LOAD_CONST               2 (2)
    # 94 BINARY_SUBSCR
    # 104 STORE_FAST               0 (group)
    # 262     >>  106 LOAD_FAST                0 (group)
    # 108 RETURN_VALUE

class LocalPath:
    """LocalPath"""
    def ImportMismatchError():
        """LocalPath.ImportMismatchError"""
        # 270           0 RESUME                   0
        # 2 LOAD_NAME                0 (__name__)
        # 4 STORE_NAME               1 (__module__)
        # 6 LOAD_CONST               0 ('LocalPath.ImportMismatchError')
        # 8 STORE_NAME               2 (__qualname__)
        # 271          10 LOAD_CONST               1 ("raised on pyimport() if there is a mismatch of __file__'s")
        # 12 STORE_NAME               3 (__doc__)
        # 14 LOAD_CONST               2 (None)
        # 16 RETURN_VALUE

    def __init__(self, path, expanduser):
        """Initialize and return a local Path instance.

        Path can be relative to the current directory.
        If path is None it defaults to the current working directory.
        If expanduser is True, tilde-expansion is performed.
        Note that Path instances always carry an absolute path.
        Note also that passing in a local path object will simply return
        the exact same path object. Use new() to get a new copy.
        """
        # 275           0 RESUME                   0
        # 285           2 LOAD_FAST                1 (path)
        # 4 POP_JUMP_FORWARD_IF_NOT_NONE    37 (to 80)
        # 286           6 LOAD_GLOBAL              1 (NULL + error)
        # 18 LOAD_ATTR                1 (checked_call)
        # 28 LOAD_GLOBAL              4 (os)
        # 40 LOAD_ATTR                3 (getcwd)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 LOAD_FAST                0 (self)
        # 66 STORE_ATTR               4 (strpath)
        # 76 LOAD_CONST               1 (None)
        # 78 RETURN_VALUE
        # 288     >>   80 NOP
        # 289          82 LOAD_GLOBAL              5 (NULL + os)
        # 94 LOAD_ATTR                5 (fspath)
        # 104 LOAD_FAST                1 (path)
        # 106 PRECALL                  1
        # 110 CALL                     1
        # 120 STORE_FAST               1 (path)
        # 122 JUMP_FORWARD            29 (to 182)
        # >>  124 PUSH_EXC_INFO
        # 290         126 LOAD_GLOBAL             12 (TypeError)
        # 138 CHECK_EXC_MATCH
        # 140 POP_JUMP_FORWARD_IF_FALSE    16 (to 174)
        # 142 POP_TOP
        # 291         144 LOAD_GLOBAL             15 (NULL + ValueError)
        # 292         156 LOAD_CONST               2 ('can only pass None, Path instances or non-empty strings to LocalPath')
        # 291         158 PRECALL                  1
        # 162 CALL                     1
        # 172 RAISE_VARARGS            1
        # 290     >>  174 RERAISE                  0
        # >>  176 COPY                     3
        # 178 POP_EXCEPT
        # 180 RERAISE                  1
        # 295     >>  182 LOAD_FAST                2 (expanduser)
        # 184 POP_JUMP_FORWARD_IF_FALSE    31 (to 248)
        # 296         186 LOAD_GLOBAL              4 (os)
        # 198 LOAD_ATTR                8 (path)
        # 208 LOAD_METHOD              9 (expanduser)
        # 230 LOAD_FAST                1 (path)
        # 232 PRECALL                  1
        # 236 CALL                     1
        # 246 STORE_FAST               1 (path)
        # 297     >>  248 LOAD_GLOBAL             21 (NULL + abspath)
        # 260 LOAD_FAST                1 (path)
        # 262 PRECALL                  1
        # 266 CALL                     1
        # 276 LOAD_FAST                0 (self)
        # 278 STORE_ATTR               4 (strpath)
        # 288 LOAD_CONST               1 (None)
        # 290 RETURN_VALUE
        # ExceptionTable:
        # 82 to 120 -> 124 [0]
        # 124 to 174 -> 176 [1] lasti

    def chown(self, user, group, rec):
        """Change ownership to the given user and group.
            user and group may be specified by a number or
            by a name.  if rec is True change ownership
            recursively.
            """
        # 301           0 RESUME                   0
        # 307           2 LOAD_GLOBAL              1 (NULL + getuserid)
        # 14 LOAD_FAST                1 (user)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               4 (uid)
        # 308          32 LOAD_GLOBAL              3 (NULL + getgroupid)
        # 44 LOAD_FAST                2 (group)
        # 46 PRECALL                  1
        # 50 CALL                     1
        # 60 STORE_FAST               5 (gid)
        # 309          62 LOAD_FAST                3 (rec)
        # 64 POP_JUMP_FORWARD_IF_FALSE    94 (to 254)
        # 310          66 LOAD_FAST                0 (self)
        # 68 LOAD_METHOD              2 (visit)
        # 90 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7F28E40, file "_pytest\_py\path.py", line 310>)
        # 92 MAKE_FUNCTION            0
        # 94 KW_NAMES                 2
        # 96 PRECALL                  1
        # 100 CALL                     1
        # 110 GET_ITER
        # >>  112 FOR_ITER                70 (to 254)
        # 114 STORE_FAST               6 (x)
        # 311         116 LOAD_FAST                6 (x)
        # 118 LOAD_METHOD              3 (check)
        # 140 LOAD_CONST               3 (0)
        # 142 KW_NAMES                 4
        # 144 PRECALL                  1
        # 148 CALL                     1
        # 158 POP_JUMP_FORWARD_IF_FALSE    46 (to 252)
        # 312         160 LOAD_GLOBAL              9 (NULL + error)
        # 172 LOAD_ATTR                5 (checked_call)
        # 182 LOAD_GLOBAL             12 (os)
        # 194 LOAD_ATTR                7 (chown)
        # 204 LOAD_GLOBAL             17 (NULL + str)
        # 216 LOAD_FAST                6 (x)
        # 218 PRECALL                  1
        # 222 CALL                     1
        # 232 LOAD_FAST                4 (uid)
        # 234 LOAD_FAST                5 (gid)
        # 236 PRECALL                  4
        # 240 CALL                     4
        # 250 POP_TOP
        # >>  252 JUMP_BACKWARD           71 (to 112)
        # 313     >>  254 LOAD_GLOBAL              9 (NULL + error)
        # 266 LOAD_ATTR                5 (checked_call)
        # 276 LOAD_GLOBAL             12 (os)
        # 288 LOAD_ATTR                7 (chown)
        # 298 LOAD_GLOBAL             17 (NULL + str)
        # 310 LOAD_FAST                0 (self)
        # 312 PRECALL                  1
        # 316 CALL                     1
        # 326 LOAD_FAST                4 (uid)
        # 328 LOAD_FAST                5 (gid)
        # 330 PRECALL                  4
        # 334 CALL                     4
        # 344 POP_TOP
        # 346 LOAD_CONST               5 (None)
        # 348 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7F28E40, file "_pytest\_py\path.py", line 310>:
        # 310           0 RESUME                   0
        # 2 LOAD_FAST                0 (x)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (0)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE

    def readlink(self):
        """Return value of a symbolic link."""
        # 315           0 RESUME                   0
        # 318           2 LOAD_GLOBAL              1 (NULL + error)
        # 14 LOAD_ATTR                1 (checked_call)
        # 24 LOAD_GLOBAL              4 (os)
        # 36 LOAD_ATTR                3 (readlink)
        # 46 LOAD_FAST                0 (self)
        # 48 LOAD_ATTR                4 (strpath)
        # 58 PRECALL                  2
        # 62 CALL                     2
        # 72 RETURN_VALUE

    def mklinkto(self, oldname):
        """Posix style hard link to another name."""
        # 320           0 RESUME                   0
        # 322           2 LOAD_GLOBAL              1 (NULL + error)
        # 14 LOAD_ATTR                1 (checked_call)
        # 24 LOAD_GLOBAL              4 (os)
        # 36 LOAD_ATTR                3 (link)
        # 46 LOAD_GLOBAL              9 (NULL + str)
        # 58 LOAD_FAST                1 (oldname)
        # 60 PRECALL                  1
        # 64 CALL                     1
        # 74 LOAD_GLOBAL              9 (NULL + str)
        # 86 LOAD_FAST                0 (self)
        # 88 PRECALL                  1
        # 92 CALL                     1
        # 102 PRECALL                  3
        # 106 CALL                     3
        # 116 POP_TOP
        # 118 LOAD_CONST               1 (None)
        # 120 RETURN_VALUE

    def mksymlinkto(self, value, absolute):
        """Create a symbolic link with the given value (pointing to another name)."""
        # 324           0 RESUME                   0
        # 326           2 LOAD_FAST                2 (absolute)
        # 4 POP_JUMP_FORWARD_IF_FALSE    52 (to 110)
        # 327           6 LOAD_GLOBAL              1 (NULL + error)
        # 18 LOAD_ATTR                1 (checked_call)
        # 28 LOAD_GLOBAL              4 (os)
        # 40 LOAD_ATTR                3 (symlink)
        # 50 LOAD_GLOBAL              9 (NULL + str)
        # 62 LOAD_FAST                1 (value)
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 LOAD_FAST                0 (self)
        # 80 LOAD_ATTR                5 (strpath)
        # 90 PRECALL                  3
        # 94 CALL                     3
        # 104 POP_TOP
        # 106 LOAD_CONST               2 (None)
        # 108 RETURN_VALUE
        # 329     >>  110 LOAD_FAST                0 (self)
        # 112 LOAD_METHOD              6 (common)
        # 134 LOAD_FAST                1 (value)
        # 136 PRECALL                  1
        # 140 CALL                     1
        # 150 STORE_FAST               3 (base)
        # 331         152 LOAD_FAST                0 (self)
        # 154 LOAD_METHOD              7 (__class__)
        # 176 LOAD_FAST                1 (value)
        # 178 PRECALL                  1
        # 182 CALL                     1
        # 192 LOAD_METHOD              8 (relto)
        # 214 LOAD_FAST                3 (base)
        # 216 PRECALL                  1
        # 220 CALL                     1
        # 230 STORE_FAST               4 (relsource)
        # 332         232 LOAD_FAST                0 (self)
        # 234 LOAD_METHOD              8 (relto)
        # 256 LOAD_FAST                3 (base)
        # 258 PRECALL                  1
        # 262 CALL                     1
        # 272 STORE_FAST               5 (reldest)
        # 333         274 LOAD_FAST                5 (reldest)
        # 276 LOAD_METHOD              9 (count)
        # 298 LOAD_FAST                0 (self)
        # 300 LOAD_ATTR               10 (sep)
        # 310 PRECALL                  1
        # 314 CALL                     1
        # 324 STORE_FAST               6 (n)
        # 334         326 LOAD_FAST                0 (self)
        # 328 LOAD_ATTR               10 (sep)
        # 338 LOAD_METHOD             11 (join)
        # 360 LOAD_CONST               1 (('..',))
        # 362 LOAD_FAST                6 (n)
        # 364 BINARY_OP                5 (*)
        # 368 LOAD_FAST                4 (relsource)
        # 370 BUILD_TUPLE              1
        # 372 BINARY_OP                0 (+)
        # 376 PRECALL                  1
        # 380 CALL                     1
        # 390 STORE_FAST               7 (target)
        # 335         392 LOAD_GLOBAL              1 (NULL + error)
        # 404 LOAD_ATTR                1 (checked_call)
        # 414 LOAD_GLOBAL              4 (os)
        # 426 LOAD_ATTR                3 (symlink)
        # 436 LOAD_FAST                7 (target)
        # 438 LOAD_FAST                0 (self)
        # 440 LOAD_ATTR                5 (strpath)
        # 450 PRECALL                  3
        # 454 CALL                     3
        # 464 POP_TOP
        # 466 LOAD_CONST               2 (None)
        # 468 RETURN_VALUE

    def __div__(self, other):
        # 337           0 RESUME                   0
        # 338           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (join)
        # 26 LOAD_GLOBAL              3 (NULL + os)
        # 38 LOAD_ATTR                2 (fspath)
        # 48 LOAD_FAST                1 (other)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 RETURN_VALUE

    def basename(self):
        """Basename part of path."""
        # 342           0 RESUME                   0
        # 345           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_getbyspec)
        # 26 LOAD_CONST               1 ('basename')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               2 (0)
        # 44 BINARY_SUBSCR
        # 54 RETURN_VALUE

    def dirname(self):
        """Dirname part of path."""
        # 347           0 RESUME                   0
        # 350           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_getbyspec)
        # 26 LOAD_CONST               1 ('dirname')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               2 (0)
        # 44 BINARY_SUBSCR
        # 54 RETURN_VALUE

    def purebasename(self):
        """Pure base name of the path."""
        # 352           0 RESUME                   0
        # 355           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_getbyspec)
        # 26 LOAD_CONST               1 ('purebasename')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               2 (0)
        # 44 BINARY_SUBSCR
        # 54 RETURN_VALUE

    def ext(self):
        """Extension of the path (including the '.')."""
        # 357           0 RESUME                   0
        # 360           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_getbyspec)
        # 26 LOAD_CONST               1 ('ext')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               2 (0)
        # 44 BINARY_SUBSCR
        # 54 RETURN_VALUE

    def read_binary(self):
        """Read and return a bytestring from reading the path."""
        # 362           0 RESUME                   0
        # 364           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (open)
        # 26 LOAD_CONST               1 ('rb')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 BEFORE_WITH
        # 44 STORE_FAST               1 (f)
        # 365          46 LOAD_FAST                1 (f)
        # 48 LOAD_METHOD              1 (read)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 364          84 SWAP                     2
        # 86 LOAD_CONST               2 (None)
        # 88 LOAD_CONST               2 (None)
        # 90 LOAD_CONST               2 (None)
        # 92 PRECALL                  2
        # 96 CALL                     2
        # 106 POP_TOP
        # 108 RETURN_VALUE
        # >>  110 PUSH_EXC_INFO
        # 112 WITH_EXCEPT_START
        # 114 POP_JUMP_FORWARD_IF_TRUE     4 (to 124)
        # 116 RERAISE                  2
        # >>  118 COPY                     3
        # 120 POP_EXCEPT
        # 122 RERAISE                  1
        # >>  124 POP_TOP
        # 126 POP_EXCEPT
        # 128 POP_TOP
        # 130 POP_TOP
        # 132 LOAD_CONST               2 (None)
        # 134 RETURN_VALUE
        # ExceptionTable:
        # 44 to 82 -> 110 [1] lasti
        # 110 to 116 -> 118 [3] lasti
        # 124 to 124 -> 118 [3] lasti

    def read_text(self, encoding):
        """Read and return a Unicode string from reading the path."""
        # 367           0 RESUME                   0
        # 369           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (open)
        # 26 LOAD_CONST               1 ('r')
        # 28 LOAD_FAST                1 (encoding)
        # 30 KW_NAMES                 2
        # 32 PRECALL                  2
        # 36 CALL                     2
        # 46 BEFORE_WITH
        # 48 STORE_FAST               2 (f)
        # 370          50 LOAD_FAST                2 (f)
        # 52 LOAD_METHOD              1 (read)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 369          88 SWAP                     2
        # 90 LOAD_CONST               3 (None)
        # 92 LOAD_CONST               3 (None)
        # 94 LOAD_CONST               3 (None)
        # 96 PRECALL                  2
        # 100 CALL                     2
        # 110 POP_TOP
        # 112 RETURN_VALUE
        # >>  114 PUSH_EXC_INFO
        # 116 WITH_EXCEPT_START
        # 118 POP_JUMP_FORWARD_IF_TRUE     4 (to 128)
        # 120 RERAISE                  2
        # >>  122 COPY                     3
        # 124 POP_EXCEPT
        # 126 RERAISE                  1
        # >>  128 POP_TOP
        # 130 POP_EXCEPT
        # 132 POP_TOP
        # 134 POP_TOP
        # 136 LOAD_CONST               3 (None)
        # 138 RETURN_VALUE
        # ExceptionTable:
        # 48 to 86 -> 114 [1] lasti
        # 114 to 120 -> 122 [3] lasti
        # 128 to 128 -> 122 [3] lasti

    def read(self, mode):
        """Read and return a bytestring from reading the path."""
        # 372           0 RESUME                   0
        # 374           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (open)
        # 26 LOAD_FAST                1 (mode)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 BEFORE_WITH
        # 44 STORE_FAST               2 (f)
        # 375          46 LOAD_FAST                2 (f)
        # 48 LOAD_METHOD              1 (read)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 374          84 SWAP                     2
        # 86 LOAD_CONST               1 (None)
        # 88 LOAD_CONST               1 (None)
        # 90 LOAD_CONST               1 (None)
        # 92 PRECALL                  2
        # 96 CALL                     2
        # 106 POP_TOP
        # 108 RETURN_VALUE
        # >>  110 PUSH_EXC_INFO
        # 112 WITH_EXCEPT_START
        # 114 POP_JUMP_FORWARD_IF_TRUE     4 (to 124)
        # 116 RERAISE                  2
        # >>  118 COPY                     3
        # 120 POP_EXCEPT
        # 122 RERAISE                  1
        # >>  124 POP_TOP
        # 126 POP_EXCEPT
        # 128 POP_TOP
        # 130 POP_TOP
        # 132 LOAD_CONST               1 (None)
        # 134 RETURN_VALUE
        # ExceptionTable:
        # 44 to 82 -> 110 [1] lasti
        # 110 to 116 -> 118 [3] lasti
        # 124 to 124 -> 118 [3] lasti

    def readlines(self, cr):
        """Read and return a list of lines from the path. if cr is False, the
        newline will be removed from the end of each line."""
        # 377           0 RESUME                   0
        # 380           2 LOAD_CONST               1 ('r')
        # 4 STORE_FAST               2 (mode)
        # 382           6 LOAD_FAST                1 (cr)
        # 8 POP_JUMP_FORWARD_IF_TRUE    42 (to 94)
        # 383          10 LOAD_FAST                0 (self)
        # 12 LOAD_METHOD              0 (read)
        # 34 LOAD_FAST                2 (mode)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 STORE_FAST               3 (content)
        # 384          52 LOAD_FAST                3 (content)
        # 54 LOAD_METHOD              1 (split)
        # 76 LOAD_CONST               2 ('\n')
        # 78 PRECALL                  1
        # 82 CALL                     1
        # 92 RETURN_VALUE
        # 386     >>   94 LOAD_FAST                0 (self)
        # 96 LOAD_METHOD              2 (open)
        # 118 LOAD_FAST                2 (mode)
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 STORE_FAST               4 (f)
        # 387         136 NOP
        # 388         138 LOAD_FAST                4 (f)
        # 140 LOAD_METHOD              3 (readlines)
        # 162 PRECALL                  0
        # 166 CALL                     0
        # 390         176 LOAD_FAST                4 (f)
        # 178 LOAD_METHOD              4 (close)
        # 200 PRECALL                  0
        # 204 CALL                     0
        # 214 POP_TOP
        # 216 RETURN_VALUE
        # >>  218 PUSH_EXC_INFO
        # 220 LOAD_FAST                4 (f)
        # 222 LOAD_METHOD              4 (close)
        # 244 PRECALL                  0
        # 248 CALL                     0
        # 258 POP_TOP
        # 260 RERAISE                  0
        # >>  262 COPY                     3
        # 264 POP_EXCEPT
        # 266 RERAISE                  1
        # ExceptionTable:
        # 138 to 174 -> 218 [0]
        # 218 to 260 -> 262 [1] lasti

    def load(self):
        """(deprecated) return object unpickled from self.read()"""
        # 392           0 RESUME                   0
        # 394           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (open)
        # 26 LOAD_CONST               1 ('rb')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 STORE_FAST               1 (f)
        # 395          44 NOP
        # 396          46 LOAD_CONST               2 (0)
        # 48 LOAD_CONST               3 (None)
        # 50 IMPORT_NAME              1 (pickle)
        # 52 STORE_FAST               2 (pickle)
        # 398          54 LOAD_GLOBAL              5 (NULL + error)
        # 66 LOAD_ATTR                3 (checked_call)
        # 76 LOAD_FAST                2 (pickle)
        # 78 LOAD_ATTR                4 (load)
        # 88 LOAD_FAST                1 (f)
        # 90 PRECALL                  2
        # 94 CALL                     2
        # 400         104 LOAD_FAST                1 (f)
        # 106 LOAD_METHOD              5 (close)
        # 128 PRECALL                  0
        # 132 CALL                     0
        # 142 POP_TOP
        # 144 RETURN_VALUE
        # >>  146 PUSH_EXC_INFO
        # 148 LOAD_FAST                1 (f)
        # 150 LOAD_METHOD              5 (close)
        # 172 PRECALL                  0
        # 176 CALL                     0
        # 186 POP_TOP
        # 188 RERAISE                  0
        # >>  190 COPY                     3
        # 192 POP_EXCEPT
        # 194 RERAISE                  1
        # ExceptionTable:
        # 46 to 102 -> 146 [0]
        # 146 to 188 -> 190 [1] lasti

    def move(self, target):
        """Move this path to target."""
        # 402           0 RESUME                   0
        # 404           2 LOAD_FAST                1 (target)
        # 4 LOAD_METHOD              0 (relto)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 POP_JUMP_FORWARD_IF_FALSE    21 (to 86)
        # 405          44 LOAD_GLOBAL              3 (NULL + error)
        # 56 LOAD_ATTR                2 (EINVAL)
        # 66 LOAD_FAST                1 (target)
        # 68 LOAD_CONST               1 ('cannot move path into a subdirectory of itself')
        # 70 PRECALL                  2
        # 74 CALL                     2
        # 84 RAISE_VARARGS            1
        # 406     >>   86 NOP
        # 407          88 LOAD_FAST                0 (self)
        # 90 LOAD_METHOD              3 (rename)
        # 112 LOAD_FAST                1 (target)
        # 114 PRECALL                  1
        # 118 CALL                     1
        # 128 POP_TOP
        # 130 LOAD_CONST               2 (None)
        # 132 RETURN_VALUE
        # >>  134 PUSH_EXC_INFO
        # 408         136 LOAD_GLOBAL              2 (error)
        # 148 LOAD_ATTR                4 (EXDEV)
        # 158 CHECK_EXC_MATCH
        # 160 POP_JUMP_FORWARD_IF_FALSE    45 (to 252)
        # 162 POP_TOP
        # 409         164 LOAD_FAST                0 (self)
        # 166 LOAD_METHOD              5 (copy)
        # 188 LOAD_FAST                1 (target)
        # 190 PRECALL                  1
        # 194 CALL                     1
        # 204 POP_TOP
        # 410         206 LOAD_FAST                0 (self)
        # 208 LOAD_METHOD              6 (remove)
        # 230 PRECALL                  0
        # 234 CALL                     0
        # 244 POP_TOP
        # 246 POP_EXCEPT
        # 248 LOAD_CONST               2 (None)
        # 250 RETURN_VALUE
        # 408     >>  252 RERAISE                  0
        # >>  254 COPY                     3
        # 256 POP_EXCEPT
        # 258 RERAISE                  1
        # ExceptionTable:
        # 88 to 128 -> 134 [0]
        # 134 to 244 -> 254 [1] lasti
        # 252 to 252 -> 254 [1] lasti

    def fnmatch(self, pattern):
        """Return true if the basename/fullname matches the glob-'pattern'.

        valid pattern characters::

            *       matches everything
            ?       matches any single character
            [seq]   matches any character in seq
            [!seq]  matches any char not in seq

        If the pattern contains a path-separator then the full path
        is used for pattern matching and a '*' is prepended to the
        pattern.

        if the pattern doesn't contain a path-separator the pattern
        is only matched against the basename.
        """
        # 412           0 RESUME                   0
        # 429           2 PUSH_NULL
        # 4 LOAD_GLOBAL              1 (NULL + FNMatcher)
        # 16 LOAD_FAST                1 (pattern)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 LOAD_FAST                0 (self)
        # 34 PRECALL                  1
        # 38 CALL                     1
        # 48 RETURN_VALUE

    def relto(self, relpath):
        """Return a string which is the relative part of the path
        to the given 'relpath'.
        """
        # 431           0 RESUME                   0
        # 435           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (relpath)
        # 16 LOAD_GLOBAL              2 (str)
        # 28 LOAD_GLOBAL              4 (LocalPath)
        # 40 BINARY_OP                7 (|)
        # 44 PRECALL                  2
        # 48 CALL                     2
        # 58 POP_JUMP_FORWARD_IF_TRUE    18 (to 96)
        # 436          60 LOAD_GLOBAL              7 (NULL + TypeError)
        # 72 LOAD_FAST                1 (relpath)
        # 74 FORMAT_VALUE             2 (repr)
        # 76 LOAD_CONST               1 (': not a string or path object')
        # 78 BUILD_STRING             2
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 RAISE_VARARGS            1
        # 437     >>   96 LOAD_GLOBAL              3 (NULL + str)
        # 108 LOAD_FAST                1 (relpath)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 STORE_FAST               2 (strrelpath)
        # 438         126 LOAD_FAST                2 (strrelpath)
        # 128 POP_JUMP_FORWARD_IF_FALSE    27 (to 184)
        # 130 LOAD_FAST                2 (strrelpath)
        # 132 LOAD_CONST               2 (-1)
        # 134 BINARY_SUBSCR
        # 144 LOAD_FAST                0 (self)
        # 146 LOAD_ATTR                4 (sep)
        # 156 COMPARE_OP               3 (!=)
        # 162 POP_JUMP_FORWARD_IF_FALSE    10 (to 184)
        # 439         164 LOAD_FAST                2 (strrelpath)
        # 166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                4 (sep)
        # 178 BINARY_OP               13 (+=)
        # 182 STORE_FAST               2 (strrelpath)
        # 442     >>  184 LOAD_FAST                0 (self)
        # 186 LOAD_ATTR                5 (strpath)
        # 196 STORE_FAST               3 (strself)
        # 443         198 LOAD_GLOBAL             12 (sys)
        # 210 LOAD_ATTR                7 (platform)
        # 220 LOAD_CONST               3 ('win32')
        # 222 COMPARE_OP               2 (==)
        # 228 POP_JUMP_FORWARD_IF_TRUE    26 (to 282)
        # 230 LOAD_GLOBAL             17 (NULL + getattr)
        # 242 LOAD_GLOBAL             18 (os)
        # 254 LOAD_CONST               4 ('_name')
        # 256 LOAD_CONST               5 (None)
        # 258 PRECALL                  3
        # 262 CALL                     3
        # 272 LOAD_CONST               6 ('nt')
        # 274 COMPARE_OP               2 (==)
        # 280 POP_JUMP_FORWARD_IF_FALSE   103 (to 488)
        # 444     >>  282 LOAD_GLOBAL             18 (os)
        # 294 LOAD_ATTR               10 (path)
        # 304 LOAD_METHOD             11 (normcase)
        # 326 LOAD_FAST                3 (strself)
        # 328 PRECALL                  1
        # 332 CALL                     1
        # 342 LOAD_METHOD             12 (startswith)
        # 364 LOAD_GLOBAL             18 (os)
        # 376 LOAD_ATTR               10 (path)
        # 386 LOAD_METHOD             11 (normcase)
        # 408 LOAD_FAST                2 (strrelpath)
        # 410 PRECALL                  1
        # 414 CALL                     1
        # 424 PRECALL                  1
        # 428 CALL                     1
        # 438 POP_JUMP_FORWARD_IF_FALSE    23 (to 486)
        # 445         440 LOAD_FAST                3 (strself)
        # 442 LOAD_GLOBAL             27 (NULL + len)
        # 454 LOAD_FAST                2 (strrelpath)
        # 456 PRECALL                  1
        # 460 CALL                     1
        # 470 LOAD_CONST               5 (None)
        # 472 BUILD_SLICE              2
        # 474 BINARY_SUBSCR
        # 484 RETURN_VALUE
        # 444     >>  486 JUMP_FORWARD            44 (to 576)
        # 446     >>  488 LOAD_FAST                3 (strself)
        # 490 LOAD_METHOD             12 (startswith)
        # 512 LOAD_FAST                2 (strrelpath)
        # 514 PRECALL                  1
        # 518 CALL                     1
        # 528 POP_JUMP_FORWARD_IF_FALSE    23 (to 576)
        # 447         530 LOAD_FAST                3 (strself)
        # 532 LOAD_GLOBAL             27 (NULL + len)
        # 544 LOAD_FAST                2 (strrelpath)
        # 546 PRECALL                  1
        # 550 CALL                     1
        # 560 LOAD_CONST               5 (None)
        # 562 BUILD_SLICE              2
        # 564 BINARY_SUBSCR
        # 574 RETURN_VALUE
        # 448     >>  576 LOAD_CONST               7 ('')
        # 578 RETURN_VALUE

    def ensure_dir(self):
        """Ensure the path joined with args is a directory."""
        # 450           0 RESUME                   0
        # 452           2 PUSH_NULL
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (ensure)
        # 16 LOAD_FAST                1 (args)
        # 18 LOAD_CONST               1 ('dir')
        # 20 LOAD_CONST               2 (True)
        # 22 BUILD_MAP                1
        # 24 CALL_FUNCTION_EX         1
        # 26 RETURN_VALUE

    def bestrelpath(self, dest):
        """Return a string which is a relative path from self
        (assumed to be a directory) to dest such that
        self.join(bestrelpath) == dest and if not such
        path can be determined return dest.
        """
        # 454           0 RESUME                   0
        # 460           2 NOP
        # 461           4 LOAD_FAST                0 (self)
        # 6 LOAD_FAST                1 (dest)
        # 8 COMPARE_OP               2 (==)
        # 14 POP_JUMP_FORWARD_IF_FALSE    12 (to 40)
        # 462          16 LOAD_GLOBAL              0 (os)
        # 28 LOAD_ATTR                1 (curdir)
        # 38 RETURN_VALUE
        # 463     >>   40 LOAD_FAST                0 (self)
        # 42 LOAD_METHOD              2 (common)
        # 64 LOAD_FAST                1 (dest)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 STORE_FAST               2 (base)
        # 464          82 LOAD_FAST                2 (base)
        # 84 POP_JUMP_FORWARD_IF_TRUE    15 (to 116)
        # 465          86 LOAD_GLOBAL              7 (NULL + str)
        # 98 LOAD_FAST                1 (dest)
        # 100 PRECALL                  1
        # 104 CALL                     1
        # 114 RETURN_VALUE
        # 466     >>  116 LOAD_FAST                0 (self)
        # 118 LOAD_METHOD              4 (relto)
        # 140 LOAD_FAST                2 (base)
        # 142 PRECALL                  1
        # 146 CALL                     1
        # 156 STORE_FAST               3 (self2base)
        # 467         158 LOAD_FAST                1 (dest)
        # 160 LOAD_METHOD              4 (relto)
        # 182 LOAD_FAST                2 (base)
        # 184 PRECALL                  1
        # 188 CALL                     1
        # 198 STORE_FAST               4 (reldest)
        # 468         200 LOAD_FAST                3 (self2base)
        # 202 POP_JUMP_FORWARD_IF_FALSE    30 (to 264)
        # 469         204 LOAD_FAST                3 (self2base)
        # 206 LOAD_METHOD              5 (count)
        # 228 LOAD_FAST                0 (self)
        # 230 LOAD_ATTR                6 (sep)
        # 240 PRECALL                  1
        # 244 CALL                     1
        # 254 LOAD_CONST               1 (1)
        # 256 BINARY_OP                0 (+)
        # 260 STORE_FAST               5 (n)
        # 262 JUMP_FORWARD             2 (to 268)
        # 471     >>  264 LOAD_CONST               2 (0)
        # 266 STORE_FAST               5 (n)
        # 472     >>  268 LOAD_GLOBAL              0 (os)
        # 280 LOAD_ATTR                7 (pardir)
        # 290 BUILD_LIST               1
        # 292 LOAD_FAST                5 (n)
        # 294 BINARY_OP                5 (*)
        # 298 STORE_FAST               6 (lst)
        # 473         300 LOAD_FAST                4 (reldest)
        # 302 POP_JUMP_FORWARD_IF_FALSE    21 (to 346)
        # 474         304 LOAD_FAST                6 (lst)
        # 306 LOAD_METHOD              8 (append)
        # 328 LOAD_FAST                4 (reldest)
        # 330 PRECALL                  1
        # 334 CALL                     1
        # 344 POP_TOP
        # 475     >>  346 LOAD_FAST                1 (dest)
        # 348 LOAD_ATTR                6 (sep)
        # 358 LOAD_METHOD              9 (join)
        # 380 LOAD_FAST                6 (lst)
        # 382 PRECALL                  1
        # 386 CALL                     1
        # 396 STORE_FAST               7 (target)
        # 476         398 LOAD_FAST                7 (target)
        # 400 RETURN_VALUE
        # >>  402 PUSH_EXC_INFO
        # 477         404 LOAD_GLOBAL             20 (AttributeError)
        # 416 CHECK_EXC_MATCH
        # 418 POP_JUMP_FORWARD_IF_FALSE    18 (to 456)
        # 420 POP_TOP
        # 478         422 LOAD_GLOBAL              7 (NULL + str)
        # 434 LOAD_FAST                1 (dest)
        # 436 PRECALL                  1
        # 440 CALL                     1
        # 450 SWAP                     2
        # 452 POP_EXCEPT
        # 454 RETURN_VALUE
        # 477     >>  456 RERAISE                  0
        # >>  458 COPY                     3
        # 460 POP_EXCEPT
        # 462 RERAISE                  1
        # ExceptionTable:
        # 4 to 36 -> 402 [0]
        # 40 to 112 -> 402 [0]
        # 116 to 398 -> 402 [0]
        # 402 to 450 -> 458 [1] lasti
        # 456 to 456 -> 458 [1] lasti

    def exists(self):
        # 480           0 RESUME                   0
        # 481           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 RETURN_VALUE

    def isdir(self):
        # 483           0 RESUME                   0
        # 484           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (1)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE

    def isfile(self):
        # 486           0 RESUME                   0
        # 487           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (1)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE

    def parts(self, reverse):
        """Return a root-first list of all ancestor directories
        plus the path itself.
        """
        # 489           0 RESUME                   0
        # 493           2 LOAD_FAST                0 (self)
        # 4 STORE_FAST               2 (current)
        # 494           6 LOAD_FAST                0 (self)
        # 8 BUILD_LIST               1
        # 10 STORE_FAST               3 (lst)
        # 495          12 NOP
        # 496     >>   14 LOAD_FAST                2 (current)
        # 16 STORE_FAST               4 (last)
        # 497          18 LOAD_FAST                2 (current)
        # 20 LOAD_METHOD              0 (dirpath)
        # 42 PRECALL                  0
        # 46 CALL                     0
        # 56 STORE_FAST               2 (current)
        # 498          58 LOAD_FAST                4 (last)
        # 60 LOAD_FAST                2 (current)
        # 62 COMPARE_OP               2 (==)
        # 68 POP_JUMP_FORWARD_IF_FALSE     1 (to 72)
        # 499          70 JUMP_FORWARD            22 (to 116)
        # 500     >>   72 LOAD_FAST                3 (lst)
        # 74 LOAD_METHOD              1 (append)
        # 96 LOAD_FAST                2 (current)
        # 98 PRECALL                  1
        # 102 CALL                     1
        # 112 POP_TOP
        # 495         114 JUMP_BACKWARD           51 (to 14)
        # 501     >>  116 LOAD_FAST                1 (reverse)
        # 118 POP_JUMP_FORWARD_IF_TRUE    20 (to 160)
        # 502         120 LOAD_FAST                3 (lst)
        # 122 LOAD_METHOD              2 (reverse)
        # 144 PRECALL                  0
        # 148 CALL                     0
        # 158 POP_TOP
        # 503     >>  160 LOAD_FAST                3 (lst)
        # 162 RETURN_VALUE

    def common(self, other):
        """Return the common part shared with the other path
        or None if there is no common part.
        """
        # 505           0 RESUME                   0
        # 509           2 LOAD_CONST               1 (None)
        # 4 STORE_FAST               2 (last)
        # 510           6 LOAD_GLOBAL              1 (NULL + zip)
        # 18 LOAD_FAST                0 (self)
        # 20 LOAD_METHOD              1 (parts)
        # 42 PRECALL                  0
        # 46 CALL                     0
        # 56 LOAD_FAST                1 (other)
        # 58 LOAD_METHOD              1 (parts)
        # 80 PRECALL                  0
        # 84 CALL                     0
        # 94 PRECALL                  2
        # 98 CALL                     2
        # 108 GET_ITER
        # >>  110 FOR_ITER                17 (to 146)
        # 112 UNPACK_SEQUENCE          2
        # 116 STORE_FAST               3 (x)
        # 118 STORE_FAST               4 (y)
        # 511         120 LOAD_FAST                3 (x)
        # 122 LOAD_FAST                4 (y)
        # 124 COMPARE_OP               3 (!=)
        # 130 POP_JUMP_FORWARD_IF_FALSE     4 (to 140)
        # 512         132 LOAD_FAST                2 (last)
        # 134 SWAP                     2
        # 136 POP_TOP
        # 138 RETURN_VALUE
        # 513     >>  140 LOAD_FAST                3 (x)
        # 142 STORE_FAST               2 (last)
        # 144 JUMP_BACKWARD           18 (to 110)
        # 514     >>  146 LOAD_FAST                2 (last)
        # 148 RETURN_VALUE

    def __add__(self, other):
        """Return new path object with 'other' added to the basename"""
        # 516           0 RESUME                   0
        # 518           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (new)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                1 (basename)
        # 38 LOAD_GLOBAL              5 (NULL + str)
        # 50 LOAD_FAST                1 (other)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 BINARY_OP                0 (+)
        # 70 KW_NAMES                 1
        # 72 PRECALL                  1
        # 76 CALL                     1
        # 86 RETURN_VALUE

    def visit(self, fil, rec, ignore, bf, sort):
        """Yields all paths below the current one

        fil is a filter (glob pattern or callable), if not matching the
        path will not be yielded, defaulting to None (everything is
        returned)

        rec is a filter (glob pattern or callable) that controls whether
        a node is descended, defaulting to None

        ignore is an Exception class that is ignoredwhen calling dirlist()
        on any of the paths (by default, all exceptions are reported)

        bf if True will cause a breadthfirst search instead of the
        default depthfirst. Default: False

        sort if True will sort entries within each directory level.
        """
        # 520           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 538           6 LOAD_GLOBAL              1 (NULL + Visitor)
        # 18 LOAD_FAST                1 (fil)
        # 20 LOAD_FAST                2 (rec)
        # 22 LOAD_FAST                3 (ignore)
        # 24 LOAD_FAST                4 (bf)
        # 26 LOAD_FAST                5 (sort)
        # 28 PRECALL                  5
        # 32 CALL                     5
        # 42 LOAD_METHOD              1 (gen)
        # 64 LOAD_FAST                0 (self)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 GET_YIELD_FROM_ITER
        # 82 LOAD_CONST               1 (None)
        # >>   84 SEND                     3 (to 92)
        # 86 YIELD_VALUE
        # 88 RESUME                   2
        # 90 JUMP_BACKWARD_NO_INTERRUPT     4 (to 84)
        # >>   92 POP_TOP
        # 94 LOAD_CONST               1 (None)
        # 96 RETURN_VALUE

    def _sortlist(self, res, sort):
        # 540           0 RESUME                   0
        # 541           2 LOAD_FAST                2 (sort)
        # 4 POP_JUMP_FORWARD_IF_FALSE    96 (to 198)
        # 542           6 LOAD_GLOBAL              1 (NULL + hasattr)
        # 18 LOAD_FAST                2 (sort)
        # 20 LOAD_CONST               1 ('__call__')
        # 22 PRECALL                  2
        # 26 CALL                     2
        # 36 POP_JUMP_FORWARD_IF_FALSE    58 (to 154)
        # 543          38 LOAD_GLOBAL              3 (NULL + warnings)
        # 50 LOAD_ATTR                2 (warn)
        # 544          60 LOAD_GLOBAL              7 (NULL + DeprecationWarning)
        # 545          72 LOAD_CONST               2 ('listdir(sort=callable) is deprecated and breaks on python3')
        # 544          74 PRECALL                  1
        # 78 CALL                     1
        # 547          88 LOAD_CONST               3 (3)
        # 543          90 KW_NAMES                 4
        # 92 PRECALL                  2
        # 96 CALL                     2
        # 106 POP_TOP
        # 549         108 LOAD_FAST                1 (res)
        # 110 LOAD_METHOD              4 (sort)
        # 132 LOAD_FAST                2 (sort)
        # 134 PRECALL                  1
        # 138 CALL                     1
        # 148 POP_TOP
        # 150 LOAD_CONST               0 (None)
        # 152 RETURN_VALUE
        # 551     >>  154 LOAD_FAST                1 (res)
        # 156 LOAD_METHOD              4 (sort)
        # 178 PRECALL                  0
        # 182 CALL                     0
        # 192 POP_TOP
        # 194 LOAD_CONST               0 (None)
        # 196 RETURN_VALUE
        # 541     >>  198 LOAD_CONST               0 (None)
        # 200 RETURN_VALUE

    def __fspath__(self):
        # 553           0 RESUME                   0
        # 554           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (strpath)
        # 14 RETURN_VALUE

    def __hash__(self):
        # 556           0 RESUME                   0
        # 557           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (strpath)
        # 14 STORE_FAST               1 (s)
        # 558          16 LOAD_GLOBAL              2 (iswin32)
        # 28 POP_JUMP_FORWARD_IF_FALSE    20 (to 70)
        # 559          30 LOAD_FAST                1 (s)
        # 32 LOAD_METHOD              2 (lower)
        # 54 PRECALL                  0
        # 58 CALL                     0
        # 68 STORE_FAST               1 (s)
        # 560     >>   70 LOAD_GLOBAL              7 (NULL + hash)
        # 82 LOAD_FAST                1 (s)
        # 84 PRECALL                  1
        # 88 CALL                     1
        # 98 RETURN_VALUE

    def __eq__(self, other):
        # 562           0 RESUME                   0
        # 563           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (fspath)
        # 24 LOAD_FAST                0 (self)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 STORE_FAST               2 (s1)
        # 564          42 NOP
        # 565          44 LOAD_GLOBAL              1 (NULL + os)
        # 56 LOAD_ATTR                1 (fspath)
        # 66 LOAD_FAST                1 (other)
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 STORE_FAST               3 (s2)
        # 84 JUMP_FORWARD            17 (to 120)
        # >>   86 PUSH_EXC_INFO
        # 566          88 LOAD_GLOBAL              4 (TypeError)
        # 100 CHECK_EXC_MATCH
        # 102 POP_JUMP_FORWARD_IF_FALSE     4 (to 112)
        # 104 POP_TOP
        # 567         106 POP_EXCEPT
        # 108 LOAD_CONST               1 (False)
        # 110 RETURN_VALUE
        # 566     >>  112 RERAISE                  0
        # >>  114 COPY                     3
        # 116 POP_EXCEPT
        # 118 RERAISE                  1
        # 568     >>  120 LOAD_GLOBAL              6 (iswin32)
        # 132 POP_JUMP_FORWARD_IF_FALSE    59 (to 252)
        # 569         134 LOAD_FAST                2 (s1)
        # 136 LOAD_METHOD              4 (lower)
        # 158 PRECALL                  0
        # 162 CALL                     0
        # 172 STORE_FAST               2 (s1)
        # 570         174 NOP
        # 571         176 LOAD_FAST                3 (s2)
        # 178 LOAD_METHOD              4 (lower)
        # 200 PRECALL                  0
        # 204 CALL                     0
        # 214 STORE_FAST               3 (s2)
        # 216 JUMP_FORWARD            17 (to 252)
        # >>  218 PUSH_EXC_INFO
        # 572         220 LOAD_GLOBAL             10 (AttributeError)
        # 232 CHECK_EXC_MATCH
        # 234 POP_JUMP_FORWARD_IF_FALSE     4 (to 244)
        # 236 POP_TOP
        # 573         238 POP_EXCEPT
        # 240 LOAD_CONST               1 (False)
        # 242 RETURN_VALUE
        # 572     >>  244 RERAISE                  0
        # >>  246 COPY                     3
        # 248 POP_EXCEPT
        # 250 RERAISE                  1
        # 574     >>  252 LOAD_FAST                2 (s1)
        # 254 LOAD_FAST                3 (s2)
        # 256 COMPARE_OP               2 (==)
        # 262 RETURN_VALUE
        # ExceptionTable:
        # 44 to 82 -> 86 [0]
        # 86 to 104 -> 114 [1] lasti
        # 112 to 112 -> 114 [1] lasti
        # 176 to 214 -> 218 [0]
        # 218 to 236 -> 246 [1] lasti
        # 244 to 244 -> 246 [1] lasti

    def __ne__(self, other):
        # 576           0 RESUME                   0
        # 577           2 LOAD_FAST                0 (self)
        # 4 LOAD_FAST                1 (other)
        # 6 COMPARE_OP               2 (==)
        # 12 UNARY_NOT
        # 14 RETURN_VALUE

    def __lt__(self, other):
        # 579           0 RESUME                   0
        # 580           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (fspath)
        # 24 LOAD_FAST                0 (self)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 LOAD_GLOBAL              1 (NULL + os)
        # 52 LOAD_ATTR                1 (fspath)
        # 62 LOAD_FAST                1 (other)
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 COMPARE_OP               0 (<)
        # 84 RETURN_VALUE

    def __gt__(self, other):
        # 582           0 RESUME                   0
        # 583           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (fspath)
        # 24 LOAD_FAST                0 (self)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 LOAD_GLOBAL              1 (NULL + os)
        # 52 LOAD_ATTR                1 (fspath)
        # 62 LOAD_FAST                1 (other)
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 COMPARE_OP               4 (>)
        # 84 RETURN_VALUE

    def samefile(self, other):
        """Return True if 'other' references the same file as 'self'."""
        # 585           0 RESUME                   0
        # 587           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (fspath)
        # 24 LOAD_FAST                1 (other)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 STORE_FAST               1 (other)
        # 588          42 LOAD_GLOBAL              5 (NULL + isabs)
        # 54 LOAD_FAST                1 (other)
        # 56 PRECALL                  1
        # 60 CALL                     1
        # 70 POP_JUMP_FORWARD_IF_TRUE    15 (to 102)
        # 589          72 LOAD_GLOBAL              7 (NULL + abspath)
        # 84 LOAD_FAST                1 (other)
        # 86 PRECALL                  1
        # 90 CALL                     1
        # 100 STORE_FAST               1 (other)
        # 590     >>  102 LOAD_FAST                0 (self)
        # 104 LOAD_FAST                1 (other)
        # 106 COMPARE_OP               2 (==)
        # 112 POP_JUMP_FORWARD_IF_FALSE     2 (to 118)
        # 591         114 LOAD_CONST               1 (True)
        # 116 RETURN_VALUE
        # 592     >>  118 LOAD_GLOBAL              9 (NULL + hasattr)
        # 130 LOAD_GLOBAL              0 (os)
        # 142 LOAD_ATTR                5 (path)
        # 152 LOAD_CONST               2 ('samefile')
        # 154 PRECALL                  2
        # 158 CALL                     2
        # 168 POP_JUMP_FORWARD_IF_TRUE     2 (to 174)
        # 593         170 LOAD_CONST               3 (False)
        # 172 RETURN_VALUE
        # 594     >>  174 LOAD_GLOBAL             13 (NULL + error)
        # 186 LOAD_ATTR                7 (checked_call)
        # 196 LOAD_GLOBAL              0 (os)
        # 208 LOAD_ATTR                5 (path)
        # 218 LOAD_ATTR                8 (samefile)
        # 228 LOAD_FAST                0 (self)
        # 230 LOAD_ATTR                9 (strpath)
        # 240 LOAD_FAST                1 (other)
        # 242 PRECALL                  3
        # 246 CALL                     3
        # 256 RETURN_VALUE

    def remove(self, rec, ignore_errors):
        """Remove a file or directory (or a directory tree if rec=1).
        if ignore_errors is True, errors while removing directories will
        be ignored.
        """
        # 596           0 RESUME                   0
        # 601           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (1)
        # 28 LOAD_CONST               2 (0)
        # 30 KW_NAMES                 3
        # 32 PRECALL                  2
        # 36 CALL                     2
        # 46 POP_JUMP_FORWARD_IF_FALSE   109 (to 266)
        # 602          48 LOAD_FAST                1 (rec)
        # 50 POP_JUMP_FORWARD_IF_FALSE    69 (to 190)
        # 604          52 LOAD_GLOBAL              2 (iswin32)
        # 64 POP_JUMP_FORWARD_IF_FALSE    23 (to 112)
        # 605          66 LOAD_FAST                0 (self)
        # 68 LOAD_METHOD              2 (chmod)
        # 90 LOAD_CONST               4 (448)
        # 92 LOAD_CONST               1 (1)
        # 94 KW_NAMES                 5
        # 96 PRECALL                  2
        # 100 CALL                     2
        # 110 POP_TOP
        # 606     >>  112 LOAD_CONST               2 (0)
        # 114 LOAD_CONST               6 (None)
        # 116 IMPORT_NAME              3 (shutil)
        # 118 STORE_FAST               3 (shutil)
        # 608         120 LOAD_GLOBAL              9 (NULL + error)
        # 132 LOAD_ATTR                5 (checked_call)
        # 609         142 LOAD_FAST                3 (shutil)
        # 144 LOAD_ATTR                6 (rmtree)
        # 154 LOAD_FAST                0 (self)
        # 156 LOAD_ATTR                7 (strpath)
        # 166 LOAD_FAST                2 (ignore_errors)
        # 608         168 KW_NAMES                 7
        # 170 PRECALL                  3
        # 174 CALL                     3
        # 184 POP_TOP
        # 186 LOAD_CONST               6 (None)
        # 188 RETURN_VALUE
        # 612     >>  190 LOAD_GLOBAL              9 (NULL + error)
        # 202 LOAD_ATTR                5 (checked_call)
        # 212 LOAD_GLOBAL             16 (os)
        # 224 LOAD_ATTR                9 (rmdir)
        # 234 LOAD_FAST                0 (self)
        # 236 LOAD_ATTR                7 (strpath)
        # 246 PRECALL                  2
        # 250 CALL                     2
        # 260 POP_TOP
        # 262 LOAD_CONST               6 (None)
        # 264 RETURN_VALUE
        # 614     >>  266 LOAD_GLOBAL              2 (iswin32)
        # 278 POP_JUMP_FORWARD_IF_FALSE    21 (to 322)
        # 615         280 LOAD_FAST                0 (self)
        # 282 LOAD_METHOD              2 (chmod)
        # 304 LOAD_CONST               4 (448)
        # 306 PRECALL                  1
        # 310 CALL                     1
        # 320 POP_TOP
        # 616     >>  322 LOAD_GLOBAL              9 (NULL + error)
        # 334 LOAD_ATTR                5 (checked_call)
        # 344 LOAD_GLOBAL             16 (os)
        # 356 LOAD_ATTR               10 (remove)
        # 366 LOAD_FAST                0 (self)
        # 368 LOAD_ATTR                7 (strpath)
        # 378 PRECALL                  2
        # 382 CALL                     2
        # 392 POP_TOP
        # 394 LOAD_CONST               6 (None)
        # 396 RETURN_VALUE

    def computehash(self, hashtype, chunksize):
        """Return hexdigest of hashvalue for this file."""
        # 618           0 RESUME                   0
        # 620           2 NOP
        # 621           4 NOP
        # 622           6 LOAD_CONST               1 (0)
        # 8 LOAD_CONST               2 (None)
        # 10 IMPORT_NAME              0 (hashlib)
        # 12 STORE_FAST               3 (mod)
        # 14 JUMP_FORWARD            39 (to 94)
        # >>   16 PUSH_EXC_INFO
        # 623          18 LOAD_GLOBAL              2 (ImportError)
        # 30 CHECK_EXC_MATCH
        # 32 POP_JUMP_FORWARD_IF_FALSE    26 (to 86)
        # 34 POP_TOP
        # 624          36 LOAD_FAST                1 (hashtype)
        # 38 LOAD_CONST               3 ('sha1')
        # 40 COMPARE_OP               2 (==)
        # 46 POP_JUMP_FORWARD_IF_FALSE     2 (to 52)
        # 625          48 LOAD_CONST               4 ('sha')
        # 50 STORE_FAST               1 (hashtype)
        # 626     >>   52 LOAD_GLOBAL              5 (NULL + __import__)
        # 64 LOAD_FAST                1 (hashtype)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 STORE_FAST               3 (mod)
        # 82 POP_EXCEPT
        # 84 JUMP_FORWARD             4 (to 94)
        # 623     >>   86 RERAISE                  0
        # >>   88 COPY                     3
        # 90 POP_EXCEPT
        # 92 RERAISE                  1
        # 627     >>   94 PUSH_NULL
        # 96 LOAD_GLOBAL              7 (NULL + getattr)
        # 108 LOAD_FAST                3 (mod)
        # 110 LOAD_FAST                1 (hashtype)
        # 112 PRECALL                  2
        # 116 CALL                     2
        # 126 PRECALL                  0
        # 130 CALL                     0
        # 140 STORE_FAST               4 (hash)
        # 142 JUMP_FORWARD            40 (to 224)
        # >>  144 PUSH_EXC_INFO
        # 628         146 LOAD_GLOBAL              8 (AttributeError)
        # 158 LOAD_GLOBAL              2 (ImportError)
        # 170 BUILD_TUPLE              2
        # 172 CHECK_EXC_MATCH
        # 174 POP_JUMP_FORWARD_IF_FALSE    20 (to 216)
        # 176 POP_TOP
        # 629         178 LOAD_GLOBAL             11 (NULL + ValueError)
        # 190 LOAD_CONST               5 ("Don't know how to compute ")
        # 192 LOAD_FAST                1 (hashtype)
        # 194 FORMAT_VALUE             2 (repr)
        # 196 LOAD_CONST               6 (' hash')
        # 198 BUILD_STRING             3
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 RAISE_VARARGS            1
        # 628     >>  216 RERAISE                  0
        # >>  218 COPY                     3
        # 220 POP_EXCEPT
        # 222 RERAISE                  1
        # 630     >>  224 LOAD_FAST                0 (self)
        # 226 LOAD_METHOD              6 (open)
        # 248 LOAD_CONST               7 ('rb')
        # 250 PRECALL                  1
        # 254 CALL                     1
        # 264 STORE_FAST               5 (f)
        # 631         266 NOP
        # 632         268 NOP
        # 633     >>  270 LOAD_FAST                5 (f)
        # 272 LOAD_METHOD              7 (read)
        # 294 LOAD_FAST                2 (chunksize)
        # 296 PRECALL                  1
        # 300 CALL                     1
        # 310 STORE_FAST               6 (buf)
        # 634         312 LOAD_FAST                6 (buf)
        # 314 POP_JUMP_FORWARD_IF_TRUE    40 (to 396)
        # 635         316 LOAD_FAST                4 (hash)
        # 318 LOAD_METHOD              8 (hexdigest)
        # 340 PRECALL                  0
        # 344 CALL                     0
        # 638         354 LOAD_FAST                5 (f)
        # 356 LOAD_METHOD              9 (close)
        # 378 PRECALL                  0
        # 382 CALL                     0
        # 392 POP_TOP
        # 394 RETURN_VALUE
        # 636     >>  396 LOAD_FAST                4 (hash)
        # 398 LOAD_METHOD             10 (update)
        # 420 LOAD_FAST                6 (buf)
        # 422 PRECALL                  1
        # 426 CALL                     1
        # 436 POP_TOP
        # 632         438 JUMP_BACKWARD           85 (to 270)
        # >>  440 PUSH_EXC_INFO
        # 638         442 LOAD_FAST                5 (f)
        # 444 LOAD_METHOD              9 (close)
        # 466 PRECALL                  0
        # 470 CALL                     0
        # 480 POP_TOP
        # 482 RERAISE                  0
        # >>  484 COPY                     3
        # 486 POP_EXCEPT
        # 488 RERAISE                  1
        # ExceptionTable:
        # 6 to 12 -> 16 [0]
        # 14 to 14 -> 144 [0]
        # 16 to 80 -> 88 [1] lasti
        # 82 to 84 -> 144 [0]
        # 86 to 86 -> 88 [1] lasti
        # 88 to 140 -> 144 [0]
        # 144 to 216 -> 218 [1] lasti
        # 268 to 352 -> 440 [0]
        # 396 to 438 -> 440 [0]
        # 440 to 482 -> 484 [1] lasti

    def new(self):
        """Create a modified version of this path.
        the following keyword arguments modify various path parts::

          a:/some/path/to/a/file.ext
          xx                           drive
          xxxxxxxxxxxxxxxxx            dirname
                            xxxxxxxx   basename
                            xxxx       purebasename
                                 xxx   ext
        """
        # 640           0 RESUME                   0
        # 651           2 LOAD_GLOBAL              0 (object)
        # 14 LOAD_METHOD              1 (__new__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_ATTR                2 (__class__)
        # 48 PRECALL                  1
        # 52 CALL                     1
        # 62 STORE_FAST               2 (obj)
        # 652          64 LOAD_FAST                1 (kw)
        # 66 POP_JUMP_FORWARD_IF_TRUE    14 (to 96)
        # 653          68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                3 (strpath)
        # 80 LOAD_FAST                2 (obj)
        # 82 STORE_ATTR               3 (strpath)
        # 654          92 LOAD_FAST                2 (obj)
        # 94 RETURN_VALUE
        # 655     >>   96 LOAD_FAST                0 (self)
        # 98 LOAD_METHOD              4 (_getbyspec)
        # 656         120 LOAD_CONST               1 ('drive,dirname,basename,purebasename,ext')
        # 655         122 PRECALL                  1
        # 126 CALL                     1
        # 136 UNPACK_SEQUENCE          5
        # 140 STORE_FAST               3 (drive)
        # 142 STORE_FAST               4 (dirname)
        # 144 STORE_FAST               5 (_basename)
        # 146 STORE_FAST               6 (purebasename)
        # 148 STORE_FAST               7 (ext)
        # 658         150 LOAD_CONST               2 ('basename')
        # 152 LOAD_FAST                1 (kw)
        # 154 CONTAINS_OP              0
        # 156 POP_JUMP_FORWARD_IF_FALSE    27 (to 212)
        # 659         158 LOAD_CONST               3 ('purebasename')
        # 160 LOAD_FAST                1 (kw)
        # 162 CONTAINS_OP              0
        # 164 POP_JUMP_FORWARD_IF_TRUE     4 (to 174)
        # 166 LOAD_CONST               4 ('ext')
        # 168 LOAD_FAST                1 (kw)
        # 170 CONTAINS_OP              0
        # 172 POP_JUMP_FORWARD_IF_FALSE    18 (to 210)
        # 660     >>  174 LOAD_GLOBAL             11 (NULL + ValueError)
        # 186 LOAD_CONST               5 ('invalid specification ')
        # 188 LOAD_FAST                1 (kw)
        # 190 FORMAT_VALUE             2 (repr)
        # 192 BUILD_STRING             2
        # 194 PRECALL                  1
        # 198 CALL                     1
        # 208 RAISE_VARARGS            1
        # 659     >>  210 JUMP_FORWARD            84 (to 380)
        # 662     >>  212 LOAD_FAST                1 (kw)
        # 214 LOAD_METHOD              6 (setdefault)
        # 236 LOAD_CONST               3 ('purebasename')
        # 238 LOAD_FAST                6 (purebasename)
        # 240 PRECALL                  2
        # 244 CALL                     2
        # 254 STORE_FAST               8 (pb)
        # 663         256 NOP
        # 664         258 LOAD_FAST                1 (kw)
        # 260 LOAD_CONST               4 ('ext')
        # 262 BINARY_SUBSCR
        # 272 STORE_FAST               7 (ext)
        # 668         274 LOAD_FAST                7 (ext)
        # 276 POP_JUMP_FORWARD_IF_FALSE    26 (to 330)
        # 278 LOAD_FAST                7 (ext)
        # 280 LOAD_METHOD              7 (startswith)
        # 302 LOAD_CONST               6 ('.')
        # 304 PRECALL                  1
        # 308 CALL                     1
        # 318 POP_JUMP_FORWARD_IF_TRUE     5 (to 330)
        # 669         320 LOAD_CONST               6 ('.')
        # 322 LOAD_FAST                7 (ext)
        # 324 BINARY_OP                0 (+)
        # 328 STORE_FAST               7 (ext)
        # >>  330 JUMP_FORWARD            16 (to 364)
        # >>  332 PUSH_EXC_INFO
        # 665         334 LOAD_GLOBAL             16 (KeyError)
        # 346 CHECK_EXC_MATCH
        # 348 POP_JUMP_FORWARD_IF_FALSE     3 (to 356)
        # 350 POP_TOP
        # 666         352 POP_EXCEPT
        # 354 JUMP_FORWARD             4 (to 364)
        # 665     >>  356 RERAISE                  0
        # >>  358 COPY                     3
        # 360 POP_EXCEPT
        # 362 RERAISE                  1
        # 670     >>  364 LOAD_FAST                8 (pb)
        # 366 LOAD_FAST                7 (ext)
        # 368 BINARY_OP                0 (+)
        # 372 LOAD_FAST                1 (kw)
        # 374 LOAD_CONST               2 ('basename')
        # 376 STORE_SUBSCR
        # 672     >>  380 LOAD_CONST               7 ('dirname')
        # 382 LOAD_FAST                1 (kw)
        # 384 CONTAINS_OP              0
        # 386 POP_JUMP_FORWARD_IF_FALSE    14 (to 416)
        # 388 LOAD_FAST                1 (kw)
        # 390 LOAD_CONST               7 ('dirname')
        # 392 BINARY_SUBSCR
        # 402 POP_JUMP_FORWARD_IF_TRUE     6 (to 416)
        # 673         404 LOAD_FAST                3 (drive)
        # 406 LOAD_FAST                1 (kw)
        # 408 LOAD_CONST               7 ('dirname')
        # 410 STORE_SUBSCR
        # 414 JUMP_FORWARD            22 (to 460)
        # 675     >>  416 LOAD_FAST                1 (kw)
        # 418 LOAD_METHOD              6 (setdefault)
        # 440 LOAD_CONST               7 ('dirname')
        # 442 LOAD_FAST                4 (dirname)
        # 444 PRECALL                  2
        # 448 CALL                     2
        # 458 POP_TOP
        # 676     >>  460 LOAD_FAST                1 (kw)
        # 462 LOAD_METHOD              6 (setdefault)
        # 484 LOAD_CONST               8 ('sep')
        # 486 LOAD_FAST                0 (self)
        # 488 LOAD_ATTR                9 (sep)
        # 498 PRECALL                  2
        # 502 CALL                     2
        # 512 POP_TOP
        # 677         514 LOAD_GLOBAL             21 (NULL + normpath)
        # 526 PUSH_NULL
        # 528 LOAD_CONST               9 ('{dirname}{sep}{basename}')
        # 530 LOAD_ATTR               11 (format)
        # 540 LOAD_CONST              10 (())
        # 542 BUILD_MAP                0
        # 544 LOAD_FAST                1 (kw)
        # 546 DICT_MERGE               1
        # 548 CALL_FUNCTION_EX         1
        # 550 PRECALL                  1
        # 554 CALL                     1
        # 564 LOAD_FAST                2 (obj)
        # 566 STORE_ATTR               3 (strpath)
        # 678         576 LOAD_FAST                2 (obj)
        # 578 RETURN_VALUE
        # ExceptionTable:
        # 258 to 272 -> 332 [0]
        # 332 to 350 -> 358 [1] lasti
        # 356 to 356 -> 358 [1] lasti

    def _getbyspec(self, spec):
        """See new for what 'spec' can be."""
        # 680           0 RESUME                   0
        # 682           2 BUILD_LIST               0
        # 4 STORE_FAST               2 (res)
        # 683           6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (strpath)
        # 18 LOAD_METHOD              1 (split)
        # 40 LOAD_FAST                0 (self)
        # 42 LOAD_ATTR                2 (sep)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 STORE_FAST               3 (parts)
        # 685          68 LOAD_GLOBAL              7 (NULL + filter)
        # 80 LOAD_CONST               1 (None)
        # 82 LOAD_FAST                1 (spec)
        # 84 LOAD_METHOD              1 (split)
        # 106 LOAD_CONST               2 (',')
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 PRECALL                  2
        # 126 CALL                     2
        # 136 STORE_FAST               4 (args)
        # 686         138 LOAD_FAST                4 (args)
        # 140 GET_ITER
        # >>  142 EXTENDED_ARG             1
        # 144 FOR_ITER               257 (to 660)
        # 146 STORE_FAST               5 (name)
        # 687         148 LOAD_FAST                5 (name)
        # 150 LOAD_CONST               3 ('drive')
        # 152 COMPARE_OP               2 (==)
        # 158 POP_JUMP_FORWARD_IF_FALSE    28 (to 216)
        # 688         160 LOAD_FAST                2 (res)
        # 162 LOAD_METHOD              4 (append)
        # 184 LOAD_FAST                3 (parts)
        # 186 LOAD_CONST               4 (0)
        # 188 BINARY_SUBSCR
        # 198 PRECALL                  1
        # 202 CALL                     1
        # 212 POP_TOP
        # 214 JUMP_BACKWARD           37 (to 142)
        # 689     >>  216 LOAD_FAST                5 (name)
        # 218 LOAD_CONST               5 ('dirname')
        # 220 COMPARE_OP               2 (==)
        # 226 POP_JUMP_FORWARD_IF_FALSE    54 (to 336)
        # 690         228 LOAD_FAST                2 (res)
        # 230 LOAD_METHOD              4 (append)
        # 252 LOAD_FAST                0 (self)
        # 254 LOAD_ATTR                2 (sep)
        # 264 LOAD_METHOD              5 (join)
        # 286 LOAD_FAST                3 (parts)
        # 288 LOAD_CONST               1 (None)
        # 290 LOAD_CONST               6 (-1)
        # 292 BUILD_SLICE              2
        # 294 BINARY_SUBSCR
        # 304 PRECALL                  1
        # 308 CALL                     1
        # 318 PRECALL                  1
        # 322 CALL                     1
        # 332 POP_TOP
        # 334 JUMP_BACKWARD           97 (to 142)
        # 692     >>  336 LOAD_FAST                3 (parts)
        # 338 LOAD_CONST               6 (-1)
        # 340 BINARY_SUBSCR
        # 350 STORE_FAST               6 (basename)
        # 693         352 LOAD_FAST                5 (name)
        # 354 LOAD_CONST               7 ('basename')
        # 356 COMPARE_OP               2 (==)
        # 362 POP_JUMP_FORWARD_IF_FALSE    22 (to 408)
        # 694         364 LOAD_FAST                2 (res)
        # 366 LOAD_METHOD              4 (append)
        # 388 LOAD_FAST                6 (basename)
        # 390 PRECALL                  1
        # 394 CALL                     1
        # 404 POP_TOP
        # 406 JUMP_BACKWARD          133 (to 142)
        # 696     >>  408 LOAD_FAST                6 (basename)
        # 410 LOAD_METHOD              6 (rfind)
        # 432 LOAD_CONST               8 ('.')
        # 434 PRECALL                  1
        # 438 CALL                     1
        # 448 STORE_FAST               7 (i)
        # 697         450 LOAD_FAST                7 (i)
        # 452 LOAD_CONST               6 (-1)
        # 454 COMPARE_OP               2 (==)
        # 460 POP_JUMP_FORWARD_IF_FALSE     5 (to 472)
        # 698         462 LOAD_FAST                6 (basename)
        # 464 LOAD_CONST               9 ('')
        # 466 STORE_FAST               9 (ext)
        # 468 STORE_FAST               8 (purebasename)
        # 470 JUMP_FORWARD            20 (to 512)
        # 700     >>  472 LOAD_FAST                6 (basename)
        # 474 LOAD_CONST               1 (None)
        # 476 LOAD_FAST                7 (i)
        # 478 BUILD_SLICE              2
        # 480 BINARY_SUBSCR
        # 490 LOAD_FAST                6 (basename)
        # 492 LOAD_FAST                7 (i)
        # 494 LOAD_CONST               1 (None)
        # 496 BUILD_SLICE              2
        # 498 BINARY_SUBSCR
        # 508 STORE_FAST               9 (ext)
        # 510 STORE_FAST               8 (purebasename)
        # 701     >>  512 LOAD_FAST                5 (name)
        # 514 LOAD_CONST              10 ('purebasename')
        # 516 COMPARE_OP               2 (==)
        # 522 POP_JUMP_FORWARD_IF_FALSE    22 (to 568)
        # 702         524 LOAD_FAST                2 (res)
        # 526 LOAD_METHOD              4 (append)
        # 548 LOAD_FAST                8 (purebasename)
        # 550 PRECALL                  1
        # 554 CALL                     1
        # 564 POP_TOP
        # 566 JUMP_BACKWARD          213 (to 142)
        # 703     >>  568 LOAD_FAST                5 (name)
        # 570 LOAD_CONST              11 ('ext')
        # 572 COMPARE_OP               2 (==)
        # 578 POP_JUMP_FORWARD_IF_FALSE    22 (to 624)
        # 704         580 LOAD_FAST                2 (res)
        # 582 LOAD_METHOD              4 (append)
        # 604 LOAD_FAST                9 (ext)
        # 606 PRECALL                  1
        # 610 CALL                     1
        # 620 POP_TOP
        # 622 JUMP_BACKWARD          241 (to 142)
        # 706     >>  624 LOAD_GLOBAL             15 (NULL + ValueError)
        # 636 LOAD_CONST              12 ('invalid part specification ')
        # 638 LOAD_FAST                5 (name)
        # 640 FORMAT_VALUE             2 (repr)
        # 642 BUILD_STRING             2
        # 644 PRECALL                  1
        # 648 CALL                     1
        # 658 RAISE_VARARGS            1
        # 707     >>  660 LOAD_FAST                2 (res)
        # 662 RETURN_VALUE

    def dirpath(self):
        """Return the directory path joined with any given path arguments."""
        # 709           0 RESUME                   0
        # 711           2 LOAD_FAST                2 (kwargs)
        # 4 POP_JUMP_FORWARD_IF_TRUE    70 (to 146)
        # 712           6 LOAD_GLOBAL              0 (object)
        # 18 LOAD_METHOD              1 (__new__)
        # 40 LOAD_FAST                0 (self)
        # 42 LOAD_ATTR                2 (__class__)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 STORE_FAST               3 (path)
        # 713          68 LOAD_GLOBAL              7 (NULL + dirname)
        # 80 LOAD_FAST                0 (self)
        # 82 LOAD_ATTR                4 (strpath)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 LOAD_FAST                3 (path)
        # 108 STORE_ATTR               4 (strpath)
        # 714         118 LOAD_FAST                1 (args)
        # 120 POP_JUMP_FORWARD_IF_FALSE    10 (to 142)
        # 715         122 PUSH_NULL
        # 124 LOAD_FAST                3 (path)
        # 126 LOAD_ATTR                5 (join)
        # 136 LOAD_FAST                1 (args)
        # 138 CALL_FUNCTION_EX         0
        # 140 STORE_FAST               3 (path)
        # 716     >>  142 LOAD_FAST                3 (path)
        # 144 RETURN_VALUE
        # 717     >>  146 PUSH_NULL
        # 148 LOAD_FAST                0 (self)
        # 150 LOAD_METHOD              6 (new)
        # 172 LOAD_CONST               1 ('')
        # 174 KW_NAMES                 2
        # 176 PRECALL                  1
        # 180 CALL                     1
        # 190 LOAD_ATTR                5 (join)
        # 200 LOAD_FAST                1 (args)
        # 202 BUILD_MAP                0
        # 204 LOAD_FAST                2 (kwargs)
        # 206 DICT_MERGE               1
        # 208 CALL_FUNCTION_EX         1
        # 210 RETURN_VALUE

    def join(self):
        """Return a new path by appending all 'args' as path
        components.  if abs=1 is used restart from root if any
        of the args is an absolute path.
        """
        # 719           0 RESUME                   0
        # 724           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (sep)
        # 14 STORE_FAST               3 (sep)
        # 725          16 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7F29980, file "_pytest\_py\path.py", line 725>)
        # 18 MAKE_FUNCTION            0
        # 20 LOAD_FAST                2 (args)
        # 22 GET_ITER
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 STORE_FAST               4 (strargs)
        # 726          40 LOAD_FAST                0 (self)
        # 42 LOAD_ATTR                1 (strpath)
        # 52 STORE_FAST               5 (strpath)
        # 727          54 LOAD_FAST                1 (abs)
        # 56 POP_JUMP_FORWARD_IF_FALSE    63 (to 184)
        # 728          58 BUILD_LIST               0
        # 60 STORE_FAST               6 (newargs)
        # 729          62 LOAD_GLOBAL              5 (NULL + reversed)
        # 74 LOAD_FAST                4 (strargs)
        # 76 PRECALL                  1
        # 80 CALL                     1
        # 90 GET_ITER
        # >>   92 FOR_ITER                45 (to 184)
        # 94 STORE_FAST               7 (arg)
        # 730          96 LOAD_GLOBAL              7 (NULL + isabs)
        # 108 LOAD_FAST                7 (arg)
        # 110 PRECALL                  1
        # 114 CALL                     1
        # 124 POP_JUMP_FORWARD_IF_FALSE     6 (to 138)
        # 731         126 LOAD_FAST                7 (arg)
        # 128 STORE_FAST               5 (strpath)
        # 732         130 LOAD_FAST                6 (newargs)
        # 132 STORE_FAST               4 (strargs)
        # 733         134 POP_TOP
        # 136 JUMP_FORWARD            23 (to 184)
        # 734     >>  138 LOAD_FAST                6 (newargs)
        # 140 LOAD_METHOD              4 (insert)
        # 162 LOAD_CONST               2 (0)
        # 164 LOAD_FAST                7 (arg)
        # 166 PRECALL                  2
        # 170 CALL                     2
        # 180 POP_TOP
        # 182 JUMP_BACKWARD           46 (to 92)
        # 736     >>  184 LOAD_FAST                5 (strpath)
        # 186 LOAD_METHOD              5 (endswith)
        # 208 LOAD_FAST                3 (sep)
        # 210 PRECALL                  1
        # 214 CALL                     1
        # 224 POP_JUMP_FORWARD_IF_FALSE     2 (to 230)
        # 226 LOAD_CONST               3 ('')
        # 228 JUMP_FORWARD             1 (to 232)
        # >>  230 LOAD_FAST                3 (sep)
        # >>  232 STORE_FAST               8 (actual_sep)
        # 737         234 LOAD_FAST                4 (strargs)
        # 236 GET_ITER
        # >>  238 FOR_ITER                83 (to 406)
        # 240 STORE_FAST               7 (arg)
        # 738         242 LOAD_FAST                7 (arg)
        # 244 LOAD_METHOD              6 (strip)
        # 266 LOAD_FAST                3 (sep)
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 STORE_FAST               7 (arg)
        # 739         284 LOAD_GLOBAL             14 (iswin32)
        # 296 POP_JUMP_FORWARD_IF_FALSE    43 (to 384)
        # 741         298 LOAD_FAST                7 (arg)
        # 300 LOAD_METHOD              6 (strip)
        # 322 LOAD_CONST               4 ('/')
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 STORE_FAST               7 (arg)
        # 742         340 LOAD_FAST                7 (arg)
        # 342 LOAD_METHOD              8 (replace)
        # 364 LOAD_CONST               4 ('/')
        # 366 LOAD_FAST                3 (sep)
        # 368 PRECALL                  2
        # 372 CALL                     2
        # 382 STORE_FAST               7 (arg)
        # 743     >>  384 LOAD_FAST                5 (strpath)
        # 386 LOAD_FAST                8 (actual_sep)
        # 388 BINARY_OP                0 (+)
        # 392 LOAD_FAST                7 (arg)
        # 394 BINARY_OP                0 (+)
        # 398 STORE_FAST               5 (strpath)
        # 744         400 LOAD_FAST                3 (sep)
        # 402 STORE_FAST               8 (actual_sep)
        # 404 JUMP_BACKWARD           84 (to 238)
        # 745     >>  406 LOAD_GLOBAL             18 (object)
        # 418 LOAD_METHOD             10 (__new__)
        # 440 LOAD_FAST                0 (self)
        # 442 LOAD_ATTR               11 (__class__)
        # 452 PRECALL                  1
        # 456 CALL                     1
        # 466 STORE_FAST               9 (obj)
        # 746         468 LOAD_GLOBAL             25 (NULL + normpath)
        # 480 LOAD_FAST                5 (strpath)
        # 482 PRECALL                  1
        # 486 CALL                     1
        # 496 LOAD_FAST                9 (obj)
        # 498 STORE_ATTR               1 (strpath)
        # 747         508 LOAD_FAST                9 (obj)
        # 510 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7F29980, file "_pytest\_py\path.py", line 725>:
        # 725           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                22 (to 52)
        # 8 STORE_FAST               1 (arg)
        # 10 LOAD_GLOBAL              1 (NULL + os)
        # 22 LOAD_ATTR                1 (fspath)
        # 32 LOAD_FAST                1 (arg)
        # 34 PRECALL                  1
        # 38 CALL                     1
        # 48 LIST_APPEND              2
        # 50 JUMP_BACKWARD           23 (to 6)
        # >>   52 RETURN_VALUE

    def open(self, mode, ensure, encoding):
        """Return an opened file with the given mode.

        If ensure is True, create parent directories if needed.
        """
        # 749           0 RESUME                   0
        # 754           2 LOAD_FAST                2 (ensure)
        # 4 POP_JUMP_FORWARD_IF_FALSE    40 (to 86)
        # 755           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (dirpath)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 LOAD_METHOD              1 (ensure)
        # 66 LOAD_CONST               1 (1)
        # 68 KW_NAMES                 2
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 756     >>   86 LOAD_FAST                3 (encoding)
        # 88 POP_JUMP_FORWARD_IF_FALSE    39 (to 168)
        # 757          90 LOAD_GLOBAL              5 (NULL + error)
        # 102 LOAD_ATTR                3 (checked_call)
        # 758         112 LOAD_GLOBAL              8 (io)
        # 124 LOAD_ATTR                5 (open)
        # 759         134 LOAD_FAST                0 (self)
        # 136 LOAD_ATTR                6 (strpath)
        # 760         146 LOAD_FAST                1 (mode)
        # 761         148 LOAD_FAST                3 (encoding)
        # 757         150 KW_NAMES                 3
        # 152 PRECALL                  4
        # 156 CALL                     4
        # 166 RETURN_VALUE
        # 763     >>  168 LOAD_GLOBAL              5 (NULL + error)
        # 180 LOAD_ATTR                3 (checked_call)
        # 190 LOAD_GLOBAL             10 (open)
        # 202 LOAD_FAST                0 (self)
        # 204 LOAD_ATTR                6 (strpath)
        # 214 LOAD_FAST                1 (mode)
        # 216 PRECALL                  3
        # 220 CALL                     3
        # 230 RETURN_VALUE

    def _fastjoin(self, name):
        # 765           0 RESUME                   0
        # 766           2 LOAD_GLOBAL              0 (object)
        # 14 LOAD_METHOD              1 (__new__)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_ATTR                2 (__class__)
        # 48 PRECALL                  1
        # 52 CALL                     1
        # 62 STORE_FAST               2 (child)
        # 767          64 LOAD_FAST                0 (self)
        # 66 LOAD_ATTR                3 (strpath)
        # 76 LOAD_FAST                0 (self)
        # 78 LOAD_ATTR                4 (sep)
        # 88 BINARY_OP                0 (+)
        # 92 LOAD_FAST                1 (name)
        # 94 BINARY_OP                0 (+)
        # 98 LOAD_FAST                2 (child)
        # 100 STORE_ATTR               3 (strpath)
        # 768         110 LOAD_FAST                2 (child)
        # 112 RETURN_VALUE

    def islink(self):
        # 770           0 RESUME                   0
        # 771           2 LOAD_GLOBAL              1 (NULL + islink)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (strpath)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 RETURN_VALUE

    def check(self):
        """Check a path for existence and properties.

        Without arguments, return True if the path exists, otherwise False.

        valid checkers::

            file = 1  # is a file
            file = 0  # is not a file (may not even exist)
            dir = 1  # is a dir
            link = 1  # is a link
            exists = 1  # exists

        You can specify multiple checker definitions, for example::

            path.check(file=1, link=1)  # a link pointing to a file
        """
        # 773           0 RESUME                   0
        # 790           2 LOAD_FAST                1 (kw)
        # 4 POP_JUMP_FORWARD_IF_TRUE    20 (to 46)
        # 791           6 LOAD_GLOBAL              1 (NULL + exists)
        # 18 LOAD_FAST                0 (self)
        # 20 LOAD_ATTR                1 (strpath)
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE
        # 792     >>   46 LOAD_GLOBAL              5 (NULL + len)
        # 58 LOAD_FAST                1 (kw)
        # 60 PRECALL                  1
        # 64 CALL                     1
        # 74 LOAD_CONST               1 (1)
        # 76 COMPARE_OP               2 (==)
        # 82 POP_JUMP_FORWARD_IF_FALSE    68 (to 220)
        # 793          84 LOAD_CONST               2 ('dir')
        # 86 LOAD_FAST                1 (kw)
        # 88 CONTAINS_OP              0
        # 90 POP_JUMP_FORWARD_IF_FALSE    30 (to 152)
        # 794          92 LOAD_FAST                1 (kw)
        # 94 LOAD_CONST               2 ('dir')
        # 96 BINARY_SUBSCR
        # 106 LOAD_GLOBAL              7 (NULL + isdir)
        # 118 LOAD_FAST                0 (self)
        # 120 LOAD_ATTR                1 (strpath)
        # 130 PRECALL                  1
        # 134 CALL                     1
        # 144 BINARY_OP               12 (^)
        # 148 UNARY_NOT
        # 150 RETURN_VALUE
        # 795     >>  152 LOAD_CONST               3 ('file')
        # 154 LOAD_FAST                1 (kw)
        # 156 CONTAINS_OP              0
        # 158 POP_JUMP_FORWARD_IF_FALSE    30 (to 220)
        # 796         160 LOAD_FAST                1 (kw)
        # 162 LOAD_CONST               3 ('file')
        # 164 BINARY_SUBSCR
        # 174 LOAD_GLOBAL              9 (NULL + isfile)
        # 186 LOAD_FAST                0 (self)
        # 188 LOAD_ATTR                1 (strpath)
        # 198 PRECALL                  1
        # 202 CALL                     1
        # 212 BINARY_OP               12 (^)
        # 216 UNARY_NOT
        # 218 RETURN_VALUE
        # 797     >>  220 LOAD_FAST                1 (kw)
        # 222 POP_JUMP_FORWARD_IF_TRUE     4 (to 232)
        # 798         224 LOAD_CONST               4 ('exists')
        # 226 LOAD_CONST               1 (1)
        # 228 BUILD_MAP                1
        # 230 STORE_FAST               1 (kw)
        # 799     >>  232 LOAD_GLOBAL             11 (NULL + Checkers)
        # 244 LOAD_FAST                0 (self)
        # 246 PRECALL                  1
        # 250 CALL                     1
        # 260 LOAD_METHOD              6 (_evaluate)
        # 282 LOAD_FAST                1 (kw)
        # 284 PRECALL                  1
        # 288 CALL                     1
        # 298 RETURN_VALUE

    def listdir(self, fil, sort):
        """List directory contents, possibly filter by the given fil func
        and possibly sorted.
        """
        # 803           0 RESUME                   0
        # 807           2 LOAD_FAST                1 (fil)
        # 4 POP_JUMP_FORWARD_IF_NOT_NONE    59 (to 124)
        # 6 LOAD_FAST                2 (sort)
        # 8 POP_JUMP_FORWARD_IF_NOT_NONE    57 (to 124)
        # 808          10 LOAD_GLOBAL              1 (NULL + error)
        # 22 LOAD_ATTR                1 (checked_call)
        # 32 LOAD_GLOBAL              4 (os)
        # 44 LOAD_ATTR                3 (listdir)
        # 54 LOAD_FAST                0 (self)
        # 56 LOAD_ATTR                4 (strpath)
        # 66 PRECALL                  2
        # 70 CALL                     2
        # 80 STORE_FAST               3 (names)
        # 809          82 LOAD_GLOBAL             11 (NULL + map_as_list)
        # 94 LOAD_FAST                0 (self)
        # 96 LOAD_ATTR                6 (_fastjoin)
        # 106 LOAD_FAST                3 (names)
        # 108 PRECALL                  2
        # 112 CALL                     2
        # 122 RETURN_VALUE
        # 810     >>  124 LOAD_GLOBAL             15 (NULL + isinstance)
        # 136 LOAD_FAST                1 (fil)
        # 138 LOAD_GLOBAL             16 (str)
        # 150 PRECALL                  2
        # 154 CALL                     2
        # 164 POP_JUMP_FORWARD_IF_FALSE    87 (to 340)
        # 811         166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                9 (_patternchars)
        # 178 LOAD_METHOD             10 (intersection)
        # 200 LOAD_FAST                1 (fil)
        # 202 PRECALL                  1
        # 206 CALL                     1
        # 216 POP_JUMP_FORWARD_IF_TRUE    46 (to 310)
        # 812         218 LOAD_FAST                0 (self)
        # 220 LOAD_METHOD              6 (_fastjoin)
        # 242 LOAD_FAST                1 (fil)
        # 244 PRECALL                  1
        # 248 CALL                     1
        # 258 STORE_FAST               4 (child)
        # 813         260 LOAD_GLOBAL             23 (NULL + exists)
        # 272 LOAD_FAST                4 (child)
        # 274 LOAD_ATTR                4 (strpath)
        # 284 PRECALL                  1
        # 288 CALL                     1
        # 298 POP_JUMP_FORWARD_IF_FALSE     3 (to 306)
        # 814         300 LOAD_FAST                4 (child)
        # 302 BUILD_LIST               1
        # 304 RETURN_VALUE
        # 815     >>  306 BUILD_LIST               0
        # 308 RETURN_VALUE
        # 816     >>  310 LOAD_GLOBAL             25 (NULL + FNMatcher)
        # 322 LOAD_FAST                1 (fil)
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 STORE_FAST               1 (fil)
        # 817     >>  340 LOAD_GLOBAL              1 (NULL + error)
        # 352 LOAD_ATTR                1 (checked_call)
        # 362 LOAD_GLOBAL              4 (os)
        # 374 LOAD_ATTR                3 (listdir)
        # 384 LOAD_FAST                0 (self)
        # 386 LOAD_ATTR                4 (strpath)
        # 396 PRECALL                  2
        # 400 CALL                     2
        # 410 STORE_FAST               3 (names)
        # 818         412 BUILD_LIST               0
        # 414 STORE_FAST               5 (res)
        # 819         416 LOAD_FAST                3 (names)
        # 418 GET_ITER
        # >>  420 FOR_ITER                57 (to 536)
        # 422 STORE_FAST               6 (name)
        # 820         424 LOAD_FAST                0 (self)
        # 426 LOAD_METHOD              6 (_fastjoin)
        # 448 LOAD_FAST                6 (name)
        # 450 PRECALL                  1
        # 454 CALL                     1
        # 464 STORE_FAST               4 (child)
        # 821         466 LOAD_FAST                1 (fil)
        # 468 POP_JUMP_FORWARD_IF_NONE    11 (to 492)
        # 470 PUSH_NULL
        # 472 LOAD_FAST                1 (fil)
        # 474 LOAD_FAST                4 (child)
        # 476 PRECALL                  1
        # 480 CALL                     1
        # 490 POP_JUMP_FORWARD_IF_FALSE    21 (to 534)
        # 822     >>  492 LOAD_FAST                5 (res)
        # 494 LOAD_METHOD             13 (append)
        # 516 LOAD_FAST                4 (child)
        # 518 PRECALL                  1
        # 522 CALL                     1
        # 532 POP_TOP
        # >>  534 JUMP_BACKWARD           58 (to 420)
        # 823     >>  536 LOAD_FAST                0 (self)
        # 538 LOAD_METHOD             14 (_sortlist)
        # 560 LOAD_FAST                5 (res)
        # 562 LOAD_FAST                2 (sort)
        # 564 PRECALL                  2
        # 568 CALL                     2
        # 578 POP_TOP
        # 824         580 LOAD_FAST                5 (res)
        # 582 RETURN_VALUE

    def size(self):
        """Return size of the underlying file object"""
        # 826           0 RESUME                   0
        # 828           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (stat)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_ATTR                1 (size)
        # 50 RETURN_VALUE

    def mtime(self):
        """Return last modification time of the path."""
        # 830           0 RESUME                   0
        # 832           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (stat)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_ATTR                1 (mtime)
        # 50 RETURN_VALUE

    def copy(self, target, mode, stat):
        """Copy path to target.

        If mode is True, will copy permission from path to target.
        If stat is True, copy permission, last modification
        time, last access time, and flags from path to target.
        """
        # 834           0 RESUME                   0
        # 841           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (1)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 POP_JUMP_FORWARD_IF_FALSE   122 (to 290)
        # 842          46 LOAD_FAST                1 (target)
        # 48 LOAD_METHOD              0 (check)
        # 70 LOAD_CONST               1 (1)
        # 72 KW_NAMES                 3
        # 74 PRECALL                  1
        # 78 CALL                     1
        # 88 POP_JUMP_FORWARD_IF_FALSE    26 (to 142)
        # 843          90 LOAD_FAST                1 (target)
        # 92 LOAD_METHOD              1 (join)
        # 114 LOAD_FAST                0 (self)
        # 116 LOAD_ATTR                2 (basename)
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 STORE_FAST               1 (target)
        # 844     >>  142 LOAD_FAST                0 (self)
        # 144 LOAD_FAST                1 (target)
        # 146 COMPARE_OP               3 (!=)
        # 152 POP_JUMP_FORWARD_IF_TRUE     2 (to 158)
        # 154 LOAD_ASSERTION_ERROR
        # 156 RAISE_VARARGS            1
        # 845     >>  158 LOAD_GLOBAL              7 (NULL + copychunked)
        # 170 LOAD_FAST                0 (self)
        # 172 LOAD_FAST                1 (target)
        # 174 PRECALL                  2
        # 178 CALL                     2
        # 188 POP_TOP
        # 846         190 LOAD_FAST                2 (mode)
        # 192 POP_JUMP_FORWARD_IF_FALSE    26 (to 246)
        # 847         194 LOAD_GLOBAL              9 (NULL + copymode)
        # 206 LOAD_FAST                0 (self)
        # 208 LOAD_ATTR                5 (strpath)
        # 218 LOAD_FAST                1 (target)
        # 220 LOAD_ATTR                5 (strpath)
        # 230 PRECALL                  2
        # 234 CALL                     2
        # 244 POP_TOP
        # 848     >>  246 LOAD_FAST                3 (stat)
        # 248 POP_JUMP_FORWARD_IF_FALSE    18 (to 286)
        # 849         250 LOAD_GLOBAL             13 (NULL + copystat)
        # 262 LOAD_FAST                0 (self)
        # 264 LOAD_FAST                1 (target)
        # 266 PRECALL                  2
        # 270 CALL                     2
        # 280 POP_TOP
        # 282 LOAD_CONST               7 (None)
        # 284 RETURN_VALUE
        # 848     >>  286 LOAD_CONST               7 (None)
        # 288 RETURN_VALUE
        # 852     >>  290 LOAD_CONST               4 (<code object rec at 0x000001EBD7F29D40, file "_pytest\_py\path.py", line 852>)
        # 292 MAKE_FUNCTION            0
        # 294 STORE_FAST               4 (rec)
        # 855         296 LOAD_FAST                0 (self)
        # 298 LOAD_METHOD              7 (visit)
        # 320 LOAD_FAST                4 (rec)
        # 322 KW_NAMES                 5
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 GET_ITER
        # >>  340 EXTENDED_ARG             1
        # 342 FOR_ITER               276 (to 896)
        # 344 STORE_FAST               5 (x)
        # 856         346 LOAD_FAST                5 (x)
        # 348 LOAD_METHOD              8 (relto)
        # 370 LOAD_FAST                0 (self)
        # 372 PRECALL                  1
        # 376 CALL                     1
        # 386 STORE_FAST               6 (relpath)
        # 857         388 LOAD_FAST                1 (target)
        # 390 LOAD_METHOD              1 (join)
        # 412 LOAD_FAST                6 (relpath)
        # 414 PRECALL                  1
        # 418 CALL                     1
        # 428 STORE_FAST               7 (newx)
        # 858         430 LOAD_FAST                7 (newx)
        # 432 LOAD_METHOD              9 (dirpath)
        # 454 PRECALL                  0
        # 458 CALL                     0
        # 468 LOAD_METHOD             10 (ensure)
        # 490 LOAD_CONST               1 (1)
        # 492 KW_NAMES                 3
        # 494 PRECALL                  1
        # 498 CALL                     1
        # 508 POP_TOP
        # 859         510 LOAD_FAST                5 (x)
        # 512 LOAD_METHOD              0 (check)
        # 534 LOAD_CONST               1 (1)
        # 536 KW_NAMES                 6
        # 538 PRECALL                  1
        # 542 CALL                     1
        # 552 POP_JUMP_FORWARD_IF_FALSE    40 (to 634)
        # 860         554 LOAD_FAST                7 (newx)
        # 556 LOAD_METHOD             11 (mksymlinkto)
        # 578 LOAD_FAST                5 (x)
        # 580 LOAD_METHOD             12 (readlink)
        # 602 PRECALL                  0
        # 606 CALL                     0
        # 616 PRECALL                  1
        # 620 CALL                     1
        # 630 POP_TOP
        # 861         632 JUMP_BACKWARD          147 (to 340)
        # 862     >>  634 LOAD_FAST                5 (x)
        # 636 LOAD_METHOD              0 (check)
        # 658 LOAD_CONST               1 (1)
        # 660 KW_NAMES                 2
        # 662 PRECALL                  1
        # 666 CALL                     1
        # 676 POP_JUMP_FORWARD_IF_FALSE    17 (to 712)
        # 863         678 LOAD_GLOBAL              7 (NULL + copychunked)
        # 690 LOAD_FAST                5 (x)
        # 692 LOAD_FAST                7 (newx)
        # 694 PRECALL                  2
        # 698 CALL                     2
        # 708 POP_TOP
        # 710 JUMP_FORWARD            44 (to 800)
        # 864     >>  712 LOAD_FAST                5 (x)
        # 714 LOAD_METHOD              0 (check)
        # 736 LOAD_CONST               1 (1)
        # 738 KW_NAMES                 3
        # 740 PRECALL                  1
        # 744 CALL                     1
        # 754 POP_JUMP_FORWARD_IF_FALSE    22 (to 800)
        # 865         756 LOAD_FAST                7 (newx)
        # 758 LOAD_METHOD             10 (ensure)
        # 780 LOAD_CONST               1 (1)
        # 782 KW_NAMES                 3
        # 784 PRECALL                  1
        # 788 CALL                     1
        # 798 POP_TOP
        # 866     >>  800 LOAD_FAST                2 (mode)
        # 802 POP_JUMP_FORWARD_IF_FALSE    26 (to 856)
        # 867         804 LOAD_GLOBAL              9 (NULL + copymode)
        # 816 LOAD_FAST                5 (x)
        # 818 LOAD_ATTR                5 (strpath)
        # 828 LOAD_FAST                7 (newx)
        # 830 LOAD_ATTR                5 (strpath)
        # 840 PRECALL                  2
        # 844 CALL                     2
        # 854 POP_TOP
        # 868     >>  856 LOAD_FAST                3 (stat)
        # 858 POP_JUMP_FORWARD_IF_FALSE    16 (to 892)
        # 869         860 LOAD_GLOBAL             13 (NULL + copystat)
        # 872 LOAD_FAST                5 (x)
        # 874 LOAD_FAST                7 (newx)
        # 876 PRECALL                  2
        # 880 CALL                     2
        # 890 POP_TOP
        # >>  892 EXTENDED_ARG             1
        # 894 JUMP_BACKWARD          278 (to 340)
        # 855     >>  896 LOAD_CONST               7 (None)
        # 898 RETURN_VALUE
        # Disassembly of <code object rec at 0x000001EBD7F29D40, file "_pytest\_py\path.py", line 852>:
        # 852           0 RESUME                   0
        # 853           2 LOAD_FAST                0 (p)
        # 4 LOAD_METHOD              0 (check)
        # 26 LOAD_CONST               1 (0)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE

    def rename(self, target):
        """Rename this path to target."""
        # 871           0 RESUME                   0
        # 873           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (fspath)
        # 24 LOAD_FAST                1 (target)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 STORE_FAST               1 (target)
        # 874          42 LOAD_GLOBAL              5 (NULL + error)
        # 54 LOAD_ATTR                3 (checked_call)
        # 64 LOAD_GLOBAL              0 (os)
        # 76 LOAD_ATTR                4 (rename)
        # 86 LOAD_FAST                0 (self)
        # 88 LOAD_ATTR                5 (strpath)
        # 98 LOAD_FAST                1 (target)
        # 100 PRECALL                  3
        # 104 CALL                     3
        # 114 RETURN_VALUE

    def dump(self, obj, bin):
        """Pickle object into path location"""
        # 876           0 RESUME                   0
        # 878           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (open)
        # 26 LOAD_CONST               1 ('wb')
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 STORE_FAST               3 (f)
        # 879          44 LOAD_CONST               2 (0)
        # 46 LOAD_CONST               3 (None)
        # 48 IMPORT_NAME              1 (pickle)
        # 50 STORE_FAST               4 (pickle)
        # 881          52 NOP
        # 882          54 LOAD_GLOBAL              5 (NULL + error)
        # 66 LOAD_ATTR                3 (checked_call)
        # 76 LOAD_FAST                4 (pickle)
        # 78 LOAD_ATTR                4 (dump)
        # 88 LOAD_FAST                1 (obj)
        # 90 LOAD_FAST                3 (f)
        # 92 LOAD_FAST                2 (bin)
        # 94 PRECALL                  4
        # 98 CALL                     4
        # 108 POP_TOP
        # 884         110 LOAD_FAST                3 (f)
        # 112 LOAD_METHOD              5 (close)
        # 134 PRECALL                  0
        # 138 CALL                     0
        # 148 POP_TOP
        # 150 LOAD_CONST               3 (None)
        # 152 RETURN_VALUE
        # >>  154 PUSH_EXC_INFO
        # 156 LOAD_FAST                3 (f)
        # 158 LOAD_METHOD              5 (close)
        # 180 PRECALL                  0
        # 184 CALL                     0
        # 194 POP_TOP
        # 196 RERAISE                  0
        # >>  198 COPY                     3
        # 200 POP_EXCEPT
        # 202 RERAISE                  1
        # ExceptionTable:
        # 54 to 108 -> 154 [0]
        # 154 to 196 -> 198 [1] lasti

    def mkdir(self):
        """Create & return the directory joined with args."""
        # 886           0 RESUME                   0
        # 888           2 PUSH_NULL
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (join)
        # 16 LOAD_FAST                1 (args)
        # 18 CALL_FUNCTION_EX         0
        # 20 STORE_FAST               2 (p)
        # 889          22 LOAD_GLOBAL              3 (NULL + error)
        # 34 LOAD_ATTR                2 (checked_call)
        # 44 LOAD_GLOBAL              6 (os)
        # 56 LOAD_ATTR                4 (mkdir)
        # 66 LOAD_GLOBAL              7 (NULL + os)
        # 78 LOAD_ATTR                5 (fspath)
        # 88 LOAD_FAST                2 (p)
        # 90 PRECALL                  1
        # 94 CALL                     1
        # 104 PRECALL                  2
        # 108 CALL                     2
        # 118 POP_TOP
        # 890         120 LOAD_FAST                2 (p)
        # 122 RETURN_VALUE

    def write_binary(self, data, ensure):
        """Write binary data into path.   If ensure is True create
        missing parent directories.
        """
        # 892           0 RESUME                   0
        # 896           2 LOAD_FAST                2 (ensure)
        # 4 POP_JUMP_FORWARD_IF_FALSE    40 (to 86)
        # 897           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (dirpath)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 LOAD_METHOD              1 (ensure)
        # 66 LOAD_CONST               1 (1)
        # 68 KW_NAMES                 2
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 898     >>   86 LOAD_FAST                0 (self)
        # 88 LOAD_METHOD              2 (open)
        # 110 LOAD_CONST               3 ('wb')
        # 112 PRECALL                  1
        # 116 CALL                     1
        # 126 BEFORE_WITH
        # 128 STORE_FAST               3 (f)
        # 899         130 LOAD_FAST                3 (f)
        # 132 LOAD_METHOD              3 (write)
        # 154 LOAD_FAST                1 (data)
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 170 POP_TOP
        # 898         172 LOAD_CONST               4 (None)
        # 174 LOAD_CONST               4 (None)
        # 176 LOAD_CONST               4 (None)
        # 178 PRECALL                  2
        # 182 CALL                     2
        # 192 POP_TOP
        # 194 LOAD_CONST               4 (None)
        # 196 RETURN_VALUE
        # >>  198 PUSH_EXC_INFO
        # 200 WITH_EXCEPT_START
        # 202 POP_JUMP_FORWARD_IF_TRUE     4 (to 212)
        # 204 RERAISE                  2
        # >>  206 COPY                     3
        # 208 POP_EXCEPT
        # 210 RERAISE                  1
        # >>  212 POP_TOP
        # 214 POP_EXCEPT
        # 216 POP_TOP
        # 218 POP_TOP
        # 220 LOAD_CONST               4 (None)
        # 222 RETURN_VALUE
        # ExceptionTable:
        # 128 to 170 -> 198 [1] lasti
        # 198 to 204 -> 206 [3] lasti
        # 212 to 212 -> 206 [3] lasti

    def write_text(self, data, encoding, ensure):
        """Write text data into path using the specified encoding.
        If ensure is True create missing parent directories.
        """
        # 901           0 RESUME                   0
        # 905           2 LOAD_FAST                3 (ensure)
        # 4 POP_JUMP_FORWARD_IF_FALSE    40 (to 86)
        # 906           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (dirpath)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 LOAD_METHOD              1 (ensure)
        # 66 LOAD_CONST               1 (1)
        # 68 KW_NAMES                 2
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 907     >>   86 LOAD_FAST                0 (self)
        # 88 LOAD_METHOD              2 (open)
        # 110 LOAD_CONST               3 ('w')
        # 112 LOAD_FAST                2 (encoding)
        # 114 KW_NAMES                 4
        # 116 PRECALL                  2
        # 120 CALL                     2
        # 130 BEFORE_WITH
        # 132 STORE_FAST               4 (f)
        # 908         134 LOAD_FAST                4 (f)
        # 136 LOAD_METHOD              3 (write)
        # 158 LOAD_FAST                1 (data)
        # 160 PRECALL                  1
        # 164 CALL                     1
        # 174 POP_TOP
        # 907         176 LOAD_CONST               5 (None)
        # 178 LOAD_CONST               5 (None)
        # 180 LOAD_CONST               5 (None)
        # 182 PRECALL                  2
        # 186 CALL                     2
        # 196 POP_TOP
        # 198 LOAD_CONST               5 (None)
        # 200 RETURN_VALUE
        # >>  202 PUSH_EXC_INFO
        # 204 WITH_EXCEPT_START
        # 206 POP_JUMP_FORWARD_IF_TRUE     4 (to 216)
        # 208 RERAISE                  2
        # >>  210 COPY                     3
        # 212 POP_EXCEPT
        # 214 RERAISE                  1
        # >>  216 POP_TOP
        # 218 POP_EXCEPT
        # 220 POP_TOP
        # 222 POP_TOP
        # 224 LOAD_CONST               5 (None)
        # 226 RETURN_VALUE
        # ExceptionTable:
        # 132 to 174 -> 202 [1] lasti
        # 202 to 208 -> 210 [3] lasti
        # 216 to 216 -> 210 [3] lasti

    def write(self, data, mode, ensure):
        """Write data into path.   If ensure is True create
        missing parent directories.
        """
        # 910           0 RESUME                   0
        # 914           2 LOAD_FAST                3 (ensure)
        # 4 POP_JUMP_FORWARD_IF_FALSE    40 (to 86)
        # 915           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (dirpath)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 LOAD_METHOD              1 (ensure)
        # 66 LOAD_CONST               1 (1)
        # 68 KW_NAMES                 2
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 POP_TOP
        # 916     >>   86 LOAD_CONST               3 ('b')
        # 88 LOAD_FAST                2 (mode)
        # 90 CONTAINS_OP              0
        # 92 POP_JUMP_FORWARD_IF_FALSE    37 (to 168)
        # 917          94 LOAD_GLOBAL              5 (NULL + isinstance)
        # 106 LOAD_FAST                1 (data)
        # 108 LOAD_GLOBAL              6 (bytes)
        # 120 PRECALL                  2
        # 124 CALL                     2
        # 134 POP_JUMP_FORWARD_IF_TRUE    15 (to 166)
        # 918         136 LOAD_GLOBAL              9 (NULL + ValueError)
        # 148 LOAD_CONST               4 ('can only process bytes')
        # 150 PRECALL                  1
        # 154 CALL                     1
        # 164 RAISE_VARARGS            1
        # 917     >>  166 JUMP_FORWARD            96 (to 360)
        # 920     >>  168 LOAD_GLOBAL              5 (NULL + isinstance)
        # 180 LOAD_FAST                1 (data)
        # 182 LOAD_GLOBAL             10 (str)
        # 194 PRECALL                  2
        # 198 CALL                     2
        # 208 POP_JUMP_FORWARD_IF_TRUE    75 (to 360)
        # 921         210 LOAD_GLOBAL              5 (NULL + isinstance)
        # 222 LOAD_FAST                1 (data)
        # 224 LOAD_GLOBAL              6 (bytes)
        # 236 PRECALL                  2
        # 240 CALL                     2
        # 250 POP_JUMP_FORWARD_IF_TRUE    16 (to 284)
        # 922         252 LOAD_GLOBAL             11 (NULL + str)
        # 264 LOAD_FAST                1 (data)
        # 266 PRECALL                  1
        # 270 CALL                     1
        # 280 STORE_FAST               1 (data)
        # 282 JUMP_FORWARD            38 (to 360)
        # 924     >>  284 LOAD_FAST                1 (data)
        # 286 LOAD_METHOD              6 (decode)
        # 308 LOAD_GLOBAL             15 (NULL + sys)
        # 320 LOAD_ATTR                8 (getdefaultencoding)
        # 330 PRECALL                  0
        # 334 CALL                     0
        # 344 PRECALL                  1
        # 348 CALL                     1
        # 358 STORE_FAST               1 (data)
        # 925     >>  360 LOAD_FAST                0 (self)
        # 362 LOAD_METHOD              9 (open)
        # 384 LOAD_FAST                2 (mode)
        # 386 PRECALL                  1
        # 390 CALL                     1
        # 400 STORE_FAST               4 (f)
        # 926         402 NOP
        # 927         404 LOAD_FAST                4 (f)
        # 406 LOAD_METHOD             10 (write)
        # 428 LOAD_FAST                1 (data)
        # 430 PRECALL                  1
        # 434 CALL                     1
        # 444 POP_TOP
        # 929         446 LOAD_FAST                4 (f)
        # 448 LOAD_METHOD             11 (close)
        # 470 PRECALL                  0
        # 474 CALL                     0
        # 484 POP_TOP
        # 486 LOAD_CONST               5 (None)
        # 488 RETURN_VALUE
        # >>  490 PUSH_EXC_INFO
        # 492 LOAD_FAST                4 (f)
        # 494 LOAD_METHOD             11 (close)
        # 516 PRECALL                  0
        # 520 CALL                     0
        # 530 POP_TOP
        # 532 RERAISE                  0
        # >>  534 COPY                     3
        # 536 POP_EXCEPT
        # 538 RERAISE                  1
        # ExceptionTable:
        # 404 to 444 -> 490 [0]
        # 490 to 532 -> 534 [1] lasti

    def _ensuredirs(self):
        # 931           0 RESUME                   0
        # 932           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (dirpath)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               1 (parent)
        # 933          42 LOAD_FAST                1 (parent)
        # 44 LOAD_FAST                0 (self)
        # 46 COMPARE_OP               2 (==)
        # 52 POP_JUMP_FORWARD_IF_FALSE     2 (to 58)
        # 934          54 LOAD_FAST                0 (self)
        # 56 RETURN_VALUE
        # 935     >>   58 LOAD_FAST                1 (parent)
        # 60 LOAD_METHOD              1 (check)
        # 82 LOAD_CONST               1 (0)
        # 84 KW_NAMES                 2
        # 86 PRECALL                  1
        # 90 CALL                     1
        # 100 POP_JUMP_FORWARD_IF_FALSE    20 (to 142)
        # 936         102 LOAD_FAST                1 (parent)
        # 104 LOAD_METHOD              2 (_ensuredirs)
        # 126 PRECALL                  0
        # 130 CALL                     0
        # 140 POP_TOP
        # 937     >>  142 LOAD_FAST                0 (self)
        # 144 LOAD_METHOD              1 (check)
        # 166 LOAD_CONST               1 (0)
        # 168 KW_NAMES                 2
        # 170 PRECALL                  1
        # 174 CALL                     1
        # 184 POP_JUMP_FORWARD_IF_FALSE    66 (to 318)
        # 938         186 NOP
        # 939         188 LOAD_FAST                0 (self)
        # 190 LOAD_METHOD              3 (mkdir)
        # 212 PRECALL                  0
        # 216 CALL                     0
        # 226 POP_TOP
        # 228 JUMP_FORWARD            44 (to 318)
        # >>  230 PUSH_EXC_INFO
        # 940         232 LOAD_GLOBAL              8 (error)
        # 244 LOAD_ATTR                5 (EEXIST)
        # 254 CHECK_EXC_MATCH
        # 256 POP_JUMP_FORWARD_IF_FALSE    26 (to 310)
        # 258 POP_TOP
        # 943         260 LOAD_FAST                0 (self)
        # 262 LOAD_METHOD              1 (check)
        # 284 LOAD_CONST               1 (0)
        # 286 KW_NAMES                 2
        # 288 PRECALL                  1
        # 292 CALL                     1
        # 302 POP_JUMP_FORWARD_IF_FALSE     1 (to 306)
        # 944         304 RAISE_VARARGS            0
        # 943     >>  306 POP_EXCEPT
        # 308 JUMP_FORWARD             4 (to 318)
        # 940     >>  310 RERAISE                  0
        # >>  312 COPY                     3
        # 314 POP_EXCEPT
        # 316 RERAISE                  1
        # 945     >>  318 LOAD_FAST                0 (self)
        # 320 RETURN_VALUE
        # ExceptionTable:
        # 188 to 226 -> 230 [0]
        # 230 to 304 -> 312 [1] lasti
        # 310 to 310 -> 312 [1] lasti

    def ensure(self):
        """Ensure that an args-joined path exists (by default as
        a file). if you specify a keyword argument 'dir=True'
        then the path is forced to be a directory path.
        """
        # 947           0 RESUME                   0
        # 952           2 PUSH_NULL
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (join)
        # 16 LOAD_FAST                1 (args)
        # 18 CALL_FUNCTION_EX         0
        # 20 STORE_FAST               3 (p)
        # 953          22 LOAD_FAST                2 (kwargs)
        # 24 LOAD_METHOD              1 (get)
        # 46 LOAD_CONST               1 ('dir')
        # 48 LOAD_CONST               2 (0)
        # 50 PRECALL                  2
        # 54 CALL                     2
        # 64 POP_JUMP_FORWARD_IF_FALSE    20 (to 106)
        # 954          66 LOAD_FAST                3 (p)
        # 68 LOAD_METHOD              2 (_ensuredirs)
        # 90 PRECALL                  0
        # 94 CALL                     0
        # 104 RETURN_VALUE
        # 956     >>  106 LOAD_FAST                3 (p)
        # 108 LOAD_METHOD              3 (dirpath)
        # 130 PRECALL                  0
        # 134 CALL                     0
        # 144 LOAD_METHOD              2 (_ensuredirs)
        # 166 PRECALL                  0
        # 170 CALL                     0
        # 180 POP_TOP
        # 957         182 LOAD_FAST                3 (p)
        # 184 LOAD_METHOD              4 (check)
        # 206 LOAD_CONST               3 (1)
        # 208 KW_NAMES                 4
        # 210 PRECALL                  1
        # 214 CALL                     1
        # 224 POP_JUMP_FORWARD_IF_TRUE    39 (to 304)
        # 958         226 LOAD_FAST                3 (p)
        # 228 LOAD_METHOD              5 (open)
        # 250 LOAD_CONST               5 ('wb')
        # 252 PRECALL                  1
        # 256 CALL                     1
        # 266 LOAD_METHOD              6 (close)
        # 288 PRECALL                  0
        # 292 CALL                     0
        # 302 POP_TOP
        # 959     >>  304 LOAD_FAST                3 (p)
        # 306 RETURN_VALUE

    def stat(self, raising):
        # 961           0 RESUME                   0
        # 962           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def stat(self, raising):
        # 964           0 RESUME                   0
        # 965           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def stat(self, raising):
        """Return an os.stat() tuple."""
        # 967           0 RESUME                   0
        # 969           2 LOAD_FAST                1 (raising)
        # 4 POP_JUMP_FORWARD_IF_FALSE    50 (to 106)
        # 970           6 LOAD_GLOBAL              1 (NULL + Stat)
        # 18 LOAD_FAST                0 (self)
        # 20 LOAD_GLOBAL              3 (NULL + error)
        # 32 LOAD_ATTR                2 (checked_call)
        # 42 LOAD_GLOBAL              6 (os)
        # 54 LOAD_ATTR                4 (stat)
        # 64 LOAD_FAST                0 (self)
        # 66 LOAD_ATTR                5 (strpath)
        # 76 PRECALL                  2
        # 80 CALL                     2
        # 90 PRECALL                  2
        # 94 CALL                     2
        # 104 RETURN_VALUE
        # 971     >>  106 NOP
        # 972         108 LOAD_GLOBAL              1 (NULL + Stat)
        # 120 LOAD_FAST                0 (self)
        # 122 LOAD_GLOBAL              7 (NULL + os)
        # 134 LOAD_ATTR                4 (stat)
        # 144 LOAD_FAST                0 (self)
        # 146 LOAD_ATTR                5 (strpath)
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 170 PRECALL                  2
        # 174 CALL                     2
        # 184 RETURN_VALUE
        # >>  186 PUSH_EXC_INFO
        # 973         188 LOAD_GLOBAL             12 (KeyboardInterrupt)
        # 200 CHECK_EXC_MATCH
        # 202 POP_JUMP_FORWARD_IF_FALSE     2 (to 208)
        # 204 POP_TOP
        # 974         206 RAISE_VARARGS            0
        # 975     >>  208 LOAD_GLOBAL             14 (Exception)
        # 220 CHECK_EXC_MATCH
        # 222 POP_JUMP_FORWARD_IF_FALSE     4 (to 232)
        # 224 POP_TOP
        # 976         226 POP_EXCEPT
        # 228 LOAD_CONST               1 (None)
        # 230 RETURN_VALUE
        # 975     >>  232 RERAISE                  0
        # >>  234 COPY                     3
        # 236 POP_EXCEPT
        # 238 RERAISE                  1
        # ExceptionTable:
        # 108 to 182 -> 186 [0]
        # 186 to 224 -> 234 [1] lasti
        # 232 to 232 -> 234 [1] lasti

    def lstat(self):
        """Return an os.lstat() tuple."""
        # 978           0 RESUME                   0
        # 980           2 LOAD_GLOBAL              1 (NULL + Stat)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_GLOBAL              3 (NULL + error)
        # 28 LOAD_ATTR                2 (checked_call)
        # 38 LOAD_GLOBAL              6 (os)
        # 50 LOAD_ATTR                4 (lstat)
        # 60 LOAD_FAST                0 (self)
        # 62 LOAD_ATTR                5 (strpath)
        # 72 PRECALL                  2
        # 76 CALL                     2
        # 86 PRECALL                  2
        # 90 CALL                     2
        # 100 RETURN_VALUE

    def setmtime(self, mtime):
        """Set modification time for the given path.  if 'mtime' is None
        (the default) then the file's mtime is set to current time.

        Note that the resolution for 'mtime' is platform dependent.
        """
        # 982           0 RESUME                   0
        # 988           2 LOAD_FAST                1 (mtime)
        # 4 POP_JUMP_FORWARD_IF_NOT_NONE    37 (to 80)
        # 989           6 LOAD_GLOBAL              1 (NULL + error)
        # 18 LOAD_ATTR                1 (checked_call)
        # 28 LOAD_GLOBAL              4 (os)
        # 40 LOAD_ATTR                3 (utime)
        # 50 LOAD_FAST                0 (self)
        # 52 LOAD_ATTR                4 (strpath)
        # 62 LOAD_FAST                1 (mtime)
        # 64 PRECALL                  3
        # 68 CALL                     3
        # 78 RETURN_VALUE
        # 990     >>   80 NOP
        # 991          82 LOAD_GLOBAL              1 (NULL + error)
        # 94 LOAD_ATTR                1 (checked_call)
        # 104 LOAD_GLOBAL              4 (os)
        # 116 LOAD_ATTR                3 (utime)
        # 126 LOAD_FAST                0 (self)
        # 128 LOAD_ATTR                4 (strpath)
        # 138 LOAD_CONST               2 (-1)
        # 140 LOAD_FAST                1 (mtime)
        # 142 BUILD_TUPLE              2
        # 144 PRECALL                  3
        # 148 CALL                     3
        # 158 RETURN_VALUE
        # >>  160 PUSH_EXC_INFO
        # 992         162 LOAD_GLOBAL              0 (error)
        # 174 LOAD_ATTR                5 (EINVAL)
        # 184 CHECK_EXC_MATCH
        # 186 POP_JUMP_FORWARD_IF_FALSE    60 (to 308)
        # 188 POP_TOP
        # 993         190 LOAD_GLOBAL              1 (NULL + error)
        # 202 LOAD_ATTR                1 (checked_call)
        # 212 LOAD_GLOBAL              4 (os)
        # 224 LOAD_ATTR                3 (utime)
        # 234 LOAD_FAST                0 (self)
        # 236 LOAD_ATTR                4 (strpath)
        # 246 LOAD_FAST                0 (self)
        # 248 LOAD_METHOD              6 (atime)
        # 270 PRECALL                  0
        # 274 CALL                     0
        # 284 LOAD_FAST                1 (mtime)
        # 286 BUILD_TUPLE              2
        # 288 PRECALL                  3
        # 292 CALL                     3
        # 302 SWAP                     2
        # 304 POP_EXCEPT
        # 306 RETURN_VALUE
        # 992     >>  308 RERAISE                  0
        # >>  310 COPY                     3
        # 312 POP_EXCEPT
        # 314 RERAISE                  1
        # ExceptionTable:
        # 82 to 156 -> 160 [0]
        # 160 to 302 -> 310 [1] lasti
        # 308 to 308 -> 310 [1] lasti

    def chdir(self):
        """Change directory to self and return old current directory"""
        # 995           0 RESUME                   0
        # 997           2 NOP
        # 998           4 LOAD_FAST                0 (self)
        # 6 LOAD_METHOD              0 (__class__)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 STORE_FAST               1 (old)
        # 44 JUMP_FORWARD            23 (to 92)
        # >>   46 PUSH_EXC_INFO
        # 999          48 LOAD_GLOBAL              2 (error)
        # 60 LOAD_ATTR                2 (ENOENT)
        # 70 CHECK_EXC_MATCH
        # 72 POP_JUMP_FORWARD_IF_FALSE     5 (to 84)
        # 74 POP_TOP
        # 1000          76 LOAD_CONST               1 (None)
        # 78 STORE_FAST               1 (old)
        # 80 POP_EXCEPT
        # 82 JUMP_FORWARD             4 (to 92)
        # 999     >>   84 RERAISE                  0
        # >>   86 COPY                     3
        # 88 POP_EXCEPT
        # 90 RERAISE                  1
        # 1001     >>   92 LOAD_GLOBAL              3 (NULL + error)
        # 104 LOAD_ATTR                3 (checked_call)
        # 114 LOAD_GLOBAL              8 (os)
        # 126 LOAD_ATTR                5 (chdir)
        # 136 LOAD_FAST                0 (self)
        # 138 LOAD_ATTR                6 (strpath)
        # 148 PRECALL                  2
        # 152 CALL                     2
        # 162 POP_TOP
        # 1002         164 LOAD_FAST                1 (old)
        # 166 RETURN_VALUE
        # ExceptionTable:
        # 4 to 42 -> 46 [0]
        # 46 to 78 -> 86 [1] lasti
        # 84 to 84 -> 86 [1] lasti

    def as_cwd(self):
        """
        Return a context manager, which changes to the path's dir during the
        managed "with" context.
        On __enter__ it returns the old dir, which might be ``None``.
        """
        # 1004           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 1011           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (chdir)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 STORE_FAST               1 (old)
        # 1012          46 NOP
        # 1013          48 LOAD_FAST                1 (old)
        # 50 YIELD_VALUE
        # 52 RESUME                   1
        # 54 POP_TOP
        # 1015          56 LOAD_FAST                1 (old)
        # 58 POP_JUMP_FORWARD_IF_NONE    22 (to 104)
        # 1016          60 LOAD_FAST                1 (old)
        # 62 LOAD_METHOD              0 (chdir)
        # 84 PRECALL                  0
        # 88 CALL                     0
        # 98 POP_TOP
        # 100 LOAD_CONST               1 (None)
        # 102 RETURN_VALUE
        # 1015     >>  104 LOAD_CONST               1 (None)
        # 106 RETURN_VALUE
        # >>  108 PUSH_EXC_INFO
        # 110 LOAD_FAST                1 (old)
        # 112 POP_JUMP_FORWARD_IF_NONE    21 (to 156)
        # 1016         114 LOAD_FAST                1 (old)
        # 116 LOAD_METHOD              0 (chdir)
        # 138 PRECALL                  0
        # 142 CALL                     0
        # 152 POP_TOP
        # 154 RERAISE                  0
        # 1015     >>  156 RERAISE                  0
        # >>  158 COPY                     3
        # 160 POP_EXCEPT
        # 162 RERAISE                  1
        # ExceptionTable:
        # 48 to 54 -> 108 [0]
        # 108 to 156 -> 158 [1] lasti

    def realpath(self):
        """Return a new path which contains no symbolic links."""
        # 1018           0 RESUME                   0
        # 1020           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (__class__)
        # 26 LOAD_GLOBAL              2 (os)
        # 38 LOAD_ATTR                2 (path)
        # 48 LOAD_METHOD              3 (realpath)
        # 70 LOAD_FAST                0 (self)
        # 72 LOAD_ATTR                4 (strpath)
        # 82 PRECALL                  1
        # 86 CALL                     1
        # 96 PRECALL                  1
        # 100 CALL                     1
        # 110 RETURN_VALUE

    def atime(self):
        """Return last access time of the path."""
        # 1022           0 RESUME                   0
        # 1024           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (stat)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_ATTR                1 (atime)
        # 50 RETURN_VALUE

    def __repr__(self):
        # 1026           0 RESUME                   0
        # 1027           2 LOAD_CONST               1 ('local(')
        # 4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (strpath)
        # 16 FORMAT_VALUE             2 (repr)
        # 18 LOAD_CONST               2 (')')
        # 20 BUILD_STRING             3
        # 22 RETURN_VALUE

    def __str__(self):
        """Return string representation of the Path."""
        # 1029           0 RESUME                   0
        # 1031           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (strpath)
        # 14 RETURN_VALUE

    def chmod(self, mode, rec):
        """Change permissions to the given mode. If mode is an
        integer it directly encodes the os-specific modes.
        if rec is True perform recursively.
        """
        # 1033           0 RESUME                   0
        # 1038           2 LOAD_GLOBAL              1 (NULL + isinstance)
        # 14 LOAD_FAST                1 (mode)
        # 16 LOAD_GLOBAL              2 (int)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_JUMP_FORWARD_IF_TRUE    19 (to 82)
        # 1039          44 LOAD_GLOBAL              5 (NULL + TypeError)
        # 56 LOAD_CONST               1 ('mode ')
        # 58 LOAD_FAST                1 (mode)
        # 60 FORMAT_VALUE             2 (repr)
        # 62 LOAD_CONST               2 (' must be an integer')
        # 64 BUILD_STRING             3
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RAISE_VARARGS            1
        # 1040     >>   82 LOAD_FAST                2 (rec)
        # 84 POP_JUMP_FORWARD_IF_FALSE    70 (to 226)
        # 1041          86 LOAD_FAST                0 (self)
        # 88 LOAD_METHOD              3 (visit)
        # 110 LOAD_FAST                2 (rec)
        # 112 KW_NAMES                 3
        # 114 PRECALL                  1
        # 118 CALL                     1
        # 128 GET_ITER
        # >>  130 FOR_ITER                47 (to 226)
        # 132 STORE_FAST               3 (x)
        # 1042         134 LOAD_GLOBAL              9 (NULL + error)
        # 146 LOAD_ATTR                5 (checked_call)
        # 156 LOAD_GLOBAL             12 (os)
        # 168 LOAD_ATTR                7 (chmod)
        # 178 LOAD_GLOBAL             17 (NULL + str)
        # 190 LOAD_FAST                3 (x)
        # 192 PRECALL                  1
        # 196 CALL                     1
        # 206 LOAD_FAST                1 (mode)
        # 208 PRECALL                  3
        # 212 CALL                     3
        # 222 POP_TOP
        # 224 JUMP_BACKWARD           48 (to 130)
        # 1043     >>  226 LOAD_GLOBAL              9 (NULL + error)
        # 238 LOAD_ATTR                5 (checked_call)
        # 248 LOAD_GLOBAL             12 (os)
        # 260 LOAD_ATTR                7 (chmod)
        # 270 LOAD_FAST                0 (self)
        # 272 LOAD_ATTR                9 (strpath)
        # 282 LOAD_FAST                1 (mode)
        # 284 PRECALL                  3
        # 288 CALL                     3
        # 298 POP_TOP
        # 300 LOAD_CONST               4 (None)
        # 302 RETURN_VALUE

    def pypkgpath(self):
        """Return the Python package path by looking for the last
        directory upwards which still contains an __init__.py.
        Return None if a pkgpath cannot be determined.
        """
        # 1045           0 RESUME                   0
        # 1050           2 LOAD_CONST               1 (None)
        # 4 STORE_FAST               1 (pkgpath)
        # 1051           6 LOAD_FAST                0 (self)
        # 8 LOAD_METHOD              0 (parts)
        # 30 LOAD_CONST               2 (True)
        # 32 KW_NAMES                 3
        # 34 PRECALL                  1
        # 38 CALL                     1
        # 48 GET_ITER
        # >>   50 FOR_ITER                87 (to 226)
        # 52 STORE_FAST               2 (parent)
        # 1052          54 LOAD_FAST                2 (parent)
        # 56 LOAD_METHOD              1 (isdir)
        # 78 PRECALL                  0
        # 82 CALL                     0
        # 92 POP_JUMP_FORWARD_IF_FALSE    65 (to 224)
        # 1053          94 LOAD_FAST                2 (parent)
        # 96 LOAD_METHOD              2 (join)
        # 118 LOAD_CONST               4 ('__init__.py')
        # 120 PRECALL                  1
        # 124 CALL                     1
        # 134 LOAD_METHOD              3 (exists)
        # 156 PRECALL                  0
        # 160 CALL                     0
        # 170 POP_JUMP_FORWARD_IF_TRUE     2 (to 176)
        # 1054         172 POP_TOP
        # 174 JUMP_FORWARD            25 (to 226)
        # 1055     >>  176 LOAD_GLOBAL              9 (NULL + isimportable)
        # 188 LOAD_FAST                2 (parent)
        # 190 LOAD_ATTR                5 (basename)
        # 200 PRECALL                  1
        # 204 CALL                     1
        # 214 POP_JUMP_FORWARD_IF_TRUE     2 (to 220)
        # 1056         216 POP_TOP
        # 218 JUMP_FORWARD             3 (to 226)
        # 1057     >>  220 LOAD_FAST                2 (parent)
        # 222 STORE_FAST               1 (pkgpath)
        # >>  224 JUMP_BACKWARD           88 (to 50)
        # 1058     >>  226 LOAD_FAST                1 (pkgpath)
        # 228 RETURN_VALUE

    def _ensuresyspath(self, ensuremode, path):
        # 1060           0 RESUME                   0
        # 1061           2 LOAD_FAST                1 (ensuremode)
        # 4 POP_JUMP_FORWARD_IF_FALSE   126 (to 258)
        # 1062           6 LOAD_GLOBAL              1 (NULL + str)
        # 18 LOAD_FAST                2 (path)
        # 20 PRECALL                  1
        # 24 CALL                     1
        # 34 STORE_FAST               3 (s)
        # 1063          36 LOAD_FAST                1 (ensuremode)
        # 38 LOAD_CONST               1 ('append')
        # 40 COMPARE_OP               2 (==)
        # 46 POP_JUMP_FORWARD_IF_FALSE    49 (to 146)
        # 1064          48 LOAD_FAST                3 (s)
        # 50 LOAD_GLOBAL              2 (sys)
        # 62 LOAD_ATTR                2 (path)
        # 72 CONTAINS_OP              1
        # 74 POP_JUMP_FORWARD_IF_FALSE    33 (to 142)
        # 1065          76 LOAD_GLOBAL              2 (sys)
        # 88 LOAD_ATTR                2 (path)
        # 98 LOAD_METHOD              3 (append)
        # 120 LOAD_FAST                3 (s)
        # 122 PRECALL                  1
        # 126 CALL                     1
        # 136 POP_TOP
        # 138 LOAD_CONST               0 (None)
        # 140 RETURN_VALUE
        # 1064     >>  142 LOAD_CONST               0 (None)
        # 144 RETURN_VALUE
        # 1067     >>  146 LOAD_FAST                3 (s)
        # 148 LOAD_GLOBAL              2 (sys)
        # 160 LOAD_ATTR                2 (path)
        # 170 LOAD_CONST               2 (0)
        # 172 BINARY_SUBSCR
        # 182 COMPARE_OP               3 (!=)
        # 188 POP_JUMP_FORWARD_IF_FALSE    36 (to 262)
        # 1068         190 LOAD_GLOBAL              2 (sys)
        # 202 LOAD_ATTR                2 (path)
        # 212 LOAD_METHOD              4 (insert)
        # 234 LOAD_CONST               2 (0)
        # 236 LOAD_FAST                3 (s)
        # 238 PRECALL                  2
        # 242 CALL                     2
        # 252 POP_TOP
        # 254 LOAD_CONST               0 (None)
        # 256 RETURN_VALUE
        # 1061     >>  258 LOAD_CONST               0 (None)
        # 260 RETURN_VALUE
        # 1067     >>  262 LOAD_CONST               0 (None)
        # 264 RETURN_VALUE

    def pyimport(self, modname, ensuresyspath):
        """Return path as an imported python module.

        If modname is None, look for the containing package
        and construct an according module name.
        The module will be put/looked up in sys.modules.
        if ensuresyspath is True then the root dir for importing
        the file (taking __init__.py files into account) will
        be prepended to sys.path if it isn't there already.
        If ensuresyspath=="append" the root dir will be appended
        if it isn't already contained in sys.path.
        if ensuresyspath is False no modification of syspath happens.

        Special value of ensuresyspath=="importlib" is intended
        purely for using in pytest, it is capable only of importing
        separate .py files outside packages, e.g. for test suite
        without any __init__.py file. It effectively allows having
        same-named test modules in different places and offers
        mild opt-in via this option. Note that it works only in
        recent versions of python.
        """
        # 1070           0 RESUME                   0
        # 1091           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (check)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_JUMP_FORWARD_IF_TRUE    20 (to 82)
        # 1092          42 LOAD_GLOBAL              3 (NULL + error)
        # 54 LOAD_ATTR                2 (ENOENT)
        # 64 LOAD_FAST                0 (self)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 RAISE_VARARGS            1
        # 1094     >>   82 LOAD_FAST                2 (ensuresyspath)
        # 84 LOAD_CONST               1 ('importlib')
        # 86 COMPARE_OP               2 (==)
        # 92 POP_JUMP_FORWARD_IF_FALSE   143 (to 380)
        # 1095          94 LOAD_FAST                1 (modname)
        # 96 POP_JUMP_FORWARD_IF_NOT_NONE     7 (to 112)
        # 1096          98 LOAD_FAST                0 (self)
        # 100 LOAD_ATTR                3 (purebasename)
        # 110 STORE_FAST               1 (modname)
        # 1097     >>  112 LOAD_GLOBAL              8 (importlib)
        # 124 LOAD_ATTR                5 (util)
        # 134 LOAD_METHOD              6 (spec_from_file_location)
        # 156 LOAD_FAST                1 (modname)
        # 158 LOAD_GLOBAL             15 (NULL + str)
        # 170 LOAD_FAST                0 (self)
        # 172 PRECALL                  1
        # 176 CALL                     1
        # 186 PRECALL                  2
        # 190 CALL                     2
        # 200 STORE_FAST               3 (spec)
        # 1098         202 LOAD_FAST                3 (spec)
        # 204 POP_JUMP_FORWARD_IF_NONE     7 (to 220)
        # 206 LOAD_FAST                3 (spec)
        # 208 LOAD_ATTR                8 (loader)
        # 218 POP_JUMP_FORWARD_IF_NOT_NONE    21 (to 262)
        # 1099     >>  220 LOAD_GLOBAL             19 (NULL + ImportError)
        # 232 LOAD_CONST               3 ("Can't find module ")
        # 234 LOAD_FAST                1 (modname)
        # 236 FORMAT_VALUE             0
        # 238 LOAD_CONST               4 (' at location ')
        # 240 LOAD_FAST                0 (self)
        # 242 FORMAT_VALUE             1 (str)
        # 244 BUILD_STRING             4
        # 246 PRECALL                  1
        # 250 CALL                     1
        # 260 RAISE_VARARGS            1
        # 1100     >>  262 LOAD_GLOBAL              8 (importlib)
        # 274 LOAD_ATTR                5 (util)
        # 284 LOAD_METHOD             10 (module_from_spec)
        # 306 LOAD_FAST                3 (spec)
        # 308 PRECALL                  1
        # 312 CALL                     1
        # 322 STORE_FAST               4 (mod)
        # 1101         324 LOAD_FAST                3 (spec)
        # 326 LOAD_ATTR                8 (loader)
        # 336 LOAD_METHOD             11 (exec_module)
        # 358 LOAD_FAST                4 (mod)
        # 360 PRECALL                  1
        # 364 CALL                     1
        # 374 POP_TOP
        # 1102         376 LOAD_FAST                4 (mod)
        # 378 RETURN_VALUE
        # 1104     >>  380 LOAD_CONST               2 (None)
        # 382 STORE_FAST               5 (pkgpath)
        # 1105         384 LOAD_FAST                1 (modname)
        # 386 EXTENDED_ARG             1
        # 388 POP_JUMP_FORWARD_IF_NOT_NONE   478 (to 1346)
        # 1106         390 LOAD_FAST                0 (self)
        # 392 LOAD_METHOD             12 (pypkgpath)
        # 414 PRECALL                  0
        # 418 CALL                     0
        # 428 STORE_FAST               5 (pkgpath)
        # 1107         430 LOAD_FAST                5 (pkgpath)
        # 432 POP_JUMP_FORWARD_IF_NONE   139 (to 712)
        # 1108         434 LOAD_FAST                5 (pkgpath)
        # 436 LOAD_METHOD             13 (dirpath)
        # 458 PRECALL                  0
        # 462 CALL                     0
        # 472 STORE_FAST               6 (pkgroot)
        # 1109         474 LOAD_FAST                0 (self)
        # 476 LOAD_METHOD             14 (new)
        # 498 LOAD_CONST               5 ('')
        # 500 KW_NAMES                 6
        # 502 PRECALL                  1
        # 506 CALL                     1
        # 516 LOAD_METHOD             15 (relto)
        # 538 LOAD_FAST                6 (pkgroot)
        # 540 PRECALL                  1
        # 544 CALL                     1
        # 554 LOAD_METHOD             16 (split)
        # 576 LOAD_FAST                0 (self)
        # 578 LOAD_ATTR               17 (sep)
        # 588 PRECALL                  1
        # 592 CALL                     1
        # 602 STORE_FAST               7 (names)
        # 1110         604 LOAD_FAST                7 (names)
        # 606 LOAD_CONST               7 (-1)
        # 608 BINARY_SUBSCR
        # 618 LOAD_CONST               8 ('__init__')
        # 620 COMPARE_OP               2 (==)
        # 626 POP_JUMP_FORWARD_IF_FALSE    20 (to 668)
        # 1111         628 LOAD_FAST                7 (names)
        # 630 LOAD_METHOD             18 (pop)
        # 652 PRECALL                  0
        # 656 CALL                     0
        # 666 POP_TOP
        # 1112     >>  668 LOAD_CONST               9 ('.')
        # 670 LOAD_METHOD             19 (join)
        # 692 LOAD_FAST                7 (names)
        # 694 PRECALL                  1
        # 698 CALL                     1
        # 708 STORE_FAST               1 (modname)
        # 710 JUMP_FORWARD            27 (to 766)
        # 1114     >>  712 LOAD_FAST                0 (self)
        # 714 LOAD_METHOD             13 (dirpath)
        # 736 PRECALL                  0
        # 740 CALL                     0
        # 750 STORE_FAST               6 (pkgroot)
        # 1115         752 LOAD_FAST                0 (self)
        # 754 LOAD_ATTR                3 (purebasename)
        # 764 STORE_FAST               1 (modname)
        # 1117     >>  766 LOAD_FAST                0 (self)
        # 768 LOAD_METHOD             20 (_ensuresyspath)
        # 790 LOAD_FAST                2 (ensuresyspath)
        # 792 LOAD_FAST                6 (pkgroot)
        # 794 PRECALL                  2
        # 798 CALL                     2
        # 808 POP_TOP
        # 1118         810 LOAD_GLOBAL             43 (NULL + __import__)
        # 822 LOAD_FAST                1 (modname)
        # 824 PRECALL                  1
        # 828 CALL                     1
        # 838 POP_TOP
        # 1119         840 LOAD_GLOBAL             44 (sys)
        # 852 LOAD_ATTR               23 (modules)
        # 862 LOAD_FAST                1 (modname)
        # 864 BINARY_SUBSCR
        # 874 STORE_FAST               4 (mod)
        # 1120         876 LOAD_FAST                0 (self)
        # 878 LOAD_ATTR               24 (basename)
        # 888 LOAD_CONST              10 ('__init__.py')
        # 890 COMPARE_OP               2 (==)
        # 896 POP_JUMP_FORWARD_IF_FALSE     2 (to 902)
        # 1121         898 LOAD_FAST                4 (mod)
        # 900 RETURN_VALUE
        # 1123     >>  902 LOAD_FAST                4 (mod)
        # 904 LOAD_ATTR               25 (__file__)
        # 914 STORE_FAST               8 (modfile)
        # 1124         916 LOAD_FAST                8 (modfile)
        # 918 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 924)
        # 920 LOAD_ASSERTION_ERROR
        # 922 RAISE_VARARGS            1
        # 1125     >>  924 LOAD_FAST                8 (modfile)
        # 926 LOAD_CONST              11 (-4)
        # 928 LOAD_CONST               2 (None)
        # 930 BUILD_SLICE              2
        # 932 BINARY_SUBSCR
        # 942 LOAD_CONST              12 (('.pyc', '.pyo'))
        # 944 CONTAINS_OP              0
        # 946 POP_JUMP_FORWARD_IF_FALSE    11 (to 970)
        # 1126         948 LOAD_FAST                8 (modfile)
        # 950 LOAD_CONST               2 (None)
        # 952 LOAD_CONST               7 (-1)
        # 954 BUILD_SLICE              2
        # 956 BINARY_SUBSCR
        # 966 STORE_FAST               8 (modfile)
        # 968 JUMP_FORWARD            34 (to 1038)
        # 1127     >>  970 LOAD_FAST                8 (modfile)
        # 972 LOAD_METHOD             26 (endswith)
        # 994 LOAD_CONST              13 ('$py.class')
        # 996 PRECALL                  1
        # 1000 CALL                     1
        # 1010 POP_JUMP_FORWARD_IF_FALSE    13 (to 1038)
        # 1128        1012 LOAD_FAST                8 (modfile)
        # 1014 LOAD_CONST               2 (None)
        # 1016 LOAD_CONST              14 (-9)
        # 1018 BUILD_SLICE              2
        # 1020 BINARY_SUBSCR
        # 1030 LOAD_CONST              15 ('.py')
        # 1032 BINARY_OP                0 (+)
        # 1036 STORE_FAST               8 (modfile)
        # 1129     >> 1038 LOAD_FAST                8 (modfile)
        # 1040 LOAD_METHOD             26 (endswith)
        # 1062 LOAD_GLOBAL             54 (os)
        # 1074 LOAD_ATTR               17 (sep)
        # 1084 LOAD_CONST              10 ('__init__.py')
        # 1086 BINARY_OP                0 (+)
        # 1090 PRECALL                  1
        # 1094 CALL                     1
        # 1104 POP_JUMP_FORWARD_IF_FALSE    21 (to 1148)
        # 1130        1106 LOAD_FAST                0 (self)
        # 1108 LOAD_ATTR               24 (basename)
        # 1118 LOAD_CONST              10 ('__init__.py')
        # 1120 COMPARE_OP               3 (!=)
        # 1126 POP_JUMP_FORWARD_IF_FALSE    10 (to 1148)
        # 1131        1128 LOAD_FAST                8 (modfile)
        # 1130 LOAD_CONST               2 (None)
        # 1132 LOAD_CONST              16 (-12)
        # 1134 BUILD_SLICE              2
        # 1136 BINARY_SUBSCR
        # 1146 STORE_FAST               8 (modfile)
        # 1132     >> 1148 NOP
        # 1133        1150 LOAD_FAST                0 (self)
        # 1152 LOAD_METHOD             28 (samefile)
        # 1174 LOAD_FAST                8 (modfile)
        # 1176 PRECALL                  1
        # 1180 CALL                     1
        # 1190 STORE_FAST               9 (issame)
        # 1192 JUMP_FORWARD            23 (to 1240)
        # >> 1194 PUSH_EXC_INFO
        # 1134        1196 LOAD_GLOBAL              2 (error)
        # 1208 LOAD_ATTR                2 (ENOENT)
        # 1218 CHECK_EXC_MATCH
        # 1220 POP_JUMP_FORWARD_IF_FALSE     5 (to 1232)
        # 1222 POP_TOP
        # 1135        1224 LOAD_CONST              17 (False)
        # 1226 STORE_FAST               9 (issame)
        # 1228 POP_EXCEPT
        # 1230 JUMP_FORWARD             4 (to 1240)
        # 1134     >> 1232 RERAISE                  0
        # >> 1234 COPY                     3
        # 1236 POP_EXCEPT
        # 1238 RERAISE                  1
        # 1136     >> 1240 LOAD_FAST                9 (issame)
        # 1242 POP_JUMP_FORWARD_IF_TRUE    49 (to 1342)
        # 1137        1244 LOAD_GLOBAL             55 (NULL + os)
        # 1256 LOAD_ATTR               29 (getenv)
        # 1266 LOAD_CONST              18 ('PY_IGNORE_IMPORTMISMATCH')
        # 1268 PRECALL                  1
        # 1272 CALL                     1
        # 1282 STORE_FAST              10 (ignore)
        # 1138        1284 LOAD_FAST               10 (ignore)
        # 1286 LOAD_CONST              19 ('1')
        # 1288 COMPARE_OP               3 (!=)
        # 1294 POP_JUMP_FORWARD_IF_FALSE    23 (to 1342)
        # 1139        1296 LOAD_FAST                0 (self)
        # 1298 LOAD_METHOD             30 (ImportMismatchError)
        # 1320 LOAD_FAST                1 (modname)
        # 1322 LOAD_FAST                8 (modfile)
        # 1324 LOAD_FAST                0 (self)
        # 1326 PRECALL                  3
        # 1330 CALL                     3
        # 1340 RAISE_VARARGS            1
        # 1140     >> 1342 LOAD_FAST                4 (mod)
        # 1344 RETURN_VALUE
        # 1142     >> 1346 NOP
        # 1143        1348 LOAD_GLOBAL             44 (sys)
        # 1360 LOAD_ATTR               23 (modules)
        # 1370 LOAD_FAST                1 (modname)
        # 1372 BINARY_SUBSCR
        # 1382 RETURN_VALUE
        # >> 1384 PUSH_EXC_INFO
        # 1144        1386 LOAD_GLOBAL             62 (KeyError)
        # 1398 CHECK_EXC_MATCH
        # 1400 POP_JUMP_FORWARD_IF_FALSE   187 (to 1776)
        # 1402 POP_TOP
        # 1146        1404 LOAD_CONST              20 (0)
        # 1406 LOAD_CONST               2 (None)
        # 1408 IMPORT_NAME             32 (types)
        # 1410 STORE_FAST              11 (types)
        # 1148        1412 LOAD_FAST               11 (types)
        # 1414 LOAD_METHOD             33 (ModuleType)
        # 1436 LOAD_FAST                1 (modname)
        # 1438 PRECALL                  1
        # 1442 CALL                     1
        # 1452 STORE_FAST               4 (mod)
        # 1149        1454 LOAD_GLOBAL             15 (NULL + str)
        # 1466 LOAD_FAST                0 (self)
        # 1468 PRECALL                  1
        # 1472 CALL                     1
        # 1482 LOAD_FAST                4 (mod)
        # 1484 STORE_ATTR              25 (__file__)
        # 1150        1494 LOAD_FAST                4 (mod)
        # 1496 LOAD_GLOBAL             44 (sys)
        # 1508 LOAD_ATTR               23 (modules)
        # 1518 LOAD_FAST                1 (modname)
        # 1520 STORE_SUBSCR
        # 1151        1524 NOP
        # 1152        1526 LOAD_GLOBAL             69 (NULL + open)
        # 1538 LOAD_GLOBAL             15 (NULL + str)
        # 1550 LOAD_FAST                0 (self)
        # 1552 PRECALL                  1
        # 1556 CALL                     1
        # 1566 LOAD_CONST              21 ('rb')
        # 1568 PRECALL                  2
        # 1572 CALL                     2
        # 1582 BEFORE_WITH
        # 1584 STORE_FAST              12 (f)
        # 1153        1586 LOAD_GLOBAL             71 (NULL + exec)
        # 1598 LOAD_FAST               12 (f)
        # 1600 LOAD_METHOD             36 (read)
        # 1622 PRECALL                  0
        # 1626 CALL                     0
        # 1636 LOAD_FAST                4 (mod)
        # 1638 LOAD_ATTR               37 (__dict__)
        # 1648 PRECALL                  2
        # 1652 CALL                     2
        # 1662 POP_TOP
        # 1152        1664 LOAD_CONST               2 (None)
        # 1666 LOAD_CONST               2 (None)
        # 1668 LOAD_CONST               2 (None)
        # 1670 PRECALL                  2
        # 1674 CALL                     2
        # 1684 POP_TOP
        # 1686 JUMP_FORWARD            11 (to 1710)
        # >> 1688 PUSH_EXC_INFO
        # 1690 WITH_EXCEPT_START
        # 1692 POP_JUMP_FORWARD_IF_TRUE     4 (to 1702)
        # 1694 RERAISE                  2
        # >> 1696 COPY                     3
        # 1698 POP_EXCEPT
        # 1700 RERAISE                  1
        # >> 1702 POP_TOP
        # 1704 POP_EXCEPT
        # 1706 POP_TOP
        # 1708 POP_TOP
        # >> 1710 JUMP_FORWARD            28 (to 1768)
        # >> 1712 PUSH_EXC_INFO
        # 1154        1714 LOAD_GLOBAL             76 (BaseException)
        # 1726 CHECK_EXC_MATCH
        # 1728 POP_JUMP_FORWARD_IF_FALSE    15 (to 1760)
        # 1730 POP_TOP
        # 1155        1732 LOAD_GLOBAL             44 (sys)
        # 1744 LOAD_ATTR               23 (modules)
        # 1754 LOAD_FAST                1 (modname)
        # 1756 DELETE_SUBSCR
        # 1156        1758 RAISE_VARARGS            0
        # 1154     >> 1760 RERAISE                  0
        # >> 1762 COPY                     3
        # 1764 POP_EXCEPT
        # 1766 RERAISE                  1
        # 1157     >> 1768 LOAD_FAST                4 (mod)
        # 1770 SWAP                     2
        # 1772 POP_EXCEPT
        # 1774 RETURN_VALUE
        # 1144     >> 1776 RERAISE                  0
        # >> 1778 COPY                     3
        # 1780 POP_EXCEPT
        # 1782 RERAISE                  1
        # ExceptionTable:
        # 1150 to 1190 -> 1194 [0]
        # 1194 to 1226 -> 1234 [1] lasti
        # 1232 to 1232 -> 1234 [1] lasti
        # 1348 to 1380 -> 1384 [0]
        # 1384 to 1522 -> 1778 [1] lasti
        # 1526 to 1582 -> 1712 [1]
        # 1584 to 1662 -> 1688 [2] lasti
        # 1664 to 1686 -> 1712 [1]
        # 1688 to 1694 -> 1696 [4] lasti
        # 1696 to 1700 -> 1712 [1]
        # 1702 to 1702 -> 1696 [4] lasti
        # 1704 to 1708 -> 1712 [1]
        # 1710 to 1710 -> 1778 [1] lasti
        # 1712 to 1760 -> 1762 [2] lasti
        # 1762 to 1770 -> 1778 [1] lasti
        # 1776 to 1776 -> 1778 [1] lasti

    def sysexec(self):
        """Return stdout text from executing a system child process,
        where the 'self' path points to executable.
        The process is directly invoked and not through a system shell.
        """
        # 1159           0 RESUME                   0
        # 1164           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (('PIPE',))
        # 6 IMPORT_NAME              0 (subprocess)
        # 8 IMPORT_FROM              1 (PIPE)
        # 10 STORE_FAST               3 (PIPE)
        # 12 POP_TOP
        # 1165          14 LOAD_CONST               1 (0)
        # 16 LOAD_CONST               3 (('Popen',))
        # 18 IMPORT_NAME              0 (subprocess)
        # 20 IMPORT_FROM              2 (Popen)
        # 22 STORE_FAST               4 (Popen)
        # 24 POP_TOP
        # 1167          26 LOAD_FAST                2 (popen_opts)
        # 28 LOAD_METHOD              3 (pop)
        # 50 LOAD_CONST               4 ('stdout')
        # 52 LOAD_CONST               5 (None)
        # 54 PRECALL                  2
        # 58 CALL                     2
        # 68 POP_TOP
        # 1168          70 LOAD_FAST                2 (popen_opts)
        # 72 LOAD_METHOD              3 (pop)
        # 94 LOAD_CONST               6 ('stderr')
        # 96 LOAD_CONST               5 (None)
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 POP_TOP
        # 1169         114 PUSH_NULL
        # 116 LOAD_FAST                4 (Popen)
        # 1170         118 LOAD_GLOBAL              9 (NULL + str)
        # 130 LOAD_FAST                0 (self)
        # 132 PRECALL                  1
        # 136 CALL                     1
        # 146 BUILD_LIST               1
        # 148 LOAD_CONST               7 (<code object <listcomp> at 0x000001EBD7F2A3D0, file "_pytest\_py\path.py", line 1170>)
        # 150 MAKE_FUNCTION            0
        # 152 LOAD_FAST                1 (argv)
        # 154 GET_ITER
        # 156 PRECALL                  0
        # 160 CALL                     0
        # 170 BINARY_OP                0 (+)
        # 1169         174 BUILD_TUPLE              1
        # 176 BUILD_MAP                0
        # 1171         178 LOAD_FAST                2 (popen_opts)
        # 1169         180 DICT_MERGE               1
        # 1172         182 LOAD_FAST                3 (PIPE)
        # 1173         184 LOAD_FAST                3 (PIPE)
        # 1169         186 LOAD_CONST               8 (('stdout', 'stderr'))
        # 188 BUILD_CONST_KEY_MAP      2
        # 190 DICT_MERGE               1
        # 192 CALL_FUNCTION_EX         1
        # 194 STORE_FAST               5 (proc)
        # 1176         196 LOAD_FAST                5 (proc)
        # 198 LOAD_METHOD              5 (communicate)
        # 220 PRECALL                  0
        # 224 CALL                     0
        # 234 UNPACK_SEQUENCE          2
        # 238 STORE_FAST               6 (stdout)
        # 240 STORE_FAST               7 (stderr)
        # 1177         242 LOAD_FAST                5 (proc)
        # 244 LOAD_METHOD              6 (wait)
        # 266 PRECALL                  0
        # 270 CALL                     0
        # 280 STORE_FAST               8 (ret)
        # 1178         282 LOAD_GLOBAL             15 (NULL + isinstance)
        # 294 LOAD_FAST                6 (stdout)
        # 296 LOAD_GLOBAL             16 (bytes)
        # 308 PRECALL                  2
        # 312 CALL                     2
        # 322 POP_JUMP_FORWARD_IF_FALSE    38 (to 400)
        # 1179         324 LOAD_FAST                6 (stdout)
        # 326 LOAD_METHOD              9 (decode)
        # 348 LOAD_GLOBAL             21 (NULL + sys)
        # 360 LOAD_ATTR               11 (getdefaultencoding)
        # 370 PRECALL                  0
        # 374 CALL                     0
        # 384 PRECALL                  1
        # 388 CALL                     1
        # 398 STORE_FAST               6 (stdout)
        # 1180     >>  400 LOAD_FAST                8 (ret)
        # 402 LOAD_CONST               1 (0)
        # 404 COMPARE_OP               3 (!=)
        # 410 POP_JUMP_FORWARD_IF_FALSE    91 (to 594)
        # 1181         412 LOAD_GLOBAL             15 (NULL + isinstance)
        # 424 LOAD_FAST                7 (stderr)
        # 426 LOAD_GLOBAL             16 (bytes)
        # 438 PRECALL                  2
        # 442 CALL                     2
        # 452 POP_JUMP_FORWARD_IF_FALSE    38 (to 530)
        # 1182         454 LOAD_FAST                7 (stderr)
        # 456 LOAD_METHOD              9 (decode)
        # 478 LOAD_GLOBAL             21 (NULL + sys)
        # 490 LOAD_ATTR               11 (getdefaultencoding)
        # 500 PRECALL                  0
        # 504 CALL                     0
        # 514 PRECALL                  1
        # 518 CALL                     1
        # 528 STORE_FAST               7 (stderr)
        # 1183     >>  530 LOAD_GLOBAL             25 (NULL + RuntimeError)
        # 1184         542 LOAD_FAST                8 (ret)
        # 1185         544 LOAD_FAST                8 (ret)
        # 1186         546 LOAD_GLOBAL              9 (NULL + str)
        # 558 LOAD_FAST                0 (self)
        # 560 PRECALL                  1
        # 564 CALL                     1
        # 1187         574 LOAD_FAST                6 (stdout)
        # 1188         576 LOAD_FAST                7 (stderr)
        # 1183         578 PRECALL                  5
        # 582 CALL                     5
        # 592 RAISE_VARARGS            1
        # 1190     >>  594 LOAD_FAST                6 (stdout)
        # 596 RETURN_VALUE
        # Disassembly of <code object <listcomp> at 0x000001EBD7F2A3D0, file "_pytest\_py\path.py", line 1170>:
        # 1170           0 RESUME                   0
        # 2 BUILD_LIST               0
        # 4 LOAD_FAST                0 (.0)
        # >>    6 FOR_ITER                17 (to 42)
        # 8 STORE_FAST               1 (arg)
        # 10 LOAD_GLOBAL              1 (NULL + str)
        # 22 LOAD_FAST                1 (arg)
        # 24 PRECALL                  1
        # 28 CALL                     1
        # 38 LIST_APPEND              2
        # 40 JUMP_BACKWARD           18 (to 6)
        # >>   42 RETURN_VALUE

    def sysfind(cls, name, checker, paths):
        """Return a path object found by looking at the systems
        underlying PATH specification. If the checker is not None
        it will be invoked to filter matching paths.  If a binary
        cannot be found, None is returned
        Note: This is probably not working on plain win32 systems
        but may work on cygwin.
        """
        # 0 MAKE_CELL                8 (systemroot)
        # 1192           2 RESUME                   0
        # 1201           4 LOAD_GLOBAL              1 (NULL + isabs)
        # 16 LOAD_FAST                1 (name)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 POP_JUMP_FORWARD_IF_FALSE    41 (to 116)
        # 1202          34 LOAD_GLOBAL              3 (NULL + local)
        # 46 LOAD_FAST                1 (name)
        # 48 PRECALL                  1
        # 52 CALL                     1
        # 62 STORE_FAST               4 (p)
        # 1203          64 LOAD_FAST                4 (p)
        # 66 LOAD_METHOD              2 (check)
        # 88 LOAD_CONST               1 (1)
        # 90 KW_NAMES                 2
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 POP_JUMP_FORWARD_IF_FALSE     2 (to 112)
        # 1204         108 LOAD_FAST                4 (p)
        # 110 RETURN_VALUE
        # 1203     >>  112 EXTENDED_ARG             1
        # 114 JUMP_FORWARD           355 (to 826)
        # 1206     >>  116 LOAD_FAST                3 (paths)
        # 118 POP_JUMP_FORWARD_IF_NOT_NONE   160 (to 440)
        # 1207         120 LOAD_GLOBAL              6 (iswin32)
        # 132 POP_JUMP_FORWARD_IF_FALSE   116 (to 366)
        # 1208         134 LOAD_GLOBAL              8 (os)
        # 146 LOAD_ATTR                5 (environ)
        # 156 LOAD_CONST               4 ('Path')
        # 158 BINARY_SUBSCR
        # 168 LOAD_METHOD              6 (split)
        # 190 LOAD_CONST               5 (';')
        # 192 PRECALL                  1
        # 196 CALL                     1
        # 206 STORE_FAST               3 (paths)
        # 1209         208 LOAD_CONST               6 ('')
        # 210 LOAD_FAST                3 (paths)
        # 212 CONTAINS_OP              1
        # 214 POP_JUMP_FORWARD_IF_FALSE    25 (to 266)
        # 216 LOAD_CONST               7 ('.')
        # 218 LOAD_FAST                3 (paths)
        # 220 CONTAINS_OP              1
        # 222 POP_JUMP_FORWARD_IF_FALSE    21 (to 266)
        # 1210         224 LOAD_FAST                3 (paths)
        # 226 LOAD_METHOD              7 (append)
        # 248 LOAD_CONST               7 ('.')
        # 250 PRECALL                  1
        # 254 CALL                     1
        # 264 POP_TOP
        # 1211     >>  266 NOP
        # 1212         268 LOAD_GLOBAL              8 (os)
        # 280 LOAD_ATTR                5 (environ)
        # 290 LOAD_CONST               8 ('SYSTEMROOT')
        # 292 BINARY_SUBSCR
        # 302 STORE_DEREF              8 (systemroot)
        # 1216         304 LOAD_CLOSURE             8 (systemroot)
        # 306 BUILD_TUPLE              1
        # 308 LOAD_CONST               9 (<code object <listcomp> at 0x000001EBD7DF3C30, file "_pytest\_py\path.py", line 1216>)
        # 310 MAKE_FUNCTION            8 (closure)
        # 1217         312 LOAD_FAST                3 (paths)
        # 1216         314 GET_ITER
        # 316 PRECALL                  0
        # 320 CALL                     0
        # 330 STORE_FAST               3 (paths)
        # 332 JUMP_FORWARD            53 (to 440)
        # >>  334 PUSH_EXC_INFO
        # 1213         336 LOAD_GLOBAL             16 (KeyError)
        # 348 CHECK_EXC_MATCH
        # 350 POP_JUMP_FORWARD_IF_FALSE     3 (to 358)
        # 352 POP_TOP
        # 1214         354 POP_EXCEPT
        # 356 JUMP_FORWARD            41 (to 440)
        # 1213     >>  358 RERAISE                  0
        # >>  360 COPY                     3
        # 362 POP_EXCEPT
        # 364 RERAISE                  1
        # 1220     >>  366 LOAD_GLOBAL              8 (os)
        # 378 LOAD_ATTR                5 (environ)
        # 388 LOAD_CONST              10 ('PATH')
        # 390 BINARY_SUBSCR
        # 400 LOAD_METHOD              6 (split)
        # 422 LOAD_CONST              11 (':')
        # 424 PRECALL                  1
        # 428 CALL                     1
        # 438 STORE_FAST               3 (paths)
        # 1221     >>  440 BUILD_LIST               0
        # 442 STORE_FAST               5 (tryadd)
        # 1222         444 LOAD_GLOBAL              6 (iswin32)
        # 456 POP_JUMP_FORWARD_IF_FALSE    50 (to 558)
        # 1223         458 LOAD_FAST                5 (tryadd)
        # 460 LOAD_GLOBAL              8 (os)
        # 472 LOAD_ATTR                5 (environ)
        # 482 LOAD_CONST              12 ('PATHEXT')
        # 484 BINARY_SUBSCR
        # 494 LOAD_METHOD              6 (split)
        # 516 LOAD_GLOBAL              8 (os)
        # 528 LOAD_ATTR                9 (pathsep)
        # 538 PRECALL                  1
        # 542 CALL                     1
        # 552 BINARY_OP               13 (+=)
        # 556 STORE_FAST               5 (tryadd)
        # 1224     >>  558 LOAD_FAST                5 (tryadd)
        # 560 LOAD_METHOD              7 (append)
        # 582 LOAD_CONST               6 ('')
        # 584 PRECALL                  1
        # 588 CALL                     1
        # 598 POP_TOP
        # 1226         600 LOAD_FAST                3 (paths)
        # 602 GET_ITER
        # >>  604 FOR_ITER               110 (to 826)
        # 606 STORE_FAST               6 (x)
        # 1227         608 LOAD_FAST                5 (tryadd)
        # 610 GET_ITER
        # >>  612 FOR_ITER               105 (to 824)
        # 614 STORE_FAST               7 (addext)
        # 1228         616 LOAD_GLOBAL              3 (NULL + local)
        # 628 LOAD_FAST                6 (x)
        # 630 PRECALL                  1
        # 634 CALL                     1
        # 644 LOAD_METHOD             10 (join)
        # 666 LOAD_FAST                1 (name)
        # 668 LOAD_CONST              13 (True)
        # 670 KW_NAMES                14
        # 672 PRECALL                  2
        # 676 CALL                     2
        # 686 LOAD_FAST                7 (addext)
        # 688 BINARY_OP                0 (+)
        # 692 STORE_FAST               4 (p)
        # 1229         694 NOP
        # 1230         696 LOAD_FAST                4 (p)
        # 698 LOAD_METHOD              2 (check)
        # 720 LOAD_CONST               1 (1)
        # 722 KW_NAMES                 2
        # 724 PRECALL                  1
        # 728 CALL                     1
        # 738 POP_JUMP_FORWARD_IF_FALSE    20 (to 780)
        # 1231         740 LOAD_FAST                2 (checker)
        # 742 POP_JUMP_FORWARD_IF_FALSE    12 (to 768)
        # 1232         744 PUSH_NULL
        # 746 LOAD_FAST                2 (checker)
        # 748 LOAD_FAST                4 (p)
        # 750 PRECALL                  1
        # 754 CALL                     1
        # 764 POP_JUMP_FORWARD_IF_TRUE     1 (to 768)
        # 1233         766 JUMP_BACKWARD           78 (to 612)
        # 1234     >>  768 LOAD_FAST                4 (p)
        # 770 SWAP                     2
        # 772 POP_TOP
        # 774 SWAP                     2
        # 776 POP_TOP
        # 778 RETURN_VALUE
        # 1230     >>  780 JUMP_BACKWARD           85 (to 612)
        # >>  782 PUSH_EXC_INFO
        # 1235         784 LOAD_GLOBAL             22 (error)
        # 796 LOAD_ATTR               12 (EACCES)
        # 806 CHECK_EXC_MATCH
        # 808 POP_JUMP_FORWARD_IF_FALSE     3 (to 816)
        # 810 POP_TOP
        # 1236         812 POP_EXCEPT
        # 814 JUMP_BACKWARD          102 (to 612)
        # 1235     >>  816 RERAISE                  0
        # >>  818 COPY                     3
        # 820 POP_EXCEPT
        # 822 RERAISE                  1
        # 1227     >>  824 JUMP_BACKWARD          111 (to 604)
        # 1237     >>  826 LOAD_CONST               3 (None)
        # 828 RETURN_VALUE
        # ExceptionTable:
        # 268 to 302 -> 334 [0]
        # 334 to 352 -> 360 [1] lasti
        # 358 to 358 -> 360 [1] lasti
        # 696 to 764 -> 782 [2]
        # 768 to 768 -> 782 [2]
        # 782 to 810 -> 818 [3] lasti
        # 816 to 816 -> 818 [3] lasti
        # Disassembly of <code object <listcomp> at 0x000001EBD7DF3C30, file "_pytest\_py\path.py", line 1216>:
        # 0 COPY_FREE_VARS           1
        # 1216           2 RESUME                   0
        # 4 BUILD_LIST               0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                24 (to 58)
        # 1217          10 STORE_FAST               1 (path)
        # 12 LOAD_FAST                1 (path)
        # 14 LOAD_METHOD              0 (replace)
        # 36 LOAD_CONST               0 ('%SystemRoot%')
        # 38 LOAD_DEREF               2 (systemroot)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 1216          54 LIST_APPEND              2
        # 56 JUMP_BACKWARD           25 (to 8)
        # >>   58 RETURN_VALUE

    def _gethomedir(cls):
        # 1239           0 RESUME                   0
        # 1241           2 NOP
        # 1242           4 LOAD_GLOBAL              0 (os)
        # 16 LOAD_ATTR                1 (environ)
        # 26 LOAD_CONST               1 ('HOME')
        # 28 BINARY_SUBSCR
        # 38 STORE_FAST               1 (x)
        # 40 JUMP_FORWARD            73 (to 188)
        # >>   42 PUSH_EXC_INFO
        # 1243          44 LOAD_GLOBAL              4 (KeyError)
        # 56 CHECK_EXC_MATCH
        # 58 POP_JUMP_FORWARD_IF_FALSE    60 (to 180)
        # 60 POP_TOP
        # 1244          62 NOP
        # 1245          64 LOAD_GLOBAL              0 (os)
        # 76 LOAD_ATTR                1 (environ)
        # 86 LOAD_CONST               2 ('HOMEDRIVE')
        # 88 BINARY_SUBSCR
        # 98 LOAD_GLOBAL              0 (os)
        # 110 LOAD_ATTR                1 (environ)
        # 120 LOAD_CONST               3 ('HOMEPATH')
        # 122 BINARY_SUBSCR
        # 132 BINARY_OP                0 (+)
        # 136 STORE_FAST               1 (x)
        # 138 JUMP_FORWARD            18 (to 176)
        # >>  140 PUSH_EXC_INFO
        # 1246         142 LOAD_GLOBAL              4 (KeyError)
        # 154 CHECK_EXC_MATCH
        # 156 POP_JUMP_FORWARD_IF_FALSE     5 (to 168)
        # 158 POP_TOP
        # 1247         160 POP_EXCEPT
        # 162 POP_EXCEPT
        # 164 LOAD_CONST               0 (None)
        # 166 RETURN_VALUE
        # 1246     >>  168 RERAISE                  0
        # >>  170 COPY                     3
        # 172 POP_EXCEPT
        # 174 RERAISE                  1
        # 1245     >>  176 POP_EXCEPT
        # 178 JUMP_FORWARD             4 (to 188)
        # 1243     >>  180 RERAISE                  0
        # >>  182 COPY                     3
        # 184 POP_EXCEPT
        # 186 RERAISE                  1
        # 1248     >>  188 PUSH_NULL
        # 190 LOAD_FAST                0 (cls)
        # 192 LOAD_FAST                1 (x)
        # 194 PRECALL                  1
        # 198 CALL                     1
        # 208 RETURN_VALUE
        # ExceptionTable:
        # 4 to 38 -> 42 [0]
        # 42 to 60 -> 182 [1] lasti
        # 64 to 136 -> 140 [1]
        # 138 to 138 -> 182 [1] lasti
        # 140 to 158 -> 170 [2] lasti
        # 160 to 160 -> 182 [1] lasti
        # 168 to 168 -> 170 [2] lasti
        # 170 to 174 -> 182 [1] lasti
        # 180 to 180 -> 182 [1] lasti

    def get_temproot(cls):
        """Return the system's temporary directory
        (where tempfiles are usually created in)
        """
        # 1253           0 RESUME                   0
        # 1258           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (tempfile)
        # 8 STORE_FAST               1 (tempfile)
        # 1260          10 LOAD_GLOBAL              3 (NULL + local)
        # 22 LOAD_FAST                1 (tempfile)
        # 24 LOAD_METHOD              2 (gettempdir)
        # 46 PRECALL                  0
        # 50 CALL                     0
        # 60 PRECALL                  1
        # 64 CALL                     1
        # 74 RETURN_VALUE

    def mkdtemp(cls, rootdir):
        """Return a Path object pointing to a fresh new temporary directory
        (which we created ourselves).
        """
        # 1262           0 RESUME                   0
        # 1267           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (tempfile)
        # 8 STORE_FAST               2 (tempfile)
        # 1269          10 LOAD_FAST                1 (rootdir)
        # 12 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 54)
        # 1270          14 LOAD_FAST                0 (cls)
        # 16 LOAD_METHOD              1 (get_temproot)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 STORE_FAST               1 (rootdir)
        # 1271     >>   54 LOAD_GLOBAL              5 (NULL + error)
        # 66 LOAD_ATTR                3 (checked_call)
        # 76 LOAD_FAST                2 (tempfile)
        # 78 LOAD_ATTR                4 (mkdtemp)
        # 88 LOAD_GLOBAL             11 (NULL + str)
        # 100 LOAD_FAST                1 (rootdir)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # 116 KW_NAMES                 3
        # 118 PRECALL                  2
        # 122 CALL                     2
        # 132 STORE_FAST               3 (path)
        # 1272         134 PUSH_NULL
        # 136 LOAD_FAST                0 (cls)
        # 138 LOAD_FAST                3 (path)
        # 140 PRECALL                  1
        # 144 CALL                     1
        # 154 RETURN_VALUE

    def make_numbered_dir(cls, prefix, rootdir, keep, lock_timeout):
        """Return unique directory with a number greater than the current
        maximum one.  The number is assumed to start directly after prefix.
        if keep is true directories with a number less than (maxnum-keep)
        will be removed. If .lock files are used (lock_timeout non-zero),
        algorithm is multi-process safe.
        """
        # 0 MAKE_CELL               22 (garbage_prefix)
        # 2 MAKE_CELL               23 (nprefix)
        # 1274           4 RESUME                   0
        # 1284           6 LOAD_FAST                2 (rootdir)
        # 8 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 50)
        # 1285          10 LOAD_FAST                0 (cls)
        # 12 LOAD_METHOD              0 (get_temproot)
        # 34 PRECALL                  0
        # 38 CALL                     0
        # 48 STORE_FAST               2 (rootdir)
        # 1287     >>   50 LOAD_FAST                1 (prefix)
        # 52 LOAD_METHOD              1 (lower)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 88 STORE_DEREF             23 (nprefix)
        # 1289          90 LOAD_CLOSURE            23 (nprefix)
        # 92 BUILD_TUPLE              1
        # 94 LOAD_CONST               2 (<code object parse_num at 0x000001EBD77CAF10, file "_pytest\_py\path.py", line 1289>)
        # 96 MAKE_FUNCTION            8 (closure)
        # 98 STORE_FAST               5 (parse_num)
        # 1298         100 LOAD_CONST               3 (<code object create_lockfile at 0x000001EBD765B330, file "_pytest\_py\path.py", line 1298>)
        # 102 MAKE_FUNCTION            0
        # 104 STORE_FAST               6 (create_lockfile)
        # 1312         106 LOAD_CONST               4 (<code object atexit_remove_lockfile at 0x000001EBD7E48DB0, file "_pytest\_py\path.py", line 1312>)
        # 108 MAKE_FUNCTION            0
        # 110 STORE_FAST               7 (atexit_remove_lockfile)
        # 1332         112 LOAD_CONST               1 (None)
        # 114 STORE_FAST               8 (lastmax)
        # 1333     >>  116 NOP
        # 1334         118 LOAD_CONST               6 (-1)
        # 120 STORE_FAST               9 (maxnum)
        # 1335         122 LOAD_FAST                2 (rootdir)
        # 124 LOAD_METHOD              2 (listdir)
        # 146 PRECALL                  0
        # 150 CALL                     0
        # 160 GET_ITER
        # >>  162 FOR_ITER                31 (to 226)
        # 164 STORE_FAST              10 (path)
        # 1336         166 PUSH_NULL
        # 168 LOAD_FAST                5 (parse_num)
        # 170 LOAD_FAST               10 (path)
        # 172 PRECALL                  1
        # 176 CALL                     1
        # 186 STORE_FAST              11 (num)
        # 1337         188 LOAD_FAST               11 (num)
        # 190 POP_JUMP_FORWARD_IF_NONE    16 (to 224)
        # 1338         192 LOAD_GLOBAL              7 (NULL + max)
        # 204 LOAD_FAST                9 (maxnum)
        # 206 LOAD_FAST               11 (num)
        # 208 PRECALL                  2
        # 212 CALL                     2
        # 222 STORE_FAST               9 (maxnum)
        # >>  224 JUMP_BACKWARD           32 (to 162)
        # 1341     >>  226 NOP
        # 1342         228 LOAD_FAST                2 (rootdir)
        # 230 LOAD_METHOD              4 (mkdir)
        # 252 LOAD_FAST                1 (prefix)
        # 254 LOAD_GLOBAL             11 (NULL + str)
        # 266 LOAD_FAST                9 (maxnum)
        # 268 LOAD_CONST               7 (1)
        # 270 BINARY_OP                0 (+)
        # 274 PRECALL                  1
        # 278 CALL                     1
        # 288 BINARY_OP                0 (+)
        # 292 PRECALL                  1
        # 296 CALL                     1
        # 306 STORE_FAST              12 (udir)
        # 1343         308 LOAD_FAST                4 (lock_timeout)
        # 310 POP_JUMP_FORWARD_IF_FALSE    22 (to 356)
        # 1344         312 PUSH_NULL
        # 314 LOAD_FAST                6 (create_lockfile)
        # 316 LOAD_FAST               12 (udir)
        # 318 PRECALL                  1
        # 322 CALL                     1
        # 332 STORE_FAST              13 (lockfile)
        # 1345         334 PUSH_NULL
        # 336 LOAD_FAST                7 (atexit_remove_lockfile)
        # 338 LOAD_FAST               13 (lockfile)
        # 340 PRECALL                  1
        # 344 CALL                     1
        # 354 POP_TOP
        # >>  356 JUMP_FORWARD            53 (to 464)
        # >>  358 PUSH_EXC_INFO
        # 1346         360 LOAD_GLOBAL             12 (error)
        # 372 LOAD_ATTR                7 (EEXIST)
        # 382 LOAD_GLOBAL             12 (error)
        # 394 LOAD_ATTR                8 (ENOENT)
        # 404 LOAD_GLOBAL             12 (error)
        # 416 LOAD_ATTR                9 (EBUSY)
        # 426 BUILD_TUPLE              3
        # 428 CHECK_EXC_MATCH
        # 430 POP_JUMP_FORWARD_IF_FALSE    12 (to 456)
        # 432 POP_TOP
        # 1355         434 LOAD_FAST                8 (lastmax)
        # 436 LOAD_FAST                9 (maxnum)
        # 438 COMPARE_OP               2 (==)
        # 444 POP_JUMP_FORWARD_IF_FALSE     1 (to 448)
        # 1356         446 RAISE_VARARGS            0
        # 1357     >>  448 LOAD_FAST                9 (maxnum)
        # 450 STORE_FAST               8 (lastmax)
        # 1358         452 POP_EXCEPT
        # 454 JUMP_BACKWARD          170 (to 116)
        # 1346     >>  456 RERAISE                  0
        # >>  458 COPY                     3
        # 460 POP_EXCEPT
        # 462 RERAISE                  1
        # 1359     >>  464 NOP
        # 1361         466 LOAD_CONST               8 (<code object get_mtime at 0x000001EBD7E48ED0, file "_pytest\_py\path.py", line 1361>)
        # 468 MAKE_FUNCTION            0
        # 470 STORE_FAST              14 (get_mtime)
        # 1368         472 LOAD_FAST                1 (prefix)
        # 474 LOAD_CONST               9 ('garbage-')
        # 476 BINARY_OP                0 (+)
        # 480 STORE_DEREF             22 (garbage_prefix)
        # 1370         482 LOAD_CLOSURE            22 (garbage_prefix)
        # 484 BUILD_TUPLE              1
        # 486 LOAD_CONST              10 (<code object is_garbage at 0x000001EBD7DF2D30, file "_pytest\_py\path.py", line 1370>)
        # 488 MAKE_FUNCTION            8 (closure)
        # 490 STORE_FAST              15 (is_garbage)
        # 1376         492 PUSH_NULL
        # 494 LOAD_FAST               14 (get_mtime)
        # 496 LOAD_FAST               12 (udir)
        # 498 PRECALL                  1
        # 502 CALL                     1
        # 512 STORE_FAST              16 (udir_time)
        # 1377         514 LOAD_FAST                3 (keep)
        # 516 EXTENDED_ARG             1
        # 518 POP_JUMP_FORWARD_IF_FALSE   336 (to 1192)
        # 520 LOAD_FAST               16 (udir_time)
        # 522 EXTENDED_ARG             1
        # 524 POP_JUMP_FORWARD_IF_FALSE   333 (to 1192)
        # 1378         526 LOAD_FAST                2 (rootdir)
        # 528 LOAD_METHOD              2 (listdir)
        # 550 PRECALL                  0
        # 554 CALL                     0
        # 564 GET_ITER
        # >>  566 EXTENDED_ARG             1
        # 568 FOR_ITER               311 (to 1192)
        # 570 STORE_FAST              10 (path)
        # 1379         572 PUSH_NULL
        # 574 LOAD_FAST                5 (parse_num)
        # 576 LOAD_FAST               10 (path)
        # 578 PRECALL                  1
        # 582 CALL                     1
        # 592 STORE_FAST              11 (num)
        # 1380         594 LOAD_FAST               11 (num)
        # 596 POP_JUMP_FORWARD_IF_NONE   232 (to 1062)
        # 598 LOAD_FAST               11 (num)
        # 600 LOAD_FAST                9 (maxnum)
        # 602 LOAD_FAST                3 (keep)
        # 604 BINARY_OP               10 (-)
        # 608 COMPARE_OP               1 (<=)
        # 614 POP_JUMP_FORWARD_IF_FALSE   223 (to 1062)
        # 1381         616 NOP
        # 1383         618 LOAD_FAST                4 (lock_timeout)
        # 620 POP_JUMP_FORWARD_IF_FALSE    11 (to 644)
        # 1384         622 PUSH_NULL
        # 624 LOAD_FAST                6 (create_lockfile)
        # 626 LOAD_FAST               10 (path)
        # 628 PRECALL                  1
        # 632 CALL                     1
        # 642 POP_TOP
        # >>  644 JUMP_FORWARD            83 (to 812)
        # >>  646 PUSH_EXC_INFO
        # 1385         648 LOAD_GLOBAL             12 (error)
        # 660 LOAD_ATTR                7 (EEXIST)
        # 670 LOAD_GLOBAL             12 (error)
        # 682 LOAD_ATTR                8 (ENOENT)
        # 692 LOAD_GLOBAL             12 (error)
        # 704 LOAD_ATTR                9 (EBUSY)
        # 714 BUILD_TUPLE              3
        # 716 CHECK_EXC_MATCH
        # 718 POP_JUMP_FORWARD_IF_FALSE    42 (to 804)
        # 720 POP_TOP
        # 1386         722 PUSH_NULL
        # 724 LOAD_FAST               14 (get_mtime)
        # 726 LOAD_FAST               10 (path)
        # 728 PRECALL                  1
        # 732 CALL                     1
        # 742 STORE_FAST              17 (path_time)
        # 1387         744 LOAD_FAST               17 (path_time)
        # 746 POP_JUMP_FORWARD_IF_TRUE     2 (to 752)
        # 1389         748 POP_EXCEPT
        # 750 JUMP_BACKWARD           93 (to 566)
        # 1390     >>  752 LOAD_GLOBAL             21 (NULL + abs)
        # 764 LOAD_FAST               16 (udir_time)
        # 766 LOAD_FAST               17 (path_time)
        # 768 BINARY_OP               10 (-)
        # 772 PRECALL                  1
        # 776 CALL                     1
        # 786 LOAD_FAST                4 (lock_timeout)
        # 788 COMPARE_OP               0 (<)
        # 794 POP_JUMP_FORWARD_IF_FALSE     2 (to 800)
        # 1393         796 POP_EXCEPT
        # 798 JUMP_BACKWARD          117 (to 566)
        # 1390     >>  800 POP_EXCEPT
        # 802 JUMP_FORWARD             4 (to 812)
        # 1385     >>  804 RERAISE                  0
        # >>  806 COPY                     3
        # 808 POP_EXCEPT
        # 810 RERAISE                  1
        # 1398     >>  812 LOAD_FAST                2 (rootdir)
        # 814 LOAD_METHOD             11 (join)
        # 836 LOAD_DEREF              22 (garbage_prefix)
        # 838 LOAD_GLOBAL             11 (NULL + str)
        # 850 LOAD_GLOBAL             25 (NULL + uuid)
        # 862 LOAD_ATTR               13 (uuid4)
        # 872 PRECALL                  0
        # 876 CALL                     0
        # 886 PRECALL                  1
        # 890 CALL                     1
        # 900 BINARY_OP                0 (+)
        # 904 PRECALL                  1
        # 908 CALL                     1
        # 918 STORE_FAST              18 (garbage_path)
        # 1399         920 NOP
        # 1400         922 LOAD_FAST               10 (path)
        # 924 LOAD_METHOD             14 (rename)
        # 946 LOAD_FAST               18 (garbage_path)
        # 948 PRECALL                  1
        # 952 CALL                     1
        # 962 POP_TOP
        # 1401         964 LOAD_FAST               18 (garbage_path)
        # 966 LOAD_METHOD             15 (remove)
        # 988 LOAD_CONST               7 (1)
        # 990 KW_NAMES                11
        # 992 PRECALL                  1
        # 996 CALL                     1
        # 1006 POP_TOP
        # 1008 JUMP_FORWARD            26 (to 1062)
        # >> 1010 PUSH_EXC_INFO
        # 1402        1012 LOAD_GLOBAL             32 (KeyboardInterrupt)
        # 1024 CHECK_EXC_MATCH
        # 1026 POP_JUMP_FORWARD_IF_FALSE     2 (to 1032)
        # 1028 POP_TOP
        # 1403        1030 RAISE_VARARGS            0
        # 1404     >> 1032 LOAD_GLOBAL             34 (Exception)
        # 1044 CHECK_EXC_MATCH
        # 1046 POP_JUMP_FORWARD_IF_FALSE     3 (to 1054)
        # 1048 POP_TOP
        # 1405        1050 POP_EXCEPT
        # 1052 JUMP_FORWARD             4 (to 1062)
        # 1404     >> 1054 RERAISE                  0
        # >> 1056 COPY                     3
        # 1058 POP_EXCEPT
        # 1060 RERAISE                  1
        # 1406     >> 1062 PUSH_NULL
        # 1064 LOAD_FAST               15 (is_garbage)
        # 1066 LOAD_FAST               10 (path)
        # 1068 PRECALL                  1
        # 1072 CALL                     1
        # 1082 POP_JUMP_FORWARD_IF_FALSE    52 (to 1188)
        # 1407        1084 NOP
        # 1408        1086 LOAD_FAST               10 (path)
        # 1088 LOAD_METHOD             15 (remove)
        # 1110 LOAD_CONST               7 (1)
        # 1112 KW_NAMES                11
        # 1114 PRECALL                  1
        # 1118 CALL                     1
        # 1128 POP_TOP
        # 1130 EXTENDED_ARG             1
        # 1132 JUMP_BACKWARD          284 (to 566)
        # >> 1134 PUSH_EXC_INFO
        # 1409        1136 LOAD_GLOBAL             32 (KeyboardInterrupt)
        # 1148 CHECK_EXC_MATCH
        # 1150 POP_JUMP_FORWARD_IF_FALSE     2 (to 1156)
        # 1152 POP_TOP
        # 1410        1154 RAISE_VARARGS            0
        # 1411     >> 1156 LOAD_GLOBAL             34 (Exception)
        # 1168 CHECK_EXC_MATCH
        # 1170 POP_JUMP_FORWARD_IF_FALSE     4 (to 1180)
        # 1172 POP_TOP
        # 1412        1174 POP_EXCEPT
        # 1176 EXTENDED_ARG             1
        # 1178 JUMP_BACKWARD          307 (to 566)
        # 1411     >> 1180 RERAISE                  0
        # >> 1182 COPY                     3
        # 1184 POP_EXCEPT
        # 1186 RERAISE                  1
        # 1406     >> 1188 EXTENDED_ARG             1
        # 1190 JUMP_BACKWARD          313 (to 566)
        # 1415     >> 1192 NOP
        # 1416        1194 LOAD_GLOBAL             36 (os)
        # 1206 LOAD_ATTR               19 (environ)
        # 1216 LOAD_CONST              12 ('USER')
        # 1218 BINARY_SUBSCR
        # 1228 STORE_FAST              19 (username)
        # 1230 JUMP_FORWARD            54 (to 1340)
        # >> 1232 PUSH_EXC_INFO
        # 1417        1234 LOAD_GLOBAL             40 (KeyError)
        # 1246 CHECK_EXC_MATCH
        # 1248 POP_JUMP_FORWARD_IF_FALSE    41 (to 1332)
        # 1250 POP_TOP
        # 1418        1252 NOP
        # 1419        1254 LOAD_GLOBAL             36 (os)
        # 1266 LOAD_ATTR               19 (environ)
        # 1276 LOAD_CONST              13 ('USERNAME')
        # 1278 BINARY_SUBSCR
        # 1288 STORE_FAST              19 (username)
        # 1290 JUMP_FORWARD            18 (to 1328)
        # >> 1292 PUSH_EXC_INFO
        # 1420        1294 LOAD_GLOBAL             40 (KeyError)
        # 1306 CHECK_EXC_MATCH
        # 1308 POP_JUMP_FORWARD_IF_FALSE     5 (to 1320)
        # 1310 POP_TOP
        # 1421        1312 LOAD_CONST              14 ('current')
        # 1314 STORE_FAST              19 (username)
        # 1316 POP_EXCEPT
        # 1318 JUMP_FORWARD             4 (to 1328)
        # 1420     >> 1320 RERAISE                  0
        # >> 1322 COPY                     3
        # 1324 POP_EXCEPT
        # 1326 RERAISE                  1
        # >> 1328 POP_EXCEPT
        # 1330 JUMP_FORWARD             4 (to 1340)
        # 1417     >> 1332 RERAISE                  0
        # >> 1334 COPY                     3
        # 1336 POP_EXCEPT
        # 1338 RERAISE                  1
        # 1423     >> 1340 LOAD_GLOBAL             11 (NULL + str)
        # 1352 LOAD_FAST               12 (udir)
        # 1354 PRECALL                  1
        # 1358 CALL                     1
        # 1368 STORE_FAST              20 (src)
        # 1424        1370 LOAD_FAST               20 (src)
        # 1372 LOAD_CONST               1 (None)
        # 1374 LOAD_FAST               20 (src)
        # 1376 LOAD_METHOD             21 (rfind)
        # 1398 LOAD_CONST              15 ('-')
        # 1400 PRECALL                  1
        # 1404 CALL                     1
        # 1414 BUILD_SLICE              2
        # 1416 BINARY_SUBSCR
        # 1426 LOAD_CONST              15 ('-')
        # 1428 BINARY_OP                0 (+)
        # 1432 LOAD_FAST               19 (username)
        # 1434 BINARY_OP                0 (+)
        # 1438 STORE_FAST              21 (dest)
        # 1425        1440 NOP
        # 1426        1442 LOAD_GLOBAL             37 (NULL + os)
        # 1454 LOAD_ATTR               22 (unlink)
        # 1464 LOAD_FAST               21 (dest)
        # 1466 PRECALL                  1
        # 1470 CALL                     1
        # 1480 POP_TOP
        # 1482 JUMP_FORWARD            16 (to 1516)
        # >> 1484 PUSH_EXC_INFO
        # 1427        1486 LOAD_GLOBAL             46 (OSError)
        # 1498 CHECK_EXC_MATCH
        # 1500 POP_JUMP_FORWARD_IF_FALSE     3 (to 1508)
        # 1502 POP_TOP
        # 1428        1504 POP_EXCEPT
        # 1506 JUMP_FORWARD             4 (to 1516)
        # 1427     >> 1508 RERAISE                  0
        # >> 1510 COPY                     3
        # 1512 POP_EXCEPT
        # 1514 RERAISE                  1
        # 1429     >> 1516 NOP
        # 1430        1518 LOAD_GLOBAL             37 (NULL + os)
        # 1530 LOAD_ATTR               24 (symlink)
        # 1540 LOAD_FAST               20 (src)
        # 1542 LOAD_FAST               21 (dest)
        # 1544 PRECALL                  2
        # 1548 CALL                     2
        # 1558 POP_TOP
        # 1560 JUMP_FORWARD            29 (to 1620)
        # >> 1562 PUSH_EXC_INFO
        # 1431        1564 LOAD_GLOBAL             46 (OSError)
        # 1576 LOAD_GLOBAL             50 (AttributeError)
        # 1588 LOAD_GLOBAL             52 (NotImplementedError)
        # 1600 BUILD_TUPLE              3
        # 1602 CHECK_EXC_MATCH
        # 1604 POP_JUMP_FORWARD_IF_FALSE     3 (to 1612)
        # 1606 POP_TOP
        # 1432        1608 POP_EXCEPT
        # 1610 JUMP_FORWARD             4 (to 1620)
        # 1431     >> 1612 RERAISE                  0
        # >> 1614 COPY                     3
        # 1616 POP_EXCEPT
        # 1618 RERAISE                  1
        # 1434     >> 1620 LOAD_FAST               12 (udir)
        # 1622 RETURN_VALUE
        # ExceptionTable:
        # 228 to 354 -> 358 [0]
        # 358 to 450 -> 458 [1] lasti
        # 456 to 456 -> 458 [1] lasti
        # 618 to 642 -> 646 [1]
        # 646 to 746 -> 806 [2] lasti
        # 752 to 794 -> 806 [2] lasti
        # 804 to 804 -> 806 [2] lasti
        # 922 to 1006 -> 1010 [1]
        # 1010 to 1048 -> 1056 [2] lasti
        # 1054 to 1054 -> 1056 [2] lasti
        # 1086 to 1128 -> 1134 [1]
        # 1134 to 1172 -> 1182 [2] lasti
        # 1180 to 1180 -> 1182 [2] lasti
        # 1194 to 1228 -> 1232 [0]
        # 1232 to 1250 -> 1334 [1] lasti
        # 1254 to 1288 -> 1292 [1]
        # 1290 to 1290 -> 1334 [1] lasti
        # 1292 to 1314 -> 1322 [2] lasti
        # 1316 to 1318 -> 1334 [1] lasti
        # 1320 to 1320 -> 1322 [2] lasti
        # 1322 to 1326 -> 1334 [1] lasti
        # 1332 to 1332 -> 1334 [1] lasti
        # 1442 to 1480 -> 1484 [0]
        # 1484 to 1502 -> 1510 [1] lasti
        # 1508 to 1508 -> 1510 [1] lasti
        # 1518 to 1558 -> 1562 [0]
        # 1562 to 1606 -> 1614 [1] lasti
        # 1612 to 1612 -> 1614 [1] lasti
        # Disassembly of <code object parse_num at 0x000001EBD77CAF10, file "_pytest\_py\path.py", line 1289>:
        # 0 COPY_FREE_VARS           1
        # 1289           2 RESUME                   0
        # 1291           4 LOAD_FAST                0 (path)
        # 6 LOAD_ATTR                0 (basename)
        # 16 LOAD_METHOD              1 (lower)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 STORE_FAST               1 (nbasename)
        # 1292          54 LOAD_FAST                1 (nbasename)
        # 56 LOAD_METHOD              2 (startswith)
        # 78 LOAD_DEREF               2 (nprefix)
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 POP_JUMP_FORWARD_IF_FALSE    54 (to 204)
        # 1293          96 NOP
        # 1294          98 LOAD_GLOBAL              7 (NULL + int)
        # 110 LOAD_FAST                1 (nbasename)
        # 112 LOAD_GLOBAL              9 (NULL + len)
        # 124 LOAD_DEREF               2 (nprefix)
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 LOAD_CONST               1 (None)
        # 142 BUILD_SLICE              2
        # 144 BINARY_SUBSCR
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 168 RETURN_VALUE
        # >>  170 PUSH_EXC_INFO
        # 1295         172 LOAD_GLOBAL             10 (ValueError)
        # 184 CHECK_EXC_MATCH
        # 186 POP_JUMP_FORWARD_IF_FALSE     4 (to 196)
        # 188 POP_TOP
        # 1296         190 POP_EXCEPT
        # 192 LOAD_CONST               1 (None)
        # 194 RETURN_VALUE
        # 1295     >>  196 RERAISE                  0
        # >>  198 COPY                     3
        # 200 POP_EXCEPT
        # 202 RERAISE                  1
        # 1292     >>  204 LOAD_CONST               1 (None)
        # 206 RETURN_VALUE
        # ExceptionTable:
        # 98 to 166 -> 170 [0]
        # 170 to 188 -> 198 [1] lasti
        # 196 to 196 -> 198 [1] lasti
        # Disassembly of <code object create_lockfile at 0x000001EBD765B330, file "_pytest\_py\path.py", line 1298>:
        # 1298           0 RESUME                   0
        # 1300           2 LOAD_GLOBAL              1 (NULL + os)
        # 14 LOAD_ATTR                1 (getpid)
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 STORE_FAST               1 (mypid)
        # 1301          40 LOAD_FAST                0 (path)
        # 42 LOAD_METHOD              2 (join)
        # 64 LOAD_CONST               1 ('.lock')
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 STORE_FAST               2 (lockfile)
        # 1302          82 LOAD_GLOBAL              7 (NULL + hasattr)
        # 94 LOAD_FAST                2 (lockfile)
        # 96 LOAD_CONST               2 ('mksymlinkto')
        # 98 PRECALL                  2
        # 102 CALL                     2
        # 112 POP_JUMP_FORWARD_IF_FALSE    35 (to 184)
        # 1303         114 LOAD_FAST                2 (lockfile)
        # 116 LOAD_METHOD              4 (mksymlinkto)
        # 138 LOAD_GLOBAL             11 (NULL + str)
        # 150 LOAD_FAST                1 (mypid)
        # 152 PRECALL                  1
        # 156 CALL                     1
        # 166 PRECALL                  1
        # 170 CALL                     1
        # 180 POP_TOP
        # 182 JUMP_FORWARD           161 (to 506)
        # 1305     >>  184 LOAD_GLOBAL             13 (NULL + error)
        # 196 LOAD_ATTR                7 (checked_call)
        # 1306         206 LOAD_GLOBAL              0 (os)
        # 218 LOAD_ATTR                8 (open)
        # 228 LOAD_GLOBAL             11 (NULL + str)
        # 240 LOAD_FAST                2 (lockfile)
        # 242 PRECALL                  1
        # 246 CALL                     1
        # 256 LOAD_GLOBAL              0 (os)
        # 268 LOAD_ATTR                9 (O_WRONLY)
        # 278 LOAD_GLOBAL              0 (os)
        # 290 LOAD_ATTR               10 (O_CREAT)
        # 300 BINARY_OP                7 (|)
        # 304 LOAD_GLOBAL              0 (os)
        # 316 LOAD_ATTR               11 (O_EXCL)
        # 326 BINARY_OP                7 (|)
        # 330 LOAD_CONST               3 (420)
        # 1305         332 PRECALL                  4
        # 336 CALL                     4
        # 346 STORE_FAST               3 (fd)
        # 1308         348 LOAD_GLOBAL              1 (NULL + os)
        # 360 LOAD_ATTR               12 (fdopen)
        # 370 LOAD_FAST                3 (fd)
        # 372 LOAD_CONST               4 ('w')
        # 374 PRECALL                  2
        # 378 CALL                     2
        # 388 BEFORE_WITH
        # 390 STORE_FAST               4 (f)
        # 1309         392 LOAD_FAST                4 (f)
        # 394 LOAD_METHOD             13 (write)
        # 416 LOAD_GLOBAL             11 (NULL + str)
        # 428 LOAD_FAST                1 (mypid)
        # 430 PRECALL                  1
        # 434 CALL                     1
        # 444 PRECALL                  1
        # 448 CALL                     1
        # 458 POP_TOP
        # 1308         460 LOAD_CONST               5 (None)
        # 462 LOAD_CONST               5 (None)
        # 464 LOAD_CONST               5 (None)
        # 466 PRECALL                  2
        # 470 CALL                     2
        # 480 POP_TOP
        # 482 JUMP_FORWARD            11 (to 506)
        # >>  484 PUSH_EXC_INFO
        # 486 WITH_EXCEPT_START
        # 488 POP_JUMP_FORWARD_IF_TRUE     4 (to 498)
        # 490 RERAISE                  2
        # >>  492 COPY                     3
        # 494 POP_EXCEPT
        # 496 RERAISE                  1
        # >>  498 POP_TOP
        # 500 POP_EXCEPT
        # 502 POP_TOP
        # 504 POP_TOP
        # 1310     >>  506 LOAD_FAST                2 (lockfile)
        # 508 RETURN_VALUE
        # ExceptionTable:
        # 390 to 458 -> 484 [1] lasti
        # 484 to 490 -> 492 [3] lasti
        # 498 to 498 -> 492 [3] lasti
        # Disassembly of <code object atexit_remove_lockfile at 0x000001EBD7E48DB0, file "_pytest\_py\path.py", line 1312>:
        # 0 MAKE_CELL                0 (lockfile)
        # 2 MAKE_CELL                2 (mypid)
        # 1312           4 RESUME                   0
        # 1314           6 LOAD_GLOBAL              1 (NULL + os)
        # 18 LOAD_ATTR                1 (getpid)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 STORE_DEREF              2 (mypid)
        # 1316          44 LOAD_CLOSURE             0 (lockfile)
        # 46 LOAD_CLOSURE             2 (mypid)
        # 48 BUILD_TUPLE              2
        # 50 LOAD_CONST               1 (<code object try_remove_lockfile at 0x000001EBD7F04570, file "_pytest\_py\path.py", line 1316>)
        # 52 MAKE_FUNCTION            8 (closure)
        # 54 STORE_FAST               1 (try_remove_lockfile)
        # 1329          56 LOAD_GLOBAL              5 (NULL + atexit)
        # 68 LOAD_ATTR                3 (register)
        # 78 LOAD_FAST                1 (try_remove_lockfile)
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 POP_TOP
        # 96 LOAD_CONST               2 (None)
        # 98 RETURN_VALUE
        # Disassembly of <code object try_remove_lockfile at 0x000001EBD7F04570, file "_pytest\_py\path.py", line 1316>:
        # 0 COPY_FREE_VARS           2
        # 1316           2 RESUME                   0
        # 1322           4 LOAD_GLOBAL              1 (NULL + os)
        # 16 LOAD_ATTR                1 (getpid)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 LOAD_DEREF               1 (mypid)
        # 42 COMPARE_OP               3 (!=)
        # 48 POP_JUMP_FORWARD_IF_FALSE     2 (to 54)
        # 1323          50 LOAD_CONST               0 (None)
        # 52 RETURN_VALUE
        # 1324     >>   54 NOP
        # 1325          56 LOAD_DEREF               0 (lockfile)
        # 58 LOAD_METHOD              2 (remove)
        # 80 PRECALL                  0
        # 84 CALL                     0
        # 94 POP_TOP
        # 96 LOAD_CONST               0 (None)
        # 98 RETURN_VALUE
        # >>  100 PUSH_EXC_INFO
        # 1326         102 LOAD_GLOBAL              6 (error)
        # 114 LOAD_ATTR                4 (Error)
        # 124 CHECK_EXC_MATCH
        # 126 POP_JUMP_FORWARD_IF_FALSE     4 (to 136)
        # 128 POP_TOP
        # 1327         130 POP_EXCEPT
        # 132 LOAD_CONST               0 (None)
        # 134 RETURN_VALUE
        # 1326     >>  136 RERAISE                  0
        # >>  138 COPY                     3
        # 140 POP_EXCEPT
        # 142 RERAISE                  1
        # ExceptionTable:
        # 56 to 94 -> 100 [0]
        # 100 to 128 -> 138 [1] lasti
        # 136 to 136 -> 138 [1] lasti
        # Disassembly of <code object get_mtime at 0x000001EBD7E48ED0, file "_pytest\_py\path.py", line 1361>:
        # 1361           0 RESUME                   0
        # 1363           2 NOP
        # 1364           4 LOAD_FAST                0 (path)
        # 6 LOAD_METHOD              0 (lstat)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 LOAD_ATTR                1 (mtime)
        # 52 RETURN_VALUE
        # >>   54 PUSH_EXC_INFO
        # 1365          56 LOAD_GLOBAL              4 (error)
        # 68 LOAD_ATTR                3 (Error)
        # 78 CHECK_EXC_MATCH
        # 80 POP_JUMP_FORWARD_IF_FALSE     4 (to 90)
        # 82 POP_TOP
        # 1366          84 POP_EXCEPT
        # 86 LOAD_CONST               1 (None)
        # 88 RETURN_VALUE
        # 1365     >>   90 RERAISE                  0
        # >>   92 COPY                     3
        # 94 POP_EXCEPT
        # 96 RERAISE                  1
        # ExceptionTable:
        # 4 to 50 -> 54 [0]
        # 54 to 82 -> 92 [1] lasti
        # 90 to 90 -> 92 [1] lasti
        # Disassembly of <code object is_garbage at 0x000001EBD7DF2D30, file "_pytest\_py\path.py", line 1370>:
        # 0 COPY_FREE_VARS           1
        # 1370           2 RESUME                   0
        # 1372           4 LOAD_FAST                0 (path)
        # 6 LOAD_ATTR                0 (basename)
        # 16 STORE_FAST               1 (bn)
        # 1373          18 LOAD_FAST                1 (bn)
        # 20 LOAD_METHOD              1 (startswith)
        # 42 LOAD_DEREF               2 (garbage_prefix)
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 RETURN_VALUE


def copymode(src, dest):
    """Copy permission from src to dst."""
    # 1437           0 RESUME                   0
    # 1439           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (shutil)
    # 8 STORE_FAST               2 (shutil)
    # 1441          10 LOAD_FAST                2 (shutil)
    # 12 LOAD_METHOD              1 (copymode)
    # 34 LOAD_FAST                0 (src)
    # 36 LOAD_FAST                1 (dest)
    # 38 PRECALL                  2
    # 42 CALL                     2
    # 52 POP_TOP
    # 54 LOAD_CONST               2 (None)
    # 56 RETURN_VALUE

def copystat(src, dest):
    """Copy permission,  last modification time,
    last access time, and flags from src to dst."""
    # 1444           0 RESUME                   0
    # 1447           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (shutil)
    # 8 STORE_FAST               2 (shutil)
    # 1449          10 LOAD_FAST                2 (shutil)
    # 12 LOAD_METHOD              1 (copystat)
    # 34 LOAD_GLOBAL              5 (NULL + str)
    # 46 LOAD_FAST                0 (src)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 LOAD_GLOBAL              5 (NULL + str)
    # 74 LOAD_FAST                1 (dest)
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 PRECALL                  2
    # 94 CALL                     2
    # 104 POP_TOP
    # 106 LOAD_CONST               2 (None)
    # 108 RETURN_VALUE

def copychunked(src, dest):
    # 1452           0 RESUME                   0
    # 1453           2 LOAD_CONST               1 (524288)
    # 4 STORE_FAST               2 (chunksize)
    # 1454           6 LOAD_FAST                0 (src)
    # 8 LOAD_METHOD              0 (open)
    # 30 LOAD_CONST               2 ('rb')
    # 32 PRECALL                  1
    # 36 CALL                     1
    # 46 STORE_FAST               3 (fsrc)
    # 1455          48 NOP
    # 1456          50 LOAD_FAST                1 (dest)
    # 52 LOAD_METHOD              0 (open)
    # 74 LOAD_CONST               3 ('wb')
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 STORE_FAST               4 (fdest)
    # 1457          92 NOP
    # 1458          94 NOP
    # 1459     >>   96 LOAD_FAST                3 (fsrc)
    # 98 LOAD_METHOD              1 (read)
    # 120 LOAD_FAST                2 (chunksize)
    # 122 PRECALL                  1
    # 126 CALL                     1
    # 136 STORE_FAST               5 (buf)
    # 1460         138 LOAD_FAST                5 (buf)
    # 140 POP_JUMP_FORWARD_IF_TRUE     1 (to 144)
    # 1461         142 JUMP_FORWARD            22 (to 188)
    # 1462     >>  144 LOAD_FAST                4 (fdest)
    # 146 LOAD_METHOD              2 (write)
    # 168 LOAD_FAST                5 (buf)
    # 170 PRECALL                  1
    # 174 CALL                     1
    # 184 POP_TOP
    # 1458         186 JUMP_BACKWARD           46 (to 96)
    # 1461     >>  188 NOP
    # 1464         190 LOAD_FAST                4 (fdest)
    # 192 LOAD_METHOD              3 (close)
    # 214 PRECALL                  0
    # 218 CALL                     0
    # 228 POP_TOP
    # 230 JUMP_FORWARD            25 (to 282)
    # >>  232 PUSH_EXC_INFO
    # 234 LOAD_FAST                4 (fdest)
    # 236 LOAD_METHOD              3 (close)
    # 258 PRECALL                  0
    # 262 CALL                     0
    # 272 POP_TOP
    # 274 RERAISE                  0
    # >>  276 COPY                     3
    # 278 POP_EXCEPT
    # 280 RERAISE                  1
    # >>  282 NOP
    # 1466         284 LOAD_FAST                3 (fsrc)
    # 286 LOAD_METHOD              3 (close)
    # 308 PRECALL                  0
    # 312 CALL                     0
    # 322 POP_TOP
    # 324 LOAD_CONST               0 (None)
    # 326 RETURN_VALUE
    # >>  328 PUSH_EXC_INFO
    # 330 LOAD_FAST                3 (fsrc)
    # 332 LOAD_METHOD              3 (close)
    # 354 PRECALL                  0
    # 358 CALL                     0
    # 368 POP_TOP
    # 370 RERAISE                  0
    # >>  372 COPY                     3
    # 374 POP_EXCEPT
    # 376 RERAISE                  1
    # ExceptionTable:
    # 50 to 90 -> 328 [0]
    # 94 to 186 -> 232 [0]
    # 190 to 230 -> 328 [0]
    # 232 to 274 -> 276 [1] lasti
    # 276 to 280 -> 328 [0]
    # 328 to 370 -> 372 [1] lasti

def isimportable(name):
    # 1469           0 RESUME                   0
    # 1470           2 LOAD_FAST                0 (name)
    # 4 POP_JUMP_FORWARD_IF_FALSE    83 (to 172)
    # 6 LOAD_FAST                0 (name)
    # 8 LOAD_CONST               1 (0)
    # 10 BINARY_SUBSCR
    # 20 LOAD_METHOD              0 (isalpha)
    # 42 PRECALL                  0
    # 46 CALL                     0
    # 56 POP_JUMP_FORWARD_IF_TRUE    12 (to 82)
    # 58 LOAD_FAST                0 (name)
    # 60 LOAD_CONST               1 (0)
    # 62 BINARY_SUBSCR
    # 72 LOAD_CONST               2 ('_')
    # 74 COMPARE_OP               2 (==)
    # 80 POP_JUMP_FORWARD_IF_FALSE    47 (to 176)
    # 1471     >>   82 LOAD_FAST                0 (name)
    # 84 LOAD_METHOD              1 (replace)
    # 106 LOAD_CONST               2 ('_')
    # 108 LOAD_CONST               3 ('')
    # 110 PRECALL                  2
    # 114 CALL                     2
    # 124 STORE_FAST               0 (name)
    # 1472         126 LOAD_FAST                0 (name)
    # 128 UNARY_NOT
    # 130 JUMP_IF_TRUE_OR_POP     19 (to 170)
    # 132 LOAD_FAST                0 (name)
    # 134 LOAD_METHOD              2 (isalnum)
    # 156 PRECALL                  0
    # 160 CALL                     0
    # >>  170 RETURN_VALUE
    # 1470     >>  172 LOAD_CONST               0 (None)
    # 174 RETURN_VALUE
    # >>  176 LOAD_CONST               0 (None)
    # 178 RETURN_VALUE
