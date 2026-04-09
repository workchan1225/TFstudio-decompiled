# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: multiprocessing\connection.py

import errno
import io
import os
import sys
import socket
import struct
import time
import tempfile
import itertools
import _multiprocessing
from  import util
from  import AuthenticationError
from context import reduction
import _winapi
from _winapi import WAIT_OBJECT_0
import selectors

def _init_timeout(timeout):
    # 60           0 RESUME                   0
    # 61           2 LOAD_GLOBAL              1 (NULL + time)
    # 14 LOAD_ATTR                1 (monotonic)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 LOAD_FAST                0 (timeout)
    # 40 BINARY_OP                0 (+)
    # 44 RETURN_VALUE

def _check_timeout(t):
    # 63           0 RESUME                   0
    # 64           2 LOAD_GLOBAL              1 (NULL + time)
    # 14 LOAD_ATTR                1 (monotonic)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 LOAD_FAST                0 (t)
    # 40 COMPARE_OP               4 (>)
    # 46 RETURN_VALUE

def arbitrary_address(family):
    """
    Return an arbitrary free address for the given family
    """
    # 70           0 RESUME                   0
    # 74           2 LOAD_FAST                0 (family)
    # 4 LOAD_CONST               1 ('AF_INET')
    # 6 COMPARE_OP               2 (==)
    # 12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
    # 75          14 LOAD_CONST               2 (('localhost', 0))
    # 16 RETURN_VALUE
    # 76     >>   18 LOAD_FAST                0 (family)
    # 20 LOAD_CONST               3 ('AF_UNIX')
    # 22 COMPARE_OP               2 (==)
    # 28 POP_JUMP_FORWARD_IF_FALSE    39 (to 108)
    # 77          30 LOAD_GLOBAL              1 (NULL + tempfile)
    # 42 LOAD_ATTR                1 (mktemp)
    # 52 LOAD_CONST               4 ('listener-')
    # 54 LOAD_GLOBAL              5 (NULL + util)
    # 66 LOAD_ATTR                3 (get_temp_dir)
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 KW_NAMES                 5
    # 92 PRECALL                  2
    # 96 CALL                     2
    # 106 RETURN_VALUE
    # 78     >>  108 LOAD_FAST                0 (family)
    # 110 LOAD_CONST               6 ('AF_PIPE')
    # 112 COMPARE_OP               2 (==)
    # 118 POP_JUMP_FORWARD_IF_FALSE    62 (to 244)
    # 79         120 LOAD_GLOBAL              1 (NULL + tempfile)
    # 132 LOAD_ATTR                1 (mktemp)
    # 142 LOAD_CONST               7 ('\\\\.\\pipe\\pyc-%d-%d-')
    # 80         144 LOAD_GLOBAL              9 (NULL + os)
    # 156 LOAD_ATTR                5 (getpid)
    # 166 PRECALL                  0
    # 170 CALL                     0
    # 180 LOAD_GLOBAL             13 (NULL + next)
    # 192 LOAD_GLOBAL             14 (_mmap_counter)
    # 204 PRECALL                  1
    # 208 CALL                     1
    # 218 BUILD_TUPLE              2
    # 79         220 BINARY_OP                6 (%)
    # 80         224 LOAD_CONST               8 ('')
    # 79         226 KW_NAMES                 5
    # 228 PRECALL                  2
    # 232 CALL                     2
    # 242 RETURN_VALUE
    # 82     >>  244 LOAD_GLOBAL             17 (NULL + ValueError)
    # 256 LOAD_CONST               9 ('unrecognized family')
    # 258 PRECALL                  1
    # 262 CALL                     1
    # 272 RAISE_VARARGS            1

def _validate_family(family):
    """
    Checks if the family is valid for the current environment.
    """
    # 84           0 RESUME                   0
    # 88           2 LOAD_GLOBAL              0 (sys)
    # 14 LOAD_ATTR                1 (platform)
    # 24 LOAD_CONST               1 ('win32')
    # 26 COMPARE_OP               3 (!=)
    # 32 POP_JUMP_FORWARD_IF_FALSE    24 (to 82)
    # 34 LOAD_FAST                0 (family)
    # 36 LOAD_CONST               2 ('AF_PIPE')
    # 38 COMPARE_OP               2 (==)
    # 44 POP_JUMP_FORWARD_IF_FALSE    18 (to 82)
    # 89          46 LOAD_GLOBAL              5 (NULL + ValueError)
    # 58 LOAD_CONST               3 ('Family %s is not recognized.')
    # 60 LOAD_FAST                0 (family)
    # 62 BINARY_OP                6 (%)
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 80 RAISE_VARARGS            1
    # 91     >>   82 LOAD_GLOBAL              0 (sys)
    # 94 LOAD_ATTR                1 (platform)
    # 104 LOAD_CONST               1 ('win32')
    # 106 COMPARE_OP               2 (==)
    # 112 POP_JUMP_FORWARD_IF_FALSE    45 (to 204)
    # 114 LOAD_FAST                0 (family)
    # 116 LOAD_CONST               4 ('AF_UNIX')
    # 118 COMPARE_OP               2 (==)
    # 124 POP_JUMP_FORWARD_IF_FALSE    41 (to 208)
    # 93         126 LOAD_GLOBAL              7 (NULL + hasattr)
    # 138 LOAD_GLOBAL              8 (socket)
    # 150 LOAD_FAST                0 (family)
    # 152 PRECALL                  2
    # 156 CALL                     2
    # 166 POP_JUMP_FORWARD_IF_TRUE    22 (to 212)
    # 94         168 LOAD_GLOBAL              5 (NULL + ValueError)
    # 180 LOAD_CONST               3 ('Family %s is not recognized.')
    # 182 LOAD_FAST                0 (family)
    # 184 BINARY_OP                6 (%)
    # 188 PRECALL                  1
    # 192 CALL                     1
    # 202 RAISE_VARARGS            1
    # 91     >>  204 LOAD_CONST               5 (None)
    # 206 RETURN_VALUE
    # >>  208 LOAD_CONST               5 (None)
    # 210 RETURN_VALUE
    # 93     >>  212 LOAD_CONST               5 (None)
    # 214 RETURN_VALUE

def address_type(address):
    """
    Return the types of the address

    This can be 'AF_INET', 'AF_UNIX', or 'AF_PIPE'
    """
    # 96           0 RESUME                   0
    # 102           2 LOAD_GLOBAL              1 (NULL + type)
    # 14 LOAD_FAST                0 (address)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 LOAD_GLOBAL              2 (tuple)
    # 42 COMPARE_OP               2 (==)
    # 48 POP_JUMP_FORWARD_IF_FALSE     2 (to 54)
    # 103          50 LOAD_CONST               1 ('AF_INET')
    # 52 RETURN_VALUE
    # 104     >>   54 LOAD_GLOBAL              1 (NULL + type)
    # 66 LOAD_FAST                0 (address)
    # 68 PRECALL                  1
    # 72 CALL                     1
    # 82 LOAD_GLOBAL              4 (str)
    # 94 IS_OP                    0
    # 96 POP_JUMP_FORWARD_IF_FALSE    23 (to 144)
    # 98 LOAD_FAST                0 (address)
    # 100 LOAD_METHOD              3 (startswith)
    # 122 LOAD_CONST               2 ('\\\\')
    # 124 PRECALL                  1
    # 128 CALL                     1
    # 138 POP_JUMP_FORWARD_IF_FALSE     2 (to 144)
    # 105         140 LOAD_CONST               3 ('AF_PIPE')
    # 142 RETURN_VALUE
    # 106     >>  144 LOAD_GLOBAL              1 (NULL + type)
    # 156 LOAD_FAST                0 (address)
    # 158 PRECALL                  1
    # 162 CALL                     1
    # 172 LOAD_GLOBAL              4 (str)
    # 184 IS_OP                    0
    # 186 POP_JUMP_FORWARD_IF_TRUE    20 (to 228)
    # 188 LOAD_GLOBAL              9 (NULL + util)
    # 200 LOAD_ATTR                5 (is_abstract_socket_namespace)
    # 210 LOAD_FAST                0 (address)
    # 212 PRECALL                  1
    # 216 CALL                     1
    # 226 POP_JUMP_FORWARD_IF_FALSE     2 (to 232)
    # 107     >>  228 LOAD_CONST               4 ('AF_UNIX')
    # 230 RETURN_VALUE
    # 109     >>  232 LOAD_GLOBAL             13 (NULL + ValueError)
    # 244 LOAD_CONST               5 ('address type of %r unrecognized')
    # 246 LOAD_FAST                0 (address)
    # 248 BINARY_OP                6 (%)
    # 252 PRECALL                  1
    # 256 CALL                     1
    # 266 RAISE_VARARGS            1

class _ConnectionBase:
    """_ConnectionBase"""
    def __init__(self, handle, readable, writable):
        # 118           0 RESUME                   0
        # 119           2 LOAD_FAST                1 (handle)
        # 4 LOAD_METHOD              0 (__index__)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               1 (handle)
        # 120          42 LOAD_FAST                1 (handle)
        # 44 LOAD_CONST               1 (0)
        # 46 COMPARE_OP               0 (<)
        # 52 POP_JUMP_FORWARD_IF_FALSE    15 (to 84)
        # 121          54 LOAD_GLOBAL              3 (NULL + ValueError)
        # 66 LOAD_CONST               2 ('invalid handle')
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 RAISE_VARARGS            1
        # 122     >>   84 LOAD_FAST                2 (readable)
        # 86 POP_JUMP_FORWARD_IF_TRUE    17 (to 122)
        # 88 LOAD_FAST                3 (writable)
        # 90 POP_JUMP_FORWARD_IF_TRUE    15 (to 122)
        # 123          92 LOAD_GLOBAL              3 (NULL + ValueError)
        # 124         104 LOAD_CONST               3 ('at least one of `readable` and `writable` must be True')
        # 123         106 PRECALL                  1
        # 110 CALL                     1
        # 120 RAISE_VARARGS            1
        # 125     >>  122 LOAD_FAST                1 (handle)
        # 124 LOAD_FAST                0 (self)
        # 126 STORE_ATTR               2 (_handle)
        # 126         136 LOAD_FAST                2 (readable)
        # 138 LOAD_FAST                0 (self)
        # 140 STORE_ATTR               3 (_readable)
        # 127         150 LOAD_FAST                3 (writable)
        # 152 LOAD_FAST                0 (self)
        # 154 STORE_ATTR               4 (_writable)
        # 164 LOAD_CONST               0 (None)
        # 166 RETURN_VALUE

    def __del__(self):
        # 131           0 RESUME                   0
        # 132           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_handle)
        # 14 POP_JUMP_FORWARD_IF_NONE    22 (to 60)
        # 133          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (_close)
        # 40 PRECALL                  0
        # 44 CALL                     0
        # 54 POP_TOP
        # 56 LOAD_CONST               0 (None)
        # 58 RETURN_VALUE
        # 132     >>   60 LOAD_CONST               0 (None)
        # 62 RETURN_VALUE

    def _check_closed(self):
        # 135           0 RESUME                   0
        # 136           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_handle)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 46)
        # 137          16 LOAD_GLOBAL              3 (NULL + OSError)
        # 28 LOAD_CONST               1 ('handle is closed')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 136     >>   46 LOAD_CONST               0 (None)
        # 48 RETURN_VALUE

    def _check_readable(self):
        # 139           0 RESUME                   0
        # 140           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_readable)
        # 14 POP_JUMP_FORWARD_IF_TRUE    15 (to 46)
        # 141          16 LOAD_GLOBAL              3 (NULL + OSError)
        # 28 LOAD_CONST               1 ('connection is write-only')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 140     >>   46 LOAD_CONST               0 (None)
        # 48 RETURN_VALUE

    def _check_writable(self):
        # 143           0 RESUME                   0
        # 144           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_writable)
        # 14 POP_JUMP_FORWARD_IF_TRUE    15 (to 46)
        # 145          16 LOAD_GLOBAL              3 (NULL + OSError)
        # 28 LOAD_CONST               1 ('connection is read-only')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 144     >>   46 LOAD_CONST               0 (None)
        # 48 RETURN_VALUE

    def _bad_message_length(self):
        # 147           0 RESUME                   0
        # 148           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_writable)
        # 14 POP_JUMP_FORWARD_IF_FALSE     8 (to 32)
        # 149          16 LOAD_CONST               1 (False)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (_readable)
        # 30 JUMP_FORWARD            20 (to 72)
        # 151     >>   32 LOAD_FAST                0 (self)
        # 34 LOAD_METHOD              2 (close)
        # 56 PRECALL                  0
        # 60 CALL                     0
        # 70 POP_TOP
        # 152     >>   72 LOAD_GLOBAL              7 (NULL + OSError)
        # 84 LOAD_CONST               2 ('bad message length')
        # 86 PRECALL                  1
        # 90 CALL                     1
        # 100 RAISE_VARARGS            1

    def closed(self):
        """True if the connection is closed"""
        # 154           0 RESUME                   0
        # 157           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_handle)
        # 14 LOAD_CONST               1 (None)
        # 16 IS_OP                    0
        # 18 RETURN_VALUE

    def readable(self):
        """True if the connection is readable"""
        # 159           0 RESUME                   0
        # 162           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_readable)
        # 14 RETURN_VALUE

    def writable(self):
        """True if the connection is writable"""
        # 164           0 RESUME                   0
        # 167           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_writable)
        # 14 RETURN_VALUE

    def fileno(self):
        """File descriptor or handle of the connection"""
        # 169           0 RESUME                   0
        # 171           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 172          42 LOAD_FAST                0 (self)
        # 44 LOAD_ATTR                1 (_handle)
        # 54 RETURN_VALUE

    def close(self):
        """Close the connection"""
        # 174           0 RESUME                   0
        # 176           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_handle)
        # 14 POP_JUMP_FORWARD_IF_NONE    42 (to 100)
        # 177          16 NOP
        # 178          18 LOAD_FAST                0 (self)
        # 20 LOAD_METHOD              1 (_close)
        # 42 PRECALL                  0
        # 46 CALL                     0
        # 56 POP_TOP
        # 180          58 LOAD_CONST               1 (None)
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               0 (_handle)
        # 72 LOAD_CONST               1 (None)
        # 74 RETURN_VALUE
        # >>   76 PUSH_EXC_INFO
        # 78 LOAD_CONST               1 (None)
        # 80 LOAD_FAST                0 (self)
        # 82 STORE_ATTR               0 (_handle)
        # 92 RERAISE                  0
        # >>   94 COPY                     3
        # 96 POP_EXCEPT
        # 98 RERAISE                  1
        # 176     >>  100 LOAD_CONST               1 (None)
        # 102 RETURN_VALUE
        # ExceptionTable:
        # 18 to 56 -> 76 [0]
        # 76 to 92 -> 94 [1] lasti

    def send_bytes(self, buf, offset, size):
        """Send the bytes data from a bytes-like object"""
        # 182           0 RESUME                   0
        # 184           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 185          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_writable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 186          82 LOAD_GLOBAL              5 (NULL + memoryview)
        # 94 LOAD_FAST                1 (buf)
        # 96 PRECALL                  1
        # 100 CALL                     1
        # 110 STORE_FAST               4 (m)
        # 187         112 LOAD_FAST                4 (m)
        # 114 LOAD_ATTR                3 (itemsize)
        # 124 LOAD_CONST               1 (1)
        # 126 COMPARE_OP               4 (>)
        # 132 POP_JUMP_FORWARD_IF_FALSE    21 (to 176)
        # 188         134 LOAD_FAST                4 (m)
        # 136 LOAD_METHOD              4 (cast)
        # 158 LOAD_CONST               2 ('B')
        # 160 PRECALL                  1
        # 164 CALL                     1
        # 174 STORE_FAST               4 (m)
        # 189     >>  176 LOAD_FAST                4 (m)
        # 178 LOAD_ATTR                5 (nbytes)
        # 188 STORE_FAST               5 (n)
        # 190         190 LOAD_FAST                2 (offset)
        # 192 LOAD_CONST               3 (0)
        # 194 COMPARE_OP               0 (<)
        # 200 POP_JUMP_FORWARD_IF_FALSE    15 (to 232)
        # 191         202 LOAD_GLOBAL             13 (NULL + ValueError)
        # 214 LOAD_CONST               4 ('offset is negative')
        # 216 PRECALL                  1
        # 220 CALL                     1
        # 230 RAISE_VARARGS            1
        # 192     >>  232 LOAD_FAST                5 (n)
        # 234 LOAD_FAST                2 (offset)
        # 236 COMPARE_OP               0 (<)
        # 242 POP_JUMP_FORWARD_IF_FALSE    15 (to 274)
        # 193         244 LOAD_GLOBAL             13 (NULL + ValueError)
        # 256 LOAD_CONST               5 ('buffer length < offset')
        # 258 PRECALL                  1
        # 262 CALL                     1
        # 272 RAISE_VARARGS            1
        # 194     >>  274 LOAD_FAST                3 (size)
        # 276 POP_JUMP_FORWARD_IF_NOT_NONE     6 (to 290)
        # 195         278 LOAD_FAST                5 (n)
        # 280 LOAD_FAST                2 (offset)
        # 282 BINARY_OP               10 (-)
        # 286 STORE_FAST               3 (size)
        # 288 JUMP_FORWARD            45 (to 380)
        # 196     >>  290 LOAD_FAST                3 (size)
        # 292 LOAD_CONST               3 (0)
        # 294 COMPARE_OP               0 (<)
        # 300 POP_JUMP_FORWARD_IF_FALSE    15 (to 332)
        # 197         302 LOAD_GLOBAL             13 (NULL + ValueError)
        # 314 LOAD_CONST               7 ('size is negative')
        # 316 PRECALL                  1
        # 320 CALL                     1
        # 330 RAISE_VARARGS            1
        # 198     >>  332 LOAD_FAST                2 (offset)
        # 334 LOAD_FAST                3 (size)
        # 336 BINARY_OP                0 (+)
        # 340 LOAD_FAST                5 (n)
        # 342 COMPARE_OP               4 (>)
        # 348 POP_JUMP_FORWARD_IF_FALSE    15 (to 380)
        # 199         350 LOAD_GLOBAL             13 (NULL + ValueError)
        # 362 LOAD_CONST               8 ('buffer length < offset + size')
        # 364 PRECALL                  1
        # 368 CALL                     1
        # 378 RAISE_VARARGS            1
        # 200     >>  380 LOAD_FAST                0 (self)
        # 382 LOAD_METHOD              7 (_send_bytes)
        # 404 LOAD_FAST                4 (m)
        # 406 LOAD_FAST                2 (offset)
        # 408 LOAD_FAST                2 (offset)
        # 410 LOAD_FAST                3 (size)
        # 412 BINARY_OP                0 (+)
        # 416 BUILD_SLICE              2
        # 418 BINARY_SUBSCR
        # 428 PRECALL                  1
        # 432 CALL                     1
        # 442 POP_TOP
        # 444 LOAD_CONST               6 (None)
        # 446 RETURN_VALUE

    def send(self, obj):
        """Send a (picklable) object"""
        # 202           0 RESUME                   0
        # 204           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 205          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_writable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 206          82 LOAD_FAST                0 (self)
        # 84 LOAD_METHOD              2 (_send_bytes)
        # 106 LOAD_GLOBAL              6 (_ForkingPickler)
        # 118 LOAD_METHOD              4 (dumps)
        # 140 LOAD_FAST                1 (obj)
        # 142 PRECALL                  1
        # 146 CALL                     1
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 170 POP_TOP
        # 172 LOAD_CONST               1 (None)
        # 174 RETURN_VALUE

    def recv_bytes(self, maxlength):
        """
        Receive bytes data as a bytes object.
        """
        # 208           0 RESUME                   0
        # 212           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 213          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_readable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 214          82 LOAD_FAST                1 (maxlength)
        # 84 POP_JUMP_FORWARD_IF_NONE    21 (to 128)
        # 86 LOAD_FAST                1 (maxlength)
        # 88 LOAD_CONST               2 (0)
        # 90 COMPARE_OP               0 (<)
        # 96 POP_JUMP_FORWARD_IF_FALSE    15 (to 128)
        # 215          98 LOAD_GLOBAL              5 (NULL + ValueError)
        # 110 LOAD_CONST               3 ('negative maxlength')
        # 112 PRECALL                  1
        # 116 CALL                     1
        # 126 RAISE_VARARGS            1
        # 216     >>  128 LOAD_FAST                0 (self)
        # 130 LOAD_METHOD              3 (_recv_bytes)
        # 152 LOAD_FAST                1 (maxlength)
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 168 STORE_FAST               2 (buf)
        # 217         170 LOAD_FAST                2 (buf)
        # 172 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 214)
        # 218         174 LOAD_FAST                0 (self)
        # 176 LOAD_METHOD              4 (_bad_message_length)
        # 198 PRECALL                  0
        # 202 CALL                     0
        # 212 POP_TOP
        # 219     >>  214 LOAD_FAST                2 (buf)
        # 216 LOAD_METHOD              5 (getvalue)
        # 238 PRECALL                  0
        # 242 CALL                     0
        # 252 RETURN_VALUE

    def recv_bytes_into(self, buf, offset):
        """
        Receive bytes data into a writeable bytes-like object.
        Return the number of bytes read.
        """
        # 221           0 RESUME                   0
        # 226           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 227          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_readable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 228          82 LOAD_GLOBAL              5 (NULL + memoryview)
        # 94 LOAD_FAST                1 (buf)
        # 96 PRECALL                  1
        # 100 CALL                     1
        # 110 BEFORE_WITH
        # 112 STORE_FAST               3 (m)
        # 230         114 LOAD_FAST                3 (m)
        # 116 LOAD_ATTR                3 (itemsize)
        # 126 STORE_FAST               4 (itemsize)
        # 231         128 LOAD_FAST                4 (itemsize)
        # 130 LOAD_GLOBAL              9 (NULL + len)
        # 142 LOAD_FAST                3 (m)
        # 144 PRECALL                  1
        # 148 CALL                     1
        # 158 BINARY_OP                5 (*)
        # 162 STORE_FAST               5 (bytesize)
        # 232         164 LOAD_FAST                2 (offset)
        # 166 LOAD_CONST               1 (0)
        # 168 COMPARE_OP               0 (<)
        # 174 POP_JUMP_FORWARD_IF_FALSE    15 (to 206)
        # 233         176 LOAD_GLOBAL             11 (NULL + ValueError)
        # 188 LOAD_CONST               2 ('negative offset')
        # 190 PRECALL                  1
        # 194 CALL                     1
        # 204 RAISE_VARARGS            1
        # 234     >>  206 LOAD_FAST                2 (offset)
        # 208 LOAD_FAST                5 (bytesize)
        # 210 COMPARE_OP               4 (>)
        # 216 POP_JUMP_FORWARD_IF_FALSE    15 (to 248)
        # 235         218 LOAD_GLOBAL             11 (NULL + ValueError)
        # 230 LOAD_CONST               3 ('offset too large')
        # 232 PRECALL                  1
        # 236 CALL                     1
        # 246 RAISE_VARARGS            1
        # 236     >>  248 LOAD_FAST                0 (self)
        # 250 LOAD_METHOD              6 (_recv_bytes)
        # 272 PRECALL                  0
        # 276 CALL                     0
        # 286 STORE_FAST               6 (result)
        # 237         288 LOAD_FAST                6 (result)
        # 290 LOAD_METHOD              7 (tell)
        # 312 PRECALL                  0
        # 316 CALL                     0
        # 326 STORE_FAST               7 (size)
        # 238         328 LOAD_FAST                5 (bytesize)
        # 330 LOAD_FAST                2 (offset)
        # 332 LOAD_FAST                7 (size)
        # 334 BINARY_OP                0 (+)
        # 338 COMPARE_OP               0 (<)
        # 344 POP_JUMP_FORWARD_IF_FALSE    33 (to 412)
        # 239         346 LOAD_GLOBAL             17 (NULL + BufferTooShort)
        # 358 LOAD_FAST                6 (result)
        # 360 LOAD_METHOD              9 (getvalue)
        # 382 PRECALL                  0
        # 386 CALL                     0
        # 396 PRECALL                  1
        # 400 CALL                     1
        # 410 RAISE_VARARGS            1
        # 241     >>  412 LOAD_FAST                6 (result)
        # 414 LOAD_METHOD             10 (seek)
        # 436 LOAD_CONST               1 (0)
        # 438 PRECALL                  1
        # 442 CALL                     1
        # 452 POP_TOP
        # 242         454 LOAD_FAST                6 (result)
        # 456 LOAD_METHOD             11 (readinto)
        # 478 LOAD_FAST                3 (m)
        # 480 LOAD_FAST                2 (offset)
        # 482 LOAD_FAST                4 (itemsize)
        # 484 BINARY_OP                2 (//)
        # 243         488 LOAD_FAST                2 (offset)
        # 490 LOAD_FAST                7 (size)
        # 492 BINARY_OP                0 (+)
        # 496 LOAD_FAST                4 (itemsize)
        # 498 BINARY_OP                2 (//)
        # 242         502 BUILD_SLICE              2
        # 504 BINARY_SUBSCR
        # 514 PRECALL                  1
        # 518 CALL                     1
        # 528 POP_TOP
        # 244         530 LOAD_FAST                7 (size)
        # 228         532 SWAP                     2
        # 534 LOAD_CONST               4 (None)
        # 536 LOAD_CONST               4 (None)
        # 538 LOAD_CONST               4 (None)
        # 540 PRECALL                  2
        # 544 CALL                     2
        # 554 POP_TOP
        # 556 RETURN_VALUE
        # >>  558 PUSH_EXC_INFO
        # 560 WITH_EXCEPT_START
        # 562 POP_JUMP_FORWARD_IF_TRUE     4 (to 572)
        # 564 RERAISE                  2
        # >>  566 COPY                     3
        # 568 POP_EXCEPT
        # 570 RERAISE                  1
        # >>  572 POP_TOP
        # 574 POP_EXCEPT
        # 576 POP_TOP
        # 578 POP_TOP
        # 580 LOAD_CONST               4 (None)
        # 582 RETURN_VALUE
        # ExceptionTable:
        # 112 to 530 -> 558 [1] lasti
        # 558 to 564 -> 566 [3] lasti
        # 572 to 572 -> 566 [3] lasti

    def recv(self):
        """Receive a (picklable) object"""
        # 246           0 RESUME                   0
        # 248           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 249          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_readable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 250          82 LOAD_FAST                0 (self)
        # 84 LOAD_METHOD              2 (_recv_bytes)
        # 106 PRECALL                  0
        # 110 CALL                     0
        # 120 STORE_FAST               1 (buf)
        # 251         122 LOAD_GLOBAL              6 (_ForkingPickler)
        # 134 LOAD_METHOD              4 (loads)
        # 156 LOAD_FAST                1 (buf)
        # 158 LOAD_METHOD              5 (getbuffer)
        # 180 PRECALL                  0
        # 184 CALL                     0
        # 194 PRECALL                  1
        # 198 CALL                     1
        # 208 RETURN_VALUE

    def poll(self, timeout):
        """Whether there is any input available to be read"""
        # 253           0 RESUME                   0
        # 255           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_check_closed)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 256          42 LOAD_FAST                0 (self)
        # 44 LOAD_METHOD              1 (_check_readable)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 POP_TOP
        # 257          82 LOAD_FAST                0 (self)
        # 84 LOAD_METHOD              2 (_poll)
        # 106 LOAD_FAST                1 (timeout)
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 RETURN_VALUE

    def __enter__(self):
        # 259           0 RESUME                   0
        # 260           2 LOAD_FAST                0 (self)
        # 4 RETURN_VALUE

    def __exit__(self, exc_type, exc_value, exc_tb):
        # 262           0 RESUME                   0
        # 263           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (close)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE


