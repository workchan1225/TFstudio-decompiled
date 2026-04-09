# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: platform.py

""" This module tries to retrieve as much platform-identifying data as
    possible. It makes this information available via function APIs.

    If called from the command line, it prints the platform
    information concatenated as single string to stdout. The output
    format is usable as part of a filename.

"""

import collections
import os
import re
import sys
import functools
import itertools

def _comparable_version(version):
    # 141           0 RESUME                   0
    # 142           2 BUILD_LIST               0
    # 4 STORE_FAST               1 (result)
    # 143           6 LOAD_GLOBAL              0 (_component_re)
    # 18 LOAD_METHOD              1 (split)
    # 40 LOAD_FAST                0 (version)
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 56 GET_ITER
    # >>   58 FOR_ITER                92 (to 244)
    # 60 STORE_FAST               2 (v)
    # 144          62 LOAD_FAST                2 (v)
    # 64 LOAD_CONST               1 ('._+-')
    # 66 CONTAINS_OP              1
    # 68 POP_JUMP_FORWARD_IF_FALSE    86 (to 242)
    # 145          70 NOP
    # 146          72 LOAD_GLOBAL              5 (NULL + int)
    # 84 LOAD_FAST                2 (v)
    # 86 LOAD_CONST               2 (10)
    # 88 PRECALL                  2
    # 92 CALL                     2
    # 102 STORE_FAST               2 (v)
    # 147         104 LOAD_CONST               3 (100)
    # 106 STORE_FAST               3 (t)
    # 108 JUMP_FORWARD            43 (to 196)
    # >>  110 PUSH_EXC_INFO
    # 148         112 LOAD_GLOBAL              6 (ValueError)
    # 124 CHECK_EXC_MATCH
    # 126 POP_JUMP_FORWARD_IF_FALSE    30 (to 188)
    # 128 POP_TOP
    # 149         130 LOAD_GLOBAL              8 (_ver_stages)
    # 142 LOAD_METHOD              5 (get)
    # 164 LOAD_FAST                2 (v)
    # 166 LOAD_CONST               4 (0)
    # 168 PRECALL                  2
    # 172 CALL                     2
    # 182 STORE_FAST               3 (t)
    # 184 POP_EXCEPT
    # 186 JUMP_FORWARD             4 (to 196)
    # 148     >>  188 RERAISE                  0
    # >>  190 COPY                     3
    # 192 POP_EXCEPT
    # 194 RERAISE                  1
    # 150     >>  196 LOAD_FAST                1 (result)
    # 198 LOAD_METHOD              6 (extend)
    # 220 LOAD_FAST                3 (t)
    # 222 LOAD_FAST                2 (v)
    # 224 BUILD_TUPLE              2
    # 226 PRECALL                  1
    # 230 CALL                     1
    # 240 POP_TOP
    # >>  242 JUMP_BACKWARD           93 (to 58)
    # 151     >>  244 LOAD_FAST                1 (result)
    # 246 RETURN_VALUE
    # ExceptionTable:
    # 72 to 106 -> 110 [1]
    # 110 to 182 -> 190 [2] lasti
    # 188 to 188 -> 190 [2] lasti

def libc_ver(executable, lib, version, chunksize):
    """ Tries to determine the libc version that the file executable
        (which defaults to the Python interpreter) is linked against.

        Returns a tuple of strings (lib,version) which default to the
        given parameters in case the lookup fails.

        Note that the function has intimate knowledge of how different
        libc versions add symbols to the executable and thus is probably
        only usable for executables compiled using gcc.

        The file is read and scanned in chunks of chunksize bytes.

    """
    # 161           0 RESUME                   0
    # 176           2 LOAD_FAST                0 (executable)
    # 4 POP_JUMP_FORWARD_IF_TRUE   125 (to 256)
    # 177           6 NOP
    # 178           8 LOAD_GLOBAL              1 (NULL + os)
    # 20 LOAD_ATTR                1 (confstr)
    # 30 LOAD_CONST               1 ('CS_GNU_LIBC_VERSION')
    # 32 PRECALL                  1
    # 36 CALL                     1
    # 46 STORE_FAST               4 (ver)
    # 180          48 LOAD_FAST                4 (ver)
    # 50 LOAD_METHOD              2 (split)
    # 72 LOAD_CONST               2 (1)
    # 74 KW_NAMES                 3
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 STORE_FAST               5 (parts)
    # 181          92 LOAD_GLOBAL              7 (NULL + len)
    # 104 LOAD_FAST                5 (parts)
    # 106 PRECALL                  1
    # 110 CALL                     1
    # 120 LOAD_CONST               4 (2)
    # 122 COMPARE_OP               2 (==)
    # 128 POP_JUMP_FORWARD_IF_FALSE    15 (to 160)
    # 182         130 LOAD_GLOBAL              9 (NULL + tuple)
    # 142 LOAD_FAST                5 (parts)
    # 144 PRECALL                  1
    # 148 CALL                     1
    # 158 RETURN_VALUE
    # 181     >>  160 JUMP_FORWARD            29 (to 220)
    # >>  162 PUSH_EXC_INFO
    # 183         164 LOAD_GLOBAL             10 (AttributeError)
    # 176 LOAD_GLOBAL             12 (ValueError)
    # 188 LOAD_GLOBAL             14 (OSError)
    # 200 BUILD_TUPLE              3
    # 202 CHECK_EXC_MATCH
    # 204 POP_JUMP_FORWARD_IF_FALSE     3 (to 212)
    # 206 POP_TOP
    # 185         208 POP_EXCEPT
    # 210 JUMP_FORWARD             4 (to 220)
    # 183     >>  212 RERAISE                  0
    # >>  214 COPY                     3
    # 216 POP_EXCEPT
    # 218 RERAISE                  1
    # 187     >>  220 LOAD_GLOBAL             16 (sys)
    # 232 LOAD_ATTR                9 (executable)
    # 242 STORE_FAST               0 (executable)
    # 189         244 LOAD_FAST                0 (executable)
    # 246 POP_JUMP_FORWARD_IF_TRUE     4 (to 256)
    # 191         248 LOAD_FAST                1 (lib)
    # 250 LOAD_FAST                2 (version)
    # 252 BUILD_TUPLE              2
    # 254 RETURN_VALUE
    # 193     >>  256 LOAD_GLOBAL             20 (_comparable_version)
    # 268 STORE_FAST               6 (V)
    # 197         270 LOAD_GLOBAL              0 (os)
    # 282 LOAD_ATTR               11 (path)
    # 292 LOAD_METHOD             12 (realpath)
    # 314 LOAD_FAST                0 (executable)
    # 316 PRECALL                  1
    # 320 CALL                     1
    # 330 STORE_FAST               0 (executable)
    # 198         332 LOAD_GLOBAL             27 (NULL + open)
    # 344 LOAD_FAST                0 (executable)
    # 346 LOAD_CONST               5 ('rb')
    # 348 PRECALL                  2
    # 352 CALL                     2
    # 362 BEFORE_WITH
    # 364 STORE_FAST               7 (f)
    # 199         366 LOAD_FAST                7 (f)
    # 368 LOAD_METHOD             14 (read)
    # 390 LOAD_FAST                3 (chunksize)
    # 392 PRECALL                  1
    # 396 CALL                     1
    # 406 STORE_FAST               8 (binary)
    # 200         408 LOAD_CONST               6 (0)
    # 410 STORE_FAST               9 (pos)
    # 201     >>  412 LOAD_FAST                9 (pos)
    # 414 LOAD_GLOBAL              7 (NULL + len)
    # 426 LOAD_FAST                8 (binary)
    # 428 PRECALL                  1
    # 432 CALL                     1
    # 442 COMPARE_OP               0 (<)
    # 448 EXTENDED_ARG             1
    # 450 POP_JUMP_FORWARD_IF_FALSE   348 (to 1148)
    # 202     >>  452 LOAD_CONST               7 (b'libc')
    # 454 LOAD_FAST                8 (binary)
    # 456 CONTAINS_OP              0
    # 458 POP_JUMP_FORWARD_IF_TRUE     4 (to 468)
    # 460 LOAD_CONST               8 (b'GLIBC')
    # 462 LOAD_FAST                8 (binary)
    # 464 CONTAINS_OP              0
    # 466 POP_JUMP_FORWARD_IF_FALSE    28 (to 524)
    # 203     >>  468 LOAD_GLOBAL             30 (_libc_search)
    # 480 LOAD_METHOD             16 (search)
    # 502 LOAD_FAST                8 (binary)
    # 504 LOAD_FAST                9 (pos)
    # 506 PRECALL                  2
    # 510 CALL                     2
    # 520 STORE_FAST              10 (m)
    # 522 JUMP_FORWARD             2 (to 528)
    # 205     >>  524 LOAD_CONST               9 (None)
    # 526 STORE_FAST              10 (m)
    # 206     >>  528 LOAD_FAST               10 (m)
    # 530 POP_JUMP_FORWARD_IF_FALSE    37 (to 606)
    # 532 LOAD_FAST               10 (m)
    # 534 LOAD_METHOD             17 (end)
    # 556 PRECALL                  0
    # 560 CALL                     0
    # 570 LOAD_GLOBAL              7 (NULL + len)
    # 582 LOAD_FAST                8 (binary)
    # 584 PRECALL                  1
    # 588 CALL                     1
    # 598 COMPARE_OP               2 (==)
    # 604 POP_JUMP_FORWARD_IF_FALSE    72 (to 750)
    # 207     >>  606 LOAD_FAST                7 (f)
    # 608 LOAD_METHOD             14 (read)
    # 630 LOAD_FAST                3 (chunksize)
    # 632 PRECALL                  1
    # 636 CALL                     1
    # 646 STORE_FAST              11 (chunk)
    # 208         648 LOAD_FAST               11 (chunk)
    # 650 POP_JUMP_FORWARD_IF_FALSE    46 (to 744)
    # 209         652 LOAD_FAST                8 (binary)
    # 654 LOAD_GLOBAL             37 (NULL + max)
    # 666 LOAD_FAST                9 (pos)
    # 668 LOAD_GLOBAL              7 (NULL + len)
    # 680 LOAD_FAST                8 (binary)
    # 682 PRECALL                  1
    # 686 CALL                     1
    # 696 LOAD_CONST              10 (1000)
    # 698 BINARY_OP               10 (-)
    # 702 PRECALL                  2
    # 706 CALL                     2
    # 716 LOAD_CONST               9 (None)
    # 718 BUILD_SLICE              2
    # 720 BINARY_SUBSCR
    # 730 LOAD_FAST               11 (chunk)
    # 732 BINARY_OP                0 (+)
    # 736 STORE_FAST               8 (binary)
    # 210         738 LOAD_CONST               6 (0)
    # 740 STORE_FAST               9 (pos)
    # 211         742 JUMP_BACKWARD          166 (to 412)
    # 212     >>  744 LOAD_FAST               10 (m)
    # 746 POP_JUMP_FORWARD_IF_TRUE     1 (to 750)
    # 213         748 JUMP_FORWARD           199 (to 1148)
    # 214     >>  750 LOAD_CONST              11 (<code object <listcomp> at 0x000001EBD77FA630, file "platform.py", line 214>)
    # 752 MAKE_FUNCTION            0
    # 216         754 LOAD_FAST               10 (m)
    # 756 LOAD_METHOD             19 (groups)
    # 778 PRECALL                  0
    # 782 CALL                     0
    # 214         792 GET_ITER
    # 794 PRECALL                  0
    # 798 CALL                     0
    # 808 UNPACK_SEQUENCE          6
    # 812 STORE_FAST              12 (libcinit)
    # 814 STORE_FAST              13 (glibc)
    # 816 STORE_FAST              14 (glibcversion)
    # 818 STORE_FAST              15 (so)
    # 820 STORE_FAST              16 (threads)
    # 822 STORE_FAST              17 (soversion)
    # 217         824 LOAD_FAST               12 (libcinit)
    # 826 POP_JUMP_FORWARD_IF_FALSE     5 (to 838)
    # 828 LOAD_FAST                1 (lib)
    # 830 POP_JUMP_FORWARD_IF_TRUE     3 (to 838)
    # 218         832 LOAD_CONST              12 ('libc')
    # 834 STORE_FAST               1 (lib)
    # 836 JUMP_FORWARD           115 (to 1068)
    # 219     >>  838 LOAD_FAST               13 (glibc)
    # 840 POP_JUMP_FORWARD_IF_FALSE    38 (to 918)
    # 220         842 LOAD_FAST                1 (lib)
    # 844 LOAD_CONST              13 ('glibc')
    # 846 COMPARE_OP               3 (!=)
    # 852 POP_JUMP_FORWARD_IF_FALSE     5 (to 864)
    # 221         854 LOAD_CONST              13 ('glibc')
    # 856 STORE_FAST               1 (lib)
    # 222         858 LOAD_FAST               14 (glibcversion)
    # 860 STORE_FAST               2 (version)
    # 862 JUMP_FORWARD           102 (to 1068)
    # 223     >>  864 PUSH_NULL
    # 866 LOAD_FAST                6 (V)
    # 868 LOAD_FAST               14 (glibcversion)
    # 870 PRECALL                  1
    # 874 CALL                     1
    # 884 PUSH_NULL
    # 886 LOAD_FAST                6 (V)
    # 888 LOAD_FAST                2 (version)
    # 890 PRECALL                  1
    # 894 CALL                     1
    # 904 COMPARE_OP               4 (>)
    # 910 POP_JUMP_FORWARD_IF_FALSE     2 (to 916)
    # 224         912 LOAD_FAST               14 (glibcversion)
    # 914 STORE_FAST               2 (version)
    # >>  916 JUMP_FORWARD            75 (to 1068)
    # 225     >>  918 LOAD_FAST               15 (so)
    # 920 POP_JUMP_FORWARD_IF_FALSE    73 (to 1068)
    # 226         922 LOAD_FAST                1 (lib)
    # 924 LOAD_CONST              13 ('glibc')
    # 926 COMPARE_OP               3 (!=)
    # 932 POP_JUMP_FORWARD_IF_FALSE    67 (to 1068)
    # 227         934 LOAD_CONST              12 ('libc')
    # 936 STORE_FAST               1 (lib)
    # 228         938 LOAD_FAST               17 (soversion)
    # 940 POP_JUMP_FORWARD_IF_FALSE    28 (to 998)
    # 942 LOAD_FAST                2 (version)
    # 944 POP_JUMP_FORWARD_IF_FALSE    24 (to 994)
    # 946 PUSH_NULL
    # 948 LOAD_FAST                6 (V)
    # 950 LOAD_FAST               17 (soversion)
    # 952 PRECALL                  1
    # 956 CALL                     1
    # 966 PUSH_NULL
    # 968 LOAD_FAST                6 (V)
    # 970 LOAD_FAST                2 (version)
    # 972 PRECALL                  1
    # 976 CALL                     1
    # 986 COMPARE_OP               4 (>)
    # 992 POP_JUMP_FORWARD_IF_FALSE     2 (to 998)
    # 229     >>  994 LOAD_FAST               17 (soversion)
    # 996 STORE_FAST               2 (version)
    # 230     >>  998 LOAD_FAST               16 (threads)
    # 1000 POP_JUMP_FORWARD_IF_FALSE    33 (to 1068)
    # 1002 LOAD_FAST                2 (version)
    # 1004 LOAD_GLOBAL              7 (NULL + len)
    # 1016 LOAD_FAST               16 (threads)
    # 1018 PRECALL                  1
    # 1022 CALL                     1
    # 1032 UNARY_NEGATIVE
    # 1034 LOAD_CONST               9 (None)
    # 1036 BUILD_SLICE              2
    # 1038 BINARY_SUBSCR
    # 1048 LOAD_FAST               16 (threads)
    # 1050 COMPARE_OP               3 (!=)
    # 1056 POP_JUMP_FORWARD_IF_FALSE     5 (to 1068)
    # 231        1058 LOAD_FAST                2 (version)
    # 1060 LOAD_FAST               16 (threads)
    # 1062 BINARY_OP                0 (+)
    # 1066 STORE_FAST               2 (version)
    # 232     >> 1068 LOAD_FAST               10 (m)
    # 1070 LOAD_METHOD             17 (end)
    # 1092 PRECALL                  0
    # 1096 CALL                     0
    # 1106 STORE_FAST               9 (pos)
    # 201        1108 LOAD_FAST                9 (pos)
    # 1110 LOAD_GLOBAL              7 (NULL + len)
    # 1122 LOAD_FAST                8 (binary)
    # 1124 PRECALL                  1
    # 1128 CALL                     1
    # 1138 COMPARE_OP               0 (<)
    # 1144 EXTENDED_ARG             1
    # 1146 POP_JUMP_BACKWARD_IF_TRUE   348 (to 452)
    # 198     >> 1148 LOAD_CONST               9 (None)
    # 1150 LOAD_CONST               9 (None)
    # 1152 LOAD_CONST               9 (None)
    # 1154 PRECALL                  2
    # 1158 CALL                     2
    # 1168 POP_TOP
    # 1170 JUMP_FORWARD            11 (to 1194)
    # >> 1172 PUSH_EXC_INFO
    # 1174 WITH_EXCEPT_START
    # 1176 POP_JUMP_FORWARD_IF_TRUE     4 (to 1186)
    # 1178 RERAISE                  2
    # >> 1180 COPY                     3
    # 1182 POP_EXCEPT
    # 1184 RERAISE                  1
    # >> 1186 POP_TOP
    # 1188 POP_EXCEPT
    # 1190 POP_TOP
    # 1192 POP_TOP
    # 233     >> 1194 LOAD_FAST                1 (lib)
    # 1196 LOAD_FAST                2 (version)
    # 1198 BUILD_TUPLE              2
    # 1200 RETURN_VALUE
    # ExceptionTable:
    # 8 to 156 -> 162 [0]
    # 162 to 206 -> 214 [1] lasti
    # 212 to 212 -> 214 [1] lasti
    # 364 to 1146 -> 1172 [1] lasti
    # 1172 to 1178 -> 1180 [3] lasti
    # 1186 to 1186 -> 1180 [3] lasti
    # Disassembly of <code object <listcomp> at 0x000001EBD77FA630, file "platform.py", line 214>:
    # 214           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                27 (to 62)
    # 216           8 STORE_FAST               1 (s)
    # 215          10 LOAD_FAST                1 (s)
    # 12 POP_JUMP_FORWARD_IF_NONE    21 (to 56)
    # 14 LOAD_FAST                1 (s)
    # 16 LOAD_METHOD              0 (decode)
    # 38 LOAD_CONST               1 ('latin1')
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 JUMP_FORWARD             1 (to 58)
    # >>   56 LOAD_FAST                1 (s)
    # 214     >>   58 LIST_APPEND              2
    # 60 JUMP_BACKWARD           28 (to 6)
    # >>   62 RETURN_VALUE

