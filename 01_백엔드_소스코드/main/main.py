# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: main.py

"""
TFstudio - Standalone Application Entry Point
Uses pywebview to create a native window with embedded Flask server
"""

import os
import sys
import threading
import time
import socket
import logging
import atexit
import signal
import subprocess
from pathlib import Path
import traceback

def _ensure_stdio():
    """Redirect stdout/stderr to devnull if they are None (--noconsole mode)."""
    # 20           0 RESUME                   0
    # 22           2 LOAD_GLOBAL              0 (sys)
    # 14 LOAD_ATTR                1 (stdout)
    # 24 POP_JUMP_FORWARD_IF_NOT_NONE    38 (to 102)
    # 23          26 LOAD_GLOBAL              5 (NULL + open)
    # 38 LOAD_GLOBAL              6 (os)
    # 50 LOAD_ATTR                4 (devnull)
    # 60 LOAD_CONST               2 ('w')
    # 62 LOAD_CONST               3 ('utf-8')
    # 64 KW_NAMES                 4
    # 66 PRECALL                  3
    # 70 CALL                     3
    # 80 LOAD_GLOBAL              0 (sys)
    # 92 STORE_ATTR               1 (stdout)
    # 24     >>  102 LOAD_GLOBAL              0 (sys)
    # 114 LOAD_ATTR                5 (stderr)
    # 124 POP_JUMP_FORWARD_IF_NOT_NONE    40 (to 206)
    # 25         126 LOAD_GLOBAL              5 (NULL + open)
    # 138 LOAD_GLOBAL              6 (os)
    # 150 LOAD_ATTR                4 (devnull)
    # 160 LOAD_CONST               2 ('w')
    # 162 LOAD_CONST               3 ('utf-8')
    # 164 KW_NAMES                 4
    # 166 PRECALL                  3
    # 170 CALL                     3
    # 180 LOAD_GLOBAL              0 (sys)
    # 192 STORE_ATTR               5 (stderr)
    # 202 LOAD_CONST               1 (None)
    # 204 RETURN_VALUE
    # 24     >>  206 LOAD_CONST               1 (None)
    # 208 RETURN_VALUE

def _show_fatal_error(title, message):
    """Show a fatal error dialog using Windows MessageBox (no dependencies required)."""
    # 30           0 RESUME                   0
    # 32           2 NOP
    # 33           4 LOAD_GLOBAL              0 (os)
    # 16 LOAD_ATTR                1 (name)
    # 26 LOAD_CONST               1 ('nt')
    # 28 COMPARE_OP               2 (==)
    # 34 POP_JUMP_FORWARD_IF_FALSE    47 (to 130)
    # 34          36 LOAD_CONST               2 (0)
    # 38 LOAD_CONST               3 (None)
    # 40 IMPORT_NAME              2 (ctypes)
    # 42 STORE_FAST               2 (ctypes)
    # 35          44 LOAD_CONST               2 (0)
    # 46 STORE_FAST               3 (MB_OK)
    # 36          48 LOAD_CONST               4 (16)
    # 50 STORE_FAST               4 (MB_ICONERROR)
    # 37          52 LOAD_FAST                2 (ctypes)
    # 54 LOAD_ATTR                3 (windll)
    # 64 LOAD_ATTR                4 (user32)
    # 74 LOAD_METHOD              5 (MessageBoxW)
    # 96 LOAD_CONST               2 (0)
    # 98 LOAD_FAST                1 (message)
    # 100 LOAD_FAST                0 (title)
    # 102 LOAD_FAST                3 (MB_OK)
    # 104 LOAD_FAST                4 (MB_ICONERROR)
    # 106 BINARY_OP                7 (|)
    # 110 PRECALL                  4
    # 114 CALL                     4
    # 124 POP_TOP
    # 126 LOAD_CONST               3 (None)
    # 128 RETURN_VALUE
    # 39     >>  130 LOAD_GLOBAL             13 (NULL + print)
    # 142 LOAD_CONST               5 ('FATAL: ')
    # 144 LOAD_FAST                0 (title)
    # 146 FORMAT_VALUE             0
    # 148 LOAD_CONST               6 ('\n')
    # 150 LOAD_FAST                1 (message)
    # 152 FORMAT_VALUE             0
    # 154 BUILD_STRING             4
    # 156 LOAD_GLOBAL             14 (sys)
    # 168 LOAD_ATTR                8 (stderr)
    # 178 KW_NAMES                 7
    # 180 PRECALL                  2
    # 184 CALL                     2
    # 194 POP_TOP
    # 196 LOAD_CONST               3 (None)
    # 198 RETURN_VALUE
    # >>  200 PUSH_EXC_INFO
    # 40         202 LOAD_GLOBAL             18 (Exception)
    # 214 CHECK_EXC_MATCH
    # 216 POP_JUMP_FORWARD_IF_FALSE     4 (to 226)
    # 218 POP_TOP
    # 41         220 POP_EXCEPT
    # 222 LOAD_CONST               3 (None)
    # 224 RETURN_VALUE
    # 40     >>  226 RERAISE                  0
    # >>  228 COPY                     3
    # 230 POP_EXCEPT
    # 232 RERAISE                  1
    # ExceptionTable:
    # 4 to 124 -> 200 [0]
    # 130 to 194 -> 200 [0]
    # 200 to 218 -> 228 [1] lasti
    # 226 to 226 -> 228 [1] lasti

def _show_info_message(title, message):
    """Show an informational dialog using Windows MessageBox."""
    # 44           0 RESUME                   0
    # 46           2 NOP
    # 47           4 LOAD_GLOBAL              0 (os)
    # 16 LOAD_ATTR                1 (name)
    # 26 LOAD_CONST               1 ('nt')
    # 28 COMPARE_OP               2 (==)
    # 34 POP_JUMP_FORWARD_IF_FALSE    47 (to 130)
    # 48          36 LOAD_CONST               2 (0)
    # 38 LOAD_CONST               3 (None)
    # 40 IMPORT_NAME              2 (ctypes)
    # 42 STORE_FAST               2 (ctypes)
    # 49          44 LOAD_CONST               2 (0)
    # 46 STORE_FAST               3 (MB_OK)
    # 50          48 LOAD_CONST               4 (64)
    # 50 STORE_FAST               4 (MB_ICONINFORMATION)
    # 51          52 LOAD_FAST                2 (ctypes)
    # 54 LOAD_ATTR                3 (windll)
    # 64 LOAD_ATTR                4 (user32)
    # 74 LOAD_METHOD              5 (MessageBoxW)
    # 96 LOAD_CONST               2 (0)
    # 98 LOAD_FAST                1 (message)
    # 100 LOAD_FAST                0 (title)
    # 102 LOAD_FAST                3 (MB_OK)
    # 104 LOAD_FAST                4 (MB_ICONINFORMATION)
    # 106 BINARY_OP                7 (|)
    # 110 PRECALL                  4
    # 114 CALL                     4
    # 124 POP_TOP
    # 126 LOAD_CONST               3 (None)
    # 128 RETURN_VALUE
    # 53     >>  130 LOAD_GLOBAL             13 (NULL + print)
    # 142 LOAD_CONST               5 ('INFO: ')
    # 144 LOAD_FAST                0 (title)
    # 146 FORMAT_VALUE             0
    # 148 LOAD_CONST               6 ('\n')
    # 150 LOAD_FAST                1 (message)
    # 152 FORMAT_VALUE             0
    # 154 BUILD_STRING             4
    # 156 LOAD_GLOBAL             14 (sys)
    # 168 LOAD_ATTR                8 (stderr)
    # 178 KW_NAMES                 7
    # 180 PRECALL                  2
    # 184 CALL                     2
    # 194 POP_TOP
    # 196 LOAD_CONST               3 (None)
    # 198 RETURN_VALUE
    # >>  200 PUSH_EXC_INFO
    # 54         202 LOAD_GLOBAL             18 (Exception)
    # 214 CHECK_EXC_MATCH
    # 216 POP_JUMP_FORWARD_IF_FALSE     4 (to 226)
    # 218 POP_TOP
    # 55         220 POP_EXCEPT
    # 222 LOAD_CONST               3 (None)
    # 224 RETURN_VALUE
    # 54     >>  226 RERAISE                  0
    # >>  228 COPY                     3
    # 230 POP_EXCEPT
    # 232 RERAISE                  1
    # ExceptionTable:
    # 4 to 124 -> 200 [0]
    # 130 to 194 -> 200 [0]
    # 200 to 218 -> 228 [1] lasti
    # 226 to 226 -> 228 [1] lasti

def _write_bootstrap_log(message):
    """Write best-effort startup diagnostics before full logger is ready."""
    # 58           0 RESUME                   0
    # 60           2 NOP
    # 61           4 LOAD_GLOBAL              0 (os)
    # 16 LOAD_ATTR                1 (name)
    # 26 LOAD_CONST               1 ('nt')
    # 28 COMPARE_OP               2 (==)
    # 34 POP_JUMP_FORWARD_IF_FALSE    84 (to 204)
    # 62          36 LOAD_GLOBAL              1 (NULL + os)
    # 48 LOAD_ATTR                2 (getenv)
    # 58 LOAD_CONST               2 ('LOCALAPPDATA')
    # 60 LOAD_GLOBAL              0 (os)
    # 72 LOAD_ATTR                3 (path)
    # 82 LOAD_METHOD              4 (expanduser)
    # 104 LOAD_CONST               3 ('~')
    # 106 PRECALL                  1
    # 110 CALL                     1
    # 120 PRECALL                  2
    # 124 CALL                     2
    # 134 STORE_FAST               1 (base_dir)
    # 63         136 LOAD_GLOBAL              0 (os)
    # 148 LOAD_ATTR                3 (path)
    # 158 LOAD_METHOD              5 (join)
    # 180 LOAD_FAST                1 (base_dir)
    # 182 LOAD_CONST               4 ('TFstudio')
    # 184 LOAD_CONST               5 ('logs')
    # 186 PRECALL                  3
    # 190 CALL                     3
    # 200 STORE_FAST               2 (log_dir)
    # 202 JUMP_FORWARD            62 (to 328)
    # 65     >>  204 LOAD_GLOBAL              0 (os)
    # 216 LOAD_ATTR                3 (path)
    # 226 LOAD_METHOD              5 (join)
    # 248 LOAD_GLOBAL              0 (os)
    # 260 LOAD_ATTR                3 (path)
    # 270 LOAD_METHOD              4 (expanduser)
    # 292 LOAD_CONST               3 ('~')
    # 294 PRECALL                  1
    # 298 CALL                     1
    # 308 LOAD_CONST               6 ('.tfstudio')
    # 310 LOAD_CONST               5 ('logs')
    # 312 PRECALL                  3
    # 316 CALL                     3
    # 326 STORE_FAST               2 (log_dir)
    # 67     >>  328 LOAD_GLOBAL              1 (NULL + os)
    # 340 LOAD_ATTR                6 (makedirs)
    # 350 LOAD_FAST                2 (log_dir)
    # 352 LOAD_CONST               7 (True)
    # 354 KW_NAMES                 8
    # 356 PRECALL                  2
    # 360 CALL                     2
    # 370 POP_TOP
    # 68         372 LOAD_GLOBAL              0 (os)
    # 384 LOAD_ATTR                3 (path)
    # 394 LOAD_METHOD              5 (join)
    # 416 LOAD_FAST                2 (log_dir)
    # 418 LOAD_CONST               9 ('bootstrap_startup.log')
    # 420 PRECALL                  2
    # 424 CALL                     2
    # 434 STORE_FAST               3 (bootstrap_log)
    # 69         436 LOAD_GLOBAL             15 (NULL + time)
    # 448 LOAD_ATTR                8 (strftime)
    # 458 LOAD_CONST              10 ('%Y-%m-%d %H:%M:%S')
    # 460 PRECALL                  1
    # 464 CALL                     1
    # 474 STORE_FAST               4 (timestamp)
    # 71         476 LOAD_GLOBAL             19 (NULL + open)
    # 488 LOAD_FAST                3 (bootstrap_log)
    # 490 LOAD_CONST              11 ('a')
    # 492 LOAD_CONST              12 ('utf-8')
    # 494 KW_NAMES                13
    # 496 PRECALL                  3
    # 500 CALL                     3
    # 510 BEFORE_WITH
    # 512 STORE_FAST               5 (f)
    # 72         514 LOAD_FAST                5 (f)
    # 516 LOAD_METHOD             10 (write)
    # 538 LOAD_FAST                4 (timestamp)
    # 540 FORMAT_VALUE             0
    # 542 LOAD_CONST              14 (' | ')
    # 544 LOAD_FAST                0 (message)
    # 546 FORMAT_VALUE             0
    # 548 LOAD_CONST              15 ('\n')
    # 550 BUILD_STRING             4
    # 552 PRECALL                  1
    # 556 CALL                     1
    # 566 POP_TOP
    # 71         568 LOAD_CONST              16 (None)
    # 570 LOAD_CONST              16 (None)
    # 572 LOAD_CONST              16 (None)
    # 574 PRECALL                  2
    # 578 CALL                     2
    # 588 POP_TOP
    # 590 LOAD_CONST              16 (None)
    # 592 RETURN_VALUE
    # >>  594 PUSH_EXC_INFO
    # 596 WITH_EXCEPT_START
    # 598 POP_JUMP_FORWARD_IF_TRUE     4 (to 608)
    # 600 RERAISE                  2
    # >>  602 COPY                     3
    # 604 POP_EXCEPT
    # 606 RERAISE                  1
    # >>  608 POP_TOP
    # 610 POP_EXCEPT
    # 612 POP_TOP
    # 614 POP_TOP
    # 616 LOAD_CONST              16 (None)
    # 618 RETURN_VALUE
    # >>  620 PUSH_EXC_INFO
    # 73         622 LOAD_GLOBAL             22 (Exception)
    # 634 CHECK_EXC_MATCH
    # 636 POP_JUMP_FORWARD_IF_FALSE     4 (to 646)
    # 638 POP_TOP
    # 74         640 POP_EXCEPT
    # 642 LOAD_CONST              16 (None)
    # 644 RETURN_VALUE
    # 73     >>  646 RERAISE                  0
    # >>  648 COPY                     3
    # 650 POP_EXCEPT
    # 652 RERAISE                  1
    # ExceptionTable:
    # 4 to 510 -> 620 [0]
    # 512 to 566 -> 594 [1] lasti
    # 568 to 588 -> 620 [0]
    # 594 to 600 -> 602 [3] lasti
    # 602 to 606 -> 620 [0]
    # 608 to 608 -> 602 [3] lasti
    # 610 to 614 -> 620 [0]
    # 620 to 638 -> 648 [1] lasti
    # 646 to 646 -> 648 [1] lasti

def setup_logging():
    """Setup logging to both console and file"""
    # 0 MAKE_CELL               14 (datetime)
    # 2 MAKE_CELL               15 (timedelta)
    # 81           4 RESUME                   0
    # 83           6 LOAD_CONST               1 (0)
    # 8 LOAD_CONST               2 (('RotatingFileHandler',))
    # 10 IMPORT_NAME              0 (logging.handlers)
    # 12 IMPORT_FROM              1 (RotatingFileHandler)
    # 14 STORE_FAST               0 (RotatingFileHandler)
    # 16 POP_TOP
    # 84          18 LOAD_CONST               1 (0)
    # 20 LOAD_CONST               3 (('datetime', 'timedelta'))
    # 22 IMPORT_NAME              2 (datetime)
    # 24 IMPORT_FROM              2 (datetime)
    # 26 STORE_DEREF             14 (datetime)
    # 28 IMPORT_FROM              3 (timedelta)
    # 30 STORE_DEREF             15 (timedelta)
    # 32 POP_TOP
    # 86          34 LOAD_CONST              43 ((3,))
    # 36 LOAD_CONST               5 ('log_directory')
    # 38 LOAD_GLOBAL              8 (str)
    # 50 LOAD_CONST               6 ('retention_days')
    # 52 LOAD_GLOBAL             10 (int)
    # 64 BUILD_TUPLE              4
    # 66 LOAD_CLOSURE            14 (datetime)
    # 68 LOAD_CLOSURE            15 (timedelta)
    # 70 BUILD_TUPLE              2
    # 72 LOAD_CONST               7 (<code object cleanup_old_tfstudio_logs at 0x000001EBD6FB8640, file "main.py", line 86>)
    # 74 MAKE_FUNCTION           13 (defaults, annotations, closure)
    # 76 STORE_FAST               1 (cleanup_old_tfstudio_logs)
    # 133          78 NOP
    # 135          80 LOAD_GLOBAL             12 (os)
    # 92 LOAD_ATTR                7 (name)
    # 102 LOAD_CONST               8 ('nt')
    # 104 COMPARE_OP               2 (==)
    # 110 POP_JUMP_FORWARD_IF_FALSE    84 (to 280)
    # 136         112 LOAD_GLOBAL             13 (NULL + os)
    # 124 LOAD_ATTR                8 (getenv)
    # 134 LOAD_CONST               9 ('LOCALAPPDATA')
    # 136 LOAD_GLOBAL             12 (os)
    # 148 LOAD_ATTR                9 (path)
    # 158 LOAD_METHOD             10 (expanduser)
    # 180 LOAD_CONST              10 ('~')
    # 182 PRECALL                  1
    # 186 CALL                     1
    # 196 PRECALL                  2
    # 200 CALL                     2
    # 210 STORE_FAST               2 (localappdata)
    # 137         212 LOAD_GLOBAL             12 (os)
    # 224 LOAD_ATTR                9 (path)
    # 234 LOAD_METHOD             11 (join)
    # 256 LOAD_FAST                2 (localappdata)
    # 258 LOAD_CONST              11 ('TFstudio')
    # 260 LOAD_CONST              12 ('logs')
    # 262 PRECALL                  3
    # 266 CALL                     3
    # 276 STORE_FAST               3 (log_dir)
    # 278 JUMP_FORWARD            62 (to 404)
    # 139     >>  280 LOAD_GLOBAL             12 (os)
    # 292 LOAD_ATTR                9 (path)
    # 302 LOAD_METHOD             11 (join)
    # 324 LOAD_GLOBAL             12 (os)
    # 336 LOAD_ATTR                9 (path)
    # 346 LOAD_METHOD             10 (expanduser)
    # 368 LOAD_CONST              10 ('~')
    # 370 PRECALL                  1
    # 374 CALL                     1
    # 384 LOAD_CONST              13 ('.tfstudio')
    # 386 LOAD_CONST              12 ('logs')
    # 388 PRECALL                  3
    # 392 CALL                     3
    # 402 STORE_FAST               3 (log_dir)
    # 141     >>  404 LOAD_GLOBAL             13 (NULL + os)
    # 416 LOAD_ATTR               12 (makedirs)
    # 426 LOAD_FAST                3 (log_dir)
    # 428 LOAD_CONST              14 (True)
    # 430 KW_NAMES                15
    # 432 PRECALL                  2
    # 436 CALL                     2
    # 446 POP_TOP
    # 143         448 PUSH_NULL
    # 450 LOAD_FAST                1 (cleanup_old_tfstudio_logs)
    # 452 LOAD_FAST                3 (log_dir)
    # 454 LOAD_CONST               4 (3)
    # 456 KW_NAMES                16
    # 458 PRECALL                  2
    # 462 CALL                     2
    # 472 STORE_FAST               4 (cleanup_result)
    # 146         474 LOAD_CONST              17 ('tfstudio_')
    # 476 LOAD_DEREF              14 (datetime)
    # 478 LOAD_METHOD             13 (now)
    # 500 PRECALL                  0
    # 504 CALL                     0
    # 514 LOAD_METHOD             14 (strftime)
    # 536 LOAD_CONST              18 ('%Y%m%d')
    # 538 PRECALL                  1
    # 542 CALL                     1
    # 552 FORMAT_VALUE             0
    # 554 LOAD_CONST              19 ('.log')
    # 556 BUILD_STRING             3
    # 558 STORE_FAST               5 (log_filename)
    # 147         560 LOAD_GLOBAL             12 (os)
    # 572 LOAD_ATTR                9 (path)
    # 582 LOAD_METHOD             11 (join)
    # 604 LOAD_FAST                3 (log_dir)
    # 606 LOAD_FAST                5 (log_filename)
    # 608 PRECALL                  2
    # 612 CALL                     2
    # 622 STORE_FAST               6 (log_path)
    # 150         624 LOAD_GLOBAL             31 (NULL + logging)
    # 636 LOAD_ATTR               16 (Formatter)
    # 151         646 LOAD_CONST              20 ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 150         648 PRECALL                  1
    # 652 CALL                     1
    # 662 STORE_FAST               7 (formatter)
    # 155         664 LOAD_GLOBAL             31 (NULL + logging)
    # 676 LOAD_ATTR               17 (getLogger)
    # 686 PRECALL                  0
    # 690 CALL                     0
    # 700 STORE_FAST               8 (root_logger)
    # 156         702 LOAD_FAST                8 (root_logger)
    # 704 LOAD_METHOD             18 (setLevel)
    # 726 LOAD_GLOBAL             30 (logging)
    # 738 LOAD_ATTR               19 (INFO)
    # 748 PRECALL                  1
    # 752 CALL                     1
    # 762 POP_TOP
    # 159         764 LOAD_FAST                8 (root_logger)
    # 766 LOAD_ATTR               20 (handlers)
    # 776 LOAD_METHOD             21 (clear)
    # 798 PRECALL                  0
    # 802 CALL                     0
    # 812 POP_TOP
    # 162         814 LOAD_GLOBAL             31 (NULL + logging)
    # 826 LOAD_ATTR               22 (StreamHandler)
    # 836 PRECALL                  0
    # 840 CALL                     0
    # 850 STORE_FAST               9 (console_handler)
    # 163         852 LOAD_FAST                9 (console_handler)
    # 854 LOAD_METHOD             23 (setFormatter)
    # 876 LOAD_FAST                7 (formatter)
    # 878 PRECALL                  1
    # 882 CALL                     1
    # 892 POP_TOP
    # 164         894 LOAD_FAST                8 (root_logger)
    # 896 LOAD_METHOD             24 (addHandler)
    # 918 LOAD_FAST                9 (console_handler)
    # 920 PRECALL                  1
    # 924 CALL                     1
    # 934 POP_TOP
    # 168         936 NOP
    # 169         938 PUSH_NULL
    # 940 LOAD_FAST                0 (RotatingFileHandler)
    # 170         942 LOAD_FAST                6 (log_path)
    # 171         944 LOAD_CONST              21 (10485760)
    # 172         946 LOAD_CONST              22 (5)
    # 173         948 LOAD_CONST              23 ('utf-8')
    # 169         950 KW_NAMES                24
    # 952 PRECALL                  4
    # 956 CALL                     4
    # 966 STORE_FAST              10 (file_handler)
    # 175         968 LOAD_FAST               10 (file_handler)
    # 970 LOAD_METHOD             23 (setFormatter)
    # 992 LOAD_FAST                7 (formatter)
    # 994 PRECALL                  1
    # 998 CALL                     1
    # 1008 POP_TOP
    # 176        1010 LOAD_FAST                8 (root_logger)
    # 1012 LOAD_METHOD             24 (addHandler)
    # 1034 LOAD_FAST               10 (file_handler)
    # 1036 PRECALL                  1
    # 1040 CALL                     1
    # 1050 POP_TOP
    # 177        1052 LOAD_FAST                8 (root_logger)
    # 1054 LOAD_METHOD             25 (info)
    # 1076 LOAD_CONST              25 ('File logging enabled: ')
    # 1078 LOAD_FAST                6 (log_path)
    # 1080 FORMAT_VALUE             0
    # 1082 BUILD_STRING             2
    # 1084 PRECALL                  1
    # 1088 CALL                     1
    # 1098 POP_TOP
    # 178        1100 LOAD_FAST                4 (cleanup_result)
    # 1102 LOAD_CONST              26 ('error')
    # 1104 BINARY_SUBSCR
    # 1114 POP_JUMP_FORWARD_IF_FALSE    40 (to 1196)
    # 179        1116 LOAD_FAST                8 (root_logger)
    # 1118 LOAD_METHOD             26 (warning)
    # 180        1140 LOAD_CONST              27 ('Old log cleanup failed: error=')
    # 181        1142 LOAD_FAST                4 (cleanup_result)
    # 1144 LOAD_CONST              26 ('error')
    # 1146 BINARY_SUBSCR
    # 180        1156 FORMAT_VALUE             0
    # 1158 LOAD_CONST              28 (', cutoff=')
    # 181        1160 LOAD_FAST                4 (cleanup_result)
    # 1162 LOAD_CONST              29 ('cutoff')
    # 1164 BINARY_SUBSCR
    # 180        1174 FORMAT_VALUE             0
    # 1176 BUILD_STRING             4
    # 179        1178 PRECALL                  1
    # 1182 CALL                     1
    # 1192 POP_TOP
    # 1194 JUMP_FORWARD            48 (to 1292)
    # 184     >> 1196 LOAD_FAST                8 (root_logger)
    # 1198 LOAD_METHOD             25 (info)
    # 185        1220 LOAD_CONST              30 ('Old log cleanup completed: removed=')
    # 186        1222 LOAD_FAST                4 (cleanup_result)
    # 1224 LOAD_CONST              31 ('removed')
    # 1226 BINARY_SUBSCR
    # 185        1236 FORMAT_VALUE             0
    # 1238 LOAD_CONST              32 (', failed=')
    # 187        1240 LOAD_FAST                4 (cleanup_result)
    # 1242 LOAD_CONST              33 ('failed')
    # 1244 BINARY_SUBSCR
    # 185        1254 FORMAT_VALUE             0
    # 1256 LOAD_CONST              28 (', cutoff=')
    # 188        1258 LOAD_FAST                4 (cleanup_result)
    # 1260 LOAD_CONST              29 ('cutoff')
    # 1262 BINARY_SUBSCR
    # 185        1272 FORMAT_VALUE             0
    # 1274 BUILD_STRING             6
    # 184        1276 PRECALL                  1
    # 1280 CALL                     1
    # 1290 POP_TOP
    # >> 1292 JUMP_FORWARD            89 (to 1472)
    # >> 1294 PUSH_EXC_INFO
    # 190        1296 LOAD_GLOBAL             54 (PermissionError)
    # 1308 CHECK_EXC_MATCH
    # 1310 POP_JUMP_FORWARD_IF_FALSE    34 (to 1380)
    # 1312 STORE_FAST              11 (e)
    # 191        1314 LOAD_FAST                8 (root_logger)
    # 1316 LOAD_METHOD             26 (warning)
    # 1338 LOAD_CONST              34 ('File logging disabled (permission denied): ')
    # 1340 LOAD_FAST               11 (e)
    # 1342 FORMAT_VALUE             0
    # 1344 BUILD_STRING             2
    # 1346 PRECALL                  1
    # 1350 CALL                     1
    # 1360 POP_TOP
    # 1362 POP_EXCEPT
    # 1364 LOAD_CONST              35 (None)
    # 1366 STORE_FAST              11 (e)
    # 1368 DELETE_FAST             11 (e)
    # 1370 JUMP_FORWARD            50 (to 1472)
    # >> 1372 LOAD_CONST              35 (None)
    # 1374 STORE_FAST              11 (e)
    # 1376 DELETE_FAST             11 (e)
    # 1378 RERAISE                  1
    # 192     >> 1380 LOAD_GLOBAL             56 (Exception)
    # 1392 CHECK_EXC_MATCH
    # 1394 POP_JUMP_FORWARD_IF_FALSE    34 (to 1464)
    # 1396 STORE_FAST              11 (e)
    # 193        1398 LOAD_FAST                8 (root_logger)
    # 1400 LOAD_METHOD             26 (warning)
    # 1422 LOAD_CONST              36 ('Failed to setup file logging: ')
    # 1424 LOAD_FAST               11 (e)
    # 1426 FORMAT_VALUE             0
    # 1428 BUILD_STRING             2
    # 1430 PRECALL                  1
    # 1434 CALL                     1
    # 1444 POP_TOP
    # 1446 POP_EXCEPT
    # 1448 LOAD_CONST              35 (None)
    # 1450 STORE_FAST              11 (e)
    # 1452 DELETE_FAST             11 (e)
    # 1454 JUMP_FORWARD             8 (to 1472)
    # >> 1456 LOAD_CONST              35 (None)
    # 1458 STORE_FAST              11 (e)
    # 1460 DELETE_FAST             11 (e)
    # 1462 RERAISE                  1
    # 192     >> 1464 RERAISE                  0
    # >> 1466 COPY                     3
    # 1468 POP_EXCEPT
    # 1470 RERAISE                  1
    # 195     >> 1472 LOAD_GLOBAL             59 (NULL + _write_bootstrap_log)
    # 1484 LOAD_CONST              37 ('setup_logging completed')
    # 1486 PRECALL                  1
    # 1490 CALL                     1
    # 1500 POP_TOP
    # 196        1502 LOAD_FAST                8 (root_logger)
    # 1504 RETURN_VALUE
    # >> 1506 PUSH_EXC_INFO
    # 197        1508 LOAD_GLOBAL             56 (Exception)
    # 1520 CHECK_EXC_MATCH
    # 1522 POP_JUMP_FORWARD_IF_FALSE   125 (to 1774)
    # 1524 STORE_FAST              12 (setup_error)
    # 198        1526 LOAD_GLOBAL             59 (NULL + _write_bootstrap_log)
    # 199        1538 LOAD_CONST              38 ('setup_logging fatal: ')
    # 1540 LOAD_GLOBAL             61 (NULL + type)
    # 1552 LOAD_FAST               12 (setup_error)
    # 1554 PRECALL                  1
    # 1558 CALL                     1
    # 1568 LOAD_ATTR               31 (__name__)
    # 1578 FORMAT_VALUE             0
    # 1580 LOAD_CONST              39 (': ')
    # 1582 LOAD_FAST               12 (setup_error)
    # 1584 FORMAT_VALUE             0
    # 1586 BUILD_STRING             4
    # 198        1588 PRECALL                  1
    # 1592 CALL                     1
    # 1602 POP_TOP
    # 201        1604 LOAD_GLOBAL             31 (NULL + logging)
    # 1616 LOAD_ATTR               32 (basicConfig)
    # 202        1626 LOAD_GLOBAL             30 (logging)
    # 1638 LOAD_ATTR               19 (INFO)
    # 203        1648 LOAD_CONST              20 ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 201        1650 KW_NAMES                40
    # 1652 PRECALL                  2
    # 1656 CALL                     2
    # 1666 POP_TOP
    # 205        1668 LOAD_GLOBAL             31 (NULL + logging)
    # 1680 LOAD_ATTR               17 (getLogger)
    # 1690 LOAD_CONST              41 ('tfstudio.bootstrap')
    # 1692 PRECALL                  1
    # 1696 CALL                     1
    # 1706 STORE_FAST              13 (fallback_logger)
    # 206        1708 LOAD_FAST               13 (fallback_logger)
    # 1710 LOAD_METHOD             33 (error)
    # 207        1732 LOAD_CONST              42 ('Logging bootstrap failed; using fallback logger: %s')
    # 208        1734 LOAD_FAST               12 (setup_error)
    # 206        1736 PRECALL                  2
    # 1740 CALL                     2
    # 1750 POP_TOP
    # 210        1752 LOAD_FAST               13 (fallback_logger)
    # 1754 SWAP                     2
    # 1756 POP_EXCEPT
    # 1758 LOAD_CONST              35 (None)
    # 1760 STORE_FAST              12 (setup_error)
    # 1762 DELETE_FAST             12 (setup_error)
    # 1764 RETURN_VALUE
    # >> 1766 LOAD_CONST              35 (None)
    # 1768 STORE_FAST              12 (setup_error)
    # 1770 DELETE_FAST             12 (setup_error)
    # 1772 RERAISE                  1
    # 197     >> 1774 RERAISE                  0
    # >> 1776 COPY                     3
    # 1778 POP_EXCEPT
    # 1780 RERAISE                  1
    # ExceptionTable:
    # 80 to 934 -> 1506 [0]
    # 938 to 1290 -> 1294 [0]
    # 1292 to 1292 -> 1506 [0]
    # 1294 to 1312 -> 1466 [1] lasti
    # 1314 to 1360 -> 1372 [1] lasti
    # 1362 to 1370 -> 1506 [0]
    # 1372 to 1396 -> 1466 [1] lasti
    # 1398 to 1444 -> 1456 [1] lasti
    # 1446 to 1454 -> 1506 [0]
    # 1456 to 1464 -> 1466 [1] lasti
    # 1466 to 1502 -> 1506 [0]
    # 1506 to 1524 -> 1776 [1] lasti
    # 1526 to 1752 -> 1766 [1] lasti
    # 1754 to 1754 -> 1776 [1] lasti
    # 1766 to 1774 -> 1776 [1] lasti
    # Disassembly of <code object cleanup_old_tfstudio_logs at 0x000001EBD6FB8640, file "main.py", line 86>:
    # 0 COPY_FREE_VARS           2
    # 86           2 RESUME                   0
    # 88           4 LOAD_CONST               1 (0)
    # 6 STORE_FAST               2 (removed_files)
    # 89           8 LOAD_CONST               1 (0)
    # 10 STORE_FAST               3 (skipped_files)
    # 90          12 LOAD_CONST               1 (0)
    # 14 STORE_FAST               4 (failed_files)
    # 92          16 LOAD_FAST                1 (retention_days)
    # 18 LOAD_CONST               2 (1)
    # 20 COMPARE_OP               0 (<)
    # 26 POP_JUMP_FORWARD_IF_FALSE     2 (to 32)
    # 93          28 LOAD_CONST               2 (1)
    # 30 STORE_FAST               1 (retention_days)
    # 95     >>   32 LOAD_DEREF              11 (datetime)
    # 34 LOAD_METHOD              0 (now)
    # 56 PRECALL                  0
    # 60 CALL                     0
    # 70 LOAD_METHOD              1 (date)
    # 92 PRECALL                  0
    # 96 CALL                     0
    # 106 PUSH_NULL
    # 108 LOAD_DEREF              12 (timedelta)
    # 110 LOAD_FAST                1 (retention_days)
    # 112 LOAD_CONST               2 (1)
    # 114 BINARY_OP               10 (-)
    # 118 KW_NAMES                 3
    # 120 PRECALL                  1
    # 124 CALL                     1
    # 134 BINARY_OP               10 (-)
    # 138 STORE_FAST               5 (cutoff_date)
    # 97         140 NOP
    # 98         142 LOAD_GLOBAL              5 (NULL + os)
    # 154 LOAD_ATTR                3 (listdir)
    # 164 LOAD_FAST                0 (log_directory)
    # 166 PRECALL                  1
    # 170 CALL                     1
    # 180 GET_ITER
    # >>  182 FOR_ITER               231 (to 646)
    # 184 STORE_FAST               6 (filename)
    # 99         186 LOAD_FAST                6 (filename)
    # 188 LOAD_METHOD              4 (startswith)
    # 210 LOAD_CONST               4 ('tfstudio_')
    # 212 PRECALL                  1
    # 216 CALL                     1
    # 226 POP_JUMP_FORWARD_IF_FALSE    21 (to 270)
    # 228 LOAD_FAST                6 (filename)
    # 230 LOAD_METHOD              5 (endswith)
    # 252 LOAD_CONST               5 ('.log')
    # 254 PRECALL                  1
    # 258 CALL                     1
    # 268 POP_JUMP_FORWARD_IF_TRUE     1 (to 272)
    # 100     >>  270 JUMP_BACKWARD           45 (to 182)
    # 102     >>  272 LOAD_FAST                6 (filename)
    # 274 LOAD_GLOBAL             13 (NULL + len)
    # 286 LOAD_CONST               4 ('tfstudio_')
    # 288 PRECALL                  1
    # 292 CALL                     1
    # 302 LOAD_GLOBAL             13 (NULL + len)
    # 314 LOAD_CONST               5 ('.log')
    # 316 PRECALL                  1
    # 320 CALL                     1
    # 330 UNARY_NEGATIVE
    # 332 BUILD_SLICE              2
    # 334 BINARY_SUBSCR
    # 344 STORE_FAST               7 (date_part)
    # 103         346 NOP
    # 104         348 LOAD_DEREF              11 (datetime)
    # 350 LOAD_METHOD              7 (strptime)
    # 372 LOAD_FAST                7 (date_part)
    # 374 LOAD_CONST               6 ('%Y%m%d')
    # 376 PRECALL                  2
    # 380 CALL                     2
    # 390 LOAD_METHOD              1 (date)
    # 412 PRECALL                  0
    # 416 CALL                     0
    # 426 STORE_FAST               8 (file_date)
    # 428 JUMP_FORWARD            21 (to 472)
    # >>  430 PUSH_EXC_INFO
    # 105         432 LOAD_GLOBAL             16 (ValueError)
    # 444 CHECK_EXC_MATCH
    # 446 POP_JUMP_FORWARD_IF_FALSE     8 (to 464)
    # 448 POP_TOP
    # 106         450 LOAD_FAST                3 (skipped_files)
    # 452 LOAD_CONST               2 (1)
    # 454 BINARY_OP               13 (+=)
    # 458 STORE_FAST               3 (skipped_files)
    # 107         460 POP_EXCEPT
    # 462 JUMP_BACKWARD          141 (to 182)
    # 105     >>  464 RERAISE                  0
    # >>  466 COPY                     3
    # 468 POP_EXCEPT
    # 470 RERAISE                  1
    # 109     >>  472 LOAD_FAST                8 (file_date)
    # 474 LOAD_FAST                5 (cutoff_date)
    # 476 COMPARE_OP               0 (<)
    # 482 POP_JUMP_FORWARD_IF_FALSE    80 (to 644)
    # 110         484 LOAD_GLOBAL              4 (os)
    # 496 LOAD_ATTR                9 (path)
    # 506 LOAD_METHOD             10 (join)
    # 528 LOAD_FAST                0 (log_directory)
    # 530 LOAD_FAST                6 (filename)
    # 532 PRECALL                  2
    # 536 CALL                     2
    # 546 STORE_FAST               9 (file_path)
    # 111         548 NOP
    # 112         550 LOAD_GLOBAL              5 (NULL + os)
    # 562 LOAD_ATTR               11 (remove)
    # 572 LOAD_FAST                9 (file_path)
    # 574 PRECALL                  1
    # 578 CALL                     1
    # 588 POP_TOP
    # 113         590 LOAD_FAST                2 (removed_files)
    # 592 LOAD_CONST               2 (1)
    # 594 BINARY_OP               13 (+=)
    # 598 STORE_FAST               2 (removed_files)
    # 600 JUMP_BACKWARD          210 (to 182)
    # >>  602 PUSH_EXC_INFO
    # 114         604 LOAD_GLOBAL             24 (Exception)
    # 616 CHECK_EXC_MATCH
    # 618 POP_JUMP_FORWARD_IF_FALSE     8 (to 636)
    # 620 POP_TOP
    # 115         622 LOAD_FAST                4 (failed_files)
    # 624 LOAD_CONST               2 (1)
    # 626 BINARY_OP               13 (+=)
    # 630 STORE_FAST               4 (failed_files)
    # 632 POP_EXCEPT
    # 634 JUMP_BACKWARD          227 (to 182)
    # 114     >>  636 RERAISE                  0
    # >>  638 COPY                     3
    # 640 POP_EXCEPT
    # 642 RERAISE                  1
    # 109     >>  644 JUMP_BACKWARD          232 (to 182)
    # 98     >>  646 JUMP_FORWARD            62 (to 772)
    # >>  648 PUSH_EXC_INFO
    # 116         650 LOAD_GLOBAL             24 (Exception)
    # 662 CHECK_EXC_MATCH
    # 664 POP_JUMP_FORWARD_IF_FALSE    49 (to 764)
    # 666 STORE_FAST              10 (e)
    # 118         668 LOAD_FAST                2 (removed_files)
    # 119         670 LOAD_FAST                3 (skipped_files)
    # 120         672 LOAD_FAST                4 (failed_files)
    # 121         674 LOAD_GLOBAL             27 (NULL + str)
    # 686 LOAD_FAST               10 (e)
    # 688 PRECALL                  1
    # 692 CALL                     1
    # 122         702 LOAD_FAST                5 (cutoff_date)
    # 704 LOAD_METHOD             14 (isoformat)
    # 726 PRECALL                  0
    # 730 CALL                     0
    # 117         740 LOAD_CONST               7 (('removed', 'skipped', 'failed', 'error', 'cutoff'))
    # 742 BUILD_CONST_KEY_MAP      5
    # 744 SWAP                     2
    # 746 POP_EXCEPT
    # 748 LOAD_CONST               8 (None)
    # 750 STORE_FAST              10 (e)
    # 752 DELETE_FAST             10 (e)
    # 754 RETURN_VALUE
    # >>  756 LOAD_CONST               8 (None)
    # 758 STORE_FAST              10 (e)
    # 760 DELETE_FAST             10 (e)
    # 762 RERAISE                  1
    # 116     >>  764 RERAISE                  0
    # >>  766 COPY                     3
    # 768 POP_EXCEPT
    # 770 RERAISE                  1
    # 126     >>  772 LOAD_FAST                2 (removed_files)
    # 127         774 LOAD_FAST                3 (skipped_files)
    # 128         776 LOAD_FAST                4 (failed_files)
    # 129         778 LOAD_CONST               9 ('')
    # 130         780 LOAD_FAST                5 (cutoff_date)
    # 782 LOAD_METHOD             14 (isoformat)
    # 804 PRECALL                  0
    # 808 CALL                     0
    # 125         818 LOAD_CONST               7 (('removed', 'skipped', 'failed', 'error', 'cutoff'))
    # 820 BUILD_CONST_KEY_MAP      5
    # 822 RETURN_VALUE
    # ExceptionTable:
    # 142 to 344 -> 648 [0]
    # 348 to 426 -> 430 [1]
    # 428 to 428 -> 648 [0]
    # 430 to 458 -> 466 [2] lasti
    # 460 to 462 -> 648 [0]
    # 464 to 464 -> 466 [2] lasti
    # 466 to 546 -> 648 [0]
    # 550 to 598 -> 602 [1]
    # 600 to 600 -> 648 [0]
    # 602 to 630 -> 638 [2] lasti
    # 632 to 634 -> 648 [0]
    # 636 to 636 -> 638 [2] lasti
    # 638 to 644 -> 648 [0]
    # 648 to 666 -> 766 [1] lasti
    # 668 to 742 -> 756 [1] lasti
    # 744 to 744 -> 766 [1] lasti
    # 756 to 764 -> 766 [1] lasti

