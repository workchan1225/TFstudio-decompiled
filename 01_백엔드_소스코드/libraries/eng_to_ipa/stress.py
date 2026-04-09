# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: eng_to_ipa\stress.py

import os
import re
import json
from eng_to_ipa.syllables import syllables
import logging

def create_phones_json():
    """Creates the phones.json file in the resources directory from the phones.txt source file from CMU"""
    # 8           0 RESUME                   0
    # 10           2 BUILD_MAP                0
    # 4 STORE_FAST               0 (phones_dict)
    # 11           6 LOAD_GLOBAL              1 (NULL + open)
    # 18 LOAD_GLOBAL              2 (os)
    # 30 LOAD_ATTR                2 (path)
    # 40 LOAD_METHOD              3 (join)
    # 62 LOAD_GLOBAL              2 (os)
    # 74 LOAD_ATTR                2 (path)
    # 84 LOAD_METHOD              4 (abspath)
    # 106 LOAD_GLOBAL              2 (os)
    # 118 LOAD_ATTR                2 (path)
    # 128 LOAD_METHOD              5 (dirname)
    # 150 LOAD_GLOBAL             12 (__file__)
    # 162 PRECALL                  1
    # 166 CALL                     1
    # 176 PRECALL                  1
    # 180 CALL                     1
    # 12         190 LOAD_CONST               1 ('resources')
    # 192 LOAD_CONST               2 ('CMU_source_files')
    # 194 LOAD_CONST               3 ('cmudict-0.7b.phones.txt')
    # 11         196 PRECALL                  4
    # 200 CALL                     4
    # 12         210 LOAD_CONST               4 ('UTF-8')
    # 11         212 KW_NAMES                 5
    # 214 PRECALL                  2
    # 218 CALL                     2
    # 228 BEFORE_WITH
    # 12         230 STORE_FAST               1 (phones_txt)
    # 14         232 LOAD_FAST                1 (phones_txt)
    # 234 LOAD_METHOD              7 (readlines)
    # 256 PRECALL                  0
    # 260 CALL                     0
    # 270 GET_ITER
    # >>  272 FOR_ITER                95 (to 464)
    # 274 STORE_FAST               2 (line)
    # 15         276 LOAD_FAST                2 (line)
    # 278 LOAD_METHOD              8 (split)
    # 300 LOAD_CONST               6 ('\t')
    # 302 PRECALL                  1
    # 306 CALL                     1
    # 316 LOAD_CONST               7 (1)
    # 318 BINARY_SUBSCR
    # 328 LOAD_METHOD              9 (replace)
    # 350 LOAD_CONST               8 ('\n')
    # 352 LOAD_CONST               9 ('')
    # 354 PRECALL                  2
    # 358 CALL                     2
    # 368 LOAD_FAST                0 (phones_dict)
    # 370 LOAD_FAST                2 (line)
    # 372 LOAD_METHOD              8 (split)
    # 394 LOAD_CONST               6 ('\t')
    # 396 PRECALL                  1
    # 400 CALL                     1
    # 410 LOAD_CONST              10 (0)
    # 412 BINARY_SUBSCR
    # 422 LOAD_METHOD             10 (lower)
    # 444 PRECALL                  0
    # 448 CALL                     0
    # 458 STORE_SUBSCR
    # 462 JUMP_BACKWARD           96 (to 272)
    # 14     >>  464 NOP
    # 11         466 LOAD_CONST              11 (None)
    # 468 LOAD_CONST              11 (None)
    # 470 LOAD_CONST              11 (None)
    # 472 PRECALL                  2
    # 476 CALL                     2
    # 486 POP_TOP
    # 488 JUMP_FORWARD            11 (to 512)
    # >>  490 PUSH_EXC_INFO
    # 492 WITH_EXCEPT_START
    # 494 POP_JUMP_FORWARD_IF_TRUE     4 (to 504)
    # 496 RERAISE                  2
    # >>  498 COPY                     3
    # 500 POP_EXCEPT
    # 502 RERAISE                  1
    # >>  504 POP_TOP
    # 506 POP_EXCEPT
    # 508 POP_TOP
    # 510 POP_TOP
    # 17     >>  512 LOAD_GLOBAL              1 (NULL + open)
    # 524 LOAD_GLOBAL              2 (os)
    # 536 LOAD_ATTR                2 (path)
    # 546 LOAD_METHOD              3 (join)
    # 568 LOAD_GLOBAL              2 (os)
    # 580 LOAD_ATTR                2 (path)
    # 590 LOAD_METHOD              4 (abspath)
    # 612 LOAD_GLOBAL              2 (os)
    # 624 LOAD_ATTR                2 (path)
    # 634 LOAD_METHOD              5 (dirname)
    # 656 LOAD_GLOBAL             12 (__file__)
    # 668 PRECALL                  1
    # 672 CALL                     1
    # 682 PRECALL                  1
    # 686 CALL                     1
    # 18         696 LOAD_CONST               1 ('resources')
    # 698 LOAD_CONST              12 ('phones.json')
    # 17         700 PRECALL                  3
    # 704 CALL                     3
    # 18         714 LOAD_CONST              13 ('w')
    # 17         716 PRECALL                  2
    # 720 CALL                     2
    # 730 BEFORE_WITH
    # 18         732 STORE_FAST               3 (phones_json)
    # 19         734 LOAD_GLOBAL             23 (NULL + json)
    # 746 LOAD_ATTR               12 (dump)
    # 756 LOAD_FAST                0 (phones_dict)
    # 758 LOAD_FAST                3 (phones_json)
    # 760 PRECALL                  2
    # 764 CALL                     2
    # 774 POP_TOP
    # 17         776 LOAD_CONST              11 (None)
    # 778 LOAD_CONST              11 (None)
    # 780 LOAD_CONST              11 (None)
    # 782 PRECALL                  2
    # 786 CALL                     2
    # 796 POP_TOP
    # 798 LOAD_CONST              11 (None)
    # 800 RETURN_VALUE
    # >>  802 PUSH_EXC_INFO
    # 804 WITH_EXCEPT_START
    # 806 POP_JUMP_FORWARD_IF_TRUE     4 (to 816)
    # 808 RERAISE                  2
    # >>  810 COPY                     3
    # 812 POP_EXCEPT
    # 814 RERAISE                  1
    # >>  816 POP_TOP
    # 818 POP_EXCEPT
    # 820 POP_TOP
    # 822 POP_TOP
    # 824 LOAD_CONST              11 (None)
    # 826 RETURN_VALUE
    # ExceptionTable:
    # 230 to 462 -> 490 [1] lasti
    # 490 to 496 -> 498 [3] lasti
    # 504 to 504 -> 498 [3] lasti
    # 732 to 774 -> 802 [1] lasti
    # 802 to 808 -> 810 [3] lasti
    # 816 to 816 -> 810 [3] lasti

