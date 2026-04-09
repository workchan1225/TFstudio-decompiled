# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: joblib\externals\loky\backend\popen_loky_win32.py

import os
import sys
import msvcrt
import _winapi
from pickle import load
from multiprocessing import process
from multiprocessing.context import set_spawning_popen
from multiprocessing.popen_spawn_win32 import Popen
from  import reduction

def _path_eq(p1, p2):
    # 20           0 RESUME                   0
    # 21           2 LOAD_FAST                0 (p1)
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
        # 55           0 RESUME                   0
        # 56           2 LOAD_GLOBAL              1 (NULL + spawn)
        # 14 LOAD_ATTR                1 (get_preparation_data)
        # 57          24 LOAD_FAST                1 (process_obj)
        # 26 LOAD_ATTR                2 (_name)
        # 36 LOAD_GLOBAL              7 (NULL + getattr)
        # 48 LOAD_FAST                1 (process_obj)
        # 50 LOAD_CONST               1 ('init_main_module')
        # 52 LOAD_CONST               2 (True)
        # 54 PRECALL                  3
        # 58 CALL                     3
        # 56          68 PRECALL                  2
        # 72 CALL                     2
        # 82 STORE_FAST               2 (prep_data)
        # 66          84 LOAD_GLOBAL              9 (NULL + _winapi)
        # 96 LOAD_ATTR                5 (CreatePipe)
        # 106 LOAD_CONST               0 (None)
        # 108 LOAD_CONST               3 (0)
        # 110 PRECALL                  2
        # 114 CALL                     2
        # 124 UNPACK_SEQUENCE          2
        # 128 STORE_FAST               3 (rhandle)
        # 130 STORE_FAST               4 (whandle)
        # 67         132 LOAD_GLOBAL             13 (NULL + msvcrt)
        # 144 LOAD_ATTR                7 (open_osfhandle)
        # 154 LOAD_FAST                4 (whandle)
        # 156 LOAD_CONST               3 (0)
        # 158 PRECALL                  2
        # 162 CALL                     2
        # 172 STORE_FAST               5 (wfd)
        # 68         174 LOAD_GLOBAL             17 (NULL + get_command_line)
        # 186 LOAD_GLOBAL             19 (NULL + os)
        # 198 LOAD_ATTR               10 (getpid)
        # 208 PRECALL                  0
        # 212 CALL                     0
        # 222 LOAD_FAST                3 (rhandle)
        # 224 KW_NAMES                 4
        # 226 PRECALL                  2
        # 230 CALL                     2
        # 240 STORE_FAST               6 (cmd)
        # 70         242 LOAD_GLOBAL              1 (NULL + spawn)
        # 254 LOAD_ATTR               11 (get_executable)
        # 264 PRECALL                  0
        # 268 CALL                     0
        # 278 STORE_FAST               7 (python_exe)
        # 73         280 BUILD_MAP                0
        # 282 LOAD_GLOBAL             18 (os)
        # 294 LOAD_ATTR               12 (environ)
        # 304 DICT_UPDATE              1
        # 306 LOAD_FAST                1 (process_obj)
        # 308 LOAD_ATTR               13 (env)
        # 318 DICT_UPDATE              1
        # 320 STORE_FAST               8 (child_env)
        # 77         322 LOAD_GLOBAL             28 (WINENV)
        # 334 POP_JUMP_FORWARD_IF_FALSE    58 (to 452)
        # 336 LOAD_GLOBAL             31 (NULL + _path_eq)
        # 348 LOAD_FAST                7 (python_exe)
        # 350 LOAD_GLOBAL             32 (sys)
        # 362 LOAD_ATTR               17 (executable)
        # 372 PRECALL                  2
        # 376 CALL                     2
        # 386 POP_JUMP_FORWARD_IF_FALSE    32 (to 452)
        # 78         388 LOAD_GLOBAL             32 (sys)
        # 400 LOAD_ATTR               18 (_base_executable)
        # 410 COPY                     1
        # 412 LOAD_FAST                6 (cmd)
        # 414 LOAD_CONST               3 (0)
        # 416 STORE_SUBSCR
        # 420 STORE_FAST               7 (python_exe)
        # 79         422 LOAD_GLOBAL             32 (sys)
        # 434 LOAD_ATTR               17 (executable)
        # 444 LOAD_FAST                8 (child_env)
        # 446 LOAD_CONST               5 ('__PYVENV_LAUNCHER__')
        # 448 STORE_SUBSCR
        # 81     >>  452 LOAD_CONST               6 (' ')
        # 454 LOAD_METHOD             19 (join)
        # 476 LOAD_CONST               7 (<code object <genexpr> at 0x000001EBD7E350D0, file "joblib\externals\loky\backend\popen_loky_win32.py", line 81>)
        # 478 MAKE_FUNCTION            0
        # 480 LOAD_FAST                6 (cmd)
        # 482 GET_ITER
        # 484 PRECALL                  0
        # 488 CALL                     0
        # 498 PRECALL                  1
        # 502 CALL                     1
        # 512 STORE_FAST               6 (cmd)
        # 83         514 LOAD_GLOBAL             41 (NULL + open)
        # 526 LOAD_FAST                5 (wfd)
        # 528 LOAD_CONST               8 ('wb')
        # 530 PRECALL                  2
        # 534 CALL                     2
        # 544 BEFORE_WITH
        # 546 STORE_FAST               9 (to_child)
        # 85         548 NOP
        # 86         550 LOAD_GLOBAL              9 (NULL + _winapi)
        # 562 LOAD_ATTR               21 (CreateProcess)
        # 87         572 LOAD_FAST                7 (python_exe)
        # 88         574 LOAD_FAST                6 (cmd)
        # 89         576 LOAD_CONST               0 (None)
        # 90         578 LOAD_CONST               0 (None)
        # 91         580 LOAD_CONST               9 (False)
        # 92         582 LOAD_CONST               3 (0)
        # 93         584 LOAD_FAST                8 (child_env)
        # 94         586 LOAD_CONST               0 (None)
        # 95         588 LOAD_CONST               0 (None)
        # 86         590 PRECALL                  9
        # 594 CALL                     9
        # 604 UNPACK_SEQUENCE          4
        # 608 STORE_FAST              10 (hp)
        # 610 STORE_FAST              11 (ht)
        # 612 STORE_FAST              12 (pid)
        # 614 STORE_FAST              13 (_)
        # 97         616 LOAD_GLOBAL              9 (NULL + _winapi)
        # 628 LOAD_ATTR               22 (CloseHandle)
        # 638 LOAD_FAST               11 (ht)
        # 640 PRECALL                  1
        # 644 CALL                     1
        # 654 POP_TOP
        # 656 JUMP_FORWARD            35 (to 728)
        # >>  658 PUSH_EXC_INFO
        # 98         660 LOAD_GLOBAL             46 (BaseException)
        # 672 CHECK_EXC_MATCH
        # 674 POP_JUMP_FORWARD_IF_FALSE    22 (to 720)
        # 676 POP_TOP
        # 99         678 LOAD_GLOBAL              9 (NULL + _winapi)
        # 690 LOAD_ATTR               22 (CloseHandle)
        # 700 LOAD_FAST                3 (rhandle)
        # 702 PRECALL                  1
        # 706 CALL                     1
        # 716 POP_TOP
        # 100         718 RAISE_VARARGS            0
        # 98     >>  720 RERAISE                  0
        # >>  722 COPY                     3
        # 724 POP_EXCEPT
        # 726 RERAISE                  1
        # 103     >>  728 LOAD_FAST               12 (pid)
        # 730 LOAD_FAST                0 (self)
        # 732 STORE_ATTR              24 (pid)
        # 104         742 LOAD_CONST               0 (None)
        # 744 LOAD_FAST                0 (self)
        # 746 STORE_ATTR              25 (returncode)
        # 105         756 LOAD_FAST               10 (hp)
        # 758 LOAD_FAST                0 (self)
        # 760 STORE_ATTR              26 (_handle)
        # 106         770 LOAD_GLOBAL             55 (NULL + int)
        # 782 LOAD_FAST               10 (hp)
        # 784 PRECALL                  1
        # 788 CALL                     1
        # 798 LOAD_FAST                0 (self)
        # 800 STORE_ATTR              28 (sentinel)
        # 107         810 LOAD_GLOBAL             59 (NULL + util)
        # 822 LOAD_ATTR               30 (Finalize)
        # 108         832 LOAD_FAST                0 (self)
        # 834 LOAD_GLOBAL             62 (_close_handles)
        # 846 LOAD_FAST                0 (self)
        # 848 LOAD_ATTR               28 (sentinel)
        # 858 LOAD_GLOBAL             55 (NULL + int)
        # 870 LOAD_FAST                3 (rhandle)
        # 872 PRECALL                  1
        # 876 CALL                     1
        # 886 BUILD_TUPLE              2
        # 107         888 PRECALL                  3
        # 892 CALL                     3
        # 902 LOAD_FAST                0 (self)
        # 904 STORE_ATTR              32 (finalizer)
        # 112         914 LOAD_GLOBAL             67 (NULL + set_spawning_popen)
        # 926 LOAD_FAST                0 (self)
        # 928 PRECALL                  1
        # 932 CALL                     1
        # 942 POP_TOP
        # 113         944 NOP
        # 114         946 LOAD_GLOBAL             69 (NULL + reduction)
        # 958 LOAD_ATTR               35 (dump)
        # 968 LOAD_FAST                2 (prep_data)
        # 970 LOAD_FAST                9 (to_child)
        # 972 PRECALL                  2
        # 976 CALL                     2
        # 986 POP_TOP
        # 115         988 LOAD_GLOBAL             69 (NULL + reduction)
        # 1000 LOAD_ATTR               35 (dump)
        # 1010 LOAD_FAST                1 (process_obj)
        # 1012 LOAD_FAST                9 (to_child)
        # 1014 PRECALL                  2
        # 1018 CALL                     2
        # 1028 POP_TOP
        # 117        1030 LOAD_GLOBAL             67 (NULL + set_spawning_popen)
        # 1042 LOAD_CONST               0 (None)
        # 1044 PRECALL                  1
        # 1048 CALL                     1
        # 1058 POP_TOP
        # 1060 JUMP_FORWARD            20 (to 1102)
        # >> 1062 PUSH_EXC_INFO
        # 1064 LOAD_GLOBAL             67 (NULL + set_spawning_popen)
        # 1076 LOAD_CONST               0 (None)
        # 1078 PRECALL                  1
        # 1082 CALL                     1
        # 1092 POP_TOP
        # 1094 RERAISE                  0
        # >> 1096 COPY                     3
        # 1098 POP_EXCEPT
        # 1100 RERAISE                  1
        # >> 1102 NOP
        # 83        1104 LOAD_CONST               0 (None)
        # 1106 LOAD_CONST               0 (None)
        # 1108 LOAD_CONST               0 (None)
        # 1110 PRECALL                  2
        # 1114 CALL                     2
        # 1124 POP_TOP
        # 1126 LOAD_CONST               0 (None)
        # 1128 RETURN_VALUE
        # >> 1130 PUSH_EXC_INFO
        # 1132 WITH_EXCEPT_START
        # 1134 POP_JUMP_FORWARD_IF_TRUE     4 (to 1144)
        # 1136 RERAISE                  2
        # >> 1138 COPY                     3
        # 1140 POP_EXCEPT
        # 1142 RERAISE                  1
        # >> 1144 POP_TOP
        # 1146 POP_EXCEPT
        # 1148 POP_TOP
        # 1150 POP_TOP
        # 1152 LOAD_CONST               0 (None)
        # 1154 RETURN_VALUE
        # ExceptionTable:
        # 546 to 546 -> 1130 [1] lasti
        # 550 to 654 -> 658 [1]
        # 656 to 656 -> 1130 [1] lasti
        # 658 to 720 -> 722 [2] lasti
        # 722 to 942 -> 1130 [1] lasti
        # 946 to 1028 -> 1062 [1]
        # 1030 to 1060 -> 1130 [1] lasti
        # 1062 to 1094 -> 1096 [2] lasti
        # 1096 to 1100 -> 1130 [1] lasti
        # 1130 to 1136 -> 1138 [3] lasti
        # 1144 to 1144 -> 1138 [3] lasti
        # Disassembly of <code object <genexpr> at 0x000001EBD7E350D0, file "joblib\externals\loky\backend\popen_loky_win32.py", line 81>:
        # 81           0 RETURN_GENERATOR
        # 2 POP_TOP
        # 4 RESUME                   0
        # 6 LOAD_FAST                0 (.0)
        # >>    8 FOR_ITER                10 (to 30)
        # 10 STORE_FAST               1 (x)
        # 12 LOAD_CONST               0 ('"')
        # 14 LOAD_FAST                1 (x)
        # 16 FORMAT_VALUE             0
        # 18 LOAD_CONST               0 ('"')
        # 20 BUILD_STRING             3
        # 22 YIELD_VALUE
        # 24 RESUME                   1
        # 26 POP_TOP
        # 28 JUMP_BACKWARD           11 (to 8)
        # >>   30 LOAD_CONST               1 (None)
        # 32 RETURN_VALUE


