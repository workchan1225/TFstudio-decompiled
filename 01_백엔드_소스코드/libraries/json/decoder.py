# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: json\decoder.py

"""Implementation of JSONDecoder
"""

import re
from json import scanner
from _json import scanstring

class JSONDecodeError:
    """JSONDecodeError"""
    def __init__(self, msg, doc, pos):
        # 31           0 RESUME                   0
        # 32           2 LOAD_FAST                2 (doc)
        # 4 LOAD_METHOD              0 (count)
        # 26 LOAD_CONST               1 ('\n')
        # 28 LOAD_CONST               2 (0)
        # 30 LOAD_FAST                3 (pos)
        # 32 PRECALL                  3
        # 36 CALL                     3
        # 46 LOAD_CONST               3 (1)
        # 48 BINARY_OP                0 (+)
        # 52 STORE_FAST               4 (lineno)
        # 33          54 LOAD_FAST                3 (pos)
        # 56 LOAD_FAST                2 (doc)
        # 58 LOAD_METHOD              1 (rfind)
        # 80 LOAD_CONST               1 ('\n')
        # 82 LOAD_CONST               2 (0)
        # 84 LOAD_FAST                3 (pos)
        # 86 PRECALL                  3
        # 90 CALL                     3
        # 100 BINARY_OP               10 (-)
        # 104 STORE_FAST               5 (colno)
        # 34         106 LOAD_CONST               4 ('%s: line %d column %d (char %d)')
        # 108 LOAD_FAST                1 (msg)
        # 110 LOAD_FAST                4 (lineno)
        # 112 LOAD_FAST                5 (colno)
        # 114 LOAD_FAST                3 (pos)
        # 116 BUILD_TUPLE              4
        # 118 BINARY_OP                6 (%)
        # 122 STORE_FAST               6 (errmsg)
        # 35         124 LOAD_GLOBAL              4 (ValueError)
        # 136 LOAD_METHOD              3 (__init__)
        # 158 LOAD_FAST                0 (self)
        # 160 LOAD_FAST                6 (errmsg)
        # 162 PRECALL                  2
        # 166 CALL                     2
        # 176 POP_TOP
        # 36         178 LOAD_FAST                1 (msg)
        # 180 LOAD_FAST                0 (self)
        # 182 STORE_ATTR               4 (msg)
        # 37         192 LOAD_FAST                2 (doc)
        # 194 LOAD_FAST                0 (self)
        # 196 STORE_ATTR               5 (doc)
        # 38         206 LOAD_FAST                3 (pos)
        # 208 LOAD_FAST                0 (self)
        # 210 STORE_ATTR               6 (pos)
        # 39         220 LOAD_FAST                4 (lineno)
        # 222 LOAD_FAST                0 (self)
        # 224 STORE_ATTR               7 (lineno)
        # 40         234 LOAD_FAST                5 (colno)
        # 236 LOAD_FAST                0 (self)
        # 238 STORE_ATTR               8 (colno)
        # 248 LOAD_CONST               0 (None)
        # 250 RETURN_VALUE

    def __reduce__(self):
        # 42           0 RESUME                   0
        # 43           2 LOAD_FAST                0 (self)
        # 4 LOAD_ATTR                0 (__class__)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_ATTR                1 (msg)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_ATTR                2 (doc)
        # 38 LOAD_FAST                0 (self)
        # 40 LOAD_ATTR                3 (pos)
        # 50 BUILD_TUPLE              3
        # 52 BUILD_TUPLE              2
        # 54 RETURN_VALUE


def _decode_uXXXX(s, pos):
    # 59           0 RESUME                   0
    # 60           2 LOAD_FAST                0 (s)
    # 4 LOAD_FAST                1 (pos)
    # 6 LOAD_CONST               1 (1)
    # 8 BINARY_OP                0 (+)
    # 12 LOAD_FAST                1 (pos)
    # 14 LOAD_CONST               2 (5)
    # 16 BINARY_OP                0 (+)
    # 20 BUILD_SLICE              2
    # 22 BINARY_SUBSCR
    # 32 STORE_FAST               2 (esc)
    # 61          34 LOAD_GLOBAL              1 (NULL + len)
    # 46 LOAD_FAST                2 (esc)
    # 48 PRECALL                  1
    # 52 CALL                     1
    # 62 LOAD_CONST               3 (4)
    # 64 COMPARE_OP               2 (==)
    # 70 POP_JUMP_FORWARD_IF_FALSE    43 (to 158)
    # 72 LOAD_FAST                2 (esc)
    # 74 LOAD_CONST               1 (1)
    # 76 BINARY_SUBSCR
    # 86 LOAD_CONST               4 ('xX')
    # 88 CONTAINS_OP              1
    # 90 POP_JUMP_FORWARD_IF_FALSE    33 (to 158)
    # 62          92 NOP
    # 63          94 LOAD_GLOBAL              3 (NULL + int)
    # 106 LOAD_FAST                2 (esc)
    # 108 LOAD_CONST               5 (16)
    # 110 PRECALL                  2
    # 114 CALL                     2
    # 124 RETURN_VALUE
    # >>  126 PUSH_EXC_INFO
    # 64         128 LOAD_GLOBAL              4 (ValueError)
    # 140 CHECK_EXC_MATCH
    # 142 POP_JUMP_FORWARD_IF_FALSE     3 (to 150)
    # 144 POP_TOP
    # 65         146 POP_EXCEPT
    # 148 JUMP_FORWARD             4 (to 158)
    # 64     >>  150 RERAISE                  0
    # >>  152 COPY                     3
    # 154 POP_EXCEPT
    # 156 RERAISE                  1
    # 66     >>  158 LOAD_CONST               6 ('Invalid \\uXXXX escape')
    # 160 STORE_FAST               3 (msg)
    # 67         162 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 174 LOAD_FAST                3 (msg)
    # 176 LOAD_FAST                0 (s)
    # 178 LOAD_FAST                1 (pos)
    # 180 PRECALL                  3
    # 184 CALL                     3
    # 194 RAISE_VARARGS            1
    # ExceptionTable:
    # 94 to 122 -> 126 [0]
    # 126 to 144 -> 152 [1] lasti
    # 150 to 150 -> 152 [1] lasti