def _norm_version(version, build):
    """ Normalize the version and build strings and return a single
        version string using the format major.minor.build (or patchlevel).
    """
    # 235           0 RESUME                   0
    # 240           2 LOAD_FAST                0 (version)
    # 4 LOAD_METHOD              0 (split)
    # 26 LOAD_CONST               1 ('.')
    # 28 PRECALL                  1
    # 32 CALL                     1
    # 42 STORE_FAST               2 (l)
    # 241          44 LOAD_FAST                1 (build)
    # 46 POP_JUMP_FORWARD_IF_FALSE    21 (to 90)
    # 242          48 LOAD_FAST                2 (l)
    # 50 LOAD_METHOD              1 (append)
    # 72 LOAD_FAST                1 (build)
    # 74 PRECALL                  1
    # 78 CALL                     1
    # 88 POP_TOP
    # 243     >>   90 NOP
    # 244          92 LOAD_GLOBAL              5 (NULL + list)
    # 104 LOAD_GLOBAL              7 (NULL + map)
    # 116 LOAD_GLOBAL              8 (str)
    # 128 LOAD_GLOBAL              7 (NULL + map)
    # 140 LOAD_GLOBAL             10 (int)
    # 152 LOAD_FAST                2 (l)
    # 154 PRECALL                  2
    # 158 CALL                     2
    # 168 PRECALL                  2
    # 172 CALL                     2
    # 182 PRECALL                  1
    # 186 CALL                     1
    # 196 STORE_FAST               3 (strings)
    # 198 JUMP_FORWARD            18 (to 236)
    # >>  200 PUSH_EXC_INFO
    # 245         202 LOAD_GLOBAL             12 (ValueError)
    # 214 CHECK_EXC_MATCH
    # 216 POP_JUMP_FORWARD_IF_FALSE     5 (to 228)
    # 218 POP_TOP
    # 246         220 LOAD_FAST                2 (l)
    # 222 STORE_FAST               3 (strings)
    # 224 POP_EXCEPT
    # 226 JUMP_FORWARD             4 (to 236)
    # 245     >>  228 RERAISE                  0
    # >>  230 COPY                     3
    # 232 POP_EXCEPT
    # 234 RERAISE                  1
    # 247     >>  236 LOAD_CONST               1 ('.')
    # 238 LOAD_METHOD              7 (join)
    # 260 LOAD_FAST                3 (strings)
    # 262 LOAD_CONST               2 (None)
    # 264 LOAD_CONST               3 (3)
    # 266 BUILD_SLICE              2
    # 268 BINARY_SUBSCR
    # 278 PRECALL                  1
    # 282 CALL                     1
    # 292 STORE_FAST               0 (version)
    # 248         294 LOAD_FAST                0 (version)
    # 296 RETURN_VALUE
    # ExceptionTable:
    # 92 to 196 -> 200 [0]
    # 200 to 222 -> 230 [1] lasti
    # 228 to 228 -> 230 [1] lasti

def _syscmd_ver(system, release, version, supported_platforms):
    """ Tries to figure out the OS version used and returns
        a tuple (system, release, version).

        It uses the "ver" shell command for this which is known
        to exists on Windows, DOS. XXX Others too ?

        In case this fails, the given parameters are used as
        defaults.

    """
    # 263           0 RESUME                   0
    # 277           2 LOAD_GLOBAL              0 (sys)
    # 14 LOAD_ATTR                1 (platform)
    # 24 LOAD_FAST                3 (supported_platforms)
    # 26 CONTAINS_OP              1
    # 28 POP_JUMP_FORWARD_IF_FALSE     5 (to 40)
    # 278          30 LOAD_FAST                0 (system)
    # 32 LOAD_FAST                1 (release)
    # 34 LOAD_FAST                2 (version)
    # 36 BUILD_TUPLE              3
    # 38 RETURN_VALUE
    # 281     >>   40 LOAD_CONST               1 (0)
    # 42 LOAD_CONST               2 (None)
    # 44 IMPORT_NAME              2 (subprocess)
    # 46 STORE_FAST               4 (subprocess)
    # 282          48 LOAD_CONST               3 (('ver', 'command /c ver', 'cmd /c ver'))
    # 50 GET_ITER
    # >>   52 FOR_ITER                71 (to 196)
    # 54 STORE_FAST               5 (cmd)
    # 283          56 NOP
    # 284          58 LOAD_FAST                4 (subprocess)
    # 60 LOAD_METHOD              3 (check_output)
    # 82 LOAD_FAST                5 (cmd)
    # 285          84 LOAD_FAST                4 (subprocess)
    # 86 LOAD_ATTR                4 (DEVNULL)
    # 286          96 LOAD_FAST                4 (subprocess)
    # 98 LOAD_ATTR                4 (DEVNULL)
    # 287         108 LOAD_CONST               4 (True)
    # 288         110 LOAD_CONST               5 ('locale')
    # 289         112 LOAD_CONST               4 (True)
    # 284         114 KW_NAMES                 6
    # 116 PRECALL                  6
    # 120 CALL                     6
    # 130 STORE_FAST               6 (info)
    # 294         132 POP_TOP
    # 134 JUMP_FORWARD            35 (to 206)
    # >>  136 PUSH_EXC_INFO
    # 290         138 LOAD_GLOBAL             10 (OSError)
    # 150 LOAD_FAST                4 (subprocess)
    # 152 LOAD_ATTR                6 (CalledProcessError)
    # 162 BUILD_TUPLE              2
    # 164 CHECK_EXC_MATCH
    # 166 POP_JUMP_FORWARD_IF_FALSE    10 (to 188)
    # 168 STORE_FAST               7 (why)
    # 292         170 POP_EXCEPT
    # 172 LOAD_CONST               2 (None)
    # 174 STORE_FAST               7 (why)
    # 176 DELETE_FAST              7 (why)
    # 178 JUMP_BACKWARD           64 (to 52)
    # 180 LOAD_CONST               2 (None)
    # 182 STORE_FAST               7 (why)
    # 184 DELETE_FAST              7 (why)
    # 186 RERAISE                  1
    # 290     >>  188 RERAISE                  0
    # >>  190 COPY                     3
    # 192 POP_EXCEPT
    # 194 RERAISE                  1
    # 296     >>  196 LOAD_FAST                0 (system)
    # 198 LOAD_FAST                1 (release)
    # 200 LOAD_FAST                2 (version)
    # 202 BUILD_TUPLE              3
    # 204 RETURN_VALUE
    # 299     >>  206 LOAD_FAST                6 (info)
    # 208 LOAD_METHOD              7 (strip)
    # 230 PRECALL                  0
    # 234 CALL                     0
    # 244 STORE_FAST               6 (info)
    # 300         246 LOAD_GLOBAL             16 (_ver_output)
    # 258 LOAD_METHOD              9 (match)
    # 280 LOAD_FAST                6 (info)
    # 282 PRECALL                  1
    # 286 CALL                     1
    # 296 STORE_FAST               8 (m)
    # 301         298 LOAD_FAST                8 (m)
    # 300 POP_JUMP_FORWARD_IF_NONE    83 (to 468)
    # 302         302 LOAD_FAST                8 (m)
    # 304 LOAD_METHOD             10 (groups)
    # 326 PRECALL                  0
    # 330 CALL                     0
    # 340 UNPACK_SEQUENCE          3
    # 344 STORE_FAST               0 (system)
    # 346 STORE_FAST               1 (release)
    # 348 STORE_FAST               2 (version)
    # 304         350 LOAD_FAST                1 (release)
    # 352 LOAD_CONST               7 (-1)
    # 354 BINARY_SUBSCR
    # 364 LOAD_CONST               8 ('.')
    # 366 COMPARE_OP               2 (==)
    # 372 POP_JUMP_FORWARD_IF_FALSE    10 (to 394)
    # 305         374 LOAD_FAST                1 (release)
    # 376 LOAD_CONST               2 (None)
    # 378 LOAD_CONST               7 (-1)
    # 380 BUILD_SLICE              2
    # 382 BINARY_SUBSCR
    # 392 STORE_FAST               1 (release)
    # 306     >>  394 LOAD_FAST                2 (version)
    # 396 LOAD_CONST               7 (-1)
    # 398 BINARY_SUBSCR
    # 408 LOAD_CONST               8 ('.')
    # 410 COMPARE_OP               2 (==)
    # 416 POP_JUMP_FORWARD_IF_FALSE    10 (to 438)
    # 307         418 LOAD_FAST                2 (version)
    # 420 LOAD_CONST               2 (None)
    # 422 LOAD_CONST               7 (-1)
    # 424 BUILD_SLICE              2
    # 426 BINARY_SUBSCR
    # 436 STORE_FAST               2 (version)
    # 310     >>  438 LOAD_GLOBAL             23 (NULL + _norm_version)
    # 450 LOAD_FAST                2 (version)
    # 452 PRECALL                  1
    # 456 CALL                     1
    # 466 STORE_FAST               2 (version)
    # 311     >>  468 LOAD_FAST                0 (system)
    # 470 LOAD_FAST                1 (release)
    # 472 LOAD_FAST                2 (version)
    # 474 BUILD_TUPLE              3
    # 476 RETURN_VALUE
    # ExceptionTable:
    # 58 to 130 -> 136 [1]
    # 136 to 168 -> 190 [2] lasti
    # 180 to 188 -> 190 [2] lasti

def win32_is_iot():
    # 342           0 RESUME                   0
    # 343           2 LOAD_GLOBAL              1 (NULL + win32_edition)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (('IoTUAP', 'NanoServer', 'WindowsCoreHeadless', 'IoTEdgeOS'))
    # 30 CONTAINS_OP              0
    # 32 RETURN_VALUE

def win32_edition():
    # 345           0 RESUME                   0
    # 346           2 NOP
    # 347           4 NOP
    # 348           6 LOAD_CONST               1 (0)
    # 8 LOAD_CONST               0 (None)
    # 10 IMPORT_NAME              0 (winreg)
    # 12 STORE_FAST               0 (winreg)
    # 14 JUMP_FORWARD            20 (to 56)
    # >>   16 PUSH_EXC_INFO
    # 349          18 LOAD_GLOBAL              2 (ImportError)
    # 30 CHECK_EXC_MATCH
    # 32 POP_JUMP_FORWARD_IF_FALSE     7 (to 48)
    # 34 POP_TOP
    # 350          36 LOAD_CONST               1 (0)
    # 38 LOAD_CONST               0 (None)
    # 40 IMPORT_NAME              2 (_winreg)
    # 42 STORE_FAST               0 (winreg)
    # 44 POP_EXCEPT
    # 46 JUMP_FORWARD             4 (to 56)
    # 349     >>   48 RERAISE                  0
    # >>   50 COPY                     3
    # 52 POP_EXCEPT
    # 54 RERAISE                  1
    # 354     >>   56 NOP
    # 355          58 LOAD_CONST               2 ('SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion')
    # 60 STORE_FAST               1 (cvkey)
    # 356          62 LOAD_FAST                0 (winreg)
    # 64 LOAD_METHOD              3 (OpenKeyEx)
    # 86 LOAD_FAST                0 (winreg)
    # 88 LOAD_ATTR                4 (HKEY_LOCAL_MACHINE)
    # 98 LOAD_FAST                1 (cvkey)
    # 100 PRECALL                  2
    # 104 CALL                     2
    # 114 BEFORE_WITH
    # 116 STORE_FAST               2 (key)
    # 357         118 LOAD_FAST                0 (winreg)
    # 120 LOAD_METHOD              5 (QueryValueEx)
    # 142 LOAD_FAST                2 (key)
    # 144 LOAD_CONST               3 ('EditionId')
    # 146 PRECALL                  2
    # 150 CALL                     2
    # 160 LOAD_CONST               1 (0)
    # 162 BINARY_SUBSCR
    # 356         172 SWAP                     2
    # 174 LOAD_CONST               0 (None)
    # 176 LOAD_CONST               0 (None)
    # 178 LOAD_CONST               0 (None)
    # 180 PRECALL                  2
    # 184 CALL                     2
    # 194 POP_TOP
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
    # 220 JUMP_FORWARD            32 (to 286)
    # >>  222 PUSH_EXC_INFO
    # 358         224 LOAD_GLOBAL             12 (OSError)
    # 236 CHECK_EXC_MATCH
    # 238 POP_JUMP_FORWARD_IF_FALSE     3 (to 246)
    # 240 POP_TOP
    # 359         242 POP_EXCEPT
    # 244 JUMP_FORWARD            20 (to 286)
    # 358     >>  246 RERAISE                  0
    # >>  248 COPY                     3
    # 250 POP_EXCEPT
    # 252 RERAISE                  1
    # >>  254 PUSH_EXC_INFO
    # 351         256 LOAD_GLOBAL              2 (ImportError)
    # 268 CHECK_EXC_MATCH
    # 270 POP_JUMP_FORWARD_IF_FALSE     3 (to 278)
    # 272 POP_TOP
    # 352         274 POP_EXCEPT
    # 276 JUMP_FORWARD             4 (to 286)
    # 351     >>  278 RERAISE                  0
    # >>  280 COPY                     3
    # 282 POP_EXCEPT
    # 284 RERAISE                  1
    # 361     >>  286 LOAD_CONST               0 (None)
    # 288 RETURN_VALUE
    # ExceptionTable:
    # 6 to 12 -> 16 [0]
    # 14 to 14 -> 254 [0]
    # 16 to 42 -> 50 [1] lasti
    # 44 to 46 -> 254 [0]
    # 48 to 48 -> 50 [1] lasti
    # 50 to 54 -> 254 [0]
    # 58 to 114 -> 222 [0]
    # 116 to 170 -> 198 [1] lasti
    # 172 to 194 -> 222 [0]
    # 198 to 204 -> 206 [3] lasti
    # 206 to 210 -> 222 [0]
    # 212 to 212 -> 206 [3] lasti
    # 214 to 218 -> 222 [0]
    # 222 to 240 -> 248 [1] lasti
    # 246 to 246 -> 248 [1] lasti
    # 254 to 272 -> 280 [1] lasti
    # 278 to 278 -> 280 [1] lasti