def get_base_path():
    """Get the base path for resources"""
    # 229           0 RESUME                   0
    # 231           2 LOAD_GLOBAL              0 (IS_FROZEN)
    # 14 POP_JUMP_FORWARD_IF_FALSE    61 (to 138)
    # 234          16 LOAD_GLOBAL              3 (NULL + str)
    # 28 LOAD_GLOBAL              5 (NULL + Path)
    # 40 LOAD_GLOBAL              6 (sys)
    # 52 LOAD_ATTR                4 (executable)
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 LOAD_METHOD              5 (resolve)
    # 98 PRECALL                  0
    # 102 CALL                     0
    # 112 LOAD_ATTR                6 (parent)
    # 122 PRECALL                  1
    # 126 CALL                     1
    # 136 RETURN_VALUE
    # 237     >>  138 LOAD_GLOBAL              3 (NULL + str)
    # 150 LOAD_GLOBAL              5 (NULL + Path)
    # 162 LOAD_GLOBAL             14 (__file__)
    # 174 PRECALL                  1
    # 178 CALL                     1
    # 188 LOAD_METHOD              5 (resolve)
    # 210 PRECALL                  0
    # 214 CALL                     0
    # 224 LOAD_ATTR                6 (parent)
    # 234 PRECALL                  1
    # 238 CALL                     1
    # 248 RETURN_VALUE

def _get_app_version_for_title():
    """Read app version from version.json without importing backend services."""
    # 240           0 RESUME                   0
    # 242           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (json)
    # 8 STORE_FAST               0 (json)
    # 245          10 LOAD_GLOBAL              3 (NULL + Path)
    # 22 LOAD_GLOBAL              5 (NULL + get_base_path)
    # 34 PRECALL                  0
    # 38 CALL                     0
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 LOAD_CONST               3 ('version.json')
    # 64 BINARY_OP               11 (/)
    # 246          68 LOAD_GLOBAL              3 (NULL + Path)
    # 80 LOAD_GLOBAL              6 (__file__)
    # 92 PRECALL                  1
    # 96 CALL                     1
    # 106 LOAD_METHOD              4 (resolve)
    # 128 PRECALL                  0
    # 132 CALL                     0
    # 142 LOAD_ATTR                5 (parent)
    # 152 LOAD_CONST               3 ('version.json')
    # 154 BINARY_OP               11 (/)
    # 244         158 BUILD_LIST               2
    # 160 STORE_FAST               1 (candidates)
    # 249         162 LOAD_FAST                1 (candidates)
    # 164 GET_ITER
    # >>  166 FOR_ITER               209 (to 586)
    # 168 STORE_FAST               2 (version_file)
    # 250         170 NOP
    # 251         172 LOAD_FAST                2 (version_file)
    # 174 LOAD_METHOD              6 (exists)
    # 196 PRECALL                  0
    # 200 CALL                     0
    # 210 POP_JUMP_FORWARD_IF_TRUE     1 (to 214)
    # 252         212 JUMP_BACKWARD           24 (to 166)
    # 253     >>  214 LOAD_GLOBAL             15 (NULL + open)
    # 226 LOAD_FAST                2 (version_file)
    # 228 LOAD_CONST               4 ('r')
    # 230 LOAD_CONST               5 ('utf-8')
    # 232 KW_NAMES                 6
    # 234 PRECALL                  3
    # 238 CALL                     3
    # 248 BEFORE_WITH
    # 250 STORE_FAST               3 (f)
    # 254         252 LOAD_FAST                0 (json)
    # 254 LOAD_METHOD              8 (load)
    # 276 LOAD_FAST                3 (f)
    # 278 PRECALL                  1
    # 282 CALL                     1
    # 292 STORE_FAST               4 (version_info)
    # 253         294 LOAD_CONST               2 (None)
    # 296 LOAD_CONST               2 (None)
    # 298 LOAD_CONST               2 (None)
    # 300 PRECALL                  2
    # 304 CALL                     2
    # 314 POP_TOP
    # 316 JUMP_FORWARD            11 (to 340)
    # >>  318 PUSH_EXC_INFO
    # 320 WITH_EXCEPT_START
    # 322 POP_JUMP_FORWARD_IF_TRUE     4 (to 332)
    # 324 RERAISE                  2
    # >>  326 COPY                     3
    # 328 POP_EXCEPT
    # 330 RERAISE                  1
    # >>  332 POP_TOP
    # 334 POP_EXCEPT
    # 336 POP_TOP
    # 338 POP_TOP
    # 255     >>  340 LOAD_GLOBAL             19 (NULL + str)
    # 352 LOAD_FAST                4 (version_info)
    # 354 LOAD_METHOD             10 (get)
    # 376 LOAD_CONST               7 ('version')
    # 378 LOAD_CONST               8 ('')
    # 380 PRECALL                  2
    # 384 CALL                     2
    # 394 PRECALL                  1
    # 398 CALL                     1
    # 408 LOAD_METHOD             11 (strip)
    # 430 PRECALL                  0
    # 434 CALL                     0
    # 444 STORE_FAST               5 (version)
    # 256         446 LOAD_FAST                5 (version)
    # 448 POP_JUMP_FORWARD_IF_FALSE     4 (to 458)
    # 257         450 LOAD_FAST                5 (version)
    # 452 SWAP                     2
    # 454 POP_TOP
    # 456 RETURN_VALUE
    # 256     >>  458 JUMP_BACKWARD          147 (to 166)
    # >>  460 PUSH_EXC_INFO
    # 258         462 LOAD_GLOBAL             24 (Exception)
    # 474 CHECK_EXC_MATCH
    # 476 POP_JUMP_FORWARD_IF_FALSE    50 (to 578)
    # 478 STORE_FAST               6 (e)
    # 259         480 LOAD_GLOBAL             27 (NULL + _write_bootstrap_log)
    # 260         492 LOAD_CONST               9 ('version read failed: ')
    # 494 LOAD_FAST                2 (version_file)
    # 496 FORMAT_VALUE             0
    # 498 LOAD_CONST              10 (' (')
    # 500 LOAD_GLOBAL             29 (NULL + type)
    # 512 LOAD_FAST                6 (e)
    # 514 PRECALL                  1
    # 518 CALL                     1
    # 528 LOAD_ATTR               15 (__name__)
    # 538 FORMAT_VALUE             0
    # 540 LOAD_CONST              11 (')')
    # 542 BUILD_STRING             5
    # 259         544 PRECALL                  1
    # 548 CALL                     1
    # 558 POP_TOP
    # 560 POP_EXCEPT
    # 562 LOAD_CONST               2 (None)
    # 564 STORE_FAST               6 (e)
    # 566 DELETE_FAST              6 (e)
    # 568 JUMP_BACKWARD          202 (to 166)
    # >>  570 LOAD_CONST               2 (None)
    # 572 STORE_FAST               6 (e)
    # 574 DELETE_FAST              6 (e)
    # 576 RERAISE                  1
    # 258     >>  578 RERAISE                  0
    # >>  580 COPY                     3
    # 582 POP_EXCEPT
    # 584 RERAISE                  1
    # 263     >>  586 LOAD_CONST              12 ('0.0.0')
    # 588 RETURN_VALUE
    # ExceptionTable:
    # 172 to 210 -> 460 [1]
    # 214 to 248 -> 460 [1]
    # 250 to 292 -> 318 [2] lasti
    # 294 to 316 -> 460 [1]
    # 318 to 324 -> 326 [4] lasti
    # 326 to 330 -> 460 [1]
    # 332 to 332 -> 326 [4] lasti
    # 334 to 450 -> 460 [1]
    # 460 to 478 -> 580 [2] lasti
    # 480 to 558 -> 570 [2] lasti
    # 570 to 578 -> 580 [2] lasti

def _is_valid_webview2_version(version):
    # 266           0 RESUME                   0
    # 267           2 LOAD_FAST                0 (version)
    # 4 JUMP_IF_TRUE_OR_POP      1 (to 8)
    # 6 LOAD_CONST               1 ('')
    # >>    8 LOAD_METHOD              0 (strip)
    # 30 PRECALL                  0
    # 34 CALL                     0
    # 44 STORE_FAST               1 (normalized)
    # 268          46 LOAD_GLOBAL              3 (NULL + bool)
    # 58 LOAD_FAST                1 (normalized)
    # 60 JUMP_IF_FALSE_OR_POP     5 (to 72)
    # 62 LOAD_FAST                1 (normalized)
    # 64 LOAD_CONST               2 ('0.0.0.0')
    # 66 COMPARE_OP               3 (!=)
    # >>   72 PRECALL                  1
    # 76 CALL                     1
    # 86 RETURN_VALUE

def _get_webview2_runtime_version():
    """Read installed WebView2 runtime version from registry on Windows."""
    # 271           0 RESUME                   0
    # 273           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               3 (!=)
    # 32 POP_JUMP_FORWARD_IF_FALSE     2 (to 38)
    # 274          34 LOAD_CONST               2 ('')
    # 36 RETURN_VALUE
    # 276     >>   38 NOP
    # 277          40 LOAD_CONST               3 (0)
    # 42 LOAD_CONST               4 (None)
    # 44 IMPORT_NAME              2 (winreg)
    # 46 STORE_FAST               0 (winreg)
    # 48 JUMP_FORWARD            17 (to 84)
    # >>   50 PUSH_EXC_INFO
    # 278          52 LOAD_GLOBAL              6 (Exception)
    # 64 CHECK_EXC_MATCH
    # 66 POP_JUMP_FORWARD_IF_FALSE     4 (to 76)
    # 68 POP_TOP
    # 279          70 POP_EXCEPT
    # 72 LOAD_CONST               2 ('')
    # 74 RETURN_VALUE
    # 278     >>   76 RERAISE                  0
    # >>   78 COPY                     3
    # 80 POP_EXCEPT
    # 82 RERAISE                  1
    # 281     >>   84 BUILD_LIST               0
    # 86 STORE_FAST               1 (key_paths)
    # 282          88 LOAD_GLOBAL              9 (NULL + hasattr)
    # 100 LOAD_FAST                0 (winreg)
    # 102 LOAD_CONST               5 ('KEY_WOW64_64KEY')
    # 104 PRECALL                  2
    # 108 CALL                     2
    # 118 POP_JUMP_FORWARD_IF_FALSE    36 (to 192)
    # 283         120 LOAD_FAST                1 (key_paths)
    # 122 LOAD_METHOD              5 (append)
    # 144 LOAD_FAST                0 (winreg)
    # 146 LOAD_ATTR                6 (HKEY_LOCAL_MACHINE)
    # 156 LOAD_CONST               6 ('SOFTWARE\\WOW6432Node\\Microsoft\\EdgeUpdate\\Clients\\')
    # 158 LOAD_GLOBAL             14 (WEBVIEW2_RUNTIME_GUID)
    # 170 FORMAT_VALUE             0
    # 172 BUILD_STRING             2
    # 174 BUILD_TUPLE              2
    # 176 PRECALL                  1
    # 180 CALL                     1
    # 190 POP_TOP
    # 284     >>  192 LOAD_FAST                1 (key_paths)
    # 194 LOAD_METHOD              8 (extend)
    # 285         216 LOAD_FAST                0 (winreg)
    # 218 LOAD_ATTR                6 (HKEY_LOCAL_MACHINE)
    # 228 LOAD_CONST               7 ('SOFTWARE\\Microsoft\\EdgeUpdate\\Clients\\')
    # 230 LOAD_GLOBAL             14 (WEBVIEW2_RUNTIME_GUID)
    # 242 FORMAT_VALUE             0
    # 244 BUILD_STRING             2
    # 246 BUILD_TUPLE              2
    # 286         248 LOAD_FAST                0 (winreg)
    # 250 LOAD_ATTR                9 (HKEY_CURRENT_USER)
    # 260 LOAD_CONST               8 ('Software\\Microsoft\\EdgeUpdate\\Clients\\')
    # 262 LOAD_GLOBAL             14 (WEBVIEW2_RUNTIME_GUID)
    # 274 FORMAT_VALUE             0
    # 276 BUILD_STRING             2
    # 278 BUILD_TUPLE              2
    # 284         280 BUILD_LIST               2
    # 282 PRECALL                  1
    # 286 CALL                     1
    # 296 POP_TOP
    # 289         298 LOAD_FAST                1 (key_paths)
    # 300 GET_ITER
    # >>  302 FOR_ITER               158 (to 620)
    # 304 UNPACK_SEQUENCE          2
    # 308 STORE_FAST               2 (hive)
    # 310 STORE_FAST               3 (key_path)
    # 290         312 NOP
    # 291         314 LOAD_FAST                0 (winreg)
    # 316 LOAD_METHOD             10 (OpenKey)
    # 338 LOAD_FAST                2 (hive)
    # 340 LOAD_FAST                3 (key_path)
    # 342 LOAD_CONST               3 (0)
    # 344 LOAD_FAST                0 (winreg)
    # 346 LOAD_ATTR               11 (KEY_READ)
    # 356 PRECALL                  4
    # 360 CALL                     4
    # 370 BEFORE_WITH
    # 372 STORE_FAST               4 (key)
    # 292         374 LOAD_FAST                0 (winreg)
    # 376 LOAD_METHOD             12 (QueryValueEx)
    # 398 LOAD_FAST                4 (key)
    # 400 LOAD_CONST               9 ('pv')
    # 402 PRECALL                  2
    # 406 CALL                     2
    # 416 UNPACK_SEQUENCE          2
    # 420 STORE_FAST               5 (pv)
    # 422 STORE_FAST               6 (_)
    # 293         424 LOAD_GLOBAL             27 (NULL + _is_valid_webview2_version)
    # 436 LOAD_GLOBAL             29 (NULL + str)
    # 448 LOAD_FAST                5 (pv)
    # 450 PRECALL                  1
    # 454 CALL                     1
    # 464 PRECALL                  1
    # 468 CALL                     1
    # 478 POP_JUMP_FORWARD_IF_FALSE    29 (to 538)
    # 294         480 LOAD_GLOBAL             29 (NULL + str)
    # 492 LOAD_FAST                5 (pv)
    # 494 PRECALL                  1
    # 498 CALL                     1
    # 291         508 SWAP                     2
    # 510 LOAD_CONST               4 (None)
    # 512 LOAD_CONST               4 (None)
    # 514 LOAD_CONST               4 (None)
    # 516 PRECALL                  2
    # 520 CALL                     2
    # 530 POP_TOP
    # 532 SWAP                     2
    # 534 POP_TOP
    # 536 RETURN_VALUE
    # 293     >>  538 NOP
    # 291         540 LOAD_CONST               4 (None)
    # 542 LOAD_CONST               4 (None)
    # 544 LOAD_CONST               4 (None)
    # 546 PRECALL                  2
    # 550 CALL                     2
    # 560 POP_TOP
    # 562 JUMP_FORWARD            11 (to 586)
    # >>  564 PUSH_EXC_INFO
    # 566 WITH_EXCEPT_START
    # 568 POP_JUMP_FORWARD_IF_TRUE     4 (to 578)
    # 570 RERAISE                  2
    # >>  572 COPY                     3
    # 574 POP_EXCEPT
    # 576 RERAISE                  1
    # >>  578 POP_TOP
    # 580 POP_EXCEPT
    # 582 POP_TOP
    # 584 POP_TOP
    # >>  586 JUMP_BACKWARD          143 (to 302)
    # >>  588 PUSH_EXC_INFO
    # 295         590 LOAD_GLOBAL              6 (Exception)
    # 602 CHECK_EXC_MATCH
    # 604 POP_JUMP_FORWARD_IF_FALSE     3 (to 612)
    # 606 POP_TOP
    # 296         608 POP_EXCEPT
    # 610 JUMP_BACKWARD          155 (to 302)
    # 295     >>  612 RERAISE                  0
    # >>  614 COPY                     3
    # 616 POP_EXCEPT
    # 618 RERAISE                  1
    # 298     >>  620 LOAD_CONST               2 ('')
    # 622 RETURN_VALUE
    # ExceptionTable:
    # 40 to 46 -> 50 [0]
    # 50 to 68 -> 78 [1] lasti
    # 76 to 76 -> 78 [1] lasti
    # 314 to 370 -> 588 [1]
    # 372 to 506 -> 564 [2] lasti
    # 508 to 530 -> 588 [1]
    # 540 to 562 -> 588 [1]
    # 564 to 570 -> 572 [4] lasti
    # 572 to 576 -> 588 [1]
    # 578 to 578 -> 572 [4] lasti
    # 580 to 584 -> 588 [1]
    # 588 to 606 -> 614 [2] lasti
    # 612 to 612 -> 614 [2] lasti

