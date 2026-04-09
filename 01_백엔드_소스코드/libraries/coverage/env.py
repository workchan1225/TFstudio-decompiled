# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: coverage\env.py

"""Determine facts about the environment."""

from __future__ import annotations
import os
import platform
import sys
from collections.abc import Iterable
from typing import Any

def <lambda>():
    # 43           0 RESUME                   0
    # 2 LOAD_CONST               1 (True)
    # 4 RETURN_VALUE

class PYBEHAVIOR:
    """PYBEHAVIOR"""

def debug_info():
    """Return a list of (name, value) pairs for printing debug information."""
    # 125           0 RESUME                   0
    # 127           2 LOAD_CONST               1 (<code object <listcomp> at 0x000001EBD7DCA120, file "coverage\env.py", line 127>)
    # 4 MAKE_FUNCTION            0
    # 129           6 LOAD_GLOBAL              1 (NULL + globals)
    # 18 PRECALL                  0
    # 22 CALL                     0
    # 32 LOAD_METHOD              1 (items)
    # 54 PRECALL                  0
    # 58 CALL                     0
    # 127          68 GET_ITER
    # 70 PRECALL                  0
    # 74 CALL                     0
    # 84 STORE_FAST               0 (info)
    # 132          86 LOAD_FAST                0 (info)
    # 88 LOAD_CONST               2 (<code object <listcomp> at 0x000001EBD7DDE130, file "coverage\env.py", line 132>)
    # 90 MAKE_FUNCTION            0
    # 133          92 LOAD_GLOBAL              4 (PYBEHAVIOR)
    # 104 LOAD_ATTR                3 (__dict__)
    # 114 LOAD_METHOD              1 (items)
    # 136 PRECALL                  0
    # 140 CALL                     0
    # 132         150 GET_ITER
    # 152 PRECALL                  0
    # 156 CALL                     0
    # 166 BINARY_OP               13 (+=)
    # 170 STORE_FAST               0 (info)
    # 135         172 LOAD_GLOBAL              9 (NULL + sorted)
    # 184 LOAD_FAST                0 (info)
    # 186 PRECALL                  1
    # 190 CALL                     1
    # 200 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7DCA120, file "coverage\env.py", line 127>:
    # 127           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                39 (to 86)
    # 129           8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (name)
    # 14 STORE_FAST               2 (value)
    # 130          16 LOAD_FAST                1 (name)
    # 18 LOAD_METHOD              0 (startswith)
    # 40 LOAD_CONST               0 ('_')
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 127          56 POP_JUMP_FORWARD_IF_TRUE    13 (to 84)
    # 130          58 LOAD_FAST                1 (name)
    # 60 LOAD_GLOBAL              2 (_UNINTERESTING_GLOBALS)
    # 72 CONTAINS_OP              1
    # 74 POP_JUMP_BACKWARD_IF_FALSE    35 (to 6)
    # 128          76 LOAD_FAST                1 (name)
    # 78 LOAD_FAST                2 (value)
    # 80 BUILD_TUPLE              2
    # 130          82 LIST_APPEND              2
    # >>   84 JUMP_BACKWARD           40 (to 6)
    # >>   86 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7DDE130, file "coverage\env.py", line 132>:
    # 132           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                30 (to 68)
    # 133           8 UNPACK_SEQUENCE          2
    # 12 STORE_FAST               1 (name)
    # 14 STORE_FAST               2 (value)
    # 16 LOAD_FAST                1 (name)
    # 18 LOAD_METHOD              0 (startswith)
    # 40 LOAD_CONST               0 ('_')
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 132          56 POP_JUMP_BACKWARD_IF_TRUE    26 (to 6)
    # 133          58 LOAD_FAST                1 (name)
    # 60 LOAD_FAST                2 (value)
    # 62 BUILD_TUPLE              2
    # 132          64 LIST_APPEND              2
    # 66 JUMP_BACKWARD           31 (to 6)
    # >>   68 RETURN_VALUE
