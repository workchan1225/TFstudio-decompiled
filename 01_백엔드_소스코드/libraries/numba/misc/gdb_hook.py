# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: numba\misc\gdb_hook.py

import os
import sys
from llvmlite import ir
from numba.core import types
from numba import gdb
from numba.core.extending import overload

def _confirm_gdb(need_ptrace_attach):
    """
    Set need_ptrace_attach to True/False to indicate whether the ptrace attach
    permission is needed for this gdb use case. Mode 0 (classic) or 1
    (restricted ptrace) is required if need_ptrace_attach is True. See:
    https://www.kernel.org/doc/Documentation/admin-guide/LSM/Yama.rst
    for details on the modes.
    """
    # 18           0 RESUME                   0
    # 26           2 LOAD_GLOBAL              0 (_unix_like)
    # 14 POP_JUMP_FORWARD_IF_TRUE    22 (to 60)
    # 27          16 LOAD_CONST               1 ('gdb support is only available on unix-like systems')
    # 18 STORE_FAST               1 (msg)
    # 28          20 LOAD_GLOBAL              3 (NULL + errors)
    # 32 LOAD_ATTR                2 (NumbaRuntimeError)
    # 42 LOAD_FAST                1 (msg)
    # 44 PRECALL                  1
    # 48 CALL                     1
    # 58 RAISE_VARARGS            1
    # 29     >>   60 LOAD_GLOBAL              6 (config)
    # 72 LOAD_ATTR                4 (GDB_BINARY)
    # 82 STORE_FAST               2 (gdbloc)
    # 30          84 LOAD_GLOBAL             10 (os)
    # 96 LOAD_ATTR                6 (path)
    # 106 LOAD_METHOD              7 (exists)
    # 128 LOAD_FAST                2 (gdbloc)
    # 130 PRECALL                  1
    # 134 CALL                     1
    # 144 POP_JUMP_FORWARD_IF_FALSE    31 (to 208)
    # 146 LOAD_GLOBAL             10 (os)
    # 158 LOAD_ATTR                6 (path)
    # 168 LOAD_METHOD              8 (isfile)
    # 190 LOAD_FAST                2 (gdbloc)
    # 192 PRECALL                  1
    # 196 CALL                     1
    # 206 POP_JUMP_FORWARD_IF_TRUE    30 (to 268)
    # 31     >>  208 LOAD_CONST               2 ('Is gdb present? Location specified (%s) does not exist. The gdb binary location can be set using Numba configuration, see: https://numba.readthedocs.io/en/stable/reference/envvars.html')
    # 210 STORE_FAST               1 (msg)
    # 35         212 LOAD_GLOBAL             19 (NULL + RuntimeError)
    # 224 LOAD_FAST                1 (msg)
    # 226 LOAD_GLOBAL              6 (config)
    # 238 LOAD_ATTR                4 (GDB_BINARY)
    # 248 BINARY_OP                6 (%)
    # 252 PRECALL                  1
    # 256 CALL                     1
    # 266 RAISE_VARARGS            1
    # 39     >>  268 LOAD_GLOBAL             10 (os)
    # 280 LOAD_ATTR                6 (path)
    # 290 LOAD_METHOD             10 (join)
    # 312 LOAD_GLOBAL             10 (os)
    # 324 LOAD_ATTR               11 (sep)
    # 334 LOAD_CONST               3 ('proc')
    # 336 LOAD_CONST               4 ('sys')
    # 338 LOAD_CONST               5 ('kernel')
    # 340 LOAD_CONST               6 ('yama')
    # 40         342 LOAD_CONST               7 ('ptrace_scope')
    # 39         344 PRECALL                  6
    # 348 CALL                     6
    # 358 STORE_FAST               3 (ptrace_scope_file)
    # 41         360 LOAD_GLOBAL             10 (os)
    # 372 LOAD_ATTR                6 (path)
    # 382 LOAD_METHOD              7 (exists)
    # 404 LOAD_FAST                3 (ptrace_scope_file)
    # 406 PRECALL                  1
    # 410 CALL                     1
    # 420 STORE_FAST               4 (has_ptrace_scope)
    # 42         422 LOAD_FAST                4 (has_ptrace_scope)
    # 424 POP_JUMP_FORWARD_IF_FALSE   101 (to 628)
    # 43         426 LOAD_GLOBAL             25 (NULL + open)
    # 438 LOAD_FAST                3 (ptrace_scope_file)
    # 440 LOAD_CONST               8 ('rt')
    # 442 PRECALL                  2
    # 446 CALL                     2
    # 456 BEFORE_WITH
    # 458 STORE_FAST               5 (f)
    # 44         460 LOAD_FAST                5 (f)
    # 462 LOAD_METHOD             13 (readline)
    # 484 PRECALL                  0
    # 488 CALL                     0
    # 498 LOAD_METHOD             14 (strip)
    # 520 PRECALL                  0
    # 524 CALL                     0
    # 534 STORE_FAST               6 (value)
    # 43         536 LOAD_CONST               9 (None)
    # 538 LOAD_CONST               9 (None)
    # 540 LOAD_CONST               9 (None)
    # 542 PRECALL                  2
    # 546 CALL                     2
    # 556 POP_TOP
    # 558 JUMP_FORWARD            11 (to 582)
    # >>  560 PUSH_EXC_INFO
    # 562 WITH_EXCEPT_START
    # 564 POP_JUMP_FORWARD_IF_TRUE     4 (to 574)
    # 566 RERAISE                  2
    # >>  568 COPY                     3
    # 570 POP_EXCEPT
    # 572 RERAISE                  1
    # >>  574 POP_TOP
    # 576 POP_EXCEPT
    # 578 POP_TOP
    # 580 POP_TOP
    # 45     >>  582 LOAD_FAST                0 (need_ptrace_attach)
    # 584 POP_JUMP_FORWARD_IF_FALSE    23 (to 632)
    # 586 LOAD_FAST                6 (value)
    # 588 LOAD_CONST              10 (('0', '1'))
    # 590 CONTAINS_OP              1
    # 592 POP_JUMP_FORWARD_IF_FALSE    21 (to 636)
    # 46         594 LOAD_CONST              11 ("gdb can launch but cannot attach to the executing program because ptrace permissions have been restricted at the system level by the Linux security module 'Yama'.\n\nDocumentation for this module and the security implications of making changes to its behaviour can be found in the Linux Kernel documentation https://www.kernel.org/doc/Documentation/admin-guide/LSM/Yama.rst\n\nDocumentation on how to adjust the behaviour of Yama on Ubuntu Linux with regards to 'ptrace_scope' can be found here https://wiki.ubuntu.com/Security/Features#ptrace.")
    # 596 STORE_FAST               1 (msg)
    # 57         598 LOAD_GLOBAL             19 (NULL + RuntimeError)
    # 610 LOAD_FAST                1 (msg)
    # 612 PRECALL                  1
    # 616 CALL                     1
    # 626 RAISE_VARARGS            1
    # 42     >>  628 LOAD_CONST               9 (None)
    # 630 RETURN_VALUE
    # 45     >>  632 LOAD_CONST               9 (None)
    # 634 RETURN_VALUE
    # >>  636 LOAD_CONST               9 (None)
    # 638 RETURN_VALUE
    # ExceptionTable:
    # 458 to 534 -> 560 [1] lasti
    # 560 to 566 -> 568 [3] lasti
    # 574 to 574 -> 568 [3] lasti