def _download_webview2_bootstrapper(bootstrapper_path):
    """Download Microsoft WebView2 Evergreen bootstrapper."""
    # 301           0 RESUME                   0
    # 303           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (urllib.request)
    # 8 STORE_FAST               1 (urllib)
    # 305          10 LOAD_FAST                0 (bootstrapper_path)
    # 12 LOAD_ATTR                1 (parent)
    # 22 LOAD_METHOD              2 (mkdir)
    # 44 LOAD_CONST               3 (True)
    # 46 LOAD_CONST               3 (True)
    # 48 KW_NAMES                 4
    # 50 PRECALL                  2
    # 54 CALL                     2
    # 64 POP_TOP
    # 306          66 LOAD_FAST                1 (urllib)
    # 68 LOAD_ATTR                3 (request)
    # 78 LOAD_METHOD              4 (urlopen)
    # 100 LOAD_GLOBAL             10 (WEBVIEW2_BOOTSTRAPPER_URL)
    # 112 LOAD_CONST               5 (60)
    # 114 KW_NAMES                 6
    # 116 PRECALL                  2
    # 120 CALL                     2
    # 130 BEFORE_WITH
    # 132 STORE_FAST               2 (response)
    # 307         134 LOAD_FAST                2 (response)
    # 136 LOAD_METHOD              6 (read)
    # 158 PRECALL                  0
    # 162 CALL                     0
    # 172 STORE_FAST               3 (payload)
    # 306         174 LOAD_CONST               2 (None)
    # 176 LOAD_CONST               2 (None)
    # 178 LOAD_CONST               2 (None)
    # 180 PRECALL                  2
    # 184 CALL                     2
    # 194 POP_TOP
    # 196 JUMP_FORWARD            11 (to 220)
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
    # 309     >>  220 LOAD_GLOBAL             15 (NULL + len)
    # 232 LOAD_FAST                3 (payload)
    # 234 PRECALL                  1
    # 238 CALL                     1
    # 248 LOAD_CONST               7 (500000)
    # 250 COMPARE_OP               0 (<)
    # 256 POP_JUMP_FORWARD_IF_FALSE    15 (to 288)
    # 310         258 LOAD_GLOBAL             17 (NULL + RuntimeError)
    # 270 LOAD_CONST               8 ('Downloaded WebView2 bootstrapper is unexpectedly small')
    # 272 PRECALL                  1
    # 276 CALL                     1
    # 286 RAISE_VARARGS            1
    # 312     >>  288 LOAD_GLOBAL             19 (NULL + open)
    # 300 LOAD_FAST                0 (bootstrapper_path)
    # 302 LOAD_CONST               9 ('wb')
    # 304 PRECALL                  2
    # 308 CALL                     2
    # 318 BEFORE_WITH
    # 320 STORE_FAST               4 (f)
    # 313         322 LOAD_FAST                4 (f)
    # 324 LOAD_METHOD             10 (write)
    # 346 LOAD_FAST                3 (payload)
    # 348 PRECALL                  1
    # 352 CALL                     1
    # 362 POP_TOP
    # 312         364 LOAD_CONST               2 (None)
    # 366 LOAD_CONST               2 (None)
    # 368 LOAD_CONST               2 (None)
    # 370 PRECALL                  2
    # 374 CALL                     2
    # 384 POP_TOP
    # 386 LOAD_CONST               2 (None)
    # 388 RETURN_VALUE
    # >>  390 PUSH_EXC_INFO
    # 392 WITH_EXCEPT_START
    # 394 POP_JUMP_FORWARD_IF_TRUE     4 (to 404)
    # 396 RERAISE                  2
    # >>  398 COPY                     3
    # 400 POP_EXCEPT
    # 402 RERAISE                  1
    # >>  404 POP_TOP
    # 406 POP_EXCEPT
    # 408 POP_TOP
    # 410 POP_TOP
    # 412 LOAD_CONST               2 (None)
    # 414 RETURN_VALUE
    # ExceptionTable:
    # 132 to 172 -> 198 [1] lasti
    # 198 to 204 -> 206 [3] lasti
    # 212 to 212 -> 206 [3] lasti
    # 320 to 362 -> 390 [1] lasti
    # 390 to 396 -> 398 [3] lasti
    # 404 to 404 -> 398 [3] lasti

def _install_webview2_runtime():
    """Install WebView2 runtime silently using Microsoft bootstrapper."""
    # 316           0 RESUME                   0
    # 318           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               3 (!=)
    # 32 POP_JUMP_FORWARD_IF_FALSE     2 (to 38)
    # 319          34 LOAD_CONST               2 ((True, ''))
    # 36 RETURN_VALUE
    # 321     >>   38 LOAD_GLOBAL              1 (NULL + os)
    # 50 LOAD_ATTR                2 (getenv)
    # 60 LOAD_CONST               3 ('LOCALAPPDATA')
    # 62 LOAD_GLOBAL              0 (os)
    # 74 LOAD_ATTR                3 (path)
    # 84 LOAD_METHOD              4 (expanduser)
    # 106 LOAD_CONST               4 ('~')
    # 108 PRECALL                  1
    # 112 CALL                     1
    # 122 PRECALL                  2
    # 126 CALL                     2
    # 136 STORE_FAST               0 (localappdata)
    # 322         138 LOAD_GLOBAL             11 (NULL + Path)
    # 150 LOAD_FAST                0 (localappdata)
    # 152 PRECALL                  1
    # 156 CALL                     1
    # 166 LOAD_CONST               5 ('TFstudio')
    # 168 BINARY_OP               11 (/)
    # 172 LOAD_CONST               6 ('runtime')
    # 174 BINARY_OP               11 (/)
    # 178 STORE_FAST               1 (runtime_dir)
    # 323         180 LOAD_FAST                1 (runtime_dir)
    # 182 LOAD_CONST               7 ('MicrosoftEdgeWebView2Setup.exe')
    # 184 BINARY_OP               11 (/)
    # 188 STORE_FAST               2 (bootstrapper_path)
    # 325         190 NOP
    # 326         192 LOAD_GLOBAL             13 (NULL + _write_bootstrap_log)
    # 204 LOAD_CONST               8 ('downloading WebView2 bootstrapper')
    # 206 PRECALL                  1
    # 210 CALL                     1
    # 220 POP_TOP
    # 327         222 LOAD_GLOBAL             15 (NULL + _download_webview2_bootstrapper)
    # 234 LOAD_FAST                2 (bootstrapper_path)
    # 236 PRECALL                  1
    # 240 CALL                     1
    # 250 POP_TOP
    # 252 JUMP_FORWARD            30 (to 314)
    # >>  254 PUSH_EXC_INFO
    # 328         256 LOAD_GLOBAL             16 (Exception)
    # 268 CHECK_EXC_MATCH
    # 270 POP_JUMP_FORWARD_IF_FALSE    17 (to 306)
    # 272 STORE_FAST               3 (download_error)
    # 329         274 LOAD_CONST               9 (False)
    # 276 LOAD_CONST              10 ('다운로드 실패: ')
    # 278 LOAD_FAST                3 (download_error)
    # 280 FORMAT_VALUE             0
    # 282 BUILD_STRING             2
    # 284 BUILD_TUPLE              2
    # 286 SWAP                     2
    # 288 POP_EXCEPT
    # 290 LOAD_CONST              11 (None)
    # 292 STORE_FAST               3 (download_error)
    # 294 DELETE_FAST              3 (download_error)
    # 296 RETURN_VALUE
    # >>  298 LOAD_CONST              11 (None)
    # 300 STORE_FAST               3 (download_error)
    # 302 DELETE_FAST              3 (download_error)
    # 304 RERAISE                  1
    # 328     >>  306 RERAISE                  0
    # >>  308 COPY                     3
    # 310 POP_EXCEPT
    # 312 RERAISE                  1
    # 331     >>  314 NOP
    # 332         316 LOAD_GLOBAL             13 (NULL + _write_bootstrap_log)
    # 328 LOAD_CONST              12 ('running WebView2 bootstrapper: ')
    # 330 LOAD_FAST                2 (bootstrapper_path)
    # 332 FORMAT_VALUE             0
    # 334 BUILD_STRING             2
    # 336 PRECALL                  1
    # 340 CALL                     1
    # 350 POP_TOP
    # 333         352 LOAD_GLOBAL             19 (NULL + subprocess)
    # 364 LOAD_ATTR               10 (run)
    # 334         374 LOAD_GLOBAL             23 (NULL + str)
    # 386 LOAD_FAST                2 (bootstrapper_path)
    # 388 PRECALL                  1
    # 392 CALL                     1
    # 402 LOAD_CONST              13 ('/silent')
    # 404 LOAD_CONST              14 ('/install')
    # 406 BUILD_LIST               3
    # 335         408 LOAD_CONST               9 (False)
    # 336         410 LOAD_CONST              15 (300)
    # 337         412 LOAD_GLOBAL              0 (os)
    # 424 LOAD_ATTR                1 (name)
    # 434 LOAD_CONST               1 ('nt')
    # 436 COMPARE_OP               2 (==)
    # 442 POP_JUMP_FORWARD_IF_FALSE    22 (to 488)
    # 444 LOAD_GLOBAL             25 (NULL + getattr)
    # 456 LOAD_GLOBAL             18 (subprocess)
    # 468 LOAD_CONST              16 ('CREATE_NO_WINDOW')
    # 470 LOAD_CONST              17 (0)
    # 472 PRECALL                  3
    # 476 CALL                     3
    # 486 JUMP_FORWARD             1 (to 490)
    # >>  488 LOAD_CONST              17 (0)
    # 333     >>  490 KW_NAMES                18
    # 492 PRECALL                  4
    # 496 CALL                     4
    # 506 STORE_FAST               4 (completed)
    # 339         508 LOAD_GLOBAL             13 (NULL + _write_bootstrap_log)
    # 520 LOAD_CONST              19 ('WebView2 bootstrapper exit code: ')
    # 522 LOAD_FAST                4 (completed)
    # 524 LOAD_ATTR               13 (returncode)
    # 534 FORMAT_VALUE             0
    # 536 BUILD_STRING             2
    # 538 PRECALL                  1
    # 542 CALL                     1
    # 552 POP_TOP
    # 554 JUMP_FORWARD            47 (to 650)
    # >>  556 PUSH_EXC_INFO
    # 340         558 LOAD_GLOBAL             18 (subprocess)
    # 570 LOAD_ATTR               14 (TimeoutExpired)
    # 580 CHECK_EXC_MATCH
    # 582 POP_JUMP_FORWARD_IF_FALSE     4 (to 592)
    # 584 POP_TOP
    # 341         586 POP_EXCEPT
    # 588 LOAD_CONST              20 ((False, '설치 시간이 초과되었습니다. 네트워크 상태를 확인해주세요.'))
    # 590 RETURN_VALUE
    # 342     >>  592 LOAD_GLOBAL             16 (Exception)
    # 604 CHECK_EXC_MATCH
    # 606 POP_JUMP_FORWARD_IF_FALSE    17 (to 642)
    # 608 STORE_FAST               5 (install_error)
    # 343         610 LOAD_CONST               9 (False)
    # 612 LOAD_CONST              21 ('설치 실행 실패: ')
    # 614 LOAD_FAST                5 (install_error)
    # 616 FORMAT_VALUE             0
    # 618 BUILD_STRING             2
    # 620 BUILD_TUPLE              2
    # 622 SWAP                     2
    # 624 POP_EXCEPT
    # 626 LOAD_CONST              11 (None)
    # 628 STORE_FAST               5 (install_error)
    # 630 DELETE_FAST              5 (install_error)
    # 632 RETURN_VALUE
    # >>  634 LOAD_CONST              11 (None)
    # 636 STORE_FAST               5 (install_error)
    # 638 DELETE_FAST              5 (install_error)
    # 640 RERAISE                  1
    # 342     >>  642 RERAISE                  0
    # >>  644 COPY                     3
    # 646 POP_EXCEPT
    # 648 RERAISE                  1
    # 345     >>  650 LOAD_GLOBAL             31 (NULL + range)
    # 662 LOAD_CONST              22 (15)
    # 664 PRECALL                  1
    # 668 CALL                     1
    # 678 GET_ITER
    # >>  680 FOR_ITER                57 (to 796)
    # 682 STORE_FAST               6 (_)
    # 346         684 LOAD_GLOBAL             33 (NULL + _get_webview2_runtime_version)
    # 696 PRECALL                  0
    # 700 CALL                     0
    # 710 STORE_FAST               7 (version)
    # 347         712 LOAD_GLOBAL             35 (NULL + _is_valid_webview2_version)
    # 724 LOAD_FAST                7 (version)
    # 726 PRECALL                  1
    # 730 CALL                     1
    # 740 POP_JUMP_FORWARD_IF_FALSE     6 (to 754)
    # 348         742 LOAD_CONST              23 (True)
    # 744 LOAD_FAST                7 (version)
    # 746 BUILD_TUPLE              2
    # 748 SWAP                     2
    # 750 POP_TOP
    # 752 RETURN_VALUE
    # 349     >>  754 LOAD_GLOBAL             37 (NULL + time)
    # 766 LOAD_ATTR               19 (sleep)
    # 776 LOAD_CONST              24 (1)
    # 778 PRECALL                  1
    # 782 CALL                     1
    # 792 POP_TOP
    # 794 JUMP_BACKWARD           58 (to 680)
    # 351     >>  796 LOAD_CONST              25 ((False, '설치 후 런타임 버전을 확인하지 못했습니다.'))
    # 798 RETURN_VALUE
    # ExceptionTable:
    # 192 to 250 -> 254 [0]
    # 254 to 272 -> 308 [1] lasti
    # 274 to 284 -> 298 [1] lasti
    # 286 to 286 -> 308 [1] lasti
    # 298 to 306 -> 308 [1] lasti
    # 316 to 552 -> 556 [0]
    # 556 to 584 -> 644 [1] lasti
    # 592 to 608 -> 644 [1] lasti
    # 610 to 620 -> 634 [1] lasti
    # 622 to 622 -> 644 [1] lasti
    # 634 to 642 -> 644 [1] lasti

def _restart_application():
    """Restart current application process."""
    # 354           0 RESUME                   0
    # 356           2 LOAD_GLOBAL              0 (sys)
    # 14 LOAD_ATTR                1 (executable)
    # 24 BUILD_LIST               1
    # 26 LOAD_GLOBAL              0 (sys)
    # 38 LOAD_ATTR                2 (argv)
    # 48 LOAD_CONST               1 (1)
    # 50 LOAD_CONST               2 (None)
    # 52 BUILD_SLICE              2
    # 54 BINARY_SUBSCR
    # 64 LIST_EXTEND              1
    # 66 STORE_FAST               0 (args)
    # 357          68 LOAD_GLOBAL              7 (NULL + subprocess)
    # 80 LOAD_ATTR                4 (Popen)
    # 358          90 LOAD_FAST                0 (args)
    # 359          92 LOAD_CONST               3 (True)
    # 360          94 LOAD_GLOBAL             10 (os)
    # 106 LOAD_ATTR                6 (name)
    # 116 LOAD_CONST               4 ('nt')
    # 118 COMPARE_OP               2 (==)
    # 124 POP_JUMP_FORWARD_IF_FALSE    22 (to 170)
    # 126 LOAD_GLOBAL             15 (NULL + getattr)
    # 138 LOAD_GLOBAL              6 (subprocess)
    # 150 LOAD_CONST               5 ('CREATE_NO_WINDOW')
    # 152 LOAD_CONST               6 (0)
    # 154 PRECALL                  3
    # 158 CALL                     3
    # 168 JUMP_FORWARD             1 (to 172)
    # >>  170 LOAD_CONST               6 (0)
    # 357     >>  172 KW_NAMES                 7
    # 174 PRECALL                  3
    # 178 CALL                     3
    # 188 POP_TOP
    # 362         190 LOAD_GLOBAL             11 (NULL + os)
    # 202 LOAD_ATTR                8 (_exit)
    # 212 LOAD_CONST               6 (0)
    # 214 PRECALL                  1
    # 218 CALL                     1
    # 228 POP_TOP
    # 230 LOAD_CONST               2 (None)
    # 232 RETURN_VALUE

def _ensure_webview2_runtime_ready():
    """Ensure WebView2 runtime exists in frozen Windows builds."""
    # 365           0 RESUME                   0
    # 367           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               3 (!=)
    # 32 POP_JUMP_FORWARD_IF_TRUE     7 (to 48)
    # 34 LOAD_GLOBAL              4 (IS_FROZEN)
    # 46 POP_JUMP_FORWARD_IF_TRUE     2 (to 52)
    # 368     >>   48 LOAD_CONST               2 (True)
    # 50 RETURN_VALUE
    # 370     >>   52 LOAD_GLOBAL              7 (NULL + _get_webview2_runtime_version)
    # 64 PRECALL                  0
    # 68 CALL                     0
    # 78 STORE_FAST               0 (version)
    # 371          80 LOAD_GLOBAL              9 (NULL + _is_valid_webview2_version)
    # 92 LOAD_FAST                0 (version)
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 POP_JUMP_FORWARD_IF_FALSE    49 (to 208)
    # 372         110 LOAD_GLOBAL             10 (logger)
    # 122 LOAD_METHOD              6 (info)
    # 144 LOAD_CONST               3 ('WebView2 runtime detected: ')
    # 146 LOAD_FAST                0 (version)
    # 148 FORMAT_VALUE             0
    # 150 BUILD_STRING             2
    # 152 PRECALL                  1
    # 156 CALL                     1
    # 166 POP_TOP
    # 373         168 LOAD_GLOBAL             15 (NULL + _write_bootstrap_log)
    # 180 LOAD_CONST               3 ('WebView2 runtime detected: ')
    # 182 LOAD_FAST                0 (version)
    # 184 FORMAT_VALUE             0
    # 186 BUILD_STRING             2
    # 188 PRECALL                  1
    # 192 CALL                     1
    # 202 POP_TOP
    # 374         204 LOAD_CONST               2 (True)
    # 206 RETURN_VALUE
    # 376     >>  208 LOAD_GLOBAL             15 (NULL + _write_bootstrap_log)
    # 220 LOAD_CONST               4 ('WebView2 runtime missing; starting auto-install')
    # 222 PRECALL                  1
    # 226 CALL                     1
    # 236 POP_TOP
    # 377         238 LOAD_GLOBAL             10 (logger)
    # 250 LOAD_METHOD              8 (warning)
    # 272 LOAD_CONST               5 ('WebView2 runtime missing. Attempting automatic installation.')
    # 274 PRECALL                  1
    # 278 CALL                     1
    # 288 POP_TOP
    # 379         290 LOAD_GLOBAL             19 (NULL + _show_info_message)
    # 380         302 LOAD_CONST               6 ('TFstudio - 웹 엔진 준비')
    # 381         304 LOAD_CONST               7 ('웹 화면 표시를 위해 필수 구성요소(WebView2)를 자동 설치합니다.\n\n최초 1회만 진행되며, 1~3분 정도 걸릴 수 있습니다.')
    # 379         306 PRECALL                  2
    # 310 CALL                     2
    # 320 POP_TOP
    # 385         322 LOAD_GLOBAL             21 (NULL + _install_webview2_runtime)
    # 334 PRECALL                  0
    # 338 CALL                     0
    # 348 UNPACK_SEQUENCE          2
    # 352 STORE_FAST               1 (installed)
    # 354 STORE_FAST               2 (details)
    # 386         356 LOAD_FAST                1 (installed)
    # 358 POP_JUMP_FORWARD_IF_FALSE    79 (to 518)
    # 387         360 LOAD_GLOBAL             10 (logger)
    # 372 LOAD_METHOD              6 (info)
    # 394 LOAD_CONST               8 ('WebView2 runtime installation completed: ')
    # 396 LOAD_FAST                2 (details)
    # 398 FORMAT_VALUE             0
    # 400 BUILD_STRING             2
    # 402 PRECALL                  1
    # 406 CALL                     1
    # 416 POP_TOP
    # 388         418 LOAD_GLOBAL             15 (NULL + _write_bootstrap_log)
    # 430 LOAD_CONST               8 ('WebView2 runtime installation completed: ')
    # 432 LOAD_FAST                2 (details)
    # 434 FORMAT_VALUE             0
    # 436 BUILD_STRING             2
    # 438 PRECALL                  1
    # 442 CALL                     1
    # 452 POP_TOP
    # 389         454 LOAD_GLOBAL             19 (NULL + _show_info_message)
    # 390         466 LOAD_CONST               9 ('TFstudio - 설치 완료')
    # 391         468 LOAD_CONST              10 ('웹 엔진 설치가 완료되어 프로그램을 자동으로 다시 시작합니다.')
    # 389         470 PRECALL                  2
    # 474 CALL                     2
    # 484 POP_TOP
    # 393         486 LOAD_GLOBAL             23 (NULL + _restart_application)
    # 498 PRECALL                  0
    # 502 CALL                     0
    # 512 POP_TOP
    # 394         514 LOAD_CONST              11 (False)
    # 516 RETURN_VALUE
    # 396     >>  518 LOAD_GLOBAL             10 (logger)
    # 530 LOAD_METHOD             12 (error)
    # 552 LOAD_CONST              12 ('WebView2 runtime installation failed: ')
    # 554 LOAD_FAST                2 (details)
    # 556 FORMAT_VALUE             0
    # 558 BUILD_STRING             2
    # 560 PRECALL                  1
    # 564 CALL                     1
    # 574 POP_TOP
    # 397         576 LOAD_GLOBAL             15 (NULL + _write_bootstrap_log)
    # 588 LOAD_CONST              12 ('WebView2 runtime installation failed: ')
    # 590 LOAD_FAST                2 (details)
    # 592 FORMAT_VALUE             0
    # 594 BUILD_STRING             2
    # 596 PRECALL                  1
    # 600 CALL                     1
    # 610 POP_TOP
    # 398         612 LOAD_GLOBAL             27 (NULL + _show_fatal_error)
    # 399         624 LOAD_CONST              13 ('TFstudio - 웹 엔진 설치 실패')
    # 400         626 LOAD_CONST              14 ('웹 엔진(WebView2) 자동 설치에 실패했습니다.\n\n사유: ')
    # 401         628 LOAD_FAST                2 (details)
    # 400         630 FORMAT_VALUE             0
    # 632 LOAD_CONST              15 ('\n\n인터넷 연결 후 프로그램을 다시 실행하면 자동으로 재시도됩니다.\n문제가 계속되면 로그를 전달해주세요:\n%LOCALAPPDATA%\\TFstudio\\logs\\')
    # 634 BUILD_STRING             3
    # 398         636 PRECALL                  2
    # 640 CALL                     2
    # 650 POP_TOP
    # 406         652 LOAD_CONST              11 (False)
    # 654 RETURN_VALUE

def get_webview_cache_path():
    """Get pywebview cache directory path

    Explicitly setting cache path prevents browser cache issues during EXE updates.
    - Windows: %LOCALAPPDATA%/TFstudio/webview_cache
    - Linux/Mac: ~/.tfstudio/webview_cache
    """
    # 408           0 RESUME                   0
    # 415           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               2 (==)
    # 32 POP_JUMP_FORWARD_IF_FALSE    84 (to 202)
    # 416          34 LOAD_GLOBAL              1 (NULL + os)
    # 46 LOAD_ATTR                2 (getenv)
    # 56 LOAD_CONST               2 ('LOCALAPPDATA')
    # 58 LOAD_GLOBAL              0 (os)
    # 70 LOAD_ATTR                3 (path)
    # 80 LOAD_METHOD              4 (expanduser)
    # 102 LOAD_CONST               3 ('~')
    # 104 PRECALL                  1
    # 108 CALL                     1
    # 118 PRECALL                  2
    # 122 CALL                     2
    # 132 STORE_FAST               0 (localappdata)
    # 417         134 LOAD_GLOBAL              0 (os)
    # 146 LOAD_ATTR                3 (path)
    # 156 LOAD_METHOD              5 (join)
    # 178 LOAD_FAST                0 (localappdata)
    # 180 LOAD_CONST               4 ('TFstudio')
    # 182 LOAD_CONST               5 ('webview_cache')
    # 184 PRECALL                  3
    # 188 CALL                     3
    # 198 STORE_FAST               1 (cache_path)
    # 200 JUMP_FORWARD            62 (to 326)
    # 419     >>  202 LOAD_GLOBAL              0 (os)
    # 214 LOAD_ATTR                3 (path)
    # 224 LOAD_METHOD              5 (join)
    # 246 LOAD_GLOBAL              0 (os)
    # 258 LOAD_ATTR                3 (path)
    # 268 LOAD_METHOD              4 (expanduser)
    # 290 LOAD_CONST               3 ('~')
    # 292 PRECALL                  1
    # 296 CALL                     1
    # 306 LOAD_CONST               6 ('.tfstudio')
    # 308 LOAD_CONST               5 ('webview_cache')
    # 310 PRECALL                  3
    # 314 CALL                     3
    # 324 STORE_FAST               1 (cache_path)
    # 421     >>  326 LOAD_GLOBAL              1 (NULL + os)
    # 338 LOAD_ATTR                6 (makedirs)
    # 348 LOAD_FAST                1 (cache_path)
    # 350 LOAD_CONST               7 (True)
    # 352 KW_NAMES                 8
    # 354 PRECALL                  2
    # 358 CALL                     2
    # 368 POP_TOP
    # 422         370 LOAD_FAST                1 (cache_path)
    # 372 RETURN_VALUE

def find_window_by_title(title):
    """ctypes를 사용하여 윈도우 타이틀로 HWND 찾기 (Windows 전용)"""
    # 424           0 RESUME                   0
    # 426           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (name)
    # 24 LOAD_CONST               1 ('nt')
    # 26 COMPARE_OP               3 (!=)
    # 32 POP_JUMP_FORWARD_IF_FALSE     2 (to 38)
    # 427          34 LOAD_CONST               2 (None)
    # 36 RETURN_VALUE
    # 429     >>   38 LOAD_CONST               3 (0)
    # 40 LOAD_CONST               2 (None)
    # 42 IMPORT_NAME              2 (ctypes)
    # 44 STORE_FAST               1 (ctypes)
    # 430          46 LOAD_FAST                1 (ctypes)
    # 48 LOAD_ATTR                3 (windll)
    # 58 LOAD_ATTR                4 (user32)
    # 68 STORE_FAST               2 (user32)
    # 431          70 LOAD_FAST                2 (user32)
    # 72 LOAD_METHOD              5 (FindWindowW)
    # 94 LOAD_CONST               2 (None)
    # 96 LOAD_FAST                0 (title)
    # 98 PRECALL                  2
    # 102 CALL                     2
    # 112 STORE_FAST               3 (hwnd)
    # 432         114 LOAD_FAST                3 (hwnd)
    # 116 POP_JUMP_FORWARD_IF_FALSE     2 (to 122)
    # 118 LOAD_FAST                3 (hwnd)
    # 120 JUMP_FORWARD             1 (to 124)
    # >>  122 LOAD_CONST               2 (None)
    # >>  124 RETURN_VALUE

