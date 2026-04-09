# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: json\scanner.py

"""JSON token scanner
"""

import re
from _json import make_scanner

def py_make_scanner(context):
    # 0 MAKE_CELL                2 (_scan_once)
    # 2 MAKE_CELL                3 (match_number)
    # 4 MAKE_CELL                4 (memo)
    # 6 MAKE_CELL                5 (object_hook)
    # 8 MAKE_CELL                6 (object_pairs_hook)
    # 10 MAKE_CELL                7 (parse_array)
    # 12 MAKE_CELL                8 (parse_constant)
    # 14 MAKE_CELL                9 (parse_float)
    # 16 MAKE_CELL               10 (parse_int)
    # 18 MAKE_CELL               11 (parse_object)
    # 20 MAKE_CELL               12 (parse_string)
    # 22 MAKE_CELL               13 (strict)
    # 15          24 RESUME                   0
    # 16          26 LOAD_FAST                0 (context)
    # 28 LOAD_ATTR                0 (parse_object)
    # 38 STORE_DEREF             11 (parse_object)
    # 17          40 LOAD_FAST                0 (context)
    # 42 LOAD_ATTR                1 (parse_array)
    # 52 STORE_DEREF              7 (parse_array)
    # 18          54 LOAD_FAST                0 (context)
    # 56 LOAD_ATTR                2 (parse_string)
    # 66 STORE_DEREF             12 (parse_string)
    # 19          68 LOAD_GLOBAL              6 (NUMBER_RE)
    # 80 LOAD_ATTR                4 (match)
    # 90 STORE_DEREF              3 (match_number)
    # 20          92 LOAD_FAST                0 (context)
    # 94 LOAD_ATTR                5 (strict)
    # 104 STORE_DEREF             13 (strict)
    # 21         106 LOAD_FAST                0 (context)
    # 108 LOAD_ATTR                6 (parse_float)
    # 118 STORE_DEREF              9 (parse_float)
    # 22         120 LOAD_FAST                0 (context)
    # 122 LOAD_ATTR                7 (parse_int)
    # 132 STORE_DEREF             10 (parse_int)
    # 23         134 LOAD_FAST                0 (context)
    # 136 LOAD_ATTR                8 (parse_constant)
    # 146 STORE_DEREF              8 (parse_constant)
    # 24         148 LOAD_FAST                0 (context)
    # 150 LOAD_ATTR                9 (object_hook)
    # 160 STORE_DEREF              5 (object_hook)
    # 25         162 LOAD_FAST                0 (context)
    # 164 LOAD_ATTR               10 (object_pairs_hook)
    # 174 STORE_DEREF              6 (object_pairs_hook)
    # 26         176 LOAD_FAST                0 (context)
    # 178 LOAD_ATTR               11 (memo)
    # 188 STORE_DEREF              4 (memo)
    # 28         190 LOAD_CLOSURE             2 (_scan_once)
    # 192 LOAD_CLOSURE             3 (match_number)
    # 194 LOAD_CLOSURE             4 (memo)
    # 196 LOAD_CLOSURE             5 (object_hook)
    # 198 LOAD_CLOSURE             6 (object_pairs_hook)
    # 200 LOAD_CLOSURE             7 (parse_array)
    # 202 LOAD_CLOSURE             8 (parse_constant)
    # 204 LOAD_CLOSURE             9 (parse_float)
    # 206 LOAD_CLOSURE            10 (parse_int)
    # 208 LOAD_CLOSURE            11 (parse_object)
    # 210 LOAD_CLOSURE            12 (parse_string)
    # 212 LOAD_CLOSURE            13 (strict)
    # 214 BUILD_TUPLE             12
    # 216 LOAD_CONST               1 (<code object _scan_once at 0x000001EBD752A660, file "json\scanner.py", line 28>)
    # 218 MAKE_FUNCTION            8 (closure)
    # 220 STORE_DEREF              2 (_scan_once)
    # 65         222 LOAD_CLOSURE             2 (_scan_once)
    # 224 LOAD_CLOSURE             4 (memo)
    # 226 BUILD_TUPLE              2
    # 228 LOAD_CONST               2 (<code object scan_once at 0x000001EBD7E30C10, file "json\scanner.py", line 65>)
    # 230 MAKE_FUNCTION            8 (closure)
    # 232 STORE_FAST               1 (scan_once)
    # 71         234 LOAD_FAST                1 (scan_once)
    # 236 RETURN_VALUE
    # Disassembly of <code object _scan_once at 0x000001EBD752A660, file "json\scanner.py", line 28>:
    # 0 COPY_FREE_VARS          12
    # 28           2 RESUME                   0
    # 29           4 NOP
    # 30           6 LOAD_FAST                0 (string)
    # 8 LOAD_FAST                1 (idx)
    # 10 BINARY_SUBSCR
    # 20 STORE_FAST               2 (nextchar)
    # 22 JUMP_FORWARD            30 (to 84)
    # >>   24 PUSH_EXC_INFO
    # 31          26 LOAD_GLOBAL              0 (IndexError)
    # 38 CHECK_EXC_MATCH
    # 40 POP_JUMP_FORWARD_IF_FALSE    17 (to 76)
    # 42 POP_TOP
    # 32          44 LOAD_GLOBAL              3 (NULL + StopIteration)
    # 56 LOAD_FAST                1 (idx)
    # 58 PRECALL                  1
    # 62 CALL                     1
    # 72 LOAD_CONST               0 (None)
    # 74 RAISE_VARARGS            2
    # 31     >>   76 RERAISE                  0
    # >>   78 COPY                     3
    # 80 POP_EXCEPT
    # 82 RERAISE                  1
    # 34     >>   84 LOAD_FAST                2 (nextchar)
    # 86 LOAD_CONST               1 ('"')
    # 88 COMPARE_OP               2 (==)
    # 94 POP_JUMP_FORWARD_IF_FALSE    16 (to 128)
    # 35          96 PUSH_NULL
    # 98 LOAD_DEREF              18 (parse_string)
    # 100 LOAD_FAST                0 (string)
    # 102 LOAD_FAST                1 (idx)
    # 104 LOAD_CONST               2 (1)
    # 106 BINARY_OP                0 (+)
    # 110 LOAD_DEREF              19 (strict)
    # 112 PRECALL                  3
    # 116 CALL                     3
    # 126 RETURN_VALUE
    # 36     >>  128 LOAD_FAST                2 (nextchar)
    # 130 LOAD_CONST               3 ('{')
    # 132 COMPARE_OP               2 (==)
    # 138 POP_JUMP_FORWARD_IF_FALSE    21 (to 182)
    # 37         140 PUSH_NULL
    # 142 LOAD_DEREF              17 (parse_object)
    # 144 LOAD_FAST                0 (string)
    # 146 LOAD_FAST                1 (idx)
    # 148 LOAD_CONST               2 (1)
    # 150 BINARY_OP                0 (+)
    # 154 BUILD_TUPLE              2
    # 156 LOAD_DEREF              19 (strict)
    # 38         158 LOAD_DEREF               8 (_scan_once)
    # 160 LOAD_DEREF              11 (object_hook)
    # 162 LOAD_DEREF              12 (object_pairs_hook)
    # 164 LOAD_DEREF              10 (memo)
    # 37         166 PRECALL                  6
    # 170 CALL                     6
    # 180 RETURN_VALUE
    # 39     >>  182 LOAD_FAST                2 (nextchar)
    # 184 LOAD_CONST               4 ('[')
    # 186 COMPARE_OP               2 (==)
    # 192 POP_JUMP_FORWARD_IF_FALSE    17 (to 228)
    # 40         194 PUSH_NULL
    # 196 LOAD_DEREF              13 (parse_array)
    # 198 LOAD_FAST                0 (string)
    # 200 LOAD_FAST                1 (idx)
    # 202 LOAD_CONST               2 (1)
    # 204 BINARY_OP                0 (+)
    # 208 BUILD_TUPLE              2
    # 210 LOAD_DEREF               8 (_scan_once)
    # 212 PRECALL                  2
    # 216 CALL                     2
    # 226 RETURN_VALUE
    # 41     >>  228 LOAD_FAST                2 (nextchar)
    # 230 LOAD_CONST               5 ('n')
    # 232 COMPARE_OP               2 (==)
    # 238 POP_JUMP_FORWARD_IF_FALSE    24 (to 288)
    # 240 LOAD_FAST                0 (string)
    # 242 LOAD_FAST                1 (idx)
    # 244 LOAD_FAST                1 (idx)
    # 246 LOAD_CONST               6 (4)
    # 248 BINARY_OP                0 (+)
    # 252 BUILD_SLICE              2
    # 254 BINARY_SUBSCR
    # 264 LOAD_CONST               7 ('null')
    # 266 COMPARE_OP               2 (==)
    # 272 POP_JUMP_FORWARD_IF_FALSE     7 (to 288)
    # 42         274 LOAD_CONST               0 (None)
    # 276 LOAD_FAST                1 (idx)
    # 278 LOAD_CONST               6 (4)
    # 280 BINARY_OP                0 (+)
    # 284 BUILD_TUPLE              2
    # 286 RETURN_VALUE
    # 43     >>  288 LOAD_FAST                2 (nextchar)
    # 290 LOAD_CONST               8 ('t')
    # 292 COMPARE_OP               2 (==)
    # 298 POP_JUMP_FORWARD_IF_FALSE    24 (to 348)
    # 300 LOAD_FAST                0 (string)
    # 302 LOAD_FAST                1 (idx)
    # 304 LOAD_FAST                1 (idx)
    # 306 LOAD_CONST               6 (4)
    # 308 BINARY_OP                0 (+)
    # 312 BUILD_SLICE              2
    # 314 BINARY_SUBSCR
    # 324 LOAD_CONST               9 ('true')
    # 326 COMPARE_OP               2 (==)
    # 332 POP_JUMP_FORWARD_IF_FALSE     7 (to 348)
    # 44         334 LOAD_CONST              10 (True)
    # 336 LOAD_FAST                1 (idx)
    # 338 LOAD_CONST               6 (4)
    # 340 BINARY_OP                0 (+)
    # 344 BUILD_TUPLE              2
    # 346 RETURN_VALUE
    # 45     >>  348 LOAD_FAST                2 (nextchar)
    # 350 LOAD_CONST              11 ('f')
    # 352 COMPARE_OP               2 (==)
    # 358 POP_JUMP_FORWARD_IF_FALSE    24 (to 408)
    # 360 LOAD_FAST                0 (string)
    # 362 LOAD_FAST                1 (idx)
    # 364 LOAD_FAST                1 (idx)
    # 366 LOAD_CONST              12 (5)
    # 368 BINARY_OP                0 (+)
    # 372 BUILD_SLICE              2
    # 374 BINARY_SUBSCR
    # 384 LOAD_CONST              13 ('false')
    # 386 COMPARE_OP               2 (==)
    # 392 POP_JUMP_FORWARD_IF_FALSE     7 (to 408)
    # 46         394 LOAD_CONST              14 (False)
    # 396 LOAD_FAST                1 (idx)
    # 398 LOAD_CONST              12 (5)
    # 400 BINARY_OP                0 (+)
    # 404 BUILD_TUPLE              2
    # 406 RETURN_VALUE
    # 48     >>  408 PUSH_NULL
    # 410 LOAD_DEREF               9 (match_number)
    # 412 LOAD_FAST                0 (string)
    # 414 LOAD_FAST                1 (idx)
    # 416 PRECALL                  2
    # 420 CALL                     2
    # 430 STORE_FAST               3 (m)
    # 49         432 LOAD_FAST                3 (m)
    # 434 POP_JUMP_FORWARD_IF_NONE    83 (to 602)
    # 50         436 LOAD_FAST                3 (m)
    # 438 LOAD_METHOD              2 (groups)
    # 460 PRECALL                  0
    # 464 CALL                     0
    # 474 UNPACK_SEQUENCE          3
    # 478 STORE_FAST               4 (integer)
    # 480 STORE_FAST               5 (frac)
    # 482 STORE_FAST               6 (exp)
    # 51         484 LOAD_FAST                5 (frac)
    # 486 POP_JUMP_FORWARD_IF_TRUE     2 (to 492)
    # 488 LOAD_FAST                6 (exp)
    # 490 POP_JUMP_FORWARD_IF_FALSE    22 (to 536)
    # 52     >>  492 PUSH_NULL
    # 494 LOAD_DEREF              15 (parse_float)
    # 496 LOAD_FAST                4 (integer)
    # 498 LOAD_FAST                5 (frac)
    # 500 JUMP_IF_TRUE_OR_POP      1 (to 504)
    # 502 LOAD_CONST              15 ('')
    # >>  504 BINARY_OP                0 (+)
    # 508 LOAD_FAST                6 (exp)
    # 510 JUMP_IF_TRUE_OR_POP      1 (to 514)
    # 512 LOAD_CONST              15 ('')
    # >>  514 BINARY_OP                0 (+)
    # 518 PRECALL                  1
    # 522 CALL                     1
    # 532 STORE_FAST               7 (res)
    # 534 JUMP_FORWARD            11 (to 558)
    # 54     >>  536 PUSH_NULL
    # 538 LOAD_DEREF              16 (parse_int)
    # 540 LOAD_FAST                4 (integer)
    # 542 PRECALL                  1
    # 546 CALL                     1
    # 556 STORE_FAST               7 (res)
    # 55     >>  558 LOAD_FAST                7 (res)
    # 560 LOAD_FAST                3 (m)
    # 562 LOAD_METHOD              3 (end)
    # 584 PRECALL                  0
    # 588 CALL                     0
    # 598 BUILD_TUPLE              2
    # 600 RETURN_VALUE
    # 56     >>  602 LOAD_FAST                2 (nextchar)
    # 604 LOAD_CONST              16 ('N')
    # 606 COMPARE_OP               2 (==)
    # 612 POP_JUMP_FORWARD_IF_FALSE    33 (to 680)
    # 614 LOAD_FAST                0 (string)
    # 616 LOAD_FAST                1 (idx)
    # 618 LOAD_FAST                1 (idx)
    # 620 LOAD_CONST              17 (3)
    # 622 BINARY_OP                0 (+)
    # 626 BUILD_SLICE              2
    # 628 BINARY_SUBSCR
    # 638 LOAD_CONST              18 ('NaN')
    # 640 COMPARE_OP               2 (==)
    # 646 POP_JUMP_FORWARD_IF_FALSE    16 (to 680)
    # 57         648 PUSH_NULL
    # 650 LOAD_DEREF              14 (parse_constant)
    # 652 LOAD_CONST              18 ('NaN')
    # 654 PRECALL                  1
    # 658 CALL                     1
    # 668 LOAD_FAST                1 (idx)
    # 670 LOAD_CONST              17 (3)
    # 672 BINARY_OP                0 (+)
    # 676 BUILD_TUPLE              2
    # 678 RETURN_VALUE
    # 58     >>  680 LOAD_FAST                2 (nextchar)
    # 682 LOAD_CONST              19 ('I')
    # 684 COMPARE_OP               2 (==)
    # 690 POP_JUMP_FORWARD_IF_FALSE    33 (to 758)
    # 692 LOAD_FAST                0 (string)
    # 694 LOAD_FAST                1 (idx)
    # 696 LOAD_FAST                1 (idx)
    # 698 LOAD_CONST              20 (8)
    # 700 BINARY_OP                0 (+)
    # 704 BUILD_SLICE              2
    # 706 BINARY_SUBSCR
    # 716 LOAD_CONST              21 ('Infinity')
    # 718 COMPARE_OP               2 (==)
    # 724 POP_JUMP_FORWARD_IF_FALSE    16 (to 758)
    # 59         726 PUSH_NULL
    # 728 LOAD_DEREF              14 (parse_constant)
    # 730 LOAD_CONST              21 ('Infinity')
    # 732 PRECALL                  1
    # 736 CALL                     1
    # 746 LOAD_FAST                1 (idx)
    # 748 LOAD_CONST              20 (8)
    # 750 BINARY_OP                0 (+)
    # 754 BUILD_TUPLE              2
    # 756 RETURN_VALUE
    # 60     >>  758 LOAD_FAST                2 (nextchar)
    # 760 LOAD_CONST              22 ('-')
    # 762 COMPARE_OP               2 (==)
    # 768 POP_JUMP_FORWARD_IF_FALSE    33 (to 836)
    # 770 LOAD_FAST                0 (string)
    # 772 LOAD_FAST                1 (idx)
    # 774 LOAD_FAST                1 (idx)
    # 776 LOAD_CONST              23 (9)
    # 778 BINARY_OP                0 (+)
    # 782 BUILD_SLICE              2
    # 784 BINARY_SUBSCR
    # 794 LOAD_CONST              24 ('-Infinity')
    # 796 COMPARE_OP               2 (==)
    # 802 POP_JUMP_FORWARD_IF_FALSE    16 (to 836)
    # 61         804 PUSH_NULL
    # 806 LOAD_DEREF              14 (parse_constant)
    # 808 LOAD_CONST              24 ('-Infinity')
    # 810 PRECALL                  1
    # 814 CALL                     1
    # 824 LOAD_FAST                1 (idx)
    # 826 LOAD_CONST              23 (9)
    # 828 BINARY_OP                0 (+)
    # 832 BUILD_TUPLE              2
    # 834 RETURN_VALUE
    # 63     >>  836 LOAD_GLOBAL              3 (NULL + StopIteration)
    # 848 LOAD_FAST                1 (idx)
    # 850 PRECALL                  1
    # 854 CALL                     1
    # 864 RAISE_VARARGS            1
    # ExceptionTable:
    # 6 to 20 -> 24 [0]
    # 24 to 76 -> 78 [1] lasti
    # Disassembly of <code object scan_once at 0x000001EBD7E30C10, file "json\scanner.py", line 65>:
    # 0 COPY_FREE_VARS           2
    # 65           2 RESUME                   0
    # 66           4 NOP
    # 67           6 PUSH_NULL
    # 8 LOAD_DEREF               2 (_scan_once)
    # 10 LOAD_FAST                0 (string)
    # 12 LOAD_FAST                1 (idx)
    # 14 PRECALL                  2
    # 18 CALL                     2
    # 69          28 LOAD_DEREF               3 (memo)
    # 30 LOAD_METHOD              0 (clear)
    # 52 PRECALL                  0
    # 56 CALL                     0
    # 66 POP_TOP
    # 68 RETURN_VALUE
    # >>   70 PUSH_EXC_INFO
    # 72 LOAD_DEREF               3 (memo)
    # 74 LOAD_METHOD              0 (clear)
    # 96 PRECALL                  0
    # 100 CALL                     0
    # 110 POP_TOP
    # 112 RERAISE                  0
    # >>  114 COPY                     3
    # 116 POP_EXCEPT
    # 118 RERAISE                  1
    # ExceptionTable:
    # 6 to 26 -> 70 [0]
    # 70 to 112 -> 114 [1] lasti