def py_scanstring(s, end, strict, _b, _m):
    """Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.

    Returns a tuple of the decoded string and the index of the character in s
    after the end quote."""
    # 69           0 RESUME                   0
    # 79           2 BUILD_LIST               0
    # 4 STORE_FAST               5 (chunks)
    # 80           6 LOAD_FAST                5 (chunks)
    # 8 LOAD_ATTR                0 (append)
    # 18 STORE_FAST               6 (_append)
    # 81          20 LOAD_FAST                1 (end)
    # 22 LOAD_CONST               1 (1)
    # 24 BINARY_OP               10 (-)
    # 28 STORE_FAST               7 (begin)
    # 82     >>   30 NOP
    # 83     >>   32 PUSH_NULL
    # 34 LOAD_FAST                4 (_m)
    # 36 LOAD_FAST                0 (s)
    # 38 LOAD_FAST                1 (end)
    # 40 PRECALL                  2
    # 44 CALL                     2
    # 54 STORE_FAST               8 (chunk)
    # 84          56 LOAD_FAST                8 (chunk)
    # 58 POP_JUMP_FORWARD_IF_NOT_NONE    17 (to 94)
    # 85          60 LOAD_GLOBAL              3 (NULL + JSONDecodeError)
    # 72 LOAD_CONST               3 ('Unterminated string starting at')
    # 74 LOAD_FAST                0 (s)
    # 76 LOAD_FAST                7 (begin)
    # 78 PRECALL                  3
    # 82 CALL                     3
    # 92 RAISE_VARARGS            1
    # 86     >>   94 LOAD_FAST                8 (chunk)
    # 96 LOAD_METHOD              2 (end)
    # 118 PRECALL                  0
    # 122 CALL                     0
    # 132 STORE_FAST               1 (end)
    # 87         134 LOAD_FAST                8 (chunk)
    # 136 LOAD_METHOD              3 (groups)
    # 158 PRECALL                  0
    # 162 CALL                     0
    # 172 UNPACK_SEQUENCE          2
    # 176 STORE_FAST               9 (content)
    # 178 STORE_FAST              10 (terminator)
    # 89         180 LOAD_FAST                9 (content)
    # 182 POP_JUMP_FORWARD_IF_FALSE    11 (to 206)
    # 90         184 PUSH_NULL
    # 186 LOAD_FAST                6 (_append)
    # 188 LOAD_FAST                9 (content)
    # 190 PRECALL                  1
    # 194 CALL                     1
    # 204 POP_TOP
    # 93     >>  206 LOAD_FAST               10 (terminator)
    # 208 LOAD_CONST               4 ('"')
    # 210 COMPARE_OP               2 (==)
    # 216 POP_JUMP_FORWARD_IF_FALSE     2 (to 222)
    # 94         218 EXTENDED_ARG             1
    # 220 JUMP_FORWARD           313 (to 848)
    # 95     >>  222 LOAD_FAST               10 (terminator)
    # 224 LOAD_CONST               5 ('\\')
    # 226 COMPARE_OP               3 (!=)
    # 232 POP_JUMP_FORWARD_IF_FALSE    52 (to 338)
    # 96         234 LOAD_FAST                2 (strict)
    # 236 POP_JUMP_FORWARD_IF_FALSE    38 (to 314)
    # 98         238 LOAD_CONST               6 ('Invalid control character {0!r} at')
    # 240 LOAD_METHOD              4 (format)
    # 262 LOAD_FAST               10 (terminator)
    # 264 PRECALL                  1
    # 268 CALL                     1
    # 278 STORE_FAST              11 (msg)
    # 99         280 LOAD_GLOBAL              3 (NULL + JSONDecodeError)
    # 292 LOAD_FAST               11 (msg)
    # 294 LOAD_FAST                0 (s)
    # 296 LOAD_FAST                1 (end)
    # 298 PRECALL                  3
    # 302 CALL                     3
    # 312 RAISE_VARARGS            1
    # 101     >>  314 PUSH_NULL
    # 316 LOAD_FAST                6 (_append)
    # 318 LOAD_FAST               10 (terminator)
    # 320 PRECALL                  1
    # 324 CALL                     1
    # 334 POP_TOP
    # 102         336 JUMP_BACKWARD          154 (to 30)
    # 103     >>  338 NOP
    # 104         340 LOAD_FAST                0 (s)
    # 342 LOAD_FAST                1 (end)
    # 344 BINARY_SUBSCR
    # 354 STORE_FAST              12 (esc)
    # 356 JUMP_FORWARD            32 (to 422)
    # >>  358 PUSH_EXC_INFO
    # 105         360 LOAD_GLOBAL             10 (IndexError)
    # 372 CHECK_EXC_MATCH
    # 374 POP_JUMP_FORWARD_IF_FALSE    19 (to 414)
    # 376 POP_TOP
    # 106         378 LOAD_GLOBAL              3 (NULL + JSONDecodeError)
    # 390 LOAD_CONST               3 ('Unterminated string starting at')
    # 107         392 LOAD_FAST                0 (s)
    # 394 LOAD_FAST                7 (begin)
    # 106         396 PRECALL                  3
    # 400 CALL                     3
    # 107         410 LOAD_CONST               2 (None)
    # 106         412 RAISE_VARARGS            2
    # 105     >>  414 RERAISE                  0
    # >>  416 COPY                     3
    # 418 POP_EXCEPT
    # 420 RERAISE                  1
    # 109     >>  422 LOAD_FAST               12 (esc)
    # 424 LOAD_CONST               7 ('u')
    # 426 COMPARE_OP               3 (!=)
    # 432 POP_JUMP_FORWARD_IF_FALSE    68 (to 570)
    # 110         434 NOP
    # 111         436 LOAD_FAST                3 (_b)
    # 438 LOAD_FAST               12 (esc)
    # 440 BINARY_SUBSCR
    # 450 STORE_FAST              13 (char)
    # 452 JUMP_FORWARD            52 (to 558)
    # >>  454 PUSH_EXC_INFO
    # 112         456 LOAD_GLOBAL             12 (KeyError)
    # 468 CHECK_EXC_MATCH
    # 470 POP_JUMP_FORWARD_IF_FALSE    39 (to 550)
    # 472 POP_TOP
    # 113         474 LOAD_CONST               8 ('Invalid \\escape: {0!r}')
    # 476 LOAD_METHOD              4 (format)
    # 498 LOAD_FAST               12 (esc)
    # 500 PRECALL                  1
    # 504 CALL                     1
    # 514 STORE_FAST              11 (msg)
    # 114         516 LOAD_GLOBAL              3 (NULL + JSONDecodeError)
    # 528 LOAD_FAST               11 (msg)
    # 530 LOAD_FAST                0 (s)
    # 532 LOAD_FAST                1 (end)
    # 534 PRECALL                  3
    # 538 CALL                     3
    # 548 RAISE_VARARGS            1
    # 112     >>  550 RERAISE                  0
    # >>  552 COPY                     3
    # 554 POP_EXCEPT
    # 556 RERAISE                  1
    # 115     >>  558 LOAD_FAST                1 (end)
    # 560 LOAD_CONST               1 (1)
    # 562 BINARY_OP               13 (+=)
    # 566 STORE_FAST               1 (end)
    # 568 JUMP_FORWARD           126 (to 822)
    # 117     >>  570 LOAD_GLOBAL             15 (NULL + _decode_uXXXX)
    # 582 LOAD_FAST                0 (s)
    # 584 LOAD_FAST                1 (end)
    # 586 PRECALL                  2
    # 590 CALL                     2
    # 600 STORE_FAST              14 (uni)
    # 118         602 LOAD_FAST                1 (end)
    # 604 LOAD_CONST               9 (5)
    # 606 BINARY_OP               13 (+=)
    # 610 STORE_FAST               1 (end)
    # 119         612 LOAD_CONST              10 (55296)
    # 614 LOAD_FAST               14 (uni)
    # 616 SWAP                     2
    # 618 COPY                     2
    # 620 COMPARE_OP               1 (<=)
    # 626 POP_JUMP_FORWARD_IF_FALSE     6 (to 640)
    # 628 LOAD_CONST              11 (56319)
    # 630 COMPARE_OP               1 (<=)
    # 636 POP_JUMP_FORWARD_IF_FALSE    77 (to 792)
    # 638 JUMP_FORWARD             2 (to 644)
    # >>  640 POP_TOP
    # 642 JUMP_FORWARD            74 (to 792)
    # >>  644 LOAD_FAST                0 (s)
    # 646 LOAD_FAST                1 (end)
    # 648 LOAD_FAST                1 (end)
    # 650 LOAD_CONST              12 (2)
    # 652 BINARY_OP                0 (+)
    # 656 BUILD_SLICE              2
    # 658 BINARY_SUBSCR
    # 668 LOAD_CONST              13 ('\\u')
    # 670 COMPARE_OP               2 (==)
    # 676 POP_JUMP_FORWARD_IF_FALSE    57 (to 792)
    # 120         678 LOAD_GLOBAL             15 (NULL + _decode_uXXXX)
    # 690 LOAD_FAST                0 (s)
    # 692 LOAD_FAST                1 (end)
    # 694 LOAD_CONST               1 (1)
    # 696 BINARY_OP                0 (+)
    # 700 PRECALL                  2
    # 704 CALL                     2
    # 714 STORE_FAST              15 (uni2)
    # 121         716 LOAD_CONST              14 (56320)
    # 718 LOAD_FAST               15 (uni2)
    # 720 SWAP                     2
    # 722 COPY                     2
    # 724 COMPARE_OP               1 (<=)
    # 730 POP_JUMP_FORWARD_IF_FALSE     6 (to 744)
    # 732 LOAD_CONST              15 (57343)
    # 734 COMPARE_OP               1 (<=)
    # 740 POP_JUMP_FORWARD_IF_FALSE    25 (to 792)
    # 742 JUMP_FORWARD             2 (to 748)
    # >>  744 POP_TOP
    # 746 JUMP_FORWARD            22 (to 792)
    # 122     >>  748 LOAD_CONST              16 (65536)
    # 750 LOAD_FAST               14 (uni)
    # 752 LOAD_CONST              10 (55296)
    # 754 BINARY_OP               10 (-)
    # 758 LOAD_CONST              17 (10)
    # 760 BINARY_OP                3 (<<)
    # 764 LOAD_FAST               15 (uni2)
    # 766 LOAD_CONST              14 (56320)
    # 768 BINARY_OP               10 (-)
    # 772 BINARY_OP                7 (|)
    # 776 BINARY_OP                0 (+)
    # 780 STORE_FAST              14 (uni)
    # 123         782 LOAD_FAST                1 (end)
    # 784 LOAD_CONST              18 (6)
    # 786 BINARY_OP               13 (+=)
    # 790 STORE_FAST               1 (end)
    # 124     >>  792 LOAD_GLOBAL             17 (NULL + chr)
    # 804 LOAD_FAST               14 (uni)
    # 806 PRECALL                  1
    # 810 CALL                     1
    # 820 STORE_FAST              13 (char)
    # 125     >>  822 PUSH_NULL
    # 824 LOAD_FAST                6 (_append)
    # 826 LOAD_FAST               13 (char)
    # 828 PRECALL                  1
    # 832 CALL                     1
    # 842 POP_TOP
    # 82         844 EXTENDED_ARG             1
    # 846 JUMP_BACKWARD          408 (to 32)
    # 126     >>  848 LOAD_CONST              19 ('')
    # 850 LOAD_METHOD              9 (join)
    # 872 LOAD_FAST                5 (chunks)
    # 874 PRECALL                  1
    # 878 CALL                     1
    # 888 LOAD_FAST                1 (end)
    # 890 BUILD_TUPLE              2
    # 892 RETURN_VALUE
    # ExceptionTable:
    # 340 to 354 -> 358 [0]
    # 358 to 414 -> 416 [1] lasti
    # 436 to 450 -> 454 [0]
    # 454 to 550 -> 552 [1] lasti