def enable_dark_title_bar(hwnd):
    """Windows 타이틀 바에 다크 모드 적용 (Windows 10 1809+)

    DwmSetWindowAttribute API를 사용하여 DWMWA_USE_IMMERSIVE_DARK_MODE 속성 설정
    """
    # 434           0 RESUME                   0
    # 439           2 LOAD_FAST                0 (hwnd)
    # 4 POP_JUMP_FORWARD_IF_FALSE    16 (to 38)
    # 6 LOAD_GLOBAL              0 (os)
    # 18 LOAD_ATTR                1 (name)
    # 28 LOAD_CONST               1 ('nt')
    # 30 COMPARE_OP               3 (!=)
    # 36 POP_JUMP_FORWARD_IF_FALSE     2 (to 42)
    # 440     >>   38 LOAD_CONST               2 (False)
    # 40 RETURN_VALUE
    # 442     >>   42 NOP
    # 443          44 LOAD_CONST               3 (0)
    # 46 LOAD_CONST               4 (None)
    # 48 IMPORT_NAME              2 (ctypes)
    # 50 STORE_FAST               1 (ctypes)
    # 445          52 LOAD_FAST                1 (ctypes)
    # 54 LOAD_ATTR                3 (windll)
    # 64 LOAD_ATTR                4 (dwmapi)
    # 74 STORE_FAST               2 (dwmapi)
    # 446          76 LOAD_CONST               5 (20)
    # 78 STORE_FAST               3 (DWMWA_USE_IMMERSIVE_DARK_MODE)
    # 447          80 LOAD_FAST                1 (ctypes)
    # 82 LOAD_METHOD              5 (c_int)
    # 104 LOAD_CONST               6 (1)
    # 106 PRECALL                  1
    # 110 CALL                     1
    # 120 STORE_FAST               4 (value)
    # 449         122 LOAD_FAST                2 (dwmapi)
    # 124 LOAD_METHOD              6 (DwmSetWindowAttribute)
    # 450         146 LOAD_FAST                0 (hwnd)
    # 451         148 LOAD_FAST                3 (DWMWA_USE_IMMERSIVE_DARK_MODE)
    # 452         150 LOAD_FAST                1 (ctypes)
    # 152 LOAD_METHOD              7 (byref)
    # 174 LOAD_FAST                4 (value)
    # 176 PRECALL                  1
    # 180 CALL                     1
    # 453         190 LOAD_FAST                1 (ctypes)
    # 192 LOAD_METHOD              8 (sizeof)
    # 214 LOAD_FAST                4 (value)
    # 216 PRECALL                  1
    # 220 CALL                     1
    # 449         230 PRECALL                  4
    # 234 CALL                     4
    # 244 STORE_FAST               5 (result)
    # 455         246 LOAD_FAST                5 (result)
    # 248 LOAD_CONST               3 (0)
    # 250 COMPARE_OP               2 (==)
    # 256 RETURN_VALUE
    # >>  258 PUSH_EXC_INFO
    # 456         260 LOAD_GLOBAL             18 (Exception)
    # 272 CHECK_EXC_MATCH
    # 274 POP_JUMP_FORWARD_IF_FALSE    40 (to 356)
    # 276 STORE_FAST               6 (e)
    # 457         278 LOAD_GLOBAL             20 (logger)
    # 290 LOAD_METHOD             11 (warning)
    # 312 LOAD_CONST               7 ('Failed to enable dark title bar: ')
    # 314 LOAD_FAST                6 (e)
    # 316 FORMAT_VALUE             0
    # 318 BUILD_STRING             2
    # 320 PRECALL                  1
    # 324 CALL                     1
    # 334 POP_TOP
    # 458         336 POP_EXCEPT
    # 338 LOAD_CONST               4 (None)
    # 340 STORE_FAST               6 (e)
    # 342 DELETE_FAST              6 (e)
    # 344 LOAD_CONST               2 (False)
    # 346 RETURN_VALUE
    # >>  348 LOAD_CONST               4 (None)
    # 350 STORE_FAST               6 (e)
    # 352 DELETE_FAST              6 (e)
    # 354 RERAISE                  1
    # 456     >>  356 RERAISE                  0
    # >>  358 COPY                     3
    # 360 POP_EXCEPT
    # 362 RERAISE                  1
    # ExceptionTable:
    # 44 to 254 -> 258 [0]
    # 258 to 276 -> 358 [1] lasti
    # 278 to 334 -> 348 [1] lasti
    # 348 to 356 -> 358 [1] lasti

def find_free_port(start_port, max_attempts):
    """Find an available port"""
    # 460           0 RESUME                   0
    # 462           2 LOAD_GLOBAL              1 (NULL + range)
    # 14 LOAD_FAST                0 (start_port)
    # 16 LOAD_FAST                0 (start_port)
    # 18 LOAD_FAST                1 (max_attempts)
    # 20 BINARY_OP                0 (+)
    # 24 PRECALL                  2
    # 28 CALL                     2
    # 38 GET_ITER
    # >>   40 FOR_ITER               106 (to 254)
    # 42 STORE_FAST               2 (port)
    # 463          44 NOP
    # 464          46 LOAD_GLOBAL              3 (NULL + socket)
    # 58 LOAD_ATTR                1 (socket)
    # 68 LOAD_GLOBAL              2 (socket)
    # 80 LOAD_ATTR                2 (AF_INET)
    # 90 LOAD_GLOBAL              2 (socket)
    # 102 LOAD_ATTR                3 (SOCK_STREAM)
    # 112 PRECALL                  2
    # 116 CALL                     2
    # 126 STORE_FAST               3 (sock)
    # 465         128 LOAD_FAST                3 (sock)
    # 130 LOAD_METHOD              4 (bind)
    # 152 LOAD_CONST               1 ('127.0.0.1')
    # 154 LOAD_FAST                2 (port)
    # 156 BUILD_TUPLE              2
    # 158 PRECALL                  1
    # 162 CALL                     1
    # 172 POP_TOP
    # 466         174 LOAD_FAST                3 (sock)
    # 176 LOAD_METHOD              5 (close)
    # 198 PRECALL                  0
    # 202 CALL                     0
    # 212 POP_TOP
    # 467         214 LOAD_FAST                2 (port)
    # 216 SWAP                     2
    # 218 POP_TOP
    # 220 RETURN_VALUE
    # >>  222 PUSH_EXC_INFO
    # 468         224 LOAD_GLOBAL             12 (OSError)
    # 236 CHECK_EXC_MATCH
    # 238 POP_JUMP_FORWARD_IF_FALSE     3 (to 246)
    # 240 POP_TOP
    # 469         242 POP_EXCEPT
    # 244 JUMP_BACKWARD          103 (to 40)
    # 468     >>  246 RERAISE                  0
    # >>  248 COPY                     3
    # 250 POP_EXCEPT
    # 252 RERAISE                  1
    # 470     >>  254 LOAD_GLOBAL             15 (NULL + RuntimeError)
    # 266 LOAD_CONST               2 ('Could not find free port in range ')
    # 268 LOAD_FAST                0 (start_port)
    # 270 FORMAT_VALUE             0
    # 272 LOAD_CONST               3 ('-')
    # 274 LOAD_FAST                0 (start_port)
    # 276 LOAD_FAST                1 (max_attempts)
    # 278 BINARY_OP                0 (+)
    # 282 FORMAT_VALUE             0
    # 284 BUILD_STRING             4
    # 286 PRECALL                  1
    # 290 CALL                     1
    # 300 RAISE_VARARGS            1
    # ExceptionTable:
    # 46 to 214 -> 222 [1]
    # 222 to 240 -> 248 [2] lasti
    # 246 to 246 -> 248 [2] lasti

def setup_environment():
    """Setup environment variables and paths"""
    # 472           0 RESUME                   0
    # 474           2 LOAD_GLOBAL              1 (NULL + get_base_path)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               0 (base_path)
    # 477          30 LOAD_GLOBAL              2 (IS_FROZEN)
    # 42 POP_JUMP_FORWARD_IF_FALSE     3 (to 50)
    # 478          44 LOAD_FAST                0 (base_path)
    # 46 STORE_FAST               1 (backend_path)
    # 48 JUMP_FORWARD            32 (to 114)
    # 480     >>   50 LOAD_GLOBAL              4 (os)
    # 62 LOAD_ATTR                3 (path)
    # 72 LOAD_METHOD              4 (join)
    # 94 LOAD_FAST                0 (base_path)
    # 96 LOAD_CONST               1 ('backend')
    # 98 PRECALL                  2
    # 102 CALL                     2
    # 112 STORE_FAST               1 (backend_path)
    # 482     >>  114 LOAD_FAST                1 (backend_path)
    # 116 LOAD_GLOBAL             10 (sys)
    # 128 LOAD_ATTR                3 (path)
    # 138 CONTAINS_OP              1
    # 140 POP_JUMP_FORWARD_IF_FALSE    32 (to 206)
    # 483         142 LOAD_GLOBAL             10 (sys)
    # 154 LOAD_ATTR                3 (path)
    # 164 LOAD_METHOD              6 (insert)
    # 186 LOAD_CONST               2 (0)
    # 188 LOAD_FAST                1 (backend_path)
    # 190 PRECALL                  2
    # 194 CALL                     2
    # 204 POP_TOP
    # 486     >>  206 LOAD_GLOBAL              5 (NULL + os)
    # 218 LOAD_ATTR                7 (chdir)
    # 228 LOAD_FAST                1 (backend_path)
    # 230 PRECALL                  1
    # 234 CALL                     1
    # 244 POP_TOP
    # 489         246 LOAD_CONST               2 (0)
    # 248 LOAD_CONST               3 (('get_data_path',))
    # 250 IMPORT_NAME              8 (app.config.paths)
    # 252 IMPORT_FROM              9 (get_data_path)
    # 254 STORE_FAST               2 (get_data_path)
    # 256 POP_TOP
    # 490         258 LOAD_CONST               2 (0)
    # 260 LOAD_CONST               4 (('apply_pending_data_path',))
    # 262 IMPORT_NAME             10 (app.config.runtime_config)
    # 264 IMPORT_FROM             11 (apply_pending_data_path)
    # 266 STORE_FAST               3 (apply_pending_data_path)
    # 268 POP_TOP
    # 491         270 LOAD_CONST               2 (0)
    # 272 LOAD_CONST               5 (('ensure_runtime_requirements', 'log_runtime_diagnostics'))
    # 274 IMPORT_NAME             12 (app.services.runtime_diagnostics_service)
    # 276 IMPORT_FROM             13 (ensure_runtime_requirements)
    # 278 STORE_FAST               4 (ensure_runtime_requirements)
    # 280 IMPORT_FROM             14 (log_runtime_diagnostics)
    # 282 STORE_FAST               5 (log_runtime_diagnostics)
    # 284 POP_TOP
    # 494         286 PUSH_NULL
    # 288 LOAD_FAST                3 (apply_pending_data_path)
    # 290 PRECALL                  0
    # 294 CALL                     0
    # 304 POP_JUMP_FORWARD_IF_FALSE    26 (to 358)
    # 495         306 LOAD_GLOBAL             30 (logger)
    # 318 LOAD_METHOD             16 (info)
    # 340 LOAD_CONST               6 ('Applied pending data path change')
    # 342 PRECALL                  1
    # 346 CALL                     1
    # 356 POP_TOP
    # 498     >>  358 PUSH_NULL
    # 360 LOAD_FAST                2 (get_data_path)
    # 362 PRECALL                  0
    # 366 CALL                     0
    # 376 STORE_FAST               6 (data_path)
    # 499         378 PUSH_NULL
    # 380 LOAD_FAST                5 (log_runtime_diagnostics)
    # 382 PRECALL                  0
    # 386 CALL                     0
    # 396 STORE_FAST               7 (diagnostics)
    # 500         398 PUSH_NULL
    # 400 LOAD_FAST                4 (ensure_runtime_requirements)
    # 402 LOAD_FAST                7 (diagnostics)
    # 404 PRECALL                  1
    # 408 CALL                     1
    # 418 POP_TOP
    # 502         420 LOAD_GLOBAL             30 (logger)
    # 432 LOAD_METHOD             16 (info)
    # 454 LOAD_CONST               7 ('Base path: ')
    # 456 LOAD_FAST                0 (base_path)
    # 458 FORMAT_VALUE             0
    # 460 BUILD_STRING             2
    # 462 PRECALL                  1
    # 466 CALL                     1
    # 476 POP_TOP
    # 503         478 LOAD_GLOBAL             30 (logger)
    # 490 LOAD_METHOD             16 (info)
    # 512 LOAD_CONST               8 ('Backend path: ')
    # 514 LOAD_FAST                1 (backend_path)
    # 516 FORMAT_VALUE             0
    # 518 BUILD_STRING             2
    # 520 PRECALL                  1
    # 524 CALL                     1
    # 534 POP_TOP
    # 504         536 LOAD_GLOBAL             30 (logger)
    # 548 LOAD_METHOD             16 (info)
    # 570 LOAD_CONST               9 ('Data path: ')
    # 572 LOAD_FAST                6 (data_path)
    # 574 FORMAT_VALUE             0
    # 576 BUILD_STRING             2
    # 578 PRECALL                  1
    # 582 CALL                     1
    # 592 POP_TOP
    # 594 LOAD_CONST              10 (None)
    # 596 RETURN_VALUE

class FlaskServer:
    """FlaskServer"""
    def __init__(self, port):
        # 509           0 RESUME                   0
        # 510           2 LOAD_FAST                1 (port)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (port)
        # 511          16 LOAD_CONST               0 (None)
        # 18 LOAD_FAST                0 (self)
        # 20 STORE_ATTR               1 (app)
        # 512          30 LOAD_CONST               0 (None)
        # 32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               2 (server_thread)
        # 513          44 LOAD_CONST               1 (False)
        # 46 LOAD_FAST                0 (self)
        # 48 STORE_ATTR               3 (is_running)
        # 514          58 LOAD_CONST               0 (None)
        # 60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               4 (_server_error)
        # 72 LOAD_CONST               0 (None)
        # 74 RETURN_VALUE

    def start(self):
        """Start the Flask server in a background thread"""
        # 516           0 RESUME                   0
        # 518           2 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
        # 14 LOAD_CONST               1 ('importing app module')
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 POP_TOP
        # 519          32 LOAD_CONST               2 (0)
        # 34 LOAD_CONST               3 (('create_app',))
        # 36 IMPORT_NAME              1 (app)
        # 38 IMPORT_FROM              2 (create_app)
        # 40 STORE_FAST               1 (create_app)
        # 42 POP_TOP
        # 520          44 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
        # 56 LOAD_CONST               4 ('importing werkzeug')
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 POP_TOP
        # 521          74 LOAD_CONST               2 (0)
        # 76 LOAD_CONST               5 (('make_server', 'WSGIRequestHandler'))
        # 78 IMPORT_NAME              3 (werkzeug.serving)
        # 80 IMPORT_FROM              4 (make_server)
        # 82 STORE_FAST               2 (make_server)
        # 84 IMPORT_FROM              5 (WSGIRequestHandler)
        # 86 STORE_FAST               3 (WSGIRequestHandler)
        # 88 POP_TOP
        # 523          90 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
        # 102 LOAD_CONST               6 ('calling create_app()')
        # 104 PRECALL                  1
        # 108 CALL                     1
        # 118 POP_TOP
        # 524         120 PUSH_NULL
        # 122 LOAD_FAST                1 (create_app)
        # 124 PRECALL                  0
        # 128 CALL                     0
        # 138 LOAD_FAST                0 (self)
        # 140 STORE_ATTR               1 (app)
        # 525         150 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
        # 162 LOAD_CONST               7 ('create_app() completed')
        # 164 PRECALL                  1
        # 168 CALL                     1
        # 178 POP_TOP
        # 528         180 PUSH_NULL
        # 182 LOAD_BUILD_CLASS
        # 184 LOAD_CONST               8 (<code object LongRunningRequestHandler at 0x000001EBD786DBD0, file "main.py", line 528>)
        # 186 MAKE_FUNCTION            0
        # 188 LOAD_CONST               9 ('LongRunningRequestHandler')
        # 190 LOAD_FAST                3 (WSGIRequestHandler)
        # 192 PRECALL                  3
        # 196 CALL                     3
        # 206 STORE_FAST               4 (LongRunningRequestHandler)
        # 537         208 PUSH_NULL
        # 210 LOAD_FAST                2 (make_server)
        # 538         212 LOAD_CONST              10 ('127.0.0.1')
        # 214 LOAD_FAST                0 (self)
        # 216 LOAD_ATTR                6 (port)
        # 226 LOAD_FAST                0 (self)
        # 228 LOAD_ATTR                1 (app)
        # 539         238 LOAD_CONST              11 (True)
        # 540         240 LOAD_FAST                4 (LongRunningRequestHandler)
        # 537         242 KW_NAMES                12
        # 244 PRECALL                  5
        # 248 CALL                     5
        # 258 LOAD_FAST                0 (self)
        # 260 STORE_ATTR               7 (server)
        # 542         270 LOAD_GLOBAL             16 (logger)
        # 282 LOAD_METHOD              9 (info)
        # 304 LOAD_CONST              13 ('Request timeout set to 14400 seconds (4 hours) for long video generation')
        # 306 PRECALL                  1
        # 310 CALL                     1
        # 320 POP_TOP
        # 545         322 LOAD_GLOBAL             21 (NULL + threading)
        # 334 LOAD_ATTR               11 (Thread)
        # 344 LOAD_FAST                0 (self)
        # 346 LOAD_ATTR               12 (_run_server)
        # 356 LOAD_CONST              11 (True)
        # 358 KW_NAMES                14
        # 360 PRECALL                  2
        # 364 CALL                     2
        # 374 LOAD_FAST                0 (self)
        # 376 STORE_ATTR              13 (server_thread)
        # 546         386 LOAD_FAST                0 (self)
        # 388 LOAD_ATTR               13 (server_thread)
        # 398 LOAD_METHOD             14 (start)
        # 420 PRECALL                  0
        # 424 CALL                     0
        # 434 POP_TOP
        # 549         436 LOAD_FAST                0 (self)
        # 438 LOAD_METHOD             15 (_wait_for_server)
        # 460 PRECALL                  0
        # 464 CALL                     0
        # 474 POP_TOP
        # 551         476 LOAD_CONST              11 (True)
        # 478 LOAD_FAST                0 (self)
        # 480 STORE_ATTR              16 (is_running)
        # 552         490 LOAD_GLOBAL             16 (logger)
        # 502 LOAD_METHOD              9 (info)
        # 524 LOAD_CONST              15 ('Flask server started on port ')
        # 526 LOAD_FAST                0 (self)
        # 528 LOAD_ATTR                6 (port)
        # 538 FORMAT_VALUE             0
        # 540 BUILD_STRING             2
        # 542 PRECALL                  1
        # 546 CALL                     1
        # 556 POP_TOP
        # 558 LOAD_CONST              16 (None)
        # 560 RETURN_VALUE
        # Disassembly of <code object LongRunningRequestHandler at 0x000001EBD786DBD0, file "main.py", line 528>:
        # 528           0 RESUME                   0
        # 2 LOAD_NAME                0 (__name__)
        # 4 STORE_NAME               1 (__module__)
        # 6 LOAD_CONST               0 ('FlaskServer.start.<locals>.LongRunningRequestHandler')
        # 8 STORE_NAME               2 (__qualname__)
        # 529          10 LOAD_CONST               1 ('프로덕션 서버의 요청 타임아웃을 4시간으로 설정\n\n            2시간 이상 걸리는 TTS 생성 및 영상 렌더링 작업을 위해\n            충분한 타임아웃 값을 설정합니다.\n            ')
        # 12 STORE_NAME               3 (__doc__)
        # 534          14 LOAD_CONST               2 (14400)
        # 16 STORE_NAME               4 (timeout)
        # 18 LOAD_CONST               3 (None)
        # 20 RETURN_VALUE

    def _run_server(self):
        """Run the server (called in background thread)"""
        # 554           0 RESUME                   0
        # 556           2 NOP
        # 557           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (server)
        # 16 LOAD_METHOD              1 (serve_forever)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 POP_TOP
        # 54 LOAD_CONST               2 (None)
        # 56 RETURN_VALUE
        # >>   58 PUSH_EXC_INFO
        # 558          60 LOAD_GLOBAL              4 (Exception)
        # 72 CHECK_EXC_MATCH
        # 74 POP_JUMP_FORWARD_IF_FALSE    47 (to 170)
        # 76 STORE_FAST               1 (e)
        # 559          78 LOAD_FAST                1 (e)
        # 80 LOAD_FAST                0 (self)
        # 82 STORE_ATTR               3 (_server_error)
        # 560          92 LOAD_GLOBAL              8 (logger)
        # 104 LOAD_METHOD              5 (error)
        # 126 LOAD_CONST               1 ('Server error: ')
        # 128 LOAD_FAST                1 (e)
        # 130 FORMAT_VALUE             0
        # 132 BUILD_STRING             2
        # 134 PRECALL                  1
        # 138 CALL                     1
        # 148 POP_TOP
        # 150 POP_EXCEPT
        # 152 LOAD_CONST               2 (None)
        # 154 STORE_FAST               1 (e)
        # 156 DELETE_FAST              1 (e)
        # 158 LOAD_CONST               2 (None)
        # 160 RETURN_VALUE
        # >>  162 LOAD_CONST               2 (None)
        # 164 STORE_FAST               1 (e)
        # 166 DELETE_FAST              1 (e)
        # 168 RERAISE                  1
        # 558     >>  170 RERAISE                  0
        # >>  172 COPY                     3
        # 174 POP_EXCEPT
        # 176 RERAISE                  1
        # ExceptionTable:
        # 4 to 52 -> 58 [0]
        # 58 to 76 -> 172 [1] lasti
        # 78 to 148 -> 162 [1] lasti
        # 162 to 170 -> 172 [1] lasti

    def _wait_for_server(self, timeout):
        """Wait for the server to be ready"""
        # 562           0 RESUME                   0
        # 564           2 LOAD_GLOBAL              1 (NULL + time)
        # 14 LOAD_ATTR                0 (time)
        # 24 PRECALL                  0
        # 28 CALL                     0
        # 38 STORE_FAST               2 (start_time)
        # 565          40 LOAD_CONST               1 (None)
        # 42 STORE_FAST               3 (last_errno)
        # 566          44 LOAD_GLOBAL              1 (NULL + time)
        # 56 LOAD_ATTR                0 (time)
        # 66 PRECALL                  0
        # 70 CALL                     0
        # 80 LOAD_FAST                2 (start_time)
        # 82 BINARY_OP               10 (-)
        # 86 LOAD_FAST                1 (timeout)
        # 88 COMPARE_OP               0 (<)
        # 94 POP_JUMP_FORWARD_IF_FALSE   207 (to 510)
        # 567     >>   96 LOAD_FAST                0 (self)
        # 98 LOAD_ATTR                1 (_server_error)
        # 108 POP_JUMP_FORWARD_IF_FALSE    23 (to 156)
        # 568         110 LOAD_GLOBAL              5 (NULL + RuntimeError)
        # 122 LOAD_CONST               2 ('Server thread error: ')
        # 124 LOAD_FAST                0 (self)
        # 126 LOAD_ATTR                1 (_server_error)
        # 136 FORMAT_VALUE             0
        # 138 BUILD_STRING             2
        # 140 PRECALL                  1
        # 144 CALL                     1
        # 154 RAISE_VARARGS            1
        # 569     >>  156 NOP
        # 570         158 LOAD_GLOBAL              7 (NULL + socket)
        # 170 LOAD_ATTR                3 (socket)
        # 180 LOAD_GLOBAL              6 (socket)
        # 192 LOAD_ATTR                4 (AF_INET)
        # 202 LOAD_GLOBAL              6 (socket)
        # 214 LOAD_ATTR                5 (SOCK_STREAM)
        # 224 PRECALL                  2
        # 228 CALL                     2
        # 238 STORE_FAST               4 (sock)
        # 571         240 LOAD_FAST                4 (sock)
        # 242 LOAD_METHOD              6 (connect_ex)
        # 264 LOAD_CONST               3 ('127.0.0.1')
        # 266 LOAD_FAST                0 (self)
        # 268 LOAD_ATTR                7 (port)
        # 278 BUILD_TUPLE              2
        # 280 PRECALL                  1
        # 284 CALL                     1
        # 294 STORE_FAST               5 (result)
        # 572         296 LOAD_FAST                4 (sock)
        # 298 LOAD_METHOD              8 (close)
        # 320 PRECALL                  0
        # 324 CALL                     0
        # 334 POP_TOP
        # 573         336 LOAD_FAST                5 (result)
        # 338 LOAD_CONST               4 (0)
        # 340 COMPARE_OP               2 (==)
        # 346 POP_JUMP_FORWARD_IF_FALSE     2 (to 352)
        # 574         348 LOAD_CONST               5 (True)
        # 350 RETURN_VALUE
        # 575     >>  352 LOAD_FAST                5 (result)
        # 354 STORE_FAST               3 (last_errno)
        # 356 JUMP_FORWARD            30 (to 418)
        # >>  358 PUSH_EXC_INFO
        # 576         360 LOAD_GLOBAL             18 (OSError)
        # 372 CHECK_EXC_MATCH
        # 374 POP_JUMP_FORWARD_IF_FALSE    17 (to 410)
        # 376 STORE_FAST               6 (e)
        # 577         378 LOAD_FAST                6 (e)
        # 380 LOAD_ATTR               10 (errno)
        # 390 STORE_FAST               3 (last_errno)
        # 392 POP_EXCEPT
        # 394 LOAD_CONST               1 (None)
        # 396 STORE_FAST               6 (e)
        # 398 DELETE_FAST              6 (e)
        # 400 JUMP_FORWARD             8 (to 418)
        # >>  402 LOAD_CONST               1 (None)
        # 404 STORE_FAST               6 (e)
        # 406 DELETE_FAST              6 (e)
        # 408 RERAISE                  1
        # 576     >>  410 RERAISE                  0
        # >>  412 COPY                     3
        # 414 POP_EXCEPT
        # 416 RERAISE                  1
        # 578     >>  418 LOAD_GLOBAL              1 (NULL + time)
        # 430 LOAD_ATTR               11 (sleep)
        # 440 LOAD_CONST               6 (0.1)
        # 442 PRECALL                  1
        # 446 CALL                     1
        # 456 POP_TOP
        # 566         458 LOAD_GLOBAL              1 (NULL + time)
        # 470 LOAD_ATTR                0 (time)
        # 480 PRECALL                  0
        # 484 CALL                     0
        # 494 LOAD_FAST                2 (start_time)
        # 496 BINARY_OP               10 (-)
        # 500 LOAD_FAST                1 (timeout)
        # 502 COMPARE_OP               0 (<)
        # 508 POP_JUMP_BACKWARD_IF_TRUE   207 (to 96)
        # 579     >>  510 LOAD_FAST                0 (self)
        # 512 LOAD_ATTR               12 (server_thread)
        # 522 POP_JUMP_FORWARD_IF_FALSE    25 (to 574)
        # 524 LOAD_FAST                0 (self)
        # 526 LOAD_ATTR               12 (server_thread)
        # 536 LOAD_METHOD             13 (is_alive)
        # 558 PRECALL                  0
        # 562 CALL                     0
        # 572 JUMP_FORWARD             1 (to 576)
        # >>  574 LOAD_CONST               7 (False)
        # >>  576 STORE_FAST               7 (thread_alive)
        # 580         578 LOAD_CONST               8 ('port=')
        # 580 LOAD_FAST                0 (self)
        # 582 LOAD_ATTR                7 (port)
        # 592 FORMAT_VALUE             0
        # 594 LOAD_CONST               9 (', thread_alive=')
        # 596 LOAD_FAST                7 (thread_alive)
        # 598 FORMAT_VALUE             0
        # 600 LOAD_CONST              10 (', last_errno=')
        # 581         602 LOAD_FAST                3 (last_errno)
        # 580         604 FORMAT_VALUE             0
        # 606 LOAD_CONST              11 (', server_error=')
        # 581         608 LOAD_FAST                0 (self)
        # 610 LOAD_ATTR                1 (_server_error)
        # 580         620 FORMAT_VALUE             0
        # 622 BUILD_STRING             8
        # 624 STORE_FAST               8 (diag)
        # 582         626 LOAD_GLOBAL             29 (NULL + _write_bootstrap_log)
        # 638 LOAD_CONST              12 ('_wait_for_server timeout: ')
        # 640 LOAD_FAST                8 (diag)
        # 642 FORMAT_VALUE             0
        # 644 BUILD_STRING             2
        # 646 PRECALL                  1
        # 650 CALL                     1
        # 660 POP_TOP
        # 583         662 LOAD_GLOBAL              5 (NULL + RuntimeError)
        # 674 LOAD_CONST              13 ('Server failed to start: ')
        # 676 LOAD_FAST                8 (diag)
        # 678 FORMAT_VALUE             0
        # 680 BUILD_STRING             2
        # 682 PRECALL                  1
        # 686 CALL                     1
        # 696 RAISE_VARARGS            1
        # ExceptionTable:
        # 158 to 346 -> 358 [0]
        # 352 to 354 -> 358 [0]
        # 358 to 376 -> 412 [1] lasti
        # 378 to 390 -> 402 [1] lasti
        # 402 to 410 -> 412 [1] lasti

    def stop(self):
        """Stop the Flask server"""
        # 585           0 RESUME                   0
        # 587           2 LOAD_GLOBAL              1 (NULL + hasattr)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_CONST               1 ('server')
        # 18 PRECALL                  2
        # 22 CALL                     2
        # 32 POP_JUMP_FORWARD_IF_FALSE    25 (to 84)
        # 588          34 LOAD_FAST                0 (self)
        # 36 LOAD_ATTR                1 (server)
        # 46 LOAD_METHOD              2 (shutdown)
        # 68 PRECALL                  0
        # 72 CALL                     0
        # 82 POP_TOP
        # 589     >>   84 LOAD_CONST               2 (False)
        # 86 LOAD_FAST                0 (self)
        # 88 STORE_ATTR               3 (is_running)
        # 590          98 LOAD_GLOBAL              8 (logger)
        # 110 LOAD_METHOD              5 (info)
        # 132 LOAD_CONST               3 ('Flask server stopped')
        # 134 PRECALL                  1
        # 138 CALL                     1
        # 148 POP_TOP
        # 150 LOAD_CONST               4 (None)
        # 152 RETURN_VALUE