def stress_type(stress):
    """Determine the kind of stress that should be evaluated"""
    # 22           0 RESUME                   0
    # 24           2 LOAD_FAST                0 (stress)
    # 4 LOAD_METHOD              0 (lower)
    # 26 PRECALL                  0
    # 30 CALL                     0
    # 40 STORE_FAST               0 (stress)
    # 25          42 LOAD_CONST               1 ('ˈ')
    # 44 LOAD_CONST               2 ('ˌ')
    # 46 LOAD_CONST               3 (('1', '2'))
    # 48 BUILD_CONST_KEY_MAP      2
    # 50 STORE_FAST               1 (default)
    # 26          52 LOAD_FAST                0 (stress)
    # 54 LOAD_CONST               4 ('primary')
    # 56 COMPARE_OP               2 (==)
    # 62 POP_JUMP_FORWARD_IF_FALSE     4 (to 72)
    # 27          64 LOAD_CONST               5 ('1')
    # 66 LOAD_CONST               1 ('ˈ')
    # 68 BUILD_MAP                1
    # 70 RETURN_VALUE
    # 28     >>   72 LOAD_FAST                0 (stress)
    # 74 LOAD_CONST               6 ('secondary')
    # 76 COMPARE_OP               2 (==)
    # 82 POP_JUMP_FORWARD_IF_FALSE     4 (to 92)
    # 29          84 LOAD_CONST               7 ('2')
    # 86 LOAD_CONST               2 ('ˌ')
    # 88 BUILD_MAP                1
    # 90 RETURN_VALUE
    # 30     >>   92 LOAD_FAST                0 (stress)
    # 94 LOAD_CONST               8 ('both')
    # 96 COMPARE_OP               2 (==)
    # 102 POP_JUMP_FORWARD_IF_TRUE     6 (to 116)
    # 104 LOAD_FAST                0 (stress)
    # 106 LOAD_CONST               9 ('all')
    # 108 COMPARE_OP               2 (==)
    # 114 POP_JUMP_FORWARD_IF_FALSE     2 (to 120)
    # 31     >>  116 LOAD_FAST                1 (default)
    # 118 RETURN_VALUE
    # 33     >>  120 LOAD_GLOBAL              3 (NULL + logging)
    # 132 LOAD_ATTR                2 (warning)
    # 142 LOAD_CONST              10 ('WARNING: stress type parameter ')
    # 144 LOAD_FAST                0 (stress)
    # 146 BINARY_OP                0 (+)
    # 150 LOAD_CONST              11 (' not recognized.')
    # 152 BINARY_OP                0 (+)
    # 156 PRECALL                  1
    # 160 CALL                     1
    # 170 POP_TOP
    # 35         172 LOAD_FAST                1 (default)
    # 174 RETURN_VALUE