def win32_ver(release, version, csd, ptype):
    # 363           0 RESUME                   0
    # 364           2 NOP
    # 365           4 LOAD_CONST               1 (0)
    # 6 LOAD_CONST               2 (('getwindowsversion',))
    # 8 IMPORT_NAME              0 (sys)
    # 10 IMPORT_FROM              1 (getwindowsversion)
    # 12 STORE_FAST               4 (getwindowsversion)
    # 14 POP_TOP
    # 16 JUMP_FORWARD            22 (to 62)
    # >>   18 PUSH_EXC_INFO
    # 366          20 LOAD_GLOBAL              4 (ImportError)
    # 32 CHECK_EXC_MATCH
    # 34 POP_JUMP_FORWARD_IF_FALSE     9 (to 54)
    # 36 POP_TOP
    # 367          38 LOAD_FAST                0 (release)
    # 40 LOAD_FAST                1 (version)
    # 42 LOAD_FAST                2 (csd)
    # 44 LOAD_FAST                3 (ptype)
    # 46 BUILD_TUPLE              4
    # 48 SWAP                     2
    # 50 POP_EXCEPT
    # 52 RETURN_VALUE
    # 366     >>   54 RERAISE                  0
    # >>   56 COPY                     3
    # 58 POP_EXCEPT
    # 60 RERAISE                  1
    # 369     >>   62 PUSH_NULL
    # 64 LOAD_FAST                4 (getwindowsversion)
    # 66 PRECALL                  0
    # 70 CALL                     0
    # 80 STORE_FAST               5 (winver)
    # 370          82 NOP
    # 371          84 LOAD_GLOBAL              7 (NULL + map)
    # 96 LOAD_GLOBAL              8 (int)
    # 108 LOAD_GLOBAL             11 (NULL + _syscmd_ver)
    # 120 PRECALL                  0
    # 124 CALL                     0
    # 134 LOAD_CONST               3 (2)
    # 136 BINARY_SUBSCR
    # 146 LOAD_METHOD              6 (split)
    # 168 LOAD_CONST               4 ('.')
    # 170 PRECALL                  1
    # 174 CALL                     1
    # 184 PRECALL                  2
    # 188 CALL                     2
    # 198 UNPACK_SEQUENCE          3
    # 202 STORE_FAST               6 (major)
    # 204 STORE_FAST               7 (minor)
    # 206 STORE_FAST               8 (build)
    # 208 JUMP_FORWARD            37 (to 284)
    # >>  210 PUSH_EXC_INFO
    # 372         212 LOAD_GLOBAL             14 (ValueError)
    # 224 CHECK_EXC_MATCH
    # 226 POP_JUMP_FORWARD_IF_FALSE    24 (to 276)
    # 228 POP_TOP
    # 373         230 LOAD_FAST                5 (winver)
    # 232 LOAD_ATTR                8 (platform_version)
    # 242 JUMP_IF_TRUE_OR_POP      9 (to 262)
    # 244 LOAD_FAST                5 (winver)
    # 246 LOAD_CONST               0 (None)
    # 248 LOAD_CONST               5 (3)
    # 250 BUILD_SLICE              2
    # 252 BINARY_SUBSCR
    # >>  262 UNPACK_SEQUENCE          3
    # 266 STORE_FAST               6 (major)
    # 268 STORE_FAST               7 (minor)
    # 270 STORE_FAST               8 (build)
    # 272 POP_EXCEPT
    # 274 JUMP_FORWARD             4 (to 284)
    # 372     >>  276 RERAISE                  0
    # >>  278 COPY                     3
    # 280 POP_EXCEPT
    # 282 RERAISE                  1
    # 374     >>  284 LOAD_CONST               6 ('{0}.{1}.{2}')
    # 286 LOAD_METHOD              9 (format)
    # 308 LOAD_FAST                6 (major)
    # 310 LOAD_FAST                7 (minor)
    # 312 LOAD_FAST                8 (build)
    # 314 PRECALL                  3
    # 318 CALL                     3
    # 328 STORE_FAST               1 (version)
    # 376         330 LOAD_GLOBAL             20 (_WIN32_CLIENT_RELEASES)
    # 342 LOAD_METHOD             11 (get)
    # 364 LOAD_FAST                6 (major)
    # 366 LOAD_FAST                7 (minor)
    # 368 BUILD_TUPLE              2
    # 370 PRECALL                  1
    # 374 CALL                     1
    # 384 JUMP_IF_TRUE_OR_POP     29 (to 444)
    # 377         386 LOAD_GLOBAL             20 (_WIN32_CLIENT_RELEASES)
    # 398 LOAD_METHOD             11 (get)
    # 420 LOAD_FAST                6 (major)
    # 422 LOAD_CONST               0 (None)
    # 424 BUILD_TUPLE              2
    # 426 PRECALL                  1
    # 430 CALL                     1
    # 376         440 JUMP_IF_TRUE_OR_POP      1 (to 444)
    # 378         442 LOAD_FAST                0 (release)
    # 376     >>  444 STORE_FAST               0 (release)
    # 383         446 LOAD_FAST                5 (winver)
    # 448 LOAD_CONST               0 (None)
    # 450 LOAD_CONST               3 (2)
    # 452 BUILD_SLICE              2
    # 454 BINARY_SUBSCR
    # 464 LOAD_FAST                6 (major)
    # 466 LOAD_FAST                7 (minor)
    # 468 BUILD_TUPLE              2
    # 470 COMPARE_OP               2 (==)
    # 476 POP_JUMP_FORWARD_IF_FALSE    71 (to 620)
    # 384         478 NOP
    # 385         480 LOAD_CONST               7 ('SP{}')
    # 482 LOAD_METHOD              9 (format)
    # 504 LOAD_FAST                5 (winver)
    # 506 LOAD_ATTR               12 (service_pack_major)
    # 516 PRECALL                  1
    # 520 CALL                     1
    # 530 STORE_FAST               2 (csd)
    # 532 JUMP_FORWARD            43 (to 620)
    # >>  534 PUSH_EXC_INFO
    # 386         536 LOAD_GLOBAL             26 (AttributeError)
    # 548 CHECK_EXC_MATCH
    # 550 POP_JUMP_FORWARD_IF_FALSE    30 (to 612)
    # 552 POP_TOP
    # 387         554 LOAD_FAST                2 (csd)
    # 556 LOAD_CONST               0 (None)
    # 558 LOAD_CONST               8 (13)
    # 560 BUILD_SLICE              2
    # 562 BINARY_SUBSCR
    # 572 LOAD_CONST               9 ('Service Pack ')
    # 574 COMPARE_OP               2 (==)
    # 580 POP_JUMP_FORWARD_IF_FALSE    13 (to 608)
    # 388         582 LOAD_CONST              10 ('SP')
    # 584 LOAD_FAST                2 (csd)
    # 586 LOAD_CONST               8 (13)
    # 588 LOAD_CONST               0 (None)
    # 590 BUILD_SLICE              2
    # 592 BINARY_SUBSCR
    # 602 BINARY_OP                0 (+)
    # 606 STORE_FAST               2 (csd)
    # >>  608 POP_EXCEPT
    # 610 JUMP_FORWARD             4 (to 620)
    # 386     >>  612 RERAISE                  0
    # >>  614 COPY                     3
    # 616 POP_EXCEPT
    # 618 RERAISE                  1
    # 391     >>  620 LOAD_GLOBAL             29 (NULL + getattr)
    # 632 LOAD_FAST                5 (winver)
    # 634 LOAD_CONST              11 ('product_type')
    # 636 LOAD_CONST               0 (None)
    # 638 PRECALL                  3
    # 642 CALL                     3
    # 652 LOAD_CONST               5 (3)
    # 654 COMPARE_OP               2 (==)
    # 660 POP_JUMP_FORWARD_IF_FALSE    58 (to 778)
    # 392         662 LOAD_GLOBAL             30 (_WIN32_SERVER_RELEASES)
    # 674 LOAD_METHOD             11 (get)
    # 696 LOAD_FAST                6 (major)
    # 698 LOAD_FAST                7 (minor)
    # 700 BUILD_TUPLE              2
    # 702 PRECALL                  1
    # 706 CALL                     1
    # 716 JUMP_IF_TRUE_OR_POP     29 (to 776)
    # 393         718 LOAD_GLOBAL             30 (_WIN32_SERVER_RELEASES)
    # 730 LOAD_METHOD             11 (get)
    # 752 LOAD_FAST                6 (major)
    # 754 LOAD_CONST               0 (None)
    # 756 BUILD_TUPLE              2
    # 758 PRECALL                  1
    # 762 CALL                     1
    # 392         772 JUMP_IF_TRUE_OR_POP      1 (to 776)
    # 394         774 LOAD_FAST                0 (release)
    # 392     >>  776 STORE_FAST               0 (release)
    # 396     >>  778 NOP
    # 397         780 NOP
    # 398         782 LOAD_CONST               1 (0)
    # 784 LOAD_CONST               0 (None)
    # 786 IMPORT_NAME             16 (winreg)
    # 788 STORE_FAST               9 (winreg)
    # 790 JUMP_FORWARD            20 (to 832)
    # >>  792 PUSH_EXC_INFO
    # 399         794 LOAD_GLOBAL              4 (ImportError)
    # 806 CHECK_EXC_MATCH
    # 808 POP_JUMP_FORWARD_IF_FALSE     7 (to 824)
    # 810 POP_TOP
    # 400         812 LOAD_CONST               1 (0)
    # 814 LOAD_CONST               0 (None)
    # 816 IMPORT_NAME             17 (_winreg)
    # 818 STORE_FAST               9 (winreg)
    # 820 POP_EXCEPT
    # 822 JUMP_FORWARD             4 (to 832)
    # 399     >>  824 RERAISE                  0
    # >>  826 COPY                     3
    # 828 POP_EXCEPT
    # 830 RERAISE                  1
    # 404     >>  832 NOP
    # 405         834 LOAD_CONST              12 ('SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion')
    # 836 STORE_FAST              10 (cvkey)
    # 406         838 LOAD_FAST                9 (winreg)
    # 840 LOAD_METHOD             18 (OpenKeyEx)
    # 862 LOAD_FAST                9 (winreg)
    # 864 LOAD_ATTR               19 (HKEY_LOCAL_MACHINE)
    # 874 LOAD_FAST               10 (cvkey)
    # 876 PRECALL                  2
    # 880 CALL                     2
    # 890 BEFORE_WITH
    # 892 STORE_FAST              11 (key)
    # 407         894 LOAD_FAST                9 (winreg)
    # 896 LOAD_METHOD             20 (QueryValueEx)
    # 918 LOAD_FAST               11 (key)
    # 920 LOAD_CONST              13 ('CurrentType')
    # 922 PRECALL                  2
    # 926 CALL                     2
    # 936 LOAD_CONST               1 (0)
    # 938 BINARY_SUBSCR
    # 948 STORE_FAST               3 (ptype)
    # 406         950 LOAD_CONST               0 (None)
    # 952 LOAD_CONST               0 (None)
    # 954 LOAD_CONST               0 (None)
    # 956 PRECALL                  2
    # 960 CALL                     2
    # 970 POP_TOP
    # 972 JUMP_FORWARD            11 (to 996)
    # >>  974 PUSH_EXC_INFO
    # 976 WITH_EXCEPT_START
    # 978 POP_JUMP_FORWARD_IF_TRUE     4 (to 988)
    # 980 RERAISE                  2
    # >>  982 COPY                     3
    # 984 POP_EXCEPT
    # 986 RERAISE                  1
    # >>  988 POP_TOP
    # 990 POP_EXCEPT
    # 992 POP_TOP
    # 994 POP_TOP
    # >>  996 JUMP_FORWARD            32 (to 1062)
    # >>  998 PUSH_EXC_INFO
    # 408        1000 LOAD_GLOBAL             42 (OSError)
    # 1012 CHECK_EXC_MATCH
    # 1014 POP_JUMP_FORWARD_IF_FALSE     3 (to 1022)
    # 1016 POP_TOP
    # 409        1018 POP_EXCEPT
    # 1020 JUMP_FORWARD            20 (to 1062)
    # 408     >> 1022 RERAISE                  0
    # >> 1024 COPY                     3
    # 1026 POP_EXCEPT
    # 1028 RERAISE                  1
    # >> 1030 PUSH_EXC_INFO
    # 401        1032 LOAD_GLOBAL              4 (ImportError)
    # 1044 CHECK_EXC_MATCH
    # 1046 POP_JUMP_FORWARD_IF_FALSE     3 (to 1054)
    # 1048 POP_TOP
    # 402        1050 POP_EXCEPT
    # 1052 JUMP_FORWARD             4 (to 1062)
    # 401     >> 1054 RERAISE                  0
    # >> 1056 COPY                     3
    # 1058 POP_EXCEPT
    # 1060 RERAISE                  1
    # 411     >> 1062 LOAD_FAST                0 (release)
    # 1064 LOAD_FAST                1 (version)
    # 1066 LOAD_FAST                2 (csd)
    # 1068 LOAD_FAST                3 (ptype)
    # 1070 BUILD_TUPLE              4
    # 1072 RETURN_VALUE
    # ExceptionTable:
    # 4 to 14 -> 18 [0]
    # 18 to 48 -> 56 [1] lasti
    # 54 to 54 -> 56 [1] lasti
    # 84 to 206 -> 210 [0]
    # 210 to 270 -> 278 [1] lasti
    # 276 to 276 -> 278 [1] lasti
    # 480 to 530 -> 534 [0]
    # 534 to 606 -> 614 [1] lasti
    # 612 to 612 -> 614 [1] lasti
    # 782 to 788 -> 792 [0]
    # 790 to 790 -> 1030 [0]
    # 792 to 818 -> 826 [1] lasti
    # 820 to 822 -> 1030 [0]
    # 824 to 824 -> 826 [1] lasti
    # 826 to 830 -> 1030 [0]
    # 834 to 890 -> 998 [0]
    # 892 to 948 -> 974 [1] lasti
    # 950 to 972 -> 998 [0]
    # 974 to 980 -> 982 [3] lasti
    # 982 to 986 -> 998 [0]
    # 988 to 988 -> 982 [3] lasti
    # 990 to 994 -> 998 [0]
    # 998 to 1016 -> 1024 [1] lasti
    # 1022 to 1022 -> 1024 [1] lasti
    # 1030 to 1048 -> 1056 [1] lasti
    # 1054 to 1054 -> 1056 [1] lasti

def _mac_ver_xml():
    # 414           0 RESUME                   0
    # 415           2 LOAD_CONST               1 ('/System/Library/CoreServices/SystemVersion.plist')
    # 4 STORE_FAST               0 (fn)
    # 416           6 LOAD_GLOBAL              0 (os)
    # 18 LOAD_ATTR                1 (path)
    # 28 LOAD_METHOD              2 (exists)
    # 50 LOAD_FAST                0 (fn)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 POP_JUMP_FORWARD_IF_TRUE     2 (to 72)
    # 417          68 LOAD_CONST               0 (None)
    # 70 RETURN_VALUE
    # 419     >>   72 NOP
    # 420          74 LOAD_CONST               2 (0)
    # 76 LOAD_CONST               0 (None)
    # 78 IMPORT_NAME              3 (plistlib)
    # 80 STORE_FAST               1 (plistlib)
    # 82 JUMP_FORWARD            17 (to 118)
    # >>   84 PUSH_EXC_INFO
    # 421          86 LOAD_GLOBAL              8 (ImportError)
    # 98 CHECK_EXC_MATCH
    # 100 POP_JUMP_FORWARD_IF_FALSE     4 (to 110)
    # 102 POP_TOP
    # 422         104 POP_EXCEPT
    # 106 LOAD_CONST               0 (None)
    # 108 RETURN_VALUE
    # 421     >>  110 RERAISE                  0
    # >>  112 COPY                     3
    # 114 POP_EXCEPT
    # 116 RERAISE                  1
    # 424     >>  118 LOAD_GLOBAL             11 (NULL + open)
    # 130 LOAD_FAST                0 (fn)
    # 132 LOAD_CONST               3 ('rb')
    # 134 PRECALL                  2
    # 138 CALL                     2
    # 148 BEFORE_WITH
    # 150 STORE_FAST               2 (f)
    # 425         152 LOAD_FAST                1 (plistlib)
    # 154 LOAD_METHOD              6 (load)
    # 176 LOAD_FAST                2 (f)
    # 178 PRECALL                  1
    # 182 CALL                     1
    # 192 STORE_FAST               3 (pl)
    # 424         194 LOAD_CONST               0 (None)
    # 196 LOAD_CONST               0 (None)
    # 198 LOAD_CONST               0 (None)
    # 200 PRECALL                  2
    # 204 CALL                     2
    # 214 POP_TOP
    # 216 JUMP_FORWARD            11 (to 240)
    # >>  218 PUSH_EXC_INFO
    # 220 WITH_EXCEPT_START
    # 222 POP_JUMP_FORWARD_IF_TRUE     4 (to 232)
    # 224 RERAISE                  2
    # >>  226 COPY                     3
    # 228 POP_EXCEPT
    # 230 RERAISE                  1
    # >>  232 POP_TOP
    # 234 POP_EXCEPT
    # 236 POP_TOP
    # 238 POP_TOP
    # 426     >>  240 LOAD_FAST                3 (pl)
    # 242 LOAD_CONST               4 ('ProductVersion')
    # 244 BINARY_SUBSCR
    # 254 STORE_FAST               4 (release)
    # 427         256 LOAD_CONST               5 (('', '', ''))
    # 258 STORE_FAST               5 (versioninfo)
    # 428         260 LOAD_GLOBAL              1 (NULL + os)
    # 272 LOAD_ATTR                7 (uname)
    # 282 PRECALL                  0
    # 286 CALL                     0
    # 296 LOAD_ATTR                8 (machine)
    # 306 STORE_FAST               6 (machine)
    # 429         308 LOAD_FAST                6 (machine)
    # 310 LOAD_CONST               6 (('ppc', 'Power Macintosh'))
    # 312 CONTAINS_OP              0
    # 314 POP_JUMP_FORWARD_IF_FALSE     2 (to 320)
    # 431         316 LOAD_CONST               7 ('PowerPC')
    # 318 STORE_FAST               6 (machine)
    # 433     >>  320 LOAD_FAST                4 (release)
    # 322 LOAD_FAST                5 (versioninfo)
    # 324 LOAD_FAST                6 (machine)
    # 326 BUILD_TUPLE              3
    # 328 RETURN_VALUE
    # ExceptionTable:
    # 74 to 80 -> 84 [0]
    # 84 to 102 -> 112 [1] lasti
    # 110 to 110 -> 112 [1] lasti
    # 150 to 192 -> 218 [1] lasti
    # 218 to 224 -> 226 [3] lasti
    # 232 to 232 -> 226 [3] lasti

def mac_ver(release, versioninfo, machine):
    """ Get macOS version information and return it as tuple (release,
        versioninfo, machine) with versioninfo being a tuple (version,
        dev_stage, non_release_version).

        Entries which cannot be determined are set to the parameter values
        which default to ''. All tuple entries are strings.
    """
    # 436           0 RESUME                   0
    # 448           2 LOAD_GLOBAL              1 (NULL + _mac_ver_xml)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 STORE_FAST               3 (info)
    # 449          30 LOAD_FAST                3 (info)
    # 32 POP_JUMP_FORWARD_IF_NONE     2 (to 38)
    # 450          34 LOAD_FAST                3 (info)
    # 36 RETURN_VALUE
    # 453     >>   38 LOAD_FAST                0 (release)
    # 40 LOAD_FAST                1 (versioninfo)
    # 42 LOAD_FAST                2 (machine)
    # 44 BUILD_TUPLE              3
    # 46 RETURN_VALUE

def _java_getprop(name, default):
    # 455           0 RESUME                   0
    # 457           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('System',))
    # 6 IMPORT_NAME              0 (java.lang)
    # 8 IMPORT_FROM              1 (System)
    # 10 STORE_FAST               2 (System)
    # 12 POP_TOP
    # 458          14 NOP
    # 459          16 LOAD_FAST                2 (System)
    # 18 LOAD_METHOD              2 (getProperty)
    # 40 LOAD_FAST                0 (name)
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 56 STORE_FAST               3 (value)
    # 460          58 LOAD_FAST                3 (value)
    # 60 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 66)
    # 461          62 LOAD_FAST                1 (default)
    # 64 RETURN_VALUE
    # 462     >>   66 LOAD_FAST                3 (value)
    # 68 RETURN_VALUE
    # >>   70 PUSH_EXC_INFO
    # 463          72 LOAD_GLOBAL              6 (AttributeError)
    # 84 CHECK_EXC_MATCH
    # 86 POP_JUMP_FORWARD_IF_FALSE     5 (to 98)
    # 88 POP_TOP
    # 464          90 LOAD_FAST                1 (default)
    # 92 SWAP                     2
    # 94 POP_EXCEPT
    # 96 RETURN_VALUE
    # 463     >>   98 RERAISE                  0
    # >>  100 COPY                     3
    # 102 POP_EXCEPT
    # 104 RERAISE                  1
    # ExceptionTable:
    # 16 to 62 -> 70 [0]
    # 66 to 66 -> 70 [0]
    # 70 to 92 -> 100 [1] lasti
    # 98 to 98 -> 100 [1] lasti