class PipeConnection:
    """PipeConnection"""
    def _close(self, _CloseHandle):
        # 277           0 RESUME                   0
        # 278           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_send_ov)
        # 14 STORE_FAST               2 (ov)
        # 279          16 LOAD_FAST                2 (ov)
        # 18 POP_JUMP_FORWARD_IF_NONE    20 (to 60)
        # 281          20 LOAD_FAST                2 (ov)
        # 22 LOAD_METHOD              1 (cancel)
        # 44 PRECALL                  0
        # 48 CALL                     0
        # 58 POP_TOP
        # 282     >>   60 PUSH_NULL
        # 62 LOAD_FAST                1 (_CloseHandle)
        # 64 LOAD_FAST                0 (self)
        # 66 LOAD_ATTR                2 (_handle)
        # 76 PRECALL                  1
        # 80 CALL                     1
        # 90 POP_TOP
        # 92 LOAD_CONST               0 (None)
        # 94 RETURN_VALUE

    def _send_bytes(self, buf):
        # 284           0 RESUME                   0
        # 285           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_send_ov)
        # 14 POP_JUMP_FORWARD_IF_NONE    15 (to 46)
        # 287          16 LOAD_GLOBAL              3 (NULL + ValueError)
        # 28 LOAD_CONST               1 ('concurrent send_bytes() calls are not supported')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 289     >>   46 LOAD_GLOBAL              5 (NULL + _winapi)
        # 58 LOAD_ATTR                3 (WriteFile)
        # 68 LOAD_FAST                0 (self)
        # 70 LOAD_ATTR                4 (_handle)
        # 80 LOAD_FAST                1 (buf)
        # 82 LOAD_CONST               2 (True)
        # 84 KW_NAMES                 3
        # 86 PRECALL                  3
        # 90 CALL                     3
        # 100 UNPACK_SEQUENCE          2
        # 104 STORE_FAST               2 (ov)
        # 106 STORE_FAST               3 (err)
        # 290         108 LOAD_FAST                2 (ov)
        # 110 LOAD_FAST                0 (self)
        # 112 STORE_ATTR               0 (_send_ov)
        # 291         122 NOP
        # 292         124 LOAD_FAST                3 (err)
        # 126 LOAD_GLOBAL              4 (_winapi)
        # 138 LOAD_ATTR                5 (ERROR_IO_PENDING)
        # 148 COMPARE_OP               2 (==)
        # 154 POP_JUMP_FORWARD_IF_FALSE    46 (to 248)
        # 293         156 LOAD_GLOBAL              5 (NULL + _winapi)
        # 168 LOAD_ATTR                6 (WaitForMultipleObjects)
        # 294         178 LOAD_FAST                2 (ov)
        # 180 LOAD_ATTR                7 (event)
        # 190 BUILD_LIST               1
        # 192 LOAD_CONST               4 (False)
        # 194 LOAD_GLOBAL             16 (INFINITE)
        # 293         206 PRECALL                  3
        # 210 CALL                     3
        # 220 STORE_FAST               4 (waitres)
        # 295         222 LOAD_FAST                4 (waitres)
        # 224 LOAD_GLOBAL             18 (WAIT_OBJECT_0)
        # 236 COMPARE_OP               2 (==)
        # 242 POP_JUMP_FORWARD_IF_TRUE     2 (to 248)
        # 244 LOAD_ASSERTION_ERROR
        # 246 RAISE_VARARGS            1
        # >>  248 JUMP_FORWARD            26 (to 302)
        # >>  250 PUSH_EXC_INFO
        # 296         252 POP_TOP
        # 297         254 LOAD_FAST                2 (ov)
        # 256 LOAD_METHOD             10 (cancel)
        # 278 PRECALL                  0
        # 282 CALL                     0
        # 292 POP_TOP
        # 298         294 RAISE_VARARGS            0
        # >>  296 COPY                     3
        # 298 POP_EXCEPT
        # 300 RERAISE                  1
        # 300     >>  302 LOAD_CONST               0 (None)
        # 304 LOAD_FAST                0 (self)
        # 306 STORE_ATTR               0 (_send_ov)
        # 301         316 LOAD_FAST                2 (ov)
        # 318 LOAD_METHOD             11 (GetOverlappedResult)
        # 340 LOAD_CONST               2 (True)
        # 342 PRECALL                  1
        # 346 CALL                     1
        # 356 UNPACK_SEQUENCE          2
        # 360 STORE_FAST               5 (nwritten)
        # 362 STORE_FAST               3 (err)
        # 364 JUMP_FORWARD            36 (to 438)
        # >>  366 PUSH_EXC_INFO
        # 300         368 LOAD_CONST               0 (None)
        # 370 LOAD_FAST                0 (self)
        # 372 STORE_ATTR               0 (_send_ov)
        # 301         382 LOAD_FAST                2 (ov)
        # 384 LOAD_METHOD             11 (GetOverlappedResult)
        # 406 LOAD_CONST               2 (True)
        # 408 PRECALL                  1
        # 412 CALL                     1
        # 422 UNPACK_SEQUENCE          2
        # 426 STORE_FAST               5 (nwritten)
        # 428 STORE_FAST               3 (err)
        # 430 RERAISE                  0
        # >>  432 COPY                     3
        # 434 POP_EXCEPT
        # 436 RERAISE                  1
        # 302     >>  438 LOAD_FAST                3 (err)
        # 440 LOAD_GLOBAL              4 (_winapi)
        # 452 LOAD_ATTR               12 (ERROR_OPERATION_ABORTED)
        # 462 COMPARE_OP               2 (==)
        # 468 POP_JUMP_FORWARD_IF_FALSE    26 (to 522)
        # 306         470 LOAD_GLOBAL             27 (NULL + OSError)
        # 482 LOAD_GLOBAL             28 (errno)
        # 494 LOAD_ATTR               15 (EPIPE)
        # 504 LOAD_CONST               5 ('handle is closed')
        # 506 PRECALL                  2
        # 510 CALL                     2
        # 520 RAISE_VARARGS            1
        # 307     >>  522 LOAD_FAST                3 (err)
        # 524 LOAD_CONST               6 (0)
        # 526 COMPARE_OP               2 (==)
        # 532 POP_JUMP_FORWARD_IF_TRUE     2 (to 538)
        # 534 LOAD_ASSERTION_ERROR
        # 536 RAISE_VARARGS            1
        # 308     >>  538 LOAD_FAST                5 (nwritten)
        # 540 LOAD_GLOBAL             33 (NULL + len)
        # 552 LOAD_FAST                1 (buf)
        # 554 PRECALL                  1
        # 558 CALL                     1
        # 568 COMPARE_OP               2 (==)
        # 574 POP_JUMP_FORWARD_IF_TRUE     2 (to 580)
        # 576 LOAD_ASSERTION_ERROR
        # 578 RAISE_VARARGS            1
        # >>  580 LOAD_CONST               0 (None)
        # 582 RETURN_VALUE
        # ExceptionTable:
        # 124 to 246 -> 250 [0]
        # 248 to 248 -> 366 [0]
        # 250 to 294 -> 296 [1] lasti
        # 296 to 300 -> 366 [0]
        # 366 to 430 -> 432 [1] lasti

    def _recv_bytes(self, maxsize):
        # 310           0 RESUME                   0
        # 311           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_got_empty_message)
        # 14 POP_JUMP_FORWARD_IF_FALSE    26 (to 68)
        # 312          16 LOAD_CONST               1 (False)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               0 (_got_empty_message)
        # 313          30 LOAD_GLOBAL              3 (NULL + io)
        # 42 LOAD_ATTR                2 (BytesIO)
        # 52 PRECALL                  0
        # 56 CALL                     0
        # 66 RETURN_VALUE
        # 315     >>   68 LOAD_FAST                1 (maxsize)
        # 70 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 76)
        # 72 LOAD_CONST               2 (128)
        # 74 JUMP_FORWARD            15 (to 106)
        # >>   76 LOAD_GLOBAL              7 (NULL + min)
        # 88 LOAD_FAST                1 (maxsize)
        # 90 LOAD_CONST               2 (128)
        # 92 PRECALL                  2
        # 96 CALL                     2
        # >>  106 STORE_FAST               2 (bsize)
        # 316         108 NOP
        # 317         110 LOAD_GLOBAL              9 (NULL + _winapi)
        # 122 LOAD_ATTR                5 (ReadFile)
        # 132 LOAD_FAST                0 (self)
        # 134 LOAD_ATTR                6 (_handle)
        # 144 LOAD_FAST                2 (bsize)
        # 318         146 LOAD_CONST               3 (True)
        # 317         148 KW_NAMES                 4
        # 150 PRECALL                  3
        # 154 CALL                     3
        # 164 UNPACK_SEQUENCE          2
        # 168 STORE_FAST               3 (ov)
        # 170 STORE_FAST               4 (err)
        # 319         172 NOP
        # 320         174 LOAD_FAST                4 (err)
        # 176 LOAD_GLOBAL              8 (_winapi)
        # 188 LOAD_ATTR                7 (ERROR_IO_PENDING)
        # 198 COMPARE_OP               2 (==)
        # 204 POP_JUMP_FORWARD_IF_FALSE    46 (to 298)
        # 321         206 LOAD_GLOBAL              9 (NULL + _winapi)
        # 218 LOAD_ATTR                8 (WaitForMultipleObjects)
        # 322         228 LOAD_FAST                3 (ov)
        # 230 LOAD_ATTR                9 (event)
        # 240 BUILD_LIST               1
        # 242 LOAD_CONST               1 (False)
        # 244 LOAD_GLOBAL             20 (INFINITE)
        # 321         256 PRECALL                  3
        # 260 CALL                     3
        # 270 STORE_FAST               5 (waitres)
        # 323         272 LOAD_FAST                5 (waitres)
        # 274 LOAD_GLOBAL             22 (WAIT_OBJECT_0)
        # 286 COMPARE_OP               2 (==)
        # 292 POP_JUMP_FORWARD_IF_TRUE     2 (to 298)
        # 294 LOAD_ASSERTION_ERROR
        # 296 RAISE_VARARGS            1
        # >>  298 JUMP_FORWARD            26 (to 352)
        # >>  300 PUSH_EXC_INFO
        # 324         302 POP_TOP
        # 325         304 LOAD_FAST                3 (ov)
        # 306 LOAD_METHOD             12 (cancel)
        # 328 PRECALL                  0
        # 332 CALL                     0
        # 342 POP_TOP
        # 326         344 RAISE_VARARGS            0
        # >>  346 COPY                     3
        # 348 POP_EXCEPT
        # 350 RERAISE                  1
        # 328     >>  352 LOAD_FAST                3 (ov)
        # 354 LOAD_METHOD             13 (GetOverlappedResult)
        # 376 LOAD_CONST               3 (True)
        # 378 PRECALL                  1
        # 382 CALL                     1
        # 392 UNPACK_SEQUENCE          2
        # 396 STORE_FAST               6 (nread)
        # 398 STORE_FAST               4 (err)
        # 329         400 LOAD_FAST                4 (err)
        # 402 LOAD_CONST               5 (0)
        # 404 COMPARE_OP               2 (==)
        # 410 POP_JUMP_FORWARD_IF_FALSE    60 (to 532)
        # 330         412 LOAD_GLOBAL              3 (NULL + io)
        # 424 LOAD_ATTR                2 (BytesIO)
        # 434 PRECALL                  0
        # 438 CALL                     0
        # 448 STORE_FAST               7 (f)
        # 331         450 LOAD_FAST                7 (f)
        # 452 LOAD_METHOD             14 (write)
        # 474 LOAD_FAST                3 (ov)
        # 476 LOAD_METHOD             15 (getbuffer)
        # 498 PRECALL                  0
        # 502 CALL                     0
        # 512 PRECALL                  1
        # 516 CALL                     1
        # 526 POP_TOP
        # 332         528 LOAD_FAST                7 (f)
        # 530 RETURN_VALUE
        # 333     >>  532 LOAD_FAST                4 (err)
        # 534 LOAD_GLOBAL              8 (_winapi)
        # 546 LOAD_ATTR               16 (ERROR_MORE_DATA)
        # 556 COMPARE_OP               2 (==)
        # 562 POP_JUMP_FORWARD_IF_FALSE    22 (to 608)
        # 334         564 LOAD_FAST                0 (self)
        # 566 LOAD_METHOD             17 (_get_more_data)
        # 588 LOAD_FAST                3 (ov)
        # 590 LOAD_FAST                1 (maxsize)
        # 592 PRECALL                  2
        # 596 CALL                     2
        # 606 RETURN_VALUE
        # 333     >>  608 JUMP_FORWARD           141 (to 892)
        # >>  610 PUSH_EXC_INFO
        # 328         612 LOAD_FAST                3 (ov)
        # 614 LOAD_METHOD             13 (GetOverlappedResult)
        # 636 LOAD_CONST               3 (True)
        # 638 PRECALL                  1
        # 642 CALL                     1
        # 652 UNPACK_SEQUENCE          2
        # 656 STORE_FAST               6 (nread)
        # 658 STORE_FAST               4 (err)
        # 329         660 LOAD_FAST                4 (err)
        # 662 LOAD_CONST               5 (0)
        # 664 COMPARE_OP               2 (==)
        # 670 POP_JUMP_FORWARD_IF_FALSE    64 (to 800)
        # 330         672 LOAD_GLOBAL              3 (NULL + io)
        # 684 LOAD_ATTR                2 (BytesIO)
        # 694 PRECALL                  0
        # 698 CALL                     0
        # 708 STORE_FAST               7 (f)
        # 331         710 LOAD_FAST                7 (f)
        # 712 LOAD_METHOD             14 (write)
        # 734 LOAD_FAST                3 (ov)
        # 736 LOAD_METHOD             15 (getbuffer)
        # 758 PRECALL                  0
        # 762 CALL                     0
        # 772 PRECALL                  1
        # 776 CALL                     1
        # 786 POP_TOP
        # 332         788 LOAD_FAST                7 (f)
        # 790 SWAP                     2
        # 792 POP_TOP
        # 794 SWAP                     2
        # 796 POP_EXCEPT
        # 798 RETURN_VALUE
        # 333     >>  800 LOAD_FAST                4 (err)
        # 802 LOAD_GLOBAL              8 (_winapi)
        # 814 LOAD_ATTR               16 (ERROR_MORE_DATA)
        # 824 COMPARE_OP               2 (==)
        # 830 POP_JUMP_FORWARD_IF_FALSE    26 (to 884)
        # 334         832 LOAD_FAST                0 (self)
        # 834 LOAD_METHOD             17 (_get_more_data)
        # 856 LOAD_FAST                3 (ov)
        # 858 LOAD_FAST                1 (maxsize)
        # 860 PRECALL                  2
        # 864 CALL                     2
        # 874 SWAP                     2
        # 876 POP_TOP
        # 878 SWAP                     2
        # 880 POP_EXCEPT
        # 882 RETURN_VALUE
        # >>  884 RERAISE                  0
        # >>  886 COPY                     3
        # 888 POP_EXCEPT
        # 890 RERAISE                  1
        # 333     >>  892 JUMP_FORWARD            47 (to 988)
        # >>  894 PUSH_EXC_INFO
        # 335         896 LOAD_GLOBAL             36 (OSError)
        # 908 CHECK_EXC_MATCH
        # 910 POP_JUMP_FORWARD_IF_FALSE    34 (to 980)
        # 912 STORE_FAST               8 (e)
        # 336         914 LOAD_FAST                8 (e)
        # 916 LOAD_ATTR               19 (winerror)
        # 926 LOAD_GLOBAL              8 (_winapi)
        # 938 LOAD_ATTR               20 (ERROR_BROKEN_PIPE)
        # 948 COMPARE_OP               2 (==)
        # 954 POP_JUMP_FORWARD_IF_FALSE     7 (to 970)
        # 337         956 LOAD_GLOBAL             42 (EOFError)
        # 968 RAISE_VARARGS            1
        # 339     >>  970 RAISE_VARARGS            0
        # >>  972 LOAD_CONST               0 (None)
        # 974 STORE_FAST               8 (e)
        # 976 DELETE_FAST              8 (e)
        # 978 RERAISE                  1
        # 335     >>  980 RERAISE                  0
        # >>  982 COPY                     3
        # 984 POP_EXCEPT
        # 986 RERAISE                  1
        # 340     >>  988 LOAD_GLOBAL             45 (NULL + RuntimeError)
        # 1000 LOAD_CONST               6 ("shouldn't get here; expected KeyboardInterrupt")
        # 1002 PRECALL                  1
        # 1006 CALL                     1
        # 1016 RAISE_VARARGS            1
        # ExceptionTable:
        # 110 to 170 -> 894 [0]
        # 174 to 296 -> 300 [0]
        # 298 to 298 -> 610 [0]
        # 300 to 344 -> 346 [1] lasti
        # 346 to 350 -> 610 [0]
        # 352 to 528 -> 894 [0]
        # 532 to 604 -> 894 [0]
        # 608 to 608 -> 894 [0]
        # 610 to 794 -> 886 [1] lasti
        # 796 to 796 -> 894 [0]
        # 800 to 878 -> 886 [1] lasti
        # 880 to 880 -> 894 [0]
        # 884 to 884 -> 886 [1] lasti
        # 886 to 890 -> 894 [0]
        # 894 to 912 -> 982 [1] lasti
        # 914 to 970 -> 972 [1] lasti
        # 972 to 980 -> 982 [1] lasti

    def _poll(self, timeout):
        # 342           0 RESUME                   0
        # 343           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_got_empty_message)
        # 14 POP_JUMP_FORWARD_IF_TRUE    35 (to 86)
        # 344          16 LOAD_GLOBAL              3 (NULL + _winapi)
        # 28 LOAD_ATTR                2 (PeekNamedPipe)
        # 38 LOAD_FAST                0 (self)
        # 40 LOAD_ATTR                3 (_handle)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 LOAD_CONST               1 (0)
        # 66 BINARY_SUBSCR
        # 76 LOAD_CONST               1 (0)
        # 78 COMPARE_OP               3 (!=)
        # 84 POP_JUMP_FORWARD_IF_FALSE     2 (to 90)
        # 345     >>   86 LOAD_CONST               2 (True)
        # 88 RETURN_VALUE
        # 346     >>   90 LOAD_GLOBAL              9 (NULL + bool)
        # 102 LOAD_GLOBAL             11 (NULL + wait)
        # 114 LOAD_FAST                0 (self)
        # 116 BUILD_LIST               1
        # 118 LOAD_FAST                1 (timeout)
        # 120 PRECALL                  2
        # 124 CALL                     2
        # 134 PRECALL                  1
        # 138 CALL                     1
        # 148 RETURN_VALUE

    def _get_more_data(self, ov, maxsize):
        # 348           0 RESUME                   0
        # 349           2 LOAD_FAST                1 (ov)
        # 4 LOAD_METHOD              0 (getbuffer)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 STORE_FAST               3 (buf)
        # 350          42 LOAD_GLOBAL              3 (NULL + io)
        # 54 LOAD_ATTR                2 (BytesIO)
        # 64 PRECALL                  0
        # 68 CALL                     0
        # 78 STORE_FAST               4 (f)
        # 351          80 LOAD_FAST                4 (f)
        # 82 LOAD_METHOD              3 (write)
        # 104 LOAD_FAST                3 (buf)
        # 106 PRECALL                  1
        # 110 CALL                     1
        # 120 POP_TOP
        # 352         122 LOAD_GLOBAL              9 (NULL + _winapi)
        # 134 LOAD_ATTR                5 (PeekNamedPipe)
        # 144 LOAD_FAST                0 (self)
        # 146 LOAD_ATTR                6 (_handle)
        # 156 PRECALL                  1
        # 160 CALL                     1
        # 170 LOAD_CONST               1 (1)
        # 172 BINARY_SUBSCR
        # 182 STORE_FAST               5 (left)
        # 353         184 LOAD_FAST                5 (left)
        # 186 LOAD_CONST               2 (0)
        # 188 COMPARE_OP               4 (>)
        # 194 POP_JUMP_FORWARD_IF_TRUE     2 (to 200)
        # 196 LOAD_ASSERTION_ERROR
        # 198 RAISE_VARARGS            1
        # 354     >>  200 LOAD_FAST                2 (maxsize)
        # 202 POP_JUMP_FORWARD_IF_NONE    42 (to 288)
        # 204 LOAD_GLOBAL             15 (NULL + len)
        # 216 LOAD_FAST                3 (buf)
        # 218 PRECALL                  1
        # 222 CALL                     1
        # 232 LOAD_FAST                5 (left)
        # 234 BINARY_OP                0 (+)
        # 238 LOAD_FAST                2 (maxsize)
        # 240 COMPARE_OP               4 (>)
        # 246 POP_JUMP_FORWARD_IF_FALSE    20 (to 288)
        # 355         248 LOAD_FAST                0 (self)
        # 250 LOAD_METHOD              8 (_bad_message_length)
        # 272 PRECALL                  0
        # 276 CALL                     0
        # 286 POP_TOP
        # 356     >>  288 LOAD_GLOBAL              9 (NULL + _winapi)
        # 300 LOAD_ATTR                9 (ReadFile)
        # 310 LOAD_FAST                0 (self)
        # 312 LOAD_ATTR                6 (_handle)
        # 322 LOAD_FAST                5 (left)
        # 324 LOAD_CONST               3 (True)
        # 326 KW_NAMES                 4
        # 328 PRECALL                  3
        # 332 CALL                     3
        # 342 UNPACK_SEQUENCE          2
        # 346 STORE_FAST               1 (ov)
        # 348 STORE_FAST               6 (err)
        # 357         350 LOAD_FAST                1 (ov)
        # 352 LOAD_METHOD             10 (GetOverlappedResult)
        # 374 LOAD_CONST               3 (True)
        # 376 PRECALL                  1
        # 380 CALL                     1
        # 390 UNPACK_SEQUENCE          2
        # 394 STORE_FAST               7 (rbytes)
        # 396 STORE_FAST               6 (err)
        # 358         398 LOAD_FAST                6 (err)
        # 400 LOAD_CONST               2 (0)
        # 402 COMPARE_OP               2 (==)
        # 408 POP_JUMP_FORWARD_IF_TRUE     2 (to 414)
        # 410 LOAD_ASSERTION_ERROR
        # 412 RAISE_VARARGS            1
        # 359     >>  414 LOAD_FAST                7 (rbytes)
        # 416 LOAD_FAST                5 (left)
        # 418 COMPARE_OP               2 (==)
        # 424 POP_JUMP_FORWARD_IF_TRUE     2 (to 430)
        # 426 LOAD_ASSERTION_ERROR
        # 428 RAISE_VARARGS            1
        # 360     >>  430 LOAD_FAST                4 (f)
        # 432 LOAD_METHOD              3 (write)
        # 454 LOAD_FAST                1 (ov)
        # 456 LOAD_METHOD              0 (getbuffer)
        # 478 PRECALL                  0
        # 482 CALL                     0
        # 492 PRECALL                  1
        # 496 CALL                     1
        # 506 POP_TOP
        # 361         508 LOAD_FAST                4 (f)
        # 510 RETURN_VALUE