def JSONObject(s_and_end, strict, scan_once, object_hook, object_pairs_hook, memo, _w, _ws):
    # 136           0 RESUME                   0
    # 138           2 LOAD_FAST                0 (s_and_end)
    # 4 UNPACK_SEQUENCE          2
    # 8 STORE_FAST               8 (s)
    # 10 STORE_FAST               9 (end)
    # 139          12 BUILD_LIST               0
    # 14 STORE_FAST              10 (pairs)
    # 140          16 LOAD_FAST               10 (pairs)
    # 18 LOAD_ATTR                0 (append)
    # 28 STORE_FAST              11 (pairs_append)
    # 142          30 LOAD_FAST                5 (memo)
    # 32 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 38)
    # 143          34 BUILD_MAP                0
    # 36 STORE_FAST               5 (memo)
    # 144     >>   38 LOAD_FAST                5 (memo)
    # 40 LOAD_ATTR                1 (setdefault)
    # 50 STORE_FAST              12 (memo_get)
    # 147          52 LOAD_FAST                8 (s)
    # 54 LOAD_FAST                9 (end)
    # 56 LOAD_FAST                9 (end)
    # 58 LOAD_CONST               1 (1)
    # 60 BINARY_OP                0 (+)
    # 64 BUILD_SLICE              2
    # 66 BINARY_SUBSCR
    # 76 STORE_FAST              13 (nextchar)
    # 149          78 LOAD_FAST               13 (nextchar)
    # 80 LOAD_CONST               2 ('"')
    # 82 COMPARE_OP               3 (!=)
    # 88 POP_JUMP_FORWARD_IF_FALSE   118 (to 326)
    # 150          90 LOAD_FAST               13 (nextchar)
    # 92 LOAD_FAST                7 (_ws)
    # 94 CONTAINS_OP              0
    # 96 POP_JUMP_FORWARD_IF_FALSE    43 (to 184)
    # 151          98 PUSH_NULL
    # 100 LOAD_FAST                6 (_w)
    # 102 LOAD_FAST                8 (s)
    # 104 LOAD_FAST                9 (end)
    # 106 PRECALL                  2
    # 110 CALL                     2
    # 120 LOAD_METHOD              2 (end)
    # 142 PRECALL                  0
    # 146 CALL                     0
    # 156 STORE_FAST               9 (end)
    # 152         158 LOAD_FAST                8 (s)
    # 160 LOAD_FAST                9 (end)
    # 162 LOAD_FAST                9 (end)
    # 164 LOAD_CONST               1 (1)
    # 166 BINARY_OP                0 (+)
    # 170 BUILD_SLICE              2
    # 172 BINARY_SUBSCR
    # 182 STORE_FAST              13 (nextchar)
    # 154     >>  184 LOAD_FAST               13 (nextchar)
    # 186 LOAD_CONST               3 ('}')
    # 188 COMPARE_OP               2 (==)
    # 194 POP_JUMP_FORWARD_IF_FALSE    42 (to 280)
    # 155         196 LOAD_FAST                4 (object_pairs_hook)
    # 198 POP_JUMP_FORWARD_IF_NONE    18 (to 236)
    # 156         200 PUSH_NULL
    # 202 LOAD_FAST                4 (object_pairs_hook)
    # 204 LOAD_FAST               10 (pairs)
    # 206 PRECALL                  1
    # 210 CALL                     1
    # 220 STORE_FAST              14 (result)
    # 157         222 LOAD_FAST               14 (result)
    # 224 LOAD_FAST                9 (end)
    # 226 LOAD_CONST               1 (1)
    # 228 BINARY_OP                0 (+)
    # 232 BUILD_TUPLE              2
    # 234 RETURN_VALUE
    # 158     >>  236 BUILD_MAP                0
    # 238 STORE_FAST              10 (pairs)
    # 159         240 LOAD_FAST                3 (object_hook)
    # 242 POP_JUMP_FORWARD_IF_NONE    11 (to 266)
    # 160         244 PUSH_NULL
    # 246 LOAD_FAST                3 (object_hook)
    # 248 LOAD_FAST               10 (pairs)
    # 250 PRECALL                  1
    # 254 CALL                     1
    # 264 STORE_FAST              10 (pairs)
    # 161     >>  266 LOAD_FAST               10 (pairs)
    # 268 LOAD_FAST                9 (end)
    # 270 LOAD_CONST               1 (1)
    # 272 BINARY_OP                0 (+)
    # 276 BUILD_TUPLE              2
    # 278 RETURN_VALUE
    # 162     >>  280 LOAD_FAST               13 (nextchar)
    # 282 LOAD_CONST               2 ('"')
    # 284 COMPARE_OP               3 (!=)
    # 290 POP_JUMP_FORWARD_IF_FALSE    17 (to 326)
    # 163         292 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 164         304 LOAD_CONST               4 ('Expecting property name enclosed in double quotes')
    # 306 LOAD_FAST                8 (s)
    # 308 LOAD_FAST                9 (end)
    # 163         310 PRECALL                  3
    # 314 CALL                     3
    # 324 RAISE_VARARGS            1
    # 165     >>  326 LOAD_FAST                9 (end)
    # 328 LOAD_CONST               1 (1)
    # 330 BINARY_OP               13 (+=)
    # 334 STORE_FAST               9 (end)
    # 166         336 NOP
    # 167     >>  338 LOAD_GLOBAL              9 (NULL + scanstring)
    # 350 LOAD_FAST                8 (s)
    # 352 LOAD_FAST                9 (end)
    # 354 LOAD_FAST                1 (strict)
    # 356 PRECALL                  3
    # 360 CALL                     3
    # 370 UNPACK_SEQUENCE          2
    # 374 STORE_FAST              15 (key)
    # 376 STORE_FAST               9 (end)
    # 168         378 PUSH_NULL
    # 380 LOAD_FAST               12 (memo_get)
    # 382 LOAD_FAST               15 (key)
    # 384 LOAD_FAST               15 (key)
    # 386 PRECALL                  2
    # 390 CALL                     2
    # 400 STORE_FAST              15 (key)
    # 171         402 LOAD_FAST                8 (s)
    # 404 LOAD_FAST                9 (end)
    # 406 LOAD_FAST                9 (end)
    # 408 LOAD_CONST               1 (1)
    # 410 BINARY_OP                0 (+)
    # 414 BUILD_SLICE              2
    # 416 BINARY_SUBSCR
    # 426 LOAD_CONST               6 (':')
    # 428 COMPARE_OP               3 (!=)
    # 434 POP_JUMP_FORWARD_IF_FALSE    64 (to 564)
    # 172         436 PUSH_NULL
    # 438 LOAD_FAST                6 (_w)
    # 440 LOAD_FAST                8 (s)
    # 442 LOAD_FAST                9 (end)
    # 444 PRECALL                  2
    # 448 CALL                     2
    # 458 LOAD_METHOD              2 (end)
    # 480 PRECALL                  0
    # 484 CALL                     0
    # 494 STORE_FAST               9 (end)
    # 173         496 LOAD_FAST                8 (s)
    # 498 LOAD_FAST                9 (end)
    # 500 LOAD_FAST                9 (end)
    # 502 LOAD_CONST               1 (1)
    # 504 BINARY_OP                0 (+)
    # 508 BUILD_SLICE              2
    # 510 BINARY_SUBSCR
    # 520 LOAD_CONST               6 (':')
    # 522 COMPARE_OP               3 (!=)
    # 528 POP_JUMP_FORWARD_IF_FALSE    17 (to 564)
    # 174         530 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 542 LOAD_CONST               7 ("Expecting ':' delimiter")
    # 544 LOAD_FAST                8 (s)
    # 546 LOAD_FAST                9 (end)
    # 548 PRECALL                  3
    # 552 CALL                     3
    # 562 RAISE_VARARGS            1
    # 175     >>  564 LOAD_FAST                9 (end)
    # 566 LOAD_CONST               1 (1)
    # 568 BINARY_OP               13 (+=)
    # 572 STORE_FAST               9 (end)
    # 177         574 NOP
    # 178         576 LOAD_FAST                8 (s)
    # 578 LOAD_FAST                9 (end)
    # 580 BINARY_SUBSCR
    # 590 LOAD_FAST                7 (_ws)
    # 592 CONTAINS_OP              0
    # 594 POP_JUMP_FORWARD_IF_FALSE    48 (to 692)
    # 179         596 LOAD_FAST                9 (end)
    # 598 LOAD_CONST               1 (1)
    # 600 BINARY_OP               13 (+=)
    # 604 STORE_FAST               9 (end)
    # 180         606 LOAD_FAST                8 (s)
    # 608 LOAD_FAST                9 (end)
    # 610 BINARY_SUBSCR
    # 620 LOAD_FAST                7 (_ws)
    # 622 CONTAINS_OP              0
    # 624 POP_JUMP_FORWARD_IF_FALSE    33 (to 692)
    # 181         626 PUSH_NULL
    # 628 LOAD_FAST                6 (_w)
    # 630 LOAD_FAST                8 (s)
    # 632 LOAD_FAST                9 (end)
    # 634 LOAD_CONST               1 (1)
    # 636 BINARY_OP                0 (+)
    # 640 PRECALL                  2
    # 644 CALL                     2
    # 654 LOAD_METHOD              2 (end)
    # 676 PRECALL                  0
    # 680 CALL                     0
    # 690 STORE_FAST               9 (end)
    # >>  692 JUMP_FORWARD            16 (to 726)
    # >>  694 PUSH_EXC_INFO
    # 182         696 LOAD_GLOBAL             10 (IndexError)
    # 708 CHECK_EXC_MATCH
    # 710 POP_JUMP_FORWARD_IF_FALSE     3 (to 718)
    # 712 POP_TOP
    # 183         714 POP_EXCEPT
    # 716 JUMP_FORWARD             4 (to 726)
    # 182     >>  718 RERAISE                  0
    # >>  720 COPY                     3
    # 722 POP_EXCEPT
    # 724 RERAISE                  1
    # 185     >>  726 NOP
    # 186         728 PUSH_NULL
    # 730 LOAD_FAST                2 (scan_once)
    # 732 LOAD_FAST                8 (s)
    # 734 LOAD_FAST                9 (end)
    # 736 PRECALL                  2
    # 740 CALL                     2
    # 750 UNPACK_SEQUENCE          2
    # 754 STORE_FAST              16 (value)
    # 756 STORE_FAST               9 (end)
    # 758 JUMP_FORWARD            41 (to 842)
    # >>  760 PUSH_EXC_INFO
    # 187         762 LOAD_GLOBAL             12 (StopIteration)
    # 774 CHECK_EXC_MATCH
    # 776 POP_JUMP_FORWARD_IF_FALSE    28 (to 834)
    # 778 STORE_FAST              17 (err)
    # 188         780 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 792 LOAD_CONST               8 ('Expecting value')
    # 794 LOAD_FAST                8 (s)
    # 796 LOAD_FAST               17 (err)
    # 798 LOAD_ATTR                7 (value)
    # 808 PRECALL                  3
    # 812 CALL                     3
    # 822 LOAD_CONST               0 (None)
    # 824 RAISE_VARARGS            2
    # >>  826 LOAD_CONST               0 (None)
    # 828 STORE_FAST              17 (err)
    # 830 DELETE_FAST             17 (err)
    # 832 RERAISE                  1
    # 187     >>  834 RERAISE                  0
    # >>  836 COPY                     3
    # 838 POP_EXCEPT
    # 840 RERAISE                  1
    # 189     >>  842 PUSH_NULL
    # 844 LOAD_FAST               11 (pairs_append)
    # 846 LOAD_FAST               15 (key)
    # 848 LOAD_FAST               16 (value)
    # 850 BUILD_TUPLE              2
    # 852 PRECALL                  1
    # 856 CALL                     1
    # 866 POP_TOP
    # 190         868 NOP
    # 191         870 LOAD_FAST                8 (s)
    # 872 LOAD_FAST                9 (end)
    # 874 BINARY_SUBSCR
    # 884 STORE_FAST              13 (nextchar)
    # 192         886 LOAD_FAST               13 (nextchar)
    # 888 LOAD_FAST                7 (_ws)
    # 890 CONTAINS_OP              0
    # 892 POP_JUMP_FORWARD_IF_FALSE    41 (to 976)
    # 193         894 PUSH_NULL
    # 896 LOAD_FAST                6 (_w)
    # 898 LOAD_FAST                8 (s)
    # 900 LOAD_FAST                9 (end)
    # 902 LOAD_CONST               1 (1)
    # 904 BINARY_OP                0 (+)
    # 908 PRECALL                  2
    # 912 CALL                     2
    # 922 LOAD_METHOD              2 (end)
    # 944 PRECALL                  0
    # 948 CALL                     0
    # 958 STORE_FAST               9 (end)
    # 194         960 LOAD_FAST                8 (s)
    # 962 LOAD_FAST                9 (end)
    # 964 BINARY_SUBSCR
    # 974 STORE_FAST              13 (nextchar)
    # >>  976 JUMP_FORWARD            18 (to 1014)
    # >>  978 PUSH_EXC_INFO
    # 195         980 LOAD_GLOBAL             10 (IndexError)
    # 992 CHECK_EXC_MATCH
    # 994 POP_JUMP_FORWARD_IF_FALSE     5 (to 1006)
    # 996 POP_TOP
    # 196         998 LOAD_CONST               9 ('')
    # 1000 STORE_FAST              13 (nextchar)
    # 1002 POP_EXCEPT
    # 1004 JUMP_FORWARD             4 (to 1014)
    # 195     >> 1006 RERAISE                  0
    # >> 1008 COPY                     3
    # 1010 POP_EXCEPT
    # 1012 RERAISE                  1
    # 197     >> 1014 LOAD_FAST                9 (end)
    # 1016 LOAD_CONST               1 (1)
    # 1018 BINARY_OP               13 (+=)
    # 1022 STORE_FAST               9 (end)
    # 199        1024 LOAD_FAST               13 (nextchar)
    # 1026 LOAD_CONST               3 ('}')
    # 1028 COMPARE_OP               2 (==)
    # 1034 POP_JUMP_FORWARD_IF_FALSE     1 (to 1038)
    # 200        1036 JUMP_FORWARD           102 (to 1242)
    # 201     >> 1038 LOAD_FAST               13 (nextchar)
    # 1040 LOAD_CONST              10 (',')
    # 1042 COMPARE_OP               3 (!=)
    # 1048 POP_JUMP_FORWARD_IF_FALSE    20 (to 1090)
    # 202        1050 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 1062 LOAD_CONST              11 ("Expecting ',' delimiter")
    # 1064 LOAD_FAST                8 (s)
    # 1066 LOAD_FAST                9 (end)
    # 1068 LOAD_CONST               1 (1)
    # 1070 BINARY_OP               10 (-)
    # 1074 PRECALL                  3
    # 1078 CALL                     3
    # 1088 RAISE_VARARGS            1
    # 203     >> 1090 PUSH_NULL
    # 1092 LOAD_FAST                6 (_w)
    # 1094 LOAD_FAST                8 (s)
    # 1096 LOAD_FAST                9 (end)
    # 1098 PRECALL                  2
    # 1102 CALL                     2
    # 1112 LOAD_METHOD              2 (end)
    # 1134 PRECALL                  0
    # 1138 CALL                     0
    # 1148 STORE_FAST               9 (end)
    # 204        1150 LOAD_FAST                8 (s)
    # 1152 LOAD_FAST                9 (end)
    # 1154 LOAD_FAST                9 (end)
    # 1156 LOAD_CONST               1 (1)
    # 1158 BINARY_OP                0 (+)
    # 1162 BUILD_SLICE              2
    # 1164 BINARY_SUBSCR
    # 1174 STORE_FAST              13 (nextchar)
    # 205        1176 LOAD_FAST                9 (end)
    # 1178 LOAD_CONST               1 (1)
    # 1180 BINARY_OP               13 (+=)
    # 1184 STORE_FAST               9 (end)
    # 206        1186 LOAD_FAST               13 (nextchar)
    # 1188 LOAD_CONST               2 ('"')
    # 1190 COMPARE_OP               3 (!=)
    # 1196 POP_JUMP_FORWARD_IF_FALSE    20 (to 1238)
    # 207        1198 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 208        1210 LOAD_CONST               4 ('Expecting property name enclosed in double quotes')
    # 1212 LOAD_FAST                8 (s)
    # 1214 LOAD_FAST                9 (end)
    # 1216 LOAD_CONST               1 (1)
    # 1218 BINARY_OP               10 (-)
    # 207        1222 PRECALL                  3
    # 1226 CALL                     3
    # 1236 RAISE_VARARGS            1
    # 166     >> 1238 EXTENDED_ARG             1
    # 1240 JUMP_BACKWARD          452 (to 338)
    # 209     >> 1242 LOAD_FAST                4 (object_pairs_hook)
    # 1244 POP_JUMP_FORWARD_IF_NONE    15 (to 1276)
    # 210        1246 PUSH_NULL
    # 1248 LOAD_FAST                4 (object_pairs_hook)
    # 1250 LOAD_FAST               10 (pairs)
    # 1252 PRECALL                  1
    # 1256 CALL                     1
    # 1266 STORE_FAST              14 (result)
    # 211        1268 LOAD_FAST               14 (result)
    # 1270 LOAD_FAST                9 (end)
    # 1272 BUILD_TUPLE              2
    # 1274 RETURN_VALUE
    # 212     >> 1276 LOAD_GLOBAL             17 (NULL + dict)
    # 1288 LOAD_FAST               10 (pairs)
    # 1290 PRECALL                  1
    # 1294 CALL                     1
    # 1304 STORE_FAST              10 (pairs)
    # 213        1306 LOAD_FAST                3 (object_hook)
    # 1308 POP_JUMP_FORWARD_IF_NONE    11 (to 1332)
    # 214        1310 PUSH_NULL
    # 1312 LOAD_FAST                3 (object_hook)
    # 1314 LOAD_FAST               10 (pairs)
    # 1316 PRECALL                  1
    # 1320 CALL                     1
    # 1330 STORE_FAST              10 (pairs)
    # 215     >> 1332 LOAD_FAST               10 (pairs)
    # 1334 LOAD_FAST                9 (end)
    # 1336 BUILD_TUPLE              2
    # 1338 RETURN_VALUE
    # ExceptionTable:
    # 576 to 690 -> 694 [0]
    # 694 to 712 -> 720 [1] lasti
    # 718 to 718 -> 720 [1] lasti
    # 728 to 756 -> 760 [0]
    # 760 to 778 -> 836 [1] lasti
    # 780 to 824 -> 826 [1] lasti
    # 826 to 834 -> 836 [1] lasti
    # 870 to 974 -> 978 [0]
    # 978 to 1000 -> 1008 [1] lasti
    # 1006 to 1006 -> 1008 [1] lasti