def java_ver(release, vendor, vminfo, osinfo):
    """ Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    """
    # 466           0 RESUME                   0
    # 479           2 NOP
    # 480           4 LOAD_CONST               1 (0)
    # 6 LOAD_CONST               2 (None)
    # 8 IMPORT_NAME              0 (java.lang)
    # 10 STORE_FAST               4 (java)
    # 12 JUMP_FORWARD            22 (to 58)
    # >>   14 PUSH_EXC_INFO
    # 481          16 LOAD_GLOBAL              2 (ImportError)
    # 28 CHECK_EXC_MATCH
    # 30 POP_JUMP_FORWARD_IF_FALSE     9 (to 50)
    # 32 POP_TOP
    # 482          34 LOAD_FAST                0 (release)
    # 36 LOAD_FAST                1 (vendor)
    # 38 LOAD_FAST                2 (vminfo)
    # 40 LOAD_FAST                3 (osinfo)
    # 42 BUILD_TUPLE              4
    # 44 SWAP                     2
    # 46 POP_EXCEPT
    # 48 RETURN_VALUE
    # 481     >>   50 RERAISE                  0
    # >>   52 COPY                     3
    # 54 POP_EXCEPT
    # 56 RERAISE                  1
    # 484     >>   58 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 70 LOAD_CONST               3 ('java.vendor')
    # 72 LOAD_FAST                1 (vendor)
    # 74 PRECALL                  2
    # 78 CALL                     2
    # 88 STORE_FAST               1 (vendor)
    # 485          90 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 102 LOAD_CONST               4 ('java.version')
    # 104 LOAD_FAST                0 (release)
    # 106 PRECALL                  2
    # 110 CALL                     2
    # 120 STORE_FAST               0 (release)
    # 486         122 LOAD_FAST                2 (vminfo)
    # 124 UNPACK_SEQUENCE          3
    # 128 STORE_FAST               5 (vm_name)
    # 130 STORE_FAST               6 (vm_release)
    # 132 STORE_FAST               7 (vm_vendor)
    # 487         134 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 146 LOAD_CONST               5 ('java.vm.name')
    # 148 LOAD_FAST                5 (vm_name)
    # 150 PRECALL                  2
    # 154 CALL                     2
    # 164 STORE_FAST               5 (vm_name)
    # 488         166 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 178 LOAD_CONST               6 ('java.vm.vendor')
    # 180 LOAD_FAST                7 (vm_vendor)
    # 182 PRECALL                  2
    # 186 CALL                     2
    # 196 STORE_FAST               7 (vm_vendor)
    # 489         198 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 210 LOAD_CONST               7 ('java.vm.version')
    # 212 LOAD_FAST                6 (vm_release)
    # 214 PRECALL                  2
    # 218 CALL                     2
    # 228 STORE_FAST               6 (vm_release)
    # 490         230 LOAD_FAST                5 (vm_name)
    # 232 LOAD_FAST                6 (vm_release)
    # 234 LOAD_FAST                7 (vm_vendor)
    # 236 BUILD_TUPLE              3
    # 238 STORE_FAST               2 (vminfo)
    # 491         240 LOAD_FAST                3 (osinfo)
    # 242 UNPACK_SEQUENCE          3
    # 246 STORE_FAST               8 (os_name)
    # 248 STORE_FAST               9 (os_version)
    # 250 STORE_FAST              10 (os_arch)
    # 492         252 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 264 LOAD_CONST               8 ('java.os.arch')
    # 266 LOAD_FAST               10 (os_arch)
    # 268 PRECALL                  2
    # 272 CALL                     2
    # 282 STORE_FAST              10 (os_arch)
    # 493         284 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 296 LOAD_CONST               9 ('java.os.name')
    # 298 LOAD_FAST                8 (os_name)
    # 300 PRECALL                  2
    # 304 CALL                     2
    # 314 STORE_FAST               8 (os_name)
    # 494         316 LOAD_GLOBAL              5 (NULL + _java_getprop)
    # 328 LOAD_CONST              10 ('java.os.version')
    # 330 LOAD_FAST                9 (os_version)
    # 332 PRECALL                  2
    # 336 CALL                     2
    # 346 STORE_FAST               9 (os_version)
    # 495         348 LOAD_FAST                8 (os_name)
    # 350 LOAD_FAST                9 (os_version)
    # 352 LOAD_FAST               10 (os_arch)
    # 354 BUILD_TUPLE              3
    # 356 STORE_FAST               3 (osinfo)
    # 497         358 LOAD_FAST                0 (release)
    # 360 LOAD_FAST                1 (vendor)
    # 362 LOAD_FAST                2 (vminfo)
    # 364 LOAD_FAST                3 (osinfo)
    # 366 BUILD_TUPLE              4
    # 368 RETURN_VALUE
    # ExceptionTable:
    # 4 to 10 -> 14 [0]
    # 14 to 44 -> 52 [1] lasti
    # 50 to 50 -> 52 [1] lasti

def system_alias(system, release, version):
    """ Returns (system, release, version) aliased to common
        marketing names used for some systems.

        It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

    """
    # 501           0 RESUME                   0
    # 510           2 LOAD_FAST                0 (system)
    # 4 LOAD_CONST               1 ('SunOS')
    # 6 COMPARE_OP               2 (==)
    # 12 POP_JUMP_FORWARD_IF_FALSE   129 (to 272)
    # 512          14 LOAD_FAST                1 (release)
    # 16 LOAD_CONST               2 ('5')
    # 18 COMPARE_OP               0 (<)
    # 24 POP_JUMP_FORWARD_IF_FALSE     5 (to 36)
    # 514          26 LOAD_FAST                0 (system)
    # 28 LOAD_FAST                1 (release)
    # 30 LOAD_FAST                2 (version)
    # 32 BUILD_TUPLE              3
    # 34 RETURN_VALUE
    # 516     >>   36 LOAD_FAST                1 (release)
    # 38 LOAD_METHOD              0 (split)
    # 60 LOAD_CONST               3 ('.')
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 STORE_FAST               3 (l)
    # 517          78 LOAD_FAST                3 (l)
    # 80 POP_JUMP_FORWARD_IF_FALSE    83 (to 248)
    # 518          82 NOP
    # 519          84 LOAD_GLOBAL              3 (NULL + int)
    # 96 LOAD_FAST                3 (l)
    # 98 LOAD_CONST               4 (0)
    # 100 BINARY_SUBSCR
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 STORE_FAST               4 (major)
    # 523         126 LOAD_FAST                4 (major)
    # 128 LOAD_CONST               5 (3)
    # 130 BINARY_OP               10 (-)
    # 134 STORE_FAST               4 (major)
    # 524         136 LOAD_GLOBAL              5 (NULL + str)
    # 148 LOAD_FAST                4 (major)
    # 150 PRECALL                  1
    # 154 CALL                     1
    # 164 LOAD_FAST                3 (l)
    # 166 LOAD_CONST               4 (0)
    # 168 STORE_SUBSCR
    # 525         172 LOAD_CONST               3 ('.')
    # 174 LOAD_METHOD              3 (join)
    # 196 LOAD_FAST                3 (l)
    # 198 PRECALL                  1
    # 202 CALL                     1
    # 212 STORE_FAST               1 (release)
    # 214 JUMP_FORWARD            16 (to 248)
    # >>  216 PUSH_EXC_INFO
    # 520         218 LOAD_GLOBAL              8 (ValueError)
    # 230 CHECK_EXC_MATCH
    # 232 POP_JUMP_FORWARD_IF_FALSE     3 (to 240)
    # 234 POP_TOP
    # 521         236 POP_EXCEPT
    # 238 JUMP_FORWARD             4 (to 248)
    # 520     >>  240 RERAISE                  0
    # >>  242 COPY                     3
    # 244 POP_EXCEPT
    # 246 RERAISE                  1
    # 526     >>  248 LOAD_FAST                1 (release)
    # 250 LOAD_CONST               6 ('6')
    # 252 COMPARE_OP               0 (<)
    # 258 POP_JUMP_FORWARD_IF_FALSE     3 (to 266)
    # 527         260 LOAD_CONST               7 ('Solaris')
    # 262 STORE_FAST               0 (system)
    # 264 JUMP_FORWARD             9 (to 284)
    # 530     >>  266 LOAD_CONST               7 ('Solaris')
    # 268 STORE_FAST               0 (system)
    # 270 JUMP_FORWARD             6 (to 284)
    # 532     >>  272 LOAD_FAST                0 (system)
    # 274 LOAD_CONST               8 (('win32', 'win16'))
    # 276 CONTAINS_OP              0
    # 278 POP_JUMP_FORWARD_IF_FALSE     2 (to 284)
    # 534         280 LOAD_CONST               9 ('Windows')
    # 282 STORE_FAST               0 (system)
    # 539     >>  284 LOAD_FAST                0 (system)
    # 286 LOAD_FAST                1 (release)
    # 288 LOAD_FAST                2 (version)
    # 290 BUILD_TUPLE              3
    # 292 RETURN_VALUE
    # ExceptionTable:
    # 84 to 124 -> 216 [0]
    # 216 to 234 -> 242 [1] lasti
    # 240 to 240 -> 242 [1] lasti

def _platform():
    """ Helper to format the platform string in a filename
        compatible format e.g. "system-version-machine".
    """
    # 543           0 RESUME                   0
    # 549           2 LOAD_CONST               1 ('-')
    # 4 LOAD_METHOD              0 (join)
    # 26 LOAD_CONST               2 (<code object <genexpr> at 0x000001EBD77FA030, file "platform.py", line 549>)
    # 28 MAKE_FUNCTION            0
    # 30 LOAD_GLOBAL              3 (NULL + filter)
    # 42 LOAD_GLOBAL              4 (len)
    # 54 LOAD_FAST                0 (args)
    # 56 PRECALL                  2
    # 60 CALL                     2
    # 70 GET_ITER
    # 72 PRECALL                  0
    # 76 CALL                     0
    # 86 PRECALL                  1
    # 90 CALL                     1
    # 100 STORE_FAST               1 (platform)
    # 552         102 LOAD_FAST                1 (platform)
    # 104 LOAD_METHOD              3 (replace)
    # 126 LOAD_CONST               3 (' ')
    # 128 LOAD_CONST               4 ('_')
    # 130 PRECALL                  2
    # 134 CALL                     2
    # 144 STORE_FAST               1 (platform)
    # 553         146 LOAD_FAST                1 (platform)
    # 148 LOAD_METHOD              3 (replace)
    # 170 LOAD_CONST               5 ('/')
    # 172 LOAD_CONST               1 ('-')
    # 174 PRECALL                  2
    # 178 CALL                     2
    # 188 STORE_FAST               1 (platform)
    # 554         190 LOAD_FAST                1 (platform)
    # 192 LOAD_METHOD              3 (replace)
    # 214 LOAD_CONST               6 ('\\')
    # 216 LOAD_CONST               1 ('-')
    # 218 PRECALL                  2
    # 222 CALL                     2
    # 232 STORE_FAST               1 (platform)
    # 555         234 LOAD_FAST                1 (platform)
    # 236 LOAD_METHOD              3 (replace)
    # 258 LOAD_CONST               7 (':')
    # 260 LOAD_CONST               1 ('-')
    # 262 PRECALL                  2
    # 266 CALL                     2
    # 276 STORE_FAST               1 (platform)
    # 556         278 LOAD_FAST                1 (platform)
    # 280 LOAD_METHOD              3 (replace)
    # 302 LOAD_CONST               8 (';')
    # 304 LOAD_CONST               1 ('-')
    # 306 PRECALL                  2
    # 310 CALL                     2
    # 320 STORE_FAST               1 (platform)
    # 557         322 LOAD_FAST                1 (platform)
    # 324 LOAD_METHOD              3 (replace)
    # 346 LOAD_CONST               9 ('"')
    # 348 LOAD_CONST               1 ('-')
    # 350 PRECALL                  2
    # 354 CALL                     2
    # 364 STORE_FAST               1 (platform)
    # 558         366 LOAD_FAST                1 (platform)
    # 368 LOAD_METHOD              3 (replace)
    # 390 LOAD_CONST              10 ('(')
    # 392 LOAD_CONST               1 ('-')
    # 394 PRECALL                  2
    # 398 CALL                     2
    # 408 STORE_FAST               1 (platform)
    # 559         410 LOAD_FAST                1 (platform)
    # 412 LOAD_METHOD              3 (replace)
    # 434 LOAD_CONST              11 (')')
    # 436 LOAD_CONST               1 ('-')
    # 438 PRECALL                  2
    # 442 CALL                     2
    # 452 STORE_FAST               1 (platform)
    # 562         454 LOAD_FAST                1 (platform)
    # 456 LOAD_METHOD              3 (replace)
    # 478 LOAD_CONST              12 ('unknown')
    # 480 LOAD_CONST              13 ('')
    # 482 PRECALL                  2
    # 486 CALL                     2
    # 496 STORE_FAST               1 (platform)
    # 565         498 NOP
    # 566     >>  500 LOAD_FAST                1 (platform)
    # 502 LOAD_METHOD              3 (replace)
    # 524 LOAD_CONST              15 ('--')
    # 526 LOAD_CONST               1 ('-')
    # 528 PRECALL                  2
    # 532 CALL                     2
    # 542 STORE_FAST               2 (cleaned)
    # 567         544 LOAD_FAST                2 (cleaned)
    # 546 LOAD_FAST                1 (platform)
    # 548 COMPARE_OP               2 (==)
    # 554 POP_JUMP_FORWARD_IF_FALSE     1 (to 558)
    # 568         556 JUMP_FORWARD             3 (to 564)
    # 569     >>  558 LOAD_FAST                2 (cleaned)
    # 560 STORE_FAST               1 (platform)
    # 565         562 JUMP_BACKWARD           32 (to 500)
    # 570     >>  564 LOAD_FAST                1 (platform)
    # 566 LOAD_CONST              16 (-1)
    # 568 BINARY_SUBSCR
    # 578 LOAD_CONST               1 ('-')
    # 580 COMPARE_OP               2 (==)
    # 586 POP_JUMP_FORWARD_IF_FALSE    22 (to 632)
    # 571     >>  588 LOAD_FAST                1 (platform)
    # 590 LOAD_CONST              17 (None)
    # 592 LOAD_CONST              16 (-1)
    # 594 BUILD_SLICE              2
    # 596 BINARY_SUBSCR
    # 606 STORE_FAST               1 (platform)
    # 570         608 LOAD_FAST                1 (platform)
    # 610 LOAD_CONST              16 (-1)
    # 612 BINARY_SUBSCR
    # 622 LOAD_CONST               1 ('-')
    # 624 COMPARE_OP               2 (==)
    # 630 POP_JUMP_BACKWARD_IF_TRUE    22 (to 588)
    # 573     >>  632 LOAD_FAST                1 (platform)
    # 634 RETURN_VALUE
    # Disassembly of <code object <genexpr> at 0x000001EBD77FA030, file "platform.py", line 549>:
    # 549           0 RETURN_GENERATOR
    # 2 POP_TOP
    # 4 RESUME                   0
    # 6 LOAD_FAST                0 (.0)
    # >>    8 FOR_ITER                24 (to 58)
    # 10 STORE_FAST               1 (x)
    # 12 LOAD_FAST                1 (x)
    # 14 LOAD_METHOD              0 (strip)
    # 36 PRECALL                  0
    # 40 CALL                     0
    # 50 YIELD_VALUE
    # 52 RESUME                   1
    # 54 POP_TOP
    # 56 JUMP_BACKWARD           25 (to 8)
    # >>   58 LOAD_CONST               0 (None)
    # 60 RETURN_VALUE

def _node(default):
    """ Helper to determine the node name of this machine.
    """
    # 575           0 RESUME                   0
    # 579           2 NOP
    # 580           4 LOAD_CONST               1 (0)
    # 6 LOAD_CONST               2 (None)
    # 8 IMPORT_NAME              0 (socket)
    # 10 STORE_FAST               1 (socket)
    # 12 JUMP_FORWARD            18 (to 50)
    # >>   14 PUSH_EXC_INFO
    # 581          16 LOAD_GLOBAL              2 (ImportError)
    # 28 CHECK_EXC_MATCH
    # 30 POP_JUMP_FORWARD_IF_FALSE     5 (to 42)
    # 32 POP_TOP
    # 583          34 LOAD_FAST                0 (default)
    # 36 SWAP                     2
    # 38 POP_EXCEPT
    # 40 RETURN_VALUE
    # 581     >>   42 RERAISE                  0
    # >>   44 COPY                     3
    # 46 POP_EXCEPT
    # 48 RERAISE                  1
    # 584     >>   50 NOP
    # 585          52 LOAD_FAST                1 (socket)
    # 54 LOAD_METHOD              2 (gethostname)
    # 76 PRECALL                  0
    # 80 CALL                     0
    # 90 RETURN_VALUE
    # >>   92 PUSH_EXC_INFO
    # 586          94 LOAD_GLOBAL              6 (OSError)
    # 106 CHECK_EXC_MATCH
    # 108 POP_JUMP_FORWARD_IF_FALSE     5 (to 120)
    # 110 POP_TOP
    # 588         112 LOAD_FAST                0 (default)
    # 114 SWAP                     2
    # 116 POP_EXCEPT
    # 118 RETURN_VALUE
    # 586     >>  120 RERAISE                  0
    # >>  122 COPY                     3
    # 124 POP_EXCEPT
    # 126 RERAISE                  1
    # ExceptionTable:
    # 4 to 10 -> 14 [0]
    # 14 to 36 -> 44 [1] lasti
    # 42 to 42 -> 44 [1] lasti
    # 52 to 88 -> 92 [0]
    # 92 to 114 -> 122 [1] lasti
    # 120 to 120 -> 122 [1] lasti

def _follow_symlinks(filepath):
    """ In case filepath is a symlink, follow it until a
        real file is reached.
    """
    # 590           0 RESUME                   0
    # 595           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (path)
    # 24 LOAD_METHOD              2 (abspath)
    # 46 LOAD_FAST                0 (filepath)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 STORE_FAST               0 (filepath)
    # 596          64 LOAD_GLOBAL              0 (os)
    # 76 LOAD_ATTR                1 (path)
    # 86 LOAD_METHOD              3 (islink)
    # 108 LOAD_FAST                0 (filepath)
    # 110 PRECALL                  1
    # 114 CALL                     1
    # 124 POP_JUMP_FORWARD_IF_FALSE   139 (to 404)
    # 597     >>  126 LOAD_GLOBAL              0 (os)
    # 138 LOAD_ATTR                1 (path)
    # 148 LOAD_METHOD              4 (normpath)
    # 598         170 LOAD_GLOBAL              0 (os)
    # 182 LOAD_ATTR                1 (path)
    # 192 LOAD_METHOD              5 (join)
    # 214 LOAD_GLOBAL              0 (os)
    # 226 LOAD_ATTR                1 (path)
    # 236 LOAD_METHOD              6 (dirname)
    # 258 LOAD_FAST                0 (filepath)
    # 260 PRECALL                  1
    # 264 CALL                     1
    # 274 LOAD_GLOBAL              1 (NULL + os)
    # 286 LOAD_ATTR                7 (readlink)
    # 296 LOAD_FAST                0 (filepath)
    # 298 PRECALL                  1
    # 302 CALL                     1
    # 312 PRECALL                  2
    # 316 CALL                     2
    # 597         326 PRECALL                  1
    # 330 CALL                     1
    # 340 STORE_FAST               0 (filepath)
    # 596         342 LOAD_GLOBAL              0 (os)
    # 354 LOAD_ATTR                1 (path)
    # 364 LOAD_METHOD              3 (islink)
    # 386 LOAD_FAST                0 (filepath)
    # 388 PRECALL                  1
    # 392 CALL                     1
    # 402 POP_JUMP_BACKWARD_IF_TRUE   139 (to 126)
    # 599     >>  404 LOAD_FAST                0 (filepath)
    # 406 RETURN_VALUE

