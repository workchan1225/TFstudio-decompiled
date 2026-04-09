# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: multiprocessing\popen_spawn_win32.py

import os
import msvcrt
import signal
import sys
import _winapi
from context import reduction
from  import spawn
from  import util

def _path_eq(p1, p2):
    # 23           0 RESUME                   0
    # 24           2 LOAD_FAST                0 (p1)
    # 4 LOAD_FAST                1 (p2)
    # 6 COMPARE_OP               2 (==)
    # 12 JUMP_IF_TRUE_OR_POP     63 (to 140)
    # 14 LOAD_GLOBAL              0 (os)
    # 26 LOAD_ATTR                1 (path)
    # 36 LOAD_METHOD              2 (normcase)
    # 58 LOAD_FAST                0 (p1)
    # 60 PRECALL                  1
    # 64 CALL                     1
    # 74 LOAD_GLOBAL              0 (os)
    # 86 LOAD_ATTR                1 (path)
    # 96 LOAD_METHOD              2 (normcase)
    # 118 LOAD_FAST                1 (p2)
    # 120 PRECALL                  1
    # 124 CALL                     1
    # 134 COMPARE_OP               2 (==)
    # >>  140 RETURN_VALUE

def _close_handles():
    # 29           0 RESUME                   0
    # 30           2 LOAD_FAST                0 (handles)
    # 4 GET_ITER
    # >>    6 FOR_ITER                22 (to 52)
    # 8 STORE_FAST               1 (handle)
    # 31          10 LOAD_GLOBAL              1 (NULL + _winapi)
    # 22 LOAD_ATTR                1 (CloseHandle)
    # 32 LOAD_FAST                1 (handle)
    # 34 PRECALL                  1
    # 38 CALL                     1
    # 48 POP_TOP
    # 50 JUMP_BACKWARD           23 (to 6)
    # 30     >>   52 LOAD_CONST               0 (None)
    # 54 RETURN_VALUE