class Connection:
    """Connection"""
    def _close(self, _close):
        # 371           0 RESUME                   0
        # 372           2 PUSH_NULL
        # 4 LOAD_FAST                1 (_close)
        # 6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (_handle)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 POP_TOP
        # 34 LOAD_CONST               0 (None)
        # 36 RETURN_VALUE

    def _close(self, _close):
        # 376           0 RESUME                   0
        # 377           2 PUSH_NULL
        # 4 LOAD_FAST                1 (_close)
        # 6 LOAD_FAST                0 (self)
        # 8 LOAD_ATTR                0 (_handle)
        # 18 PRECALL                  1
        # 22 CALL                     1
        # 32 POP_TOP
        # 34 LOAD_CONST               0 (None)
        # 36 RETURN_VALUE

    def _send(self, buf, write):
        # 381           0 RESUME                   0
        # 382           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_FAST                1 (buf)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               3 (remaining)
        # 383          32 NOP
        # 384     >>   34 PUSH_NULL
        # 36 LOAD_FAST                2 (write)
        # 38 LOAD_FAST                0 (self)
        # 40 LOAD_ATTR                1 (_handle)
        # 50 LOAD_FAST                1 (buf)
        # 52 PRECALL                  2
        # 56 CALL                     2
        # 66 STORE_FAST               4 (n)
        # 385          68 LOAD_FAST                3 (remaining)
        # 70 LOAD_FAST                4 (n)
        # 72 BINARY_OP               23 (-=)
        # 76 STORE_FAST               3 (remaining)
        # 386          78 LOAD_FAST                3 (remaining)
        # 80 LOAD_CONST               2 (0)
        # 82 COMPARE_OP               2 (==)
        # 88 POP_JUMP_FORWARD_IF_FALSE     2 (to 94)
        # 387          90 LOAD_CONST               0 (None)
        # 92 RETURN_VALUE
        # 388     >>   94 LOAD_FAST                1 (buf)
        # 96 LOAD_FAST                4 (n)
        # 98 LOAD_CONST               0 (None)
        # 100 BUILD_SLICE              2
        # 102 BINARY_SUBSCR
        # 112 STORE_FAST               1 (buf)
        # 383         114 JUMP_BACKWARD           41 (to 34)

    def _recv(self, size, read):
        # 390           0 RESUME                   0
        # 391           2 LOAD_GLOBAL              1 (NULL + io)
        # 14 LOAD_ATTR                1 (BytesIO)
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 STORE_FAST               3 (buf)
        # 392          40 LOAD_FAST                0 (self)
        # 42 LOAD_ATTR                2 (_handle)
        # 52 STORE_FAST               4 (handle)
        # 393          54 LOAD_FAST                1 (size)
        # 56 STORE_FAST               5 (remaining)
        # 394          58 LOAD_FAST                5 (remaining)
        # 60 LOAD_CONST               1 (0)
        # 62 COMPARE_OP               4 (>)
        # 68 POP_JUMP_FORWARD_IF_FALSE    93 (to 256)
        # 395     >>   70 PUSH_NULL
        # 72 LOAD_FAST                2 (read)
        # 74 LOAD_FAST                4 (handle)
        # 76 LOAD_FAST                5 (remaining)
        # 78 PRECALL                  2
        # 82 CALL                     2
        # 92 STORE_FAST               6 (chunk)
        # 396          94 LOAD_GLOBAL              7 (NULL + len)
        # 106 LOAD_FAST                6 (chunk)
        # 108 PRECALL                  1
        # 112 CALL                     1
        # 122 STORE_FAST               7 (n)
        # 397         124 LOAD_FAST                7 (n)
        # 126 LOAD_CONST               1 (0)
        # 128 COMPARE_OP               2 (==)
        # 134 POP_JUMP_FORWARD_IF_FALSE    28 (to 192)
        # 398         136 LOAD_FAST                5 (remaining)
        # 138 LOAD_FAST                1 (size)
        # 140 COMPARE_OP               2 (==)
        # 146 POP_JUMP_FORWARD_IF_FALSE     7 (to 162)
        # 399         148 LOAD_GLOBAL              8 (EOFError)
        # 160 RAISE_VARARGS            1
        # 401     >>  162 LOAD_GLOBAL             11 (NULL + OSError)
        # 174 LOAD_CONST               2 ('got end of file during message')
        # 176 PRECALL                  1
        # 180 CALL                     1
        # 190 RAISE_VARARGS            1
        # 402     >>  192 LOAD_FAST                3 (buf)
        # 194 LOAD_METHOD              6 (write)
        # 216 LOAD_FAST                6 (chunk)
        # 218 PRECALL                  1
        # 222 CALL                     1
        # 232 POP_TOP
        # 403         234 LOAD_FAST                5 (remaining)
        # 236 LOAD_FAST                7 (n)
        # 238 BINARY_OP               23 (-=)
        # 242 STORE_FAST               5 (remaining)
        # 394         244 LOAD_FAST                5 (remaining)
        # 246 LOAD_CONST               1 (0)
        # 248 COMPARE_OP               4 (>)
        # 254 POP_JUMP_BACKWARD_IF_TRUE    93 (to 70)
        # 404     >>  256 LOAD_FAST                3 (buf)
        # 258 RETURN_VALUE

    def _send_bytes(self, buf):
        # 406           0 RESUME                   0
        # 407           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_FAST                1 (buf)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 STORE_FAST               2 (n)
        # 408          32 LOAD_FAST                2 (n)
        # 34 LOAD_CONST               1 (2147483647)
        # 36 COMPARE_OP               4 (>)
        # 42 POP_JUMP_FORWARD_IF_FALSE   107 (to 258)
        # 409          44 LOAD_GLOBAL              3 (NULL + struct)
        # 56 LOAD_ATTR                2 (pack)
        # 66 LOAD_CONST               2 ('!i')
        # 68 LOAD_CONST               3 (-1)
        # 70 PRECALL                  2
        # 74 CALL                     2
        # 84 STORE_FAST               3 (pre_header)
        # 410          86 LOAD_GLOBAL              3 (NULL + struct)
        # 98 LOAD_ATTR                2 (pack)
        # 108 LOAD_CONST               4 ('!Q')
        # 110 LOAD_FAST                2 (n)
        # 112 PRECALL                  2
        # 116 CALL                     2
        # 126 STORE_FAST               4 (header)
        # 411         128 LOAD_FAST                0 (self)
        # 130 LOAD_METHOD              3 (_send)
        # 152 LOAD_FAST                3 (pre_header)
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 168 POP_TOP
        # 412         170 LOAD_FAST                0 (self)
        # 172 LOAD_METHOD              3 (_send)
        # 194 LOAD_FAST                4 (header)
        # 196 PRECALL                  1
        # 200 CALL                     1
        # 210 POP_TOP
        # 413         212 LOAD_FAST                0 (self)
        # 214 LOAD_METHOD              3 (_send)
        # 236 LOAD_FAST                1 (buf)
        # 238 PRECALL                  1
        # 242 CALL                     1
        # 252 POP_TOP
        # 254 LOAD_CONST               0 (None)
        # 256 RETURN_VALUE
        # 416     >>  258 LOAD_GLOBAL              3 (NULL + struct)
        # 270 LOAD_ATTR                2 (pack)
        # 280 LOAD_CONST               2 ('!i')
        # 282 LOAD_FAST                2 (n)
        # 284 PRECALL                  2
        # 288 CALL                     2
        # 298 STORE_FAST               4 (header)
        # 417         300 LOAD_FAST                2 (n)
        # 302 LOAD_CONST               5 (16384)
        # 304 COMPARE_OP               4 (>)
        # 310 POP_JUMP_FORWARD_IF_FALSE    44 (to 400)
        # 420         312 LOAD_FAST                0 (self)
        # 314 LOAD_METHOD              3 (_send)
        # 336 LOAD_FAST                4 (header)
        # 338 PRECALL                  1
        # 342 CALL                     1
        # 352 POP_TOP
        # 421         354 LOAD_FAST                0 (self)
        # 356 LOAD_METHOD              3 (_send)
        # 378 LOAD_FAST                1 (buf)
        # 380 PRECALL                  1
        # 384 CALL                     1
        # 394 POP_TOP
        # 396 LOAD_CONST               0 (None)
        # 398 RETURN_VALUE
        # 427     >>  400 LOAD_FAST                0 (self)
        # 402 LOAD_METHOD              3 (_send)
        # 424 LOAD_FAST                4 (header)
        # 426 LOAD_FAST                1 (buf)
        # 428 BINARY_OP                0 (+)
        # 432 PRECALL                  1
        # 436 CALL                     1
        # 446 POP_TOP
        # 448 LOAD_CONST               0 (None)
        # 450 RETURN_VALUE

    def _recv_bytes(self, maxsize):
        # 429           0 RESUME                   0
        # 430           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_recv)
        # 26 LOAD_CONST               1 (4)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 STORE_FAST               2 (buf)
        # 431          44 LOAD_GLOBAL              3 (NULL + struct)
        # 56 LOAD_ATTR                2 (unpack)
        # 66 LOAD_CONST               2 ('!i')
        # 68 LOAD_FAST                2 (buf)
        # 70 LOAD_METHOD              3 (getvalue)
        # 92 PRECALL                  0
        # 96 CALL                     0
        # 106 PRECALL                  2
        # 110 CALL                     2
        # 120 UNPACK_SEQUENCE          1
        # 124 STORE_FAST               3 (size)
        # 432         126 LOAD_FAST                3 (size)
        # 128 LOAD_CONST               3 (-1)
        # 130 COMPARE_OP               2 (==)
        # 136 POP_JUMP_FORWARD_IF_FALSE    62 (to 262)
        # 433         138 LOAD_FAST                0 (self)
        # 140 LOAD_METHOD              0 (_recv)
        # 162 LOAD_CONST               4 (8)
        # 164 PRECALL                  1
        # 168 CALL                     1
        # 178 STORE_FAST               2 (buf)
        # 434         180 LOAD_GLOBAL              3 (NULL + struct)
        # 192 LOAD_ATTR                2 (unpack)
        # 202 LOAD_CONST               5 ('!Q')
        # 204 LOAD_FAST                2 (buf)
        # 206 LOAD_METHOD              3 (getvalue)
        # 228 PRECALL                  0
        # 232 CALL                     0
        # 242 PRECALL                  2
        # 246 CALL                     2
        # 256 UNPACK_SEQUENCE          1
        # 260 STORE_FAST               3 (size)
        # 435     >>  262 LOAD_FAST                1 (maxsize)
        # 264 POP_JUMP_FORWARD_IF_NONE     8 (to 282)
        # 266 LOAD_FAST                3 (size)
        # 268 LOAD_FAST                1 (maxsize)
        # 270 COMPARE_OP               4 (>)
        # 276 POP_JUMP_FORWARD_IF_FALSE     2 (to 282)
        # 436         278 LOAD_CONST               0 (None)
        # 280 RETURN_VALUE
        # 437     >>  282 LOAD_FAST                0 (self)
        # 284 LOAD_METHOD              0 (_recv)
        # 306 LOAD_FAST                3 (size)
        # 308 PRECALL                  1
        # 312 CALL                     1
        # 322 RETURN_VALUE

    def _poll(self, timeout):
        # 439           0 RESUME                   0
        # 440           2 LOAD_GLOBAL              1 (NULL + wait)
        # 14 LOAD_FAST                0 (self)
        # 16 BUILD_LIST               1
        # 18 LOAD_FAST                1 (timeout)
        # 20 PRECALL                  2
        # 24 CALL                     2
        # 34 STORE_FAST               2 (r)
        # 441          36 LOAD_GLOBAL              3 (NULL + bool)
        # 48 LOAD_FAST                2 (r)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 RETURN_VALUE