def _syscmd_file(target, default):
    """ Interface to the system's file command.

        The function uses the -b option of the file command to have it
        omit the filename in its output. Follow the symlinks. It returns
        default in case the command should fail.

    """
    # 602           0 RESUME                   0
    # 611           2 LOAD_GLOBAL              0 (sys)
    # 14 LOAD_ATTR                1 (platform)
    # 24 LOAD_CONST               1 (('dos', 'win32', 'win16'))
    # 26 CONTAINS_OP              0
    # 28 POP_JUMP_FORWARD_IF_FALSE     2 (to 34)
    # 613          30 LOAD_FAST                1 (default)
    # 32 RETURN_VALUE
    # 615     >>   34 NOP
    # 616          36 LOAD_CONST               2 (0)
    # 38 LOAD_CONST               3 (None)
    # 40 IMPORT_NAME              2 (subprocess)
    # 42 STORE_FAST               2 (subprocess)
    # 44 JUMP_FORWARD            18 (to 82)
    # >>   46 PUSH_EXC_INFO
    # 617          48 LOAD_GLOBAL              6 (ImportError)
    # 60 CHECK_EXC_MATCH
    # 62 POP_JUMP_FORWARD_IF_FALSE     5 (to 74)
    # 64 POP_TOP
    # 618          66 LOAD_FAST                1 (default)
    # 68 SWAP                     2
    # 70 POP_EXCEPT
    # 72 RETURN_VALUE
    # 617     >>   74 RERAISE                  0
    # >>   76 COPY                     3
    # 78 POP_EXCEPT
    # 80 RERAISE                  1
    # 619     >>   82 LOAD_GLOBAL              9 (NULL + _follow_symlinks)
    # 94 LOAD_FAST                0 (target)
    # 96 PRECALL                  1
    # 100 CALL                     1
    # 110 STORE_FAST               0 (target)
    # 622         112 LOAD_GLOBAL             11 (NULL + dict)
    # 124 LOAD_GLOBAL             12 (os)
    # 136 LOAD_ATTR                7 (environ)
    # 146 LOAD_CONST               4 ('C')
    # 148 KW_NAMES                 5
    # 150 PRECALL                  2
    # 154 CALL                     2
    # 164 STORE_FAST               3 (env)
    # 623         166 NOP
    # 625         168 LOAD_FAST                2 (subprocess)
    # 170 LOAD_METHOD              8 (check_output)
    # 192 LOAD_CONST               6 ('file')
    # 194 LOAD_CONST               7 ('-b')
    # 196 LOAD_FAST                0 (target)
    # 198 BUILD_LIST               3
    # 626         200 LOAD_FAST                2 (subprocess)
    # 202 LOAD_ATTR                9 (DEVNULL)
    # 627         212 LOAD_FAST                3 (env)
    # 625         214 KW_NAMES                 8
    # 216 PRECALL                  3
    # 220 CALL                     3
    # 230 STORE_FAST               4 (output)
    # 232 JUMP_FORWARD            25 (to 284)
    # >>  234 PUSH_EXC_INFO
    # 628         236 LOAD_GLOBAL             20 (OSError)
    # 248 LOAD_FAST                2 (subprocess)
    # 250 LOAD_ATTR               11 (CalledProcessError)
    # 260 BUILD_TUPLE              2
    # 262 CHECK_EXC_MATCH
    # 264 POP_JUMP_FORWARD_IF_FALSE     5 (to 276)
    # 266 POP_TOP
    # 629         268 LOAD_FAST                1 (default)
    # 270 SWAP                     2
    # 272 POP_EXCEPT
    # 274 RETURN_VALUE
    # 628     >>  276 RERAISE                  0
    # >>  278 COPY                     3
    # 280 POP_EXCEPT
    # 282 RERAISE                  1
    # 630     >>  284 LOAD_FAST                4 (output)
    # 286 POP_JUMP_FORWARD_IF_TRUE     2 (to 292)
    # 631         288 LOAD_FAST                1 (default)
    # 290 RETURN_VALUE
    # 634     >>  292 LOAD_FAST                4 (output)
    # 294 LOAD_METHOD             12 (decode)
    # 316 LOAD_CONST               9 ('latin-1')
    # 318 PRECALL                  1
    # 322 CALL                     1
    # 332 RETURN_VALUE
    # ExceptionTable:
    # 36 to 42 -> 46 [0]
    # 46 to 68 -> 76 [1] lasti
    # 74 to 74 -> 76 [1] lasti
    # 168 to 230 -> 234 [0]
    # 234 to 270 -> 278 [1] lasti
    # 276 to 276 -> 278 [1] lasti

def architecture(executable, bits, linkage):
    """ Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.

        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable. Both values are returned as strings.

        Values that cannot be determined are returned as given by the
        parameter presets. If bits is given as '', the sizeof(pointer)
        (or sizeof(long) on Python version < 1.5.2) is used as
        indicator for the supported pointer size.

        The function relies on the system's "file" command to do the
        actual work. This is available on most if not all Unix
        platforms. On some non-Unix platforms where the "file" command
        does not exist and the executable is set to the Python interpreter
        binary defaults from _default_architecture are used.

    """
    # 646           0 RESUME                   0
    # 669           2 LOAD_FAST                1 (bits)
    # 4 POP_JUMP_FORWARD_IF_TRUE    46 (to 98)
    # 670           6 LOAD_CONST               1 (0)
    # 8 LOAD_CONST               2 (None)
    # 10 IMPORT_NAME              0 (struct)
    # 12 STORE_FAST               3 (struct)
    # 671          14 LOAD_FAST                3 (struct)
    # 16 LOAD_METHOD              1 (calcsize)
    # 38 LOAD_CONST               3 ('P')
    # 40 PRECALL                  1
    # 44 CALL                     1
    # 54 STORE_FAST               4 (size)
    # 672          56 LOAD_GLOBAL              5 (NULL + str)
    # 68 LOAD_FAST                4 (size)
    # 70 LOAD_CONST               4 (8)
    # 72 BINARY_OP                5 (*)
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 LOAD_CONST               5 ('bit')
    # 92 BINARY_OP                0 (+)
    # 96 STORE_FAST               1 (bits)
    # 675     >>   98 LOAD_FAST                0 (executable)
    # 100 POP_JUMP_FORWARD_IF_FALSE    17 (to 136)
    # 676         102 LOAD_GLOBAL              7 (NULL + _syscmd_file)
    # 114 LOAD_FAST                0 (executable)
    # 116 LOAD_CONST               6 ('')
    # 118 PRECALL                  2
    # 122 CALL                     2
    # 132 STORE_FAST               5 (fileout)
    # 134 JUMP_FORWARD             2 (to 140)
    # 678     >>  136 LOAD_CONST               6 ('')
    # 138 STORE_FAST               5 (fileout)
    # 680     >>  140 LOAD_FAST                5 (fileout)
    # 142 POP_JUMP_FORWARD_IF_TRUE    73 (to 290)
    # 681         144 LOAD_FAST                0 (executable)
    # 146 LOAD_GLOBAL              8 (sys)
    # 158 LOAD_ATTR                5 (executable)
    # 168 COMPARE_OP               2 (==)
    # 174 POP_JUMP_FORWARD_IF_FALSE    57 (to 290)
    # 684         176 LOAD_GLOBAL              8 (sys)
    # 188 LOAD_ATTR                6 (platform)
    # 198 LOAD_GLOBAL             14 (_default_architecture)
    # 210 CONTAINS_OP              0
    # 212 POP_JUMP_FORWARD_IF_FALSE    34 (to 282)
    # 685         214 LOAD_GLOBAL             14 (_default_architecture)
    # 226 LOAD_GLOBAL              8 (sys)
    # 238 LOAD_ATTR                6 (platform)
    # 248 BINARY_SUBSCR
    # 258 UNPACK_SEQUENCE          2
    # 262 STORE_FAST               6 (b)
    # 264 STORE_FAST               7 (l)
    # 686         266 LOAD_FAST                6 (b)
    # 268 POP_JUMP_FORWARD_IF_FALSE     2 (to 274)
    # 687         270 LOAD_FAST                6 (b)
    # 272 STORE_FAST               1 (bits)
    # 688     >>  274 LOAD_FAST                7 (l)
    # 276 POP_JUMP_FORWARD_IF_FALSE     2 (to 282)
    # 689         278 LOAD_FAST                7 (l)
    # 280 STORE_FAST               2 (linkage)
    # 690     >>  282 LOAD_FAST                1 (bits)
    # 284 LOAD_FAST                2 (linkage)
    # 286 BUILD_TUPLE              2
    # 288 RETURN_VALUE
    # 692     >>  290 LOAD_CONST               7 ('executable')
    # 292 LOAD_FAST                5 (fileout)
    # 294 CONTAINS_OP              1
    # 296 POP_JUMP_FORWARD_IF_FALSE     8 (to 314)
    # 298 LOAD_CONST               8 ('shared object')
    # 300 LOAD_FAST                5 (fileout)
    # 302 CONTAINS_OP              1
    # 304 POP_JUMP_FORWARD_IF_FALSE     4 (to 314)
    # 694         306 LOAD_FAST                1 (bits)
    # 308 LOAD_FAST                2 (linkage)
    # 310 BUILD_TUPLE              2
    # 312 RETURN_VALUE
    # 697     >>  314 LOAD_CONST               9 ('32-bit')
    # 316 LOAD_FAST                5 (fileout)
    # 318 CONTAINS_OP              0
    # 320 POP_JUMP_FORWARD_IF_FALSE     3 (to 328)
    # 698         322 LOAD_CONST              10 ('32bit')
    # 324 STORE_FAST               1 (bits)
    # 326 JUMP_FORWARD             6 (to 340)
    # 699     >>  328 LOAD_CONST              11 ('64-bit')
    # 330 LOAD_FAST                5 (fileout)
    # 332 CONTAINS_OP              0
    # 334 POP_JUMP_FORWARD_IF_FALSE     2 (to 340)
    # 700         336 LOAD_CONST              12 ('64bit')
    # 338 STORE_FAST               1 (bits)
    # 703     >>  340 LOAD_CONST              13 ('ELF')
    # 342 LOAD_FAST                5 (fileout)
    # 344 CONTAINS_OP              0
    # 346 POP_JUMP_FORWARD_IF_FALSE     3 (to 354)
    # 704         348 LOAD_CONST              13 ('ELF')
    # 350 STORE_FAST               2 (linkage)
    # 352 JUMP_FORWARD            29 (to 412)
    # 705     >>  354 LOAD_CONST              14 ('PE')
    # 356 LOAD_FAST                5 (fileout)
    # 358 CONTAINS_OP              0
    # 360 POP_JUMP_FORWARD_IF_FALSE    10 (to 382)
    # 707         362 LOAD_CONST              15 ('Windows')
    # 364 LOAD_FAST                5 (fileout)
    # 366 CONTAINS_OP              0
    # 368 POP_JUMP_FORWARD_IF_FALSE     3 (to 376)
    # 708         370 LOAD_CONST              16 ('WindowsPE')
    # 372 STORE_FAST               2 (linkage)
    # 374 JUMP_FORWARD            18 (to 412)
    # 710     >>  376 LOAD_CONST              14 ('PE')
    # 378 STORE_FAST               2 (linkage)
    # 380 JUMP_FORWARD            15 (to 412)
    # 711     >>  382 LOAD_CONST              17 ('COFF')
    # 384 LOAD_FAST                5 (fileout)
    # 386 CONTAINS_OP              0
    # 388 POP_JUMP_FORWARD_IF_FALSE     3 (to 396)
    # 712         390 LOAD_CONST              17 ('COFF')
    # 392 STORE_FAST               2 (linkage)
    # 394 JUMP_FORWARD             8 (to 412)
    # 713     >>  396 LOAD_CONST              18 ('MS-DOS')
    # 398 LOAD_FAST                5 (fileout)
    # 400 CONTAINS_OP              0
    # 402 POP_JUMP_FORWARD_IF_FALSE     3 (to 410)
    # 714         404 LOAD_CONST              19 ('MSDOS')
    # 406 STORE_FAST               2 (linkage)
    # 408 JUMP_FORWARD             1 (to 412)
    # 717     >>  410 NOP
    # 719     >>  412 LOAD_FAST                1 (bits)
    # 414 LOAD_FAST                2 (linkage)
    # 416 BUILD_TUPLE              2
    # 418 RETURN_VALUE

def _get_machine_win32():
    # 722           0 RESUME                   0
    # 730           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (environ)
    # 24 LOAD_METHOD              2 (get)
    # 46 LOAD_CONST               1 ('PROCESSOR_ARCHITEW6432')
    # 48 LOAD_CONST               2 ('')
    # 50 PRECALL                  2
    # 54 CALL                     2
    # 64 JUMP_IF_TRUE_OR_POP     31 (to 128)
    # 731          66 LOAD_GLOBAL              0 (os)
    # 78 LOAD_ATTR                1 (environ)
    # 88 LOAD_METHOD              2 (get)
    # 110 LOAD_CONST               3 ('PROCESSOR_ARCHITECTURE')
    # 112 LOAD_CONST               2 ('')
    # 114 PRECALL                  2
    # 118 CALL                     2
    # 729     >>  128 RETURN_VALUE

class _Processor:
    """_Processor"""
    def get(cls):
        # 736           0 RESUME                   0
        # 738           2 LOAD_GLOBAL              1 (NULL + getattr)
        # 14 LOAD_FAST                0 (cls)
        # 16 LOAD_CONST               1 ('get_')
        # 18 LOAD_GLOBAL              2 (sys)
        # 30 LOAD_ATTR                2 (platform)
        # 40 FORMAT_VALUE             0
        # 42 BUILD_STRING             2
        # 44 LOAD_FAST                0 (cls)
        # 46 LOAD_ATTR                3 (from_subprocess)
        # 56 PRECALL                  3
        # 60 CALL                     3
        # 70 STORE_FAST               1 (func)
        # 739          72 PUSH_NULL
        # 74 LOAD_FAST                1 (func)
        # 76 PRECALL                  0
        # 80 CALL                     0
        # 90 JUMP_IF_TRUE_OR_POP      1 (to 94)
        # 92 LOAD_CONST               2 ('')
        # >>   94 RETURN_VALUE

    def get_win32():
        # 741           0 RESUME                   0
        # 742           2 LOAD_GLOBAL              0 (os)
        # 14 LOAD_ATTR                1 (environ)
        # 24 LOAD_METHOD              2 (get)
        # 46 LOAD_CONST               1 ('PROCESSOR_IDENTIFIER')
        # 48 LOAD_GLOBAL              7 (NULL + _get_machine_win32)
        # 60 PRECALL                  0
        # 64 CALL                     0
        # 74 PRECALL                  2
        # 78 CALL                     2
        # 88 RETURN_VALUE

    def get_OpenVMS():
        # 744           0 RESUME                   0
        # 745           2 NOP
        # 746           4 LOAD_CONST               1 (0)
        # 6 LOAD_CONST               0 (None)
        # 8 IMPORT_NAME              0 (vms_lib)
        # 10 STORE_FAST               0 (vms_lib)
        # 750          12 LOAD_FAST                0 (vms_lib)
        # 14 LOAD_METHOD              1 (getsyi)
        # 36 LOAD_CONST               2 ('SYI$_CPU')
        # 38 LOAD_CONST               1 (0)
        # 40 PRECALL                  2
        # 44 CALL                     2
        # 54 UNPACK_SEQUENCE          2
        # 58 STORE_FAST               1 (csid)
        # 60 STORE_FAST               2 (cpu_number)
        # 751          62 LOAD_FAST                2 (cpu_number)
        # 64 LOAD_CONST               3 (128)
        # 66 COMPARE_OP               5 (>=)
        # 72 POP_JUMP_FORWARD_IF_FALSE     2 (to 78)
        # 74 LOAD_CONST               4 ('Alpha')
        # 76 JUMP_FORWARD             1 (to 80)
        # >>   78 LOAD_CONST               5 ('VAX')
        # >>   80 RETURN_VALUE
        # >>   82 PUSH_EXC_INFO
        # 747          84 LOAD_GLOBAL              4 (ImportError)
        # 96 CHECK_EXC_MATCH
        # 98 POP_JUMP_FORWARD_IF_FALSE     4 (to 108)
        # 100 POP_TOP
        # 748         102 POP_EXCEPT
        # 104 LOAD_CONST               0 (None)
        # 106 RETURN_VALUE
        # 747     >>  108 RERAISE                  0
        # >>  110 COPY                     3
        # 112 POP_EXCEPT
        # 114 RERAISE                  1
        # ExceptionTable:
        # 4 to 10 -> 82 [0]
        # 82 to 100 -> 110 [1] lasti
        # 108 to 108 -> 110 [1] lasti

    def from_subprocess():
        """
        Fall back to `uname -p`
        """
        # 753           0 RESUME                   0
        # 757           2 NOP
        # 758           4 LOAD_CONST               1 (0)
        # 6 LOAD_CONST               2 (None)
        # 8 IMPORT_NAME              0 (subprocess)
        # 10 STORE_FAST               0 (subprocess)
        # 12 JUMP_FORWARD            17 (to 48)
        # >>   14 PUSH_EXC_INFO
        # 759          16 LOAD_GLOBAL              2 (ImportError)
        # 28 CHECK_EXC_MATCH
        # 30 POP_JUMP_FORWARD_IF_FALSE     4 (to 40)
        # 32 POP_TOP
        # 760          34 POP_EXCEPT
        # 36 LOAD_CONST               2 (None)
        # 38 RETURN_VALUE
        # 759     >>   40 RERAISE                  0
        # >>   42 COPY                     3
        # 44 POP_EXCEPT
        # 46 RERAISE                  1
        # 761     >>   48 NOP
        # 762          50 LOAD_FAST                0 (subprocess)
        # 52 LOAD_METHOD              2 (check_output)
        # 763          74 LOAD_CONST               3 ('uname')
        # 76 LOAD_CONST               4 ('-p')
        # 78 BUILD_LIST               2
        # 764          80 LOAD_FAST                0 (subprocess)
        # 82 LOAD_ATTR                3 (DEVNULL)
        # 765          92 LOAD_CONST               5 (True)
        # 766          94 LOAD_CONST               6 ('utf8')
        # 762          96 KW_NAMES                 7
        # 98 PRECALL                  4
        # 102 CALL                     4
        # 767         112 LOAD_METHOD              4 (strip)
        # 134 PRECALL                  0
        # 138 CALL                     0
        # 762         148 RETURN_VALUE
        # >>  150 PUSH_EXC_INFO
        # 768         152 LOAD_GLOBAL             10 (OSError)
        # 164 LOAD_FAST                0 (subprocess)
        # 166 LOAD_ATTR                6 (CalledProcessError)
        # 176 BUILD_TUPLE              2
        # 178 CHECK_EXC_MATCH
        # 180 POP_JUMP_FORWARD_IF_FALSE     4 (to 190)
        # 182 POP_TOP
        # 769         184 POP_EXCEPT
        # 186 LOAD_CONST               2 (None)
        # 188 RETURN_VALUE
        # 768     >>  190 RERAISE                  0
        # >>  192 COPY                     3
        # 194 POP_EXCEPT
        # 196 RERAISE                  1
        # ExceptionTable:
        # 4 to 10 -> 14 [0]
        # 14 to 32 -> 42 [1] lasti
        # 40 to 40 -> 42 [1] lasti
        # 50 to 146 -> 150 [0]
        # 150 to 182 -> 192 [1] lasti
        # 190 to 190 -> 192 [1] lasti


