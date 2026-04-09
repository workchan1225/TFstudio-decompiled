# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: backports\tarfile\compat\py38.py

import sys

def removesuffix(self, suffix):
    # 6           0 RESUME                   0
    # 8           2 LOAD_FAST                1 (suffix)
    # 4 POP_JUMP_FORWARD_IF_FALSE    45 (to 96)
    # 6 LOAD_FAST                0 (self)
    # 8 LOAD_METHOD              0 (endswith)
    # 30 LOAD_FAST                1 (suffix)
    # 32 PRECALL                  1
    # 36 CALL                     1
    # 46 POP_JUMP_FORWARD_IF_FALSE    24 (to 96)
    # 9          48 LOAD_FAST                0 (self)
    # 50 LOAD_CONST               0 (None)
    # 52 LOAD_GLOBAL              3 (NULL + len)
    # 64 LOAD_FAST                1 (suffix)
    # 66 PRECALL                  1
    # 70 CALL                     1
    # 80 UNARY_NEGATIVE
    # 82 BUILD_SLICE              2
    # 84 BINARY_SUBSCR
    # 94 RETURN_VALUE
    # 11     >>   96 LOAD_FAST                0 (self)
    # 98 LOAD_CONST               0 (None)
    # 100 LOAD_CONST               0 (None)
    # 102 BUILD_SLICE              2
    # 104 BINARY_SUBSCR
    # 114 RETURN_VALUE

def removeprefix(self, prefix):
    # 13           0 RESUME                   0
    # 14           2 LOAD_FAST                0 (self)
    # 4 LOAD_METHOD              0 (startswith)
    # 26 LOAD_FAST                1 (prefix)
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 POP_JUMP_FORWARD_IF_FALSE    23 (to 90)
    # 15          44 LOAD_FAST                0 (self)
    # 46 LOAD_GLOBAL              3 (NULL + len)
    # 58 LOAD_FAST                1 (prefix)
    # 60 PRECALL                  1
    # 64 CALL                     1
    # 74 LOAD_CONST               0 (None)
    # 76 BUILD_SLICE              2
    # 78 BINARY_SUBSCR
    # 88 RETURN_VALUE
    # 17     >>   90 LOAD_FAST                0 (self)
    # 92 LOAD_CONST               0 (None)
    # 94 LOAD_CONST               0 (None)
    # 96 BUILD_SLICE              2
    # 98 BINARY_SUBSCR
    # 108 RETURN_VALUE