class Listener:
    """Listener"""
    def __init__(self, address, family, backlog, authkey):
        # 455           0 RESUME                   0
        # 456           2 LOAD_FAST                2 (family)
        # 4 JUMP_IF_TRUE_OR_POP     23 (to 52)
        # 6 LOAD_FAST                1 (address)
        # 8 POP_JUMP_FORWARD_IF_FALSE    15 (to 40)
        # 10 LOAD_GLOBAL              1 (NULL + address_type)
        # 22 LOAD_FAST                1 (address)
        # 24 PRECALL                  1
        # 28 CALL                     1
        # 38 JUMP_IF_TRUE_OR_POP      6 (to 52)
        # 457     >>   40 LOAD_GLOBAL              2 (default_family)
        # 456     >>   52 STORE_FAST               2 (family)
        # 458          54 LOAD_FAST                1 (address)
        # 56 JUMP_IF_TRUE_OR_POP     14 (to 86)
        # 58 LOAD_GLOBAL              5 (NULL + arbitrary_address)
        # 70 LOAD_FAST                2 (family)
        # 72 PRECALL                  1
        # 76 CALL                     1
        # >>   86 STORE_FAST               1 (address)
        # 460          88 LOAD_GLOBAL              7 (NULL + _validate_family)
        # 100 LOAD_FAST                2 (family)
        # 102 PRECALL                  1
        # 106 CALL                     1
        # 116 POP_TOP
        # 461         118 LOAD_FAST                2 (family)
        # 120 LOAD_CONST               1 ('AF_PIPE')
        # 122 COMPARE_OP               2 (==)
        # 128 POP_JUMP_FORWARD_IF_FALSE    22 (to 174)
        # 462         130 LOAD_GLOBAL              9 (NULL + PipeListener)
        # 142 LOAD_FAST                1 (address)
        # 144 LOAD_FAST                3 (backlog)
        # 146 PRECALL                  2
        # 150 CALL                     2
        # 160 LOAD_FAST                0 (self)
        # 162 STORE_ATTR               5 (_listener)
        # 172 JUMP_FORWARD            22 (to 218)
        # 464     >>  174 LOAD_GLOBAL             13 (NULL + SocketListener)
        # 186 LOAD_FAST                1 (address)
        # 188 LOAD_FAST                2 (family)
        # 190 LOAD_FAST                3 (backlog)
        # 192 PRECALL                  3
        # 196 CALL                     3
        # 206 LOAD_FAST                0 (self)
        # 208 STORE_ATTR               5 (_listener)
        # 466     >>  218 LOAD_FAST                4 (authkey)
        # 220 POP_JUMP_FORWARD_IF_NONE    36 (to 294)
        # 222 LOAD_GLOBAL             15 (NULL + isinstance)
        # 234 LOAD_FAST                4 (authkey)
        # 236 LOAD_GLOBAL             16 (bytes)
        # 248 PRECALL                  2
        # 252 CALL                     2
        # 262 POP_JUMP_FORWARD_IF_TRUE    15 (to 294)
        # 467         264 LOAD_GLOBAL             19 (NULL + TypeError)
        # 276 LOAD_CONST               2 ('authkey should be a byte string')
        # 278 PRECALL                  1
        # 282 CALL                     1
        # 292 RAISE_VARARGS            1
        # 469     >>  294 LOAD_FAST                4 (authkey)
        # 296 LOAD_FAST                0 (self)
        # 298 STORE_ATTR              10 (_authkey)
        # 308 LOAD_CONST               0 (None)
        # 310 RETURN_VALUE

    def accept(self):
        """
        Accept a connection on the bound socket or named pipe of `self`.

        Returns a `Connection` object.
        """
        # 471           0 RESUME                   0
        # 477           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_listener)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 46)
        # 478          16 LOAD_GLOBAL              3 (NULL + OSError)
        # 28 LOAD_CONST               2 ('listener is closed')
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RAISE_VARARGS            1
        # 479     >>   46 LOAD_FAST                0 (self)
        # 48 LOAD_ATTR                0 (_listener)
        # 58 LOAD_METHOD              2 (accept)
        # 80 PRECALL                  0
        # 84 CALL                     0
        # 94 STORE_FAST               1 (c)
        # 480          96 LOAD_FAST                0 (self)
        # 98 LOAD_ATTR                3 (_authkey)
        # 108 POP_JUMP_FORWARD_IF_FALSE    42 (to 194)
        # 481         110 LOAD_GLOBAL              9 (NULL + deliver_challenge)
        # 122 LOAD_FAST                1 (c)
        # 124 LOAD_FAST                0 (self)
        # 126 LOAD_ATTR                3 (_authkey)
        # 136 PRECALL                  2
        # 140 CALL                     2
        # 150 POP_TOP
        # 482         152 LOAD_GLOBAL             11 (NULL + answer_challenge)
        # 164 LOAD_FAST                1 (c)
        # 166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                3 (_authkey)
        # 178 PRECALL                  2
        # 182 CALL                     2
        # 192 POP_TOP
        # 483     >>  194 LOAD_FAST                1 (c)
        # 196 RETURN_VALUE

    def close(self):
        """
        Close the bound socket or named pipe of `self`.
        """
        # 485           0 RESUME                   0
        # 489           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_listener)
        # 14 STORE_FAST               1 (listener)
        # 490          16 LOAD_FAST                1 (listener)
        # 18 POP_JUMP_FORWARD_IF_NONE    29 (to 78)
        # 491          20 LOAD_CONST               1 (None)
        # 22 LOAD_FAST                0 (self)
        # 24 STORE_ATTR               0 (_listener)
        # 492          34 LOAD_FAST                1 (listener)
        # 36 LOAD_METHOD              1 (close)
        # 58 PRECALL                  0
        # 62 CALL                     0
        # 72 POP_TOP
        # 74 LOAD_CONST               1 (None)
        # 76 RETURN_VALUE
        # 490     >>   78 LOAD_CONST               1 (None)
        # 80 RETURN_VALUE

    def address(self):
        # 494           0 RESUME                   0
        # 496           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_listener)
        # 14 LOAD_ATTR                1 (_address)
        # 24 RETURN_VALUE

    def last_accepted(self):
        # 498           0 RESUME                   0
        # 500           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_listener)
        # 14 LOAD_ATTR                1 (_last_accepted)
        # 24 RETURN_VALUE

    def __enter__(self):
        # 502           0 RESUME                   0
        # 503           2 LOAD_FAST                0 (self)
        # 4 RETURN_VALUE

    def __exit__(self, exc_type, exc_value, exc_tb):
        # 505           0 RESUME                   0
        # 506           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (close)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE


def Client(address, family, authkey):
    """
    Returns a connection to the address of a `Listener`
    """
    # 509           0 RESUME                   0
    # 513           2 LOAD_FAST                1 (family)
    # 4 JUMP_IF_TRUE_OR_POP     14 (to 34)
    # 6 LOAD_GLOBAL              1 (NULL + address_type)
    # 18 LOAD_FAST                0 (address)
    # 20 PRECALL                  1
    # 24 CALL                     1
    # >>   34 STORE_FAST               1 (family)
    # 514          36 LOAD_GLOBAL              3 (NULL + _validate_family)
    # 48 LOAD_FAST                1 (family)
    # 50 PRECALL                  1
    # 54 CALL                     1
    # 64 POP_TOP
    # 515          66 LOAD_FAST                1 (family)
    # 68 LOAD_CONST               1 ('AF_PIPE')
    # 70 COMPARE_OP               2 (==)
    # 76 POP_JUMP_FORWARD_IF_FALSE    16 (to 110)
    # 516          78 LOAD_GLOBAL              5 (NULL + PipeClient)
    # 90 LOAD_FAST                0 (address)
    # 92 PRECALL                  1
    # 96 CALL                     1
    # 106 STORE_FAST               3 (c)
    # 108 JUMP_FORWARD            15 (to 140)
    # 518     >>  110 LOAD_GLOBAL              7 (NULL + SocketClient)
    # 122 LOAD_FAST                0 (address)
    # 124 PRECALL                  1
    # 128 CALL                     1
    # 138 STORE_FAST               3 (c)
    # 520     >>  140 LOAD_FAST                2 (authkey)
    # 142 POP_JUMP_FORWARD_IF_NONE    36 (to 216)
    # 144 LOAD_GLOBAL              9 (NULL + isinstance)
    # 156 LOAD_FAST                2 (authkey)
    # 158 LOAD_GLOBAL             10 (bytes)
    # 170 PRECALL                  2
    # 174 CALL                     2
    # 184 POP_JUMP_FORWARD_IF_TRUE    15 (to 216)
    # 521         186 LOAD_GLOBAL             13 (NULL + TypeError)
    # 198 LOAD_CONST               3 ('authkey should be a byte string')
    # 200 PRECALL                  1
    # 204 CALL                     1
    # 214 RAISE_VARARGS            1
    # 523     >>  216 LOAD_FAST                2 (authkey)
    # 218 POP_JUMP_FORWARD_IF_NONE    32 (to 284)
    # 524         220 LOAD_GLOBAL             15 (NULL + answer_challenge)
    # 232 LOAD_FAST                3 (c)
    # 234 LOAD_FAST                2 (authkey)
    # 236 PRECALL                  2
    # 240 CALL                     2
    # 250 POP_TOP
    # 525         252 LOAD_GLOBAL             17 (NULL + deliver_challenge)
    # 264 LOAD_FAST                3 (c)
    # 266 LOAD_FAST                2 (authkey)
    # 268 PRECALL                  2
    # 272 CALL                     2
    # 282 POP_TOP
    # 527     >>  284 LOAD_FAST                3 (c)
    # 286 RETURN_VALUE

def Pipe(duplex):
    """
        Returns pair of connection objects at either end of a pipe
        """
    # 532           0 RESUME                   0
    # 536           2 LOAD_FAST                0 (duplex)
    # 4 POP_JUMP_FORWARD_IF_FALSE   131 (to 268)
    # 537           6 LOAD_GLOBAL              1 (NULL + socket)
    # 18 LOAD_ATTR                1 (socketpair)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 UNPACK_SEQUENCE          2
    # 46 STORE_FAST               1 (s1)
    # 48 STORE_FAST               2 (s2)
    # 538          50 LOAD_FAST                1 (s1)
    # 52 LOAD_METHOD              2 (setblocking)
    # 74 LOAD_CONST               1 (True)
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 POP_TOP
    # 539          92 LOAD_FAST                2 (s2)
    # 94 LOAD_METHOD              2 (setblocking)
    # 116 LOAD_CONST               1 (True)
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 POP_TOP
    # 540         134 LOAD_GLOBAL              7 (NULL + Connection)
    # 146 LOAD_FAST                1 (s1)
    # 148 LOAD_METHOD              4 (detach)
    # 170 PRECALL                  0
    # 174 CALL                     0
    # 184 PRECALL                  1
    # 188 CALL                     1
    # 198 STORE_FAST               3 (c1)
    # 541         200 LOAD_GLOBAL              7 (NULL + Connection)
    # 212 LOAD_FAST                2 (s2)
    # 214 LOAD_METHOD              4 (detach)
    # 236 PRECALL                  0
    # 240 CALL                     0
    # 250 PRECALL                  1
    # 254 CALL                     1
    # 264 STORE_FAST               4 (c2)
    # 266 JUMP_FORWARD            56 (to 380)
    # 543     >>  268 LOAD_GLOBAL             11 (NULL + os)
    # 280 LOAD_ATTR                6 (pipe)
    # 290 PRECALL                  0
    # 294 CALL                     0
    # 304 UNPACK_SEQUENCE          2
    # 308 STORE_FAST               5 (fd1)
    # 310 STORE_FAST               6 (fd2)
    # 544         312 LOAD_GLOBAL              7 (NULL + Connection)
    # 324 LOAD_FAST                5 (fd1)
    # 326 LOAD_CONST               2 (False)
    # 328 KW_NAMES                 3
    # 330 PRECALL                  2
    # 334 CALL                     2
    # 344 STORE_FAST               3 (c1)
    # 545         346 LOAD_GLOBAL              7 (NULL + Connection)
    # 358 LOAD_FAST                6 (fd2)
    # 360 LOAD_CONST               2 (False)
    # 362 KW_NAMES                 4
    # 364 PRECALL                  2
    # 368 CALL                     2
    # 378 STORE_FAST               4 (c2)
    # 547     >>  380 LOAD_FAST                3 (c1)
    # 382 LOAD_FAST                4 (c2)
    # 384 BUILD_TUPLE              2
    # 386 RETURN_VALUE