def hook_gdb():
    # 0 MAKE_CELL                2 (gdbimpl)
    # 60           2 RESUME                   0
    # 62           4 LOAD_GLOBAL              1 (NULL + _confirm_gdb)
    # 16 PRECALL                  0
    # 20 CALL                     0
    # 30 POP_TOP
    # 63          32 LOAD_GLOBAL              3 (NULL + gen_gdb_impl)
    # 44 LOAD_FAST                0 (args)
    # 46 LOAD_CONST               1 (True)
    # 48 PRECALL                  2
    # 52 CALL                     2
    # 62 STORE_DEREF              2 (gdbimpl)
    # 65          64 LOAD_CLOSURE             2 (gdbimpl)
    # 66 BUILD_TUPLE              1
    # 68 LOAD_CONST               2 (<code object impl at 0x000001EBD7E34F10, file "numba\misc\gdb_hook.py", line 65>)
    # 70 MAKE_FUNCTION            8 (closure)
    # 72 STORE_FAST               1 (impl)
    # 67          74 LOAD_FAST                1 (impl)
    # 76 RETURN_VALUE
    # Disassembly of <code object impl at 0x000001EBD7E34F10, file "numba\misc\gdb_hook.py", line 65>:
    # 0 COPY_FREE_VARS           1
    # 65           2 RESUME                   0
    # 66           4 PUSH_NULL
    # 6 LOAD_DEREF               1 (gdbimpl)
    # 8 PRECALL                  0
    # 12 CALL                     0
    # 22 POP_TOP
    # 24 LOAD_CONST               0 (None)
    # 26 RETURN_VALUE

def hook_gdb_init():
    # 0 MAKE_CELL                2 (gdbimpl)
    # 70           2 RESUME                   0
    # 72           4 LOAD_GLOBAL              1 (NULL + _confirm_gdb)
    # 16 PRECALL                  0
    # 20 CALL                     0
    # 30 POP_TOP
    # 73          32 LOAD_GLOBAL              3 (NULL + gen_gdb_impl)
    # 44 LOAD_FAST                0 (args)
    # 46 LOAD_CONST               1 (False)
    # 48 PRECALL                  2
    # 52 CALL                     2
    # 62 STORE_DEREF              2 (gdbimpl)
    # 75          64 LOAD_CLOSURE             2 (gdbimpl)
    # 66 BUILD_TUPLE              1
    # 68 LOAD_CONST               2 (<code object impl at 0x000001EBD7E35ED0, file "numba\misc\gdb_hook.py", line 75>)
    # 70 MAKE_FUNCTION            8 (closure)
    # 72 STORE_FAST               1 (impl)
    # 77          74 LOAD_FAST                1 (impl)
    # 76 RETURN_VALUE
    # Disassembly of <code object impl at 0x000001EBD7E35ED0, file "numba\misc\gdb_hook.py", line 75>:
    # 0 COPY_FREE_VARS           1
    # 75           2 RESUME                   0
    # 76           4 PUSH_NULL
    # 6 LOAD_DEREF               1 (gdbimpl)
    # 8 PRECALL                  0
    # 12 CALL                     0
    # 22 POP_TOP
    # 24 LOAD_CONST               0 (None)
    # 26 RETURN_VALUE

