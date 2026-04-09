# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: distutils\sysconfig.py

"""Provide access to Python's configuration information.  The specific
configuration variables available depend heavily on the platform and
configuration.  The values may be retrieved using
get_config_var(name), and the list of variables is available via
get_config_vars().keys().  Additional convenience functions are also
available.

Written by:   Fred L. Drake, Jr.
Email:        <fdrake@acm.org>
"""

import _imp
import os
import re
import sys
import warnings
from functools import partial
from errors import DistutilsPlatformError
from sysconfig import _PREFIX

def parse_config_h(fp, g):
    # 61           0 RESUME                   0
    # 62           2 LOAD_GLOBAL              1 (NULL + sysconfig_parse_config_h)
    # 14 LOAD_FAST                0 (fp)
    # 16 LOAD_FAST                1 (g)
    # 18 KW_NAMES                 1
    # 20 PRECALL                  2
    # 24 CALL                     2
    # 34 RETURN_VALUE

def parse_makefile(fn, g):
    """Parse a Makefile-style file.
    A dictionary containing name/value pairs is returned.  If an
    optional dictionary is passed in as the second argument, it is
    used instead of a new dictionary.
    """
    # 72           0 RESUME                   0
    # 78           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('TextFile',))
    # 6 IMPORT_NAME              0 (distutils.text_file)
    # 8 IMPORT_FROM              1 (TextFile)
    # 10 STORE_FAST               2 (TextFile)
    # 12 POP_TOP
    # 79          14 PUSH_NULL
    # 16 LOAD_FAST                2 (TextFile)
    # 18 LOAD_FAST                0 (fn)
    # 20 LOAD_CONST               3 (1)
    # 22 LOAD_CONST               3 (1)
    # 24 LOAD_CONST               3 (1)
    # 26 LOAD_CONST               4 ('surrogateescape')
    # 28 KW_NAMES                 5
    # 30 PRECALL                  5
    # 34 CALL                     5
    # 44 STORE_FAST               3 (fp)
    # 81          46 LOAD_FAST                1 (g)
    # 48 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 54)
    # 82          50 BUILD_MAP                0
    # 52 STORE_FAST               1 (g)
    # 83     >>   54 BUILD_MAP                0
    # 56 STORE_FAST               4 (done)
    # 84          58 BUILD_MAP                0
    # 60 STORE_FAST               5 (notdone)
    # 86          62 NOP
    # 87     >>   64 LOAD_FAST                3 (fp)
    # 66 LOAD_METHOD              2 (readline)
    # 88 PRECALL                  0
    # 92 CALL                     0
    # 102 STORE_FAST               6 (line)
    # 88         104 LOAD_FAST                6 (line)
    # 106 POP_JUMP_FORWARD_IF_NOT_NONE     1 (to 110)
    # 89         108 JUMP_FORWARD           169 (to 448)
    # 90     >>  110 LOAD_GLOBAL              7 (NULL + re)
    # 122 LOAD_ATTR                4 (match)
    # 132 LOAD_GLOBAL             10 (_variable_rx)
    # 144 LOAD_FAST                6 (line)
    # 146 PRECALL                  2
    # 150 CALL                     2
    # 160 STORE_FAST               7 (m)
    # 91         162 LOAD_FAST                7 (m)
    # 164 POP_JUMP_FORWARD_IF_FALSE   140 (to 446)
    # 92         166 LOAD_FAST                7 (m)
    # 168 LOAD_METHOD              6 (group)
    # 190 LOAD_CONST               3 (1)
    # 192 LOAD_CONST               8 (2)
    # 194 PRECALL                  2
    # 198 CALL                     2
    # 208 UNPACK_SEQUENCE          2
    # 212 STORE_FAST               8 (n)
    # 214 STORE_FAST               9 (v)
    # 93         216 LOAD_FAST                9 (v)
    # 218 LOAD_METHOD              7 (strip)
    # 240 PRECALL                  0
    # 244 CALL                     0
    # 254 STORE_FAST               9 (v)
    # 95         256 LOAD_FAST                9 (v)
    # 258 LOAD_METHOD              8 (replace)
    # 280 LOAD_CONST               9 ('$$')
    # 282 LOAD_CONST              10 ('')
    # 284 PRECALL                  2
    # 288 CALL                     2
    # 298 STORE_FAST              10 (tmpv)
    # 97         300 LOAD_CONST              11 ('$')
    # 302 LOAD_FAST               10 (tmpv)
    # 304 CONTAINS_OP              0
    # 306 POP_JUMP_FORWARD_IF_FALSE     6 (to 320)
    # 98         308 LOAD_FAST                9 (v)
    # 310 LOAD_FAST                5 (notdone)
    # 312 LOAD_FAST                8 (n)
    # 314 STORE_SUBSCR
    # 318 JUMP_FORWARD            63 (to 446)
    # 100     >>  320 NOP
    # 101         322 LOAD_GLOBAL             19 (NULL + int)
    # 334 LOAD_FAST                9 (v)
    # 336 PRECALL                  1
    # 340 CALL                     1
    # 350 STORE_FAST               9 (v)
    # 106         352 LOAD_FAST                9 (v)
    # 354 LOAD_FAST                4 (done)
    # 356 LOAD_FAST                8 (n)
    # 358 STORE_SUBSCR
    # 362 JUMP_FORWARD            41 (to 446)
    # >>  364 PUSH_EXC_INFO
    # 102         366 LOAD_GLOBAL             20 (ValueError)
    # 378 CHECK_EXC_MATCH
    # 380 POP_JUMP_FORWARD_IF_FALSE    28 (to 438)
    # 382 POP_TOP
    # 104         384 LOAD_FAST                9 (v)
    # 386 LOAD_METHOD              8 (replace)
    # 408 LOAD_CONST               9 ('$$')
    # 410 LOAD_CONST              11 ('$')
    # 412 PRECALL                  2
    # 416 CALL                     2
    # 426 LOAD_FAST                4 (done)
    # 428 LOAD_FAST                8 (n)
    # 430 STORE_SUBSCR
    # 434 POP_EXCEPT
    # 436 JUMP_FORWARD             4 (to 446)
    # 102     >>  438 RERAISE                  0
    # >>  440 COPY                     3
    # 442 POP_EXCEPT
    # 444 RERAISE                  1
    # 86     >>  446 JUMP_BACKWARD          192 (to 64)
    # 112     >>  448 LOAD_CONST              12 (('CFLAGS', 'LDFLAGS', 'CPPFLAGS'))
    # 450 STORE_FAST              11 (renamed_variables)
    # 115         452 LOAD_FAST                5 (notdone)
    # 454 EXTENDED_ARG             1
    # 456 POP_JUMP_FORWARD_IF_FALSE   452 (to 1362)
    # 116     >>  458 LOAD_GLOBAL             23 (NULL + list)
    # 470 LOAD_FAST                5 (notdone)
    # 472 PRECALL                  1
    # 476 CALL                     1
    # 486 GET_ITER
    # >>  488 EXTENDED_ARG             1
    # 490 FOR_ITER               432 (to 1356)
    # 492 STORE_FAST              12 (name)
    # 117         494 LOAD_FAST                5 (notdone)
    # 496 LOAD_FAST               12 (name)
    # 498 BINARY_SUBSCR
    # 508 STORE_FAST              13 (value)
    # 118         510 LOAD_GLOBAL              7 (NULL + re)
    # 522 LOAD_ATTR               12 (search)
    # 532 LOAD_GLOBAL             26 (_findvar1_rx)
    # 544 LOAD_FAST               13 (value)
    # 546 PRECALL                  2
    # 550 CALL                     2
    # 560 JUMP_IF_TRUE_OR_POP     25 (to 612)
    # 562 LOAD_GLOBAL              7 (NULL + re)
    # 574 LOAD_ATTR               12 (search)
    # 584 LOAD_GLOBAL             28 (_findvar2_rx)
    # 596 LOAD_FAST               13 (value)
    # 598 PRECALL                  2
    # 602 CALL                     2
    # >>  612 STORE_FAST               7 (m)
    # 119         614 LOAD_FAST                7 (m)
    # 616 EXTENDED_ARG             1
    # 618 POP_JUMP_FORWARD_IF_FALSE   363 (to 1346)
    # 120         620 LOAD_FAST                7 (m)
    # 622 LOAD_METHOD              6 (group)
    # 644 LOAD_CONST               3 (1)
    # 646 PRECALL                  1
    # 650 CALL                     1
    # 660 STORE_FAST               8 (n)
    # 121         662 LOAD_CONST               7 (True)
    # 664 STORE_FAST              14 (found)
    # 122         666 LOAD_FAST                8 (n)
    # 668 LOAD_FAST                4 (done)
    # 670 CONTAINS_OP              0
    # 672 POP_JUMP_FORWARD_IF_FALSE    22 (to 718)
    # 123         674 LOAD_GLOBAL             31 (NULL + str)
    # 686 LOAD_FAST                4 (done)
    # 688 LOAD_FAST                8 (n)
    # 690 BINARY_SUBSCR
    # 700 PRECALL                  1
    # 704 CALL                     1
    # 714 STORE_FAST              15 (item)
    # 716 JUMP_FORWARD           122 (to 962)
    # 124     >>  718 LOAD_FAST                8 (n)
    # 720 LOAD_FAST                5 (notdone)
    # 722 CONTAINS_OP              0
    # 724 POP_JUMP_FORWARD_IF_FALSE     3 (to 732)
    # 126         726 LOAD_CONST              13 (False)
    # 728 STORE_FAST              14 (found)
    # 730 JUMP_FORWARD           115 (to 962)
    # 127     >>  732 LOAD_FAST                8 (n)
    # 734 LOAD_GLOBAL             32 (os)
    # 746 LOAD_ATTR               17 (environ)
    # 756 CONTAINS_OP              0
    # 758 POP_JUMP_FORWARD_IF_FALSE    19 (to 798)
    # 129         760 LOAD_GLOBAL             32 (os)
    # 772 LOAD_ATTR               17 (environ)
    # 782 LOAD_FAST                8 (n)
    # 784 BINARY_SUBSCR
    # 794 STORE_FAST              15 (item)
    # 796 JUMP_FORWARD            82 (to 962)
    # 131     >>  798 LOAD_FAST                8 (n)
    # 800 LOAD_FAST               11 (renamed_variables)
    # 802 CONTAINS_OP              0
    # 804 POP_JUMP_FORWARD_IF_FALSE    71 (to 948)
    # 132         806 LOAD_FAST               12 (name)
    # 808 LOAD_METHOD             18 (startswith)
    # 830 LOAD_CONST              14 ('PY_')
    # 832 PRECALL                  1
    # 836 CALL                     1
    # 846 POP_JUMP_FORWARD_IF_FALSE    15 (to 878)
    # 848 LOAD_FAST               12 (name)
    # 850 LOAD_CONST              15 (3)
    # 852 LOAD_CONST               6 (None)
    # 854 BUILD_SLICE              2
    # 856 BINARY_SUBSCR
    # 866 LOAD_FAST               11 (renamed_variables)
    # 868 CONTAINS_OP              0
    # 870 POP_JUMP_FORWARD_IF_FALSE     3 (to 878)
    # 133         872 LOAD_CONST              10 ('')
    # 874 STORE_FAST              15 (item)
    # 876 JUMP_FORWARD            42 (to 962)
    # 135     >>  878 LOAD_CONST              14 ('PY_')
    # 880 LOAD_FAST                8 (n)
    # 882 BINARY_OP                0 (+)
    # 886 LOAD_FAST                5 (notdone)
    # 888 CONTAINS_OP              0
    # 890 POP_JUMP_FORWARD_IF_FALSE     3 (to 898)
    # 136         892 LOAD_CONST              13 (False)
    # 894 STORE_FAST              14 (found)
    # 896 JUMP_FORWARD            32 (to 962)
    # 139     >>  898 LOAD_GLOBAL             31 (NULL + str)
    # 910 LOAD_FAST                4 (done)
    # 912 LOAD_CONST              14 ('PY_')
    # 914 LOAD_FAST                8 (n)
    # 916 BINARY_OP                0 (+)
    # 920 BINARY_SUBSCR
    # 930 PRECALL                  1
    # 934 CALL                     1
    # 944 STORE_FAST              15 (item)
    # 946 JUMP_FORWARD             7 (to 962)
    # 141     >>  948 LOAD_CONST              10 ('')
    # 950 COPY                     1
    # 952 LOAD_FAST                4 (done)
    # 954 LOAD_FAST                8 (n)
    # 956 STORE_SUBSCR
    # 960 STORE_FAST              15 (item)
    # 142     >>  962 LOAD_FAST               14 (found)
    # 964 POP_JUMP_FORWARD_IF_FALSE   188 (to 1342)
    # 143         966 LOAD_FAST               13 (value)
    # 968 LOAD_FAST                7 (m)
    # 970 LOAD_METHOD             19 (end)
    # 992 PRECALL                  0
    # 996 CALL                     0
    # 1006 LOAD_CONST               6 (None)
    # 1008 BUILD_SLICE              2
    # 1010 BINARY_SUBSCR
    # 1020 STORE_FAST              16 (after)
    # 144        1022 LOAD_FAST               13 (value)
    # 1024 LOAD_CONST               6 (None)
    # 1026 LOAD_FAST                7 (m)
    # 1028 LOAD_METHOD             20 (start)
    # 1050 PRECALL                  0
    # 1054 CALL                     0
    # 1064 BUILD_SLICE              2
    # 1066 BINARY_SUBSCR
    # 1076 LOAD_FAST               15 (item)
    # 1078 BINARY_OP                0 (+)
    # 1082 LOAD_FAST               16 (after)
    # 1084 BINARY_OP                0 (+)
    # 1088 STORE_FAST              13 (value)
    # 145        1090 LOAD_CONST              11 ('$')
    # 1092 LOAD_FAST               16 (after)
    # 1094 CONTAINS_OP              0
    # 1096 POP_JUMP_FORWARD_IF_FALSE     7 (to 1112)
    # 146        1098 LOAD_FAST               13 (value)
    # 1100 LOAD_FAST                5 (notdone)
    # 1102 LOAD_FAST               12 (name)
    # 1104 STORE_SUBSCR
    # 1108 EXTENDED_ARG             1
    # 1110 JUMP_BACKWARD          312 (to 488)
    # 148     >> 1112 LOAD_GLOBAL             19 (NULL + int)
    # 1124 LOAD_FAST               13 (value)
    # 1126 PRECALL                  1
    # 1130 CALL                     1
    # 1140 STORE_FAST              13 (value)
    # 152        1142 LOAD_FAST               13 (value)
    # 1144 LOAD_FAST                4 (done)
    # 1146 LOAD_FAST               12 (name)
    # 1148 STORE_SUBSCR
    # 1152 JUMP_FORWARD            39 (to 1232)
    # >> 1154 PUSH_EXC_INFO
    # 149        1156 LOAD_GLOBAL             20 (ValueError)
    # 1168 CHECK_EXC_MATCH
    # 1170 POP_JUMP_FORWARD_IF_FALSE    26 (to 1224)
    # 1172 POP_TOP
    # 150        1174 LOAD_FAST               13 (value)
    # 1176 LOAD_METHOD              7 (strip)
    # 1198 PRECALL                  0
    # 1202 CALL                     0
    # 1212 LOAD_FAST                4 (done)
    # 1214 LOAD_FAST               12 (name)
    # 1216 STORE_SUBSCR
    # 1220 POP_EXCEPT
    # 1222 JUMP_FORWARD             4 (to 1232)
    # 149     >> 1224 RERAISE                  0
    # >> 1226 COPY                     3
    # 1228 POP_EXCEPT
    # 1230 RERAISE                  1
    # 153     >> 1232 LOAD_FAST                5 (notdone)
    # 1234 LOAD_FAST               12 (name)
    # 1236 DELETE_SUBSCR
    # 155        1238 LOAD_FAST               12 (name)
    # 1240 LOAD_METHOD             18 (startswith)
    # 1262 LOAD_CONST              14 ('PY_')
    # 1264 PRECALL                  1
    # 1268 CALL                     1
    # 1278 POP_JUMP_FORWARD_IF_FALSE    31 (to 1342)
    # 156        1280 LOAD_FAST               12 (name)
    # 1282 LOAD_CONST              15 (3)
    # 1284 LOAD_CONST               6 (None)
    # 1286 BUILD_SLICE              2
    # 1288 BINARY_SUBSCR
    # 1298 LOAD_FAST               11 (renamed_variables)
    # 1300 CONTAINS_OP              0
    # 1302 POP_JUMP_FORWARD_IF_FALSE    19 (to 1342)
    # 158        1304 LOAD_FAST               12 (name)
    # 1306 LOAD_CONST              15 (3)
    # 1308 LOAD_CONST               6 (None)
    # 1310 BUILD_SLICE              2
    # 1312 BINARY_SUBSCR
    # 1322 STORE_FAST              12 (name)
    # 159        1324 LOAD_FAST               12 (name)
    # 1326 LOAD_FAST                4 (done)
    # 1328 CONTAINS_OP              1
    # 1330 POP_JUMP_FORWARD_IF_FALSE     5 (to 1342)
    # 160        1332 LOAD_FAST               13 (value)
    # 1334 LOAD_FAST                4 (done)
    # 1336 LOAD_FAST               12 (name)
    # 1338 STORE_SUBSCR
    # >> 1342 EXTENDED_ARG             1
    # 1344 JUMP_BACKWARD          429 (to 488)
    # 163     >> 1346 LOAD_FAST                5 (notdone)
    # 1348 LOAD_FAST               12 (name)
    # 1350 DELETE_SUBSCR
    # 1352 EXTENDED_ARG             1
    # 1354 JUMP_BACKWARD          434 (to 488)
    # 115     >> 1356 LOAD_FAST                5 (notdone)
    # 1358 EXTENDED_ARG             1
    # 1360 POP_JUMP_BACKWARD_IF_TRUE   452 (to 458)
    # 165     >> 1362 LOAD_FAST                3 (fp)
    # 1364 LOAD_METHOD             21 (close)
    # 1386 PRECALL                  0
    # 1390 CALL                     0
    # 1400 POP_TOP
    # 168        1402 LOAD_FAST                4 (done)
    # 1404 LOAD_METHOD             22 (items)
    # 1426 PRECALL                  0
    # 1430 CALL                     0
    # 1440 GET_ITER
    # >> 1442 FOR_ITER                49 (to 1542)
    # 1444 UNPACK_SEQUENCE          2
    # 1448 STORE_FAST              17 (k)
    # 1450 STORE_FAST               9 (v)
    # 169        1452 LOAD_GLOBAL             47 (NULL + isinstance)
    # 1464 LOAD_FAST                9 (v)
    # 1466 LOAD_GLOBAL             30 (str)
    # 1478 PRECALL                  2
    # 1482 CALL                     2
    # 1492 POP_JUMP_FORWARD_IF_FALSE    23 (to 1540)
    # 170        1494 LOAD_FAST                9 (v)
    # 1496 LOAD_METHOD              7 (strip)
    # 1518 PRECALL                  0
    # 1522 CALL                     0
    # 1532 LOAD_FAST                4 (done)
    # 1534 LOAD_FAST               17 (k)
    # 1536 STORE_SUBSCR
    # >> 1540 JUMP_BACKWARD           50 (to 1442)
    # 173     >> 1542 LOAD_FAST                1 (g)
    # 1544 LOAD_METHOD             24 (update)
    # 1566 LOAD_FAST                4 (done)
    # 1568 PRECALL                  1
    # 1572 CALL                     1
    # 1582 POP_TOP
    # 174        1584 LOAD_FAST                1 (g)
    # 1586 RETURN_VALUE
    # ExceptionTable:
    # 322 to 350 -> 364 [0]
    # 364 to 432 -> 440 [1] lasti
    # 438 to 438 -> 440 [1] lasti
    # 1112 to 1140 -> 1154 [1]
    # 1154 to 1218 -> 1226 [2] lasti
    # 1224 to 1224 -> 1226 [2] lasti