class SocketListener:
    """SocketListener"""
    def __init__(self, address, family, backlog):
        # 599           0 RESUME                   0
        # 600           2 LOAD_GLOBAL              1 (NULL + socket)
        # 14 LOAD_ATTR                0 (socket)
        # 24 LOAD_GLOBAL              3 (NULL + getattr)
        # 36 LOAD_GLOBAL              0 (socket)
        # 48 LOAD_FAST                2 (family)
        # 50 PRECALL                  2
        # 54 CALL                     2
        # 64 PRECALL                  1
        # 68 CALL                     1
        # 78 LOAD_FAST                0 (self)
        # 80 STORE_ATTR               2 (_socket)
        # 601          90 NOP
        # 603          92 LOAD_GLOBAL              6 (os)
        # 104 LOAD_ATTR                4 (name)
        # 114 LOAD_CONST               1 ('posix')
        # 116 COMPARE_OP               2 (==)
        # 122 POP_JUMP_FORWARD_IF_FALSE    48 (to 220)
        # 604         124 LOAD_FAST                0 (self)
        # 126 LOAD_ATTR                2 (_socket)
        # 136 LOAD_METHOD              5 (setsockopt)
        # 158 LOAD_GLOBAL              0 (socket)
        # 170 LOAD_ATTR                6 (SOL_SOCKET)
        # 605         180 LOAD_GLOBAL              0 (socket)
        # 192 LOAD_ATTR                7 (SO_REUSEADDR)
        # 202 LOAD_CONST               2 (1)
        # 604         204 PRECALL                  3
        # 208 CALL                     3
        # 218 POP_TOP
        # 606     >>  220 LOAD_FAST                0 (self)
        # 222 LOAD_ATTR                2 (_socket)
        # 232 LOAD_METHOD              8 (setblocking)
        # 254 LOAD_CONST               3 (True)
        # 256 PRECALL                  1
        # 260 CALL                     1
        # 270 POP_TOP
        # 607         272 LOAD_FAST                0 (self)
        # 274 LOAD_ATTR                2 (_socket)
        # 284 LOAD_METHOD              9 (bind)
        # 306 LOAD_FAST                1 (address)
        # 308 PRECALL                  1
        # 312 CALL                     1
        # 322 POP_TOP
        # 608         324 LOAD_FAST                0 (self)
        # 326 LOAD_ATTR                2 (_socket)
        # 336 LOAD_METHOD             10 (listen)
        # 358 LOAD_FAST                3 (backlog)
        # 360 PRECALL                  1
        # 364 CALL                     1
        # 374 POP_TOP
        # 609         376 LOAD_FAST                0 (self)
        # 378 LOAD_ATTR                2 (_socket)
        # 388 LOAD_METHOD             11 (getsockname)
        # 410 PRECALL                  0
        # 414 CALL                     0
        # 424 LOAD_FAST                0 (self)
        # 426 STORE_ATTR              12 (_address)
        # 436 JUMP_FORWARD            40 (to 518)
        # >>  438 PUSH_EXC_INFO
        # 610         440 LOAD_GLOBAL             26 (OSError)
        # 452 CHECK_EXC_MATCH
        # 454 POP_JUMP_FORWARD_IF_FALSE    27 (to 510)
        # 456 POP_TOP
        # 611         458 LOAD_FAST                0 (self)
        # 460 LOAD_ATTR                2 (_socket)
        # 470 LOAD_METHOD             14 (close)
        # 492 PRECALL                  0
        # 496 CALL                     0
        # 506 POP_TOP
        # 612         508 RAISE_VARARGS            0
        # 610     >>  510 RERAISE                  0
        # >>  512 COPY                     3
        # 514 POP_EXCEPT
        # 516 RERAISE                  1
        # 613     >>  518 LOAD_FAST                2 (family)
        # 520 LOAD_FAST                0 (self)
        # 522 STORE_ATTR              15 (_family)
        # 614         532 LOAD_CONST               0 (None)
        # 534 LOAD_FAST                0 (self)
        # 536 STORE_ATTR              16 (_last_accepted)
        # 616         546 LOAD_FAST                2 (family)
        # 548 LOAD_CONST               4 ('AF_UNIX')
        # 550 COMPARE_OP               2 (==)
        # 556 POP_JUMP_FORWARD_IF_FALSE    62 (to 682)
        # 558 LOAD_GLOBAL             35 (NULL + util)
        # 570 LOAD_ATTR               18 (is_abstract_socket_namespace)
        # 580 LOAD_FAST                1 (address)
        # 582 PRECALL                  1
        # 586 CALL                     1
        # 596 POP_JUMP_FORWARD_IF_TRUE    42 (to 682)
        # 618         598 LOAD_GLOBAL             35 (NULL + util)
        # 610 LOAD_ATTR               19 (Finalize)
        # 619         620 LOAD_FAST                0 (self)
        # 622 LOAD_GLOBAL              6 (os)
        # 634 LOAD_ATTR               20 (unlink)
        # 644 LOAD_FAST                1 (address)
        # 646 BUILD_TUPLE              1
        # 648 LOAD_CONST               5 (0)
        # 618         650 KW_NAMES                 6
        # 652 PRECALL                  4
        # 656 CALL                     4
        # 666 LOAD_FAST                0 (self)
        # 668 STORE_ATTR              21 (_unlink)
        # 678 LOAD_CONST               0 (None)
        # 680 RETURN_VALUE
        # 622     >>  682 LOAD_CONST               0 (None)
        # 684 LOAD_FAST                0 (self)
        # 686 STORE_ATTR              21 (_unlink)
        # 696 LOAD_CONST               0 (None)
        # 698 RETURN_VALUE
        # ExceptionTable:
        # 92 to 434 -> 438 [0]
        # 438 to 510 -> 512 [1] lasti

    def accept(self):
        # 624           0 RESUME                   0
        # 625           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_socket)
        # 14 LOAD_METHOD              1 (accept)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 UNPACK_SEQUENCE          2
        # 54 STORE_FAST               1 (s)
        # 56 LOAD_FAST                0 (self)
        # 58 STORE_ATTR               2 (_last_accepted)
        # 626          68 LOAD_FAST                1 (s)
        # 70 LOAD_METHOD              3 (setblocking)
        # 92 LOAD_CONST               1 (True)
        # 94 PRECALL                  1
        # 98 CALL                     1
        # 108 POP_TOP
        # 627         110 LOAD_GLOBAL              9 (NULL + Connection)
        # 122 LOAD_FAST                1 (s)
        # 124 LOAD_METHOD              5 (detach)
        # 146 PRECALL                  0
        # 150 CALL                     0
        # 160 PRECALL                  1
        # 164 CALL                     1
        # 174 RETURN_VALUE

    def close(self):
        # 629           0 RESUME                   0
        # 630           2 NOP
        # 631           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (_socket)
        # 16 LOAD_METHOD              1 (close)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 POP_TOP
        # 633          54 LOAD_FAST                0 (self)
        # 56 LOAD_ATTR                2 (_unlink)
        # 66 STORE_FAST               1 (unlink)
        # 634          68 LOAD_FAST                1 (unlink)
        # 70 POP_JUMP_FORWARD_IF_NONE    19 (to 110)
        # 635          72 LOAD_CONST               0 (None)
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               2 (_unlink)
        # 636          86 PUSH_NULL
        # 88 LOAD_FAST                1 (unlink)
        # 90 PRECALL                  0
        # 94 CALL                     0
        # 104 POP_TOP
        # 106 LOAD_CONST               0 (None)
        # 108 RETURN_VALUE
        # 634     >>  110 LOAD_CONST               0 (None)
        # 112 RETURN_VALUE
        # >>  114 PUSH_EXC_INFO
        # 633         116 LOAD_FAST                0 (self)
        # 118 LOAD_ATTR                2 (_unlink)
        # 128 STORE_FAST               1 (unlink)
        # 634         130 LOAD_FAST                1 (unlink)
        # 132 POP_JUMP_FORWARD_IF_NONE    18 (to 170)
        # 635         134 LOAD_CONST               0 (None)
        # 136 LOAD_FAST                0 (self)
        # 138 STORE_ATTR               2 (_unlink)
        # 636         148 PUSH_NULL
        # 150 LOAD_FAST                1 (unlink)
        # 152 PRECALL                  0
        # 156 CALL                     0
        # 166 POP_TOP
        # 168 RERAISE                  0
        # 634     >>  170 RERAISE                  0
        # >>  172 COPY                     3
        # 174 POP_EXCEPT
        # 176 RERAISE                  1
        # ExceptionTable:
        # 4 to 52 -> 114 [0]
        # 114 to 170 -> 172 [1] lasti


def SocketClient(address):
    """
    Return a connection object connected to the socket given by `address`
    """
    # 639           0 RESUME                   0
    # 643           2 LOAD_GLOBAL              1 (NULL + address_type)
    # 14 LOAD_FAST                0 (address)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               1 (family)
    # 644          32 LOAD_GLOBAL              3 (NULL + socket)
    # 44 LOAD_ATTR                1 (socket)
    # 54 LOAD_GLOBAL              5 (NULL + getattr)
    # 66 LOAD_GLOBAL              2 (socket)
    # 78 LOAD_FAST                1 (family)
    # 80 PRECALL                  2
    # 84 CALL                     2
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 BEFORE_WITH
    # 110 STORE_FAST               2 (s)
    # 645         112 LOAD_FAST                2 (s)
    # 114 LOAD_METHOD              3 (setblocking)
    # 136 LOAD_CONST               1 (True)
    # 138 PRECALL                  1
    # 142 CALL                     1
    # 152 POP_TOP
    # 646         154 LOAD_FAST                2 (s)
    # 156 LOAD_METHOD              4 (connect)
    # 178 LOAD_FAST                0 (address)
    # 180 PRECALL                  1
    # 184 CALL                     1
    # 194 POP_TOP
    # 647         196 LOAD_GLOBAL             11 (NULL + Connection)
    # 208 LOAD_FAST                2 (s)
    # 210 LOAD_METHOD              6 (detach)
    # 232 PRECALL                  0
    # 236 CALL                     0
    # 246 PRECALL                  1
    # 250 CALL                     1
    # 644         260 SWAP                     2
    # 262 LOAD_CONST               2 (None)
    # 264 LOAD_CONST               2 (None)
    # 266 LOAD_CONST               2 (None)
    # 268 PRECALL                  2
    # 272 CALL                     2
    # 282 POP_TOP
    # 284 RETURN_VALUE
    # >>  286 PUSH_EXC_INFO
    # 288 WITH_EXCEPT_START
    # 290 POP_JUMP_FORWARD_IF_TRUE     4 (to 300)
    # 292 RERAISE                  2
    # >>  294 COPY                     3
    # 296 POP_EXCEPT
    # 298 RERAISE                  1
    # >>  300 POP_TOP
    # 302 POP_EXCEPT
    # 304 POP_TOP
    # 306 POP_TOP
    # 308 LOAD_CONST               2 (None)
    # 310 RETURN_VALUE
    # ExceptionTable:
    # 110 to 258 -> 286 [1] lasti
    # 286 to 292 -> 294 [3] lasti
    # 300 to 300 -> 294 [3] lasti

class PipeListener:
    """PipeListener"""
    def __init__(self, address, backlog):
        # 659           0 RESUME                   0
        # 660           2 LOAD_FAST                1 (address)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (_address)
        # 661          16 LOAD_FAST                0 (self)
        # 18 LOAD_METHOD              1 (_new_handle)
        # 40 LOAD_CONST               1 (True)
        # 42 KW_NAMES                 2
        # 44 PRECALL                  1
        # 48 CALL                     1
        # 58 BUILD_LIST               1
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               2 (_handle_queue)
        # 663          72 LOAD_CONST               0 (None)
        # 74 LOAD_FAST                0 (self)
        # 76 STORE_ATTR               3 (_last_accepted)
        # 664          86 LOAD_GLOBAL              9 (NULL + util)
        # 98 LOAD_ATTR                5 (sub_debug)
        # 108 LOAD_CONST               3 ('listener created with address=%r')
        # 110 LOAD_FAST                0 (self)
        # 112 LOAD_ATTR                0 (_address)
        # 122 PRECALL                  2
        # 126 CALL                     2
        # 136 POP_TOP
        # 665         138 LOAD_GLOBAL              9 (NULL + util)
        # 150 LOAD_ATTR                6 (Finalize)
        # 666         160 LOAD_FAST                0 (self)
        # 162 LOAD_GLOBAL             14 (PipeListener)
        # 174 LOAD_ATTR                8 (_finalize_pipe_listener)
        # 667         184 LOAD_FAST                0 (self)
        # 186 LOAD_ATTR                2 (_handle_queue)
        # 196 LOAD_FAST                0 (self)
        # 198 LOAD_ATTR                0 (_address)
        # 208 BUILD_TUPLE              2
        # 210 LOAD_CONST               4 (0)
        # 665         212 KW_NAMES                 5
        # 214 PRECALL                  4
        # 218 CALL                     4
        # 228 LOAD_FAST                0 (self)
        # 230 STORE_ATTR               9 (close)
        # 240 LOAD_CONST               0 (None)
        # 242 RETURN_VALUE

    def _new_handle(self, first):
        # 670           0 RESUME                   0
        # 671           2 LOAD_GLOBAL              0 (_winapi)
        # 14 LOAD_ATTR                1 (PIPE_ACCESS_DUPLEX)
        # 24 LOAD_GLOBAL              0 (_winapi)
        # 36 LOAD_ATTR                2 (FILE_FLAG_OVERLAPPED)
        # 46 BINARY_OP                7 (|)
        # 50 STORE_FAST               2 (flags)
        # 672          52 LOAD_FAST                1 (first)
        # 54 POP_JUMP_FORWARD_IF_FALSE    15 (to 86)
        # 673          56 LOAD_FAST                2 (flags)
        # 58 LOAD_GLOBAL              0 (_winapi)
        # 70 LOAD_ATTR                3 (FILE_FLAG_FIRST_PIPE_INSTANCE)
        # 80 BINARY_OP               20 (|=)
        # 84 STORE_FAST               2 (flags)
        # 674     >>   86 LOAD_GLOBAL              1 (NULL + _winapi)
        # 98 LOAD_ATTR                4 (CreateNamedPipe)
        # 675         108 LOAD_FAST                0 (self)
        # 110 LOAD_ATTR                5 (_address)
        # 120 LOAD_FAST                2 (flags)
        # 676         122 LOAD_GLOBAL              0 (_winapi)
        # 134 LOAD_ATTR                6 (PIPE_TYPE_MESSAGE)
        # 144 LOAD_GLOBAL              0 (_winapi)
        # 156 LOAD_ATTR                7 (PIPE_READMODE_MESSAGE)
        # 166 BINARY_OP                7 (|)
        # 677         170 LOAD_GLOBAL              0 (_winapi)
        # 182 LOAD_ATTR                8 (PIPE_WAIT)
        # 676         192 BINARY_OP                7 (|)
        # 678         196 LOAD_GLOBAL              0 (_winapi)
        # 208 LOAD_ATTR                9 (PIPE_UNLIMITED_INSTANCES)
        # 218 LOAD_GLOBAL             20 (BUFSIZE)
        # 230 LOAD_GLOBAL             20 (BUFSIZE)
        # 679         242 LOAD_GLOBAL              0 (_winapi)
        # 254 LOAD_ATTR               11 (NMPWAIT_WAIT_FOREVER)
        # 264 LOAD_GLOBAL              0 (_winapi)
        # 276 LOAD_ATTR               12 (NULL)
        # 674         286 PRECALL                  8
        # 290 CALL                     8
        # 300 RETURN_VALUE

    def accept(self):
        # 682           0 RESUME                   0
        # 683           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_handle_queue)
        # 14 LOAD_METHOD              1 (append)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_METHOD              2 (_new_handle)
        # 60 PRECALL                  0
        # 64 CALL                     0
        # 74 PRECALL                  1
        # 78 CALL                     1
        # 88 POP_TOP
        # 684          90 LOAD_FAST                0 (self)
        # 92 LOAD_ATTR                0 (_handle_queue)
        # 102 LOAD_METHOD              3 (pop)
        # 124 LOAD_CONST               1 (0)
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 STORE_FAST               1 (handle)
        # 685         142 NOP
        # 686         144 LOAD_GLOBAL              9 (NULL + _winapi)
        # 156 LOAD_ATTR                5 (ConnectNamedPipe)
        # 166 LOAD_FAST                1 (handle)
        # 168 LOAD_CONST               2 (True)
        # 170 KW_NAMES                 3
        # 172 PRECALL                  2
        # 176 CALL                     2
        # 186 STORE_FAST               2 (ov)
        # 693         188 NOP
        # 694         190 LOAD_GLOBAL              9 (NULL + _winapi)
        # 202 LOAD_ATTR                6 (WaitForMultipleObjects)
        # 695         212 LOAD_FAST                2 (ov)
        # 214 LOAD_ATTR                7 (event)
        # 224 BUILD_LIST               1
        # 226 LOAD_CONST               4 (False)
        # 228 LOAD_GLOBAL             16 (INFINITE)
        # 694         240 PRECALL                  3
        # 244 CALL                     3
        # 254 STORE_FAST               3 (res)
        # 256 JUMP_FORWARD            46 (to 350)
        # >>  258 PUSH_EXC_INFO
        # 696         260 POP_TOP
        # 697         262 LOAD_FAST                2 (ov)
        # 264 LOAD_METHOD              9 (cancel)
        # 286 PRECALL                  0
        # 290 CALL                     0
        # 300 POP_TOP
        # 698         302 LOAD_GLOBAL              9 (NULL + _winapi)
        # 314 LOAD_ATTR               10 (CloseHandle)
        # 324 LOAD_FAST                1 (handle)
        # 326 PRECALL                  1
        # 330 CALL                     1
        # 340 POP_TOP
        # 699         342 RAISE_VARARGS            0
        # >>  344 COPY                     3
        # 346 POP_EXCEPT
        # 348 RERAISE                  1
        # 694     >>  350 NOP
        # 701         352 LOAD_FAST                2 (ov)
        # 354 LOAD_METHOD             11 (GetOverlappedResult)
        # 376 LOAD_CONST               2 (True)
        # 378 PRECALL                  1
        # 382 CALL                     1
        # 392 UNPACK_SEQUENCE          2
        # 396 STORE_FAST               4 (_)
        # 398 STORE_FAST               5 (err)
        # 702         400 LOAD_FAST                5 (err)
        # 402 LOAD_CONST               1 (0)
        # 404 COMPARE_OP               2 (==)
        # 410 POP_JUMP_FORWARD_IF_TRUE     2 (to 416)
        # 412 LOAD_ASSERTION_ERROR
        # 414 RAISE_VARARGS            1
        # >>  416 JUMP_FORWARD            82 (to 582)
        # >>  418 PUSH_EXC_INFO
        # 701         420 LOAD_FAST                2 (ov)
        # 422 LOAD_METHOD             11 (GetOverlappedResult)
        # 444 LOAD_CONST               2 (True)
        # 446 PRECALL                  1
        # 450 CALL                     1
        # 460 UNPACK_SEQUENCE          2
        # 464 STORE_FAST               4 (_)
        # 466 STORE_FAST               5 (err)
        # 702         468 LOAD_FAST                5 (err)
        # 470 LOAD_CONST               1 (0)
        # 472 COMPARE_OP               2 (==)
        # 478 POP_JUMP_FORWARD_IF_TRUE     2 (to 484)
        # 480 LOAD_ASSERTION_ERROR
        # 482 RAISE_VARARGS            1
        # >>  484 RERAISE                  0
        # >>  486 COPY                     3
        # 488 POP_EXCEPT
        # 490 RERAISE                  1
        # >>  492 PUSH_EXC_INFO
        # 687         494 LOAD_GLOBAL             24 (OSError)
        # 506 CHECK_EXC_MATCH
        # 508 POP_JUMP_FORWARD_IF_FALSE    32 (to 574)
        # 510 STORE_FAST               6 (e)
        # 688         512 LOAD_FAST                6 (e)
        # 514 LOAD_ATTR               13 (winerror)
        # 524 LOAD_GLOBAL              8 (_winapi)
        # 536 LOAD_ATTR               14 (ERROR_NO_DATA)
        # 546 COMPARE_OP               3 (!=)
        # 552 POP_JUMP_FORWARD_IF_FALSE     1 (to 556)
        # 689         554 RAISE_VARARGS            0
        # 688     >>  556 POP_EXCEPT
        # 558 LOAD_CONST               0 (None)
        # 560 STORE_FAST               6 (e)
        # 562 DELETE_FAST              6 (e)
        # 564 JUMP_FORWARD             8 (to 582)
        # >>  566 LOAD_CONST               0 (None)
        # 568 STORE_FAST               6 (e)
        # 570 DELETE_FAST              6 (e)
        # 572 RERAISE                  1
        # 687     >>  574 RERAISE                  0
        # >>  576 COPY                     3
        # 578 POP_EXCEPT
        # 580 RERAISE                  1
        # 703     >>  582 LOAD_GLOBAL             31 (NULL + PipeConnection)
        # 594 LOAD_FAST                1 (handle)
        # 596 PRECALL                  1
        # 600 CALL                     1
        # 610 RETURN_VALUE
        # ExceptionTable:
        # 144 to 186 -> 492 [0]
        # 190 to 254 -> 258 [0]
        # 256 to 256 -> 418 [0]
        # 258 to 342 -> 344 [1] lasti
        # 344 to 348 -> 418 [0]
        # 418 to 484 -> 486 [1] lasti
        # 492 to 510 -> 576 [1] lasti
        # 512 to 554 -> 566 [1] lasti
        # 566 to 574 -> 576 [1] lasti

    def _finalize_pipe_listener(queue, address):
        # 705           0 RESUME                   0
        # 707           2 LOAD_GLOBAL              1 (NULL + util)
        # 14 LOAD_ATTR                1 (sub_debug)
        # 24 LOAD_CONST               1 ('closing listener with address=%r')
        # 26 LOAD_FAST                1 (address)
        # 28 PRECALL                  2
        # 32 CALL                     2
        # 42 POP_TOP
        # 708          44 LOAD_FAST                0 (queue)
        # 46 GET_ITER
        # >>   48 FOR_ITER                22 (to 94)
        # 50 STORE_FAST               2 (handle)
        # 709          52 LOAD_GLOBAL              5 (NULL + _winapi)
        # 64 LOAD_ATTR                3 (CloseHandle)
        # 74 LOAD_FAST                2 (handle)
        # 76 PRECALL                  1
        # 80 CALL                     1
        # 90 POP_TOP
        # 92 JUMP_BACKWARD           23 (to 48)
        # 708     >>   94 LOAD_CONST               0 (None)
        # 96 RETURN_VALUE