def JSONArray(s_and_end, scan_once, _w, _ws):
    # 217           0 RESUME                   0
    # 218           2 LOAD_FAST                0 (s_and_end)
    # 4 UNPACK_SEQUENCE          2
    # 8 STORE_FAST               4 (s)
    # 10 STORE_FAST               5 (end)
    # 219          12 BUILD_LIST               0
    # 14 STORE_FAST               6 (values)
    # 220          16 LOAD_FAST                4 (s)
    # 18 LOAD_FAST                5 (end)
    # 20 LOAD_FAST                5 (end)
    # 22 LOAD_CONST               1 (1)
    # 24 BINARY_OP                0 (+)
    # 28 BUILD_SLICE              2
    # 30 BINARY_SUBSCR
    # 40 STORE_FAST               7 (nextchar)
    # 221          42 LOAD_FAST                7 (nextchar)
    # 44 LOAD_FAST                3 (_ws)
    # 46 CONTAINS_OP              0
    # 48 POP_JUMP_FORWARD_IF_FALSE    46 (to 142)
    # 222          50 PUSH_NULL
    # 52 LOAD_FAST                2 (_w)
    # 54 LOAD_FAST                4 (s)
    # 56 LOAD_FAST                5 (end)
    # 58 LOAD_CONST               1 (1)
    # 60 BINARY_OP                0 (+)
    # 64 PRECALL                  2
    # 68 CALL                     2
    # 78 LOAD_METHOD              0 (end)
    # 100 PRECALL                  0
    # 104 CALL                     0
    # 114 STORE_FAST               5 (end)
    # 223         116 LOAD_FAST                4 (s)
    # 118 LOAD_FAST                5 (end)
    # 120 LOAD_FAST                5 (end)
    # 122 LOAD_CONST               1 (1)
    # 124 BINARY_OP                0 (+)
    # 128 BUILD_SLICE              2
    # 130 BINARY_SUBSCR
    # 140 STORE_FAST               7 (nextchar)
    # 225     >>  142 LOAD_FAST                7 (nextchar)
    # 144 LOAD_CONST               2 (']')
    # 146 COMPARE_OP               2 (==)
    # 152 POP_JUMP_FORWARD_IF_FALSE     7 (to 168)
    # 226         154 LOAD_FAST                6 (values)
    # 156 LOAD_FAST                5 (end)
    # 158 LOAD_CONST               1 (1)
    # 160 BINARY_OP                0 (+)
    # 164 BUILD_TUPLE              2
    # 166 RETURN_VALUE
    # 227     >>  168 LOAD_FAST                6 (values)
    # 170 LOAD_ATTR                1 (append)
    # 180 STORE_FAST               8 (_append)
    # 228         182 NOP
    # 229     >>  184 NOP
    # 230         186 PUSH_NULL
    # 188 LOAD_FAST                1 (scan_once)
    # 190 LOAD_FAST                4 (s)
    # 192 LOAD_FAST                5 (end)
    # 194 PRECALL                  2
    # 198 CALL                     2
    # 208 UNPACK_SEQUENCE          2
    # 212 STORE_FAST               9 (value)
    # 214 STORE_FAST               5 (end)
    # 216 JUMP_FORWARD            41 (to 300)
    # >>  218 PUSH_EXC_INFO
    # 231         220 LOAD_GLOBAL              4 (StopIteration)
    # 232 CHECK_EXC_MATCH
    # 234 POP_JUMP_FORWARD_IF_FALSE    28 (to 292)
    # 236 STORE_FAST              10 (err)
    # 232         238 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 250 LOAD_CONST               4 ('Expecting value')
    # 252 LOAD_FAST                4 (s)
    # 254 LOAD_FAST               10 (err)
    # 256 LOAD_ATTR                4 (value)
    # 266 PRECALL                  3
    # 270 CALL                     3
    # 280 LOAD_CONST               0 (None)
    # 282 RAISE_VARARGS            2
    # >>  284 LOAD_CONST               0 (None)
    # 286 STORE_FAST              10 (err)
    # 288 DELETE_FAST             10 (err)
    # 290 RERAISE                  1
    # 231     >>  292 RERAISE                  0
    # >>  294 COPY                     3
    # 296 POP_EXCEPT
    # 298 RERAISE                  1
    # 233     >>  300 PUSH_NULL
    # 302 LOAD_FAST                8 (_append)
    # 304 LOAD_FAST                9 (value)
    # 306 PRECALL                  1
    # 310 CALL                     1
    # 320 POP_TOP
    # 234         322 LOAD_FAST                4 (s)
    # 324 LOAD_FAST                5 (end)
    # 326 LOAD_FAST                5 (end)
    # 328 LOAD_CONST               1 (1)
    # 330 BINARY_OP                0 (+)
    # 334 BUILD_SLICE              2
    # 336 BINARY_SUBSCR
    # 346 STORE_FAST               7 (nextchar)
    # 235         348 LOAD_FAST                7 (nextchar)
    # 350 LOAD_FAST                3 (_ws)
    # 352 CONTAINS_OP              0
    # 354 POP_JUMP_FORWARD_IF_FALSE    46 (to 448)
    # 236         356 PUSH_NULL
    # 358 LOAD_FAST                2 (_w)
    # 360 LOAD_FAST                4 (s)
    # 362 LOAD_FAST                5 (end)
    # 364 LOAD_CONST               1 (1)
    # 366 BINARY_OP                0 (+)
    # 370 PRECALL                  2
    # 374 CALL                     2
    # 384 LOAD_METHOD              0 (end)
    # 406 PRECALL                  0
    # 410 CALL                     0
    # 420 STORE_FAST               5 (end)
    # 237         422 LOAD_FAST                4 (s)
    # 424 LOAD_FAST                5 (end)
    # 426 LOAD_FAST                5 (end)
    # 428 LOAD_CONST               1 (1)
    # 430 BINARY_OP                0 (+)
    # 434 BUILD_SLICE              2
    # 436 BINARY_SUBSCR
    # 446 STORE_FAST               7 (nextchar)
    # 238     >>  448 LOAD_FAST                5 (end)
    # 450 LOAD_CONST               1 (1)
    # 452 BINARY_OP               13 (+=)
    # 456 STORE_FAST               5 (end)
    # 239         458 LOAD_FAST                7 (nextchar)
    # 460 LOAD_CONST               2 (']')
    # 462 COMPARE_OP               2 (==)
    # 468 POP_JUMP_FORWARD_IF_FALSE     1 (to 472)
    # 240         470 JUMP_FORWARD           103 (to 678)
    # 241     >>  472 LOAD_FAST                7 (nextchar)
    # 474 LOAD_CONST               5 (',')
    # 476 COMPARE_OP               3 (!=)
    # 482 POP_JUMP_FORWARD_IF_FALSE    20 (to 524)
    # 242         484 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
    # 496 LOAD_CONST               6 ("Expecting ',' delimiter")
    # 498 LOAD_FAST                4 (s)
    # 500 LOAD_FAST                5 (end)
    # 502 LOAD_CONST               1 (1)
    # 504 BINARY_OP               10 (-)
    # 508 PRECALL                  3
    # 512 CALL                     3
    # 522 RAISE_VARARGS            1
    # 243     >>  524 NOP
    # 244         526 LOAD_FAST                4 (s)
    # 528 LOAD_FAST                5 (end)
    # 530 BINARY_SUBSCR
    # 540 LOAD_FAST                3 (_ws)
    # 542 CONTAINS_OP              0
    # 544 POP_JUMP_FORWARD_IF_FALSE    48 (to 642)
    # 245         546 LOAD_FAST                5 (end)
    # 548 LOAD_CONST               1 (1)
    # 550 BINARY_OP               13 (+=)
    # 554 STORE_FAST               5 (end)
    # 246         556 LOAD_FAST                4 (s)
    # 558 LOAD_FAST                5 (end)
    # 560 BINARY_SUBSCR
    # 570 LOAD_FAST                3 (_ws)
    # 572 CONTAINS_OP              0
    # 574 POP_JUMP_FORWARD_IF_FALSE    33 (to 642)
    # 247         576 PUSH_NULL
    # 578 LOAD_FAST                2 (_w)
    # 580 LOAD_FAST                4 (s)
    # 582 LOAD_FAST                5 (end)
    # 584 LOAD_CONST               1 (1)
    # 586 BINARY_OP                0 (+)
    # 590 PRECALL                  2
    # 594 CALL                     2
    # 604 LOAD_METHOD              0 (end)
    # 626 PRECALL                  0
    # 630 CALL                     0
    # 640 STORE_FAST               5 (end)
    # >>  642 JUMP_FORWARD            16 (to 676)
    # >>  644 PUSH_EXC_INFO
    # 248         646 LOAD_GLOBAL             10 (IndexError)
    # 658 CHECK_EXC_MATCH
    # 660 POP_JUMP_FORWARD_IF_FALSE     3 (to 668)
    # 662 POP_TOP
    # 249         664 POP_EXCEPT
    # 666 JUMP_FORWARD             4 (to 676)
    # 248     >>  668 RERAISE                  0
    # >>  670 COPY                     3
    # 672 POP_EXCEPT
    # 674 RERAISE                  1
    # 228     >>  676 JUMP_BACKWARD          247 (to 184)
    # 251     >>  678 LOAD_FAST                6 (values)
    # 680 LOAD_FAST                5 (end)
    # 682 BUILD_TUPLE              2
    # 684 RETURN_VALUE
    # ExceptionTable:
    # 186 to 214 -> 218 [0]
    # 218 to 236 -> 294 [1] lasti
    # 238 to 282 -> 284 [1] lasti
    # 284 to 292 -> 294 [1] lasti
    # 526 to 640 -> 644 [0]
    # 644 to 662 -> 670 [1] lasti
    # 668 to 668 -> 670 [1] lasti