def customize_compiler(compiler):
    """Do any platform-specific customization of a CCompiler instance.

    Mainly needed on Unix, so we can plug in the information that
    varies across Unices and is stored in Python's Makefile.
    """
    # 193           0 RESUME                   0
    # 199           2 LOAD_FAST                0 (compiler)
    # 4 LOAD_ATTR                0 (compiler_type)
    # 14 LOAD_CONST               1 ('unix')
    # 16 COMPARE_OP               2 (==)
    # 22 EXTENDED_ARG             2
    # 24 POP_JUMP_FORWARD_IF_FALSE   642 (to 1310)
    # 200          26 LOAD_GLOBAL              2 (sys)
    # 38 LOAD_ATTR                2 (platform)
    # 48 LOAD_CONST               2 ('darwin')
    # 50 COMPARE_OP               2 (==)
    # 56 POP_JUMP_FORWARD_IF_FALSE    66 (to 190)
    # 209          58 LOAD_GLOBAL              6 (_config_vars)
    # 70 LOAD_METHOD              4 (get)
    # 92 LOAD_CONST               3 ('CUSTOMIZED_OSX_COMPILER')
    # 94 PRECALL                  1
    # 98 CALL                     1
    # 108 POP_JUMP_FORWARD_IF_TRUE    40 (to 190)
    # 210         110 LOAD_CONST               4 (0)
    # 112 LOAD_CONST               5 (None)
    # 114 IMPORT_NAME              5 (_osx_support)
    # 116 STORE_FAST               1 (_osx_support)
    # 211         118 LOAD_FAST                1 (_osx_support)
    # 120 LOAD_METHOD              6 (customize_compiler)
    # 142 LOAD_GLOBAL              6 (_config_vars)
    # 154 PRECALL                  1
    # 158 CALL                     1
    # 168 POP_TOP
    # 212         170 LOAD_CONST               6 ('True')
    # 172 LOAD_GLOBAL              6 (_config_vars)
    # 184 LOAD_CONST               3 ('CUSTOMIZED_OSX_COMPILER')
    # 186 STORE_SUBSCR
    # 215     >>  190 LOAD_GLOBAL             15 (NULL + get_config_vars)
    # 202 LOAD_CONST               7 ('CC')
    # 204 LOAD_CONST               8 ('CXX')
    # 206 LOAD_CONST               9 ('CFLAGS')
    # 216         208 LOAD_CONST              10 ('CCSHARED')
    # 210 LOAD_CONST              11 ('LDSHARED')
    # 212 LOAD_CONST              12 ('SHLIB_SUFFIX')
    # 214 LOAD_CONST              13 ('AR')
    # 216 LOAD_CONST              14 ('ARFLAGS')
    # 215         218 PRECALL                  8
    # 222 CALL                     8
    # 214         232 UNPACK_SEQUENCE          8
    # 236 STORE_FAST               2 (cc)
    # 238 STORE_FAST               3 (cxx)
    # 240 STORE_FAST               4 (cflags)
    # 242 STORE_FAST               5 (ccshared)
    # 244 STORE_FAST               6 (ldshared)
    # 246 STORE_FAST               7 (shlib_suffix)
    # 248 STORE_FAST               8 (ar)
    # 250 STORE_FAST               9 (ar_flags)
    # 218         252 LOAD_CONST               7 ('CC')
    # 254 LOAD_GLOBAL             16 (os)
    # 266 LOAD_ATTR                9 (environ)
    # 276 CONTAINS_OP              0
    # 278 POP_JUMP_FORWARD_IF_FALSE    97 (to 474)
    # 219         280 LOAD_GLOBAL             16 (os)
    # 292 LOAD_ATTR                9 (environ)
    # 302 LOAD_CONST               7 ('CC')
    # 304 BINARY_SUBSCR
    # 314 STORE_FAST              10 (newcc)
    # 220         316 LOAD_GLOBAL              2 (sys)
    # 328 LOAD_ATTR                2 (platform)
    # 338 LOAD_CONST               2 ('darwin')
    # 340 COMPARE_OP               2 (==)
    # 346 POP_JUMP_FORWARD_IF_FALSE    61 (to 470)
    # 221         348 LOAD_CONST              11 ('LDSHARED')
    # 350 LOAD_GLOBAL             16 (os)
    # 362 LOAD_ATTR                9 (environ)
    # 372 CONTAINS_OP              1
    # 374 POP_JUMP_FORWARD_IF_FALSE    47 (to 470)
    # 222         376 LOAD_FAST                6 (ldshared)
    # 378 LOAD_METHOD             10 (startswith)
    # 400 LOAD_FAST                2 (cc)
    # 402 PRECALL                  1
    # 406 CALL                     1
    # 221         416 POP_JUMP_FORWARD_IF_FALSE    26 (to 470)
    # 225         418 LOAD_FAST               10 (newcc)
    # 420 LOAD_FAST                6 (ldshared)
    # 422 LOAD_GLOBAL             23 (NULL + len)
    # 434 LOAD_FAST                2 (cc)
    # 436 PRECALL                  1
    # 440 CALL                     1
    # 450 LOAD_CONST               5 (None)
    # 452 BUILD_SLICE              2
    # 454 BINARY_SUBSCR
    # 464 BINARY_OP                0 (+)
    # 468 STORE_FAST               6 (ldshared)
    # 226     >>  470 LOAD_FAST               10 (newcc)
    # 472 STORE_FAST               2 (cc)
    # 227     >>  474 LOAD_CONST               8 ('CXX')
    # 476 LOAD_GLOBAL             16 (os)
    # 488 LOAD_ATTR                9 (environ)
    # 498 CONTAINS_OP              0
    # 500 POP_JUMP_FORWARD_IF_FALSE    18 (to 538)
    # 228         502 LOAD_GLOBAL             16 (os)
    # 514 LOAD_ATTR                9 (environ)
    # 524 LOAD_CONST               8 ('CXX')
    # 526 BINARY_SUBSCR
    # 536 STORE_FAST               3 (cxx)
    # 229     >>  538 LOAD_CONST              11 ('LDSHARED')
    # 540 LOAD_GLOBAL             16 (os)
    # 552 LOAD_ATTR                9 (environ)
    # 562 CONTAINS_OP              0
    # 564 POP_JUMP_FORWARD_IF_FALSE    18 (to 602)
    # 230         566 LOAD_GLOBAL             16 (os)
    # 578 LOAD_ATTR                9 (environ)
    # 588 LOAD_CONST              11 ('LDSHARED')
    # 590 BINARY_SUBSCR
    # 600 STORE_FAST               6 (ldshared)
    # 231     >>  602 LOAD_CONST              15 ('CPP')
    # 604 LOAD_GLOBAL             16 (os)
    # 616 LOAD_ATTR                9 (environ)
    # 626 CONTAINS_OP              0
    # 628 POP_JUMP_FORWARD_IF_FALSE    19 (to 668)
    # 232         630 LOAD_GLOBAL             16 (os)
    # 642 LOAD_ATTR                9 (environ)
    # 652 LOAD_CONST              15 ('CPP')
    # 654 BINARY_SUBSCR
    # 664 STORE_FAST              11 (cpp)
    # 666 JUMP_FORWARD             5 (to 678)
    # 234     >>  668 LOAD_FAST                2 (cc)
    # 670 LOAD_CONST              16 (' -E')
    # 672 BINARY_OP                0 (+)
    # 676 STORE_FAST              11 (cpp)
    # 235     >>  678 LOAD_CONST              17 ('LDFLAGS')
    # 680 LOAD_GLOBAL             16 (os)
    # 692 LOAD_ATTR                9 (environ)
    # 702 CONTAINS_OP              0
    # 704 POP_JUMP_FORWARD_IF_FALSE    24 (to 754)
    # 236         706 LOAD_FAST                6 (ldshared)
    # 708 LOAD_CONST              18 (' ')
    # 710 BINARY_OP                0 (+)
    # 714 LOAD_GLOBAL             16 (os)
    # 726 LOAD_ATTR                9 (environ)
    # 736 LOAD_CONST              17 ('LDFLAGS')
    # 738 BINARY_SUBSCR
    # 748 BINARY_OP                0 (+)
    # 752 STORE_FAST               6 (ldshared)
    # 237     >>  754 LOAD_CONST               9 ('CFLAGS')
    # 756 LOAD_GLOBAL             16 (os)
    # 768 LOAD_ATTR                9 (environ)
    # 778 CONTAINS_OP              0
    # 780 POP_JUMP_FORWARD_IF_FALSE    48 (to 878)
    # 238         782 LOAD_FAST                4 (cflags)
    # 784 LOAD_CONST              18 (' ')
    # 786 BINARY_OP                0 (+)
    # 790 LOAD_GLOBAL             16 (os)
    # 802 LOAD_ATTR                9 (environ)
    # 812 LOAD_CONST               9 ('CFLAGS')
    # 814 BINARY_SUBSCR
    # 824 BINARY_OP                0 (+)
    # 828 STORE_FAST               4 (cflags)
    # 239         830 LOAD_FAST                6 (ldshared)
    # 832 LOAD_CONST              18 (' ')
    # 834 BINARY_OP                0 (+)
    # 838 LOAD_GLOBAL             16 (os)
    # 850 LOAD_ATTR                9 (environ)
    # 860 LOAD_CONST               9 ('CFLAGS')
    # 862 BINARY_SUBSCR
    # 872 BINARY_OP                0 (+)
    # 876 STORE_FAST               6 (ldshared)
    # 240     >>  878 LOAD_CONST              19 ('CPPFLAGS')
    # 880 LOAD_GLOBAL             16 (os)
    # 892 LOAD_ATTR                9 (environ)
    # 902 CONTAINS_OP              0
    # 904 POP_JUMP_FORWARD_IF_FALSE    72 (to 1050)
    # 241         906 LOAD_FAST               11 (cpp)
    # 908 LOAD_CONST              18 (' ')
    # 910 BINARY_OP                0 (+)
    # 914 LOAD_GLOBAL             16 (os)
    # 926 LOAD_ATTR                9 (environ)
    # 936 LOAD_CONST              19 ('CPPFLAGS')
    # 938 BINARY_SUBSCR
    # 948 BINARY_OP                0 (+)
    # 952 STORE_FAST              11 (cpp)
    # 242         954 LOAD_FAST                4 (cflags)
    # 956 LOAD_CONST              18 (' ')
    # 958 BINARY_OP                0 (+)
    # 962 LOAD_GLOBAL             16 (os)
    # 974 LOAD_ATTR                9 (environ)
    # 984 LOAD_CONST              19 ('CPPFLAGS')
    # 986 BINARY_SUBSCR
    # 996 BINARY_OP                0 (+)
    # 1000 STORE_FAST               4 (cflags)
    # 243        1002 LOAD_FAST                6 (ldshared)
    # 1004 LOAD_CONST              18 (' ')
    # 1006 BINARY_OP                0 (+)
    # 1010 LOAD_GLOBAL             16 (os)
    # 1022 LOAD_ATTR                9 (environ)
    # 1032 LOAD_CONST              19 ('CPPFLAGS')
    # 1034 BINARY_SUBSCR
    # 1044 BINARY_OP                0 (+)
    # 1048 STORE_FAST               6 (ldshared)
    # 244     >> 1050 LOAD_CONST              13 ('AR')
    # 1052 LOAD_GLOBAL             16 (os)
    # 1064 LOAD_ATTR                9 (environ)
    # 1074 CONTAINS_OP              0
    # 1076 POP_JUMP_FORWARD_IF_FALSE    18 (to 1114)
    # 245        1078 LOAD_GLOBAL             16 (os)
    # 1090 LOAD_ATTR                9 (environ)
    # 1100 LOAD_CONST              13 ('AR')
    # 1102 BINARY_SUBSCR
    # 1112 STORE_FAST               8 (ar)
    # 246     >> 1114 LOAD_CONST              14 ('ARFLAGS')
    # 1116 LOAD_GLOBAL             16 (os)
    # 1128 LOAD_ATTR                9 (environ)
    # 1138 CONTAINS_OP              0
    # 1140 POP_JUMP_FORWARD_IF_FALSE    25 (to 1192)
    # 247        1142 LOAD_FAST                8 (ar)
    # 1144 LOAD_CONST              18 (' ')
    # 1146 BINARY_OP                0 (+)
    # 1150 LOAD_GLOBAL             16 (os)
    # 1162 LOAD_ATTR                9 (environ)
    # 1172 LOAD_CONST              14 ('ARFLAGS')
    # 1174 BINARY_SUBSCR
    # 1184 BINARY_OP                0 (+)
    # 1188 STORE_FAST              12 (archiver)
    # 1190 JUMP_FORWARD             8 (to 1208)
    # 249     >> 1192 LOAD_FAST                8 (ar)
    # 1194 LOAD_CONST              18 (' ')
    # 1196 BINARY_OP                0 (+)
    # 1200 LOAD_FAST                9 (ar_flags)
    # 1202 BINARY_OP                0 (+)
    # 1206 STORE_FAST              12 (archiver)
    # 251     >> 1208 LOAD_FAST                2 (cc)
    # 1210 LOAD_CONST              18 (' ')
    # 1212 BINARY_OP                0 (+)
    # 1216 LOAD_FAST                4 (cflags)
    # 1218 BINARY_OP                0 (+)
    # 1222 STORE_FAST              13 (cc_cmd)
    # 252        1224 LOAD_FAST                0 (compiler)
    # 1226 LOAD_METHOD             12 (set_executables)
    # 253        1248 LOAD_FAST               11 (cpp)
    # 254        1250 LOAD_FAST               13 (cc_cmd)
    # 255        1252 LOAD_FAST               13 (cc_cmd)
    # 1254 LOAD_CONST              18 (' ')
    # 1256 BINARY_OP                0 (+)
    # 1260 LOAD_FAST                5 (ccshared)
    # 1262 BINARY_OP                0 (+)
    # 256        1266 LOAD_FAST                3 (cxx)
    # 257        1268 LOAD_FAST                6 (ldshared)
    # 258        1270 LOAD_FAST                2 (cc)
    # 259        1272 LOAD_FAST               12 (archiver)
    # 252        1274 KW_NAMES                20
    # 1276 PRECALL                  7
    # 1280 CALL                     7
    # 1290 POP_TOP
    # 261        1292 LOAD_FAST                7 (shlib_suffix)
    # 1294 LOAD_FAST                0 (compiler)
    # 1296 STORE_ATTR              13 (shared_lib_extension)
    # 1306 LOAD_CONST               5 (None)
    # 1308 RETURN_VALUE
    # 199     >> 1310 LOAD_CONST               5 (None)
    # 1312 RETURN_VALUE