def get_command_line(pipe_handle, parent_pid):
    """Returns prefix of command line used for spawning a child process."""
    # 120           0 RESUME                   0
    # 122           2 LOAD_GLOBAL              1 (NULL + getattr)
    # 14 LOAD_GLOBAL              2 (sys)
    # 26 LOAD_CONST               1 ('frozen')
    # 28 LOAD_CONST               2 (False)
    # 30 PRECALL                  3
    # 34 CALL                     3
    # 44 POP_JUMP_FORWARD_IF_FALSE    15 (to 76)
    # 123          46 LOAD_GLOBAL              2 (sys)
    # 58 LOAD_ATTR                2 (executable)
    # 68 LOAD_CONST               3 ('--multiprocessing-fork')
    # 70 LOAD_FAST                0 (pipe_handle)
    # 72 BUILD_LIST               3
    # 74 RETURN_VALUE
    # 126     >>   76 LOAD_CONST               4 ('from joblib.externals.loky.backend.popen_loky_win32 import main; main(pipe_handle=')
    # 127          78 LOAD_FAST                0 (pipe_handle)
    # 126          80 FORMAT_VALUE             0
    # 82 LOAD_CONST               5 (', parent_pid=')
    # 127          84 LOAD_FAST                1 (parent_pid)
    # 126          86 FORMAT_VALUE             0
    # 88 LOAD_CONST               6 (')')
    # 90 BUILD_STRING             5
    # 125          92 STORE_FAST               3 (prog)
    # 129          94 LOAD_GLOBAL              7 (NULL + util)
    # 106 LOAD_ATTR                4 (_args_from_interpreter_flags)
    # 116 PRECALL                  0
    # 120 CALL                     0
    # 130 STORE_FAST               4 (opts)
    # 131         132 LOAD_GLOBAL             11 (NULL + spawn)
    # 144 LOAD_ATTR                6 (get_executable)
    # 154 PRECALL                  0
    # 158 CALL                     0
    # 130         168 BUILD_LIST               1
    # 132         170 LOAD_FAST                4 (opts)
    # 130         172 LIST_EXTEND              1
    # 133         174 LOAD_CONST               7 ('-c')
    # 130         176 LIST_APPEND              1
    # 134         178 LOAD_FAST                3 (prog)
    # 130         180 LIST_APPEND              1
    # 135         182 LOAD_CONST               3 ('--multiprocessing-fork')
    # 130         184 LIST_APPEND              1
    # 186 RETURN_VALUE