def _unknown_as_blank(val):
    # 772           0 RESUME                   0
    # 773           2 LOAD_FAST                0 (val)
    # 4 LOAD_CONST               1 ('unknown')
    # 6 COMPARE_OP               2 (==)
    # 12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
    # 14 LOAD_CONST               2 ('')
    # 16 JUMP_FORWARD             1 (to 20)
    # >>   18 LOAD_FAST                0 (val)
    # >>   20 RETURN_VALUE

class uname_result:
    """uname_result"""
    def processor(self):
        # 792           0 RESUME                   0
        # 794           2 LOAD_GLOBAL              1 (NULL + _unknown_as_blank)
        # 14 LOAD_GLOBAL              2 (_Processor)
        # 26 LOAD_METHOD              2 (get)
        # 48 PRECALL                  0
        # 52 CALL                     0
        # 62 PRECALL                  1
        # 66 CALL                     1
        # 76 RETURN_VALUE

    def __iter__(self):
        # 0 COPY_FREE_VARS           1
        # 796           2 RESUME                   0
        # 797           4 LOAD_GLOBAL              1 (NULL + itertools)
        # 16 LOAD_ATTR                1 (chain)
        # 798          26 LOAD_GLOBAL              5 (NULL + super)
        # 38 PRECALL                  0
        # 42 CALL                     0
        # 52 LOAD_METHOD              3 (__iter__)
        # 74 PRECALL                  0
        # 78 CALL                     0
        # 799          88 LOAD_FAST                0 (self)
        # 90 LOAD_ATTR                4 (processor)
        # 100 BUILD_TUPLE              1
        # 797         102 PRECALL                  2
        # 106 CALL                     2
        # 116 RETURN_VALUE

    def _make(cls, iterable):
        # 802           0 RESUME                   0
        # 805           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_FAST                0 (cls)
        # 16 LOAD_ATTR                1 (_fields)
        # 26 PRECALL                  1
        # 30 CALL                     1
        # 40 LOAD_CONST               1 (1)
        # 42 BINARY_OP               10 (-)
        # 46 STORE_FAST               2 (num_fields)
        # 806          48 PUSH_NULL
        # 50 LOAD_FAST                0 (cls)
        # 52 LOAD_ATTR                2 (__new__)
        # 62 LOAD_FAST                0 (cls)
        # 64 BUILD_LIST               1
        # 66 LOAD_FAST                1 (iterable)
        # 68 LIST_EXTEND              1
        # 70 LIST_TO_TUPLE
        # 72 CALL_FUNCTION_EX         0
        # 74 STORE_FAST               3 (result)
        # 807          76 LOAD_GLOBAL              1 (NULL + len)
        # 88 LOAD_FAST                3 (result)
        # 90 PRECALL                  1
        # 94 CALL                     1
        # 104 LOAD_FAST                2 (num_fields)
        # 106 LOAD_CONST               1 (1)
        # 108 BINARY_OP                0 (+)
        # 112 COMPARE_OP               3 (!=)
        # 118 POP_JUMP_FORWARD_IF_FALSE    36 (to 192)
        # 808         120 LOAD_CONST               2 ('Expected ')
        # 122 LOAD_FAST                2 (num_fields)
        # 124 FORMAT_VALUE             0
        # 126 LOAD_CONST               3 (' arguments, got ')
        # 128 LOAD_GLOBAL              1 (NULL + len)
        # 140 LOAD_FAST                3 (result)
        # 142 PRECALL                  1
        # 146 CALL                     1
        # 156 FORMAT_VALUE             0
        # 158 BUILD_STRING             4
        # 160 STORE_FAST               4 (msg)
        # 809         162 LOAD_GLOBAL              7 (NULL + TypeError)
        # 174 LOAD_FAST                4 (msg)
        # 176 PRECALL                  1
        # 180 CALL                     1
        # 190 RAISE_VARARGS            1
        # 810     >>  192 LOAD_FAST                3 (result)
        # 194 RETURN_VALUE

    def __getitem__(self, key):
        # 812           0 RESUME                   0
        # 813           2 LOAD_GLOBAL              1 (NULL + tuple)
        # 14 LOAD_FAST                0 (self)
        # 16 PRECALL                  1
        # 20 CALL                     1
        # 30 LOAD_FAST                1 (key)
        # 32 BINARY_SUBSCR
        # 42 RETURN_VALUE

    def __len__(self):
        # 815           0 RESUME                   0
        # 816           2 LOAD_GLOBAL              1 (NULL + len)
        # 14 LOAD_GLOBAL              3 (NULL + tuple)
        # 26 LOAD_GLOBAL              5 (NULL + iter)
        # 38 LOAD_FAST                0 (self)
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 PRECALL                  1
        # 58 CALL                     1
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 RETURN_VALUE

    def __reduce__(self):
        # 818           0 RESUME                   0
        # 819           2 LOAD_GLOBAL              0 (uname_result)
        # 14 LOAD_GLOBAL              3 (NULL + tuple)
        # 26 LOAD_FAST                0 (self)
        # 28 PRECALL                  1
        # 32 CALL                     1
        # 42 LOAD_CONST               0 (None)
        # 44 LOAD_GLOBAL              5 (NULL + len)
        # 56 LOAD_FAST                0 (self)
        # 58 LOAD_ATTR                3 (_fields)
        # 68 PRECALL                  1
        # 72 CALL                     1
        # 82 LOAD_CONST               1 (1)
        # 84 BINARY_OP               10 (-)
        # 88 BUILD_SLICE              2
        # 90 BINARY_SUBSCR
        # 100 BUILD_TUPLE              2
        # 102 RETURN_VALUE


def uname():
    """ Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    """
    # 825           0 RESUME                   0
    # 839           2 LOAD_GLOBAL              0 (_uname_cache)
    # 14 POP_JUMP_FORWARD_IF_NONE     7 (to 30)
    # 840          16 LOAD_GLOBAL              0 (_uname_cache)
    # 28 RETURN_VALUE
    # 843     >>   30 NOP
    # 844          32 LOAD_GLOBAL              3 (NULL + os)
    # 44 LOAD_ATTR                2 (uname)
    # 54 PRECALL                  0
    # 58 CALL                     0
    # 68 COPY                     1
    # 70 UNPACK_SEQUENCE          5
    # 74 STORE_FAST               0 (system)
    # 76 STORE_FAST               1 (node)
    # 78 STORE_FAST               2 (release)
    # 80 STORE_FAST               3 (version)
    # 82 STORE_FAST               4 (machine)
    # 84 STORE_FAST               5 (infos)
    # 86 JUMP_FORWARD            50 (to 188)
    # >>   88 PUSH_EXC_INFO
    # 845          90 LOAD_GLOBAL              6 (AttributeError)
    # 102 CHECK_EXC_MATCH
    # 104 POP_JUMP_FORWARD_IF_FALSE    37 (to 180)
    # 106 POP_TOP
    # 846         108 LOAD_GLOBAL              8 (sys)
    # 120 LOAD_ATTR                5 (platform)
    # 130 STORE_FAST               0 (system)
    # 847         132 LOAD_GLOBAL             13 (NULL + _node)
    # 144 PRECALL                  0
    # 148 CALL                     0
    # 158 STORE_FAST               1 (node)
    # 848         160 LOAD_CONST               2 ('')
    # 162 COPY                     1
    # 164 STORE_FAST               2 (release)
    # 166 COPY                     1
    # 168 STORE_FAST               3 (version)
    # 170 STORE_FAST               4 (machine)
    # 849         172 LOAD_CONST               3 (())
    # 174 STORE_FAST               5 (infos)
    # 176 POP_EXCEPT
    # 178 JUMP_FORWARD             4 (to 188)
    # 845     >>  180 RERAISE                  0
    # >>  182 COPY                     3
    # 184 POP_EXCEPT
    # 186 RERAISE                  1
    # 851     >>  188 LOAD_GLOBAL             15 (NULL + any)
    # 200 LOAD_FAST                5 (infos)
    # 202 PRECALL                  1
    # 206 CALL                     1
    # 216 POP_JUMP_FORWARD_IF_TRUE   186 (to 590)
    # 855         218 LOAD_FAST                0 (system)
    # 220 LOAD_CONST               4 ('win32')
    # 222 COMPARE_OP               2 (==)
    # 228 POP_JUMP_FORWARD_IF_FALSE    35 (to 300)
    # 856         230 LOAD_GLOBAL             17 (NULL + win32_ver)
    # 242 PRECALL                  0
    # 246 CALL                     0
    # 256 UNPACK_SEQUENCE          4
    # 260 STORE_FAST               2 (release)
    # 262 STORE_FAST               3 (version)
    # 264 STORE_FAST               6 (csd)
    # 266 STORE_FAST               7 (ptype)
    # 857         268 LOAD_FAST                4 (machine)
    # 270 JUMP_IF_TRUE_OR_POP     13 (to 298)
    # 272 LOAD_GLOBAL             19 (NULL + _get_machine_win32)
    # 284 PRECALL                  0
    # 288 CALL                     0
    # >>  298 STORE_FAST               4 (machine)
    # 861     >>  300 LOAD_FAST                2 (release)
    # 302 POP_JUMP_FORWARD_IF_FALSE     2 (to 308)
    # 304 LOAD_FAST                3 (version)
    # 306 POP_JUMP_FORWARD_IF_TRUE    61 (to 430)
    # 862     >>  308 LOAD_GLOBAL             21 (NULL + _syscmd_ver)
    # 320 LOAD_FAST                0 (system)
    # 322 PRECALL                  1
    # 326 CALL                     1
    # 336 UNPACK_SEQUENCE          3
    # 340 STORE_FAST               0 (system)
    # 342 STORE_FAST               2 (release)
    # 344 STORE_FAST               3 (version)
    # 865         346 LOAD_FAST                0 (system)
    # 348 LOAD_CONST               5 ('Microsoft Windows')
    # 350 COMPARE_OP               2 (==)
    # 356 POP_JUMP_FORWARD_IF_FALSE     3 (to 364)
    # 866         358 LOAD_CONST               6 ('Windows')
    # 360 STORE_FAST               0 (system)
    # 362 JUMP_FORWARD            33 (to 430)
    # 867     >>  364 LOAD_FAST                0 (system)
    # 366 LOAD_CONST               7 ('Microsoft')
    # 368 COMPARE_OP               2 (==)
    # 374 POP_JUMP_FORWARD_IF_FALSE    27 (to 430)
    # 376 LOAD_FAST                2 (release)
    # 378 LOAD_CONST               6 ('Windows')
    # 380 COMPARE_OP               2 (==)
    # 386 POP_JUMP_FORWARD_IF_FALSE    21 (to 430)
    # 872         388 LOAD_CONST               6 ('Windows')
    # 390 STORE_FAST               0 (system)
    # 873         392 LOAD_CONST               8 ('6.0')
    # 394 LOAD_FAST                3 (version)
    # 396 LOAD_CONST               1 (None)
    # 398 LOAD_CONST               9 (3)
    # 400 BUILD_SLICE              2
    # 402 BINARY_SUBSCR
    # 412 COMPARE_OP               2 (==)
    # 418 POP_JUMP_FORWARD_IF_FALSE     3 (to 426)
    # 874         420 LOAD_CONST              10 ('Vista')
    # 422 STORE_FAST               2 (release)
    # 424 JUMP_FORWARD             2 (to 430)
    # 876     >>  426 LOAD_CONST               2 ('')
    # 428 STORE_FAST               2 (release)
    # 880     >>  430 LOAD_FAST                0 (system)
    # 432 LOAD_CONST              11 (('win32', 'win16'))
    # 434 CONTAINS_OP              0
    # 436 POP_JUMP_FORWARD_IF_FALSE    16 (to 470)
    # 881         438 LOAD_FAST                3 (version)
    # 440 POP_JUMP_FORWARD_IF_TRUE    11 (to 464)
    # 882         442 LOAD_FAST                0 (system)
    # 444 LOAD_CONST               4 ('win32')
    # 446 COMPARE_OP               2 (==)
    # 452 POP_JUMP_FORWARD_IF_FALSE     3 (to 460)
    # 883         454 LOAD_CONST              12 ('32bit')
    # 456 STORE_FAST               3 (version)
    # 458 JUMP_FORWARD             2 (to 464)
    # 885     >>  460 LOAD_CONST              13 ('16bit')
    # 462 STORE_FAST               3 (version)
    # 886     >>  464 LOAD_CONST               6 ('Windows')
    # 466 STORE_FAST               0 (system)
    # 468 JUMP_FORWARD            60 (to 590)
    # 888     >>  470 LOAD_FAST                0 (system)
    # 472 LOAD_CONST               1 (None)
    # 474 LOAD_CONST              14 (4)
    # 476 BUILD_SLICE              2
    # 478 BINARY_SUBSCR
    # 488 LOAD_CONST              15 ('java')
    # 490 COMPARE_OP               2 (==)
    # 496 POP_JUMP_FORWARD_IF_FALSE    46 (to 590)
    # 889         498 LOAD_GLOBAL             23 (NULL + java_ver)
    # 510 PRECALL                  0
    # 514 CALL                     0
    # 524 UNPACK_SEQUENCE          4
    # 528 STORE_FAST               2 (release)
    # 530 STORE_FAST               8 (vendor)
    # 532 STORE_FAST               9 (vminfo)
    # 534 STORE_FAST              10 (osinfo)
    # 890         536 LOAD_CONST              16 ('Java')
    # 538 STORE_FAST               0 (system)
    # 891         540 LOAD_CONST              17 (', ')
    # 542 LOAD_METHOD             12 (join)
    # 564 LOAD_FAST                9 (vminfo)
    # 566 PRECALL                  1
    # 570 CALL                     1
    # 580 STORE_FAST               3 (version)
    # 892         582 LOAD_FAST                3 (version)
    # 584 POP_JUMP_FORWARD_IF_TRUE     2 (to 590)
    # 893         586 LOAD_FAST                8 (vendor)
    # 588 STORE_FAST               3 (version)
    # 896     >>  590 LOAD_FAST                0 (system)
    # 592 LOAD_CONST              18 ('OpenVMS')
    # 594 COMPARE_OP               2 (==)
    # 600 POP_JUMP_FORWARD_IF_FALSE    12 (to 626)
    # 898         602 LOAD_FAST                2 (release)
    # 604 POP_JUMP_FORWARD_IF_FALSE     6 (to 618)
    # 606 LOAD_FAST                2 (release)
    # 608 LOAD_CONST              19 ('0')
    # 610 COMPARE_OP               2 (==)
    # 616 POP_JUMP_FORWARD_IF_FALSE     4 (to 626)
    # 899     >>  618 LOAD_FAST                3 (version)
    # 620 STORE_FAST               2 (release)
    # 900         622 LOAD_CONST               2 ('')
    # 624 STORE_FAST               3 (version)
    # 903     >>  626 LOAD_FAST                0 (system)
    # 628 LOAD_CONST               7 ('Microsoft')
    # 630 COMPARE_OP               2 (==)
    # 636 POP_JUMP_FORWARD_IF_FALSE    10 (to 658)
    # 638 LOAD_FAST                2 (release)
    # 640 LOAD_CONST               6 ('Windows')
    # 642 COMPARE_OP               2 (==)
    # 648 POP_JUMP_FORWARD_IF_FALSE     4 (to 658)
    # 904         650 LOAD_CONST               6 ('Windows')
    # 652 STORE_FAST               0 (system)
    # 905         654 LOAD_CONST              10 ('Vista')
    # 656 STORE_FAST               2 (release)
    # 907     >>  658 LOAD_FAST                0 (system)
    # 660 LOAD_FAST                1 (node)
    # 662 LOAD_FAST                2 (release)
    # 664 LOAD_FAST                3 (version)
    # 666 LOAD_FAST                4 (machine)
    # 668 BUILD_TUPLE              5
    # 670 STORE_FAST              11 (vals)
    # 909         672 LOAD_GLOBAL             27 (NULL + uname_result)
    # 684 LOAD_GLOBAL             29 (NULL + map)
    # 696 LOAD_GLOBAL             30 (_unknown_as_blank)
    # 708 LOAD_FAST               11 (vals)
    # 710 PRECALL                  2
    # 714 CALL                     2
    # 724 CALL_FUNCTION_EX         0
    # 726 STORE_GLOBAL             0 (_uname_cache)
    # 910         728 LOAD_GLOBAL              0 (_uname_cache)
    # 740 RETURN_VALUE
    # ExceptionTable:
    # 32 to 84 -> 88 [0]
    # 88 to 174 -> 182 [1] lasti
    # 180 to 180 -> 182 [1] lasti

