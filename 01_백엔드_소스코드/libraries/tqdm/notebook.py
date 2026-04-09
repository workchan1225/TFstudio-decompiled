# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: tqdm\notebook.py

"""
IPython/Jupyter Notebook progressbar decorator for iterators.
Includes a default `range` iterator printing to `stderr`.

Usage:
>>> from tqdm.notebook import trange, tqdm
>>> for i in trange(10):
...     ...
"""

import re
import sys
from html import escape
from weakref import proxy
from std import tqdm
import ipywidgets
import warnings
from IPython.html.widgets import html
from IPython.html.widgets import HTML
from IPython.html.widgets import FloatProgress
from IPython.html.widgets import HBox
from ipywidgets import HTML
from ipywidgets import FloatProgress
from ipywidgets import HBox
from IPython.html.widgets import ContainerWidget
from IPython.html.widgets import FloatProgressWidget
from IPython.display import display

class TqdmHBox:
    """TqdmHBox"""
    def _json_(self, pretty):
        # 71           0 RESUME                   0
        # 72           2 LOAD_GLOBAL              1 (NULL + getattr)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_CONST               1 ('pbar')
        # 18 LOAD_CONST               0 (None)
        # 20 PRECALL                  3
        # 24 CALL                     3
        # 34 STORE_FAST               2 (pbar)
        # 73          36 LOAD_FAST                2 (pbar)
        # 38 POP_JUMP_FORWARD_IF_NOT_NONE     2 (to 44)
        # 74          40 BUILD_MAP                0
        # 42 RETURN_VALUE
        # 75     >>   44 LOAD_FAST                2 (pbar)
        # 46 LOAD_ATTR                1 (format_dict)
        # 56 STORE_FAST               3 (d)
        # 76          58 LOAD_FAST                1 (pretty)
        # 60 POP_JUMP_FORWARD_IF_NONE     6 (to 74)
        # 77          62 LOAD_FAST                1 (pretty)
        # 64 UNARY_NOT
        # 66 LOAD_FAST                3 (d)
        # 68 LOAD_CONST               2 ('ascii')
        # 70 STORE_SUBSCR
        # 78     >>   74 LOAD_FAST                3 (d)
        # 76 RETURN_VALUE

    def __repr__(self, pretty):
        # 0 COPY_FREE_VARS           1
        # 80           2 RESUME                   0
        # 81           4 LOAD_GLOBAL              1 (NULL + getattr)
        # 16 LOAD_FAST                0 (self)
        # 18 LOAD_CONST               1 ('pbar')
        # 20 LOAD_CONST               0 (None)
        # 22 PRECALL                  3
        # 26 CALL                     3
        # 36 STORE_FAST               2 (pbar)
        # 82          38 LOAD_FAST                2 (pbar)
        # 40 POP_JUMP_FORWARD_IF_NOT_NONE    32 (to 106)
        # 83          42 LOAD_GLOBAL              3 (NULL + super)
        # 54 PRECALL                  0
        # 58 CALL                     0
        # 68 LOAD_METHOD              2 (__repr__)
        # 90 PRECALL                  0
        # 94 CALL                     0
        # 104 RETURN_VALUE
        # 84     >>  106 PUSH_NULL
        # 108 LOAD_FAST                2 (pbar)
        # 110 LOAD_ATTR                3 (format_meter)
        # 120 LOAD_CONST               2 (())
        # 122 BUILD_MAP                0
        # 124 LOAD_FAST                0 (self)
        # 126 LOAD_METHOD              4 (_json_)
        # 148 LOAD_FAST                1 (pretty)
        # 150 PRECALL                  1
        # 154 CALL                     1
        # 164 DICT_MERGE               1
        # 166 CALL_FUNCTION_EX         1
        # 168 RETURN_VALUE

    def _repr_pretty_(self, pp):
        # 86           0 RESUME                   0
        # 87           2 LOAD_FAST                1 (pp)
        # 4 LOAD_METHOD              0 (text)
        # 26 LOAD_FAST                0 (self)
        # 28 LOAD_METHOD              1 (__repr__)
        # 50 LOAD_CONST               1 (True)
        # 52 PRECALL                  1
        # 56 CALL                     1
        # 66 PRECALL                  1
        # 70 CALL                     1
        # 80 POP_TOP
        # 82 LOAD_CONST               0 (None)
        # 84 RETURN_VALUE