def init_gdb_codegen(cgctx, builder, signature, args, const_args, do_break):
    # 0 MAKE_CELL                0 (cgctx)
    # 2 MAKE_CELL               40 (mod)
    # 80           4 RESUME                   0
    # 83           6 LOAD_GLOBAL              1 (NULL + ir)
    # 18 LOAD_ATTR                1 (IntType)
    # 28 LOAD_CONST               1 (8)
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 STORE_FAST               6 (int8_t)
    # 84          46 LOAD_GLOBAL              1 (NULL + ir)
    # 58 LOAD_ATTR                1 (IntType)
    # 68 LOAD_CONST               2 (32)
    # 70 PRECALL                  1
    # 74 CALL                     1
    # 84 STORE_FAST               7 (int32_t)
    # 85          86 LOAD_GLOBAL              1 (NULL + ir)
    # 98 LOAD_ATTR                1 (IntType)
    # 108 LOAD_GLOBAL              4 (utils)
    # 120 LOAD_ATTR                3 (MACHINE_BITS)
    # 130 PRECALL                  1
    # 134 CALL                     1
    # 144 STORE_FAST               8 (intp_t)
    # 86         146 LOAD_GLOBAL              1 (NULL + ir)
    # 158 LOAD_ATTR                4 (PointerType)
    # 168 LOAD_GLOBAL              1 (NULL + ir)
    # 180 LOAD_ATTR                1 (IntType)
    # 190 LOAD_CONST               1 (8)
    # 192 PRECALL                  1
    # 196 CALL                     1
    # 206 PRECALL                  1
    # 210 CALL                     1
    # 220 STORE_FAST               9 (char_ptr)
    # 87         222 PUSH_NULL
    # 224 LOAD_FAST                7 (int32_t)
    # 226 LOAD_CONST               3 (0)
    # 228 PRECALL                  1
    # 232 CALL                     1
    # 242 STORE_FAST              10 (zero_i32t)
    # 89         244 LOAD_FAST                1 (builder)
    # 246 LOAD_ATTR                5 (module)
    # 256 STORE_DEREF             40 (mod)
    # 90         258 LOAD_GLOBAL             13 (NULL + cgutils)
    # 270 LOAD_ATTR                7 (alloca_once)
    # 280 LOAD_FAST                1 (builder)
    # 282 LOAD_FAST                7 (int32_t)
    # 284 LOAD_CONST               4 (1)
    # 286 KW_NAMES                 5
    # 288 PRECALL                  3
    # 292 CALL                     3
    # 302 STORE_FAST              11 (pid)
    # 93         304 LOAD_GLOBAL             13 (NULL + cgutils)
    # 316 LOAD_ATTR                7 (alloca_once)
    # 326 LOAD_FAST                1 (builder)
    # 328 LOAD_FAST                6 (int8_t)
    # 330 LOAD_CONST               6 (12)
    # 332 KW_NAMES                 5
    # 334 PRECALL                  3
    # 338 CALL                     3
    # 348 STORE_FAST              12 (pidstr)
    # 96         350 LOAD_DEREF               0 (cgctx)
    # 352 LOAD_METHOD              8 (insert_const_string)
    # 374 LOAD_DEREF              40 (mod)
    # 376 LOAD_CONST               7 ('%d')
    # 378 PRECALL                  2
    # 382 CALL                     2
    # 392 STORE_FAST              13 (intfmt)
    # 97         394 LOAD_DEREF               0 (cgctx)
    # 396 LOAD_METHOD              8 (insert_const_string)
    # 418 LOAD_DEREF              40 (mod)
    # 420 LOAD_GLOBAL             18 (config)
    # 432 LOAD_ATTR               10 (GDB_BINARY)
    # 442 PRECALL                  2
    # 446 CALL                     2
    # 456 STORE_FAST              14 (gdb_str)
    # 98         458 LOAD_DEREF               0 (cgctx)
    # 460 LOAD_METHOD              8 (insert_const_string)
    # 482 LOAD_DEREF              40 (mod)
    # 484 LOAD_CONST               8 ('attach')
    # 486 PRECALL                  2
    # 490 CALL                     2
    # 500 STORE_FAST              15 (attach_str)
    # 100         502 BUILD_LIST               0
    # 504 STORE_FAST              16 (new_args)
    # 105         506 LOAD_FAST               16 (new_args)
    # 508 LOAD_METHOD             11 (extend)
    # 530 LOAD_CONST               9 ('-x')
    # 532 LOAD_GLOBAL             24 (os)
    # 544 LOAD_ATTR               13 (path)
    # 554 LOAD_METHOD             14 (join)
    # 576 LOAD_GLOBAL             30 (_path)
    # 588 LOAD_CONST              10 ('cmdlang.gdb')
    # 590 PRECALL                  2
    # 594 CALL                     2
    # 604 BUILD_LIST               2
    # 606 PRECALL                  1
    # 610 CALL                     1
    # 620 POP_TOP
    # 107         622 LOAD_FAST               16 (new_args)
    # 624 LOAD_METHOD             11 (extend)
    # 646 LOAD_CONST              11 ('-ex')
    # 648 LOAD_CONST              12 ('c')
    # 650 BUILD_LIST               2
    # 652 PRECALL                  1
    # 656 CALL                     1
    # 666 POP_TOP
    # 109         668 LOAD_GLOBAL             33 (NULL + any)
    # 680 LOAD_CONST              13 (<code object <listcomp> at 0x000001EBD7DDFC30, file "numba\misc\gdb_hook.py", line 109>)
    # 682 MAKE_FUNCTION            0
    # 684 LOAD_FAST                4 (const_args)
    # 686 GET_ITER
    # 688 PRECALL                  0
    # 692 CALL                     0
    # 702 PRECALL                  1
    # 706 CALL                     1
    # 716 POP_JUMP_FORWARD_IF_FALSE    20 (to 758)
    # 110         718 LOAD_GLOBAL             35 (NULL + errors)
    # 730 LOAD_ATTR               18 (RequireLiteralValue)
    # 740 LOAD_FAST                4 (const_args)
    # 742 PRECALL                  1
    # 746 CALL                     1
    # 756 RAISE_VARARGS            1
    # 111     >>  758 LOAD_FAST               16 (new_args)
    # 760 LOAD_METHOD             11 (extend)
    # 782 LOAD_CONST              14 (<code object <listcomp> at 0x000001EBD7E35A70, file "numba\misc\gdb_hook.py", line 111>)
    # 784 MAKE_FUNCTION            0
    # 786 LOAD_FAST                4 (const_args)
    # 788 GET_ITER
    # 790 PRECALL                  0
    # 794 CALL                     0
    # 804 PRECALL                  1
    # 808 CALL                     1
    # 818 POP_TOP
    # 112         820 LOAD_CLOSURE             0 (cgctx)
    # 822 LOAD_CLOSURE            40 (mod)
    # 824 BUILD_TUPLE              2
    # 826 LOAD_CONST              15 (<code object <listcomp> at 0x000001EBD7DDFE30, file "numba\misc\gdb_hook.py", line 112>)
    # 828 MAKE_FUNCTION            8 (closure)
    # 830 LOAD_FAST               16 (new_args)
    # 832 GET_ITER
    # 834 PRECALL                  0
    # 838 CALL                     0
    # 848 STORE_FAST              17 (cmdlang)
    # 115         850 LOAD_GLOBAL              1 (NULL + ir)
    # 862 LOAD_ATTR               19 (FunctionType)
    # 872 LOAD_FAST                7 (int32_t)
    # 874 LOAD_GLOBAL             41 (NULL + tuple)
    # 886 PRECALL                  0
    # 890 CALL                     0
    # 900 PRECALL                  2
    # 904 CALL                     2
    # 914 STORE_FAST              18 (fnty)
    # 116         916 LOAD_GLOBAL             13 (NULL + cgutils)
    # 928 LOAD_ATTR               21 (get_or_insert_function)
    # 938 LOAD_DEREF              40 (mod)
    # 940 LOAD_FAST               18 (fnty)
    # 942 LOAD_CONST              16 ('getpid')
    # 944 PRECALL                  3
    # 948 CALL                     3
    # 958 STORE_FAST              19 (getpid)
    # 120         960 LOAD_GLOBAL              1 (NULL + ir)
    # 972 LOAD_ATTR               19 (FunctionType)
    # 121         982 LOAD_FAST                7 (int32_t)
    # 984 LOAD_FAST                9 (char_ptr)
    # 986 LOAD_FAST                8 (intp_t)
    # 988 LOAD_FAST                9 (char_ptr)
    # 990 BUILD_TUPLE              3
    # 992 LOAD_CONST              17 (True)
    # 120         994 KW_NAMES                18
    # 996 PRECALL                  3
    # 1000 CALL                     3
    # 1010 STORE_FAST              18 (fnty)
    # 122        1012 LOAD_GLOBAL             13 (NULL + cgutils)
    # 1024 LOAD_ATTR               21 (get_or_insert_function)
    # 1034 LOAD_DEREF              40 (mod)
    # 1036 LOAD_FAST               18 (fnty)
    # 1038 LOAD_CONST              19 ('snprintf')
    # 1040 PRECALL                  3
    # 1044 CALL                     3
    # 1054 STORE_FAST              20 (snprintf)
    # 125        1056 LOAD_GLOBAL              1 (NULL + ir)
    # 1068 LOAD_ATTR               19 (FunctionType)
    # 1078 LOAD_FAST                7 (int32_t)
    # 1080 LOAD_GLOBAL             41 (NULL + tuple)
    # 1092 PRECALL                  0
    # 1096 CALL                     0
    # 1106 PRECALL                  2
    # 1110 CALL                     2
    # 1120 STORE_FAST              18 (fnty)
    # 126        1122 LOAD_GLOBAL             13 (NULL + cgutils)
    # 1134 LOAD_ATTR               21 (get_or_insert_function)
    # 1144 LOAD_DEREF              40 (mod)
    # 1146 LOAD_FAST               18 (fnty)
    # 1148 LOAD_CONST              20 ('fork')
    # 1150 PRECALL                  3
    # 1154 CALL                     3
    # 1164 STORE_FAST              21 (fork)
    # 129        1166 LOAD_GLOBAL              1 (NULL + ir)
    # 1178 LOAD_ATTR               19 (FunctionType)
    # 1188 LOAD_FAST                7 (int32_t)
    # 1190 LOAD_FAST                9 (char_ptr)
    # 1192 LOAD_FAST                9 (char_ptr)
    # 1194 BUILD_TUPLE              2
    # 1196 LOAD_CONST              17 (True)
    # 1198 KW_NAMES                18
    # 1200 PRECALL                  3
    # 1204 CALL                     3
    # 1214 STORE_FAST              18 (fnty)
    # 130        1216 LOAD_GLOBAL             13 (NULL + cgutils)
    # 1228 LOAD_ATTR               21 (get_or_insert_function)
    # 1238 LOAD_DEREF              40 (mod)
    # 1240 LOAD_FAST               18 (fnty)
    # 1242 LOAD_CONST              21 ('execl')
    # 1244 PRECALL                  3
    # 1248 CALL                     3
    # 1258 STORE_FAST              22 (execl)
    # 133        1260 LOAD_GLOBAL              1 (NULL + ir)
    # 1272 LOAD_ATTR               19 (FunctionType)
    # 1282 LOAD_FAST                7 (int32_t)
    # 1284 LOAD_FAST                7 (int32_t)
    # 1286 BUILD_TUPLE              1
    # 1288 PRECALL                  2
    # 1292 CALL                     2
    # 1302 STORE_FAST              18 (fnty)
    # 134        1304 LOAD_GLOBAL             13 (NULL + cgutils)
    # 1316 LOAD_ATTR               21 (get_or_insert_function)
    # 1326 LOAD_DEREF              40 (mod)
    # 1328 LOAD_FAST               18 (fnty)
    # 1330 LOAD_CONST              22 ('sleep')
    # 1332 PRECALL                  3
    # 1336 CALL                     3
    # 1346 STORE_FAST              23 (sleep)
    # 137        1348 LOAD_GLOBAL              1 (NULL + ir)
    # 1360 LOAD_ATTR               19 (FunctionType)
    # 1370 LOAD_GLOBAL              1 (NULL + ir)
    # 1382 LOAD_ATTR               22 (VoidType)
    # 1392 PRECALL                  0
    # 1396 CALL                     0
    # 1406 LOAD_GLOBAL             41 (NULL + tuple)
    # 1418 PRECALL                  0
    # 1422 CALL                     0
    # 1432 PRECALL                  2
    # 1436 CALL                     2
    # 1446 STORE_FAST              18 (fnty)
    # 138        1448 LOAD_GLOBAL             13 (NULL + cgutils)
    # 1460 LOAD_ATTR               21 (get_or_insert_function)
    # 1470 LOAD_DEREF              40 (mod)
    # 1472 LOAD_FAST               18 (fnty)
    # 139        1474 LOAD_CONST              23 ('numba_gdb_breakpoint')
    # 138        1476 PRECALL                  3
    # 1480 CALL                     3
    # 1490 STORE_FAST              24 (breakpoint)
    # 142        1492 LOAD_FAST                1 (builder)
    # 1494 LOAD_METHOD             23 (call)
    # 1516 LOAD_FAST               19 (getpid)
    # 1518 LOAD_GLOBAL             41 (NULL + tuple)
    # 1530 PRECALL                  0
    # 1534 CALL                     0
    # 1544 PRECALL                  2
    # 1548 CALL                     2
    # 1558 STORE_FAST              25 (parent_pid)
    # 143        1560 LOAD_FAST                1 (builder)
    # 1562 LOAD_METHOD             24 (store)
    # 1584 LOAD_FAST               25 (parent_pid)
    # 1586 LOAD_FAST               11 (pid)
    # 1588 PRECALL                  2
    # 1592 CALL                     2
    # 1602 POP_TOP
    # 144        1604 LOAD_FAST                1 (builder)
    # 1606 LOAD_METHOD             25 (gep)
    # 1628 LOAD_FAST               12 (pidstr)
    # 1630 LOAD_FAST               10 (zero_i32t)
    # 1632 BUILD_LIST               1
    # 1634 LOAD_CONST              17 (True)
    # 1636 KW_NAMES                24
    # 1638 PRECALL                  3
    # 1642 CALL                     3
    # 1652 STORE_FAST              26 (pidstr_ptr)
    # 145        1654 LOAD_FAST                1 (builder)
    # 1656 LOAD_METHOD             26 (load)
    # 1678 LOAD_FAST               11 (pid)
    # 1680 PRECALL                  1
    # 1684 CALL                     1
    # 1694 STORE_FAST              27 (pid_val)
    # 148        1696 LOAD_FAST                1 (builder)
    # 1698 LOAD_METHOD             23 (call)
    # 149        1720 LOAD_FAST               20 (snprintf)
    # 1722 LOAD_FAST               26 (pidstr_ptr)
    # 1724 PUSH_NULL
    # 1726 LOAD_FAST                8 (intp_t)
    # 1728 LOAD_CONST               6 (12)
    # 1730 PRECALL                  1
    # 1734 CALL                     1
    # 1744 LOAD_FAST               13 (intfmt)
    # 1746 LOAD_FAST               27 (pid_val)
    # 1748 BUILD_TUPLE              4
    # 148        1750 PRECALL                  2
    # 1754 CALL                     2
    # 1764 STORE_FAST              28 (stat)
    # 150        1766 LOAD_FAST                1 (builder)
    # 1768 LOAD_METHOD             27 (icmp_signed)
    # 1790 LOAD_CONST              25 ('>')
    # 1792 LOAD_FAST               28 (stat)
    # 1794 PUSH_NULL
    # 1796 LOAD_FAST                7 (int32_t)
    # 1798 LOAD_CONST               6 (12)
    # 1800 PRECALL                  1
    # 1804 CALL                     1
    # 1814 PRECALL                  3
    # 1818 CALL                     3
    # 1828 STORE_FAST              29 (invalid_write)
    # 151        1830 LOAD_FAST                1 (builder)
    # 1832 LOAD_METHOD             28 (if_then)
    # 1854 LOAD_FAST               29 (invalid_write)
    # 1856 LOAD_CONST              26 (False)
    # 1858 KW_NAMES                27
    # 1860 PRECALL                  2
    # 1864 CALL                     2
    # 1874 BEFORE_WITH
    # 1876 POP_TOP
    # 152        1878 LOAD_CONST              28 ('Internal error: `snprintf` buffer would have overflowed.')
    # 1880 STORE_FAST              30 (msg)
    # 153        1882 LOAD_DEREF               0 (cgctx)
    # 1884 LOAD_ATTR               29 (call_conv)
    # 1894 LOAD_METHOD             30 (return_user_exc)
    # 1916 LOAD_FAST                1 (builder)
    # 1918 LOAD_GLOBAL             62 (RuntimeError)
    # 1930 LOAD_FAST               30 (msg)
    # 1932 BUILD_TUPLE              1
    # 1934 PRECALL                  3
    # 1938 CALL                     3
    # 1948 POP_TOP
    # 151        1950 LOAD_CONST               0 (None)
    # 1952 LOAD_CONST               0 (None)
    # 1954 LOAD_CONST               0 (None)
    # 1956 PRECALL                  2
    # 1960 CALL                     2
    # 1970 POP_TOP
    # 1972 JUMP_FORWARD            11 (to 1996)
    # >> 1974 PUSH_EXC_INFO
    # 1976 WITH_EXCEPT_START
    # 1978 POP_JUMP_FORWARD_IF_TRUE     4 (to 1988)
    # 1980 RERAISE                  2
    # >> 1982 COPY                     3
    # 1984 POP_EXCEPT
    # 1986 RERAISE                  1
    # >> 1988 POP_TOP
    # 1990 POP_EXCEPT
    # 1992 POP_TOP
    # 1994 POP_TOP
    # 156     >> 1996 LOAD_FAST                1 (builder)
    # 1998 LOAD_METHOD             23 (call)
    # 2020 LOAD_FAST               21 (fork)
    # 2022 LOAD_GLOBAL             41 (NULL + tuple)
    # 2034 PRECALL                  0
    # 2038 CALL                     0
    # 2048 PRECALL                  2
    # 2052 CALL                     2
    # 2062 STORE_FAST              31 (child_pid)
    # 157        2064 LOAD_FAST                1 (builder)
    # 2066 LOAD_METHOD             27 (icmp_signed)
    # 2088 LOAD_CONST              29 ('==')
    # 2090 LOAD_FAST               31 (child_pid)
    # 2092 PUSH_NULL
    # 2094 LOAD_FAST                7 (int32_t)
    # 2096 LOAD_CONST              30 (-1)
    # 2098 PRECALL                  1
    # 2102 CALL                     1
    # 2112 PRECALL                  3
    # 2116 CALL                     3
    # 2126 STORE_FAST              32 (fork_failed)
    # 158        2128 LOAD_FAST                1 (builder)
    # 2130 LOAD_METHOD             28 (if_then)
    # 2152 LOAD_FAST               32 (fork_failed)
    # 2154 LOAD_CONST              26 (False)
    # 2156 KW_NAMES                27
    # 2158 PRECALL                  2
    # 2162 CALL                     2
    # 2172 BEFORE_WITH
    # 2174 POP_TOP
    # 159        2176 LOAD_CONST              31 ('Internal error: `fork` failed.')
    # 2178 STORE_FAST              30 (msg)
    # 160        2180 LOAD_DEREF               0 (cgctx)
    # 2182 LOAD_ATTR               29 (call_conv)
    # 2192 LOAD_METHOD             30 (return_user_exc)
    # 2214 LOAD_FAST                1 (builder)
    # 2216 LOAD_GLOBAL             62 (RuntimeError)
    # 2228 LOAD_FAST               30 (msg)
    # 2230 BUILD_TUPLE              1
    # 2232 PRECALL                  3
    # 2236 CALL                     3
    # 2246 POP_TOP
    # 158        2248 LOAD_CONST               0 (None)
    # 2250 LOAD_CONST               0 (None)
    # 2252 LOAD_CONST               0 (None)
    # 2254 PRECALL                  2
    # 2258 CALL                     2
    # 2268 POP_TOP
    # 2270 JUMP_FORWARD            11 (to 2294)
    # >> 2272 PUSH_EXC_INFO
    # 2274 WITH_EXCEPT_START
    # 2276 POP_JUMP_FORWARD_IF_TRUE     4 (to 2286)
    # 2278 RERAISE                  2
    # >> 2280 COPY                     3
    # 2282 POP_EXCEPT
    # 2284 RERAISE                  1
    # >> 2286 POP_TOP
    # 2288 POP_EXCEPT
    # 2290 POP_TOP
    # 2292 POP_TOP
    # 162     >> 2294 LOAD_FAST                1 (builder)
    # 2296 LOAD_METHOD             27 (icmp_signed)
    # 2318 LOAD_CONST              29 ('==')
    # 2320 LOAD_FAST               31 (child_pid)
    # 2322 LOAD_FAST               10 (zero_i32t)
    # 2324 PRECALL                  3
    # 2328 CALL                     3
    # 2338 STORE_FAST              33 (is_child)
    # 163        2340 LOAD_FAST                1 (builder)
    # 2342 LOAD_METHOD             32 (if_else)
    # 2364 LOAD_FAST               33 (is_child)
    # 2366 PRECALL                  1
    # 2370 CALL                     1
    # 2380 BEFORE_WITH
    # 2382 UNPACK_SEQUENCE          2
    # 2386 STORE_FAST              34 (then)
    # 2388 STORE_FAST              35 (orelse)
    # 164        2390 LOAD_FAST               34 (then)
    # 2392 BEFORE_WITH
    # 2394 POP_TOP
    # 166        2396 LOAD_GLOBAL              1 (NULL + ir)
    # 2408 LOAD_ATTR               33 (Constant)
    # 2418 LOAD_FAST                9 (char_ptr)
    # 2420 LOAD_CONST               0 (None)
    # 2422 PRECALL                  2
    # 2426 CALL                     2
    # 2436 STORE_FAST              36 (nullptr)
    # 167        2438 LOAD_FAST                1 (builder)
    # 2440 LOAD_METHOD             25 (gep)
    # 168        2462 LOAD_FAST               14 (gdb_str)
    # 2464 LOAD_FAST               10 (zero_i32t)
    # 2466 BUILD_LIST               1
    # 2468 LOAD_CONST              17 (True)
    # 167        2470 KW_NAMES                24
    # 2472 PRECALL                  3
    # 2476 CALL                     3
    # 2486 STORE_FAST              37 (gdb_str_ptr)
    # 169        2488 LOAD_FAST                1 (builder)
    # 2490 LOAD_METHOD             25 (gep)
    # 170        2512 LOAD_FAST               15 (attach_str)
    # 2514 LOAD_FAST               10 (zero_i32t)
    # 2516 BUILD_LIST               1
    # 2518 LOAD_CONST              17 (True)
    # 169        2520 KW_NAMES                24
    # 2522 PRECALL                  3
    # 2526 CALL                     3
    # 2536 STORE_FAST              38 (attach_str_ptr)
    # 171        2538 LOAD_GLOBAL             13 (NULL + cgutils)
    # 2550 LOAD_ATTR               34 (printf)
    # 172        2560 LOAD_FAST                1 (builder)
    # 2562 LOAD_CONST              32 ('Attaching to PID: %s\n')
    # 2564 LOAD_FAST               12 (pidstr)
    # 171        2566 PRECALL                  3
    # 2570 CALL                     3
    # 2580 POP_TOP
    # 174        2582 LOAD_FAST               37 (gdb_str_ptr)
    # 175        2584 LOAD_FAST               37 (gdb_str_ptr)
    # 176        2586 LOAD_FAST               38 (attach_str_ptr)
    # 177        2588 LOAD_FAST               26 (pidstr_ptr)
    # 173        2590 BUILD_TUPLE              4
    # 2592 STORE_FAST              39 (buf)
    # 178        2594 LOAD_FAST               39 (buf)
    # 2596 LOAD_GLOBAL             41 (NULL + tuple)
    # 2608 LOAD_FAST               17 (cmdlang)
    # 2610 PRECALL                  1
    # 2614 CALL                     1
    # 2624 BINARY_OP                0 (+)
    # 2628 LOAD_FAST               36 (nullptr)
    # 2630 BUILD_TUPLE              1
    # 2632 BINARY_OP                0 (+)
    # 2636 STORE_FAST              39 (buf)
    # 179        2638 LOAD_FAST                1 (builder)
    # 2640 LOAD_METHOD             23 (call)
    # 2662 LOAD_FAST               22 (execl)
    # 2664 LOAD_FAST               39 (buf)
    # 2666 PRECALL                  2
    # 2670 CALL                     2
    # 2680 POP_TOP
    # 164        2682 LOAD_CONST               0 (None)
    # 2684 LOAD_CONST               0 (None)
    # 2686 LOAD_CONST               0 (None)
    # 2688 PRECALL                  2
    # 2692 CALL                     2
    # 2702 POP_TOP
    # 2704 JUMP_FORWARD            11 (to 2728)
    # >> 2706 PUSH_EXC_INFO
    # 2708 WITH_EXCEPT_START
    # 2710 POP_JUMP_FORWARD_IF_TRUE     4 (to 2720)
    # 2712 RERAISE                  2
    # >> 2714 COPY                     3
    # 2716 POP_EXCEPT
    # 2718 RERAISE                  1
    # >> 2720 POP_TOP
    # 2722 POP_EXCEPT
    # 2724 POP_TOP
    # 2726 POP_TOP
    # 180     >> 2728 LOAD_FAST               35 (orelse)
    # 2730 BEFORE_WITH
    # 2732 POP_TOP
    # 182        2734 LOAD_FAST                1 (builder)
    # 2736 LOAD_METHOD             23 (call)
    # 2758 LOAD_FAST               23 (sleep)
    # 2760 PUSH_NULL
    # 2762 LOAD_FAST                7 (int32_t)
    # 2764 LOAD_CONST              33 (10)
    # 2766 PRECALL                  1
    # 2770 CALL                     1
    # 2780 BUILD_TUPLE              1
    # 2782 PRECALL                  2
    # 2786 CALL                     2
    # 2796 POP_TOP
    # 184        2798 LOAD_FAST                5 (do_break)
    # 2800 LOAD_CONST              17 (True)
    # 2802 IS_OP                    0
    # 2804 POP_JUMP_FORWARD_IF_FALSE    34 (to 2874)
    # 185        2806 LOAD_FAST                1 (builder)
    # 2808 LOAD_METHOD             23 (call)
    # 2830 LOAD_FAST               24 (breakpoint)
    # 2832 LOAD_GLOBAL             41 (NULL + tuple)
    # 2844 PRECALL                  0
    # 2848 CALL                     0
    # 2858 PRECALL                  2
    # 2862 CALL                     2
    # 2872 POP_TOP
    # 180     >> 2874 LOAD_CONST               0 (None)
    # 2876 LOAD_CONST               0 (None)
    # 2878 LOAD_CONST               0 (None)
    # 2880 PRECALL                  2
    # 2884 CALL                     2
    # 2894 POP_TOP
    # 2896 JUMP_FORWARD            11 (to 2920)
    # >> 2898 PUSH_EXC_INFO
    # 2900 WITH_EXCEPT_START
    # 2902 POP_JUMP_FORWARD_IF_TRUE     4 (to 2912)
    # 2904 RERAISE                  2
    # >> 2906 COPY                     3
    # 2908 POP_EXCEPT
    # 2910 RERAISE                  1
    # >> 2912 POP_TOP
    # 2914 POP_EXCEPT
    # 2916 POP_TOP
    # 2918 POP_TOP
    # 163     >> 2920 LOAD_CONST               0 (None)
    # 2922 LOAD_CONST               0 (None)
    # 2924 LOAD_CONST               0 (None)
    # 2926 PRECALL                  2
    # 2930 CALL                     2
    # 2940 POP_TOP
    # 2942 LOAD_CONST               0 (None)
    # 2944 RETURN_VALUE
    # >> 2946 PUSH_EXC_INFO
    # 2948 WITH_EXCEPT_START
    # 2950 POP_JUMP_FORWARD_IF_TRUE     4 (to 2960)
    # 2952 RERAISE                  2
    # >> 2954 COPY                     3
    # 2956 POP_EXCEPT
    # 2958 RERAISE                  1
    # >> 2960 POP_TOP
    # 2962 POP_EXCEPT
    # 2964 POP_TOP
    # 2966 POP_TOP
    # 2968 LOAD_CONST               0 (None)
    # 2970 RETURN_VALUE
    # ExceptionTable:
    # 1876 to 1948 -> 1974 [1] lasti
    # 1974 to 1980 -> 1982 [3] lasti
    # 1988 to 1988 -> 1982 [3] lasti
    # 2174 to 2246 -> 2272 [1] lasti
    # 2272 to 2278 -> 2280 [3] lasti
    # 2286 to 2286 -> 2280 [3] lasti
    # 2382 to 2392 -> 2946 [1] lasti
    # 2394 to 2680 -> 2706 [2] lasti
    # 2682 to 2704 -> 2946 [1] lasti
    # 2706 to 2712 -> 2714 [4] lasti
    # 2714 to 2718 -> 2946 [1] lasti
    # 2720 to 2720 -> 2714 [4] lasti
    # 2722 to 2730 -> 2946 [1] lasti
    # 2732 to 2872 -> 2898 [2] lasti
    # 2874 to 2896 -> 2946 [1] lasti
    # 2898 to 2904 -> 2906 [4] lasti
    # 2906 to 2910 -> 2946 [1] lasti
    # 2912 to 2912 -> 2906 [4] lasti
    # 2914 to 2918 -> 2946 [1] lasti
    # 2946 to 2952 -> 2954 [3] lasti
    # 2960 to 2960 -> 2954 [3] lasti
    # Disassembly of <code object <listcomp> at 0x000001EBD7DDFC30, file "numba\misc\gdb_hook.py", line 109>:
    # 109           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                29 (to 66)
    # 8 STORE_FAST               1 (x)
    # 10 LOAD_GLOBAL              1 (NULL + isinstance)
    # 22 LOAD_FAST                1 (x)
    # 24 LOAD_GLOBAL              2 (types)
    # 36 LOAD_ATTR                2 (StringLiteral)
    # 46 PRECALL                  2
    # 50 CALL                     2
    # 60 UNARY_NOT
    # 62 LIST_APPEND              2
    # 64 JUMP_BACKWARD           30 (to 6)
    # >>   66 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7E35A70, file "numba\misc\gdb_hook.py", line 111>:
    # 111           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                 9 (to 26)
    # 8 STORE_FAST               1 (x)
    # 10 LOAD_FAST                1 (x)
    # 12 LOAD_ATTR                0 (literal_value)
    # 22 LIST_APPEND              2
    # 24 JUMP_BACKWARD           10 (to 6)
    # >>   26 RETURN_VALUE
    # Disassembly of <code object <listcomp> at 0x000001EBD7DDFE30, file "numba\misc\gdb_hook.py", line 112>:
    # 0 COPY_FREE_VARS           2
    # 112           2 RESUME                   0
    # 4 BUILD_LIST               0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                24 (to 58)
    # 10 STORE_FAST               1 (x)
    # 12 LOAD_DEREF               2 (cgctx)
    # 14 LOAD_METHOD              0 (insert_const_string)
    # 36 LOAD_DEREF               3 (mod)
    # 38 LOAD_FAST                1 (x)
    # 40 PRECALL                  2
    # 44 CALL                     2
    # 54 LIST_APPEND              2
    # 56 JUMP_BACKWARD           25 (to 8)
    # >>   58 RETURN_VALUE