def system():
    """ Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.

    """
    # 914           0 RESUME                   0
    # 921           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (system)
    # 38 RETURN_VALUE

def node():
    """ Returns the computer's network name (which may not be fully
        qualified)

        An empty string is returned if the value cannot be determined.

    """
    # 923           0 RESUME                   0
    # 931           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (node)
    # 38 RETURN_VALUE

def release():
    """ Returns the system's release, e.g. '2.2.0' or 'NT'

        An empty string is returned if the value cannot be determined.

    """
    # 933           0 RESUME                   0
    # 940           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (release)
    # 38 RETURN_VALUE

def version():
    """ Returns the system's release version, e.g. '#3 on degas'

        An empty string is returned if the value cannot be determined.

    """
    # 942           0 RESUME                   0
    # 949           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (version)
    # 38 RETURN_VALUE

def machine():
    """ Returns the machine type, e.g. 'i386'

        An empty string is returned if the value cannot be determined.

    """
    # 951           0 RESUME                   0
    # 958           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (machine)
    # 38 RETURN_VALUE

def processor():
    """ Returns the (true) processor name, e.g. 'amdk6'

        An empty string is returned if the value cannot be
        determined. Note that many platforms do not provide this
        information or simply return the same value as for machine(),
        e.g.  NetBSD does this.

    """
    # 960           0 RESUME                   0
    # 970           2 LOAD_GLOBAL              1 (NULL + uname)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_ATTR                1 (processor)
    # 38 RETURN_VALUE

def _sys_version(sys_version):
    """ Returns a parsed version of Python's sys.version as tuple
        (name, version, branch, revision, buildno, builddate, compiler)
        referring to the Python implementation name, version, branch,
        revision, build number, build date/time as string and the compiler
        identification string.

        Note that unlike the Python sys.version, the returned value
        for the Python version will always include the patchlevel (it
        defaults to '.0').

        The function returns empty strings for tuple entries that
        cannot be determined.

        sys_version may be given to parse an alternative version
        string, e.g. if the version was read from a different Python
        interpreter.

    """
    # 1002           0 RESUME                   0
    # 1023           2 LOAD_FAST                0 (sys_version)
    # 4 POP_JUMP_FORWARD_IF_NOT_NONE    12 (to 30)
    # 1024           6 LOAD_GLOBAL              0 (sys)
    # 18 LOAD_ATTR                1 (version)
    # 28 STORE_FAST               0 (sys_version)
    # 1027     >>   30 LOAD_GLOBAL              4 (_sys_version_cache)
    # 42 LOAD_METHOD              3 (get)
    # 64 LOAD_FAST                0 (sys_version)
    # 66 LOAD_CONST               1 (None)
    # 68 PRECALL                  2
    # 72 CALL                     2
    # 82 STORE_FAST               1 (result)
    # 1028          84 LOAD_FAST                1 (result)
    # 86 POP_JUMP_FORWARD_IF_NONE     2 (to 92)
    # 1029          88 LOAD_FAST                1 (result)
    # 90 RETURN_VALUE
    # 1032     >>   92 LOAD_CONST               2 ('IronPython')
    # 94 LOAD_FAST                0 (sys_version)
    # 96 CONTAINS_OP              0
    # 98 POP_JUMP_FORWARD_IF_FALSE   139 (to 378)
    # 1034         100 LOAD_CONST               2 ('IronPython')
    # 102 STORE_FAST               2 (name)
    # 1035         104 LOAD_FAST                0 (sys_version)
    # 106 LOAD_METHOD              4 (startswith)
    # 128 LOAD_CONST               2 ('IronPython')
    # 130 PRECALL                  1
    # 134 CALL                     1
    # 144 POP_JUMP_FORWARD_IF_FALSE    27 (to 200)
    # 1036         146 LOAD_GLOBAL             10 (_ironpython_sys_version_parser)
    # 158 LOAD_METHOD              6 (match)
    # 180 LOAD_FAST                0 (sys_version)
    # 182 PRECALL                  1
    # 186 CALL                     1
    # 196 STORE_FAST               3 (match)
    # 198 JUMP_FORWARD            26 (to 252)
    # 1038     >>  200 LOAD_GLOBAL             14 (_ironpython26_sys_version_parser)
    # 212 LOAD_METHOD              6 (match)
    # 234 LOAD_FAST                0 (sys_version)
    # 236 PRECALL                  1
    # 240 CALL                     1
    # 250 STORE_FAST               3 (match)
    # 1040     >>  252 LOAD_FAST                3 (match)
    # 254 POP_JUMP_FORWARD_IF_NOT_NONE    31 (to 318)
    # 1041         256 LOAD_GLOBAL             17 (NULL + ValueError)
    # 1042         268 LOAD_CONST               3 ('failed to parse IronPython sys.version: %s')
    # 1043         270 LOAD_GLOBAL             19 (NULL + repr)
    # 282 LOAD_FAST                0 (sys_version)
    # 284 PRECALL                  1
    # 288 CALL                     1
    # 1042         298 BINARY_OP                6 (%)
    # 1041         302 PRECALL                  1
    # 306 CALL                     1
    # 316 RAISE_VARARGS            1
    # 1045     >>  318 LOAD_FAST                3 (match)
    # 320 LOAD_METHOD             10 (groups)
    # 342 PRECALL                  0
    # 346 CALL                     0
    # 356 UNPACK_SEQUENCE          3
    # 360 STORE_FAST               4 (version)
    # 362 STORE_FAST               5 (alt_version)
    # 364 STORE_FAST               6 (compiler)
    # 1046         366 LOAD_CONST               4 ('')
    # 368 STORE_FAST               7 (buildno)
    # 1047         370 LOAD_CONST               4 ('')
    # 372 STORE_FAST               8 (builddate)
    # 374 EXTENDED_ARG             1
    # 376 JUMP_FORWARD           330 (to 1038)
    # 1049     >>  378 LOAD_GLOBAL              0 (sys)
    # 390 LOAD_ATTR               11 (platform)
    # 400 LOAD_METHOD              4 (startswith)
    # 422 LOAD_CONST               5 ('java')
    # 424 PRECALL                  1
    # 428 CALL                     1
    # 438 POP_JUMP_FORWARD_IF_FALSE   104 (to 648)
    # 1051         440 LOAD_CONST               6 ('Jython')
    # 442 STORE_FAST               2 (name)
    # 1052         444 LOAD_GLOBAL             24 (_sys_version_parser)
    # 456 LOAD_METHOD              6 (match)
    # 478 LOAD_FAST                0 (sys_version)
    # 480 PRECALL                  1
    # 484 CALL                     1
    # 494 STORE_FAST               3 (match)
    # 1053         496 LOAD_FAST                3 (match)
    # 498 POP_JUMP_FORWARD_IF_NOT_NONE    31 (to 562)
    # 1054         500 LOAD_GLOBAL             17 (NULL + ValueError)
    # 1055         512 LOAD_CONST               7 ('failed to parse Jython sys.version: %s')
    # 1056         514 LOAD_GLOBAL             19 (NULL + repr)
    # 526 LOAD_FAST                0 (sys_version)
    # 528 PRECALL                  1
    # 532 CALL                     1
    # 1055         542 BINARY_OP                6 (%)
    # 1054         546 PRECALL                  1
    # 550 CALL                     1
    # 560 RAISE_VARARGS            1
    # 1057     >>  562 LOAD_FAST                3 (match)
    # 564 LOAD_METHOD             10 (groups)
    # 586 PRECALL                  0
    # 590 CALL                     0
    # 600 UNPACK_SEQUENCE          5
    # 604 STORE_FAST               4 (version)
    # 606 STORE_FAST               7 (buildno)
    # 608 STORE_FAST               8 (builddate)
    # 610 STORE_FAST               9 (buildtime)
    # 612 STORE_FAST              10 (_)
    # 1058         614 LOAD_FAST                8 (builddate)
    # 616 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 622)
    # 1059         618 LOAD_CONST               4 ('')
    # 620 STORE_FAST               8 (builddate)
    # 1060     >>  622 LOAD_GLOBAL              0 (sys)
    # 634 LOAD_ATTR               11 (platform)
    # 644 STORE_FAST               6 (compiler)
    # 646 JUMP_FORWARD           195 (to 1038)
    # 1062     >>  648 LOAD_CONST               8 ('PyPy')
    # 650 LOAD_FAST                0 (sys_version)
    # 652 CONTAINS_OP              0
    # 654 POP_JUMP_FORWARD_IF_FALSE    89 (to 834)
    # 1064         656 LOAD_CONST               8 ('PyPy')
    # 658 STORE_FAST               2 (name)
    # 1065         660 LOAD_GLOBAL             26 (_pypy_sys_version_parser)
    # 672 LOAD_METHOD              6 (match)
    # 694 LOAD_FAST                0 (sys_version)
    # 696 PRECALL                  1
    # 700 CALL                     1
    # 710 STORE_FAST               3 (match)
    # 1066         712 LOAD_FAST                3 (match)
    # 714 POP_JUMP_FORWARD_IF_NOT_NONE    31 (to 778)
    # 1067         716 LOAD_GLOBAL             17 (NULL + ValueError)
    # 728 LOAD_CONST               9 ('failed to parse PyPy sys.version: %s')
    # 1068         730 LOAD_GLOBAL             19 (NULL + repr)
    # 742 LOAD_FAST                0 (sys_version)
    # 744 PRECALL                  1
    # 748 CALL                     1
    # 1067         758 BINARY_OP                6 (%)
    # 762 PRECALL                  1
    # 766 CALL                     1
    # 776 RAISE_VARARGS            1
    # 1069     >>  778 LOAD_FAST                3 (match)
    # 780 LOAD_METHOD             10 (groups)
    # 802 PRECALL                  0
    # 806 CALL                     0
    # 816 UNPACK_SEQUENCE          4
    # 820 STORE_FAST               4 (version)
    # 822 STORE_FAST               7 (buildno)
    # 824 STORE_FAST               8 (builddate)
    # 826 STORE_FAST               9 (buildtime)
    # 1070         828 LOAD_CONST               4 ('')
    # 830 STORE_FAST               6 (compiler)
    # 832 JUMP_FORWARD           102 (to 1038)
    # 1074     >>  834 LOAD_GLOBAL             24 (_sys_version_parser)
    # 846 LOAD_METHOD              6 (match)
    # 868 LOAD_FAST                0 (sys_version)
    # 870 PRECALL                  1
    # 874 CALL                     1
    # 884 STORE_FAST               3 (match)
    # 1075         886 LOAD_FAST                3 (match)
    # 888 POP_JUMP_FORWARD_IF_NOT_NONE    31 (to 952)
    # 1076         890 LOAD_GLOBAL             17 (NULL + ValueError)
    # 1077         902 LOAD_CONST              10 ('failed to parse CPython sys.version: %s')
    # 1078         904 LOAD_GLOBAL             19 (NULL + repr)
    # 916 LOAD_FAST                0 (sys_version)
    # 918 PRECALL                  1
    # 922 CALL                     1
    # 1077         932 BINARY_OP                6 (%)
    # 1076         936 PRECALL                  1
    # 940 CALL                     1
    # 950 RAISE_VARARGS            1
    # 1080     >>  952 LOAD_FAST                3 (match)
    # 954 LOAD_METHOD             10 (groups)
    # 976 PRECALL                  0
    # 980 CALL                     0
    # 1079         990 UNPACK_SEQUENCE          5
    # 994 STORE_FAST               4 (version)
    # 996 STORE_FAST               7 (buildno)
    # 998 STORE_FAST               8 (builddate)
    # 1000 STORE_FAST               9 (buildtime)
    # 1002 STORE_FAST               6 (compiler)
    # 1081        1004 LOAD_CONST              11 ('CPython')
    # 1006 STORE_FAST               2 (name)
    # 1082        1008 LOAD_FAST                8 (builddate)
    # 1010 POP_JUMP_FORWARD_IF_NOT_NONE     3 (to 1018)
    # 1083        1012 LOAD_CONST               4 ('')
    # 1014 STORE_FAST               8 (builddate)
    # 1016 JUMP_FORWARD            10 (to 1038)
    # 1084     >> 1018 LOAD_FAST                9 (buildtime)
    # 1020 POP_JUMP_FORWARD_IF_FALSE     8 (to 1038)
    # 1085        1022 LOAD_FAST                8 (builddate)
    # 1024 LOAD_CONST              12 (' ')
    # 1026 BINARY_OP                0 (+)
    # 1030 LOAD_FAST                9 (buildtime)
    # 1032 BINARY_OP                0 (+)
    # 1036 STORE_FAST               8 (builddate)
    # 1087     >> 1038 LOAD_GLOBAL             29 (NULL + hasattr)
    # 1050 LOAD_GLOBAL              0 (sys)
    # 1062 LOAD_CONST              13 ('_git')
    # 1064 PRECALL                  2
    # 1068 CALL                     2
    # 1078 POP_JUMP_FORWARD_IF_FALSE    17 (to 1114)
    # 1088        1080 LOAD_GLOBAL              0 (sys)
    # 1092 LOAD_ATTR               15 (_git)
    # 1102 UNPACK_SEQUENCE          3
    # 1106 STORE_FAST              10 (_)
    # 1108 STORE_FAST              11 (branch)
    # 1110 STORE_FAST              12 (revision)
    # 1112 JUMP_FORWARD            42 (to 1198)
    # 1089     >> 1114 LOAD_GLOBAL             29 (NULL + hasattr)
    # 1126 LOAD_GLOBAL              0 (sys)
    # 1138 LOAD_CONST              14 ('_mercurial')
    # 1140 PRECALL                  2
    # 1144 CALL                     2
    # 1154 POP_JUMP_FORWARD_IF_FALSE    17 (to 1190)
    # 1090        1156 LOAD_GLOBAL              0 (sys)
    # 1168 LOAD_ATTR               16 (_mercurial)
    # 1178 UNPACK_SEQUENCE          3
    # 1182 STORE_FAST              10 (_)
    # 1184 STORE_FAST              11 (branch)
    # 1186 STORE_FAST              12 (revision)
    # 1188 JUMP_FORWARD             4 (to 1198)
    # 1092     >> 1190 LOAD_CONST               4 ('')
    # 1192 STORE_FAST              11 (branch)
    # 1093        1194 LOAD_CONST               4 ('')
    # 1196 STORE_FAST              12 (revision)
    # 1096     >> 1198 LOAD_FAST                4 (version)
    # 1200 LOAD_METHOD             17 (split)
    # 1222 LOAD_CONST              15 ('.')
    # 1224 PRECALL                  1
    # 1228 CALL                     1
    # 1238 STORE_FAST              13 (l)
    # 1097        1240 LOAD_GLOBAL             37 (NULL + len)
    # 1252 LOAD_FAST               13 (l)
    # 1254 PRECALL                  1
    # 1258 CALL                     1
    # 1268 LOAD_CONST              16 (2)
    # 1270 COMPARE_OP               2 (==)
    # 1276 POP_JUMP_FORWARD_IF_FALSE    42 (to 1362)
    # 1098        1278 LOAD_FAST               13 (l)
    # 1280 LOAD_METHOD             19 (append)
    # 1302 LOAD_CONST              17 ('0')
    # 1304 PRECALL                  1
    # 1308 CALL                     1
    # 1318 POP_TOP
    # 1099        1320 LOAD_CONST              15 ('.')
    # 1322 LOAD_METHOD             20 (join)
    # 1344 LOAD_FAST               13 (l)
    # 1346 PRECALL                  1
    # 1350 CALL                     1
    # 1360 STORE_FAST               4 (version)
    # 1102     >> 1362 LOAD_FAST                2 (name)
    # 1364 LOAD_FAST                4 (version)
    # 1366 LOAD_FAST               11 (branch)
    # 1368 LOAD_FAST               12 (revision)
    # 1370 LOAD_FAST                7 (buildno)
    # 1372 LOAD_FAST                8 (builddate)
    # 1374 LOAD_FAST                6 (compiler)
    # 1376 BUILD_TUPLE              7
    # 1378 STORE_FAST               1 (result)
    # 1103        1380 LOAD_FAST                1 (result)
    # 1382 LOAD_GLOBAL              4 (_sys_version_cache)
    # 1394 LOAD_FAST                0 (sys_version)
    # 1396 STORE_SUBSCR
    # 1104        1400 LOAD_FAST                1 (result)
    # 1402 RETURN_VALUE

def python_implementation():
    """ Returns a string identifying the Python implementation.

        Currently, the following implementations are identified:
          'CPython' (C implementation of Python),
          'IronPython' (.NET implementation of Python),
          'Jython' (Java implementation of Python),
          'PyPy' (Python implementation of Python).

    """
    # 1106           0 RESUME                   0
    # 1117           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (0)
    # 30 BINARY_SUBSCR
    # 40 RETURN_VALUE

def python_version():
    """ Returns the Python version as string 'major.minor.patchlevel'

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    """
    # 1119           0 RESUME                   0
    # 1127           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (1)
    # 30 BINARY_SUBSCR
    # 40 RETURN_VALUE

def python_version_tuple():
    """ Returns the Python version as tuple (major, minor, patchlevel)
        of strings.

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    """
    # 1129           0 RESUME                   0
    # 1138           2 LOAD_GLOBAL              1 (NULL + tuple)
    # 14 LOAD_GLOBAL              3 (NULL + _sys_version)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 LOAD_CONST               1 (1)
    # 42 BINARY_SUBSCR
    # 52 LOAD_METHOD              2 (split)
    # 74 LOAD_CONST               2 ('.')
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 PRECALL                  1
    # 94 CALL                     1
    # 104 RETURN_VALUE

def python_branch():
    """ Returns a string identifying the Python implementation
        branch.

        For CPython this is the SCM branch from which the
        Python binary was built.

        If not available, an empty string is returned.

    """
    # 1140           0 RESUME                   0
    # 1152           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (2)
    # 30 BINARY_SUBSCR
    # 40 RETURN_VALUE