def cleanup():
    """Cleanup function called on exit"""
    # 592           0 RESUME                   0
    # 594           2 LOAD_GLOBAL              0 (logger)
    # 14 LOAD_METHOD              1 (info)
    # 36 LOAD_CONST               1 ('Cleaning up...')
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 POP_TOP
    # 597          54 NOP
    # 598          56 LOAD_GLOBAL              4 (_flask_server)
    # 68 POP_JUMP_FORWARD_IF_FALSE   185 (to 440)
    # 70 LOAD_GLOBAL              7 (NULL + hasattr)
    # 82 LOAD_GLOBAL              4 (_flask_server)
    # 94 LOAD_CONST               2 ('app')
    # 96 PRECALL                  2
    # 100 CALL                     2
    # 110 POP_JUMP_FORWARD_IF_FALSE   164 (to 440)
    # 112 LOAD_GLOBAL              4 (_flask_server)
    # 124 LOAD_ATTR                4 (app)
    # 134 POP_JUMP_FORWARD_IF_FALSE   152 (to 440)
    # 599         136 LOAD_CONST               3 (0)
    # 138 LOAD_CONST               4 (('LicenseService',))
    # 140 IMPORT_NAME              5 (app.services.license_service)
    # 142 IMPORT_FROM              6 (LicenseService)
    # 144 STORE_FAST               0 (LicenseService)
    # 146 POP_TOP
    # 600         148 LOAD_CONST               3 (0)
    # 150 LOAD_CONST               5 (('License',))
    # 152 IMPORT_NAME              7 (app.models.license)
    # 154 IMPORT_FROM              8 (License)
    # 156 STORE_FAST               1 (License)
    # 158 POP_TOP
    # 601         160 LOAD_GLOBAL              4 (_flask_server)
    # 172 LOAD_ATTR                4 (app)
    # 182 LOAD_METHOD              9 (app_context)
    # 204 PRECALL                  0
    # 208 CALL                     0
    # 218 BEFORE_WITH
    # 220 POP_TOP
    # 602         222 LOAD_FAST                1 (License)
    # 224 LOAD_ATTR               10 (query)
    # 234 LOAD_METHOD             11 (first)
    # 256 PRECALL                  0
    # 260 CALL                     0
    # 270 STORE_FAST               2 (license_obj)
    # 603         272 LOAD_FAST                2 (license_obj)
    # 274 POP_JUMP_FORWARD_IF_FALSE    59 (to 394)
    # 276 LOAD_FAST                2 (license_obj)
    # 278 LOAD_ATTR               12 (session_token)
    # 288 POP_JUMP_FORWARD_IF_FALSE    52 (to 394)
    # 604         290 LOAD_FAST                0 (LicenseService)
    # 292 LOAD_METHOD             13 (logout_session)
    # 314 LOAD_FAST                2 (license_obj)
    # 316 LOAD_ATTR               12 (session_token)
    # 326 PRECALL                  1
    # 330 CALL                     1
    # 340 POP_TOP
    # 605         342 LOAD_GLOBAL              0 (logger)
    # 354 LOAD_METHOD              1 (info)
    # 376 LOAD_CONST               6 ('Session logged out on cleanup')
    # 378 PRECALL                  1
    # 382 CALL                     1
    # 392 POP_TOP
    # 601     >>  394 LOAD_CONST               7 (None)
    # 396 LOAD_CONST               7 (None)
    # 398 LOAD_CONST               7 (None)
    # 400 PRECALL                  2
    # 404 CALL                     2
    # 414 POP_TOP
    # 416 JUMP_FORWARD            11 (to 440)
    # >>  418 PUSH_EXC_INFO
    # 420 WITH_EXCEPT_START
    # 422 POP_JUMP_FORWARD_IF_TRUE     4 (to 432)
    # 424 RERAISE                  2
    # >>  426 COPY                     3
    # 428 POP_EXCEPT
    # 430 RERAISE                  1
    # >>  432 POP_TOP
    # 434 POP_EXCEPT
    # 436 POP_TOP
    # 438 POP_TOP
    # >>  440 JUMP_FORWARD            52 (to 546)
    # >>  442 PUSH_EXC_INFO
    # 606         444 LOAD_GLOBAL             28 (Exception)
    # 456 CHECK_EXC_MATCH
    # 458 POP_JUMP_FORWARD_IF_FALSE    39 (to 538)
    # 460 STORE_FAST               3 (e)
    # 607         462 LOAD_GLOBAL              0 (logger)
    # 474 LOAD_METHOD             15 (warning)
    # 496 LOAD_CONST               8 ('Session logout on cleanup failed: ')
    # 498 LOAD_FAST                3 (e)
    # 500 FORMAT_VALUE             0
    # 502 BUILD_STRING             2
    # 504 PRECALL                  1
    # 508 CALL                     1
    # 518 POP_TOP
    # 520 POP_EXCEPT
    # 522 LOAD_CONST               7 (None)
    # 524 STORE_FAST               3 (e)
    # 526 DELETE_FAST              3 (e)
    # 528 JUMP_FORWARD             8 (to 546)
    # >>  530 LOAD_CONST               7 (None)
    # 532 STORE_FAST               3 (e)
    # 534 DELETE_FAST              3 (e)
    # 536 RERAISE                  1
    # 606     >>  538 RERAISE                  0
    # >>  540 COPY                     3
    # 542 POP_EXCEPT
    # 544 RERAISE                  1
    # 610     >>  546 NOP
    # 611         548 LOAD_CONST               3 (0)
    # 550 LOAD_CONST               7 (None)
    # 552 IMPORT_NAME             16 (psutil)
    # 554 STORE_FAST               4 (psutil)
    # 612         556 LOAD_FAST                4 (psutil)
    # 558 LOAD_METHOD             17 (Process)
    # 580 PRECALL                  0
    # 584 CALL                     0
    # 594 STORE_FAST               5 (current_process)
    # 613         596 LOAD_FAST                5 (current_process)
    # 598 LOAD_METHOD             18 (children)
    # 620 LOAD_CONST               9 (True)
    # 622 KW_NAMES                10
    # 624 PRECALL                  1
    # 628 CALL                     1
    # 638 STORE_FAST               6 (children)
    # 614         640 LOAD_FAST                6 (children)
    # 642 GET_ITER
    # >>  644 FOR_ITER               110 (to 866)
    # 646 STORE_FAST               7 (child)
    # 615         648 NOP
    # 616         650 LOAD_CONST              11 ('ffmpeg')
    # 652 LOAD_FAST                7 (child)
    # 654 LOAD_METHOD             19 (name)
    # 676 PRECALL                  0
    # 680 CALL                     0
    # 690 LOAD_METHOD             20 (lower)
    # 712 PRECALL                  0
    # 716 CALL                     0
    # 726 CONTAINS_OP              0
    # 728 POP_JUMP_FORWARD_IF_TRUE    40 (to 810)
    # 730 LOAD_CONST              12 ('ffprobe')
    # 732 LOAD_FAST                7 (child)
    # 734 LOAD_METHOD             19 (name)
    # 756 PRECALL                  0
    # 760 CALL                     0
    # 770 LOAD_METHOD             20 (lower)
    # 792 PRECALL                  0
    # 796 CALL                     0
    # 806 CONTAINS_OP              0
    # 808 POP_JUMP_FORWARD_IF_FALSE    20 (to 850)
    # 617     >>  810 LOAD_FAST                7 (child)
    # 812 LOAD_METHOD             21 (kill)
    # 834 PRECALL                  0
    # 838 CALL                     0
    # 848 POP_TOP
    # >>  850 JUMP_BACKWARD          104 (to 644)
    # >>  852 PUSH_EXC_INFO
    # 618         854 POP_TOP
    # 619         856 POP_EXCEPT
    # 858 JUMP_BACKWARD          108 (to 644)
    # >>  860 COPY                     3
    # 862 POP_EXCEPT
    # 864 RERAISE                  1
    # 614     >>  866 LOAD_CONST               7 (None)
    # 868 RETURN_VALUE
    # >>  870 PUSH_EXC_INFO
    # 620         872 POP_TOP
    # 621         874 POP_EXCEPT
    # 876 LOAD_CONST               7 (None)
    # 878 RETURN_VALUE
    # >>  880 COPY                     3
    # 882 POP_EXCEPT
    # 884 RERAISE                  1
    # ExceptionTable:
    # 56 to 218 -> 442 [0]
    # 220 to 392 -> 418 [1] lasti
    # 394 to 416 -> 442 [0]
    # 418 to 424 -> 426 [3] lasti
    # 426 to 430 -> 442 [0]
    # 432 to 432 -> 426 [3] lasti
    # 434 to 438 -> 442 [0]
    # 442 to 460 -> 540 [1] lasti
    # 462 to 518 -> 530 [1] lasti
    # 530 to 538 -> 540 [1] lasti
    # 548 to 646 -> 870 [0]
    # 650 to 848 -> 852 [1]
    # 850 to 850 -> 870 [0]
    # 852 to 854 -> 860 [2] lasti
    # 856 to 864 -> 870 [0]
    # 870 to 872 -> 880 [1] lasti