def gen_gdb_impl(const_args, do_break):
    # 0 MAKE_CELL                0 (const_args)
    # 2 MAKE_CELL                1 (do_break)
    # 188           4 RESUME                   0
    # 189           6 LOAD_GLOBAL              0 (intrinsic)
    # 190          18 LOAD_CLOSURE             0 (const_args)
    # 20 LOAD_CLOSURE             1 (do_break)
    # 22 BUILD_TUPLE              2
    # 24 LOAD_CONST               1 (<code object gdb_internal at 0x000001EBD7DDF430, file "numba\misc\gdb_hook.py", line 189>)
    # 26 MAKE_FUNCTION            8 (closure)
    # 189          28 PRECALL                  0
    # 32 CALL                     0
    # 190          42 STORE_FAST               2 (gdb_internal)
    # 198          44 LOAD_FAST                2 (gdb_internal)
    # 46 RETURN_VALUE
    # Disassembly of <code object gdb_internal at 0x000001EBD7DDF430, file "numba\misc\gdb_hook.py", line 189>:
    # 0 COPY_FREE_VARS           2
    # 189           2 RESUME                   0
    # 191           4 LOAD_GLOBAL              1 (NULL + types)
    # 16 LOAD_ATTR                1 (void)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               1 (function_sig)
    # 193          42 LOAD_CLOSURE             3 (const_args)
    # 44 LOAD_CLOSURE             4 (do_break)
    # 46 BUILD_TUPLE              2
    # 48 LOAD_CONST               1 (<code object codegen at 0x000001EBD7E30C10, file "numba\misc\gdb_hook.py", line 193>)
    # 50 MAKE_FUNCTION            8 (closure)
    # 52 STORE_FAST               2 (codegen)
    # 197          54 LOAD_FAST                1 (function_sig)
    # 56 LOAD_FAST                2 (codegen)
    # 58 BUILD_TUPLE              2
    # 60 RETURN_VALUE
    # Disassembly of <code object codegen at 0x000001EBD7E30C10, file "numba\misc\gdb_hook.py", line 193>:
    # 0 COPY_FREE_VARS           2
    # 193           2 RESUME                   0
    # 194           4 LOAD_GLOBAL              1 (NULL + init_gdb_codegen)
    # 16 LOAD_FAST                0 (cgctx)
    # 18 LOAD_FAST                1 (builder)
    # 20 LOAD_FAST                2 (signature)
    # 22 LOAD_FAST                3 (args)
    # 24 LOAD_DEREF               4 (const_args)
    # 195          26 LOAD_DEREF               5 (do_break)
    # 194          28 KW_NAMES                 1
    # 30 PRECALL                  6
    # 34 CALL                     6
    # 44 POP_TOP
    # 196          46 LOAD_FAST                0 (cgctx)
    # 48 LOAD_METHOD              1 (get_constant)
    # 70 LOAD_GLOBAL              4 (types)
    # 82 LOAD_ATTR                3 (none)
    # 92 LOAD_CONST               0 (None)
    # 94 PRECALL                  2
    # 98 CALL                     2
    # 108 RETURN_VALUE

