# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: joblib\externals\loky\backend\_posix_reduction.py

import os
import socket
import _socket
from multiprocessing.connection import Connection
from multiprocessing.context import get_spawning_popen
from reduction import register

def _mk_inheritable(fd):
    # 24           0 RESUME                   0
    # 25           2 LOAD_GLOBAL              1 (NULL + os)
    # 14 LOAD_ATTR                1 (set_inheritable)
    # 24 LOAD_FAST                0 (fd)
    # 26 LOAD_CONST               1 (True)
    # 28 PRECALL                  2
    # 32 CALL                     2
    # 42 POP_TOP
    # 26          44 LOAD_FAST                0 (fd)
    # 46 RETURN_VALUE

def DupFd(fd):
    """Return a wrapper for an fd."""
    # 29           0 RESUME                   0
    # 31           2 LOAD_GLOBAL              1 (NULL + get_spawning_popen)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               1 (popen_obj)
    # 32          30 LOAD_FAST                1 (popen_obj)
    # 32 POP_JUMP_FORWARD_IF_NONE    40 (to 114)
    # 33          34 LOAD_FAST                1 (popen_obj)
    # 36 LOAD_METHOD              1 (DupFd)
    # 58 LOAD_FAST                1 (popen_obj)
    # 60 LOAD_METHOD              2 (duplicate_for_child)
    # 82 LOAD_FAST                0 (fd)
    # 84 PRECALL                  1
    # 88 CALL                     1
    # 98 PRECALL                  1
    # 102 CALL                     1
    # 112 RETURN_VALUE
    # 34     >>  114 LOAD_GLOBAL              6 (HAVE_SEND_HANDLE)
    # 126 POP_JUMP_FORWARD_IF_FALSE    27 (to 182)
    # 35         128 LOAD_CONST               2 (0)
    # 130 LOAD_CONST               3 (('resource_sharer',))
    # 132 IMPORT_NAME              4 (multiprocessing)
    # 134 IMPORT_FROM              5 (resource_sharer)
    # 136 STORE_FAST               2 (resource_sharer)
    # 138 POP_TOP
    # 37         140 LOAD_FAST                2 (resource_sharer)
    # 142 LOAD_METHOD              1 (DupFd)
    # 164 LOAD_FAST                0 (fd)
    # 166 PRECALL                  1
    # 170 CALL                     1
    # 180 RETURN_VALUE
    # 39     >>  182 LOAD_GLOBAL             13 (NULL + TypeError)
    # 40         194 LOAD_CONST               4 ('Cannot pickle connection object. This object can only be passed when spawning a new process')
    # 39         196 PRECALL                  1
    # 200 CALL                     1
    # 210 RAISE_VARARGS            1

def _reduce_socket(s):
    # 45           0 RESUME                   0
    # 46           2 LOAD_GLOBAL              1 (NULL + DupFd)
    # 14 LOAD_FAST                0 (s)
    # 16 LOAD_METHOD              1 (fileno)
    # 38 PRECALL                  0
    # 42 CALL                     0
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               1 (df)
    # 47          68 LOAD_GLOBAL              4 (_rebuild_socket)
    # 80 LOAD_FAST                1 (df)
    # 82 LOAD_FAST                0 (s)
    # 84 LOAD_ATTR                3 (family)
    # 94 LOAD_FAST                0 (s)
    # 96 LOAD_ATTR                4 (type)
    # 106 LOAD_FAST                0 (s)
    # 108 LOAD_ATTR                5 (proto)
    # 118 BUILD_TUPLE              4
    # 120 BUILD_TUPLE              2
    # 122 RETURN_VALUE

def _rebuild_socket(df, family, type, proto):
    # 50           0 RESUME                   0
    # 51           2 LOAD_FAST                0 (df)
    # 4 LOAD_METHOD              0 (detach)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               4 (fd)
    # 52          42 LOAD_GLOBAL              3 (NULL + socket)
    # 54 LOAD_ATTR                2 (fromfd)
    # 64 LOAD_FAST                4 (fd)
    # 66 LOAD_FAST                1 (family)
    # 68 LOAD_FAST                2 (type)
    # 70 LOAD_FAST                3 (proto)
    # 72 PRECALL                  4
    # 76 CALL                     4
    # 86 RETURN_VALUE

def rebuild_connection(df, readable, writable):
    # 55           0 RESUME                   0
    # 56           2 LOAD_FAST                0 (df)
    # 4 LOAD_METHOD              0 (detach)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               3 (fd)
    # 57          42 LOAD_GLOBAL              3 (NULL + Connection)
    # 54 LOAD_FAST                3 (fd)
    # 56 LOAD_FAST                1 (readable)
    # 58 LOAD_FAST                2 (writable)
    # 60 PRECALL                  3
    # 64 CALL                     3
    # 74 RETURN_VALUE

def reduce_connection(conn):
    # 60           0 RESUME                   0
    # 61           2 LOAD_GLOBAL              1 (NULL + DupFd)
    # 14 LOAD_FAST                0 (conn)
    # 16 LOAD_METHOD              1 (fileno)
    # 38 PRECALL                  0
    # 42 CALL                     0
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 STORE_FAST               1 (df)
    # 62          68 LOAD_GLOBAL              4 (rebuild_connection)
    # 80 LOAD_FAST                1 (df)
    # 82 LOAD_FAST                0 (conn)
    # 84 LOAD_ATTR                3 (readable)
    # 94 LOAD_FAST                0 (conn)
    # 96 LOAD_ATTR                4 (writable)
    # 106 BUILD_TUPLE              3
    # 108 BUILD_TUPLE              2
    # 110 RETURN_VALUE