def python_revision():
    """ Returns a string identifying the Python implementation
        revision.

        For CPython this is the SCM revision from which the
        Python binary was built.

        If not available, an empty string is returned.

    """
    # 1154           0 RESUME                   0
    # 1165           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (3)
    # 30 BINARY_SUBSCR
    # 40 RETURN_VALUE

def python_build():
    """ Returns a tuple (buildno, builddate) stating the Python
        build number and date as strings.

    """
    # 1167           0 RESUME                   0
    # 1173           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (4)
    # 30 LOAD_CONST               2 (6)
    # 32 BUILD_SLICE              2
    # 34 BINARY_SUBSCR
    # 44 RETURN_VALUE

def python_compiler():
    """ Returns a string identifying the compiler used for compiling
        Python.

    """
    # 1175           0 RESUME                   0
    # 1181           2 LOAD_GLOBAL              1 (NULL + _sys_version)
    # 14 PRECALL                  0
    # 18 CALL                     0
    # 28 LOAD_CONST               1 (6)
    # 30 BINARY_SUBSCR
    # 40 RETURN_VALUE

def platform(aliased, terse):
    """ Returns a single string identifying the underlying platform
        with as much useful information as possible (but no more :).

        The output is intended to be human readable rather than
        machine parseable. It may look different on different
        platforms and this is intended.

        If "aliased" is true, the function will use aliases for
        various platforms that report system names which differ from
        their common names, e.g. SunOS will be reported as
        Solaris. The system_alias() function is used to implement
        this.

        Setting terse to true causes the function to return only the
        absolute minimum information needed to identify the platform.

    """
    # 1187           0 RESUME                   0
    # 1206           2 LOAD_GLOBAL              0 (_platform_cache)
    # 14 LOAD_METHOD              1 (get)
    # 36 LOAD_FAST                0 (aliased)
    # 38 LOAD_FAST                1 (terse)
    # 40 BUILD_TUPLE              2
    # 42 LOAD_CONST               1 (None)
    # 44 PRECALL                  2
    # 48 CALL                     2
    # 58 STORE_FAST               2 (result)
    # 1207          60 LOAD_FAST                2 (result)
    # 62 POP_JUMP_FORWARD_IF_NONE     2 (to 68)
    # 1208          64 LOAD_FAST                2 (result)
    # 66 RETURN_VALUE
    # 1212     >>   68 LOAD_GLOBAL              5 (NULL + uname)
    # 80 PRECALL                  0
    # 84 CALL                     0
    # 94 UNPACK_SEQUENCE          6
    # 98 STORE_FAST               3 (system)
    # 100 STORE_FAST               4 (node)
    # 102 STORE_FAST               5 (release)
    # 104 STORE_FAST               6 (version)
    # 106 STORE_FAST               7 (machine)
    # 108 STORE_FAST               8 (processor)
    # 1213         110 LOAD_FAST                7 (machine)
    # 112 LOAD_FAST                8 (processor)
    # 114 COMPARE_OP               2 (==)
    # 120 POP_JUMP_FORWARD_IF_FALSE     2 (to 126)
    # 1214         122 LOAD_CONST               2 ('')
    # 124 STORE_FAST               8 (processor)
    # 1215     >>  126 LOAD_FAST                0 (aliased)
    # 128 POP_JUMP_FORWARD_IF_FALSE    21 (to 172)
    # 1216         130 LOAD_GLOBAL              7 (NULL + system_alias)
    # 142 LOAD_FAST                3 (system)
    # 144 LOAD_FAST                5 (release)
    # 146 LOAD_FAST                6 (version)
    # 148 PRECALL                  3
    # 152 CALL                     3
    # 162 UNPACK_SEQUENCE          3
    # 166 STORE_FAST               3 (system)
    # 168 STORE_FAST               5 (release)
    # 170 STORE_FAST               6 (version)
    # 1218     >>  172 LOAD_FAST                3 (system)
    # 174 LOAD_CONST               3 ('Darwin')
    # 176 COMPARE_OP               2 (==)
    # 182 POP_JUMP_FORWARD_IF_FALSE    26 (to 236)
    # 1220         184 LOAD_GLOBAL              9 (NULL + mac_ver)
    # 196 PRECALL                  0
    # 200 CALL                     0
    # 210 LOAD_CONST               4 (0)
    # 212 BINARY_SUBSCR
    # 222 STORE_FAST               9 (macos_release)
    # 1221         224 LOAD_FAST                9 (macos_release)
    # 226 POP_JUMP_FORWARD_IF_FALSE     4 (to 236)
    # 1222         228 LOAD_CONST               5 ('macOS')
    # 230 STORE_FAST               3 (system)
    # 1223         232 LOAD_FAST                9 (macos_release)
    # 234 STORE_FAST               5 (release)
    # 1225     >>  236 LOAD_FAST                3 (system)
    # 238 LOAD_CONST               6 ('Windows')
    # 240 COMPARE_OP               2 (==)
    # 246 POP_JUMP_FORWARD_IF_FALSE    58 (to 364)
    # 1227         248 LOAD_GLOBAL             11 (NULL + win32_ver)
    # 260 LOAD_FAST                6 (version)
    # 262 PRECALL                  1
    # 266 CALL                     1
    # 276 UNPACK_SEQUENCE          4
    # 280 STORE_FAST              10 (rel)
    # 282 STORE_FAST              11 (vers)
    # 284 STORE_FAST              12 (csd)
    # 286 STORE_FAST              13 (ptype)
    # 1228         288 LOAD_FAST                1 (terse)
    # 290 POP_JUMP_FORWARD_IF_FALSE    17 (to 326)
    # 1229         292 LOAD_GLOBAL             13 (NULL + _platform)
    # 304 LOAD_FAST                3 (system)
    # 306 LOAD_FAST                5 (release)
    # 308 PRECALL                  2
    # 312 CALL                     2
    # 322 STORE_FAST              14 (platform)
    # 324 JUMP_FORWARD           204 (to 734)
    # 1231     >>  326 LOAD_GLOBAL             13 (NULL + _platform)
    # 338 LOAD_FAST                3 (system)
    # 340 LOAD_FAST                5 (release)
    # 342 LOAD_FAST                6 (version)
    # 344 LOAD_FAST               12 (csd)
    # 346 PRECALL                  4
    # 350 CALL                     4
    # 360 STORE_FAST              14 (platform)
    # 362 JUMP_FORWARD           185 (to 734)
    # 1233     >>  364 LOAD_FAST                3 (system)
    # 366 LOAD_CONST               7 (('Linux',))
    # 368 CONTAINS_OP              0
    # 370 POP_JUMP_FORWARD_IF_FALSE    41 (to 454)
    # 1235         372 LOAD_GLOBAL             15 (NULL + libc_ver)
    # 384 PRECALL                  0
    # 388 CALL                     0
    # 398 UNPACK_SEQUENCE          2
    # 402 STORE_FAST              15 (libcname)
    # 404 STORE_FAST              16 (libcversion)
    # 1236         406 LOAD_GLOBAL             13 (NULL + _platform)
    # 418 LOAD_FAST                3 (system)
    # 420 LOAD_FAST                5 (release)
    # 422 LOAD_FAST                7 (machine)
    # 424 LOAD_FAST                8 (processor)
    # 1237         426 LOAD_CONST               8 ('with')
    # 1238         428 LOAD_FAST               15 (libcname)
    # 430 LOAD_FAST               16 (libcversion)
    # 432 BINARY_OP                0 (+)
    # 1236         436 PRECALL                  6
    # 440 CALL                     6
    # 450 STORE_FAST              14 (platform)
    # 452 JUMP_FORWARD           140 (to 734)
    # 1239     >>  454 LOAD_FAST                3 (system)
    # 456 LOAD_CONST               9 ('Java')
    # 458 COMPARE_OP               2 (==)
    # 464 POP_JUMP_FORWARD_IF_FALSE    67 (to 600)
    # 1241         466 LOAD_GLOBAL             17 (NULL + java_ver)
    # 478 PRECALL                  0
    # 482 CALL                     0
    # 492 UNPACK_SEQUENCE          4
    # 496 STORE_FAST              17 (r)
    # 498 STORE_FAST              18 (v)
    # 500 STORE_FAST              19 (vminfo)
    # 502 UNPACK_SEQUENCE          3
    # 506 STORE_FAST              20 (os_name)
    # 508 STORE_FAST              21 (os_version)
    # 510 STORE_FAST              22 (os_arch)
    # 1242         512 LOAD_FAST                1 (terse)
    # 514 POP_JUMP_FORWARD_IF_TRUE     2 (to 520)
    # 516 LOAD_FAST               20 (os_name)
    # 518 POP_JUMP_FORWARD_IF_TRUE    18 (to 556)
    # 1243     >>  520 LOAD_GLOBAL             13 (NULL + _platform)
    # 532 LOAD_FAST                3 (system)
    # 534 LOAD_FAST                5 (release)
    # 536 LOAD_FAST                6 (version)
    # 538 PRECALL                  3
    # 542 CALL                     3
    # 552 STORE_FAST              14 (platform)
    # 554 JUMP_FORWARD            89 (to 734)
    # 1245     >>  556 LOAD_GLOBAL             13 (NULL + _platform)
    # 568 LOAD_FAST                3 (system)
    # 570 LOAD_FAST                5 (release)
    # 572 LOAD_FAST                6 (version)
    # 1246         574 LOAD_CONST              10 ('on')
    # 1247         576 LOAD_FAST               20 (os_name)
    # 578 LOAD_FAST               21 (os_version)
    # 580 LOAD_FAST               22 (os_arch)
    # 1245         582 PRECALL                  7
    # 586 CALL                     7
    # 596 STORE_FAST              14 (platform)
    # 598 JUMP_FORWARD            67 (to 734)
    # 1251     >>  600 LOAD_FAST                1 (terse)
    # 602 POP_JUMP_FORWARD_IF_FALSE    17 (to 638)
    # 1252         604 LOAD_GLOBAL             13 (NULL + _platform)
    # 616 LOAD_FAST                3 (system)
    # 618 LOAD_FAST                5 (release)
    # 620 PRECALL                  2
    # 624 CALL                     2
    # 634 STORE_FAST              14 (platform)
    # 636 JUMP_FORWARD            48 (to 734)
    # 1254     >>  638 LOAD_GLOBAL             19 (NULL + architecture)
    # 650 LOAD_GLOBAL             20 (sys)
    # 662 LOAD_ATTR               11 (executable)
    # 672 PRECALL                  1
    # 676 CALL                     1
    # 686 UNPACK_SEQUENCE          2
    # 690 STORE_FAST              23 (bits)
    # 692 STORE_FAST              24 (linkage)
    # 1255         694 LOAD_GLOBAL             13 (NULL + _platform)
    # 706 LOAD_FAST                3 (system)
    # 708 LOAD_FAST                5 (release)
    # 710 LOAD_FAST                7 (machine)
    # 1256         712 LOAD_FAST                8 (processor)
    # 714 LOAD_FAST               23 (bits)
    # 716 LOAD_FAST               24 (linkage)
    # 1255         718 PRECALL                  6
    # 722 CALL                     6
    # 732 STORE_FAST              14 (platform)
    # 1258     >>  734 LOAD_FAST               14 (platform)
    # 736 LOAD_GLOBAL              0 (_platform_cache)
    # 748 LOAD_FAST                0 (aliased)
    # 750 LOAD_FAST                1 (terse)
    # 752 BUILD_TUPLE              2
    # 754 STORE_SUBSCR
    # 1259         758 LOAD_FAST               14 (platform)
    # 760 RETURN_VALUE

def _parse_os_release(lines):
    # 1276           0 RESUME                   0
    # 1280           2 LOAD_CONST               1 ('Linux')
    # 1281           4 LOAD_CONST               2 ('linux')
    # 1282           6 LOAD_CONST               1 ('Linux')
    # 1279           8 LOAD_CONST               3 (('NAME', 'ID', 'PRETTY_NAME'))
    # 10 BUILD_CONST_KEY_MAP      3
    # 12 STORE_FAST               1 (info)
    # 1285          14 LOAD_FAST                0 (lines)
    # 16 GET_ITER
    # >>   18 FOR_ITER                98 (to 216)
    # 20 STORE_FAST               2 (line)
    # 1286          22 LOAD_GLOBAL              0 (_os_release_line)
    # 34 LOAD_METHOD              1 (match)
    # 56 LOAD_FAST                2 (line)
    # 58 PRECALL                  1
    # 62 CALL                     1
    # 72 STORE_FAST               3 (mo)
    # 1287          74 LOAD_FAST                3 (mo)
    # 76 POP_JUMP_FORWARD_IF_NONE    68 (to 214)
    # 1288          78 LOAD_GLOBAL              4 (_os_release_unescape)
    # 90 LOAD_METHOD              3 (sub)
    # 1289         112 LOAD_CONST               4 ('\\1')
    # 114 LOAD_FAST                3 (mo)
    # 116 LOAD_METHOD              4 (group)
    # 138 LOAD_CONST               5 ('value')
    # 140 PRECALL                  1
    # 144 CALL                     1
    # 1288         154 PRECALL                  2
    # 158 CALL                     2
    # 168 LOAD_FAST                1 (info)
    # 170 LOAD_FAST                3 (mo)
    # 172 LOAD_METHOD              4 (group)
    # 194 LOAD_CONST               6 ('name')
    # 196 PRECALL                  1
    # 200 CALL                     1
    # 210 STORE_SUBSCR
    # >>  214 JUMP_BACKWARD           99 (to 18)
    # 1292     >>  216 LOAD_FAST                1 (info)
    # 218 RETURN_VALUE

def freedesktop_os_release():
    """Return operation system identification from freedesktop.org os-release
    """
    # 1295           0 RESUME                   0
    # 1300           2 LOAD_GLOBAL              0 (_os_release_cache)
    # 14 POP_JUMP_FORWARD_IF_NOT_NONE   143 (to 302)
    # 1301          16 LOAD_CONST               1 (None)
    # 18 STORE_FAST               0 (errno)
    # 1302          20 LOAD_GLOBAL              2 (_os_release_candidates)
    # 32 GET_ITER
    # >>   34 FOR_ITER                90 (to 216)
    # 36 STORE_FAST               1 (candidate)
    # 1303          38 NOP
    # 1304          40 LOAD_GLOBAL              5 (NULL + open)
    # 52 LOAD_FAST                1 (candidate)
    # 54 LOAD_CONST               2 ('utf-8')
    # 56 KW_NAMES                 3
    # 58 PRECALL                  2
    # 62 CALL                     2
    # 72 BEFORE_WITH
    # 74 STORE_FAST               2 (f)
    # 1305          76 LOAD_GLOBAL              7 (NULL + _parse_os_release)
    # 88 LOAD_FAST                2 (f)
    # 90 PRECALL                  1
    # 94 CALL                     1
    # 104 STORE_GLOBAL             0 (_os_release_cache)
    # 1304         106 LOAD_CONST               1 (None)
    # 108 LOAD_CONST               1 (None)
    # 110 LOAD_CONST               1 (None)
    # 112 PRECALL                  2
    # 116 CALL                     2
    # 126 POP_TOP
    # 128 JUMP_FORWARD            11 (to 152)
    # >>  130 PUSH_EXC_INFO
    # 132 WITH_EXCEPT_START
    # 134 POP_JUMP_FORWARD_IF_TRUE     4 (to 144)
    # 136 RERAISE                  2
    # >>  138 COPY                     3
    # 140 POP_EXCEPT
    # 142 RERAISE                  1
    # >>  144 POP_TOP
    # 146 POP_EXCEPT
    # 148 POP_TOP
    # 150 POP_TOP
    # 1306     >>  152 POP_TOP
    # 154 JUMP_FORWARD            73 (to 302)
    # >>  156 PUSH_EXC_INFO
    # 1307         158 LOAD_GLOBAL              8 (OSError)
    # 170 CHECK_EXC_MATCH
    # 172 POP_JUMP_FORWARD_IF_FALSE    17 (to 208)
    # 174 STORE_FAST               3 (e)
    # 1308         176 LOAD_FAST                3 (e)
    # 178 LOAD_ATTR                5 (errno)
    # 188 STORE_FAST               0 (errno)
    # 190 POP_EXCEPT
    # 192 LOAD_CONST               1 (None)
    # 194 STORE_FAST               3 (e)
    # 196 DELETE_FAST              3 (e)
    # 198 JUMP_BACKWARD           83 (to 34)
    # >>  200 LOAD_CONST               1 (None)
    # 202 STORE_FAST               3 (e)
    # 204 DELETE_FAST              3 (e)
    # 206 RERAISE                  1
    # 1307     >>  208 RERAISE                  0
    # >>  210 COPY                     3
    # 212 POP_EXCEPT
    # 214 RERAISE                  1
    # 1310     >>  216 LOAD_GLOBAL              9 (NULL + OSError)
    # 1311         228 LOAD_FAST                0 (errno)
    # 1312         230 LOAD_CONST               4 ('Unable to read files ')
    # 232 LOAD_CONST               5 (', ')
    # 234 LOAD_METHOD              6 (join)
    # 256 LOAD_GLOBAL              2 (_os_release_candidates)
    # 268 PRECALL                  1
    # 272 CALL                     1
    # 282 FORMAT_VALUE             0
    # 284 BUILD_STRING             2
    # 1310         286 PRECALL                  2
    # 290 CALL                     2
    # 300 RAISE_VARARGS            1
    # 1315     >>  302 LOAD_GLOBAL              0 (_os_release_cache)
    # 314 LOAD_METHOD              7 (copy)
    # 336 PRECALL                  0
    # 340 CALL                     0
    # 350 RETURN_VALUE
    # ExceptionTable:
    # 40 to 72 -> 156 [1]
    # 74 to 104 -> 130 [2] lasti
    # 106 to 128 -> 156 [1]
    # 130 to 136 -> 138 [4] lasti
    # 138 to 142 -> 156 [1]
    # 144 to 144 -> 138 [4] lasti
    # 146 to 150 -> 156 [1]
    # 156 to 174 -> 210 [2] lasti
    # 176 to 188 -> 200 [2] lasti
    # 200 to 208 -> 210 [2] lasti