def get_python_inc(plat_specific, prefix):
    """Return the directory containing installed Python header files.

    If 'plat_specific' is false (the default), this is the path to the
    non-platform-specific header files, i.e. Python.h and so on;
    otherwise, this is the path to platform-specific header files
    (namely pyconfig.h).

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
    # 264           0 RESUME                   0
    # 275           2 LOAD_FAST                1 (prefix)
    # 4 POP_JUMP_FORWARD_IF_NOT_NONE    16 (to 38)
    # 276           6 LOAD_FAST                0 (plat_specific)
    # 8 POP_JUMP_FORWARD_IF_FALSE     7 (to 24)
    # 10 LOAD_GLOBAL              0 (BASE_EXEC_PREFIX)
    # 22 JUMP_IF_TRUE_OR_POP      6 (to 36)
    # >>   24 LOAD_GLOBAL              2 (BASE_PREFIX)
    # >>   36 STORE_FAST               1 (prefix)
    # 277     >>   38 LOAD_GLOBAL              4 (os)
    # 50 LOAD_ATTR                3 (name)
    # 60 LOAD_CONST               2 ('posix')
    # 62 COMPARE_OP               2 (==)
    # 68 POP_JUMP_FORWARD_IF_FALSE   150 (to 370)
    # 278          70 LOAD_GLOBAL              8 (python_build)
    # 82 POP_JUMP_FORWARD_IF_FALSE    85 (to 254)
    # 284          84 LOAD_FAST                0 (plat_specific)
    # 86 POP_JUMP_FORWARD_IF_FALSE     7 (to 102)
    # 285          88 LOAD_GLOBAL             10 (project_base)
    # 100 RETURN_VALUE
    # 287     >>  102 LOAD_GLOBAL              4 (os)
    # 114 LOAD_ATTR                6 (path)
    # 124 LOAD_METHOD              7 (join)
    # 146 LOAD_GLOBAL             17 (NULL + get_config_var)
    # 158 LOAD_CONST               3 ('srcdir')
    # 160 PRECALL                  1
    # 164 CALL                     1
    # 174 LOAD_CONST               4 ('Include')
    # 176 PRECALL                  2
    # 180 CALL                     2
    # 190 STORE_FAST               2 (incdir)
    # 288         192 LOAD_GLOBAL              4 (os)
    # 204 LOAD_ATTR                6 (path)
    # 214 LOAD_METHOD              9 (normpath)
    # 236 LOAD_FAST                2 (incdir)
    # 238 PRECALL                  1
    # 242 CALL                     1
    # 252 RETURN_VALUE
    # 289     >>  254 LOAD_CONST               5 ('python')
    # 256 LOAD_GLOBAL             21 (NULL + get_python_version)
    # 268 PRECALL                  0
    # 272 CALL                     0
    # 282 BINARY_OP                0 (+)
    # 286 LOAD_GLOBAL             22 (build_flags)
    # 298 BINARY_OP                0 (+)
    # 302 STORE_FAST               3 (python_dir)
    # 290         304 LOAD_GLOBAL              4 (os)
    # 316 LOAD_ATTR                6 (path)
    # 326 LOAD_METHOD              7 (join)
    # 348 LOAD_FAST                1 (prefix)
    # 350 LOAD_CONST               6 ('include')
    # 352 LOAD_FAST                3 (python_dir)
    # 354 PRECALL                  3
    # 358 CALL                     3
    # 368 RETURN_VALUE
    # 291     >>  370 LOAD_GLOBAL              4 (os)
    # 382 LOAD_ATTR                3 (name)
    # 392 LOAD_CONST               7 ('nt')
    # 394 COMPARE_OP               2 (==)
    # 400 POP_JUMP_FORWARD_IF_FALSE   122 (to 646)
    # 292         402 LOAD_GLOBAL              8 (python_build)
    # 414 POP_JUMP_FORWARD_IF_FALSE    83 (to 582)
    # 295         416 LOAD_GLOBAL              4 (os)
    # 428 LOAD_ATTR                6 (path)
    # 438 LOAD_METHOD              7 (join)
    # 460 LOAD_FAST                1 (prefix)
    # 462 LOAD_CONST               6 ('include')
    # 464 PRECALL                  2
    # 468 CALL                     2
    # 478 LOAD_GLOBAL              4 (os)
    # 490 LOAD_ATTR                6 (path)
    # 500 LOAD_ATTR               12 (pathsep)
    # 510 BINARY_OP                0 (+)
    # 296         514 LOAD_GLOBAL              4 (os)
    # 526 LOAD_ATTR                6 (path)
    # 536 LOAD_METHOD              7 (join)
    # 558 LOAD_FAST                1 (prefix)
    # 560 LOAD_CONST               8 ('PC')
    # 562 PRECALL                  2
    # 566 CALL                     2
    # 295         576 BINARY_OP                0 (+)
    # 580 RETURN_VALUE
    # 297     >>  582 LOAD_GLOBAL              4 (os)
    # 594 LOAD_ATTR                6 (path)
    # 604 LOAD_METHOD              7 (join)
    # 626 LOAD_FAST                1 (prefix)
    # 628 LOAD_CONST               6 ('include')
    # 630 PRECALL                  2
    # 634 CALL                     2
    # 644 RETURN_VALUE
    # 299     >>  646 LOAD_GLOBAL             27 (NULL + DistutilsPlatformError)
    # 300         658 LOAD_CONST               9 ("I don't know where Python installs its C header files on platform '%s'")
    # 301         660 LOAD_GLOBAL              4 (os)
    # 672 LOAD_ATTR                3 (name)
    # 300         682 BINARY_OP                6 (%)
    # 299         686 PRECALL                  1
    # 690 CALL                     1
    # 700 RAISE_VARARGS            1

def get_python_lib(plat_specific, standard_lib, prefix):
    """Return the directory containing the Python library (standard or
    site additions).

    If 'plat_specific' is true, return the directory containing
    platform-specific modules, i.e. any module from a non-pure-Python
    module distribution; otherwise, return the platform-shared library
    directory.  If 'standard_lib' is true, return the directory
    containing standard Python library modules; otherwise, return the
    directory for site-specific modules.

    If 'prefix' is supplied, use it instead of sys.base_prefix or
    sys.base_exec_prefix -- i.e., ignore 'plat_specific'.
    """
    # 304           0 RESUME                   0
    # 318           2 LOAD_FAST                2 (prefix)
    # 4 POP_JUMP_FORWARD_IF_NOT_NONE    35 (to 76)
    # 319           6 LOAD_FAST                1 (standard_lib)
    # 8 POP_JUMP_FORWARD_IF_FALSE    17 (to 44)
    # 320          10 LOAD_FAST                0 (plat_specific)
    # 12 POP_JUMP_FORWARD_IF_FALSE     7 (to 28)
    # 14 LOAD_GLOBAL              0 (BASE_EXEC_PREFIX)
    # 26 JUMP_IF_TRUE_OR_POP      6 (to 40)
    # >>   28 LOAD_GLOBAL              2 (BASE_PREFIX)
    # >>   40 STORE_FAST               2 (prefix)
    # 42 JUMP_FORWARD            16 (to 76)
    # 322     >>   44 LOAD_FAST                0 (plat_specific)
    # 46 POP_JUMP_FORWARD_IF_FALSE     7 (to 62)
    # 48 LOAD_GLOBAL              4 (EXEC_PREFIX)
    # 60 JUMP_IF_TRUE_OR_POP      6 (to 74)
    # >>   62 LOAD_GLOBAL              6 (PREFIX)
    # >>   74 STORE_FAST               2 (prefix)
    # 324     >>   76 LOAD_GLOBAL              8 (os)
    # 88 LOAD_ATTR                5 (name)
    # 98 LOAD_CONST               2 ('posix')
    # 100 COMPARE_OP               2 (==)
    # 106 POP_JUMP_FORWARD_IF_FALSE   103 (to 314)
    # 325         108 LOAD_FAST                0 (plat_specific)
    # 110 POP_JUMP_FORWARD_IF_TRUE     2 (to 116)
    # 112 LOAD_FAST                1 (standard_lib)
    # 114 POP_JUMP_FORWARD_IF_FALSE    13 (to 142)
    # 328     >>  116 LOAD_GLOBAL             12 (sys)
    # 128 LOAD_ATTR                7 (platlibdir)
    # 138 STORE_FAST               3 (libdir)
    # 140 JUMP_FORWARD             2 (to 146)
    # 331     >>  142 LOAD_CONST               3 ('lib')
    # 144 STORE_FAST               3 (libdir)
    # 332     >>  146 LOAD_GLOBAL              8 (os)
    # 158 LOAD_ATTR                8 (path)
    # 168 LOAD_METHOD              9 (join)
    # 190 LOAD_FAST                2 (prefix)
    # 192 LOAD_FAST                3 (libdir)
    # 333         194 LOAD_CONST               4 ('python')
    # 196 LOAD_GLOBAL             21 (NULL + get_python_version)
    # 208 PRECALL                  0
    # 212 CALL                     0
    # 222 BINARY_OP                0 (+)
    # 332         226 PRECALL                  3
    # 230 CALL                     3
    # 240 STORE_FAST               4 (libpython)
    # 334         242 LOAD_FAST                1 (standard_lib)
    # 244 POP_JUMP_FORWARD_IF_FALSE     2 (to 250)
    # 335         246 LOAD_FAST                4 (libpython)
    # 248 RETURN_VALUE
    # 337     >>  250 LOAD_GLOBAL              8 (os)
    # 262 LOAD_ATTR                8 (path)
    # 272 LOAD_METHOD              9 (join)
    # 294 LOAD_FAST                4 (libpython)
    # 296 LOAD_CONST               5 ('site-packages')
    # 298 PRECALL                  2
    # 302 CALL                     2
    # 312 RETURN_VALUE
    # 338     >>  314 LOAD_GLOBAL              8 (os)
    # 326 LOAD_ATTR                5 (name)
    # 336 LOAD_CONST               6 ('nt')
    # 338 COMPARE_OP               2 (==)
    # 344 POP_JUMP_FORWARD_IF_FALSE    67 (to 480)
    # 339         346 LOAD_FAST                1 (standard_lib)
    # 348 POP_JUMP_FORWARD_IF_FALSE    32 (to 414)
    # 340         350 LOAD_GLOBAL              8 (os)
    # 362 LOAD_ATTR                8 (path)
    # 372 LOAD_METHOD              9 (join)
    # 394 LOAD_FAST                2 (prefix)
    # 396 LOAD_CONST               7 ('Lib')
    # 398 PRECALL                  2
    # 402 CALL                     2
    # 412 RETURN_VALUE
    # 342     >>  414 LOAD_GLOBAL              8 (os)
    # 426 LOAD_ATTR                8 (path)
    # 436 LOAD_METHOD              9 (join)
    # 458 LOAD_FAST                2 (prefix)
    # 460 LOAD_CONST               7 ('Lib')
    # 462 LOAD_CONST               5 ('site-packages')
    # 464 PRECALL                  3
    # 468 CALL                     3
    # 478 RETURN_VALUE
    # 344     >>  480 LOAD_GLOBAL             23 (NULL + DistutilsPlatformError)
    # 345         492 LOAD_CONST               8 ("I don't know where Python installs its library on platform '%s'")
    # 346         494 LOAD_GLOBAL              8 (os)
    # 506 LOAD_ATTR                5 (name)
    # 345         516 BINARY_OP                6 (%)
    # 344         520 PRECALL                  1
    # 524 CALL                     1
    # 534 RAISE_VARARGS            1