def is_forking(argv):
    """Return whether commandline indicates we are forking."""
    # 139           0 RESUME                   0
    # 141           2 LOAD_GLOBAL              1 (NULL + len)
    # 14 LOAD_FAST                0 (argv)
    # 16 PRECALL                  1
    # 20 CALL                     1
    # 30 LOAD_CONST               1 (2)
    # 32 COMPARE_OP               5 (>=)
    # 38 POP_JUMP_FORWARD_IF_FALSE    14 (to 68)
    # 40 LOAD_FAST                0 (argv)
    # 42 LOAD_CONST               2 (1)
    # 44 BINARY_SUBSCR
    # 54 LOAD_CONST               3 ('--multiprocessing-fork')
    # 56 COMPARE_OP               2 (==)
    # 62 POP_JUMP_FORWARD_IF_FALSE     2 (to 68)
    # 142          64 LOAD_CONST               4 (True)
    # 66 RETURN_VALUE
    # 144     >>   68 LOAD_CONST               5 (False)
    # 70 RETURN_VALUE

def main(pipe_handle, parent_pid):
    """Run code specified by data received over pipe."""
    # 147           0 RESUME                   0
    # 149           2 LOAD_GLOBAL              1 (NULL + is_forking)
    # 14 LOAD_GLOBAL              2 (sys)
    # 26 LOAD_ATTR                2 (argv)
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 POP_JUMP_FORWARD_IF_TRUE    10 (to 72)
    # 52 LOAD_ASSERTION_ERROR
    # 54 LOAD_CONST               1 ('Not forking')
    # 56 PRECALL                  0
    # 60 CALL                     0
    # 70 RAISE_VARARGS            1
    # 151     >>   72 LOAD_FAST                1 (parent_pid)
    # 74 POP_JUMP_FORWARD_IF_NONE    46 (to 168)
    # 152          76 LOAD_GLOBAL              7 (NULL + _winapi)
    # 88 LOAD_ATTR                4 (OpenProcess)
    # 153          98 LOAD_GLOBAL              6 (_winapi)
    # 110 LOAD_ATTR                5 (SYNCHRONIZE)
    # 120 LOAD_GLOBAL              6 (_winapi)
    # 132 LOAD_ATTR                6 (PROCESS_DUP_HANDLE)
    # 142 BINARY_OP                7 (|)
    # 146 LOAD_CONST               3 (False)
    # 148 LOAD_FAST                1 (parent_pid)
    # 152         150 PRECALL                  3
    # 154 CALL                     3
    # 164 STORE_FAST               2 (source_process)
    # 166 JUMP_FORWARD             2 (to 172)
    # 156     >>  168 LOAD_CONST               2 (None)
    # 170 STORE_FAST               2 (source_process)
    # 157     >>  172 LOAD_GLOBAL             15 (NULL + reduction)
    # 184 LOAD_ATTR                8 (duplicate)
    # 158         194 LOAD_FAST                0 (pipe_handle)
    # 196 LOAD_FAST                2 (source_process)
    # 157         198 KW_NAMES                 4
    # 200 PRECALL                  2
    # 204 CALL                     2
    # 214 STORE_FAST               3 (new_handle)
    # 160         216 LOAD_GLOBAL             19 (NULL + msvcrt)
    # 228 LOAD_ATTR               10 (open_osfhandle)
    # 238 LOAD_FAST                3 (new_handle)
    # 240 LOAD_GLOBAL             22 (os)
    # 252 LOAD_ATTR               12 (O_RDONLY)
    # 262 PRECALL                  2
    # 266 CALL                     2
    # 276 STORE_FAST               4 (fd)
    # 161         278 LOAD_FAST                2 (source_process)
    # 280 STORE_FAST               5 (parent_sentinel)
    # 163         282 LOAD_GLOBAL             23 (NULL + os)
    # 294 LOAD_ATTR               13 (fdopen)
    # 304 LOAD_FAST                4 (fd)
    # 306 LOAD_CONST               5 ('rb')
    # 308 LOAD_CONST               6 (True)
    # 310 KW_NAMES                 7
    # 312 PRECALL                  3
    # 316 CALL                     3
    # 326 BEFORE_WITH
    # 328 STORE_FAST               6 (from_parent)
    # 164         330 LOAD_CONST               6 (True)
    # 332 LOAD_GLOBAL             29 (NULL + process)
    # 344 LOAD_ATTR               15 (current_process)
    # 354 PRECALL                  0
    # 358 CALL                     0
    # 368 STORE_ATTR              16 (_inheriting)
    # 165         378 NOP
    # 166         380 LOAD_GLOBAL             35 (NULL + load)
    # 392 LOAD_FAST                6 (from_parent)
    # 394 PRECALL                  1
    # 398 CALL                     1
    # 408 STORE_FAST               7 (preparation_data)
    # 167         410 LOAD_GLOBAL             37 (NULL + spawn)
    # 422 LOAD_ATTR               19 (prepare)
    # 432 LOAD_FAST                7 (preparation_data)
    # 434 LOAD_FAST                5 (parent_sentinel)
    # 436 PRECALL                  2
    # 440 CALL                     2
    # 450 POP_TOP
    # 168         452 LOAD_GLOBAL             35 (NULL + load)
    # 464 LOAD_FAST                6 (from_parent)
    # 466 PRECALL                  1
    # 470 CALL                     1
    # 480 STORE_FAST               8 (self)
    # 170         482 LOAD_GLOBAL             29 (NULL + process)
    # 494 LOAD_ATTR               15 (current_process)
    # 504 PRECALL                  0
    # 508 CALL                     0
    # 518 DELETE_ATTR             16 (_inheriting)
    # 520 JUMP_FORWARD            24 (to 570)
    # >>  522 PUSH_EXC_INFO
    # 524 LOAD_GLOBAL             29 (NULL + process)
    # 536 LOAD_ATTR               15 (current_process)
    # 546 PRECALL                  0
    # 550 CALL                     0
    # 560 DELETE_ATTR             16 (_inheriting)
    # 562 RERAISE                  0
    # >>  564 COPY                     3
    # 566 POP_EXCEPT
    # 568 RERAISE                  1
    # >>  570 NOP
    # 163         572 LOAD_CONST               2 (None)
    # 574 LOAD_CONST               2 (None)
    # 576 LOAD_CONST               2 (None)
    # 578 PRECALL                  2
    # 582 CALL                     2
    # 592 POP_TOP
    # 594 JUMP_FORWARD            11 (to 618)
    # >>  596 PUSH_EXC_INFO
    # 598 WITH_EXCEPT_START
    # 600 POP_JUMP_FORWARD_IF_TRUE     4 (to 610)
    # 602 RERAISE                  2
    # >>  604 COPY                     3
    # 606 POP_EXCEPT
    # 608 RERAISE                  1
    # >>  610 POP_TOP
    # 612 POP_EXCEPT
    # 614 POP_TOP
    # 616 POP_TOP
    # 172     >>  618 LOAD_FAST                8 (self)
    # 620 LOAD_METHOD             20 (_bootstrap)
    # 642 LOAD_FAST                5 (parent_sentinel)
    # 644 PRECALL                  1
    # 648 CALL                     1
    # 658 STORE_FAST               9 (exitcode)
    # 173         660 LOAD_GLOBAL              3 (NULL + sys)
    # 672 LOAD_ATTR               21 (exit)
    # 682 LOAD_FAST                9 (exitcode)
    # 684 PRECALL                  1
    # 688 CALL                     1
    # 698 POP_TOP
    # 700 LOAD_CONST               2 (None)
    # 702 RETURN_VALUE
    # ExceptionTable:
    # 328 to 376 -> 596 [1] lasti
    # 380 to 480 -> 522 [1]
    # 482 to 520 -> 596 [1] lasti
    # 522 to 562 -> 564 [2] lasti
    # 564 to 568 -> 596 [1] lasti
    # 596 to 602 -> 604 [3] lasti
    # 610 to 610 -> 604 [3] lasti