class Api:
    """Api"""
    def __init__(self, window):
        # 627           0 RESUME                   0
        # 628           2 LOAD_FAST                1 (window)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (_window)
        # 16 LOAD_CONST               0 (None)
        # 18 RETURN_VALUE

    def reload(self):
        """Reload the current page (F5 새로고침)"""
        # 630           0 RESUME                   0
        # 632           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_window)
        # 14 POP_JUMP_FORWARD_IF_FALSE   108 (to 232)
        # 633          16 NOP
        # 635          18 LOAD_FAST                0 (self)
        # 20 LOAD_ATTR                0 (_window)
        # 30 LOAD_METHOD              1 (evaluate_js)
        # 52 LOAD_CONST               1 ('window.location.reload()')
        # 54 PRECALL                  1
        # 58 CALL                     1
        # 68 POP_TOP
        # 636          70 LOAD_GLOBAL              4 (logger)
        # 82 LOAD_METHOD              3 (info)
        # 104 LOAD_CONST               2 ('Page reloaded via F5')
        # 106 PRECALL                  1
        # 110 CALL                     1
        # 120 POP_TOP
        # 122 LOAD_CONST               4 (None)
        # 124 RETURN_VALUE
        # >>  126 PUSH_EXC_INFO
        # 637         128 LOAD_GLOBAL              8 (Exception)
        # 140 CHECK_EXC_MATCH
        # 142 POP_JUMP_FORWARD_IF_FALSE    40 (to 224)
        # 144 STORE_FAST               1 (e)
        # 638         146 LOAD_GLOBAL              4 (logger)
        # 158 LOAD_METHOD              5 (error)
        # 180 LOAD_CONST               3 ('Failed to reload: ')
        # 182 LOAD_FAST                1 (e)
        # 184 FORMAT_VALUE             0
        # 186 BUILD_STRING             2
        # 188 PRECALL                  1
        # 192 CALL                     1
        # 202 POP_TOP
        # 204 POP_EXCEPT
        # 206 LOAD_CONST               4 (None)
        # 208 STORE_FAST               1 (e)
        # 210 DELETE_FAST              1 (e)
        # 212 LOAD_CONST               4 (None)
        # 214 RETURN_VALUE
        # >>  216 LOAD_CONST               4 (None)
        # 218 STORE_FAST               1 (e)
        # 220 DELETE_FAST              1 (e)
        # 222 RERAISE                  1
        # 637     >>  224 RERAISE                  0
        # >>  226 COPY                     3
        # 228 POP_EXCEPT
        # 230 RERAISE                  1
        # 632     >>  232 LOAD_CONST               4 (None)
        # 234 RETURN_VALUE
        # ExceptionTable:
        # 18 to 120 -> 126 [0]
        # 126 to 144 -> 226 [1] lasti
        # 146 to 202 -> 216 [1] lasti
        # 216 to 224 -> 226 [1] lasti

    def open_devtools(self):
        """Open developer tools (F12) - only works in debug mode with EdgeChromium"""
        # 640           0 RESUME                   0
        # 642           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (_window)
        # 14 POP_JUMP_FORWARD_IF_TRUE     2 (to 20)
        # 643          16 LOAD_CONST               1 (False)
        # 18 RETURN_VALUE
        # 644     >>   20 NOP
        # 646          22 LOAD_GLOBAL              3 (NULL + hasattr)
        # 34 LOAD_FAST                0 (self)
        # 36 LOAD_ATTR                0 (_window)
        # 46 LOAD_CONST               2 ('gui')
        # 48 PRECALL                  2
        # 52 CALL                     2
        # 62 POP_JUMP_FORWARD_IF_FALSE   112 (to 288)
        # 64 LOAD_GLOBAL              3 (NULL + hasattr)
        # 76 LOAD_FAST                0 (self)
        # 78 LOAD_ATTR                0 (_window)
        # 88 LOAD_ATTR                2 (gui)
        # 98 LOAD_CONST               3 ('webview')
        # 100 PRECALL                  2
        # 104 CALL                     2
        # 114 POP_JUMP_FORWARD_IF_FALSE    86 (to 288)
        # 647         116 LOAD_FAST                0 (self)
        # 118 LOAD_ATTR                0 (_window)
        # 128 LOAD_ATTR                2 (gui)
        # 138 LOAD_ATTR                3 (webview)
        # 148 STORE_FAST               1 (webview_ctrl)
        # 648         150 LOAD_GLOBAL              3 (NULL + hasattr)
        # 162 LOAD_FAST                1 (webview_ctrl)
        # 164 LOAD_CONST               4 ('CoreWebView2')
        # 166 PRECALL                  2
        # 170 CALL                     2
        # 180 POP_JUMP_FORWARD_IF_FALSE    53 (to 288)
        # 649         182 LOAD_FAST                1 (webview_ctrl)
        # 184 LOAD_ATTR                4 (CoreWebView2)
        # 194 LOAD_METHOD              5 (OpenDevToolsWindow)
        # 216 PRECALL                  0
        # 220 CALL                     0
        # 230 POP_TOP
        # 650         232 LOAD_GLOBAL             12 (logger)
        # 244 LOAD_METHOD              7 (info)
        # 266 LOAD_CONST               5 ('Developer tools opened via F12')
        # 268 PRECALL                  1
        # 272 CALL                     1
        # 282 POP_TOP
        # 651         284 LOAD_CONST               6 (True)
        # 286 RETURN_VALUE
        # 652     >>  288 LOAD_GLOBAL             12 (logger)
        # 300 LOAD_METHOD              8 (warning)
        # 322 LOAD_CONST               7 ('Developer tools not available (EdgeChromium only)')
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 POP_TOP
        # 653         340 LOAD_CONST               1 (False)
        # 342 RETURN_VALUE
        # >>  344 PUSH_EXC_INFO
        # 654         346 LOAD_GLOBAL             18 (Exception)
        # 358 CHECK_EXC_MATCH
        # 360 POP_JUMP_FORWARD_IF_FALSE    40 (to 442)
        # 362 STORE_FAST               2 (e)
        # 655         364 LOAD_GLOBAL             12 (logger)
        # 376 LOAD_METHOD             10 (error)
        # 398 LOAD_CONST               8 ('Failed to open developer tools: ')
        # 400 LOAD_FAST                2 (e)
        # 402 FORMAT_VALUE             0
        # 404 BUILD_STRING             2
        # 406 PRECALL                  1
        # 410 CALL                     1
        # 420 POP_TOP
        # 656         422 POP_EXCEPT
        # 424 LOAD_CONST               9 (None)
        # 426 STORE_FAST               2 (e)
        # 428 DELETE_FAST              2 (e)
        # 430 LOAD_CONST               1 (False)
        # 432 RETURN_VALUE
        # >>  434 LOAD_CONST               9 (None)
        # 436 STORE_FAST               2 (e)
        # 438 DELETE_FAST              2 (e)
        # 440 RERAISE                  1
        # 654     >>  442 RERAISE                  0
        # >>  444 COPY                     3
        # 446 POP_EXCEPT
        # 448 RERAISE                  1
        # ExceptionTable:
        # 22 to 282 -> 344 [0]
        # 288 to 338 -> 344 [0]
        # 344 to 362 -> 444 [1] lasti
        # 364 to 420 -> 434 [1] lasti
        # 434 to 442 -> 444 [1] lasti

    def save_file_dialog(self, source_path, default_filename, file_types):
        """
        파일 저장 대화상자를 열고 소스 파일을 사용자가 선택한 위치로 복사

        Args:
            source_path: 복사할 소스 파일의 절대 경로
            default_filename: 저장 대화상자에 표시할 기본 파일명
            file_types: 파일 필터 목록 (예: ['Vrew Files (*.vrew)', 'All Files (*.*)'])

        Returns:
            dict: {'success': bool, 'path': str or None, 'error': str or None}
        """
        # 658           0 RESUME                   0
        # 670           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (webview)
        # 8 STORE_FAST               4 (webview)
        # 671          10 LOAD_CONST               1 (0)
        # 12 LOAD_CONST               2 (None)
        # 14 IMPORT_NAME              1 (shutil)
        # 16 STORE_FAST               5 (shutil)
        # 673          18 LOAD_FAST                0 (self)
        # 20 LOAD_ATTR                2 (_window)
        # 30 POP_JUMP_FORWARD_IF_TRUE     6 (to 44)
        # 674          32 LOAD_CONST               3 (False)
        # 34 LOAD_CONST               2 (None)
        # 36 LOAD_CONST               4 ('Window not available')
        # 38 LOAD_CONST               5 (('success', 'path', 'error'))
        # 40 BUILD_CONST_KEY_MAP      3
        # 42 RETURN_VALUE
        # 676     >>   44 NOP
        # 678          46 LOAD_GLOBAL              6 (os)
        # 58 LOAD_ATTR                4 (path)
        # 68 LOAD_METHOD              5 (exists)
        # 90 LOAD_FAST                1 (source_path)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 POP_JUMP_FORWARD_IF_TRUE     9 (to 126)
        # 679         108 LOAD_CONST               3 (False)
        # 110 LOAD_CONST               2 (None)
        # 112 LOAD_CONST               6 ('Source file not found: ')
        # 114 LOAD_FAST                1 (source_path)
        # 116 FORMAT_VALUE             0
        # 118 BUILD_STRING             2
        # 120 LOAD_CONST               5 (('success', 'path', 'error'))
        # 122 BUILD_CONST_KEY_MAP      3
        # 124 RETURN_VALUE
        # 682     >>  126 LOAD_FAST                3 (file_types)
        # 128 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 136)
        # 683         130 LOAD_CONST               7 (('All Files (*.*)',))
        # 132 STORE_FAST               3 (file_types)
        # 134 JUMP_FORWARD            15 (to 166)
        # 685     >>  136 LOAD_GLOBAL             13 (NULL + tuple)
        # 148 LOAD_FAST                3 (file_types)
        # 150 PRECALL                  1
        # 154 CALL                     1
        # 164 STORE_FAST               3 (file_types)
        # 688     >>  166 LOAD_FAST                0 (self)
        # 168 LOAD_ATTR                2 (_window)
        # 178 LOAD_METHOD              7 (create_file_dialog)
        # 689         200 LOAD_FAST                4 (webview)
        # 202 LOAD_ATTR                8 (SAVE_DIALOG)
        # 690         212 LOAD_FAST                2 (default_filename)
        # 691         214 LOAD_FAST                3 (file_types)
        # 688         216 KW_NAMES                 8
        # 218 PRECALL                  3
        # 222 CALL                     3
        # 232 STORE_FAST               6 (result)
        # 694         234 LOAD_FAST                6 (result)
        # 236 POP_JUMP_FORWARD_IF_FALSE   107 (to 452)
        # 238 LOAD_GLOBAL             19 (NULL + len)
        # 250 LOAD_FAST                6 (result)
        # 252 PRECALL                  1
        # 256 CALL                     1
        # 266 LOAD_CONST               1 (0)
        # 268 COMPARE_OP               4 (>)
        # 274 POP_JUMP_FORWARD_IF_FALSE    88 (to 452)
        # 695         276 LOAD_GLOBAL             21 (NULL + isinstance)
        # 288 LOAD_FAST                6 (result)
        # 290 LOAD_GLOBAL             22 (str)
        # 302 PRECALL                  2
        # 306 CALL                     2
        # 316 POP_JUMP_FORWARD_IF_FALSE     2 (to 322)
        # 318 LOAD_FAST                6 (result)
        # 320 JUMP_FORWARD             7 (to 336)
        # >>  322 LOAD_FAST                6 (result)
        # 324 LOAD_CONST               1 (0)
        # 326 BINARY_SUBSCR
        # >>  336 STORE_FAST               7 (dest_path)
        # 698         338 LOAD_FAST                5 (shutil)
        # 340 LOAD_METHOD             12 (copy2)
        # 362 LOAD_FAST                1 (source_path)
        # 364 LOAD_FAST                7 (dest_path)
        # 366 PRECALL                  2
        # 370 CALL                     2
        # 380 POP_TOP
        # 699         382 LOAD_GLOBAL             26 (logger)
        # 394 LOAD_METHOD             14 (info)
        # 416 LOAD_CONST               9 ('File saved: ')
        # 418 LOAD_FAST                7 (dest_path)
        # 420 FORMAT_VALUE             0
        # 422 BUILD_STRING             2
        # 424 PRECALL                  1
        # 428 CALL                     1
        # 438 POP_TOP
        # 701         440 LOAD_CONST              10 (True)
        # 442 LOAD_FAST                7 (dest_path)
        # 444 LOAD_CONST               2 (None)
        # 446 LOAD_CONST               5 (('success', 'path', 'error'))
        # 448 BUILD_CONST_KEY_MAP      3
        # 450 RETURN_VALUE
        # 704     >>  452 LOAD_GLOBAL             26 (logger)
        # 464 LOAD_METHOD             14 (info)
        # 486 LOAD_CONST              11 ('Save dialog cancelled by user')
        # 488 PRECALL                  1
        # 492 CALL                     1
        # 502 POP_TOP
        # 705         504 LOAD_CONST               3 (False)
        # 506 LOAD_CONST               2 (None)
        # 508 LOAD_CONST              12 ('cancelled')
        # 510 LOAD_CONST               5 (('success', 'path', 'error'))
        # 512 BUILD_CONST_KEY_MAP      3
        # 514 RETURN_VALUE
        # >>  516 PUSH_EXC_INFO
        # 707         518 LOAD_GLOBAL             30 (Exception)
        # 530 CHECK_EXC_MATCH
        # 532 POP_JUMP_FORWARD_IF_FALSE    58 (to 650)
        # 534 STORE_FAST               8 (e)
        # 708         536 LOAD_GLOBAL             26 (logger)
        # 548 LOAD_METHOD             16 (error)
        # 570 LOAD_CONST              13 ('Failed to save file: ')
        # 572 LOAD_FAST                8 (e)
        # 574 FORMAT_VALUE             0
        # 576 BUILD_STRING             2
        # 578 PRECALL                  1
        # 582 CALL                     1
        # 592 POP_TOP
        # 709         594 LOAD_CONST               3 (False)
        # 596 LOAD_CONST               2 (None)
        # 598 LOAD_GLOBAL             23 (NULL + str)
        # 610 LOAD_FAST                8 (e)
        # 612 PRECALL                  1
        # 616 CALL                     1
        # 626 LOAD_CONST               5 (('success', 'path', 'error'))
        # 628 BUILD_CONST_KEY_MAP      3
        # 630 SWAP                     2
        # 632 POP_EXCEPT
        # 634 LOAD_CONST               2 (None)
        # 636 STORE_FAST               8 (e)
        # 638 DELETE_FAST              8 (e)
        # 640 RETURN_VALUE
        # >>  642 LOAD_CONST               2 (None)
        # 644 STORE_FAST               8 (e)
        # 646 DELETE_FAST              8 (e)
        # 648 RERAISE                  1
        # 707     >>  650 RERAISE                  0
        # >>  652 COPY                     3
        # 654 POP_EXCEPT
        # 656 RERAISE                  1
        # ExceptionTable:
        # 46 to 122 -> 516 [0]
        # 126 to 448 -> 516 [0]
        # 452 to 512 -> 516 [0]
        # 516 to 534 -> 652 [1] lasti
        # 536 to 628 -> 642 [1] lasti
        # 630 to 630 -> 652 [1] lasti
        # 642 to 650 -> 652 [1] lasti

    def save_blob_dialog(self, data_base64, default_filename, file_types):
        """
        저장 대화상자를 열고 Base64 데이터를 파일로 저장 (프론트엔드에서 생성된 Blob용)

        Args:
            data_base64: Base64로 인코딩된 파일 데이터
            default_filename: 저장 대화상자에 표시할 기본 파일명
            file_types: 파일 필터 목록 (예: ['ZIP Files (*.zip)', 'All Files (*.*)'])

        Returns:
            dict: {'success': bool, 'path': str or None, 'error': str or None}
        """
        # 711           0 RESUME                   0
        # 723           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (webview)
        # 8 STORE_FAST               4 (webview)
        # 724          10 LOAD_CONST               1 (0)
        # 12 LOAD_CONST               2 (None)
        # 14 IMPORT_NAME              1 (base64)
        # 16 STORE_FAST               5 (base64)
        # 726          18 LOAD_FAST                0 (self)
        # 20 LOAD_ATTR                2 (_window)
        # 30 POP_JUMP_FORWARD_IF_TRUE     6 (to 44)
        # 727          32 LOAD_CONST               3 (False)
        # 34 LOAD_CONST               2 (None)
        # 36 LOAD_CONST               4 ('Window not available')
        # 38 LOAD_CONST               5 (('success', 'path', 'error'))
        # 40 BUILD_CONST_KEY_MAP      3
        # 42 RETURN_VALUE
        # 729     >>   44 NOP
        # 731          46 LOAD_FAST                3 (file_types)
        # 48 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 56)
        # 732          50 LOAD_CONST               6 (('All Files (*.*)',))
        # 52 STORE_FAST               3 (file_types)
        # 54 JUMP_FORWARD            15 (to 86)
        # 734     >>   56 LOAD_GLOBAL              7 (NULL + tuple)
        # 68 LOAD_FAST                3 (file_types)
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 STORE_FAST               3 (file_types)
        # 737     >>   86 LOAD_FAST                0 (self)
        # 88 LOAD_ATTR                2 (_window)
        # 98 LOAD_METHOD              4 (create_file_dialog)
        # 738         120 LOAD_FAST                4 (webview)
        # 122 LOAD_ATTR                5 (SAVE_DIALOG)
        # 739         132 LOAD_FAST                2 (default_filename)
        # 740         134 LOAD_FAST                3 (file_types)
        # 737         136 KW_NAMES                 7
        # 138 PRECALL                  3
        # 142 CALL                     3
        # 152 STORE_FAST               6 (result)
        # 743         154 LOAD_FAST                6 (result)
        # 156 POP_JUMP_FORWARD_IF_FALSE   167 (to 492)
        # 158 LOAD_GLOBAL             13 (NULL + len)
        # 170 LOAD_FAST                6 (result)
        # 172 PRECALL                  1
        # 176 CALL                     1
        # 186 LOAD_CONST               1 (0)
        # 188 COMPARE_OP               4 (>)
        # 194 POP_JUMP_FORWARD_IF_FALSE   148 (to 492)
        # 744         196 LOAD_GLOBAL             15 (NULL + isinstance)
        # 208 LOAD_FAST                6 (result)
        # 210 LOAD_GLOBAL             16 (str)
        # 222 PRECALL                  2
        # 226 CALL                     2
        # 236 POP_JUMP_FORWARD_IF_FALSE     2 (to 242)
        # 238 LOAD_FAST                6 (result)
        # 240 JUMP_FORWARD             7 (to 256)
        # >>  242 LOAD_FAST                6 (result)
        # 244 LOAD_CONST               1 (0)
        # 246 BINARY_SUBSCR
        # >>  256 STORE_FAST               7 (dest_path)
        # 747         258 LOAD_FAST                5 (base64)
        # 260 LOAD_METHOD              9 (b64decode)
        # 282 LOAD_FAST                1 (data_base64)
        # 284 PRECALL                  1
        # 288 CALL                     1
        # 298 STORE_FAST               8 (file_data)
        # 748         300 LOAD_GLOBAL             21 (NULL + open)
        # 312 LOAD_FAST                7 (dest_path)
        # 314 LOAD_CONST               8 ('wb')
        # 316 PRECALL                  2
        # 320 CALL                     2
        # 330 BEFORE_WITH
        # 332 STORE_FAST               9 (f)
        # 749         334 LOAD_FAST                9 (f)
        # 336 LOAD_METHOD             11 (write)
        # 358 LOAD_FAST                8 (file_data)
        # 360 PRECALL                  1
        # 364 CALL                     1
        # 374 POP_TOP
        # 748         376 LOAD_CONST               2 (None)
        # 378 LOAD_CONST               2 (None)
        # 380 LOAD_CONST               2 (None)
        # 382 PRECALL                  2
        # 386 CALL                     2
        # 396 POP_TOP
        # 398 JUMP_FORWARD            11 (to 422)
        # >>  400 PUSH_EXC_INFO
        # 402 WITH_EXCEPT_START
        # 404 POP_JUMP_FORWARD_IF_TRUE     4 (to 414)
        # 406 RERAISE                  2
        # >>  408 COPY                     3
        # 410 POP_EXCEPT
        # 412 RERAISE                  1
        # >>  414 POP_TOP
        # 416 POP_EXCEPT
        # 418 POP_TOP
        # 420 POP_TOP
        # 751     >>  422 LOAD_GLOBAL             24 (logger)
        # 434 LOAD_METHOD             13 (info)
        # 456 LOAD_CONST               9 ('Blob saved: ')
        # 458 LOAD_FAST                7 (dest_path)
        # 460 FORMAT_VALUE             0
        # 462 BUILD_STRING             2
        # 464 PRECALL                  1
        # 468 CALL                     1
        # 478 POP_TOP
        # 752         480 LOAD_CONST              10 (True)
        # 482 LOAD_FAST                7 (dest_path)
        # 484 LOAD_CONST               2 (None)
        # 486 LOAD_CONST               5 (('success', 'path', 'error'))
        # 488 BUILD_CONST_KEY_MAP      3
        # 490 RETURN_VALUE
        # 754     >>  492 LOAD_GLOBAL             24 (logger)
        # 504 LOAD_METHOD             13 (info)
        # 526 LOAD_CONST              11 ('Save dialog cancelled by user')
        # 528 PRECALL                  1
        # 532 CALL                     1
        # 542 POP_TOP
        # 755         544 LOAD_CONST               3 (False)
        # 546 LOAD_CONST               2 (None)
        # 548 LOAD_CONST              12 ('cancelled')
        # 550 LOAD_CONST               5 (('success', 'path', 'error'))
        # 552 BUILD_CONST_KEY_MAP      3
        # 554 RETURN_VALUE
        # >>  556 PUSH_EXC_INFO
        # 757         558 LOAD_GLOBAL             28 (Exception)
        # 570 CHECK_EXC_MATCH
        # 572 POP_JUMP_FORWARD_IF_FALSE    58 (to 690)
        # 574 STORE_FAST              10 (e)
        # 758         576 LOAD_GLOBAL             24 (logger)
        # 588 LOAD_METHOD             15 (error)
        # 610 LOAD_CONST              13 ('Failed to save blob: ')
        # 612 LOAD_FAST               10 (e)
        # 614 FORMAT_VALUE             0
        # 616 BUILD_STRING             2
        # 618 PRECALL                  1
        # 622 CALL                     1
        # 632 POP_TOP
        # 759         634 LOAD_CONST               3 (False)
        # 636 LOAD_CONST               2 (None)
        # 638 LOAD_GLOBAL             17 (NULL + str)
        # 650 LOAD_FAST               10 (e)
        # 652 PRECALL                  1
        # 656 CALL                     1
        # 666 LOAD_CONST               5 (('success', 'path', 'error'))
        # 668 BUILD_CONST_KEY_MAP      3
        # 670 SWAP                     2
        # 672 POP_EXCEPT
        # 674 LOAD_CONST               2 (None)
        # 676 STORE_FAST              10 (e)
        # 678 DELETE_FAST             10 (e)
        # 680 RETURN_VALUE
        # >>  682 LOAD_CONST               2 (None)
        # 684 STORE_FAST              10 (e)
        # 686 DELETE_FAST             10 (e)
        # 688 RERAISE                  1
        # 757     >>  690 RERAISE                  0
        # >>  692 COPY                     3
        # 694 POP_EXCEPT
        # 696 RERAISE                  1
        # ExceptionTable:
        # 46 to 330 -> 556 [0]
        # 332 to 374 -> 400 [1] lasti
        # 376 to 398 -> 556 [0]
        # 400 to 406 -> 408 [3] lasti
        # 408 to 412 -> 556 [0]
        # 414 to 414 -> 408 [3] lasti
        # 416 to 488 -> 556 [0]
        # 492 to 552 -> 556 [0]
        # 556 to 574 -> 692 [1] lasti
        # 576 to 668 -> 682 [1] lasti
        # 670 to 670 -> 692 [1] lasti
        # 682 to 690 -> 692 [1] lasti

    def select_folder_dialog(self, initial_path):
        """
        폴더 선택 대화상자를 열고 선택한 폴더 경로를 반환

        Args:
            initial_path: 초기 폴더 경로 (선택 사항)

        Returns:
            dict: {'success': bool, 'path': str or None, 'error': str or None}
        """
        # 761           0 RESUME                   0
        # 771           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (webview)
        # 8 STORE_FAST               2 (webview)
        # 773          10 LOAD_FAST                0 (self)
        # 12 LOAD_ATTR                1 (_window)
        # 22 POP_JUMP_FORWARD_IF_TRUE     6 (to 36)
        # 774          24 LOAD_CONST               3 (False)
        # 26 LOAD_CONST               2 (None)
        # 28 LOAD_CONST               4 ('Window not available')
        # 30 LOAD_CONST               5 (('success', 'path', 'error'))
        # 32 BUILD_CONST_KEY_MAP      3
        # 34 RETURN_VALUE
        # 776     >>   36 NOP
        # 778          38 LOAD_CONST               2 (None)
        # 40 STORE_FAST               3 (directory)
        # 779          42 LOAD_FAST                1 (initial_path)
        # 44 POP_JUMP_FORWARD_IF_FALSE    33 (to 112)
        # 46 LOAD_GLOBAL              4 (os)
        # 58 LOAD_ATTR                3 (path)
        # 68 LOAD_METHOD              4 (isdir)
        # 90 LOAD_FAST                1 (initial_path)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 POP_JUMP_FORWARD_IF_FALSE     2 (to 112)
        # 780         108 LOAD_FAST                1 (initial_path)
        # 110 STORE_FAST               3 (directory)
        # 783     >>  112 LOAD_FAST                0 (self)
        # 114 LOAD_ATTR                1 (_window)
        # 124 LOAD_METHOD              5 (create_file_dialog)
        # 784         146 LOAD_FAST                2 (webview)
        # 148 LOAD_ATTR                6 (FOLDER_DIALOG)
        # 785         158 LOAD_FAST                3 (directory)
        # 783         160 KW_NAMES                 6
        # 162 PRECALL                  2
        # 166 CALL                     2
        # 176 STORE_FAST               4 (result)
        # 788         178 LOAD_FAST                4 (result)
        # 180 POP_JUMP_FORWARD_IF_FALSE    85 (to 352)
        # 182 LOAD_GLOBAL             15 (NULL + len)
        # 194 LOAD_FAST                4 (result)
        # 196 PRECALL                  1
        # 200 CALL                     1
        # 210 LOAD_CONST               1 (0)
        # 212 COMPARE_OP               4 (>)
        # 218 POP_JUMP_FORWARD_IF_FALSE    66 (to 352)
        # 789         220 LOAD_GLOBAL             17 (NULL + isinstance)
        # 232 LOAD_FAST                4 (result)
        # 234 LOAD_GLOBAL             18 (str)
        # 246 PRECALL                  2
        # 250 CALL                     2
        # 260 POP_JUMP_FORWARD_IF_FALSE     2 (to 266)
        # 262 LOAD_FAST                4 (result)
        # 264 JUMP_FORWARD             7 (to 280)
        # >>  266 LOAD_FAST                4 (result)
        # 268 LOAD_CONST               1 (0)
        # 270 BINARY_SUBSCR
        # >>  280 STORE_FAST               5 (selected_path)
        # 790         282 LOAD_GLOBAL             20 (logger)
        # 294 LOAD_METHOD             11 (info)
        # 316 LOAD_CONST               7 ('Folder selected: ')
        # 318 LOAD_FAST                5 (selected_path)
        # 320 FORMAT_VALUE             0
        # 322 BUILD_STRING             2
        # 324 PRECALL                  1
        # 328 CALL                     1
        # 338 POP_TOP
        # 791         340 LOAD_CONST               8 (True)
        # 342 LOAD_FAST                5 (selected_path)
        # 344 LOAD_CONST               2 (None)
        # 346 LOAD_CONST               5 (('success', 'path', 'error'))
        # 348 BUILD_CONST_KEY_MAP      3
        # 350 RETURN_VALUE
        # 794     >>  352 LOAD_GLOBAL             20 (logger)
        # 364 LOAD_METHOD             11 (info)
        # 386 LOAD_CONST               9 ('Folder selection cancelled by user')
        # 388 PRECALL                  1
        # 392 CALL                     1
        # 402 POP_TOP
        # 795         404 LOAD_CONST               3 (False)
        # 406 LOAD_CONST               2 (None)
        # 408 LOAD_CONST              10 ('cancelled')
        # 410 LOAD_CONST               5 (('success', 'path', 'error'))
        # 412 BUILD_CONST_KEY_MAP      3
        # 414 RETURN_VALUE
        # >>  416 PUSH_EXC_INFO
        # 797         418 LOAD_GLOBAL             24 (Exception)
        # 430 CHECK_EXC_MATCH
        # 432 POP_JUMP_FORWARD_IF_FALSE    58 (to 550)
        # 434 STORE_FAST               6 (e)
        # 798         436 LOAD_GLOBAL             20 (logger)
        # 448 LOAD_METHOD             13 (error)
        # 470 LOAD_CONST              11 ('Failed to select folder: ')
        # 472 LOAD_FAST                6 (e)
        # 474 FORMAT_VALUE             0
        # 476 BUILD_STRING             2
        # 478 PRECALL                  1
        # 482 CALL                     1
        # 492 POP_TOP
        # 799         494 LOAD_CONST               3 (False)
        # 496 LOAD_CONST               2 (None)
        # 498 LOAD_GLOBAL             19 (NULL + str)
        # 510 LOAD_FAST                6 (e)
        # 512 PRECALL                  1
        # 516 CALL                     1
        # 526 LOAD_CONST               5 (('success', 'path', 'error'))
        # 528 BUILD_CONST_KEY_MAP      3
        # 530 SWAP                     2
        # 532 POP_EXCEPT
        # 534 LOAD_CONST               2 (None)
        # 536 STORE_FAST               6 (e)
        # 538 DELETE_FAST              6 (e)
        # 540 RETURN_VALUE
        # >>  542 LOAD_CONST               2 (None)
        # 544 STORE_FAST               6 (e)
        # 546 DELETE_FAST              6 (e)
        # 548 RERAISE                  1
        # 797     >>  550 RERAISE                  0
        # >>  552 COPY                     3
        # 554 POP_EXCEPT
        # 556 RERAISE                  1
        # ExceptionTable:
        # 38 to 348 -> 416 [0]
        # 352 to 412 -> 416 [0]
        # 416 to 434 -> 552 [1] lasti
        # 436 to 528 -> 542 [1] lasti
        # 530 to 530 -> 552 [1] lasti
        # 542 to 550 -> 552 [1] lasti

    def open_folder(self, folder_path):
        """
        폴더를 탐색기에서 열기

        Args:
            folder_path: 열 폴더의 절대 경로

        Returns:
            dict: {'success': bool, 'error': str or None}
        """
        # 801           0 RESUME                   0
        # 811           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (('open_folder_foreground',))
        # 6 IMPORT_NAME              0 (app.utils.folder_utils)
        # 8 IMPORT_FROM              1 (open_folder_foreground)
        # 10 STORE_FAST               2 (open_folder_foreground)
        # 12 POP_TOP
        # 813          14 NOP
        # 814          16 LOAD_GLOBAL              4 (os)
        # 28 LOAD_ATTR                3 (path)
        # 38 LOAD_METHOD              4 (exists)
        # 60 LOAD_FAST                1 (folder_path)
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 POP_JUMP_FORWARD_IF_TRUE     8 (to 94)
        # 815          78 LOAD_CONST               3 (False)
        # 80 LOAD_CONST               4 ('Folder not found: ')
        # 82 LOAD_FAST                1 (folder_path)
        # 84 FORMAT_VALUE             0
        # 86 BUILD_STRING             2
        # 88 LOAD_CONST               5 (('success', 'error'))
        # 90 BUILD_CONST_KEY_MAP      2
        # 92 RETURN_VALUE
        # 818     >>   94 PUSH_NULL
        # 96 LOAD_FAST                2 (open_folder_foreground)
        # 98 LOAD_FAST                1 (folder_path)
        # 100 PRECALL                  1
        # 104 CALL                     1
        # 114 STORE_FAST               3 (success)
        # 820         116 LOAD_FAST                3 (success)
        # 118 POP_JUMP_FORWARD_IF_FALSE    34 (to 188)
        # 821         120 LOAD_GLOBAL             10 (logger)
        # 132 LOAD_METHOD              6 (info)
        # 154 LOAD_CONST               6 ('Folder opened: ')
        # 156 LOAD_FAST                1 (folder_path)
        # 158 FORMAT_VALUE             0
        # 160 BUILD_STRING             2
        # 162 PRECALL                  1
        # 166 CALL                     1
        # 176 POP_TOP
        # 822         178 LOAD_CONST               7 (True)
        # 180 LOAD_CONST               8 (None)
        # 182 LOAD_CONST               5 (('success', 'error'))
        # 184 BUILD_CONST_KEY_MAP      2
        # 186 RETURN_VALUE
        # 824     >>  188 LOAD_CONST               3 (False)
        # 190 LOAD_CONST               9 ('Failed to open folder')
        # 192 LOAD_CONST               5 (('success', 'error'))
        # 194 BUILD_CONST_KEY_MAP      2
        # 196 RETURN_VALUE
        # >>  198 PUSH_EXC_INFO
        # 826         200 LOAD_GLOBAL             14 (Exception)
        # 212 CHECK_EXC_MATCH
        # 214 POP_JUMP_FORWARD_IF_FALSE    57 (to 330)
        # 216 STORE_FAST               4 (e)
        # 827         218 LOAD_GLOBAL             10 (logger)
        # 230 LOAD_METHOD              8 (error)
        # 252 LOAD_CONST              10 ('Failed to open folder: ')
        # 254 LOAD_FAST                4 (e)
        # 256 FORMAT_VALUE             0
        # 258 BUILD_STRING             2
        # 260 PRECALL                  1
        # 264 CALL                     1
        # 274 POP_TOP
        # 828         276 LOAD_CONST               3 (False)
        # 278 LOAD_GLOBAL             19 (NULL + str)
        # 290 LOAD_FAST                4 (e)
        # 292 PRECALL                  1
        # 296 CALL                     1
        # 306 LOAD_CONST               5 (('success', 'error'))
        # 308 BUILD_CONST_KEY_MAP      2
        # 310 SWAP                     2
        # 312 POP_EXCEPT
        # 314 LOAD_CONST               8 (None)
        # 316 STORE_FAST               4 (e)
        # 318 DELETE_FAST              4 (e)
        # 320 RETURN_VALUE
        # >>  322 LOAD_CONST               8 (None)
        # 324 STORE_FAST               4 (e)
        # 326 DELETE_FAST              4 (e)
        # 328 RERAISE                  1
        # 826     >>  330 RERAISE                  0
        # >>  332 COPY                     3
        # 334 POP_EXCEPT
        # 336 RERAISE                  1
        # ExceptionTable:
        # 16 to 90 -> 198 [0]
        # 94 to 184 -> 198 [0]
        # 188 to 194 -> 198 [0]
        # 198 to 216 -> 332 [1] lasti
        # 218 to 308 -> 322 [1] lasti
        # 310 to 310 -> 332 [1] lasti
        # 322 to 330 -> 332 [1] lasti

    def select_file_dialog(self, initial_path, file_types, allow_multiple):
        """
        파일 선택 대화상자를 열고 선택한 파일 경로를 반환

        Args:
            initial_path: 초기 폴더 경로 (선택 사항)
            file_types: 파일 필터 목록 (예: ['Image Files (*.png;*.jpg;*.jpeg;*.gif;*.webp)', 'All Files (*.*)'])
            allow_multiple: 다중 선택 허용 여부 (기본값: False)

        Returns:
            dict: {'success': bool, 'paths': list or None, 'error': str or None}
        """
        # 830           0 RESUME                   0
        # 842           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (webview)
        # 8 STORE_FAST               4 (webview)
        # 844          10 LOAD_FAST                0 (self)
        # 12 LOAD_ATTR                1 (_window)
        # 22 POP_JUMP_FORWARD_IF_TRUE     6 (to 36)
        # 845          24 LOAD_CONST               3 (False)
        # 26 LOAD_CONST               2 (None)
        # 28 LOAD_CONST               4 ('Window not available')
        # 30 LOAD_CONST               5 (('success', 'paths', 'error'))
        # 32 BUILD_CONST_KEY_MAP      3
        # 34 RETURN_VALUE
        # 847     >>   36 NOP
        # 849          38 LOAD_CONST               2 (None)
        # 40 STORE_FAST               5 (directory)
        # 850          42 LOAD_FAST                1 (initial_path)
        # 44 POP_JUMP_FORWARD_IF_FALSE    96 (to 238)
        # 852          46 LOAD_GLOBAL              4 (os)
        # 58 LOAD_ATTR                3 (path)
        # 68 LOAD_METHOD              4 (isfile)
        # 90 LOAD_FAST                1 (initial_path)
        # 92 PRECALL                  1
        # 96 CALL                     1
        # 106 POP_JUMP_FORWARD_IF_FALSE    32 (to 172)
        # 853         108 LOAD_GLOBAL              4 (os)
        # 120 LOAD_ATTR                3 (path)
        # 130 LOAD_METHOD              5 (dirname)
        # 152 LOAD_FAST                1 (initial_path)
        # 154 PRECALL                  1
        # 158 CALL                     1
        # 168 STORE_FAST               5 (directory)
        # 170 JUMP_FORWARD            33 (to 238)
        # 854     >>  172 LOAD_GLOBAL              4 (os)
        # 184 LOAD_ATTR                3 (path)
        # 194 LOAD_METHOD              6 (isdir)
        # 216 LOAD_FAST                1 (initial_path)
        # 218 PRECALL                  1
        # 222 CALL                     1
        # 232 POP_JUMP_FORWARD_IF_FALSE     2 (to 238)
        # 855         234 LOAD_FAST                1 (initial_path)
        # 236 STORE_FAST               5 (directory)
        # 858     >>  238 LOAD_FAST                2 (file_types)
        # 240 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 248)
        # 859         242 LOAD_CONST               6 (('Image Files (*.png;*.jpg;*.jpeg;*.gif;*.webp)', 'All Files (*.*)'))
        # 244 STORE_FAST               2 (file_types)
        # 246 JUMP_FORWARD            15 (to 278)
        # 861     >>  248 LOAD_GLOBAL             15 (NULL + tuple)
        # 260 LOAD_FAST                2 (file_types)
        # 262 PRECALL                  1
        # 266 CALL                     1
        # 276 STORE_FAST               2 (file_types)
        # 864     >>  278 LOAD_FAST                0 (self)
        # 280 LOAD_ATTR                1 (_window)
        # 290 LOAD_METHOD              8 (create_file_dialog)
        # 865         312 LOAD_FAST                4 (webview)
        # 314 LOAD_ATTR                9 (OPEN_DIALOG)
        # 866         324 LOAD_FAST                5 (directory)
        # 867         326 LOAD_FAST                3 (allow_multiple)
        # 868         328 LOAD_FAST                2 (file_types)
        # 864         330 KW_NAMES                 7
        # 332 PRECALL                  4
        # 336 CALL                     4
        # 346 STORE_FAST               6 (result)
        # 871         348 LOAD_FAST                6 (result)
        # 350 POP_JUMP_FORWARD_IF_FALSE    93 (to 538)
        # 352 LOAD_GLOBAL             21 (NULL + len)
        # 364 LOAD_FAST                6 (result)
        # 366 PRECALL                  1
        # 370 CALL                     1
        # 380 LOAD_CONST               1 (0)
        # 382 COMPARE_OP               4 (>)
        # 388 POP_JUMP_FORWARD_IF_FALSE    74 (to 538)
        # 873         390 LOAD_GLOBAL             23 (NULL + isinstance)
        # 402 LOAD_FAST                6 (result)
        # 404 LOAD_GLOBAL             24 (str)
        # 416 PRECALL                  2
        # 420 CALL                     2
        # 430 POP_JUMP_FORWARD_IF_FALSE     3 (to 438)
        # 432 LOAD_FAST                6 (result)
        # 434 BUILD_LIST               1
        # 436 JUMP_FORWARD            14 (to 466)
        # >>  438 LOAD_GLOBAL             27 (NULL + list)
        # 450 LOAD_FAST                6 (result)
        # 452 PRECALL                  1
        # 456 CALL                     1
        # >>  466 STORE_FAST               7 (paths)
        # 874         468 LOAD_GLOBAL             28 (logger)
        # 480 LOAD_METHOD             15 (info)
        # 502 LOAD_CONST               8 ('File(s) selected: ')
        # 504 LOAD_FAST                7 (paths)
        # 506 FORMAT_VALUE             0
        # 508 BUILD_STRING             2
        # 510 PRECALL                  1
        # 514 CALL                     1
        # 524 POP_TOP
        # 875         526 LOAD_CONST               9 (True)
        # 528 LOAD_FAST                7 (paths)
        # 530 LOAD_CONST               2 (None)
        # 532 LOAD_CONST               5 (('success', 'paths', 'error'))
        # 534 BUILD_CONST_KEY_MAP      3
        # 536 RETURN_VALUE
        # 878     >>  538 LOAD_GLOBAL             28 (logger)
        # 550 LOAD_METHOD             15 (info)
        # 572 LOAD_CONST              10 ('File selection cancelled by user')
        # 574 PRECALL                  1
        # 578 CALL                     1
        # 588 POP_TOP
        # 879         590 LOAD_CONST               3 (False)
        # 592 LOAD_CONST               2 (None)
        # 594 LOAD_CONST              11 ('cancelled')
        # 596 LOAD_CONST               5 (('success', 'paths', 'error'))
        # 598 BUILD_CONST_KEY_MAP      3
        # 600 RETURN_VALUE
        # >>  602 PUSH_EXC_INFO
        # 881         604 LOAD_GLOBAL             32 (Exception)
        # 616 CHECK_EXC_MATCH
        # 618 POP_JUMP_FORWARD_IF_FALSE    58 (to 736)
        # 620 STORE_FAST               8 (e)
        # 882         622 LOAD_GLOBAL             28 (logger)
        # 634 LOAD_METHOD             17 (error)
        # 656 LOAD_CONST              12 ('Failed to select file: ')
        # 658 LOAD_FAST                8 (e)
        # 660 FORMAT_VALUE             0
        # 662 BUILD_STRING             2
        # 664 PRECALL                  1
        # 668 CALL                     1
        # 678 POP_TOP
        # 883         680 LOAD_CONST               3 (False)
        # 682 LOAD_CONST               2 (None)
        # 684 LOAD_GLOBAL             25 (NULL + str)
        # 696 LOAD_FAST                8 (e)
        # 698 PRECALL                  1
        # 702 CALL                     1
        # 712 LOAD_CONST               5 (('success', 'paths', 'error'))
        # 714 BUILD_CONST_KEY_MAP      3
        # 716 SWAP                     2
        # 718 POP_EXCEPT
        # 720 LOAD_CONST               2 (None)
        # 722 STORE_FAST               8 (e)
        # 724 DELETE_FAST              8 (e)
        # 726 RETURN_VALUE
        # >>  728 LOAD_CONST               2 (None)
        # 730 STORE_FAST               8 (e)
        # 732 DELETE_FAST              8 (e)
        # 734 RERAISE                  1
        # 881     >>  736 RERAISE                  0
        # >>  738 COPY                     3
        # 740 POP_EXCEPT
        # 742 RERAISE                  1
        # ExceptionTable:
        # 38 to 534 -> 602 [0]
        # 538 to 598 -> 602 [0]
        # 602 to 620 -> 738 [1] lasti
        # 622 to 714 -> 728 [1] lasti
        # 716 to 716 -> 738 [1] lasti
        # 728 to 736 -> 738 [1] lasti

    def read_file_as_base64(self, file_path):
        """
        파일을 읽어 Base64 데이터 URL로 반환 (이미지 파일용)

        Args:
            file_path: 읽을 파일의 절대 경로

        Returns:
            dict: {'success': bool, 'dataUrl': str or None, 'mimeType': str or None, 'error': str or None}
        """
        # 885           0 RESUME                   0
        # 895           2 LOAD_CONST               1 (0)
        # 4 LOAD_CONST               2 (None)
        # 6 IMPORT_NAME              0 (base64)
        # 8 STORE_FAST               2 (base64)
        # 896          10 LOAD_CONST               1 (0)
        # 12 LOAD_CONST               2 (None)
        # 14 IMPORT_NAME              1 (mimetypes)
        # 16 STORE_FAST               3 (mimetypes)
        # 898          18 NOP
        # 899          20 LOAD_GLOBAL              4 (os)
        # 32 LOAD_ATTR                3 (path)
        # 42 LOAD_METHOD              4 (exists)
        # 64 LOAD_FAST                1 (file_path)
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 POP_JUMP_FORWARD_IF_TRUE    10 (to 102)
        # 900          82 LOAD_CONST               3 (False)
        # 84 LOAD_CONST               2 (None)
        # 86 LOAD_CONST               2 (None)
        # 88 LOAD_CONST               4 ('File not found: ')
        # 90 LOAD_FAST                1 (file_path)
        # 92 FORMAT_VALUE             0
        # 94 BUILD_STRING             2
        # 96 LOAD_CONST               5 (('success', 'dataUrl', 'mimeType', 'error'))
        # 98 BUILD_CONST_KEY_MAP      4
        # 100 RETURN_VALUE
        # 903     >>  102 LOAD_GLOBAL              4 (os)
        # 114 LOAD_ATTR                3 (path)
        # 124 LOAD_METHOD              5 (getsize)
        # 146 LOAD_FAST                1 (file_path)
        # 148 PRECALL                  1
        # 152 CALL                     1
        # 162 STORE_FAST               4 (file_size)
        # 904         164 LOAD_FAST                4 (file_size)
        # 166 LOAD_CONST               6 (10485760)
        # 168 COMPARE_OP               4 (>)
        # 174 POP_JUMP_FORWARD_IF_FALSE     7 (to 190)
        # 905         176 LOAD_CONST               3 (False)
        # 178 LOAD_CONST               2 (None)
        # 180 LOAD_CONST               2 (None)
        # 182 LOAD_CONST               7 ('File size exceeds 10MB limit')
        # 184 LOAD_CONST               5 (('success', 'dataUrl', 'mimeType', 'error'))
        # 186 BUILD_CONST_KEY_MAP      4
        # 188 RETURN_VALUE
        # 908     >>  190 LOAD_FAST                3 (mimetypes)
        # 192 LOAD_METHOD              6 (guess_type)
        # 214 LOAD_FAST                1 (file_path)
        # 216 PRECALL                  1
        # 220 CALL                     1
        # 230 UNPACK_SEQUENCE          2
        # 234 STORE_FAST               5 (mime_type)
        # 236 STORE_FAST               6 (_)
        # 909         238 LOAD_FAST                5 (mime_type)
        # 240 POP_JUMP_FORWARD_IF_TRUE    86 (to 414)
        # 911         242 LOAD_GLOBAL              4 (os)
        # 254 LOAD_ATTR                3 (path)
        # 264 LOAD_METHOD              7 (splitext)
        # 286 LOAD_FAST                1 (file_path)
        # 288 PRECALL                  1
        # 292 CALL                     1
        # 302 LOAD_CONST               8 (1)
        # 304 BINARY_SUBSCR
        # 314 LOAD_METHOD              8 (lower)
        # 336 PRECALL                  0
        # 340 CALL                     0
        # 350 STORE_FAST               7 (ext)
        # 913         352 LOAD_CONST               9 ('image/png')
        # 914         354 LOAD_CONST              10 ('image/jpeg')
        # 915         356 LOAD_CONST              10 ('image/jpeg')
        # 916         358 LOAD_CONST              11 ('image/gif')
        # 917         360 LOAD_CONST              12 ('image/webp')
        # 918         362 LOAD_CONST              13 ('image/bmp')
        # 912         364 LOAD_CONST              14 (('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'))
        # 366 BUILD_CONST_KEY_MAP      6
        # 368 STORE_FAST               8 (mime_map)
        # 920         370 LOAD_FAST                8 (mime_map)
        # 372 LOAD_METHOD              9 (get)
        # 394 LOAD_FAST                7 (ext)
        # 396 LOAD_CONST              15 ('application/octet-stream')
        # 398 PRECALL                  2
        # 402 CALL                     2
        # 412 STORE_FAST               5 (mime_type)
        # 923     >>  414 LOAD_GLOBAL             21 (NULL + open)
        # 426 LOAD_FAST                1 (file_path)
        # 428 LOAD_CONST              16 ('rb')
        # 430 PRECALL                  2
        # 434 CALL                     2
        # 444 BEFORE_WITH
        # 446 STORE_FAST               9 (f)
        # 924         448 LOAD_FAST                9 (f)
        # 450 LOAD_METHOD             11 (read)
        # 472 PRECALL                  0
        # 476 CALL                     0
        # 486 STORE_FAST              10 (file_data)
        # 923         488 LOAD_CONST               2 (None)
        # 490 LOAD_CONST               2 (None)
        # 492 LOAD_CONST               2 (None)
        # 494 PRECALL                  2
        # 498 CALL                     2
        # 508 POP_TOP
        # 510 JUMP_FORWARD            11 (to 534)
        # >>  512 PUSH_EXC_INFO
        # 514 WITH_EXCEPT_START
        # 516 POP_JUMP_FORWARD_IF_TRUE     4 (to 526)
        # 518 RERAISE                  2
        # >>  520 COPY                     3
        # 522 POP_EXCEPT
        # 524 RERAISE                  1
        # >>  526 POP_TOP
        # 528 POP_EXCEPT
        # 530 POP_TOP
        # 532 POP_TOP
        # 926     >>  534 LOAD_FAST                2 (base64)
        # 536 LOAD_METHOD             12 (b64encode)
        # 558 LOAD_FAST               10 (file_data)
        # 560 PRECALL                  1
        # 564 CALL                     1
        # 574 LOAD_METHOD             13 (decode)
        # 596 LOAD_CONST              17 ('utf-8')
        # 598 PRECALL                  1
        # 602 CALL                     1
        # 612 STORE_FAST              11 (base64_data)
        # 927         614 LOAD_CONST              18 ('data:')
        # 616 LOAD_FAST                5 (mime_type)
        # 618 FORMAT_VALUE             0
        # 620 LOAD_CONST              19 (';base64,')
        # 622 LOAD_FAST               11 (base64_data)
        # 624 FORMAT_VALUE             0
        # 626 BUILD_STRING             4
        # 628 STORE_FAST              12 (data_url)
        # 929         630 LOAD_GLOBAL             28 (logger)
        # 642 LOAD_METHOD             15 (info)
        # 664 LOAD_CONST              20 ('File read as base64: ')
        # 666 LOAD_FAST                1 (file_path)
        # 668 FORMAT_VALUE             0
        # 670 LOAD_CONST              21 (' (')
        # 672 LOAD_GLOBAL             33 (NULL + len)
        # 684 LOAD_FAST               10 (file_data)
        # 686 PRECALL                  1
        # 690 CALL                     1
        # 700 FORMAT_VALUE             0
        # 702 LOAD_CONST              22 (' bytes)')
        # 704 BUILD_STRING             5
        # 706 PRECALL                  1
        # 710 CALL                     1
        # 720 POP_TOP
        # 930         722 LOAD_CONST              23 (True)
        # 724 LOAD_FAST               12 (data_url)
        # 726 LOAD_FAST                5 (mime_type)
        # 728 LOAD_CONST               2 (None)
        # 730 LOAD_CONST               5 (('success', 'dataUrl', 'mimeType', 'error'))
        # 732 BUILD_CONST_KEY_MAP      4
        # 734 RETURN_VALUE
        # >>  736 PUSH_EXC_INFO
        # 932         738 LOAD_GLOBAL             34 (Exception)
        # 750 CHECK_EXC_MATCH
        # 752 POP_JUMP_FORWARD_IF_FALSE    59 (to 872)
        # 754 STORE_FAST              13 (e)
        # 933         756 LOAD_GLOBAL             28 (logger)
        # 768 LOAD_METHOD             18 (error)
        # 790 LOAD_CONST              24 ('Failed to read file as base64: ')
        # 792 LOAD_FAST               13 (e)
        # 794 FORMAT_VALUE             0
        # 796 BUILD_STRING             2
        # 798 PRECALL                  1
        # 802 CALL                     1
        # 812 POP_TOP
        # 934         814 LOAD_CONST               3 (False)
        # 816 LOAD_CONST               2 (None)
        # 818 LOAD_CONST               2 (None)
        # 820 LOAD_GLOBAL             39 (NULL + str)
        # 832 LOAD_FAST               13 (e)
        # 834 PRECALL                  1
        # 838 CALL                     1
        # 848 LOAD_CONST               5 (('success', 'dataUrl', 'mimeType', 'error'))
        # 850 BUILD_CONST_KEY_MAP      4
        # 852 SWAP                     2
        # 854 POP_EXCEPT
        # 856 LOAD_CONST               2 (None)
        # 858 STORE_FAST              13 (e)
        # 860 DELETE_FAST             13 (e)
        # 862 RETURN_VALUE
        # >>  864 LOAD_CONST               2 (None)
        # 866 STORE_FAST              13 (e)
        # 868 DELETE_FAST             13 (e)
        # 870 RERAISE                  1
        # 932     >>  872 RERAISE                  0
        # >>  874 COPY                     3
        # 876 POP_EXCEPT
        # 878 RERAISE                  1
        # ExceptionTable:
        # 20 to 98 -> 736 [0]
        # 102 to 186 -> 736 [0]
        # 190 to 444 -> 736 [0]
        # 446 to 486 -> 512 [1] lasti
        # 488 to 510 -> 736 [0]
        # 512 to 518 -> 520 [3] lasti
        # 520 to 524 -> 736 [0]
        # 526 to 526 -> 520 [3] lasti
        # 528 to 732 -> 736 [0]
        # 736 to 754 -> 874 [1] lasti
        # 756 to 850 -> 864 [1] lasti
        # 852 to 852 -> 874 [1] lasti
        # 864 to 872 -> 874 [1] lasti

    def open_external_url(self, url):
        """
        Open external URL in system default browser.

        Args:
            url: Fully qualified URL (http/https)

        Returns:
            dict: {'success': bool, 'error': str or None}
        """
        # 936           0 RESUME                   0
        # 946           2 NOP
        # 947           4 LOAD_FAST                1 (url)
        # 6 POP_JUMP_FORWARD_IF_FALSE    21 (to 50)
        # 8 LOAD_GLOBAL              1 (NULL + isinstance)
        # 20 LOAD_FAST                1 (url)
        # 22 LOAD_GLOBAL              2 (str)
        # 34 PRECALL                  2
        # 38 CALL                     2
        # 48 POP_JUMP_FORWARD_IF_TRUE     5 (to 60)
        # 948     >>   50 LOAD_CONST               1 (False)
        # 52 LOAD_CONST               2 ('Invalid URL')
        # 54 LOAD_CONST               3 (('success', 'error'))
        # 56 BUILD_CONST_KEY_MAP      2
        # 58 RETURN_VALUE
        # 950     >>   60 LOAD_FAST                1 (url)
        # 62 LOAD_METHOD              2 (strip)
        # 84 PRECALL                  0
        # 88 CALL                     0
        # 98 STORE_FAST               2 (normalized)
        # 951         100 LOAD_FAST                2 (normalized)
        # 102 LOAD_METHOD              3 (startswith)
        # 124 LOAD_CONST               4 ('http://')
        # 126 PRECALL                  1
        # 130 CALL                     1
        # 140 POP_JUMP_FORWARD_IF_TRUE    26 (to 194)
        # 142 LOAD_FAST                2 (normalized)
        # 144 LOAD_METHOD              3 (startswith)
        # 166 LOAD_CONST               5 ('https://')
        # 168 PRECALL                  1
        # 172 CALL                     1
        # 182 POP_JUMP_FORWARD_IF_TRUE     5 (to 194)
        # 952         184 LOAD_CONST               1 (False)
        # 186 LOAD_CONST               6 ('Only http/https URLs are allowed')
        # 188 LOAD_CONST               3 (('success', 'error'))
        # 190 BUILD_CONST_KEY_MAP      2
        # 192 RETURN_VALUE
        # 954     >>  194 LOAD_CONST               7 (0)
        # 196 LOAD_CONST               8 (None)
        # 198 IMPORT_NAME              4 (webbrowser)
        # 200 STORE_FAST               3 (webbrowser)
        # 956         202 LOAD_FAST                3 (webbrowser)
        # 204 LOAD_METHOD              5 (open)
        # 226 LOAD_FAST                2 (normalized)
        # 228 LOAD_CONST               9 (2)
        # 230 KW_NAMES                10
        # 232 PRECALL                  2
        # 236 CALL                     2
        # 246 STORE_FAST               4 (opened)
        # 957         248 LOAD_FAST                4 (opened)
        # 250 POP_JUMP_FORWARD_IF_FALSE    34 (to 320)
        # 958         252 LOAD_GLOBAL             12 (logger)
        # 264 LOAD_METHOD              7 (info)
        # 286 LOAD_CONST              11 ('Opened external URL: ')
        # 288 LOAD_FAST                2 (normalized)
        # 290 FORMAT_VALUE             0
        # 292 BUILD_STRING             2
        # 294 PRECALL                  1
        # 298 CALL                     1
        # 308 POP_TOP
        # 959         310 LOAD_CONST              12 (True)
        # 312 LOAD_CONST               8 (None)
        # 314 LOAD_CONST               3 (('success', 'error'))
        # 316 BUILD_CONST_KEY_MAP      2
        # 318 RETURN_VALUE
        # 961     >>  320 LOAD_CONST               1 (False)
        # 322 LOAD_CONST              13 ('Failed to open browser')
        # 324 LOAD_CONST               3 (('success', 'error'))
        # 326 BUILD_CONST_KEY_MAP      2
        # 328 RETURN_VALUE
        # >>  330 PUSH_EXC_INFO
        # 963         332 LOAD_GLOBAL             16 (Exception)
        # 344 CHECK_EXC_MATCH
        # 346 POP_JUMP_FORWARD_IF_FALSE    57 (to 462)
        # 348 STORE_FAST               5 (e)
        # 964         350 LOAD_GLOBAL             12 (logger)
        # 362 LOAD_METHOD              9 (error)
        # 384 LOAD_CONST              14 ('Failed to open external URL: ')
        # 386 LOAD_FAST                5 (e)
        # 388 FORMAT_VALUE             0
        # 390 BUILD_STRING             2
        # 392 PRECALL                  1
        # 396 CALL                     1
        # 406 POP_TOP
        # 965         408 LOAD_CONST               1 (False)
        # 410 LOAD_GLOBAL              3 (NULL + str)
        # 422 LOAD_FAST                5 (e)
        # 424 PRECALL                  1
        # 428 CALL                     1
        # 438 LOAD_CONST               3 (('success', 'error'))
        # 440 BUILD_CONST_KEY_MAP      2
        # 442 SWAP                     2
        # 444 POP_EXCEPT
        # 446 LOAD_CONST               8 (None)
        # 448 STORE_FAST               5 (e)
        # 450 DELETE_FAST              5 (e)
        # 452 RETURN_VALUE
        # >>  454 LOAD_CONST               8 (None)
        # 456 STORE_FAST               5 (e)
        # 458 DELETE_FAST              5 (e)
        # 460 RERAISE                  1
        # 963     >>  462 RERAISE                  0
        # >>  464 COPY                     3
        # 466 POP_EXCEPT
        # 468 RERAISE                  1
        # ExceptionTable:
        # 4 to 56 -> 330 [0]
        # 60 to 190 -> 330 [0]
        # 194 to 316 -> 330 [0]
        # 320 to 326 -> 330 [0]
        # 330 to 348 -> 464 [1] lasti
        # 350 to 440 -> 454 [1] lasti
        # 442 to 442 -> 464 [1] lasti
        # 454 to 462 -> 464 [1] lasti