class tqdm_notebook:
    """tqdm_notebook"""
    def status_printer(_, total, desc, ncols):
        """
        Manage the printing of an IPython/Jupyter Notebook progress bar widget.
        """
        # 94           0 RESUME                   0
        # 107           2 LOAD_GLOBAL              0 (IProgress)
        # 14 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 56)
        # 108          16 LOAD_GLOBAL              3 (NULL + ImportError)
        # 28 LOAD_GLOBAL              4 (WARN_NOIPYW)
        # 40 PRECALL                  1
        # 44 CALL                     1
        # 54 RAISE_VARARGS            1
        # 109     >>   56 LOAD_FAST                1 (total)
        # 58 POP_JUMP_FORWARD_IF_FALSE    18 (to 96)
        # 110          60 LOAD_GLOBAL              1 (NULL + IProgress)
        # 72 LOAD_CONST               2 (0)
        # 74 LOAD_FAST                1 (total)
        # 76 KW_NAMES                 3
        # 78 PRECALL                  2
        # 82 CALL                     2
        # 92 STORE_FAST               4 (pbar)
        # 94 JUMP_FORWARD            45 (to 186)
        # 112     >>   96 LOAD_GLOBAL              1 (NULL + IProgress)
        # 108 LOAD_CONST               2 (0)
        # 110 LOAD_CONST               4 (1)
        # 112 KW_NAMES                 3
        # 114 PRECALL                  2
        # 118 CALL                     2
        # 128 STORE_FAST               4 (pbar)
        # 113         130 LOAD_CONST               4 (1)
        # 132 LOAD_FAST                4 (pbar)
        # 134 STORE_ATTR               3 (value)
        # 114         144 LOAD_CONST               5 ('info')
        # 146 LOAD_FAST                4 (pbar)
        # 148 STORE_ATTR               4 (bar_style)
        # 115         158 LOAD_FAST                3 (ncols)
        # 160 POP_JUMP_FORWARD_IF_NOT_NONE    12 (to 186)
        # 116         162 LOAD_CONST               6 ('20px')
        # 164 LOAD_FAST                4 (pbar)
        # 166 LOAD_ATTR                5 (layout)
        # 176 STORE_ATTR               6 (width)
        # 118     >>  186 LOAD_GLOBAL             15 (NULL + HTML)
        # 198 PRECALL                  0
        # 202 CALL                     0
        # 212 STORE_FAST               5 (ltext)
        # 119         214 LOAD_GLOBAL             15 (NULL + HTML)
        # 226 PRECALL                  0
        # 230 CALL                     0
        # 240 STORE_FAST               6 (rtext)
        # 120         242 LOAD_FAST                2 (desc)
        # 244 POP_JUMP_FORWARD_IF_FALSE     7 (to 260)
        # 121         246 LOAD_FAST                2 (desc)
        # 248 LOAD_FAST                5 (ltext)
        # 250 STORE_ATTR               3 (value)
        # 122     >>  260 LOAD_GLOBAL             17 (NULL + TqdmHBox)
        # 272 LOAD_FAST                5 (ltext)
        # 274 LOAD_FAST                4 (pbar)
        # 276 LOAD_FAST                6 (rtext)
        # 278 BUILD_LIST               3
        # 280 KW_NAMES                 7
        # 282 PRECALL                  1
        # 286 CALL                     1
        # 296 STORE_FAST               7 (container)
        # 124         298 LOAD_FAST                3 (ncols)
        # 300 POP_JUMP_FORWARD_IF_NONE   105 (to 512)
        # 126         302 LOAD_GLOBAL             19 (NULL + str)
        # 314 LOAD_FAST                3 (ncols)
        # 316 PRECALL                  1
        # 320 CALL                     1
        # 330 STORE_FAST               3 (ncols)
        # 127         332 NOP
        # 128         334 LOAD_GLOBAL             21 (NULL + int)
        # 346 LOAD_FAST                3 (ncols)
        # 348 PRECALL                  1
        # 352 CALL                     1
        # 362 LOAD_CONST               2 (0)
        # 364 COMPARE_OP               4 (>)
        # 370 POP_JUMP_FORWARD_IF_FALSE     5 (to 382)
        # 129         372 LOAD_FAST                3 (ncols)
        # 374 LOAD_CONST               8 ('px')
        # 376 BINARY_OP               13 (+=)
        # 380 STORE_FAST               3 (ncols)
        # >>  382 JUMP_FORWARD            16 (to 416)
        # >>  384 PUSH_EXC_INFO
        # 130         386 LOAD_GLOBAL             22 (ValueError)
        # 398 CHECK_EXC_MATCH
        # 400 POP_JUMP_FORWARD_IF_FALSE     3 (to 408)
        # 402 POP_TOP
        # 131         404 POP_EXCEPT
        # 406 JUMP_FORWARD             4 (to 416)
        # 130     >>  408 RERAISE                  0
        # >>  410 COPY                     3
        # 412 POP_EXCEPT
        # 414 RERAISE                  1
        # 132     >>  416 LOAD_CONST               9 ('2')
        # 418 LOAD_FAST                4 (pbar)
        # 420 LOAD_ATTR                5 (layout)
        # 430 STORE_ATTR              12 (flex)
        # 133         440 LOAD_FAST                3 (ncols)
        # 442 LOAD_FAST                7 (container)
        # 444 LOAD_ATTR                5 (layout)
        # 454 STORE_ATTR               6 (width)
        # 134         464 LOAD_CONST              10 ('inline-flex')
        # 466 LOAD_FAST                7 (container)
        # 468 LOAD_ATTR                5 (layout)
        # 478 STORE_ATTR              13 (display)
        # 135         488 LOAD_CONST              11 ('row wrap')
        # 490 LOAD_FAST                7 (container)
        # 492 LOAD_ATTR                5 (layout)
        # 502 STORE_ATTR              14 (flex_flow)
        # 137     >>  512 LOAD_FAST                7 (container)
        # 514 RETURN_VALUE
        # ExceptionTable:
        # 334 to 380 -> 384 [0]
        # 384 to 402 -> 410 [1] lasti
        # 408 to 408 -> 410 [1] lasti

    def display(self, msg, pos, close, bar_style, check_delay):
        # 139           0 RESUME                   0
        # 149           2 LOAD_FAST                1 (msg)
        # 4 POP_JUMP_FORWARD_IF_TRUE    55 (to 116)
        # 6 LOAD_FAST                3 (close)
        # 8 POP_JUMP_FORWARD_IF_TRUE    53 (to 116)
        # 150          10 LOAD_FAST                0 (self)
        # 12 LOAD_ATTR                0 (format_dict)
        # 22 STORE_FAST               6 (d)
        # 152          24 LOAD_FAST                6 (d)
        # 26 LOAD_CONST               1 ('bar_format')
        # 28 BINARY_SUBSCR
        # 38 JUMP_IF_TRUE_OR_POP      1 (to 42)
        # 40 LOAD_CONST               2 ('{l_bar}<bar/>{r_bar}')
        # >>   42 LOAD_METHOD              1 (replace)
        # 153          64 LOAD_CONST               3 ('{bar}')
        # 66 LOAD_CONST               4 ('<bar/>')
        # 152          68 PRECALL                  2
        # 72 CALL                     2
        # 82 LOAD_FAST                6 (d)
        # 84 LOAD_CONST               1 ('bar_format')
        # 86 STORE_SUBSCR
        # 154          90 PUSH_NULL
        # 92 LOAD_FAST                0 (self)
        # 94 LOAD_ATTR                2 (format_meter)
        # 104 LOAD_CONST              17 (())
        # 106 BUILD_MAP                0
        # 108 LOAD_FAST                6 (d)
        # 110 DICT_MERGE               1
        # 112 CALL_FUNCTION_EX         1
        # 114 STORE_FAST               1 (msg)
        # 156     >>  116 LOAD_FAST                0 (self)
        # 118 LOAD_ATTR                3 (container)
        # 128 LOAD_ATTR                4 (children)
        # 138 UNPACK_SEQUENCE          3
        # 142 STORE_FAST               7 (ltext)
        # 144 STORE_FAST               8 (pbar)
        # 146 STORE_FAST               9 (rtext)
        # 157         148 LOAD_FAST                0 (self)
        # 150 LOAD_ATTR                5 (n)
        # 160 LOAD_FAST                8 (pbar)
        # 162 STORE_ATTR               6 (value)
        # 159         172 LOAD_FAST                1 (msg)
        # 174 POP_JUMP_FORWARD_IF_FALSE   105 (to 386)
        # 160         176 LOAD_FAST                1 (msg)
        # 178 LOAD_METHOD              1 (replace)
        # 200 LOAD_CONST               5 (' ')
        # 202 LOAD_CONST               6 ('\u2007')
        # 204 PRECALL                  2
        # 208 CALL                     2
        # 218 STORE_FAST               1 (msg)
        # 162         220 LOAD_CONST               4 ('<bar/>')
        # 222 LOAD_FAST                1 (msg)
        # 224 CONTAINS_OP              0
        # 226 POP_JUMP_FORWARD_IF_FALSE    46 (to 320)
        # 163         228 LOAD_GLOBAL             15 (NULL + map)
        # 240 LOAD_GLOBAL             16 (escape)
        # 252 LOAD_GLOBAL             19 (NULL + re)
        # 264 LOAD_ATTR               10 (split)
        # 274 LOAD_CONST               7 ('\\|?<bar/>\\|?')
        # 276 LOAD_FAST                1 (msg)
        # 278 LOAD_CONST               8 (1)
        # 280 KW_NAMES                 9
        # 282 PRECALL                  3
        # 286 CALL                     3
        # 296 PRECALL                  2
        # 300 CALL                     2
        # 310 UNPACK_SEQUENCE          2
        # 314 STORE_FAST              10 (left)
        # 316 STORE_FAST              11 (right)
        # 318 JUMP_FORWARD            17 (to 354)
        # 165     >>  320 LOAD_CONST              10 ('')
        # 322 LOAD_GLOBAL             17 (NULL + escape)
        # 334 LOAD_FAST                1 (msg)
        # 336 PRECALL                  1
        # 340 CALL                     1
        # 350 STORE_FAST              11 (right)
        # 352 STORE_FAST              10 (left)
        # 168     >>  354 LOAD_FAST               10 (left)
        # 356 LOAD_FAST                7 (ltext)
        # 358 STORE_ATTR               6 (value)
        # 170         368 LOAD_FAST               11 (right)
        # 370 POP_JUMP_FORWARD_IF_FALSE     7 (to 386)
        # 171         372 LOAD_FAST               11 (right)
        # 374 LOAD_FAST                9 (rtext)
        # 376 STORE_ATTR               6 (value)
        # 174     >>  386 LOAD_FAST                4 (bar_style)
        # 388 POP_JUMP_FORWARD_IF_FALSE    24 (to 438)
        # 177         390 LOAD_FAST                8 (pbar)
        # 392 LOAD_ATTR               11 (bar_style)
        # 402 LOAD_CONST              11 ('danger')
        # 404 COMPARE_OP               3 (!=)
        # 410 POP_JUMP_FORWARD_IF_TRUE     6 (to 424)
        # 412 LOAD_FAST                4 (bar_style)
        # 414 LOAD_CONST              12 ('success')
        # 416 COMPARE_OP               3 (!=)
        # 422 POP_JUMP_FORWARD_IF_FALSE     7 (to 438)
        # 178     >>  424 LOAD_FAST                4 (bar_style)
        # 426 LOAD_FAST                8 (pbar)
        # 428 STORE_ATTR              11 (bar_style)
        # 181     >>  438 LOAD_FAST                3 (close)
        # 440 POP_JUMP_FORWARD_IF_FALSE    83 (to 608)
        # 442 LOAD_FAST                8 (pbar)
        # 444 LOAD_ATTR               11 (bar_style)
        # 454 LOAD_CONST              11 ('danger')
        # 456 COMPARE_OP               3 (!=)
        # 462 POP_JUMP_FORWARD_IF_FALSE    72 (to 608)
        # 182         464 NOP
        # 183         466 LOAD_FAST                0 (self)
        # 468 LOAD_ATTR                3 (container)
        # 478 LOAD_METHOD             12 (close)
        # 500 PRECALL                  0
        # 504 CALL                     0
        # 514 POP_TOP
        # 516 JUMP_FORWARD            28 (to 574)
        # >>  518 PUSH_EXC_INFO
        # 184         520 LOAD_GLOBAL             26 (AttributeError)
        # 532 CHECK_EXC_MATCH
        # 534 POP_JUMP_FORWARD_IF_FALSE    15 (to 566)
        # 536 POP_TOP
        # 185         538 LOAD_CONST              13 (False)
        # 540 LOAD_FAST                0 (self)
        # 542 LOAD_ATTR                3 (container)
        # 552 STORE_ATTR              14 (visible)
        # 562 POP_EXCEPT
        # 564 JUMP_FORWARD             4 (to 574)
        # 184     >>  566 RERAISE                  0
        # >>  568 COPY                     3
        # 570 POP_EXCEPT
        # 572 RERAISE                  1
        # 186     >>  574 LOAD_CONST              14 ('hidden')
        # 576 LOAD_FAST                0 (self)
        # 578 LOAD_ATTR                3 (container)
        # 588 LOAD_ATTR               15 (layout)
        # 598 STORE_ATTR              16 (visibility)
        # 188     >>  608 LOAD_FAST                5 (check_delay)
        # 610 POP_JUMP_FORWARD_IF_FALSE    47 (to 706)
        # 612 LOAD_FAST                0 (self)
        # 614 LOAD_ATTR               17 (delay)
        # 624 LOAD_CONST              15 (0)
        # 626 COMPARE_OP               4 (>)
        # 632 POP_JUMP_FORWARD_IF_FALSE    38 (to 710)
        # 634 LOAD_FAST                0 (self)
        # 636 LOAD_ATTR               18 (displayed)
        # 646 POP_JUMP_FORWARD_IF_TRUE    33 (to 714)
        # 189         648 LOAD_GLOBAL             39 (NULL + display)
        # 660 LOAD_FAST                0 (self)
        # 662 LOAD_ATTR                3 (container)
        # 672 PRECALL                  1
        # 676 CALL                     1
        # 686 POP_TOP
        # 190         688 LOAD_CONST              16 (True)
        # 690 LOAD_FAST                0 (self)
        # 692 STORE_ATTR              18 (displayed)
        # 702 LOAD_CONST               0 (None)
        # 704 RETURN_VALUE
        # 188     >>  706 LOAD_CONST               0 (None)
        # 708 RETURN_VALUE
        # >>  710 LOAD_CONST               0 (None)
        # 712 RETURN_VALUE
        # >>  714 LOAD_CONST               0 (None)
        # 716 RETURN_VALUE
        # ExceptionTable:
        # 466 to 514 -> 518 [0]
        # 518 to 560 -> 568 [1] lasti
        # 566 to 566 -> 568 [1] lasti

    def colour(self):
        # 192           0 RESUME                   0
        # 194           2 LOAD_GLOBAL              1 (NULL + hasattr)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_CONST               1 ('container')
        # 18 PRECALL                  2
        # 22 CALL                     2
        # 32 POP_JUMP_FORWARD_IF_FALSE    28 (to 90)
        # 195          34 LOAD_FAST                0 (self)
        # 36 LOAD_ATTR                1 (container)
        # 46 LOAD_ATTR                2 (children)
        # 56 LOAD_CONST               2 (-2)
        # 58 BINARY_SUBSCR
        # 68 LOAD_ATTR                3 (style)
        # 78 LOAD_ATTR                4 (bar_color)
        # 88 RETURN_VALUE
        # 194     >>   90 LOAD_CONST               0 (None)
        # 92 RETURN_VALUE

    def colour(self, bar_color):
        # 197           0 RESUME                   0
        # 199           2 LOAD_GLOBAL              1 (NULL + hasattr)
        # 14 LOAD_FAST                0 (self)
        # 16 LOAD_CONST               1 ('container')
        # 18 PRECALL                  2
        # 22 CALL                     2
        # 32 POP_JUMP_FORWARD_IF_FALSE    30 (to 94)
        # 200          34 LOAD_FAST                1 (bar_color)
        # 36 LOAD_FAST                0 (self)
        # 38 LOAD_ATTR                1 (container)
        # 48 LOAD_ATTR                2 (children)
        # 58 LOAD_CONST               2 (-2)
        # 60 BINARY_SUBSCR
        # 70 LOAD_ATTR                3 (style)
        # 80 STORE_ATTR               4 (bar_color)
        # 90 LOAD_CONST               0 (None)
        # 92 RETURN_VALUE
        # 199     >>   94 LOAD_CONST               0 (None)
        # 96 RETURN_VALUE

    def __init__(self):
        """
        Supports the usual `tqdm.tqdm` parameters as well as those listed below.

        Parameters
        ----------
        display  : Whether to call `display(self.container)` immediately
            [default: True].
        """
        # 0 COPY_FREE_VARS           1
        # 202           2 RESUME                   0
        # 211           4 LOAD_FAST                2 (kwargs)
        # 6 LOAD_METHOD              0 (copy)
        # 28 PRECALL                  0
        # 32 CALL                     0
        # 42 STORE_FAST               2 (kwargs)
        # 213          44 LOAD_FAST                2 (kwargs)
        # 46 LOAD_METHOD              1 (get)
        # 68 LOAD_CONST               1 ('file')
        # 70 LOAD_GLOBAL              4 (sys)
        # 82 LOAD_ATTR                3 (stderr)
        # 92 PRECALL                  2
        # 96 CALL                     2
        # 106 STORE_FAST               3 (file_kwarg)
        # 214         108 LOAD_FAST                3 (file_kwarg)
        # 110 LOAD_GLOBAL              4 (sys)
        # 122 LOAD_ATTR                3 (stderr)
        # 132 IS_OP                    0
        # 134 POP_JUMP_FORWARD_IF_TRUE     2 (to 140)
        # 136 LOAD_FAST                3 (file_kwarg)
        # 138 POP_JUMP_FORWARD_IF_NOT_NONE    15 (to 170)
        # 215     >>  140 LOAD_GLOBAL              4 (sys)
        # 152 LOAD_ATTR                4 (stdout)
        # 162 LOAD_FAST                2 (kwargs)
        # 164 LOAD_CONST               1 ('file')
        # 166 STORE_SUBSCR
        # 218     >>  170 LOAD_CONST               3 (True)
        # 172 LOAD_FAST                2 (kwargs)
        # 174 LOAD_CONST               4 ('gui')
        # 176 STORE_SUBSCR
        # 220         180 LOAD_GLOBAL             11 (NULL + bool)
        # 192 LOAD_FAST                2 (kwargs)
        # 194 LOAD_METHOD              1 (get)
        # 216 LOAD_CONST               5 ('disable')
        # 218 LOAD_CONST               6 (False)
        # 220 PRECALL                  2
        # 224 CALL                     2
        # 234 PRECALL                  1
        # 238 CALL                     1
        # 248 LOAD_FAST                2 (kwargs)
        # 250 LOAD_CONST               5 ('disable')
        # 252 STORE_SUBSCR
        # 221         256 LOAD_FAST                2 (kwargs)
        # 258 LOAD_METHOD              6 (pop)
        # 280 LOAD_CONST               7 ('colour')
        # 282 LOAD_CONST               2 (None)
        # 284 PRECALL                  2
        # 288 CALL                     2
        # 298 STORE_FAST               4 (colour)
        # 222         300 LOAD_FAST                2 (kwargs)
        # 302 LOAD_METHOD              6 (pop)
        # 324 LOAD_CONST               8 ('display')
        # 326 LOAD_CONST               3 (True)
        # 328 PRECALL                  2
        # 332 CALL                     2
        # 342 STORE_FAST               5 (display_here)
        # 223         344 PUSH_NULL
        # 346 LOAD_GLOBAL             15 (NULL + super)
        # 358 PRECALL                  0
        # 362 CALL                     0
        # 372 LOAD_ATTR                8 (__init__)
        # 382 LOAD_FAST                1 (args)
        # 384 BUILD_MAP                0
        # 386 LOAD_FAST                2 (kwargs)
        # 388 DICT_MERGE               1
        # 390 CALL_FUNCTION_EX         1
        # 392 POP_TOP
        # 224         394 LOAD_FAST                0 (self)
        # 396 LOAD_ATTR                9 (disable)
        # 406 POP_JUMP_FORWARD_IF_TRUE     8 (to 424)
        # 408 LOAD_FAST                2 (kwargs)
        # 410 LOAD_CONST               4 ('gui')
        # 412 BINARY_SUBSCR
        # 422 POP_JUMP_FORWARD_IF_TRUE    10 (to 444)
        # 225     >>  424 LOAD_CONST               9 (<code object <lambda> at 0x000001EBD7F2FE70, file "tqdm\notebook.py", line 225>)
        # 426 MAKE_FUNCTION            0
        # 428 LOAD_FAST                0 (self)
        # 430 STORE_ATTR              10 (disp)
        # 226         440 LOAD_CONST               2 (None)
        # 442 RETURN_VALUE
        # 229     >>  444 LOAD_FAST                0 (self)
        # 446 LOAD_ATTR               11 (dynamic_ncols)
        # 456 POP_JUMP_FORWARD_IF_FALSE     2 (to 462)
        # 458 LOAD_CONST              10 ('100%')
        # 460 JUMP_FORWARD            21 (to 504)
        # >>  462 LOAD_FAST                2 (kwargs)
        # 464 LOAD_METHOD              1 (get)
        # 486 LOAD_CONST              11 ('ncols')
        # 488 LOAD_CONST               2 (None)
        # 490 PRECALL                  2
        # 494 CALL                     2
        # >>  504 LOAD_FAST                0 (self)
        # 506 STORE_ATTR              12 (ncols)
        # 232         516 LOAD_FAST                0 (self)
        # 518 LOAD_ATTR               13 (unit_scale)
        # 528 LOAD_CONST               3 (True)
        # 530 IS_OP                    0
        # 532 POP_JUMP_FORWARD_IF_FALSE     2 (to 538)
        # 534 LOAD_CONST              12 (1)
        # 536 JUMP_FORWARD             8 (to 554)
        # >>  538 LOAD_FAST                0 (self)
        # 540 LOAD_ATTR               13 (unit_scale)
        # 550 JUMP_IF_TRUE_OR_POP      1 (to 554)
        # 552 LOAD_CONST              12 (1)
        # >>  554 STORE_FAST               6 (unit_scale)
        # 233         556 LOAD_FAST                0 (self)
        # 558 LOAD_ATTR               14 (total)
        # 568 POP_JUMP_FORWARD_IF_FALSE    10 (to 590)
        # 570 LOAD_FAST                0 (self)
        # 572 LOAD_ATTR               14 (total)
        # 582 LOAD_FAST                6 (unit_scale)
        # 584 BINARY_OP                5 (*)
        # 588 JUMP_FORWARD             6 (to 602)
        # >>  590 LOAD_FAST                0 (self)
        # 592 LOAD_ATTR               14 (total)
        # >>  602 STORE_FAST               7 (total)
        # 234         604 LOAD_FAST                0 (self)
        # 606 LOAD_METHOD             15 (status_printer)
        # 628 LOAD_FAST                0 (self)
        # 630 LOAD_ATTR               16 (fp)
        # 640 LOAD_FAST                7 (total)
        # 642 LOAD_FAST                0 (self)
        # 644 LOAD_ATTR               17 (desc)
        # 654 LOAD_FAST                0 (self)
        # 656 LOAD_ATTR               12 (ncols)
        # 666 PRECALL                  4
        # 670 CALL                     4
        # 680 LOAD_FAST                0 (self)
        # 682 STORE_ATTR              18 (container)
        # 235         692 LOAD_GLOBAL             39 (NULL + proxy)
        # 704 LOAD_FAST                0 (self)
        # 706 PRECALL                  1
        # 710 CALL                     1
        # 720 LOAD_FAST                0 (self)
        # 722 LOAD_ATTR               18 (container)
        # 732 STORE_ATTR              20 (pbar)
        # 236         742 LOAD_CONST               6 (False)
        # 744 LOAD_FAST                0 (self)
        # 746 STORE_ATTR              21 (displayed)
        # 237         756 LOAD_FAST                5 (display_here)
        # 758 POP_JUMP_FORWARD_IF_FALSE    38 (to 836)
        # 760 LOAD_FAST                0 (self)
        # 762 LOAD_ATTR               22 (delay)
        # 772 LOAD_CONST              13 (0)
        # 774 COMPARE_OP               1 (<=)
        # 780 POP_JUMP_FORWARD_IF_FALSE    27 (to 836)
        # 238         782 LOAD_GLOBAL             47 (NULL + display)
        # 794 LOAD_FAST                0 (self)
        # 796 LOAD_ATTR               18 (container)
        # 806 PRECALL                  1
        # 810 CALL                     1
        # 820 POP_TOP
        # 239         822 LOAD_CONST               3 (True)
        # 824 LOAD_FAST                0 (self)
        # 826 STORE_ATTR              21 (displayed)
        # 240     >>  836 LOAD_FAST                0 (self)
        # 838 LOAD_ATTR               23 (display)
        # 848 LOAD_FAST                0 (self)
        # 850 STORE_ATTR              10 (disp)
        # 241         860 LOAD_FAST                4 (colour)
        # 862 LOAD_FAST                0 (self)
        # 864 STORE_ATTR              24 (colour)
        # 244         874 LOAD_FAST                0 (self)
        # 876 LOAD_ATTR                9 (disable)
        # 886 POP_JUMP_FORWARD_IF_TRUE    24 (to 936)
        # 245         888 LOAD_FAST                0 (self)
        # 890 LOAD_METHOD             23 (display)
        # 912 LOAD_CONST               6 (False)
        # 914 KW_NAMES                14
        # 916 PRECALL                  1
        # 920 CALL                     1
        # 930 POP_TOP
        # 932 LOAD_CONST               2 (None)
        # 934 RETURN_VALUE
        # 244     >>  936 LOAD_CONST               2 (None)
        # 938 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7F2FE70, file "tqdm\notebook.py", line 225>:
        # 225           0 RESUME                   0
        # 2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def __iter__(self):
        # 0 COPY_FREE_VARS           1
        # 247           2 RETURN_GENERATOR
        # 4 POP_TOP
        # 6 RESUME                   0
        # 248           8 NOP
        # 249          10 LOAD_GLOBAL              1 (NULL + super)
        # 22 PRECALL                  0
        # 26 CALL                     0
        # 36 LOAD_METHOD              1 (__iter__)
        # 58 PRECALL                  0
        # 62 CALL                     0
        # 72 STORE_FAST               1 (it)
        # 250          74 LOAD_FAST                1 (it)
        # 76 GET_ITER
        # >>   78 FOR_ITER                 6 (to 92)
        # 80 STORE_FAST               2 (obj)
        # 252          82 LOAD_FAST                2 (obj)
        # 84 YIELD_VALUE
        # 86 RESUME                   1
        # 88 POP_TOP
        # 90 JUMP_BACKWARD            7 (to 78)
        # 250     >>   92 LOAD_CONST               0 (None)
        # 94 RETURN_VALUE
        # >>   96 PUSH_EXC_INFO
        # 254          98 POP_TOP
        # 255         100 LOAD_FAST                0 (self)
        # 102 LOAD_METHOD              2 (disp)
        # 124 LOAD_CONST               1 ('danger')
        # 126 KW_NAMES                 2
        # 128 PRECALL                  1
        # 132 CALL                     1
        # 142 POP_TOP
        # 256         144 RAISE_VARARGS            0
        # >>  146 COPY                     3
        # 148 POP_EXCEPT
        # 150 RERAISE                  1
        # ExceptionTable:
        # 10 to 90 -> 96 [0]
        # 96 to 144 -> 146 [1] lasti

    def update(self, n):
        # 0 COPY_FREE_VARS           1
        # 260           2 RESUME                   0
        # 261           4 NOP
        # 262           6 LOAD_GLOBAL              1 (NULL + super)
        # 18 PRECALL                  0
        # 22 CALL                     0
        # 32 LOAD_METHOD              1 (update)
        # 54 LOAD_FAST                1 (n)
        # 56 KW_NAMES                 1
        # 58 PRECALL                  1
        # 62 CALL                     1
        # 72 RETURN_VALUE
        # >>   74 PUSH_EXC_INFO
        # 264          76 POP_TOP
        # 267          78 LOAD_FAST                0 (self)
        # 80 LOAD_METHOD              2 (disp)
        # 102 LOAD_CONST               2 ('danger')
        # 104 KW_NAMES                 3
        # 106 PRECALL                  1
        # 110 CALL                     1
        # 120 POP_TOP
        # 268         122 RAISE_VARARGS            0
        # >>  124 COPY                     3
        # 126 POP_EXCEPT
        # 128 RERAISE                  1
        # ExceptionTable:
        # 6 to 70 -> 74 [0]
        # 74 to 122 -> 124 [1] lasti

    def close(self):
        # 0 COPY_FREE_VARS           1
        # 272           2 RESUME                   0
        # 273           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (disable)
        # 16 POP_JUMP_FORWARD_IF_FALSE     2 (to 22)
        # 274          18 LOAD_CONST               0 (None)
        # 20 RETURN_VALUE
        # 275     >>   22 LOAD_GLOBAL              3 (NULL + super)
        # 34 PRECALL                  0
        # 38 CALL                     0
        # 48 LOAD_METHOD              2 (close)
        # 70 PRECALL                  0
        # 74 CALL                     0
        # 84 POP_TOP
        # 278          86 LOAD_FAST                0 (self)
        # 88 LOAD_ATTR                3 (total)
        # 98 POP_JUMP_FORWARD_IF_FALSE    41 (to 182)
        # 100 LOAD_FAST                0 (self)
        # 102 LOAD_ATTR                4 (n)
        # 112 LOAD_FAST                0 (self)
        # 114 LOAD_ATTR                3 (total)
        # 124 COMPARE_OP               0 (<)
        # 130 POP_JUMP_FORWARD_IF_FALSE    25 (to 182)
        # 279         132 LOAD_FAST                0 (self)
        # 134 LOAD_METHOD              5 (disp)
        # 156 LOAD_CONST               1 ('danger')
        # 158 LOAD_CONST               2 (False)
        # 160 KW_NAMES                 3
        # 162 PRECALL                  2
        # 166 CALL                     2
        # 176 POP_TOP
        # 178 LOAD_CONST               0 (None)
        # 180 RETURN_VALUE
        # 281     >>  182 LOAD_FAST                0 (self)
        # 184 LOAD_ATTR                6 (leave)
        # 194 POP_JUMP_FORWARD_IF_FALSE    25 (to 246)
        # 282         196 LOAD_FAST                0 (self)
        # 198 LOAD_METHOD              5 (disp)
        # 220 LOAD_CONST               4 ('success')
        # 222 LOAD_CONST               2 (False)
        # 224 KW_NAMES                 3
        # 226 PRECALL                  2
        # 230 CALL                     2
        # 240 POP_TOP
        # 242 LOAD_CONST               0 (None)
        # 244 RETURN_VALUE
        # 284     >>  246 LOAD_FAST                0 (self)
        # 248 LOAD_METHOD              5 (disp)
        # 270 LOAD_CONST               5 (True)
        # 272 LOAD_CONST               2 (False)
        # 274 KW_NAMES                 6
        # 276 PRECALL                  2
        # 280 CALL                     2
        # 290 POP_TOP
        # 292 LOAD_CONST               0 (None)
        # 294 RETURN_VALUE

    def clear(self):
        # 286           0 RESUME                   0
        # 287           2 LOAD_CONST               0 (None)
        # 4 RETURN_VALUE

    def reset(self, total):
        """
        Resets to 0 iterations for repeated use.

        Consider combining with `leave=True`.

        Parameters
        ----------
        total  : int or float, optional. Total to use for the new bar.
        """
        # 0 COPY_FREE_VARS           1
        # 289           2 RESUME                   0
        # 299           4 LOAD_FAST                0 (self)
        # 6 LOAD_ATTR                0 (disable)
        # 16 POP_JUMP_FORWARD_IF_FALSE    34 (to 86)
        # 300          18 LOAD_GLOBAL              3 (NULL + super)
        # 30 PRECALL                  0
        # 34 CALL                     0
        # 44 LOAD_METHOD              2 (reset)
        # 66 LOAD_FAST                1 (total)
        # 68 KW_NAMES                 1
        # 70 PRECALL                  1
        # 74 CALL                     1
        # 84 RETURN_VALUE
        # 301     >>   86 LOAD_FAST                0 (self)
        # 88 LOAD_ATTR                3 (container)
        # 98 LOAD_ATTR                4 (children)
        # 108 UNPACK_SEQUENCE          3
        # 112 STORE_FAST               2 (_)
        # 114 STORE_FAST               3 (pbar)
        # 116 STORE_FAST               2 (_)
        # 302         118 LOAD_CONST               2 ('')
        # 120 LOAD_FAST                3 (pbar)
        # 122 STORE_ATTR               5 (bar_style)
        # 303         132 LOAD_FAST                1 (total)
        # 134 POP_JUMP_FORWARD_IF_NONE    33 (to 202)
        # 304         136 LOAD_FAST                1 (total)
        # 138 LOAD_FAST                3 (pbar)
        # 140 STORE_ATTR               6 (max)
        # 305         150 LOAD_FAST                0 (self)
        # 152 LOAD_ATTR                7 (total)
        # 162 POP_JUMP_FORWARD_IF_TRUE    19 (to 202)
        # 164 LOAD_FAST                0 (self)
        # 166 LOAD_ATTR                8 (ncols)
        # 176 POP_JUMP_FORWARD_IF_NOT_NONE    12 (to 202)
        # 306         178 LOAD_CONST               3 (None)
        # 180 LOAD_FAST                3 (pbar)
        # 182 LOAD_ATTR                9 (layout)
        # 192 STORE_ATTR              10 (width)
        # 307     >>  202 LOAD_GLOBAL              3 (NULL + super)
        # 214 PRECALL                  0
        # 218 CALL                     0
        # 228 LOAD_METHOD              2 (reset)
        # 250 LOAD_FAST                1 (total)
        # 252 KW_NAMES                 1
        # 254 PRECALL                  1
        # 258 CALL                     1
        # 268 RETURN_VALUE


def tnrange():
    """Shortcut for `tqdm.notebook.tqdm(range(*args), **kwargs)`."""
    # 310           0 RESUME                   0
    # 312           2 LOAD_GLOBAL              1 (NULL + tqdm_notebook)
    # 14 LOAD_GLOBAL              3 (NULL + range)
    # 26 LOAD_FAST                0 (args)
    # 28 CALL_FUNCTION_EX         0
    # 30 BUILD_TUPLE              1
    # 32 BUILD_MAP                0
    # 34 LOAD_FAST                1 (kwargs)
    # 36 DICT_MERGE               1
    # 38 CALL_FUNCTION_EX         1
    # 40 RETURN_VALUE
