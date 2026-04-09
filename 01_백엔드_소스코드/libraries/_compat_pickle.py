# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: _compat_pickle.py

"""__builtin__"""

def <genexpr>(.0):
    # 165           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                11 (to 32)
    # 10 UNPACK_SEQUENCE          2
    # 14 STORE_FAST               1 (k)
    # 16 STORE_FAST               2 (v)
    # 18 LOAD_FAST                2 (v)
    # 20 LOAD_FAST                1 (k)
    # 22 BUILD_TUPLE              2
    # 24 YIELD_VALUE
    # 26 RESUME                   1
    # 28 POP_TOP
    # 30 JUMP_BACKWARD           12 (to 8)
    # >>   32 LOAD_CONST               0 (None)
    # 34 RETURN_VALUE