class JSONDecoder:
    """JSONDecoder"""
    def __init__(self):
        """``object_hook``, if specified, will be called with the result
        of every JSON object decoded and its return value will be used in
        place of the given ``dict``.  This can be used to provide custom
        deserializations (e.g. to support JSON-RPC class hinting).

        ``object_pairs_hook``, if specified will be called with the result of
        every JSON object decoded with an ordered list of pairs.  The return
        value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders.
        If ``object_hook`` is also defined, the ``object_pairs_hook`` takes
        priority.

        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).

        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).

        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.

        If ``strict`` is false (true is the default), then control
        characters will be allowed inside strings.  Control characters in
        this context are those with character codes in the 0-31 range,
        including ``'\t'`` (tab), ``'\n'``, ``'\r'`` and ``'\0'``.
        """
        # 284           0 RESUME                   0
        # 319           2 LOAD_FAST                1 (object_hook)
        # 4 LOAD_FAST                0 (self)
        # 6 STORE_ATTR               0 (object_hook)
        # 320          16 LOAD_FAST                2 (parse_float)
        # 18 JUMP_IF_TRUE_OR_POP      6 (to 32)
        # 20 LOAD_GLOBAL              2 (float)
        # >>   32 LOAD_FAST                0 (self)
        # 34 STORE_ATTR               2 (parse_float)
        # 321          44 LOAD_FAST                3 (parse_int)
        # 46 JUMP_IF_TRUE_OR_POP      6 (to 60)
        # 48 LOAD_GLOBAL              6 (int)
        # >>   60 LOAD_FAST                0 (self)
        # 62 STORE_ATTR               4 (parse_int)
        # 322          72 LOAD_FAST                4 (parse_constant)
        # 74 JUMP_IF_TRUE_OR_POP     11 (to 98)
        # 76 LOAD_GLOBAL             10 (_CONSTANTS)
        # 88 LOAD_ATTR                6 (__getitem__)
        # >>   98 LOAD_FAST                0 (self)
        # 100 STORE_ATTR               7 (parse_constant)
        # 323         110 LOAD_FAST                5 (strict)
        # 112 LOAD_FAST                0 (self)
        # 114 STORE_ATTR               8 (strict)
        # 324         124 LOAD_FAST                6 (object_pairs_hook)
        # 126 LOAD_FAST                0 (self)
        # 128 STORE_ATTR               9 (object_pairs_hook)
        # 325         138 LOAD_GLOBAL             20 (JSONObject)
        # 150 LOAD_FAST                0 (self)
        # 152 STORE_ATTR              11 (parse_object)
        # 326         162 LOAD_GLOBAL             24 (JSONArray)
        # 174 LOAD_FAST                0 (self)
        # 176 STORE_ATTR              13 (parse_array)
        # 327         186 LOAD_GLOBAL             28 (scanstring)
        # 198 LOAD_FAST                0 (self)
        # 200 STORE_ATTR              15 (parse_string)
        # 328         210 BUILD_MAP                0
        # 212 LOAD_FAST                0 (self)
        # 214 STORE_ATTR              16 (memo)
        # 329         224 LOAD_GLOBAL             35 (NULL + scanner)
        # 236 LOAD_ATTR               18 (make_scanner)
        # 246 LOAD_FAST                0 (self)
        # 248 PRECALL                  1
        # 252 CALL                     1
        # 262 LOAD_FAST                0 (self)
        # 264 STORE_ATTR              19 (scan_once)
        # 274 LOAD_CONST               1 (None)
        # 276 RETURN_VALUE

    def decode(self, s, _w):
        """Return the Python representation of ``s`` (a ``str`` instance
        containing a JSON document).

        """
        # 332           0 RESUME                   0
        # 337           2 LOAD_FAST                0 (self)
        # 4 LOAD_METHOD              0 (raw_decode)
        # 26 LOAD_FAST                1 (s)
        # 28 PUSH_NULL
        # 30 LOAD_FAST                2 (_w)
        # 32 LOAD_FAST                1 (s)
        # 34 LOAD_CONST               1 (0)
        # 36 PRECALL                  2
        # 40 CALL                     2
        # 50 LOAD_METHOD              1 (end)
        # 72 PRECALL                  0
        # 76 CALL                     0
        # 86 KW_NAMES                 2
        # 88 PRECALL                  2
        # 92 CALL                     2
        # 102 UNPACK_SEQUENCE          2
        # 106 STORE_FAST               3 (obj)
        # 108 STORE_FAST               4 (end)
        # 338         110 PUSH_NULL
        # 112 LOAD_FAST                2 (_w)
        # 114 LOAD_FAST                1 (s)
        # 116 LOAD_FAST                4 (end)
        # 118 PRECALL                  2
        # 122 CALL                     2
        # 132 LOAD_METHOD              1 (end)
        # 154 PRECALL                  0
        # 158 CALL                     0
        # 168 STORE_FAST               4 (end)
        # 339         170 LOAD_FAST                4 (end)
        # 172 LOAD_GLOBAL              5 (NULL + len)
        # 184 LOAD_FAST                1 (s)
        # 186 PRECALL                  1
        # 190 CALL                     1
        # 200 COMPARE_OP               3 (!=)
        # 206 POP_JUMP_FORWARD_IF_FALSE    17 (to 242)
        # 340         208 LOAD_GLOBAL              7 (NULL + JSONDecodeError)
        # 220 LOAD_CONST               3 ('Extra data')
        # 222 LOAD_FAST                1 (s)
        # 224 LOAD_FAST                4 (end)
        # 226 PRECALL                  3
        # 230 CALL                     3
        # 240 RAISE_VARARGS            1
        # 341     >>  242 LOAD_FAST                3 (obj)
        # 244 RETURN_VALUE

    def raw_decode(self, s, idx):
        """Decode a JSON document from ``s`` (a ``str`` beginning with
        a JSON document) and return a 2-tuple of the Python
        representation and the index in ``s`` where the document ended.

        This can be used to decode a JSON document from a string that may
        have extraneous data at the end.

        """
        # 343           0 RESUME                   0
        # 352           2 NOP
        # 353           4 LOAD_FAST                0 (self)
        # 6 LOAD_METHOD              0 (scan_once)
        # 28 LOAD_FAST                1 (s)
        # 30 LOAD_FAST                2 (idx)
        # 32 PRECALL                  2
        # 36 CALL                     2
        # 46 UNPACK_SEQUENCE          2
        # 50 STORE_FAST               3 (obj)
        # 52 STORE_FAST               4 (end)
        # 54 JUMP_FORWARD            41 (to 138)
        # >>   56 PUSH_EXC_INFO
        # 354          58 LOAD_GLOBAL              2 (StopIteration)
        # 70 CHECK_EXC_MATCH
        # 72 POP_JUMP_FORWARD_IF_FALSE    28 (to 130)
        # 74 STORE_FAST               5 (err)
        # 355          76 LOAD_GLOBAL              5 (NULL + JSONDecodeError)
        # 88 LOAD_CONST               1 ('Expecting value')
        # 90 LOAD_FAST                1 (s)
        # 92 LOAD_FAST                5 (err)
        # 94 LOAD_ATTR                3 (value)
        # 104 PRECALL                  3
        # 108 CALL                     3
        # 118 LOAD_CONST               2 (None)
        # 120 RAISE_VARARGS            2
        # >>  122 LOAD_CONST               2 (None)
        # 124 STORE_FAST               5 (err)
        # 126 DELETE_FAST              5 (err)
        # 128 RERAISE                  1
        # 354     >>  130 RERAISE                  0
        # >>  132 COPY                     3
        # 134 POP_EXCEPT
        # 136 RERAISE                  1
        # 356     >>  138 LOAD_FAST                3 (obj)
        # 140 LOAD_FAST                4 (end)
        # 142 BUILD_TUPLE              2
        # 144 RETURN_VALUE
        # ExceptionTable:
        # 4 to 52 -> 56 [0]
        # 56 to 74 -> 132 [1] lasti
        # 76 to 120 -> 122 [1] lasti
        # 122 to 130 -> 132 [1] lasti