def hook_gdb_breakpoint():
    """
    Adds the Numba break point into the source
    """
    # 0 MAKE_CELL                1 (bp_impl)
    # 201           2 RESUME                   0
    # 206           4 LOAD_GLOBAL              0 (sys)
    # 16 LOAD_ATTR                1 (platform)
    # 26 LOAD_METHOD              2 (startswith)
    # 48 LOAD_CONST               1 ('linux')
    # 50 PRECALL                  1
    # 54 CALL                     1
    # 64 POP_JUMP_FORWARD_IF_TRUE    15 (to 96)
    # 207          66 LOAD_GLOBAL              7 (NULL + RuntimeError)
    # 78 LOAD_CONST               2 ('gdb is only available on linux')
    # 80 PRECALL                  1
    # 84 CALL                     1
    # 94 RAISE_VARARGS            1
    # 208     >>   96 LOAD_GLOBAL              9 (NULL + gen_bp_impl)
    # 108 PRECALL                  0
    # 112 CALL                     0
    # 122 STORE_DEREF              1 (bp_impl)
    # 210         124 LOAD_CLOSURE             1 (bp_impl)
    # 126 BUILD_TUPLE              1
    # 128 LOAD_CONST               3 (<code object impl at 0x000001EBD7E365D0, file "numba\misc\gdb_hook.py", line 210>)
    # 130 MAKE_FUNCTION            8 (closure)
    # 132 STORE_FAST               0 (impl)
    # 212         134 LOAD_FAST                0 (impl)
    # 136 RETURN_VALUE
    # Disassembly of <code object impl at 0x000001EBD7E365D0, file "numba\misc\gdb_hook.py", line 210>:
    # 0 COPY_FREE_VARS           1
    # 210           2 RESUME                   0
    # 211           4 PUSH_NULL
    # 6 LOAD_DEREF               0 (bp_impl)
    # 8 PRECALL                  0
    # 12 CALL                     0
    # 22 POP_TOP
    # 24 LOAD_CONST               0 (None)
    # 26 RETURN_VALUE