def PipeClient(address):
    """
        Return a connection object connected to the pipe given by `address`
        """
    # 711           0 RESUME                   0
    # 715           2 LOAD_GLOBAL              1 (NULL + _init_timeout)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               1 (t)
    # 716          30 NOP
    # 717     >>   32 NOP
    # 718          34 LOAD_GLOBAL              3 (NULL + _winapi)
    # 46 LOAD_ATTR                2 (WaitNamedPipe)
    # 56 LOAD_FAST                0 (address)
    # 58 LOAD_CONST               2 (1000)
    # 60 PRECALL                  2
    # 64 CALL                     2
    # 74 POP_TOP
    # 719          76 LOAD_GLOBAL              3 (NULL + _winapi)
    # 88 LOAD_ATTR                3 (CreateFile)
    # 720          98 LOAD_FAST                0 (address)
    # 100 LOAD_GLOBAL              2 (_winapi)
    # 112 LOAD_ATTR                4 (GENERIC_READ)
    # 122 LOAD_GLOBAL              2 (_winapi)
    # 134 LOAD_ATTR                5 (GENERIC_WRITE)
    # 144 BINARY_OP                7 (|)
    # 721         148 LOAD_CONST               3 (0)
    # 150 LOAD_GLOBAL              2 (_winapi)
    # 162 LOAD_ATTR                6 (NULL)
    # 172 LOAD_GLOBAL              2 (_winapi)
    # 184 LOAD_ATTR                7 (OPEN_EXISTING)
    # 722         194 LOAD_GLOBAL              2 (_winapi)
    # 206 LOAD_ATTR                8 (FILE_FLAG_OVERLAPPED)
    # 216 LOAD_GLOBAL              2 (_winapi)
    # 228 LOAD_ATTR                6 (NULL)
    # 719         238 PRECALL                  7
    # 242 CALL                     7
    # 252 STORE_FAST               2 (h)
    # 729         254 JUMP_FORWARD            71 (to 398)
    # >>  256 PUSH_EXC_INFO
    # 724         258 LOAD_GLOBAL             18 (OSError)
    # 270 CHECK_EXC_MATCH
    # 272 POP_JUMP_FORWARD_IF_FALSE    57 (to 388)
    # 274 STORE_FAST               3 (e)
    # 725         276 LOAD_FAST                3 (e)
    # 278 LOAD_ATTR               10 (winerror)
    # 288 LOAD_GLOBAL              2 (_winapi)
    # 300 LOAD_ATTR               11 (ERROR_SEM_TIMEOUT)
    # 726         310 LOAD_GLOBAL              2 (_winapi)
    # 322 LOAD_ATTR               12 (ERROR_PIPE_BUSY)
    # 725         332 BUILD_TUPLE              2
    # 334 CONTAINS_OP              1
    # 336 POP_JUMP_FORWARD_IF_TRUE    15 (to 368)
    # 726         338 LOAD_GLOBAL             27 (NULL + _check_timeout)
    # 350 LOAD_FAST                1 (t)
    # 352 PRECALL                  1
    # 356 CALL                     1
    # 725         366 POP_JUMP_FORWARD_IF_FALSE     1 (to 370)
    # 727     >>  368 RAISE_VARARGS            0
    # 725     >>  370 POP_EXCEPT
    # 372 LOAD_CONST               4 (None)
    # 374 STORE_FAST               3 (e)
    # 376 DELETE_FAST              3 (e)
    # 378 JUMP_FORWARD             8 (to 396)
    # >>  380 LOAD_CONST               4 (None)
    # 382 STORE_FAST               3 (e)
    # 384 DELETE_FAST              3 (e)
    # 386 RERAISE                  1
    # 724     >>  388 RERAISE                  0
    # >>  390 COPY                     3
    # 392 POP_EXCEPT
    # 394 RERAISE                  1
    # 716     >>  396 JUMP_BACKWARD          183 (to 32)
    # 733     >>  398 LOAD_GLOBAL              3 (NULL + _winapi)
    # 410 LOAD_ATTR               14 (SetNamedPipeHandleState)
    # 734         420 LOAD_FAST                2 (h)
    # 422 LOAD_GLOBAL              2 (_winapi)
    # 434 LOAD_ATTR               15 (PIPE_READMODE_MESSAGE)
    # 444 LOAD_CONST               4 (None)
    # 446 LOAD_CONST               4 (None)
    # 733         448 PRECALL                  4
    # 452 CALL                     4
    # 462 POP_TOP
    # 736         464 LOAD_GLOBAL             33 (NULL + PipeConnection)
    # 476 LOAD_FAST                2 (h)
    # 478 PRECALL                  1
    # 482 CALL                     1
    # 492 RETURN_VALUE
    # ExceptionTable:
    # 34 to 252 -> 256 [0]
    # 256 to 274 -> 390 [1] lasti
    # 276 to 368 -> 380 [1] lasti
    # 380 to 388 -> 390 [1] lasti

def deliver_challenge(connection, authkey):
    # 748           0 RESUME                   0
    # 749           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               0 (None)
    # 6 IMPORT_NAME              0 (hmac)
    # 8 STORE_FAST               2 (hmac)
    # 750          10 LOAD_GLOBAL              3 (NULL + isinstance)
    # 22 LOAD_FAST                1 (authkey)
    # 24 LOAD_GLOBAL              4 (bytes)
    # 36 PRECALL                  2
    # 40 CALL                     2
    # 50 POP_JUMP_FORWARD_IF_TRUE    47 (to 146)
    # 751          52 LOAD_GLOBAL              7 (NULL + ValueError)
    # 752          64 LOAD_CONST               2 ('Authkey must be bytes, not {0!s}')
    # 66 LOAD_METHOD              4 (format)
    # 88 LOAD_GLOBAL             11 (NULL + type)
    # 100 LOAD_FAST                1 (authkey)
    # 102 PRECALL                  1
    # 106 CALL                     1
    # 116 PRECALL                  1
    # 120 CALL                     1
    # 751         130 PRECALL                  1
    # 134 CALL                     1
    # 144 RAISE_VARARGS            1
    # 753     >>  146 LOAD_GLOBAL             13 (NULL + os)
    # 158 LOAD_ATTR                7 (urandom)
    # 168 LOAD_GLOBAL             16 (MESSAGE_LENGTH)
    # 180 PRECALL                  1
    # 184 CALL                     1
    # 194 STORE_FAST               3 (message)
    # 754         196 LOAD_FAST                0 (connection)
    # 198 LOAD_METHOD              9 (send_bytes)
    # 220 LOAD_GLOBAL             20 (CHALLENGE)
    # 232 LOAD_FAST                3 (message)
    # 234 BINARY_OP                0 (+)
    # 238 PRECALL                  1
    # 242 CALL                     1
    # 252 POP_TOP
    # 755         254 LOAD_FAST                2 (hmac)
    # 256 LOAD_METHOD             11 (new)
    # 278 LOAD_FAST                1 (authkey)
    # 280 LOAD_FAST                3 (message)
    # 282 LOAD_CONST               3 ('md5')
    # 284 PRECALL                  3
    # 288 CALL                     3
    # 298 LOAD_METHOD             12 (digest)
    # 320 PRECALL                  0
    # 324 CALL                     0
    # 334 STORE_FAST               4 (digest)
    # 756         336 LOAD_FAST                0 (connection)
    # 338 LOAD_METHOD             13 (recv_bytes)
    # 360 LOAD_CONST               4 (256)
    # 362 PRECALL                  1
    # 366 CALL                     1
    # 376 STORE_FAST               5 (response)
    # 757         378 LOAD_FAST                5 (response)
    # 380 LOAD_FAST                4 (digest)
    # 382 COMPARE_OP               2 (==)
    # 388 POP_JUMP_FORWARD_IF_FALSE    28 (to 446)
    # 758         390 LOAD_FAST                0 (connection)
    # 392 LOAD_METHOD              9 (send_bytes)
    # 414 LOAD_GLOBAL             28 (WELCOME)
    # 426 PRECALL                  1
    # 430 CALL                     1
    # 440 POP_TOP
    # 442 LOAD_CONST               0 (None)
    # 444 RETURN_VALUE
    # 760     >>  446 LOAD_FAST                0 (connection)
    # 448 LOAD_METHOD              9 (send_bytes)
    # 470 LOAD_GLOBAL             30 (FAILURE)
    # 482 PRECALL                  1
    # 486 CALL                     1
    # 496 POP_TOP
    # 761         498 LOAD_GLOBAL             33 (NULL + AuthenticationError)
    # 510 LOAD_CONST               5 ('digest received was wrong')
    # 512 PRECALL                  1
    # 516 CALL                     1
    # 526 RAISE_VARARGS            1

def answer_challenge(connection, authkey):
    # 763           0 RESUME                   0
    # 764           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               0 (None)
    # 6 IMPORT_NAME              0 (hmac)
    # 8 STORE_FAST               2 (hmac)
    # 765          10 LOAD_GLOBAL              3 (NULL + isinstance)
    # 22 LOAD_FAST                1 (authkey)
    # 24 LOAD_GLOBAL              4 (bytes)
    # 36 PRECALL                  2
    # 40 CALL                     2
    # 50 POP_JUMP_FORWARD_IF_TRUE    47 (to 146)
    # 766          52 LOAD_GLOBAL              7 (NULL + ValueError)
    # 767          64 LOAD_CONST               2 ('Authkey must be bytes, not {0!s}')
    # 66 LOAD_METHOD              4 (format)
    # 88 LOAD_GLOBAL             11 (NULL + type)
    # 100 LOAD_FAST                1 (authkey)
    # 102 PRECALL                  1
    # 106 CALL                     1
    # 116 PRECALL                  1
    # 120 CALL                     1
    # 766         130 PRECALL                  1
    # 134 CALL                     1
    # 144 RAISE_VARARGS            1
    # 768     >>  146 LOAD_FAST                0 (connection)
    # 148 LOAD_METHOD              6 (recv_bytes)
    # 170 LOAD_CONST               3 (256)
    # 172 PRECALL                  1
    # 176 CALL                     1
    # 186 STORE_FAST               3 (message)
    # 769         188 LOAD_FAST                3 (message)
    # 190 LOAD_CONST               0 (None)
    # 192 LOAD_GLOBAL             15 (NULL + len)
    # 204 LOAD_GLOBAL             16 (CHALLENGE)
    # 216 PRECALL                  1
    # 220 CALL                     1
    # 230 BUILD_SLICE              2
    # 232 BINARY_SUBSCR
    # 242 LOAD_GLOBAL             16 (CHALLENGE)
    # 254 COMPARE_OP               2 (==)
    # 260 POP_JUMP_FORWARD_IF_TRUE    13 (to 288)
    # 262 LOAD_ASSERTION_ERROR
    # 264 LOAD_CONST               4 ('message = %r')
    # 266 LOAD_FAST                3 (message)
    # 268 BINARY_OP                6 (%)
    # 272 PRECALL                  0
    # 276 CALL                     0
    # 286 RAISE_VARARGS            1
    # 770     >>  288 LOAD_FAST                3 (message)
    # 290 LOAD_GLOBAL             15 (NULL + len)
    # 302 LOAD_GLOBAL             16 (CHALLENGE)
    # 314 PRECALL                  1
    # 318 CALL                     1
    # 328 LOAD_CONST               0 (None)
    # 330 BUILD_SLICE              2
    # 332 BINARY_SUBSCR
    # 342 STORE_FAST               3 (message)
    # 771         344 LOAD_FAST                2 (hmac)
    # 346 LOAD_METHOD              9 (new)
    # 368 LOAD_FAST                1 (authkey)
    # 370 LOAD_FAST                3 (message)
    # 372 LOAD_CONST               5 ('md5')
    # 374 PRECALL                  3
    # 378 CALL                     3
    # 388 LOAD_METHOD             10 (digest)
    # 410 PRECALL                  0
    # 414 CALL                     0
    # 424 STORE_FAST               4 (digest)
    # 772         426 LOAD_FAST                0 (connection)
    # 428 LOAD_METHOD             11 (send_bytes)
    # 450 LOAD_FAST                4 (digest)
    # 452 PRECALL                  1
    # 456 CALL                     1
    # 466 POP_TOP
    # 773         468 LOAD_FAST                0 (connection)
    # 470 LOAD_METHOD              6 (recv_bytes)
    # 492 LOAD_CONST               3 (256)
    # 494 PRECALL                  1
    # 498 CALL                     1
    # 508 STORE_FAST               5 (response)
    # 774         510 LOAD_FAST                5 (response)
    # 512 LOAD_GLOBAL             24 (WELCOME)
    # 524 COMPARE_OP               3 (!=)
    # 530 POP_JUMP_FORWARD_IF_FALSE    15 (to 562)
    # 775         532 LOAD_GLOBAL             27 (NULL + AuthenticationError)
    # 544 LOAD_CONST               6 ('digest sent was rejected')
    # 546 PRECALL                  1
    # 550 CALL                     1
    # 560 RAISE_VARARGS            1
    # 774     >>  562 LOAD_CONST               0 (None)
    # 564 RETURN_VALUE

class ConnectionWrapper:
    """ConnectionWrapper"""
    def __init__(self, conn, dumps, loads):
        # 782           0 RESUME                   0
        # 783           2 LOAD_FAST                1 (conn)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (_conn)
        # 784          16 LOAD_FAST                2 (dumps)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (_dumps)
        # 785          30 LOAD_FAST                3 (loads)
        # 32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               2 (_loads)
        # 786          44 LOAD_CONST               1 (('fileno', 'close', 'poll', 'recv_bytes', 'send_bytes'))
        # 46 GET_ITER
        # >>   48 FOR_ITER                35 (to 120)
        # 50 STORE_FAST               4 (attr)
        # 787          52 LOAD_GLOBAL              7 (NULL + getattr)
        # 64 LOAD_FAST                1 (conn)
        # 66 LOAD_FAST                4 (attr)
        # 68 PRECALL                  2
        # 72 CALL                     2
        # 82 STORE_FAST               5 (obj)
        # 788          84 LOAD_GLOBAL              9 (NULL + setattr)
        # 96 LOAD_FAST                0 (self)
        # 98 LOAD_FAST                4 (attr)
        # 100 LOAD_FAST                5 (obj)
        # 102 PRECALL                  3
        # 106 CALL                     3
        # 116 POP_TOP
        # 118 JUMP_BACKWARD           36 (to 48)
        # 786     >>  120 LOAD_CONST               0 (None)
        # 122 RETURN_VALUE

    def send(self, obj):
        # 789           0 RESUME                   0
        # 790           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (_dumps)
        # 26 LOAD_FAST                1 (obj)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 STORE_FAST               2 (s)
        # 791          44 LOAD_FAST                0 (self)
        # 46 LOAD_ATTR                1 (_conn)
        # 56 LOAD_METHOD              2 (send_bytes)
        # 78 LOAD_FAST                2 (s)
        # 80 PRECALL                  1
        # 84 CALL                     1
        # 94 POP_TOP
        # 96 LOAD_CONST               0 (None)
        # 98 RETURN_VALUE

    def recv(self):
        # 792           0 RESUME                   0
        # 793           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_conn)
        # 14 LOAD_METHOD              1 (recv_bytes)
        # 36 PRECALL                  0
        # 40 CALL                     0
        # 50 STORE_FAST               1 (s)
        # 794          52 LOAD_FAST                0 (self)
        # 54 LOAD_METHOD              2 (_loads)
        # 76 LOAD_FAST                1 (s)
        # 78 PRECALL                  1
        # 82 CALL                     1
        # 92 RETURN_VALUE


def _xml_dumps(obj):
    # 796           0 RESUME                   0
    # 797           2 LOAD_GLOBAL              0 (xmlrpclib)
    # 14 LOAD_METHOD              1 (dumps)
    # 36 LOAD_FAST                0 (obj)
    # 38 BUILD_TUPLE              1
    # 40 LOAD_CONST               0 (None)
    # 42 LOAD_CONST               0 (None)
    # 44 LOAD_CONST               0 (None)
    # 46 LOAD_CONST               1 (1)
    # 48 PRECALL                  5
    # 52 CALL                     5
    # 62 LOAD_METHOD              2 (encode)
    # 84 LOAD_CONST               2 ('utf-8')
    # 86 PRECALL                  1
    # 90 CALL                     1
    # 100 RETURN_VALUE