def run_with_webview():
    """Run the application with pywebview native window"""
    # 0 MAKE_CELL               17 (server)
    # 2 MAKE_CELL               18 (webview)
    # 4 MAKE_CELL               19 (window_title)
    # 968           6 RESUME                   0
    # 970           8 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 20 LOAD_CONST               1 ('run_with_webview entered')
    # 22 PRECALL                  1
    # 26 CALL                     1
    # 36 POP_TOP
    # 972          38 LOAD_GLOBAL              3 (NULL + _ensure_webview2_runtime_ready)
    # 50 PRECALL                  0
    # 54 CALL                     0
    # 64 POP_JUMP_FORWARD_IF_TRUE     2 (to 70)
    # 973          66 LOAD_CONST               2 (None)
    # 68 RETURN_VALUE
    # 975     >>   70 LOAD_CONST               3 (0)
    # 72 LOAD_CONST               2 (None)
    # 74 IMPORT_NAME              2 (webview)
    # 76 STORE_DEREF             18 (webview)
    # 976          78 LOAD_CONST               3 (0)
    # 80 LOAD_CONST               4 (('Menu', 'MenuAction', 'MenuSeparator'))
    # 82 IMPORT_NAME              3 (webview.menu)
    # 84 IMPORT_FROM              4 (Menu)
    # 86 STORE_FAST               0 (Menu)
    # 88 IMPORT_FROM              5 (MenuAction)
    # 90 STORE_FAST               1 (MenuAction)
    # 92 IMPORT_FROM              6 (MenuSeparator)
    # 94 STORE_FAST               2 (MenuSeparator)
    # 96 POP_TOP
    # 979          98 LOAD_CONST               5 (False)
    # 100 LOAD_DEREF              18 (webview)
    # 102 LOAD_ATTR                7 (settings)
    # 112 LOAD_CONST               6 ('SHOW_DEFAULT_MENUS')
    # 114 STORE_SUBSCR
    # 982         118 LOAD_GLOBAL             16 (IS_FROZEN)
    # 130 POP_JUMP_FORWARD_IF_TRUE    42 (to 216)
    # 983         132 LOAD_CONST               7 ('1')
    # 134 LOAD_GLOBAL             18 (os)
    # 146 LOAD_ATTR               10 (environ)
    # 156 LOAD_CONST               8 ('TFSTUDIO_DEBUG_BROWSER')
    # 158 STORE_SUBSCR
    # 984         162 LOAD_GLOBAL             23 (NULL + get_base_path)
    # 174 PRECALL                  0
    # 178 CALL                     0
    # 188 LOAD_GLOBAL             18 (os)
    # 200 LOAD_ATTR               10 (environ)
    # 210 LOAD_CONST               9 ('TFSTUDIO_PROJECT_ROOT')
    # 212 STORE_SUBSCR
    # 986     >>  216 LOAD_GLOBAL             25 (NULL + setup_environment)
    # 228 PRECALL                  0
    # 232 CALL                     0
    # 242 POP_TOP
    # 987         244 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 256 LOAD_CONST              10 ('setup_environment completed')
    # 258 PRECALL                  1
    # 262 CALL                     1
    # 272 POP_TOP
    # 989         274 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 286 LOAD_CONST              11 ('resolving app version')
    # 288 PRECALL                  1
    # 292 CALL                     1
    # 302 POP_TOP
    # 990         304 LOAD_GLOBAL             27 (NULL + _get_app_version_for_title)
    # 316 PRECALL                  0
    # 320 CALL                     0
    # 330 STORE_FAST               3 (app_version)
    # 991         332 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 344 LOAD_CONST              12 ('app version resolved: ')
    # 346 LOAD_FAST                3 (app_version)
    # 348 FORMAT_VALUE             0
    # 350 BUILD_STRING             2
    # 352 PRECALL                  1
    # 356 CALL                     1
    # 366 POP_TOP
    # 993         368 LOAD_CONST              13 ('TFstudio v')
    # 370 LOAD_FAST                3 (app_version)
    # 372 FORMAT_VALUE             0
    # 374 BUILD_STRING             2
    # 376 STORE_DEREF             19 (window_title)
    # 996         378 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 390 LOAD_CONST              14 ('finding free port')
    # 392 PRECALL                  1
    # 396 CALL                     1
    # 406 POP_TOP
    # 997         408 LOAD_GLOBAL             29 (NULL + find_free_port)
    # 420 LOAD_CONST              15 (5000)
    # 422 PRECALL                  1
    # 426 CALL                     1
    # 436 STORE_FAST               4 (port)
    # 998         438 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 450 LOAD_CONST              16 ('port selected: ')
    # 452 LOAD_FAST                4 (port)
    # 454 FORMAT_VALUE             0
    # 456 BUILD_STRING             2
    # 458 PRECALL                  1
    # 462 CALL                     1
    # 472 POP_TOP
    # 999         474 LOAD_GLOBAL             30 (logger)
    # 486 LOAD_METHOD             16 (info)
    # 508 LOAD_CONST              17 ('Using port: ')
    # 510 LOAD_FAST                4 (port)
    # 512 FORMAT_VALUE             0
    # 514 BUILD_STRING             2
    # 516 PRECALL                  1
    # 520 CALL                     1
    # 530 POP_TOP
    # 1003         532 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 544 LOAD_CONST              18 ('starting flask server')
    # 546 PRECALL                  1
    # 550 CALL                     1
    # 560 POP_TOP
    # 1004         562 LOAD_GLOBAL             35 (NULL + FlaskServer)
    # 574 LOAD_FAST                4 (port)
    # 576 PRECALL                  1
    # 580 CALL                     1
    # 590 STORE_DEREF             17 (server)
    # 1005         592 LOAD_DEREF              17 (server)
    # 594 STORE_GLOBAL            18 (_flask_server)
    # 1006         596 NOP
    # 1007         598 LOAD_DEREF              17 (server)
    # 600 LOAD_METHOD             19 (start)
    # 622 PRECALL                  0
    # 626 CALL                     0
    # 636 POP_TOP
    # 638 JUMP_FORWARD           245 (to 1130)
    # >>  640 PUSH_EXC_INFO
    # 1008         642 LOAD_GLOBAL             40 (RuntimeError)
    # 654 CHECK_EXC_MATCH
    # 656 POP_JUMP_FORWARD_IF_FALSE    72 (to 802)
    # 658 STORE_FAST               5 (e)
    # 1009         660 LOAD_GLOBAL             43 (NULL + str)
    # 672 LOAD_FAST                5 (e)
    # 674 PRECALL                  1
    # 678 CALL                     1
    # 688 STORE_FAST               6 (error_str)
    # 1010         690 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 702 LOAD_CONST              19 ('flask server start failed: ')
    # 704 LOAD_FAST                6 (error_str)
    # 706 FORMAT_VALUE             0
    # 708 BUILD_STRING             2
    # 710 PRECALL                  1
    # 714 CALL                     1
    # 724 POP_TOP
    # 1011         726 LOAD_GLOBAL             16 (IS_FROZEN)
    # 738 POP_JUMP_FORWARD_IF_FALSE    26 (to 792)
    # 1012         740 LOAD_GLOBAL             45 (NULL + _show_fatal_error)
    # 1013         752 LOAD_CONST              20 ('TFstudio - 서버 시작 실패')
    # 1014         754 LOAD_CONST              21 ('내부 서버를 시작하지 못했습니다.\n\n원인: ')
    # 1015         756 LOAD_FAST                6 (error_str)
    # 1014         758 FORMAT_VALUE             0
    # 760 LOAD_CONST              22 ('\n\n해결 방법:\n1. 다른 프로그램이 포트를 사용 중인지 확인\n2. 프로그램을 재시작\n3. 문제 지속 시 로그 전달: %LOCALAPPDATA%\\TFstudio\\logs\\')
    # 762 BUILD_STRING             3
    # 1012         764 PRECALL                  2
    # 768 CALL                     2
    # 778 POP_TOP
    # 1021         780 POP_EXCEPT
    # 782 LOAD_CONST               2 (None)
    # 784 STORE_FAST               5 (e)
    # 786 DELETE_FAST              5 (e)
    # 788 LOAD_CONST               2 (None)
    # 790 RETURN_VALUE
    # 1022     >>  792 RAISE_VARARGS            0
    # >>  794 LOAD_CONST               2 (None)
    # 796 STORE_FAST               5 (e)
    # 798 DELETE_FAST              5 (e)
    # 800 RERAISE                  1
    # 1023     >>  802 LOAD_GLOBAL             46 (Exception)
    # 814 CHECK_EXC_MATCH
    # 816 POP_JUMP_FORWARD_IF_FALSE    99 (to 1016)
    # 818 STORE_FAST               5 (e)
    # 1024         820 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 832 LOAD_CONST              19 ('flask server start failed: ')
    # 834 LOAD_GLOBAL             49 (NULL + type)
    # 846 LOAD_FAST                5 (e)
    # 848 PRECALL                  1
    # 852 CALL                     1
    # 862 LOAD_ATTR               25 (__name__)
    # 872 FORMAT_VALUE             0
    # 874 LOAD_CONST              23 (': ')
    # 876 LOAD_FAST                5 (e)
    # 878 FORMAT_VALUE             0
    # 880 BUILD_STRING             4
    # 882 PRECALL                  1
    # 886 CALL                     1
    # 896 POP_TOP
    # 1025         898 LOAD_GLOBAL             16 (IS_FROZEN)
    # 910 POP_JUMP_FORWARD_IF_FALSE    47 (to 1006)
    # 1026         912 LOAD_GLOBAL             45 (NULL + _show_fatal_error)
    # 1027         924 LOAD_CONST              24 ('TFstudio - 서버 초기화 실패')
    # 1028         926 LOAD_CONST              25 ('내부 서버 초기화 중 오류가 발생했습니다.\n\n')
    # 1029         928 LOAD_GLOBAL             49 (NULL + type)
    # 940 LOAD_FAST                5 (e)
    # 942 PRECALL                  1
    # 946 CALL                     1
    # 956 LOAD_ATTR               25 (__name__)
    # 1028         966 FORMAT_VALUE             0
    # 968 LOAD_CONST              23 (': ')
    # 1029         970 LOAD_FAST                5 (e)
    # 1028         972 FORMAT_VALUE             0
    # 974 LOAD_CONST              26 ('\n\n로그 파일 위치: %LOCALAPPDATA%\\TFstudio\\logs\\')
    # 976 BUILD_STRING             5
    # 1026         978 PRECALL                  2
    # 982 CALL                     2
    # 992 POP_TOP
    # 1032         994 POP_EXCEPT
    # 996 LOAD_CONST               2 (None)
    # 998 STORE_FAST               5 (e)
    # 1000 DELETE_FAST              5 (e)
    # 1002 LOAD_CONST               2 (None)
    # 1004 RETURN_VALUE
    # 1033     >> 1006 RAISE_VARARGS            0
    # >> 1008 LOAD_CONST               2 (None)
    # 1010 STORE_FAST               5 (e)
    # 1012 DELETE_FAST              5 (e)
    # 1014 RERAISE                  1
    # 1034     >> 1016 LOAD_GLOBAL             52 (BaseException)
    # 1028 CHECK_EXC_MATCH
    # 1030 POP_JUMP_FORWARD_IF_FALSE    45 (to 1122)
    # 1032 STORE_FAST               5 (e)
    # 1036        1034 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 1046 LOAD_CONST              27 ('flask server start aborted: ')
    # 1048 LOAD_GLOBAL             49 (NULL + type)
    # 1060 LOAD_FAST                5 (e)
    # 1062 PRECALL                  1
    # 1066 CALL                     1
    # 1076 LOAD_ATTR               25 (__name__)
    # 1086 FORMAT_VALUE             0
    # 1088 LOAD_CONST              23 (': ')
    # 1090 LOAD_FAST                5 (e)
    # 1092 FORMAT_VALUE             0
    # 1094 BUILD_STRING             4
    # 1096 PRECALL                  1
    # 1100 CALL                     1
    # 1110 POP_TOP
    # 1037        1112 RAISE_VARARGS            0
    # >> 1114 LOAD_CONST               2 (None)
    # 1116 STORE_FAST               5 (e)
    # 1118 DELETE_FAST              5 (e)
    # 1120 RERAISE                  1
    # 1034     >> 1122 RERAISE                  0
    # >> 1124 COPY                     3
    # 1126 POP_EXCEPT
    # 1128 RERAISE                  1
    # 1038     >> 1130 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 1142 LOAD_CONST              28 ('flask server started on port ')
    # 1144 LOAD_FAST                4 (port)
    # 1146 FORMAT_VALUE             0
    # 1148 BUILD_STRING             2
    # 1150 PRECALL                  1
    # 1154 CALL                     1
    # 1164 POP_TOP
    # 1041        1166 LOAD_GLOBAL             55 (NULL + atexit)
    # 1178 LOAD_ATTR               28 (register)
    # 1188 LOAD_GLOBAL             58 (cleanup)
    # 1200 PRECALL                  1
    # 1204 CALL                     1
    # 1214 POP_TOP
    # 1042        1216 LOAD_GLOBAL             55 (NULL + atexit)
    # 1228 LOAD_ATTR               28 (register)
    # 1238 LOAD_DEREF              17 (server)
    # 1240 LOAD_ATTR               30 (stop)
    # 1250 PRECALL                  1
    # 1254 CALL                     1
    # 1264 POP_TOP
    # 1045        1266 LOAD_GLOBAL             63 (NULL + Api)
    # 1278 PRECALL                  0
    # 1282 CALL                     0
    # 1292 STORE_FAST               7 (api)
    # 1048        1294 LOAD_CLOSURE            18 (webview)
    # 1296 BUILD_TUPLE              1
    # 1298 LOAD_CONST              29 (<code object menu_reload at 0x000001EBD778B630, file "main.py", line 1048>)
    # 1300 MAKE_FUNCTION            8 (closure)
    # 1302 STORE_FAST               8 (menu_reload)
    # 1064        1304 LOAD_CLOSURE            18 (webview)
    # 1306 BUILD_TUPLE              1
    # 1308 LOAD_CONST              30 (<code object menu_devtools at 0x000001EBD778B2D0, file "main.py", line 1064>)
    # 1310 MAKE_FUNCTION            8 (closure)
    # 1312 STORE_FAST               9 (menu_devtools)
    # 1092        1314 LOAD_GLOBAL             16 (IS_FROZEN)
    # 1326 POP_JUMP_FORWARD_IF_FALSE    25 (to 1378)
    # 1095        1328 PUSH_NULL
    # 1330 LOAD_FAST                0 (Menu)
    # 1332 LOAD_CONST              31 ('도구')
    # 1096        1334 PUSH_NULL
    # 1336 LOAD_FAST                1 (MenuAction)
    # 1338 LOAD_CONST              32 ('새로고침 (F5)')
    # 1340 LOAD_FAST                8 (menu_reload)
    # 1342 PRECALL                  2
    # 1346 CALL                     2
    # 1095        1356 BUILD_LIST               1
    # 1358 PRECALL                  2
    # 1362 CALL                     2
    # 1094        1372 BUILD_LIST               1
    # 1374 STORE_FAST              10 (app_menu)
    # 1376 JUMP_FORWARD            44 (to 1466)
    # 1102     >> 1378 PUSH_NULL
    # 1380 LOAD_FAST                0 (Menu)
    # 1382 LOAD_CONST              31 ('도구')
    # 1103        1384 PUSH_NULL
    # 1386 LOAD_FAST                1 (MenuAction)
    # 1388 LOAD_CONST              32 ('새로고침 (F5)')
    # 1390 LOAD_FAST                8 (menu_reload)
    # 1392 PRECALL                  2
    # 1396 CALL                     2
    # 1104        1406 PUSH_NULL
    # 1408 LOAD_FAST                2 (MenuSeparator)
    # 1410 PRECALL                  0
    # 1414 CALL                     0
    # 1105        1424 PUSH_NULL
    # 1426 LOAD_FAST                1 (MenuAction)
    # 1428 LOAD_CONST              33 ('개발자 도구 (F12)')
    # 1430 LOAD_FAST                9 (menu_devtools)
    # 1432 PRECALL                  2
    # 1436 CALL                     2
    # 1102        1446 BUILD_LIST               3
    # 1448 PRECALL                  2
    # 1452 CALL                     2
    # 1101        1462 BUILD_LIST               1
    # 1464 STORE_FAST              10 (app_menu)
    # 1110     >> 1466 LOAD_DEREF              18 (webview)
    # 1468 LOAD_METHOD             32 (create_window)
    # 1111        1490 LOAD_DEREF              19 (window_title)
    # 1112        1492 LOAD_CONST              34 ('http://127.0.0.1:')
    # 1494 LOAD_FAST                4 (port)
    # 1496 FORMAT_VALUE             0
    # 1498 BUILD_STRING             2
    # 1113        1500 LOAD_CONST              35 (1600)
    # 1114        1502 LOAD_CONST              36 (900)
    # 1115        1504 LOAD_CONST              37 (True)
    # 1116        1506 LOAD_CONST              38 ((1200, 700))
    # 1117        1508 LOAD_CONST              39 ('#1a1d29')
    # 1118        1510 LOAD_CONST              37 (True)
    # 1119        1512 LOAD_FAST                7 (api)
    # 1110        1514 KW_NAMES                40
    # 1516 PRECALL                  9
    # 1520 CALL                     9
    # 1530 STORE_FAST              11 (window)
    # 1123        1532 LOAD_FAST               11 (window)
    # 1534 LOAD_FAST                7 (api)
    # 1536 STORE_ATTR              33 (_window)
    # 1125        1546 LOAD_CLOSURE            17 (server)
    # 1548 BUILD_TUPLE              1
    # 1550 LOAD_CONST              41 (<code object on_closing at 0x000001EBD77EC3F0, file "main.py", line 1125>)
    # 1552 MAKE_FUNCTION            8 (closure)
    # 1554 STORE_FAST              12 (on_closing)
    # 1132        1556 LOAD_FAST               11 (window)
    # 1558 LOAD_ATTR               34 (events)
    # 1568 COPY                     1
    # 1570 LOAD_ATTR               35 (closing)
    # 1580 LOAD_FAST               12 (on_closing)
    # 1582 BINARY_OP               13 (+=)
    # 1586 SWAP                     2
    # 1588 STORE_ATTR              35 (closing)
    # 1134        1598 LOAD_CLOSURE            19 (window_title)
    # 1600 BUILD_TUPLE              1
    # 1602 LOAD_CONST              42 (<code object on_shown at 0x000001EBD7326640, file "main.py", line 1134>)
    # 1604 MAKE_FUNCTION            8 (closure)
    # 1606 STORE_FAST              13 (on_shown)
    # 1146        1608 LOAD_FAST               11 (window)
    # 1610 LOAD_ATTR               34 (events)
    # 1620 COPY                     1
    # 1622 LOAD_ATTR               36 (shown)
    # 1632 LOAD_FAST               13 (on_shown)
    # 1634 BINARY_OP               13 (+=)
    # 1638 SWAP                     2
    # 1640 STORE_ATTR              36 (shown)
    # 1151        1650 LOAD_GLOBAL             75 (NULL + get_webview_cache_path)
    # 1662 PRECALL                  0
    # 1666 CALL                     0
    # 1676 STORE_FAST              14 (cache_path)
    # 1152        1678 LOAD_GLOBAL             30 (logger)
    # 1690 LOAD_METHOD             16 (info)
    # 1712 LOAD_CONST              43 ('WebView cache path: ')
    # 1714 LOAD_FAST               14 (cache_path)
    # 1716 FORMAT_VALUE             0
    # 1718 BUILD_STRING             2
    # 1720 PRECALL                  1
    # 1724 CALL                     1
    # 1734 POP_TOP
    # 1156        1736 LOAD_GLOBAL             16 (IS_FROZEN)
    # 1748 UNARY_NOT
    # 1750 STORE_FAST              15 (is_debug)
    # 1157        1752 LOAD_GLOBAL             30 (logger)
    # 1764 LOAD_METHOD             16 (info)
    # 1786 LOAD_CONST              44 ('Debug mode: ')
    # 1788 LOAD_FAST               15 (is_debug)
    # 1790 FORMAT_VALUE             0
    # 1792 BUILD_STRING             2
    # 1794 PRECALL                  1
    # 1798 CALL                     1
    # 1808 POP_TOP
    # 1160        1810 LOAD_FAST               10 (app_menu)
    # 1161        1812 LOAD_FAST               15 (is_debug)
    # 1162        1814 LOAD_FAST               14 (cache_path)
    # 1163        1816 LOAD_CONST               5 (False)
    # 1159        1818 LOAD_CONST              45 (('menu', 'debug', 'storage_path', 'private_mode'))
    # 1820 BUILD_CONST_KEY_MAP      4
    # 1822 STORE_FAST              16 (start_kwargs)
    # 1165        1824 LOAD_GLOBAL             18 (os)
    # 1836 LOAD_ATTR               38 (name)
    # 1846 LOAD_CONST              46 ('nt')
    # 1848 COMPARE_OP               2 (==)
    # 1854 POP_JUMP_FORWARD_IF_FALSE    31 (to 1918)
    # 1166        1856 LOAD_CONST              47 ('edgechromium')
    # 1858 LOAD_FAST               16 (start_kwargs)
    # 1860 LOAD_CONST              48 ('gui')
    # 1862 STORE_SUBSCR
    # 1167        1866 LOAD_GLOBAL             30 (logger)
    # 1878 LOAD_METHOD             16 (info)
    # 1900 LOAD_CONST              49 ('pywebview renderer forced: edgechromium')
    # 1902 PRECALL                  1
    # 1906 CALL                     1
    # 1916 POP_TOP
    # 1169     >> 1918 NOP
    # 1170        1920 PUSH_NULL
    # 1922 LOAD_DEREF              18 (webview)
    # 1924 LOAD_ATTR               19 (start)
    # 1934 LOAD_CONST              57 (())
    # 1936 BUILD_MAP                0
    # 1938 LOAD_FAST               16 (start_kwargs)
    # 1940 DICT_MERGE               1
    # 1942 CALL_FUNCTION_EX         1
    # 1944 POP_TOP
    # 1946 JUMP_FORWARD           141 (to 2230)
    # >> 1948 PUSH_EXC_INFO
    # 1171        1950 LOAD_GLOBAL             46 (Exception)
    # 1962 CHECK_EXC_MATCH
    # 1964 POP_JUMP_FORWARD_IF_FALSE   128 (to 2222)
    # 1966 STORE_FAST               5 (e)
    # 1172        1968 LOAD_GLOBAL              1 (NULL + _write_bootstrap_log)
    # 1980 LOAD_CONST              50 ('webview.start() failed: ')
    # 1982 LOAD_GLOBAL             49 (NULL + type)
    # 1994 LOAD_FAST                5 (e)
    # 1996 PRECALL                  1
    # 2000 CALL                     1
    # 2010 LOAD_ATTR               25 (__name__)
    # 2020 FORMAT_VALUE             0
    # 2022 LOAD_CONST              23 (': ')
    # 2024 LOAD_FAST                5 (e)
    # 2026 FORMAT_VALUE             0
    # 2028 BUILD_STRING             4
    # 2030 PRECALL                  1
    # 2034 CALL                     1
    # 2044 POP_TOP
    # 1173        2046 LOAD_GLOBAL             30 (logger)
    # 2058 LOAD_METHOD             39 (error)
    # 2080 LOAD_CONST              51 ('WebView startup failed: ')
    # 2082 LOAD_FAST                5 (e)
    # 2084 FORMAT_VALUE             0
    # 2086 BUILD_STRING             2
    # 2088 LOAD_CONST              37 (True)
    # 2090 KW_NAMES                52
    # 2092 PRECALL                  2
    # 2096 CALL                     2
    # 2106 POP_TOP
    # 1174        2108 LOAD_GLOBAL             16 (IS_FROZEN)
    # 2120 POP_JUMP_FORWARD_IF_FALSE    41 (to 2204)
    # 1175        2122 LOAD_GLOBAL             45 (NULL + _show_fatal_error)
    # 1176        2134 LOAD_CONST              53 ('TFstudio - UI 초기화 실패')
    # 1177        2136 LOAD_CONST              54 ('화면을 표시하지 못했습니다.\n\n원인: ')
    # 1178        2138 LOAD_GLOBAL             49 (NULL + type)
    # 2150 LOAD_FAST                5 (e)
    # 2152 PRECALL                  1
    # 2156 CALL                     1
    # 2166 LOAD_ATTR               25 (__name__)
    # 1177        2176 FORMAT_VALUE             0
    # 2178 LOAD_CONST              23 (': ')
    # 1178        2180 LOAD_FAST                5 (e)
    # 1177        2182 FORMAT_VALUE             0
    # 2184 LOAD_CONST              55 ('\n\n해결 방법:\n1. 프로그램을 재시작해주세요\n2. WebView2 런타임이 설치되어 있는지 확인\n3. 문제 지속 시 로그 전달: %LOCALAPPDATA%\\TFstudio\\logs\\')
    # 2186 BUILD_STRING             5
    # 1175        2188 PRECALL                  2
    # 2192 CALL                     2
    # 2202 POP_TOP
    # >> 2204 POP_EXCEPT
    # 2206 LOAD_CONST               2 (None)
    # 2208 STORE_FAST               5 (e)
    # 2210 DELETE_FAST              5 (e)
    # 2212 JUMP_FORWARD             8 (to 2230)
    # >> 2214 LOAD_CONST               2 (None)
    # 2216 STORE_FAST               5 (e)
    # 2218 DELETE_FAST              5 (e)
    # 2220 RERAISE                  1
    # 1171     >> 2222 RERAISE                  0
    # >> 2224 COPY                     3
    # 2226 POP_EXCEPT
    # 2228 RERAISE                  1
    # 1185     >> 2230 LOAD_GLOBAL             30 (logger)
    # 2242 LOAD_METHOD             16 (info)
    # 2264 LOAD_CONST              56 ('Application closed')
    # 2266 PRECALL                  1
    # 2270 CALL                     1
    # 2280 POP_TOP
    # 2282 LOAD_CONST               2 (None)
    # 2284 RETURN_VALUE
    # ExceptionTable:
    # 598 to 636 -> 640 [0]
    # 640 to 658 -> 1124 [1] lasti
    # 660 to 778 -> 794 [1] lasti
    # 792 to 792 -> 794 [1] lasti
    # 794 to 818 -> 1124 [1] lasti
    # 820 to 992 -> 1008 [1] lasti
    # 1006 to 1006 -> 1008 [1] lasti
    # 1008 to 1032 -> 1124 [1] lasti
    # 1034 to 1112 -> 1114 [1] lasti
    # 1114 to 1122 -> 1124 [1] lasti
    # 1920 to 1944 -> 1948 [0]
    # 1948 to 1966 -> 2224 [1] lasti
    # 1968 to 2202 -> 2214 [1] lasti
    # 2214 to 2222 -> 2224 [1] lasti
    # Disassembly of <code object menu_reload at 0x000001EBD778B630, file "main.py", line 1048>:
    # 0 COPY_FREE_VARS           1
    # 1048           2 RESUME                   0
    # 1050           4 LOAD_CLOSURE             1 (webview)
    # 6 BUILD_TUPLE              1
    # 8 LOAD_CONST               1 (<code object do_reload at 0x000001EBD7155FB0, file "main.py", line 1050>)
    # 10 MAKE_FUNCTION            8 (closure)
    # 12 STORE_FAST               0 (do_reload)
    # 1061          14 LOAD_GLOBAL              1 (NULL + threading)
    # 26 LOAD_ATTR                1 (Thread)
    # 36 LOAD_FAST                0 (do_reload)
    # 38 LOAD_CONST               2 (True)
    # 40 KW_NAMES                 3
    # 42 PRECALL                  2
    # 46 CALL                     2
    # 56 LOAD_METHOD              2 (start)
    # 78 PRECALL                  0
    # 82 CALL                     0
    # 92 POP_TOP
    # 94 LOAD_CONST               4 (None)
    # 96 RETURN_VALUE
    # Disassembly of <code object do_reload at 0x000001EBD7155FB0, file "main.py", line 1050>:
    # 0 COPY_FREE_VARS           1
    # 1050           2 RESUME                   0
    # 1051           4 LOAD_DEREF               2 (webview)
    # 6 LOAD_METHOD              0 (active_window)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 STORE_FAST               0 (win)
    # 1052          44 LOAD_FAST                0 (win)
    # 46 POP_JUMP_FORWARD_IF_FALSE   103 (to 254)
    # 1053          48 NOP
    # 1055          50 LOAD_FAST                0 (win)
    # 52 LOAD_METHOD              1 (evaluate_js)
    # 74 LOAD_CONST               1 ('window.location.reload()')
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 POP_TOP
    # 1056          92 LOAD_GLOBAL              4 (logger)
    # 104 LOAD_METHOD              3 (info)
    # 126 LOAD_CONST               2 ('Page reloaded via menu')
    # 128 PRECALL                  1
    # 132 CALL                     1
    # 142 POP_TOP
    # 144 LOAD_CONST               0 (None)
    # 146 RETURN_VALUE
    # >>  148 PUSH_EXC_INFO
    # 1057         150 LOAD_GLOBAL              8 (Exception)
    # 162 CHECK_EXC_MATCH
    # 164 POP_JUMP_FORWARD_IF_FALSE    40 (to 246)
    # 166 STORE_FAST               1 (e)
    # 1058         168 LOAD_GLOBAL              4 (logger)
    # 180 LOAD_METHOD              5 (error)
    # 202 LOAD_CONST               3 ('Failed to reload page: ')
    # 204 LOAD_FAST                1 (e)
    # 206 FORMAT_VALUE             0
    # 208 BUILD_STRING             2
    # 210 PRECALL                  1
    # 214 CALL                     1
    # 224 POP_TOP
    # 226 POP_EXCEPT
    # 228 LOAD_CONST               0 (None)
    # 230 STORE_FAST               1 (e)
    # 232 DELETE_FAST              1 (e)
    # 234 LOAD_CONST               0 (None)
    # 236 RETURN_VALUE
    # >>  238 LOAD_CONST               0 (None)
    # 240 STORE_FAST               1 (e)
    # 242 DELETE_FAST              1 (e)
    # 244 RERAISE                  1
    # 1057     >>  246 RERAISE                  0
    # >>  248 COPY                     3
    # 250 POP_EXCEPT
    # 252 RERAISE                  1
    # 1052     >>  254 LOAD_CONST               0 (None)
    # 256 RETURN_VALUE
    # ExceptionTable:
    # 50 to 142 -> 148 [0]
    # 148 to 166 -> 248 [1] lasti
    # 168 to 224 -> 238 [1] lasti
    # 238 to 246 -> 248 [1] lasti
    # Disassembly of <code object menu_devtools at 0x000001EBD778B2D0, file "main.py", line 1064>:
    # 0 COPY_FREE_VARS           1
    # 1064           2 RESUME                   0
    # 1066           4 LOAD_CLOSURE             1 (webview)
    # 6 BUILD_TUPLE              1
    # 8 LOAD_CONST               1 (<code object do_devtools at 0x000001EBD7634650, file "main.py", line 1066>)
    # 10 MAKE_FUNCTION            8 (closure)
    # 12 STORE_FAST               0 (do_devtools)
    # 1089          14 LOAD_GLOBAL              1 (NULL + threading)
    # 26 LOAD_ATTR                1 (Thread)
    # 36 LOAD_FAST                0 (do_devtools)
    # 38 LOAD_CONST               2 (True)
    # 40 KW_NAMES                 3
    # 42 PRECALL                  2
    # 46 CALL                     2
    # 56 LOAD_METHOD              2 (start)
    # 78 PRECALL                  0
    # 82 CALL                     0
    # 92 POP_TOP
    # 94 LOAD_CONST               4 (None)
    # 96 RETURN_VALUE
    # Disassembly of <code object do_devtools at 0x000001EBD7634650, file "main.py", line 1066>:
    # 0 COPY_FREE_VARS           1
    # 1066           2 RESUME                   0
    # 1067           4 LOAD_DEREF               5 (webview)
    # 6 LOAD_METHOD              0 (active_window)
    # 28 PRECALL                  0
    # 32 CALL                     0
    # 42 STORE_FAST               0 (win)
    # 1068          44 LOAD_FAST                0 (win)
    # 46 POP_JUMP_FORWARD_IF_TRUE    28 (to 104)
    # 1069          48 LOAD_GLOBAL              2 (logger)
    # 60 LOAD_METHOD              2 (warning)
    # 82 LOAD_CONST               1 ('No active window for devtools')
    # 84 PRECALL                  1
    # 88 CALL                     1
    # 98 POP_TOP
    # 1070         100 LOAD_CONST               0 (None)
    # 102 RETURN_VALUE
    # 1072     >>  104 NOP
    # 1074         106 LOAD_CONST               2 (0)
    # 108 LOAD_CONST               3 (('winforms',))
    # 110 IMPORT_NAME              3 (webview.platforms)
    # 112 IMPORT_FROM              4 (winforms)
    # 114 STORE_FAST               1 (winforms)
    # 116 POP_TOP
    # 1075         118 LOAD_FAST                1 (winforms)
    # 120 LOAD_ATTR                5 (BrowserView)
    # 130 LOAD_ATTR                6 (instances)
    # 140 LOAD_METHOD              7 (get)
    # 162 LOAD_FAST                0 (win)
    # 164 LOAD_ATTR                8 (uid)
    # 174 PRECALL                  1
    # 178 CALL                     1
    # 188 STORE_FAST               2 (browser_view)
    # 1076         190 LOAD_FAST                2 (browser_view)
    # 192 POP_JUMP_FORWARD_IF_FALSE   141 (to 476)
    # 194 LOAD_GLOBAL             19 (NULL + hasattr)
    # 206 LOAD_FAST                2 (browser_view)
    # 208 LOAD_CONST               4 ('browser')
    # 210 PRECALL                  2
    # 214 CALL                     2
    # 224 POP_JUMP_FORWARD_IF_FALSE   125 (to 476)
    # 226 LOAD_FAST                2 (browser_view)
    # 228 LOAD_ATTR               10 (browser)
    # 238 POP_JUMP_FORWARD_IF_FALSE   118 (to 476)
    # 1077         240 LOAD_FAST                2 (browser_view)
    # 242 LOAD_ATTR               10 (browser)
    # 252 LOAD_ATTR               11 (webview)
    # 262 STORE_FAST               3 (webview_ctrl)
    # 1078         264 LOAD_FAST                3 (webview_ctrl)
    # 266 POP_JUMP_FORWARD_IF_FALSE    76 (to 420)
    # 268 LOAD_GLOBAL             19 (NULL + hasattr)
    # 280 LOAD_FAST                3 (webview_ctrl)
    # 282 LOAD_CONST               5 ('CoreWebView2')
    # 284 PRECALL                  2
    # 288 CALL                     2
    # 298 POP_JUMP_FORWARD_IF_FALSE    60 (to 420)
    # 300 LOAD_FAST                3 (webview_ctrl)
    # 302 LOAD_ATTR               12 (CoreWebView2)
    # 312 POP_JUMP_FORWARD_IF_FALSE    53 (to 420)
    # 1079         314 LOAD_FAST                3 (webview_ctrl)
    # 316 LOAD_ATTR               12 (CoreWebView2)
    # 326 LOAD_METHOD             13 (OpenDevToolsWindow)
    # 348 PRECALL                  0
    # 352 CALL                     0
    # 362 POP_TOP
    # 1080         364 LOAD_GLOBAL              2 (logger)
    # 376 LOAD_METHOD             14 (info)
    # 398 LOAD_CONST               6 ('Developer tools opened via menu')
    # 400 PRECALL                  1
    # 404 CALL                     1
    # 414 POP_TOP
    # 416 LOAD_CONST               0 (None)
    # 418 RETURN_VALUE
    # 1082     >>  420 LOAD_GLOBAL              2 (logger)
    # 432 LOAD_METHOD              2 (warning)
    # 454 LOAD_CONST               7 ('CoreWebView2 not available for devtools')
    # 456 PRECALL                  1
    # 460 CALL                     1
    # 470 POP_TOP
    # 472 LOAD_CONST               0 (None)
    # 474 RETURN_VALUE
    # 1084     >>  476 LOAD_GLOBAL              2 (logger)
    # 488 LOAD_METHOD              2 (warning)
    # 510 LOAD_CONST               8 ('BrowserView not found for devtools')
    # 512 PRECALL                  1
    # 516 CALL                     1
    # 526 POP_TOP
    # 528 LOAD_CONST               0 (None)
    # 530 RETURN_VALUE
    # >>  532 PUSH_EXC_INFO
    # 1085         534 LOAD_GLOBAL             30 (Exception)
    # 546 CHECK_EXC_MATCH
    # 548 POP_JUMP_FORWARD_IF_FALSE    40 (to 630)
    # 550 STORE_FAST               4 (e)
    # 1086         552 LOAD_GLOBAL              2 (logger)
    # 564 LOAD_METHOD             16 (error)
    # 586 LOAD_CONST               9 ('Failed to open developer tools: ')
    # 588 LOAD_FAST                4 (e)
    # 590 FORMAT_VALUE             0
    # 592 BUILD_STRING             2
    # 594 PRECALL                  1
    # 598 CALL                     1
    # 608 POP_TOP
    # 610 POP_EXCEPT
    # 612 LOAD_CONST               0 (None)
    # 614 STORE_FAST               4 (e)
    # 616 DELETE_FAST              4 (e)
    # 618 LOAD_CONST               0 (None)
    # 620 RETURN_VALUE
    # >>  622 LOAD_CONST               0 (None)
    # 624 STORE_FAST               4 (e)
    # 626 DELETE_FAST              4 (e)
    # 628 RERAISE                  1
    # 1085     >>  630 RERAISE                  0
    # >>  632 COPY                     3
    # 634 POP_EXCEPT
    # 636 RERAISE                  1
    # ExceptionTable:
    # 106 to 414 -> 532 [0]
    # 420 to 470 -> 532 [0]
    # 476 to 526 -> 532 [0]
    # 532 to 550 -> 632 [1] lasti
    # 552 to 608 -> 622 [1] lasti
    # 622 to 630 -> 632 [1] lasti
    # Disassembly of <code object on_closing at 0x000001EBD77EC3F0, file "main.py", line 1125>:
    # 0 COPY_FREE_VARS           1
    # 1125           2 RESUME                   0
    # 1127           4 LOAD_GLOBAL              0 (logger)
    # 16 LOAD_METHOD              1 (info)
    # 38 LOAD_CONST               1 ('Window closing...')
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 POP_TOP
    # 1128          56 LOAD_DEREF               0 (server)
    # 58 LOAD_METHOD              2 (stop)
    # 80 PRECALL                  0
    # 84 CALL                     0
    # 94 POP_TOP
    # 1129          96 LOAD_GLOBAL              7 (NULL + cleanup)
    # 108 PRECALL                  0
    # 112 CALL                     0
    # 122 POP_TOP
    # 1130         124 LOAD_CONST               2 (True)
    # 126 RETURN_VALUE
    # Disassembly of <code object on_shown at 0x000001EBD7326640, file "main.py", line 1134>:
    # 0 COPY_FREE_VARS           1
    # 1134           2 RESUME                   0
    # 1136           4 LOAD_GLOBAL              0 (os)
    # 16 LOAD_ATTR                1 (name)
    # 26 LOAD_CONST               1 ('nt')
    # 28 COMPARE_OP               2 (==)
    # 34 POP_JUMP_FORWARD_IF_FALSE   116 (to 268)
    # 1137          36 LOAD_GLOBAL              5 (NULL + find_window_by_title)
    # 48 LOAD_DEREF               1 (window_title)
    # 50 PRECALL                  1
    # 54 CALL                     1
    # 64 STORE_FAST               0 (hwnd)
    # 1138          66 LOAD_FAST                0 (hwnd)
    # 68 POP_JUMP_FORWARD_IF_FALSE    71 (to 212)
    # 1139          70 LOAD_GLOBAL              7 (NULL + enable_dark_title_bar)
    # 82 LOAD_FAST                0 (hwnd)
    # 84 PRECALL                  1
    # 88 CALL                     1
    # 98 POP_JUMP_FORWARD_IF_FALSE    28 (to 156)
    # 1140         100 LOAD_GLOBAL              8 (logger)
    # 112 LOAD_METHOD              5 (info)
    # 134 LOAD_CONST               2 ('Dark title bar enabled successfully')
    # 136 PRECALL                  1
    # 140 CALL                     1
    # 150 POP_TOP
    # 152 LOAD_CONST               5 (None)
    # 154 RETURN_VALUE
    # 1142     >>  156 LOAD_GLOBAL              8 (logger)
    # 168 LOAD_METHOD              6 (warning)
    # 190 LOAD_CONST               3 ('Failed to enable dark title bar')
    # 192 PRECALL                  1
    # 196 CALL                     1
    # 206 POP_TOP
    # 208 LOAD_CONST               5 (None)
    # 210 RETURN_VALUE
    # 1144     >>  212 LOAD_GLOBAL              8 (logger)
    # 224 LOAD_METHOD              6 (warning)
    # 246 LOAD_CONST               4 ('Window handle not found for dark title bar')
    # 248 PRECALL                  1
    # 252 CALL                     1
    # 262 POP_TOP
    # 264 LOAD_CONST               5 (None)
    # 266 RETURN_VALUE
    # 1136     >>  268 LOAD_CONST               5 (None)
    # 270 RETURN_VALUE