def find_stress(word, type):
    """Convert stress marking numbers from CMU into actual stress markings
    :param word: the CMU word string to be evaluated for stress markings
    :param type: type of stress to be evaluated (primary, secondary, or both)"""
    # 42           0 RESUME                   0
    # 47           2 LOAD_GLOBAL              1 (NULL + syllables)
    # 14 LOAD_ATTR                1 (cmu_syllable_count)
    # 24 LOAD_FAST                0 (word)
    # 26 PRECALL                  1
    # 30 CALL                     1
    # 40 STORE_FAST               2 (syll_count)
    # 49          42 LOAD_FAST                0 (word)
    # 44 LOAD_METHOD              2 (startswith)
    # 66 LOAD_CONST               1 ('__IGNORE__')
    # 68 PRECALL                  1
    # 72 CALL                     1
    # 82 EXTENDED_ARG             2
    # 84 POP_JUMP_FORWARD_IF_TRUE   679 (to 1444)
    # 86 LOAD_FAST                2 (syll_count)
    # 88 LOAD_CONST               2 (1)
    # 90 COMPARE_OP               4 (>)
    # 96 EXTENDED_ARG             2
    # 98 POP_JUMP_FORWARD_IF_FALSE   672 (to 1444)
    # 50         100 LOAD_FAST                0 (word)
    # 102 LOAD_METHOD              3 (split)
    # 124 LOAD_CONST               3 (' ')
    # 126 PRECALL                  1
    # 130 CALL                     1
    # 140 STORE_FAST               3 (symbols)
    # 51         142 LOAD_GLOBAL              9 (NULL + stress_type)
    # 154 LOAD_FAST                1 (type)
    # 156 PRECALL                  1
    # 160 CALL                     1
    # 170 STORE_FAST               4 (stress_map)
    # 52         172 BUILD_LIST               0
    # 174 STORE_FAST               5 (new_word)
    # 53         176 BUILD_LIST               0
    # 178 LOAD_CONST               4 (('sp', 'st', 'sk', 'fr', 'fl'))
    # 180 LIST_EXTEND              1
    # 182 STORE_FAST               6 (clusters)
    # 54         184 BUILD_LIST               0
    # 186 LOAD_CONST               5 (('nasal', 'fricative', 'vowel'))
    # 188 LIST_EXTEND              1
    # 190 STORE_FAST               7 (stop_set)
    # 56         192 LOAD_FAST                3 (symbols)
    # 194 GET_ITER
    # >>  196 EXTENDED_ARG             2
    # 198 FOR_ITER               601 (to 1402)
    # 200 STORE_FAST               8 (c)
    # 58         202 LOAD_FAST                8 (c)
    # 204 LOAD_CONST               6 (-1)
    # 206 BINARY_SUBSCR
    # 216 LOAD_FAST                4 (stress_map)
    # 218 LOAD_METHOD              5 (keys)
    # 240 PRECALL                  0
    # 244 CALL                     0
    # 254 CONTAINS_OP              0
    # 256 EXTENDED_ARG             1
    # 258 POP_JUMP_FORWARD_IF_FALSE   484 (to 1228)
    # 60         260 LOAD_FAST                5 (new_word)
    # 262 POP_JUMP_FORWARD_IF_TRUE    76 (to 416)
    # 62         264 LOAD_FAST                5 (new_word)
    # 266 LOAD_METHOD              6 (append)
    # 288 LOAD_GLOBAL             15 (NULL + re)
    # 300 LOAD_ATTR                8 (sub)
    # 310 LOAD_CONST               7 ('\\d')
    # 312 LOAD_CONST               8 ('')
    # 314 LOAD_FAST                4 (stress_map)
    # 316 LOAD_GLOBAL             15 (NULL + re)
    # 328 LOAD_ATTR                9 (findall)
    # 338 LOAD_CONST               7 ('\\d')
    # 340 LOAD_FAST                8 (c)
    # 342 PRECALL                  2
    # 346 CALL                     2
    # 356 LOAD_CONST               9 (0)
    # 358 BINARY_SUBSCR
    # 368 BINARY_SUBSCR
    # 378 LOAD_FAST                8 (c)
    # 380 BINARY_OP                0 (+)
    # 384 PRECALL                  3
    # 388 CALL                     3
    # 398 PRECALL                  1
    # 402 CALL                     1
    # 412 POP_TOP
    # 414 JUMP_BACKWARD          110 (to 196)
    # 64     >>  416 LOAD_FAST                4 (stress_map)
    # 418 LOAD_FAST                8 (c)
    # 420 LOAD_CONST               6 (-1)
    # 422 BINARY_SUBSCR
    # 432 BINARY_SUBSCR
    # 442 STORE_FAST               9 (stress_mark)
    # 65         444 LOAD_CONST              10 (False)
    # 446 STORE_FAST              10 (placed)
    # 66         448 LOAD_CONST              10 (False)
    # 450 STORE_FAST              11 (hiatus)
    # 67         452 LOAD_FAST                5 (new_word)
    # 454 LOAD_CONST              11 (None)
    # 456 LOAD_CONST              11 (None)
    # 458 LOAD_CONST               6 (-1)
    # 460 BUILD_SLICE              3
    # 462 BINARY_SUBSCR
    # 472 STORE_FAST               5 (new_word)
    # 68         474 LOAD_GLOBAL             21 (NULL + enumerate)
    # 486 LOAD_FAST                5 (new_word)
    # 488 PRECALL                  1
    # 492 CALL                     1
    # 502 GET_ITER
    # >>  504 FOR_ITER               253 (to 1012)
    # 506 UNPACK_SEQUENCE          2
    # 510 STORE_FAST              12 (i)
    # 512 STORE_FAST              13 (sym)
    # 69         514 LOAD_GLOBAL             15 (NULL + re)
    # 526 LOAD_ATTR                8 (sub)
    # 536 LOAD_CONST              12 ('[0-9ˈˌ]')
    # 538 LOAD_CONST               8 ('')
    # 540 LOAD_FAST               13 (sym)
    # 542 PRECALL                  3
    # 546 CALL                     3
    # 556 STORE_FAST              13 (sym)
    # 70         558 LOAD_GLOBAL             15 (NULL + re)
    # 570 LOAD_ATTR                8 (sub)
    # 580 LOAD_CONST              12 ('[0-9ˈˌ]')
    # 582 LOAD_CONST               8 ('')
    # 584 LOAD_FAST                5 (new_word)
    # 586 LOAD_FAST               12 (i)
    # 588 LOAD_CONST               2 (1)
    # 590 BINARY_OP               10 (-)
    # 594 BINARY_SUBSCR
    # 604 PRECALL                  3
    # 608 CALL                     3
    # 618 STORE_FAST              14 (prev_sym)
    # 71         620 LOAD_GLOBAL             22 (phones)
    # 632 LOAD_GLOBAL             15 (NULL + re)
    # 644 LOAD_ATTR                8 (sub)
    # 654 LOAD_CONST              12 ('[0-9ˈˌ]')
    # 656 LOAD_CONST               8 ('')
    # 658 LOAD_FAST                5 (new_word)
    # 660 LOAD_FAST               12 (i)
    # 662 LOAD_CONST               2 (1)
    # 664 BINARY_OP               10 (-)
    # 668 BINARY_SUBSCR
    # 678 PRECALL                  3
    # 682 CALL                     3
    # 692 BINARY_SUBSCR
    # 702 STORE_FAST              15 (prev_phone)
    # 72         704 LOAD_GLOBAL             22 (phones)
    # 716 LOAD_FAST               13 (sym)
    # 718 BINARY_SUBSCR
    # 728 LOAD_FAST                7 (stop_set)
    # 730 CONTAINS_OP              0
    # 732 POP_JUMP_FORWARD_IF_TRUE    16 (to 766)
    # 734 LOAD_FAST               12 (i)
    # 736 LOAD_CONST               9 (0)
    # 738 COMPARE_OP               4 (>)
    # 744 POP_JUMP_FORWARD_IF_FALSE     6 (to 758)
    # 746 LOAD_FAST               15 (prev_phone)
    # 748 LOAD_CONST              13 ('stop')
    # 750 COMPARE_OP               2 (==)
    # 756 POP_JUMP_FORWARD_IF_TRUE     4 (to 766)
    # >>  758 LOAD_FAST               13 (sym)
    # 760 LOAD_CONST              14 (('er', 'w', 'j'))
    # 762 CONTAINS_OP              0
    # 764 POP_JUMP_FORWARD_IF_FALSE   122 (to 1010)
    # 73     >>  766 LOAD_FAST               13 (sym)
    # 768 LOAD_FAST               14 (prev_sym)
    # 770 BINARY_OP                0 (+)
    # 774 LOAD_FAST                6 (clusters)
    # 776 CONTAINS_OP              0
    # 778 POP_JUMP_FORWARD_IF_FALSE    15 (to 810)
    # 74         780 LOAD_FAST                9 (stress_mark)
    # 782 LOAD_FAST                5 (new_word)
    # 784 LOAD_FAST               12 (i)
    # 786 BINARY_SUBSCR
    # 796 BINARY_OP                0 (+)
    # 800 LOAD_FAST                5 (new_word)
    # 802 LOAD_FAST               12 (i)
    # 804 STORE_SUBSCR
    # 808 JUMP_FORWARD            96 (to 1002)
    # 75     >>  810 LOAD_FAST               15 (prev_phone)
    # 812 LOAD_CONST              15 ('vowel')
    # 814 COMPARE_OP               2 (==)
    # 820 POP_JUMP_FORWARD_IF_TRUE    27 (to 876)
    # 822 LOAD_FAST               12 (i)
    # 824 LOAD_CONST               9 (0)
    # 826 COMPARE_OP               4 (>)
    # 832 POP_JUMP_FORWARD_IF_FALSE    21 (to 876)
    # 76         834 LOAD_FAST                9 (stress_mark)
    # 836 LOAD_FAST                5 (new_word)
    # 838 LOAD_FAST               12 (i)
    # 840 LOAD_CONST               2 (1)
    # 842 BINARY_OP               10 (-)
    # 846 BINARY_SUBSCR
    # 856 BINARY_OP                0 (+)
    # 860 LOAD_FAST                5 (new_word)
    # 862 LOAD_FAST               12 (i)
    # 864 LOAD_CONST               2 (1)
    # 866 BINARY_OP               10 (-)
    # 870 STORE_SUBSCR
    # 874 JUMP_FORWARD            63 (to 1002)
    # 78     >>  876 LOAD_GLOBAL             22 (phones)
    # 888 LOAD_FAST               13 (sym)
    # 890 BINARY_SUBSCR
    # 900 LOAD_CONST              15 ('vowel')
    # 902 COMPARE_OP               2 (==)
    # 908 POP_JUMP_FORWARD_IF_FALSE    32 (to 974)
    # 79         910 LOAD_CONST              16 (True)
    # 912 STORE_FAST              11 (hiatus)
    # 80         914 LOAD_FAST                9 (stress_mark)
    # 916 LOAD_GLOBAL             15 (NULL + re)
    # 928 LOAD_ATTR                8 (sub)
    # 938 LOAD_CONST              12 ('[0-9ˈˌ]')
    # 940 LOAD_CONST               8 ('')
    # 942 LOAD_FAST                8 (c)
    # 944 PRECALL                  3
    # 948 CALL                     3
    # 958 BINARY_OP                0 (+)
    # 962 BUILD_LIST               1
    # 964 LOAD_FAST                5 (new_word)
    # 966 BINARY_OP                0 (+)
    # 970 STORE_FAST               5 (new_word)
    # 972 JUMP_FORWARD            14 (to 1002)
    # 82     >>  974 LOAD_FAST                9 (stress_mark)
    # 976 LOAD_FAST                5 (new_word)
    # 978 LOAD_FAST               12 (i)
    # 980 BINARY_SUBSCR
    # 990 BINARY_OP                0 (+)
    # 994 LOAD_FAST                5 (new_word)
    # 996 LOAD_FAST               12 (i)
    # 998 STORE_SUBSCR
    # 83     >> 1002 LOAD_CONST              16 (True)
    # 1004 STORE_FAST              10 (placed)
    # 84        1006 POP_TOP
    # 1008 JUMP_FORWARD             1 (to 1012)
    # 72     >> 1010 JUMP_BACKWARD          254 (to 504)
    # 85     >> 1012 LOAD_FAST               10 (placed)
    # 1014 POP_JUMP_FORWARD_IF_TRUE    48 (to 1112)
    # 86        1016 LOAD_FAST                5 (new_word)
    # 1018 POP_JUMP_FORWARD_IF_FALSE    46 (to 1112)
    # 87        1020 LOAD_FAST                9 (stress_mark)
    # 1022 LOAD_FAST                5 (new_word)
    # 1024 LOAD_GLOBAL             25 (NULL + len)
    # 1036 LOAD_FAST                5 (new_word)
    # 1038 PRECALL                  1
    # 1042 CALL                     1
    # 1052 LOAD_CONST               2 (1)
    # 1054 BINARY_OP               10 (-)
    # 1058 BINARY_SUBSCR
    # 1068 BINARY_OP                0 (+)
    # 1072 LOAD_FAST                5 (new_word)
    # 1074 LOAD_GLOBAL             25 (NULL + len)
    # 1086 LOAD_FAST                5 (new_word)
    # 1088 PRECALL                  1
    # 1092 CALL                     1
    # 1102 LOAD_CONST               2 (1)
    # 1104 BINARY_OP               10 (-)
    # 1108 STORE_SUBSCR
    # 88     >> 1112 LOAD_FAST                5 (new_word)
    # 1114 LOAD_CONST              11 (None)
    # 1116 LOAD_CONST              11 (None)
    # 1118 LOAD_CONST               6 (-1)
    # 1120 BUILD_SLICE              3
    # 1122 BINARY_SUBSCR
    # 1132 STORE_FAST               5 (new_word)
    # 89        1134 LOAD_FAST               11 (hiatus)
    # 1136 POP_JUMP_FORWARD_IF_TRUE    43 (to 1224)
    # 90        1138 LOAD_FAST                5 (new_word)
    # 1140 LOAD_METHOD              6 (append)
    # 1162 LOAD_GLOBAL             15 (NULL + re)
    # 1174 LOAD_ATTR                8 (sub)
    # 1184 LOAD_CONST               7 ('\\d')
    # 1186 LOAD_CONST               8 ('')
    # 1188 LOAD_FAST                8 (c)
    # 1190 PRECALL                  3
    # 1194 CALL                     3
    # 1204 PRECALL                  1
    # 1208 CALL                     1
    # 1218 POP_TOP
    # 91        1220 LOAD_CONST              10 (False)
    # 1222 STORE_FAST              11 (hiatus)
    # >> 1224 EXTENDED_ARG             2
    # 1226 JUMP_BACKWARD          516 (to 196)
    # 93     >> 1228 LOAD_FAST                8 (c)
    # 1230 LOAD_METHOD              2 (startswith)
    # 1252 LOAD_CONST               1 ('__IGNORE__')
    # 1254 PRECALL                  1
    # 1258 CALL                     1
    # 1268 POP_JUMP_FORWARD_IF_FALSE    23 (to 1316)
    # 94        1270 LOAD_FAST                5 (new_word)
    # 1272 LOAD_METHOD              6 (append)
    # 1294 LOAD_FAST                8 (c)
    # 1296 PRECALL                  1
    # 1300 CALL                     1
    # 1310 POP_TOP
    # 1312 EXTENDED_ARG             2
    # 1314 JUMP_BACKWARD          560 (to 196)
    # 96     >> 1316 LOAD_FAST                5 (new_word)
    # 1318 LOAD_METHOD              6 (append)
    # 1340 LOAD_GLOBAL             15 (NULL + re)
    # 1352 LOAD_ATTR                8 (sub)
    # 1362 LOAD_CONST               7 ('\\d')
    # 1364 LOAD_CONST               8 ('')
    # 1366 LOAD_FAST                8 (c)
    # 1368 PRECALL                  3
    # 1372 CALL                     3
    # 1382 PRECALL                  1
    # 1386 CALL                     1
    # 1396 POP_TOP
    # 1398 EXTENDED_ARG             2
    # 1400 JUMP_BACKWARD          603 (to 196)
    # 98     >> 1402 LOAD_CONST               3 (' ')
    # 1404 LOAD_METHOD             13 (join)
    # 1426 LOAD_FAST                5 (new_word)
    # 1428 PRECALL                  1
    # 1432 CALL                     1
    # 1442 RETURN_VALUE
    # 100     >> 1444 LOAD_FAST                0 (word)
    # 1446 LOAD_METHOD              2 (startswith)
    # 1468 LOAD_CONST               1 ('__IGNORE__')
    # 1470 PRECALL                  1
    # 1474 CALL                     1
    # 1484 POP_JUMP_FORWARD_IF_FALSE     2 (to 1490)
    # 101        1486 LOAD_FAST                0 (word)
    # 1488 RETURN_VALUE
    # 103     >> 1490 LOAD_GLOBAL             15 (NULL + re)
    # 1502 LOAD_ATTR                8 (sub)
    # 1512 LOAD_CONST              17 ('[0-9]')
    # 1514 LOAD_CONST               8 ('')
    # 1516 LOAD_FAST                0 (word)
    # 1518 PRECALL                  3
    # 1522 CALL                     3
    # 1532 RETURN_VALUE