def _xml_loads(s):
    # 799           0 RESUME                   0
    # 800           2 LOAD_GLOBAL              0 (xmlrpclib)
    # 14 LOAD_METHOD              1 (loads)
    # 36 LOAD_FAST                0 (s)
    # 38 LOAD_METHOD              2 (decode)
    # 60 LOAD_CONST               1 ('utf-8')
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 UNPACK_SEQUENCE          2
    # 94 UNPACK_SEQUENCE          1
    # 98 STORE_FAST               1 (obj)
    # 100 STORE_FAST               2 (method)
    # 801         102 LOAD_FAST                1 (obj)
    # 104 RETURN_VALUE

class XmlListener:
    """XmlListener"""
    def accept(self):
        # 804           0 RESUME                   0
        # 806           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               0 (None)
        # 6 IMPORT_NAME              0 (xmlrpc.client)
        # 8 IMPORT_FROM              1 (client)
        # 10 STORE_GLOBAL             2 (xmlrpclib)
        # 12 POP_TOP
        # 807          14 LOAD_GLOBAL              6 (Listener)
        # 26 LOAD_METHOD              4 (accept)
        # 48 LOAD_FAST                0 (self)
        # 50 PRECALL                  1
        # 54 CALL                     1
        # 64 STORE_FAST               1 (obj)
        # 808          66 LOAD_GLOBAL             11 (NULL + ConnectionWrapper)
        # 78 LOAD_FAST                1 (obj)
        # 80 LOAD_GLOBAL             12 (_xml_dumps)
        # 92 LOAD_GLOBAL             14 (_xml_loads)
        # 104 PRECALL                  3
        # 108 CALL                     3
        # 118 RETURN_VALUE


def XmlClient():
    # 810           0 RESUME                   0
    # 812           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               0 (None)
    # 6 IMPORT_NAME              0 (xmlrpc.client)
    # 8 IMPORT_FROM              1 (client)
    # 10 STORE_GLOBAL             2 (xmlrpclib)
    # 12 POP_TOP
    # 813          14 LOAD_GLOBAL              7 (NULL + ConnectionWrapper)
    # 26 LOAD_GLOBAL              9 (NULL + Client)
    # 38 LOAD_FAST                0 (args)
    # 40 BUILD_MAP                0
    # 42 LOAD_FAST                1 (kwds)
    # 44 DICT_MERGE               1
    # 46 CALL_FUNCTION_EX         1
    # 48 LOAD_GLOBAL             10 (_xml_dumps)
    # 60 LOAD_GLOBAL             12 (_xml_loads)
    # 72 PRECALL                  3
    # 76 CALL                     3
    # 86 RETURN_VALUE

def _exhaustive_wait(handles, timeout):
    # 821           0 RESUME                   0
    # 824           2 LOAD_GLOBAL              1 (NULL + list)
    # 14 LOAD_FAST                0 (handles)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 STORE_FAST               2 (L)
    # 825          32 BUILD_LIST               0
    # 34 STORE_FAST               3 (ready)
    # 826          36 LOAD_FAST                2 (L)
    # 38 POP_JUMP_FORWARD_IF_FALSE   199 (to 438)
    # 827     >>   40 LOAD_GLOBAL              3 (NULL + _winapi)
    # 52 LOAD_ATTR                2 (WaitForMultipleObjects)
    # 62 LOAD_FAST                2 (L)
    # 64 LOAD_CONST               1 (False)
    # 66 LOAD_FAST                1 (timeout)
    # 68 PRECALL                  3
    # 72 CALL                     3
    # 82 STORE_FAST               4 (res)
    # 828          84 LOAD_FAST                4 (res)
    # 86 LOAD_GLOBAL              6 (WAIT_TIMEOUT)
    # 98 COMPARE_OP               2 (==)
    # 104 POP_JUMP_FORWARD_IF_FALSE     1 (to 108)
    # 829         106 JUMP_FORWARD           165 (to 438)
    # 830     >>  108 LOAD_GLOBAL              8 (WAIT_OBJECT_0)
    # 120 LOAD_FAST                4 (res)
    # 122 SWAP                     2
    # 124 COPY                     2
    # 126 COMPARE_OP               1 (<=)
    # 132 POP_JUMP_FORWARD_IF_FALSE    27 (to 188)
    # 134 LOAD_GLOBAL              8 (WAIT_OBJECT_0)
    # 146 LOAD_GLOBAL             11 (NULL + len)
    # 158 LOAD_FAST                2 (L)
    # 160 PRECALL                  1
    # 164 CALL                     1
    # 174 BINARY_OP                0 (+)
    # 178 COMPARE_OP               0 (<)
    # 184 POP_JUMP_FORWARD_IF_FALSE    14 (to 214)
    # 186 JUMP_FORWARD             2 (to 192)
    # >>  188 POP_TOP
    # 190 JUMP_FORWARD            11 (to 214)
    # 831     >>  192 LOAD_FAST                4 (res)
    # 194 LOAD_GLOBAL              8 (WAIT_OBJECT_0)
    # 206 BINARY_OP               23 (-=)
    # 210 STORE_FAST               4 (res)
    # 212 JUMP_FORWARD            68 (to 350)
    # 832     >>  214 LOAD_GLOBAL             12 (WAIT_ABANDONED_0)
    # 226 LOAD_FAST                4 (res)
    # 228 SWAP                     2
    # 230 COPY                     2
    # 232 COMPARE_OP               1 (<=)
    # 238 POP_JUMP_FORWARD_IF_FALSE    27 (to 294)
    # 240 LOAD_GLOBAL             12 (WAIT_ABANDONED_0)
    # 252 LOAD_GLOBAL             11 (NULL + len)
    # 264 LOAD_FAST                2 (L)
    # 266 PRECALL                  1
    # 270 CALL                     1
    # 280 BINARY_OP                0 (+)
    # 284 COMPARE_OP               0 (<)
    # 290 POP_JUMP_FORWARD_IF_FALSE    14 (to 320)
    # 292 JUMP_FORWARD             2 (to 298)
    # >>  294 POP_TOP
    # 296 JUMP_FORWARD            11 (to 320)
    # 833     >>  298 LOAD_FAST                4 (res)
    # 300 LOAD_GLOBAL             12 (WAIT_ABANDONED_0)
    # 312 BINARY_OP               23 (-=)
    # 316 STORE_FAST               4 (res)
    # 318 JUMP_FORWARD            15 (to 350)
    # 835     >>  320 LOAD_GLOBAL             15 (NULL + RuntimeError)
    # 332 LOAD_CONST               2 ('Should not get here')
    # 334 PRECALL                  1
    # 338 CALL                     1
    # 348 RAISE_VARARGS            1
    # 836     >>  350 LOAD_FAST                3 (ready)
    # 352 LOAD_METHOD              8 (append)
    # 374 LOAD_FAST                2 (L)
    # 376 LOAD_FAST                4 (res)
    # 378 BINARY_SUBSCR
    # 388 PRECALL                  1
    # 392 CALL                     1
    # 402 POP_TOP
    # 837         404 LOAD_FAST                2 (L)
    # 406 LOAD_FAST                4 (res)
    # 408 LOAD_CONST               3 (1)
    # 410 BINARY_OP                0 (+)
    # 414 LOAD_CONST               0 (None)
    # 416 BUILD_SLICE              2
    # 418 BINARY_SUBSCR
    # 428 STORE_FAST               2 (L)
    # 838         430 LOAD_CONST               4 (0)
    # 432 STORE_FAST               1 (timeout)
    # 826         434 LOAD_FAST                2 (L)
    # 436 POP_JUMP_BACKWARD_IF_TRUE   199 (to 40)
    # 839     >>  438 LOAD_FAST                3 (ready)
    # 440 RETURN_VALUE