class Popen:
    """Popen"""
    def __init__(self, process_obj):
        # 45           0 RESUME                   0
        # 46           2 LOAD_GLOBAL              1 (NULL + spawn)
        # 14 LOAD_ATTR                1 (get_preparation_data)
        # 24 LOAD_FAST                1 (process_obj)
        # 26 LOAD_ATTR                2 (_name)
        # 36 PRECALL                  1
        # 40 CALL                     1
        # 50 STORE_FAST               2 (prep_data)
        # 54          52 LOAD_GLOBAL              7 (NULL + _winapi)
        # 64 LOAD_ATTR                4 (CreatePipe)
        # 74 LOAD_CONST               0 (None)
        # 76 LOAD_CONST               1 (0)
        # 78 PRECALL                  2
        # 82 CALL                     2
        # 92 UNPACK_SEQUENCE          2
        # 96 STORE_FAST               3 (rhandle)
        # 98 STORE_FAST               4 (whandle)
        # 55         100 LOAD_GLOBAL             11 (NULL + msvcrt)
        # 112 LOAD_ATTR                6 (open_osfhandle)
        # 122 LOAD_FAST                4 (whandle)
        # 124 LOAD_CONST               1 (0)
        # 126 PRECALL                  2
        # 130 CALL                     2
        # 140 STORE_FAST               5 (wfd)
        # 56         142 LOAD_GLOBAL              1 (NULL + spawn)
        # 154 LOAD_ATTR                7 (get_command_line)
        # 164 LOAD_GLOBAL             17 (NULL + os)
        # 176 LOAD_ATTR                9 (getpid)
        # 186 PRECALL                  0
        # 190 CALL                     0
        # 57         200 LOAD_FAST                3 (rhandle)
        # 56         202 KW_NAMES                 2
        # 204 PRECALL                  2
        # 208 CALL                     2
        # 218 STORE_FAST               6 (cmd)
        # 59         220 LOAD_GLOBAL              1 (NULL + spawn)
        # 232 LOAD_ATTR               10 (get_executable)
        # 242 PRECALL                  0
        # 246 CALL                     0
        # 256 STORE_FAST               7 (python_exe)
        # 63         258 LOAD_GLOBAL             22 (WINENV)
        # 270 POP_JUMP_FORWARD_IF_FALSE    89 (to 450)
        # 272 LOAD_GLOBAL             25 (NULL + _path_eq)
        # 284 LOAD_FAST                7 (python_exe)
        # 286 LOAD_GLOBAL             26 (sys)
        # 298 LOAD_ATTR               14 (executable)
        # 308 PRECALL                  2
        # 312 CALL                     2
        # 322 POP_JUMP_FORWARD_IF_FALSE    63 (to 450)
        # 64         324 LOAD_GLOBAL             26 (sys)
        # 336 LOAD_ATTR               15 (_base_executable)
        # 346 COPY                     1
        # 348 LOAD_FAST                6 (cmd)
        # 350 LOAD_CONST               1 (0)
        # 352 STORE_SUBSCR
        # 356 STORE_FAST               7 (python_exe)
        # 65         358 LOAD_GLOBAL             16 (os)
        # 370 LOAD_ATTR               16 (environ)
        # 380 LOAD_METHOD             17 (copy)
        # 402 PRECALL                  0
        # 406 CALL                     0
        # 416 STORE_FAST               8 (env)
        # 66         418 LOAD_GLOBAL             26 (sys)
        # 430 LOAD_ATTR               14 (executable)
        # 440 LOAD_FAST                8 (env)
        # 442 LOAD_CONST               3 ('__PYVENV_LAUNCHER__')
        # 444 STORE_SUBSCR
        # 448 JUMP_FORWARD             2 (to 454)
        # 68     >>  450 LOAD_CONST               0 (None)
        # 452 STORE_FAST               8 (env)
        # 70     >>  454 LOAD_CONST               4 (' ')
        # 456 LOAD_METHOD             18 (join)
        # 478 LOAD_CONST               5 (<code object <genexpr> at 0x000001EBD7E36B10, file "multiprocessing\popen_spawn_win32.py", line 70>)
        # 480 MAKE_FUNCTION            0
        # 482 LOAD_FAST                6 (cmd)
        # 484 GET_ITER
        # 486 PRECALL                  0
        # 490 CALL                     0
        # 500 PRECALL                  1
        # 504 CALL                     1
        # 514 STORE_FAST               6 (cmd)
        # 72         516 LOAD_GLOBAL             39 (NULL + open)
        # 528 LOAD_FAST                5 (wfd)
        # 530 LOAD_CONST               6 ('wb')
        # 532 LOAD_CONST               7 (True)
        # 534 KW_NAMES                 8
        # 536 PRECALL                  3
        # 540 CALL                     3
        # 550 BEFORE_WITH
        # 552 STORE_FAST               9 (to_child)
        # 74         554 NOP
        # 75         556 LOAD_GLOBAL              7 (NULL + _winapi)
        # 568 LOAD_ATTR               20 (CreateProcess)
        # 76         578 LOAD_FAST                7 (python_exe)
        # 580 LOAD_FAST                6 (cmd)
        # 77         582 LOAD_CONST               0 (None)
        # 584 LOAD_CONST               0 (None)
        # 586 LOAD_CONST               9 (False)
        # 588 LOAD_CONST               1 (0)
        # 590 LOAD_FAST                8 (env)
        # 592 LOAD_CONST               0 (None)
        # 594 LOAD_CONST               0 (None)
        # 75         596 PRECALL                  9
        # 600 CALL                     9
        # 610 UNPACK_SEQUENCE          4
        # 614 STORE_FAST              10 (hp)
        # 616 STORE_FAST              11 (ht)
        # 618 STORE_FAST              12 (pid)
        # 620 STORE_FAST              13 (tid)
        # 78         622 LOAD_GLOBAL              7 (NULL + _winapi)
        # 634 LOAD_ATTR               21 (CloseHandle)
        # 644 LOAD_FAST               11 (ht)
        # 646 PRECALL                  1
        # 650 CALL                     1
        # 660 POP_TOP
        # 662 JUMP_FORWARD            26 (to 716)
        # >>  664 PUSH_EXC_INFO
        # 79         666 POP_TOP
        # 80         668 LOAD_GLOBAL              7 (NULL + _winapi)
        # 680 LOAD_ATTR               21 (CloseHandle)
        # 690 LOAD_FAST                3 (rhandle)
        # 692 PRECALL                  1
        # 696 CALL                     1
        # 706 POP_TOP
        # 81         708 RAISE_VARARGS            0
        # >>  710 COPY                     3
        # 712 POP_EXCEPT
        # 714 RERAISE                  1
        # 84     >>  716 LOAD_FAST               12 (pid)
        # 718 LOAD_FAST                0 (self)
        # 720 STORE_ATTR              22 (pid)
        # 85         730 LOAD_CONST               0 (None)
        # 732 LOAD_FAST                0 (self)
        # 734 STORE_ATTR              23 (returncode)
        # 86         744 LOAD_FAST               10 (hp)
        # 746 LOAD_FAST                0 (self)
        # 748 STORE_ATTR              24 (_handle)
        # 87         758 LOAD_GLOBAL             51 (NULL + int)
        # 770 LOAD_FAST               10 (hp)
        # 772 PRECALL                  1
        # 776 CALL                     1
        # 786 LOAD_FAST                0 (self)
        # 788 STORE_ATTR              26 (sentinel)
        # 88         798 LOAD_GLOBAL             55 (NULL + util)
        # 810 LOAD_ATTR               28 (Finalize)
        # 820 LOAD_FAST                0 (self)
        # 822 LOAD_GLOBAL             58 (_close_handles)
        # 89         834 LOAD_FAST                0 (self)
        # 836 LOAD_ATTR               26 (sentinel)
        # 846 LOAD_GLOBAL             51 (NULL + int)
        # 858 LOAD_FAST                3 (rhandle)
        # 860 PRECALL                  1
        # 864 CALL                     1
        # 874 BUILD_TUPLE              2
        # 88         876 PRECALL                  3
        # 880 CALL                     3
        # 890 LOAD_FAST                0 (self)
        # 892 STORE_ATTR              30 (finalizer)
        # 92         902 LOAD_GLOBAL             63 (NULL + set_spawning_popen)
        # 914 LOAD_FAST                0 (self)
        # 916 PRECALL                  1
        # 920 CALL                     1
        # 930 POP_TOP
        # 93         932 NOP
        # 94         934 LOAD_GLOBAL             65 (NULL + reduction)
        # 946 LOAD_ATTR               33 (dump)
        # 956 LOAD_FAST                2 (prep_data)
        # 958 LOAD_FAST                9 (to_child)
        # 960 PRECALL                  2
        # 964 CALL                     2
        # 974 POP_TOP
        # 95         976 LOAD_GLOBAL             65 (NULL + reduction)
        # 988 LOAD_ATTR               33 (dump)
        # 998 LOAD_FAST                1 (process_obj)
        # 1000 LOAD_FAST                9 (to_child)
        # 1002 PRECALL                  2
        # 1006 CALL                     2
        # 1016 POP_TOP
        # 97        1018 LOAD_GLOBAL             63 (NULL + set_spawning_popen)
        # 1030 LOAD_CONST               0 (None)
        # 1032 PRECALL                  1
        # 1036 CALL                     1
        # 1046 POP_TOP
        # 1048 JUMP_FORWARD            20 (to 1090)
        # >> 1050 PUSH_EXC_INFO
        # 1052 LOAD_GLOBAL             63 (NULL + set_spawning_popen)
        # 1064 LOAD_CONST               0 (None)
        # 1066 PRECALL                  1
        # 1070 CALL                     1
        # 1080 POP_TOP
        # 1082 RERAISE                  0
        # >> 1084 COPY                     3
        # 1086 POP_EXCEPT
        # 1088 RERAISE                  1
        # >> 1090 NOP
        # 72        1092 LOAD_CONST               0 (None)
        # 1094 LOAD_CONST               0 (None)
        # 1096 LOAD_CONST               0 (None)
        # 1098 PRECALL                  2
        # 1102 CALL                     2
        # 1112 POP_TOP
        # 1114 LOAD_CONST               0 (None)
        # 1116 RETURN_VALUE
        # >> 1118 PUSH_EXC_INFO
        # 1120 WITH_EXCEPT_START
        # 1122 POP_JUMP_FORWARD_IF_TRUE     4 (to 1132)
        # 1124 RERAISE                  2
        # >> 1126 COPY                     3
        # 1128 POP_EXCEPT
        # 1130 RERAISE                  1
        # >> 1132 POP_TOP
        # 1134 POP_EXCEPT
        # 1136 POP_TOP
        # 1138 POP_TOP
        # 1140 LOAD_CONST               0 (None)
        # 1142 RETURN_VALUE
        # ExceptionTable:
        # 552 to 552 -> 1118 [1] lasti
        # 556 to 660 -> 664 [1]
        # 662 to 662 -> 1118 [1] lasti
        # 664 to 708 -> 710 [2] lasti
        # 710 to 930 -> 1118 [1] lasti
        # 934 to 1016 -> 1050 [1]
        # 1018 to 1048 -> 1118 [1] lasti
        # 1050 to 1082 -> 1084 [2] lasti
        # 1084 to 1088 -> 1118 [1] lasti
        # 1118 to 1124 -> 1126 [3] lasti
        # 1132 to 1132 -> 1126 [3] lasti
        # Disassembly of <code object <genexpr> at 0x000001EBD7E36B10, file "multiprocessing\popen_spawn_win32.py", line 70>:
        # 70           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                 9 (to 28)
        # 10 STORE_FAST               1 (x)
        # 12 LOAD_CONST               0 ('"%s"')
        # 14 LOAD_FAST                1 (x)
        # 16 BINARY_OP                6 (%)
        # 20 YIELD_VALUE
        # 22 RESUME                   1
        # 24 POP_TOP
        # 26 JUMP_BACKWARD           10 (to 8)
        # >>   28 LOAD_CONST               1 (None)
        # 30 RETURN_VALUE

    def duplicate_for_child(self, handle):
        # 99           0 RESUME                   0
        # 100           2 LOAD_FAST                0 (self)
        # 4 LOAD_GLOBAL              1 (NULL + get_spawning_popen)
        # 16 PRECALL                  0
        # 20 CALL                     0
        # 30 IS_OP                    0
        # 32 POP_JUMP_FORWARD_IF_TRUE     2 (to 38)
        # 34 LOAD_ASSERTION_ERROR
        # 36 RAISE_VARARGS            1
        # 101     >>   38 LOAD_GLOBAL              3 (NULL + reduction)
        # 50 LOAD_ATTR                2 (duplicate)
        # 60 LOAD_FAST                1 (handle)
        # 62 LOAD_FAST                0 (self)
        # 64 LOAD_ATTR                3 (sentinel)
        # 74 PRECALL                  2
        # 78 CALL                     2
        # 88 RETURN_VALUE

    def wait(self, timeout):
        # 103           0 RESUME                   0
        # 104           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (returncode)
        # 14 POP_JUMP_FORWARD_IF_NONE     7 (to 30)
        # 105          16 LOAD_FAST                0 (self)
        # 18 LOAD_ATTR                0 (returncode)
        # 28 RETURN_VALUE
        # 107     >>   30 LOAD_FAST                1 (timeout)
        # 32 POP_JUMP_FORWARD_IF_NOT_NONE    13 (to 60)
        # 108          34 LOAD_GLOBAL              2 (_winapi)
        # 46 LOAD_ATTR                2 (INFINITE)
        # 56 STORE_FAST               2 (msecs)
        # 58 JUMP_FORWARD            35 (to 130)
        # 110     >>   60 LOAD_GLOBAL              7 (NULL + max)
        # 72 LOAD_CONST               1 (0)
        # 74 LOAD_GLOBAL              9 (NULL + int)
        # 86 LOAD_FAST                1 (timeout)
        # 88 LOAD_CONST               2 (1000)
        # 90 BINARY_OP                5 (*)
        # 94 LOAD_CONST               3 (0.5)
        # 96 BINARY_OP                0 (+)
        # 100 PRECALL                  1
        # 104 CALL                     1
        # 114 PRECALL                  2
        # 118 CALL                     2
        # 128 STORE_FAST               2 (msecs)
        # 112     >>  130 LOAD_GLOBAL              3 (NULL + _winapi)
        # 142 LOAD_ATTR                5 (WaitForSingleObject)
        # 152 LOAD_GLOBAL              9 (NULL + int)
        # 164 LOAD_FAST                0 (self)
        # 166 LOAD_ATTR                6 (_handle)
        # 176 PRECALL                  1
        # 180 CALL                     1
        # 190 LOAD_FAST                2 (msecs)
        # 192 PRECALL                  2
        # 196 CALL                     2
        # 206 STORE_FAST               3 (res)
        # 113         208 LOAD_FAST                3 (res)
        # 210 LOAD_GLOBAL              2 (_winapi)
        # 222 LOAD_ATTR                7 (WAIT_OBJECT_0)
        # 232 COMPARE_OP               2 (==)
        # 238 POP_JUMP_FORWARD_IF_FALSE    56 (to 352)
        # 114         240 LOAD_GLOBAL              3 (NULL + _winapi)
        # 252 LOAD_ATTR                8 (GetExitCodeProcess)
        # 262 LOAD_FAST                0 (self)
        # 264 LOAD_ATTR                6 (_handle)
        # 274 PRECALL                  1
        # 278 CALL                     1
        # 288 STORE_FAST               4 (code)
        # 115         290 LOAD_FAST                4 (code)
        # 292 LOAD_GLOBAL             18 (TERMINATE)
        # 304 COMPARE_OP               2 (==)
        # 310 POP_JUMP_FORWARD_IF_FALSE    13 (to 338)
        # 116         312 LOAD_GLOBAL             20 (signal)
        # 324 LOAD_ATTR               11 (SIGTERM)
        # 334 UNARY_NEGATIVE
        # 336 STORE_FAST               4 (code)
        # 117     >>  338 LOAD_FAST                4 (code)
        # 340 LOAD_FAST                0 (self)
        # 342 STORE_ATTR               0 (returncode)
        # 119     >>  352 LOAD_FAST                0 (self)
        # 354 LOAD_ATTR                0 (returncode)
        # 364 RETURN_VALUE

    def poll(self):
        # 121           0 RESUME                   0
        # 122           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (wait)
        # 26 LOAD_CONST               1 (0)
        # 28 KW_NAMES                 2
        # 30 PRECALL                  1
        # 34 CALL                     1
        # 44 RETURN_VALUE

    def terminate(self):
        # 124           0 RESUME                   0
        # 125           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (returncode)
        # 14 POP_JUMP_FORWARD_IF_NONE     2 (to 20)
        # 126          16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE
        # 128     >>   20 NOP
        # 129          22 LOAD_GLOBAL              3 (NULL + _winapi)
        # 34 LOAD_ATTR                2 (TerminateProcess)
        # 44 LOAD_GLOBAL              7 (NULL + int)
        # 56 LOAD_FAST                0 (self)
        # 58 LOAD_ATTR                4 (_handle)
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 LOAD_GLOBAL             10 (TERMINATE)
        # 94 PRECALL                  2
        # 98 CALL                     2
        # 108 POP_TOP
        # 110 LOAD_CONST               0 (None)
        # 112 RETURN_VALUE
        # >>  114 PUSH_EXC_INFO
        # 130         116 LOAD_GLOBAL             12 (PermissionError)
        # 128 CHECK_EXC_MATCH
        # 130 POP_JUMP_FORWARD_IF_FALSE    59 (to 250)
        # 132 POP_TOP
        # 133         134 LOAD_GLOBAL              3 (NULL + _winapi)
        # 146 LOAD_ATTR                7 (GetExitCodeProcess)
        # 156 LOAD_GLOBAL              7 (NULL + int)
        # 168 LOAD_FAST                0 (self)
        # 170 LOAD_ATTR                4 (_handle)
        # 180 PRECALL                  1
        # 184 CALL                     1
        # 194 PRECALL                  1
        # 198 CALL                     1
        # 208 STORE_FAST               1 (code)
        # 134         210 LOAD_FAST                1 (code)
        # 212 LOAD_GLOBAL              2 (_winapi)
        # 224 LOAD_ATTR                8 (STILL_ACTIVE)
        # 234 COMPARE_OP               2 (==)
        # 240 POP_JUMP_FORWARD_IF_FALSE     1 (to 244)
        # 135         242 RAISE_VARARGS            0
        # 134     >>  244 POP_EXCEPT
        # 246 LOAD_CONST               0 (None)
        # 248 RETURN_VALUE
        # 130     >>  250 RERAISE                  0
        # >>  252 COPY                     3
        # 254 POP_EXCEPT
        # 256 RERAISE                  1
        # ExceptionTable:
        # 22 to 108 -> 114 [0]
        # 114 to 242 -> 252 [1] lasti
        # 250 to 250 -> 252 [1] lasti

    def close(self):
        # 144           0 RESUME                   0
        # 145           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (finalizer)
        # 26 PRECALL                  0
        # 30 CALL                     0
        # 40 POP_TOP
        # 42 LOAD_CONST               0 (None)
        # 44 RETURN_VALUE