def run_development():
    """Run in development mode (Flask dev server)"""
    # 1187           0 RESUME                   0
    # 1189           2 LOAD_GLOBAL              1 (NULL + setup_environment)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 POP_TOP
    # 1191          30 LOAD_CONST               1 (0)
    # 32 LOAD_CONST               2 (('create_app',))
    # 34 IMPORT_NAME              1 (app)
    # 36 IMPORT_FROM              2 (create_app)
    # 38 STORE_FAST               0 (create_app)
    # 40 POP_TOP
    # 1193          42 PUSH_NULL
    # 44 LOAD_FAST                0 (create_app)
    # 46 PRECALL                  0
    # 50 CALL                     0
    # 60 STORE_FAST               1 (app)
    # 1194          62 LOAD_FAST                1 (app)
    # 64 LOAD_METHOD              3 (run)
    # 86 LOAD_CONST               3 (True)
    # 88 LOAD_CONST               4 ('127.0.0.1')
    # 90 LOAD_CONST               5 (5000)
    # 92 KW_NAMES                 6
    # 94 PRECALL                  3
    # 98 CALL                     3
    # 108 POP_TOP
    # 110 LOAD_CONST               7 (None)
    # 112 RETURN_VALUE

def main():
    """Main entry point"""
    # 1196           0 RESUME                   0
    # 1199           2 LOAD_CONST               1 ('--dev')
    # 4 LOAD_GLOBAL              0 (sys)
    # 16 LOAD_ATTR                1 (argv)
    # 26 CONTAINS_OP              0
    # 28 POP_JUMP_FORWARD_IF_TRUE     7 (to 44)
    # 30 LOAD_GLOBAL              4 (IS_FROZEN)
    # 42 POP_JUMP_FORWARD_IF_TRUE    76 (to 196)
    # 1200     >>   44 LOAD_CONST               2 ('--webview')
    # 46 LOAD_GLOBAL              0 (sys)
    # 58 LOAD_ATTR                1 (argv)
    # 68 CONTAINS_OP              0
    # 70 POP_JUMP_FORWARD_IF_FALSE    16 (to 104)
    # 1202          72 LOAD_GLOBAL              7 (NULL + run_with_webview)
    # 84 PRECALL                  0
    # 88 CALL                     0
    # 98 POP_TOP
    # 100 LOAD_CONST               5 (None)
    # 102 RETURN_VALUE
    # 1205     >>  104 LOAD_GLOBAL              9 (NULL + print)
    # 116 LOAD_CONST               3 ("Development mode: Use 'start.bat' or 'python backend/run.py'")
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 POP_TOP
    # 1206         134 LOAD_GLOBAL              9 (NULL + print)
    # 146 LOAD_CONST               4 ('For webview mode: python main.py --webview')
    # 148 PRECALL                  1
    # 152 CALL                     1
    # 162 POP_TOP
    # 1207         164 LOAD_GLOBAL             11 (NULL + run_development)
    # 176 PRECALL                  0
    # 180 CALL                     0
    # 190 POP_TOP
    # 192 LOAD_CONST               5 (None)
    # 194 RETURN_VALUE
    # 1210     >>  196 LOAD_GLOBAL              7 (NULL + run_with_webview)
    # 208 PRECALL                  0
    # 212 CALL                     0
    # 222 POP_TOP
    # 224 LOAD_CONST               5 (None)
    # 226 RETURN_VALUE