def wait(object_list, timeout):
    """
        Wait till an object in object_list is ready/readable.

        Returns list of those objects in object_list which are ready/readable.
        """
    # 0 MAKE_CELL               10 (ready_objects)
    # 2 MAKE_CELL               11 (waithandle_to_obj)
    # 843           4 RESUME                   0
    # 849           6 LOAD_FAST                1 (timeout)
    # 8 POP_JUMP_FORWARD_IF_NOT_NONE     8 (to 26)
    # 850          10 LOAD_GLOBAL              0 (INFINITE)
    # 22 STORE_FAST               1 (timeout)
    # 24 JUMP_FORWARD            30 (to 86)
    # 851     >>   26 LOAD_FAST                1 (timeout)
    # 28 LOAD_CONST               2 (0)
    # 30 COMPARE_OP               0 (<)
    # 36 POP_JUMP_FORWARD_IF_FALSE     3 (to 44)
    # 852          38 LOAD_CONST               2 (0)
    # 40 STORE_FAST               1 (timeout)
    # 42 JUMP_FORWARD            21 (to 86)
    # 854     >>   44 LOAD_GLOBAL              3 (NULL + int)
    # 56 LOAD_FAST                1 (timeout)
    # 58 LOAD_CONST               3 (1000)
    # 60 BINARY_OP                5 (*)
    # 64 LOAD_CONST               4 (0.5)
    # 66 BINARY_OP                0 (+)
    # 70 PRECALL                  1
    # 74 CALL                     1
    # 84 STORE_FAST               1 (timeout)
    # 856     >>   86 LOAD_GLOBAL              5 (NULL + list)
    # 98 LOAD_FAST                0 (object_list)
    # 100 PRECALL                  1
    # 104 CALL                     1
    # 114 STORE_FAST               0 (object_list)
    # 857         116 BUILD_MAP                0
    # 118 STORE_DEREF             11 (waithandle_to_obj)
    # 858         120 BUILD_LIST               0
    # 122 STORE_FAST               2 (ov_list)
    # 859         124 LOAD_GLOBAL              7 (NULL + set)
    # 136 PRECALL                  0
    # 140 CALL                     0
    # 150 STORE_DEREF             10 (ready_objects)
    # 860         152 LOAD_GLOBAL              7 (NULL + set)
    # 164 PRECALL                  0
    # 168 CALL                     0
    # 178 STORE_FAST               3 (ready_handles)
    # 862         180 NOP
    # 863         182 LOAD_FAST                0 (object_list)
    # 184 GET_ITER
    # >>  186 EXTENDED_ARG             1
    # 188 FOR_ITER               322 (to 834)
    # 190 STORE_FAST               4 (o)
    # 864         192 NOP
    # 865         194 LOAD_GLOBAL              9 (NULL + getattr)
    # 206 LOAD_FAST                4 (o)
    # 208 LOAD_CONST               5 ('fileno')
    # 210 PRECALL                  2
    # 214 CALL                     2
    # 224 STORE_FAST               5 (fileno)
    # 870         226 NOP
    # 871         228 LOAD_GLOBAL             11 (NULL + _winapi)
    # 240 LOAD_ATTR                6 (ReadFile)
    # 250 PUSH_NULL
    # 252 LOAD_FAST                5 (fileno)
    # 254 PRECALL                  0
    # 258 CALL                     0
    # 268 LOAD_CONST               2 (0)
    # 270 LOAD_CONST               6 (True)
    # 272 PRECALL                  3
    # 276 CALL                     3
    # 286 UNPACK_SEQUENCE          2
    # 290 STORE_FAST               6 (ov)
    # 292 STORE_FAST               7 (err)
    # 294 JUMP_FORWARD            42 (to 380)
    # >>  296 PUSH_EXC_INFO
    # 872         298 LOAD_GLOBAL             14 (OSError)
    # 310 CHECK_EXC_MATCH
    # 312 POP_JUMP_FORWARD_IF_FALSE    29 (to 372)
    # 314 STORE_FAST               8 (e)
    # 873         316 LOAD_CONST               1 (None)
    # 318 LOAD_FAST                8 (e)
    # 320 LOAD_ATTR                8 (winerror)
    # 330 STORE_FAST               7 (err)
    # 332 STORE_FAST               6 (ov)
    # 874         334 LOAD_FAST                7 (err)
    # 336 LOAD_GLOBAL             18 (_ready_errors)
    # 348 CONTAINS_OP              1
    # 350 POP_JUMP_FORWARD_IF_FALSE     1 (to 354)
    # 875         352 RAISE_VARARGS            0
    # 874     >>  354 POP_EXCEPT
    # 356 LOAD_CONST               1 (None)
    # 358 STORE_FAST               8 (e)
    # 360 DELETE_FAST              8 (e)
    # 362 JUMP_FORWARD             8 (to 380)
    # >>  364 LOAD_CONST               1 (None)
    # 366 STORE_FAST               8 (e)
    # 368 DELETE_FAST              8 (e)
    # 370 RERAISE                  1
    # 872     >>  372 RERAISE                  0
    # >>  374 COPY                     3
    # 376 POP_EXCEPT
    # 378 RERAISE                  1
    # 876     >>  380 LOAD_FAST                7 (err)
    # 382 LOAD_GLOBAL             10 (_winapi)
    # 394 LOAD_ATTR               10 (ERROR_IO_PENDING)
    # 404 COMPARE_OP               2 (==)
    # 410 POP_JUMP_FORWARD_IF_FALSE    32 (to 476)
    # 877         412 LOAD_FAST                2 (ov_list)
    # 414 LOAD_METHOD             11 (append)
    # 436 LOAD_FAST                6 (ov)
    # 438 PRECALL                  1
    # 442 CALL                     1
    # 452 POP_TOP
    # 878         454 LOAD_FAST                4 (o)
    # 456 LOAD_DEREF              11 (waithandle_to_obj)
    # 458 LOAD_FAST                6 (ov)
    # 460 LOAD_ATTR               12 (event)
    # 470 STORE_SUBSCR
    # 474 JUMP_BACKWARD          145 (to 186)
    # 883     >>  476 LOAD_FAST                6 (ov)
    # 478 POP_JUMP_FORWARD_IF_FALSE   112 (to 704)
    # 480 LOAD_GLOBAL             27 (NULL + sys)
    # 492 LOAD_ATTR               14 (getwindowsversion)
    # 502 PRECALL                  0
    # 506 CALL                     0
    # 516 LOAD_CONST               1 (None)
    # 518 LOAD_CONST               7 (2)
    # 520 BUILD_SLICE              2
    # 522 BINARY_SUBSCR
    # 532 LOAD_CONST               8 ((6, 2))
    # 534 COMPARE_OP               5 (>=)
    # 540 POP_JUMP_FORWARD_IF_FALSE    81 (to 704)
    # 886         542 NOP
    # 887         544 LOAD_FAST                6 (ov)
    # 546 LOAD_METHOD             15 (GetOverlappedResult)
    # 568 LOAD_CONST               9 (False)
    # 570 PRECALL                  1
    # 574 CALL                     1
    # 584 UNPACK_SEQUENCE          2
    # 588 STORE_FAST               9 (_)
    # 590 STORE_FAST               7 (err)
    # 592 JUMP_FORWARD            30 (to 654)
    # >>  594 PUSH_EXC_INFO
    # 888         596 LOAD_GLOBAL             14 (OSError)
    # 608 CHECK_EXC_MATCH
    # 610 POP_JUMP_FORWARD_IF_FALSE    17 (to 646)
    # 612 STORE_FAST               8 (e)
    # 889         614 LOAD_FAST                8 (e)
    # 616 LOAD_ATTR                8 (winerror)
    # 626 STORE_FAST               7 (err)
    # 628 POP_EXCEPT
    # 630 LOAD_CONST               1 (None)
    # 632 STORE_FAST               8 (e)
    # 634 DELETE_FAST              8 (e)
    # 636 JUMP_FORWARD             8 (to 654)
    # >>  638 LOAD_CONST               1 (None)
    # 640 STORE_FAST               8 (e)
    # 642 DELETE_FAST              8 (e)
    # 644 RERAISE                  1
    # 888     >>  646 RERAISE                  0
    # >>  648 COPY                     3
    # 650 POP_EXCEPT
    # 652 RERAISE                  1
    # 890     >>  654 LOAD_FAST                7 (err)
    # 656 POP_JUMP_FORWARD_IF_TRUE    23 (to 704)
    # 658 LOAD_GLOBAL             33 (NULL + hasattr)
    # 670 LOAD_FAST                4 (o)
    # 672 LOAD_CONST              10 ('_got_empty_message')
    # 674 PRECALL                  2
    # 678 CALL                     2
    # 688 POP_JUMP_FORWARD_IF_FALSE     7 (to 704)
    # 891         690 LOAD_CONST               6 (True)
    # 692 LOAD_FAST                4 (o)
    # 694 STORE_ATTR              17 (_got_empty_message)
    # 892     >>  704 LOAD_DEREF              10 (ready_objects)
    # 706 LOAD_METHOD             18 (add)
    # 728 LOAD_FAST                4 (o)
    # 730 PRECALL                  1
    # 734 CALL                     1
    # 744 POP_TOP
    # 893         746 LOAD_CONST               2 (0)
    # 748 STORE_FAST               1 (timeout)
    # 750 EXTENDED_ARG             1
    # 752 JUMP_BACKWARD          284 (to 186)
    # >>  754 PUSH_EXC_INFO
    # 866         756 LOAD_GLOBAL             38 (AttributeError)
    # 768 CHECK_EXC_MATCH
    # 770 POP_JUMP_FORWARD_IF_FALSE    27 (to 826)
    # 772 POP_TOP
    # 867         774 LOAD_FAST                4 (o)
    # 776 LOAD_DEREF              11 (waithandle_to_obj)
    # 778 LOAD_FAST                4 (o)
    # 780 LOAD_METHOD             20 (__index__)
    # 802 PRECALL                  0
    # 806 CALL                     0
    # 816 STORE_SUBSCR
    # 820 POP_EXCEPT
    # 822 EXTENDED_ARG             1
    # 824 JUMP_BACKWARD          320 (to 186)
    # 866     >>  826 RERAISE                  0
    # >>  828 COPY                     3
    # 830 POP_EXCEPT
    # 832 RERAISE                  1
    # 895     >>  834 LOAD_GLOBAL             43 (NULL + _exhaustive_wait)
    # 846 LOAD_DEREF              11 (waithandle_to_obj)
    # 848 LOAD_METHOD             22 (keys)
    # 870 PRECALL                  0
    # 874 CALL                     0
    # 884 LOAD_FAST                1 (timeout)
    # 886 PRECALL                  2
    # 890 CALL                     2
    # 900 STORE_FAST               3 (ready_handles)
    # 898         902 LOAD_FAST                2 (ov_list)
    # 904 GET_ITER
    # >>  906 FOR_ITER                22 (to 952)
    # 908 STORE_FAST               6 (ov)
    # 899         910 LOAD_FAST                6 (ov)
    # 912 LOAD_METHOD             23 (cancel)
    # 934 PRECALL                  0
    # 938 CALL                     0
    # 948 POP_TOP
    # 950 JUMP_BACKWARD           23 (to 906)
    # 902     >>  952 LOAD_FAST                2 (ov_list)
    # 954 GET_ITER
    # >>  956 FOR_ITER               147 (to 1252)
    # 958 STORE_FAST               6 (ov)
    # 903         960 NOP
    # 904         962 LOAD_FAST                6 (ov)
    # 964 LOAD_METHOD             15 (GetOverlappedResult)
    # 986 LOAD_CONST               6 (True)
    # 988 PRECALL                  1
    # 992 CALL                     1
    # 1002 UNPACK_SEQUENCE          2
    # 1006 STORE_FAST               9 (_)
    # 1008 STORE_FAST               7 (err)
    # 1010 JUMP_FORWARD            40 (to 1092)
    # >> 1012 PUSH_EXC_INFO
    # 905        1014 LOAD_GLOBAL             14 (OSError)
    # 1026 CHECK_EXC_MATCH
    # 1028 POP_JUMP_FORWARD_IF_FALSE    27 (to 1084)
    # 1030 STORE_FAST               8 (e)
    # 906        1032 LOAD_FAST                8 (e)
    # 1034 LOAD_ATTR                8 (winerror)
    # 1044 STORE_FAST               7 (err)
    # 907        1046 LOAD_FAST                7 (err)
    # 1048 LOAD_GLOBAL             18 (_ready_errors)
    # 1060 CONTAINS_OP              1
    # 1062 POP_JUMP_FORWARD_IF_FALSE     1 (to 1066)
    # 908        1064 RAISE_VARARGS            0
    # 907     >> 1066 POP_EXCEPT
    # 1068 LOAD_CONST               1 (None)
    # 1070 STORE_FAST               8 (e)
    # 1072 DELETE_FAST              8 (e)
    # 1074 JUMP_FORWARD             8 (to 1092)
    # >> 1076 LOAD_CONST               1 (None)
    # 1078 STORE_FAST               8 (e)
    # 1080 DELETE_FAST              8 (e)
    # 1082 RERAISE                  1
    # 905     >> 1084 RERAISE                  0
    # >> 1086 COPY                     3
    # 1088 POP_EXCEPT
    # 1090 RERAISE                  1
    # 909     >> 1092 LOAD_FAST                7 (err)
    # 1094 LOAD_GLOBAL             10 (_winapi)
    # 1106 LOAD_ATTR               24 (ERROR_OPERATION_ABORTED)
    # 1116 COMPARE_OP               3 (!=)
    # 1122 POP_JUMP_FORWARD_IF_FALSE    63 (to 1250)
    # 910        1124 LOAD_DEREF              11 (waithandle_to_obj)
    # 1126 LOAD_FAST                6 (ov)
    # 1128 LOAD_ATTR               12 (event)
    # 1138 BINARY_SUBSCR
    # 1148 STORE_FAST               4 (o)
    # 911        1150 LOAD_DEREF              10 (ready_objects)
    # 1152 LOAD_METHOD             18 (add)
    # 1174 LOAD_FAST                4 (o)
    # 1176 PRECALL                  1
    # 1180 CALL                     1
    # 1190 POP_TOP
    # 912        1192 LOAD_FAST                7 (err)
    # 1194 LOAD_CONST               2 (0)
    # 1196 COMPARE_OP               2 (==)
    # 1202 POP_JUMP_FORWARD_IF_FALSE    23 (to 1250)
    # 915        1204 LOAD_GLOBAL             33 (NULL + hasattr)
    # 1216 LOAD_FAST                4 (o)
    # 1218 LOAD_CONST              10 ('_got_empty_message')
    # 1220 PRECALL                  2
    # 1224 CALL                     2
    # 1234 POP_JUMP_FORWARD_IF_FALSE     7 (to 1250)
    # 916        1236 LOAD_CONST               6 (True)
    # 1238 LOAD_FAST                4 (o)
    # 1240 STORE_ATTR              17 (_got_empty_message)
    # >> 1250 JUMP_BACKWARD          148 (to 956)
    # 902     >> 1252 JUMP_FORWARD           180 (to 1614)
    # >> 1254 PUSH_EXC_INFO
    # 898        1256 LOAD_FAST                2 (ov_list)
    # 1258 GET_ITER
    # >> 1260 FOR_ITER                22 (to 1306)
    # 1262 STORE_FAST               6 (ov)
    # 899        1264 LOAD_FAST                6 (ov)
    # 1266 LOAD_METHOD             23 (cancel)
    # 1288 PRECALL                  0
    # 1292 CALL                     0
    # 1302 POP_TOP
    # 1304 JUMP_BACKWARD           23 (to 1260)
    # 902     >> 1306 LOAD_FAST                2 (ov_list)
    # 1308 GET_ITER
    # >> 1310 FOR_ITER               147 (to 1606)
    # 1312 STORE_FAST               6 (ov)
    # 903        1314 NOP
    # 904        1316 LOAD_FAST                6 (ov)
    # 1318 LOAD_METHOD             15 (GetOverlappedResult)
    # 1340 LOAD_CONST               6 (True)
    # 1342 PRECALL                  1
    # 1346 CALL                     1
    # 1356 UNPACK_SEQUENCE          2
    # 1360 STORE_FAST               9 (_)
    # 1362 STORE_FAST               7 (err)
    # 1364 JUMP_FORWARD            40 (to 1446)
    # >> 1366 PUSH_EXC_INFO
    # 905        1368 LOAD_GLOBAL             14 (OSError)
    # 1380 CHECK_EXC_MATCH
    # 1382 POP_JUMP_FORWARD_IF_FALSE    27 (to 1438)
    # 1384 STORE_FAST               8 (e)
    # 906        1386 LOAD_FAST                8 (e)
    # 1388 LOAD_ATTR                8 (winerror)
    # 1398 STORE_FAST               7 (err)
    # 907        1400 LOAD_FAST                7 (err)
    # 1402 LOAD_GLOBAL             18 (_ready_errors)
    # 1414 CONTAINS_OP              1
    # 1416 POP_JUMP_FORWARD_IF_FALSE     1 (to 1420)
    # 908        1418 RAISE_VARARGS            0
    # 907     >> 1420 POP_EXCEPT
    # 1422 LOAD_CONST               1 (None)
    # 1424 STORE_FAST               8 (e)
    # 1426 DELETE_FAST              8 (e)
    # 1428 JUMP_FORWARD             8 (to 1446)
    # >> 1430 LOAD_CONST               1 (None)
    # 1432 STORE_FAST               8 (e)
    # 1434 DELETE_FAST              8 (e)
    # 1436 RERAISE                  1
    # 905     >> 1438 RERAISE                  0
    # >> 1440 COPY                     3
    # 1442 POP_EXCEPT
    # 1444 RERAISE                  1
    # 909     >> 1446 LOAD_FAST                7 (err)
    # 1448 LOAD_GLOBAL             10 (_winapi)
    # 1460 LOAD_ATTR               24 (ERROR_OPERATION_ABORTED)
    # 1470 COMPARE_OP               3 (!=)
    # 1476 POP_JUMP_FORWARD_IF_FALSE    63 (to 1604)
    # 910        1478 LOAD_DEREF              11 (waithandle_to_obj)
    # 1480 LOAD_FAST                6 (ov)
    # 1482 LOAD_ATTR               12 (event)
    # 1492 BINARY_SUBSCR
    # 1502 STORE_FAST               4 (o)
    # 911        1504 LOAD_DEREF              10 (ready_objects)
    # 1506 LOAD_METHOD             18 (add)
    # 1528 LOAD_FAST                4 (o)
    # 1530 PRECALL                  1
    # 1534 CALL                     1
    # 1544 POP_TOP
    # 912        1546 LOAD_FAST                7 (err)
    # 1548 LOAD_CONST               2 (0)
    # 1550 COMPARE_OP               2 (==)
    # 1556 POP_JUMP_FORWARD_IF_FALSE    23 (to 1604)
    # 915        1558 LOAD_GLOBAL             33 (NULL + hasattr)
    # 1570 LOAD_FAST                4 (o)
    # 1572 LOAD_CONST              10 ('_got_empty_message')
    # 1574 PRECALL                  2
    # 1578 CALL                     2
    # 1588 POP_JUMP_FORWARD_IF_FALSE     7 (to 1604)
    # 916        1590 LOAD_CONST               6 (True)
    # 1592 LOAD_FAST                4 (o)
    # 1594 STORE_ATTR              17 (_got_empty_message)
    # >> 1604 JUMP_BACKWARD          148 (to 1310)
    # 902     >> 1606 RERAISE                  0
    # >> 1608 COPY                     3
    # 1610 POP_EXCEPT
    # 1612 RERAISE                  1
    # 918     >> 1614 LOAD_DEREF              10 (ready_objects)
    # 1616 LOAD_METHOD             25 (update)
    # 1638 LOAD_CLOSURE            11 (waithandle_to_obj)
    # 1640 BUILD_TUPLE              1
    # 1642 LOAD_CONST              11 (<code object <genexpr> at 0x000001EBD7E36790, file "multiprocessing\connection.py", line 918>)
    # 1644 MAKE_FUNCTION            8 (closure)
    # 1646 LOAD_FAST                3 (ready_handles)
    # 1648 GET_ITER
    # 1650 PRECALL                  0
    # 1654 CALL                     0
    # 1664 PRECALL                  1
    # 1668 CALL                     1
    # 1678 POP_TOP
    # 919        1680 LOAD_CLOSURE            10 (ready_objects)
    # 1682 BUILD_TUPLE              1
    # 1684 LOAD_CONST              12 (<code object <listcomp> at 0x000001EBD7E36870, file "multiprocessing\connection.py", line 919>)
    # 1686 MAKE_FUNCTION            8 (closure)
    # 1688 LOAD_FAST                0 (object_list)
    # 1690 GET_ITER
    # 1692 PRECALL                  0
    # 1696 CALL                     0
    # 1706 RETURN_VALUE
    # ExceptionTable:
    # 182 to 190 -> 1254 [0]
    # 194 to 224 -> 754 [1]
    # 228 to 292 -> 296 [1]
    # 294 to 294 -> 1254 [0]
    # 296 to 314 -> 374 [2] lasti
    # 316 to 352 -> 364 [2] lasti
    # 354 to 362 -> 1254 [0]
    # 364 to 372 -> 374 [2] lasti
    # 374 to 540 -> 1254 [0]
    # 544 to 590 -> 594 [1]
    # 592 to 592 -> 1254 [0]
    # 594 to 612 -> 648 [2] lasti
    # 614 to 626 -> 638 [2] lasti
    # 628 to 636 -> 1254 [0]
    # 638 to 646 -> 648 [2] lasti
    # 648 to 752 -> 1254 [0]
    # 754 to 818 -> 828 [2] lasti
    # 820 to 824 -> 1254 [0]
    # 826 to 826 -> 828 [2] lasti
    # 828 to 900 -> 1254 [0]
    # 962 to 1008 -> 1012 [1]
    # 1012 to 1030 -> 1086 [2] lasti
    # 1032 to 1064 -> 1076 [2] lasti
    # 1076 to 1084 -> 1086 [2] lasti
    # 1254 to 1312 -> 1608 [1] lasti
    # 1316 to 1362 -> 1366 [3]
    # 1364 to 1364 -> 1608 [1] lasti
    # 1366 to 1384 -> 1440 [4] lasti
    # 1386 to 1418 -> 1430 [4] lasti
    # 1420 to 1428 -> 1608 [1] lasti
    # 1430 to 1438 -> 1440 [4] lasti
    # 1440 to 1606 -> 1608 [1] lasti
    # Disassembly of <code object <genexpr> at 0x000001EBD7E36790, file "multiprocessing\connection.py", line 918>:
    # 0 COPY_FREE_VARS           1
    # 918           2 RETURN_GENERATOR
    # 4 POP_TOP
    # 6 RESUME                   0
    # 8 LOAD_FAST                0 (.0)
    # >>   10 FOR_ITER                12 (to 36)
    # 12 STORE_FAST               1 (h)
    # 14 LOAD_DEREF               2 (waithandle_to_obj)
    # 16 LOAD_FAST                1 (h)
    # 18 BINARY_SUBSCR
    # 28 YIELD_VALUE
    # 30 RESUME                   1
    # 32 POP_TOP
    # 34 JUMP_BACKWARD           13 (to 10)
    # >>   36 LOAD_CONST               0 (None)
    # 38 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E36870, file "multiprocessing\connection.py", line 919>:
    # 0 COPY_FREE_VARS           1
    # 919           2 RESUME                   0
    # 4 BUILD_LIST               0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                 8 (to 26)
    # 10 STORE_FAST               1 (o)
    # 12 LOAD_FAST                1 (o)
    # 14 LOAD_DEREF               2 (ready_objects)
    # 16 CONTAINS_OP              0
    # 18 POP_JUMP_BACKWARD_IF_FALSE     6 (to 8)
    # 20 LOAD_FAST                1 (o)
    # 22 LIST_APPEND              2
    # 24 JUMP_BACKWARD            9 (to 8)
    # >>   26 RETURN_VALUE

def reduce_connection(conn):
    # 961           0 RESUME                   0
    # 962           2 LOAD_FAST                0 (conn)
    # 4 LOAD_METHOD              0 (fileno)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               1 (handle)
    # 963          42 LOAD_GLOBAL              3 (NULL + socket)
    # 54 LOAD_ATTR                2 (fromfd)
    # 64 LOAD_FAST                1 (handle)
    # 66 LOAD_GLOBAL              2 (socket)
    # 78 LOAD_ATTR                3 (AF_INET)
    # 88 LOAD_GLOBAL              2 (socket)
    # 100 LOAD_ATTR                4 (SOCK_STREAM)
    # 110 PRECALL                  3
    # 114 CALL                     3
    # 124 BEFORE_WITH
    # 126 STORE_FAST               2 (s)
    # 964         128 LOAD_CONST               1 (1)
    # 130 LOAD_CONST               2 (('resource_sharer',))
    # 132 IMPORT_NAME              5
    # 134 IMPORT_FROM              6 (resource_sharer)
    # 136 STORE_FAST               3 (resource_sharer)
    # 138 POP_TOP
    # 965         140 LOAD_FAST                3 (resource_sharer)
    # 142 LOAD_METHOD              7 (DupSocket)
    # 164 LOAD_FAST                2 (s)
    # 166 PRECALL                  1
    # 170 CALL                     1
    # 180 STORE_FAST               4 (ds)
    # 966         182 LOAD_GLOBAL             16 (rebuild_connection)
    # 194 LOAD_FAST                4 (ds)
    # 196 LOAD_FAST                0 (conn)
    # 198 LOAD_ATTR                9 (readable)
    # 208 LOAD_FAST                0 (conn)
    # 210 LOAD_ATTR               10 (writable)
    # 220 BUILD_TUPLE              3
    # 222 BUILD_TUPLE              2
    # 963         224 SWAP                     2
    # 226 LOAD_CONST               0 (None)
    # 228 LOAD_CONST               0 (None)
    # 230 LOAD_CONST               0 (None)
    # 232 PRECALL                  2
    # 236 CALL                     2
    # 246 POP_TOP
    # 248 RETURN_VALUE
    # >>  250 PUSH_EXC_INFO
    # 252 WITH_EXCEPT_START
    # 254 POP_JUMP_FORWARD_IF_TRUE     4 (to 264)
    # 256 RERAISE                  2
    # >>  258 COPY                     3
    # 260 POP_EXCEPT
    # 262 RERAISE                  1
    # >>  264 POP_TOP
    # 266 POP_EXCEPT
    # 268 POP_TOP
    # 270 POP_TOP
    # 272 LOAD_CONST               0 (None)
    # 274 RETURN_VALUE
    # ExceptionTable:
    # 126 to 222 -> 250 [1] lasti
    # 250 to 256 -> 258 [3] lasti
    # 264 to 264 -> 258 [3] lasti

def rebuild_connection(ds, readable, writable):
    # 967           0 RESUME                   0
    # 968           2 LOAD_FAST                0 (ds)
    # 4 LOAD_METHOD              0 (detach)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               3 (sock)
    # 969          42 LOAD_GLOBAL              3 (NULL + Connection)
    # 54 LOAD_FAST                3 (sock)
    # 56 LOAD_METHOD              0 (detach)
    # 78 PRECALL                  0
    # 82 CALL                     0
    # 92 LOAD_FAST                1 (readable)
    # 94 LOAD_FAST                2 (writable)
    # 96 PRECALL                  3
    # 100 CALL                     3
    # 110 RETURN_VALUE

def reduce_pipe_connection(conn):
    # 972           0 RESUME                   0
    # 973           2 LOAD_FAST                0 (conn)
    # 4 LOAD_ATTR                0 (readable)
    # 14 POP_JUMP_FORWARD_IF_FALSE    12 (to 40)
    # 16 LOAD_GLOBAL              2 (_winapi)
    # 28 LOAD_ATTR                2 (FILE_GENERIC_READ)
    # 38 JUMP_FORWARD             1 (to 42)
    # >>   40 LOAD_CONST               1 (0)
    # 974     >>   42 LOAD_FAST                0 (conn)
    # 44 LOAD_ATTR                3 (writable)
    # 54 POP_JUMP_FORWARD_IF_FALSE    12 (to 80)
    # 56 LOAD_GLOBAL              2 (_winapi)
    # 68 LOAD_ATTR                4 (FILE_GENERIC_WRITE)
    # 78 JUMP_FORWARD             1 (to 82)
    # >>   80 LOAD_CONST               1 (0)
    # 973     >>   82 BINARY_OP                7 (|)
    # 86 STORE_FAST               1 (access)
    # 975          88 LOAD_GLOBAL             11 (NULL + reduction)
    # 100 LOAD_ATTR                6 (DupHandle)
    # 110 LOAD_FAST                0 (conn)
    # 112 LOAD_METHOD              7 (fileno)
    # 134 PRECALL                  0
    # 138 CALL                     0
    # 148 LOAD_FAST                1 (access)
    # 150 PRECALL                  2
    # 154 CALL                     2
    # 164 STORE_FAST               2 (dh)
    # 976         166 LOAD_GLOBAL             16 (rebuild_pipe_connection)
    # 178 LOAD_FAST                2 (dh)
    # 180 LOAD_FAST                0 (conn)
    # 182 LOAD_ATTR                0 (readable)
    # 192 LOAD_FAST                0 (conn)
    # 194 LOAD_ATTR                3 (writable)
    # 204 BUILD_TUPLE              3
    # 206 BUILD_TUPLE              2
    # 208 RETURN_VALUE

def rebuild_pipe_connection(dh, readable, writable):
    # 977           0 RESUME                   0
    # 978           2 LOAD_FAST                0 (dh)
    # 4 LOAD_METHOD              0 (detach)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               3 (handle)
    # 979          42 LOAD_GLOBAL              3 (NULL + PipeConnection)
    # 54 LOAD_FAST                3 (handle)
    # 56 LOAD_FAST                1 (readable)
    # 58 LOAD_FAST                2 (writable)
    # 60 PRECALL                  3
    # 64 CALL                     3
    # 74 RETURN_VALUE