def gen_bp_impl():
    # 215           0 RESUME                   0
    # 216           2 LOAD_GLOBAL              0 (intrinsic)
    # 217          14 LOAD_CONST               1 (<code object bp_internal at 0x000001EBD7E225B0, file "numba\misc\gdb_hook.py", line 216>)
    # 16 MAKE_FUNCTION            0
    # 216          18 PRECALL                  0
    # 22 CALL                     0
    # 217          32 STORE_FAST               0 (bp_internal)
    # 228          34 LOAD_FAST                0 (bp_internal)
    # 36 RETURN_VALUE
    # Disassembly of <code object bp_internal at 0x000001EBD7E225B0, file "numba\misc\gdb_hook.py", line 216>:
    # 216           0 RESUME                   0
    # 218           2 LOAD_GLOBAL              1 (NULL + types)
    # 14 LOAD_ATTR                1 (void)
    # 24 PRECALL                  0
    # 28 CALL                     0
    # 38 STORE_FAST               1 (function_sig)
    # 220          40 LOAD_CONST               1 (<code object codegen at 0x000001EBD70D23D0, file "numba\misc\gdb_hook.py", line 220>)
    # 42 MAKE_FUNCTION            0
    # 44 STORE_FAST               2 (codegen)
    # 227          46 LOAD_FAST                1 (function_sig)
    # 48 LOAD_FAST                2 (codegen)
    # 50 BUILD_TUPLE              2
    # 52 RETURN_VALUE
    # Disassembly of <code object codegen at 0x000001EBD70D23D0, file "numba\misc\gdb_hook.py", line 220>:
    # 220           0 RESUME                   0
    # 221           2 LOAD_FAST                1 (builder)
    # 4 LOAD_ATTR                0 (module)
    # 14 STORE_FAST               4 (mod)
    # 222          16 LOAD_GLOBAL              3 (NULL + ir)
    # 28 LOAD_ATTR                2 (FunctionType)
    # 38 LOAD_GLOBAL              3 (NULL + ir)
    # 50 LOAD_ATTR                3 (VoidType)
    # 60 PRECALL                  0
    # 64 CALL                     0
    # 74 LOAD_GLOBAL              9 (NULL + tuple)
    # 86 PRECALL                  0
    # 90 CALL                     0
    # 100 PRECALL                  2
    # 104 CALL                     2
    # 114 STORE_FAST               5 (fnty)
    # 223         116 LOAD_GLOBAL             11 (NULL + cgutils)
    # 128 LOAD_ATTR                6 (get_or_insert_function)
    # 138 LOAD_FAST                4 (mod)
    # 140 LOAD_FAST                5 (fnty)
    # 224         142 LOAD_CONST               1 ('numba_gdb_breakpoint')
    # 223         144 PRECALL                  3
    # 148 CALL                     3
    # 158 STORE_FAST               6 (breakpoint)
    # 225         160 LOAD_FAST                1 (builder)
    # 162 LOAD_METHOD              7 (call)
    # 184 LOAD_FAST                6 (breakpoint)
    # 186 LOAD_GLOBAL              9 (NULL + tuple)
    # 198 PRECALL                  0
    # 202 CALL                     0
    # 212 PRECALL                  2
    # 216 CALL                     2
    # 226 POP_TOP
    # 226         228 LOAD_FAST                0 (cgctx)
    # 230 LOAD_METHOD              8 (get_constant)
    # 252 LOAD_GLOBAL             18 (types)
    # 264 LOAD_ATTR               10 (none)
    # 274 LOAD_CONST               0 (None)
    # 276 PRECALL                  2
    # 280 CALL                     2
    # 290 RETURN_VALUE
