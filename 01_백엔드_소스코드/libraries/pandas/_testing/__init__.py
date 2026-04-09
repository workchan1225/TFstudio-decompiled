# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: pandas\_testing\__init__.py

from __future__ import annotations
from decimal import Decimal
import operator
import os
from sys import byteorder
from typing import TYPE_CHECKING
import numpy
from pandas._config import using_string_dtype
from pandas._config.localization import can_set_locale
from pandas.compat import HAS_PYARROW
import pandas
from pandas import ArrowDtype
from pandas._testing._io import round_trip_pathlib
from pandas._testing._warnings import assert_produces_warning
from pandas._testing.asserters import assert_almost_equal
from pandas._testing.compat import get_dtype
from pandas._testing.contexts import decompress_file
from pandas.core.arrays import ArrowExtensionArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.construction import extract_array
from collections.abc import Callable
from pandas._typing import Dtype
import pyarrow

def <listcomp>(.0):
    # 165           0 RESUME                   0
    # 2 BUILD_LIST               0
    # 4 LOAD_FAST                0 (.0)
    # >>    6 FOR_ITER                19 (to 46)
    # 167           8 STORE_FAST               1 (cls)
    # 168          10 LOAD_CONST               0 (('Y', 'M', 'W', 'D', 'h', 'm', 's', 'ms', 'us', 'ns', 'ps', 'fs', 'as'))
    # 165          12 GET_ITER
    # >>   14 FOR_ITER                14 (to 44)
    # 168          16 STORE_FAST               2 (unit)
    # 166          18 PUSH_NULL
    # 20 LOAD_FAST                1 (cls)
    # 22 LOAD_CONST               1 ('NaT')
    # 24 LOAD_FAST                2 (unit)
    # 26 PRECALL                  2
    # 30 CALL                     2
    # 165          40 LIST_APPEND              3
    # 42 JUMP_BACKWARD           15 (to 14)
    # >>   44 JUMP_BACKWARD           20 (to 6)
    # >>   46 RETURN_VALUE

def box_expected(expected, box_cls, transpose):
    """
    Helper function to wrap the expected output of a test in a given box_class.

    Parameters
    ----------
    expected : np.ndarray, Index, Series
    box_cls : {Index, Series, DataFrame}

    Returns
    -------
    subclass of box_cls
    """
    # 272           0 RESUME                   0
    # 285           2 LOAD_FAST                1 (box_cls)
    # 4 LOAD_GLOBAL              0 (pd)
    # 16 LOAD_ATTR                1 (array)
    # 26 IS_OP                    0
    # 28 POP_JUMP_FORWARD_IF_FALSE    83 (to 196)
    # 286          30 LOAD_GLOBAL              5 (NULL + isinstance)
    # 42 LOAD_FAST                0 (expected)
    # 44 LOAD_GLOBAL              6 (RangeIndex)
    # 56 PRECALL                  2
    # 60 CALL                     2
    # 70 POP_JUMP_FORWARD_IF_FALSE    39 (to 150)
    # 288          72 LOAD_GLOBAL              9 (NULL + NumpyExtensionArray)
    # 84 LOAD_GLOBAL             11 (NULL + np)
    # 96 LOAD_ATTR                6 (asarray)
    # 106 LOAD_FAST                0 (expected)
    # 108 LOAD_ATTR                7 (_values)
    # 118 PRECALL                  1
    # 122 CALL                     1
    # 132 PRECALL                  1
    # 136 CALL                     1
    # 146 STORE_FAST               0 (expected)
    # 148 JUMP_FORWARD           242 (to 634)
    # 290     >>  150 LOAD_GLOBAL              1 (NULL + pd)
    # 162 LOAD_ATTR                1 (array)
    # 172 LOAD_FAST                0 (expected)
    # 174 LOAD_CONST               1 (False)
    # 176 KW_NAMES                 2
    # 178 PRECALL                  2
    # 182 CALL                     2
    # 192 STORE_FAST               0 (expected)
    # 194 JUMP_FORWARD           219 (to 634)
    # 291     >>  196 LOAD_FAST                1 (box_cls)
    # 198 LOAD_GLOBAL             16 (Index)
    # 210 IS_OP                    0
    # 212 POP_JUMP_FORWARD_IF_FALSE    18 (to 250)
    # 292         214 LOAD_GLOBAL             17 (NULL + Index)
    # 226 LOAD_FAST                0 (expected)
    # 228 LOAD_CONST               1 (False)
    # 230 KW_NAMES                 2
    # 232 PRECALL                  2
    # 236 CALL                     2
    # 246 STORE_FAST               0 (expected)
    # 248 JUMP_FORWARD           192 (to 634)
    # 293     >>  250 LOAD_FAST                1 (box_cls)
    # 252 LOAD_GLOBAL             18 (Series)
    # 264 IS_OP                    0
    # 266 POP_JUMP_FORWARD_IF_FALSE    16 (to 300)
    # 294         268 LOAD_GLOBAL             19 (NULL + Series)
    # 280 LOAD_FAST                0 (expected)
    # 282 PRECALL                  1
    # 286 CALL                     1
    # 296 STORE_FAST               0 (expected)
    # 298 JUMP_FORWARD           167 (to 634)
    # 295     >>  300 LOAD_FAST                1 (box_cls)
    # 302 LOAD_GLOBAL             20 (DataFrame)
    # 314 IS_OP                    0
    # 316 POP_JUMP_FORWARD_IF_FALSE    69 (to 456)
    # 296         318 LOAD_GLOBAL             19 (NULL + Series)
    # 330 LOAD_FAST                0 (expected)
    # 332 PRECALL                  1
    # 336 CALL                     1
    # 346 LOAD_METHOD             11 (to_frame)
    # 368 PRECALL                  0
    # 372 CALL                     0
    # 382 STORE_FAST               0 (expected)
    # 297         384 LOAD_FAST                2 (transpose)
    # 386 POP_JUMP_FORWARD_IF_FALSE    33 (to 454)
    # 302         388 LOAD_FAST                0 (expected)
    # 390 LOAD_ATTR               12 (T)
    # 400 STORE_FAST               0 (expected)
    # 303         402 LOAD_GLOBAL              1 (NULL + pd)
    # 414 LOAD_ATTR               13 (concat)
    # 424 LOAD_FAST                0 (expected)
    # 426 BUILD_LIST               1
    # 428 LOAD_CONST               3 (2)
    # 430 BINARY_OP                5 (*)
    # 434 LOAD_CONST               4 (True)
    # 436 KW_NAMES                 5
    # 438 PRECALL                  2
    # 442 CALL                     2
    # 452 STORE_FAST               0 (expected)
    # >>  454 JUMP_FORWARD            89 (to 634)
    # 304     >>  456 LOAD_FAST                1 (box_cls)
    # 458 LOAD_GLOBAL             10 (np)
    # 470 LOAD_ATTR               14 (ndarray)
    # 480 IS_OP                    0
    # 482 POP_JUMP_FORWARD_IF_TRUE    14 (to 512)
    # 484 LOAD_FAST                1 (box_cls)
    # 486 LOAD_GLOBAL             10 (np)
    # 498 LOAD_ATTR                1 (array)
    # 508 IS_OP                    0
    # 510 POP_JUMP_FORWARD_IF_FALSE    21 (to 554)
    # 305     >>  512 LOAD_GLOBAL             11 (NULL + np)
    # 524 LOAD_ATTR                1 (array)
    # 534 LOAD_FAST                0 (expected)
    # 536 PRECALL                  1
    # 540 CALL                     1
    # 550 STORE_FAST               0 (expected)
    # 552 JUMP_FORWARD            40 (to 634)
    # 306     >>  554 LOAD_FAST                1 (box_cls)
    # 556 LOAD_GLOBAL             30 (to_array)
    # 568 IS_OP                    0
    # 570 POP_JUMP_FORWARD_IF_FALSE    16 (to 604)
    # 307         572 LOAD_GLOBAL             31 (NULL + to_array)
    # 584 LOAD_FAST                0 (expected)
    # 586 PRECALL                  1
    # 590 CALL                     1
    # 600 STORE_FAST               0 (expected)
    # 602 JUMP_FORWARD            15 (to 634)
    # 309     >>  604 LOAD_GLOBAL             33 (NULL + NotImplementedError)
    # 616 LOAD_FAST                1 (box_cls)
    # 618 PRECALL                  1
    # 622 CALL                     1
    # 632 RAISE_VARARGS            1
    # 310     >>  634 LOAD_FAST                0 (expected)
    # 636 RETURN_VALUE

def to_array(obj):
    """
    Similar to pd.array, but does not cast numpy dtypes to nullable dtypes.
    """
    # 313           0 RESUME                   0
    # 318           2 LOAD_GLOBAL              1 (NULL + getattr)
    # 14 LOAD_FAST                0 (obj)
    # 16 LOAD_CONST               1 ('dtype')
    # 18 LOAD_CONST               2 (None)
    # 20 PRECALL                  3
    # 24 CALL                     3
    # 34 STORE_FAST               1 (dtype)
    # 320          36 LOAD_FAST                1 (dtype)
    # 38 POP_JUMP_FORWARD_IF_NOT_NONE    20 (to 80)
    # 321          40 LOAD_GLOBAL              3 (NULL + np)
    # 52 LOAD_ATTR                2 (asarray)
    # 62 LOAD_FAST                0 (obj)
    # 64 PRECALL                  1
    # 68 CALL                     1
    # 78 RETURN_VALUE
    # 323     >>   80 LOAD_GLOBAL              7 (NULL + extract_array)
    # 92 LOAD_FAST                0 (obj)
    # 94 LOAD_CONST               3 (True)
    # 96 KW_NAMES                 4
    # 98 PRECALL                  2
    # 102 CALL                     2
    # 112 RETURN_VALUE

class SubclassedSeries:
    """SubclassedSeries"""
    def _constructor(self):
        # 329           0 RESUME                   0
        # 336           2 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7E40F10, file "pandas\_testing\__init__.py", line 336>)
        # 4 MAKE_FUNCTION            0
        # 6 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E40F10, file "pandas\_testing\__init__.py", line 336>:
        # 336           0 RESUME                   0
        # 2 LOAD_GLOBAL              1 (NULL + SubclassedSeries)
        # 14 LOAD_FAST                0 (args)
        # 16 BUILD_MAP                0
        # 18 LOAD_FAST                1 (kwargs)
        # 20 DICT_MERGE               1
        # 22 CALL_FUNCTION_EX         1
        # 24 RETURN_VALUE

    def _constructor_expanddim(self):
        # 338           0 RESUME                   0
        # 340           2 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7E40FF0, file "pandas\_testing\__init__.py", line 340>)
        # 4 MAKE_FUNCTION            0
        # 6 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E40FF0, file "pandas\_testing\__init__.py", line 340>:
        # 340           0 RESUME                   0
        # 2 LOAD_GLOBAL              1 (NULL + SubclassedDataFrame)
        # 14 LOAD_FAST                0 (args)
        # 16 BUILD_MAP                0
        # 18 LOAD_FAST                1 (kwargs)
        # 20 DICT_MERGE               1
        # 22 CALL_FUNCTION_EX         1
        # 24 RETURN_VALUE


class SubclassedDataFrame:
    """SubclassedDataFrame"""
    def _constructor(self):
        # 346           0 RESUME                   0
        # 348           2 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7E410D0, file "pandas\_testing\__init__.py", line 348>)
        # 4 MAKE_FUNCTION            0
        # 6 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E410D0, file "pandas\_testing\__init__.py", line 348>:
        # 348           0 RESUME                   0
        # 2 LOAD_GLOBAL              1 (NULL + SubclassedDataFrame)
        # 14 LOAD_FAST                0 (args)
        # 16 BUILD_MAP                0
        # 18 LOAD_FAST                1 (kwargs)
        # 20 DICT_MERGE               1
        # 22 CALL_FUNCTION_EX         1
        # 24 RETURN_VALUE

    def _constructor_sliced(self):
        # 351           0 RESUME                   0
        # 353           2 LOAD_CONST               1 (<code object <lambda> at 0x000001EBD7E411B0, file "pandas\_testing\__init__.py", line 353>)
        # 4 MAKE_FUNCTION            0
        # 6 RETURN_VALUE
        # Disassembly of <code object <lambda> at 0x000001EBD7E411B0, file "pandas\_testing\__init__.py", line 353>:
        # 353           0 RESUME                   0
        # 2 LOAD_GLOBAL              1 (NULL + SubclassedSeries)
        # 14 LOAD_FAST                0 (args)
        # 16 BUILD_MAP                0
        # 18 LOAD_FAST                1 (kwargs)
        # 20 DICT_MERGE               1
        # 22 CALL_FUNCTION_EX         1
        # 24 RETURN_VALUE


def convert_rows_list_to_csv_str(rows_list):
    """
    Convert list of CSV rows to single CSV-formatted string for current OS.

    This method is used for creating expected value of to_csv() method.

    Parameters
    ----------
    rows_list : List[str]
        Each element represents the row of csv.

    Returns
    -------
    str
        Expected output of to_csv() in current OS.
    """
    # 356           0 RESUME                   0
    # 372           2 LOAD_GLOBAL              0 (os)
    # 14 LOAD_ATTR                1 (linesep)
    # 24 STORE_FAST               1 (sep)
    # 373          26 LOAD_FAST                1 (sep)
    # 28 LOAD_METHOD              2 (join)
    # 50 LOAD_FAST                0 (rows_list)
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 LOAD_FAST                1 (sep)
    # 68 BINARY_OP                0 (+)
    # 72 RETURN_VALUE

def external_error_raised(expected_exception):
    """
    Helper function to mark pytest.raises that have an external error message.

    Parameters
    ----------
    expected_exception : Exception
        Expected error to raise.

    Returns
    -------
    Callable
        Regular `pytest.raises` function with `match` equal to `None`.
    """
    # 376           0 RESUME                   0
    # 390           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (None)
    # 6 IMPORT_NAME              0 (pytest)
    # 8 STORE_FAST               1 (pytest)
    # 392          10 LOAD_FAST                1 (pytest)
    # 12 LOAD_METHOD              1 (raises)
    # 34 LOAD_FAST                0 (expected_exception)
    # 36 LOAD_CONST               2 (None)
    # 38 KW_NAMES                 3
    # 40 PRECALL                  2
    # 44 CALL                     2
    # 54 RETURN_VALUE

def get_cython_table_params(ndframe, func_names_and_expected):
    """
    Combine frame, functions from com._cython_table
    keys and expected result.

    Parameters
    ----------
    ndframe : DataFrame or Series
    func_names_and_expected : Sequence of two items
        The first item is a name of an NDFrame method ('sum', 'prod') etc.
        The second item is the expected return value.

    Returns
    -------
    list
        List of three items (DataFrame, function, expected result)
    """
    # 395           0 RESUME                   0
    # 412           2 BUILD_LIST               0
    # 4 STORE_FAST               2 (results)
    # 413           6 LOAD_FAST                1 (func_names_and_expected)
    # 8 GET_ITER
    # >>   10 FOR_ITER                29 (to 70)
    # 12 UNPACK_SEQUENCE          2
    # 16 STORE_FAST               3 (func_name)
    # 18 STORE_FAST               4 (expected)
    # 414          20 LOAD_FAST                2 (results)
    # 22 LOAD_METHOD              0 (append)
    # 44 LOAD_FAST                0 (ndframe)
    # 46 LOAD_FAST                3 (func_name)
    # 48 LOAD_FAST                4 (expected)
    # 50 BUILD_TUPLE              3
    # 52 PRECALL                  1
    # 56 CALL                     1
    # 66 POP_TOP
    # 68 JUMP_BACKWARD           30 (to 10)
    # 415     >>   70 LOAD_FAST                2 (results)
    # 72 RETURN_VALUE

def get_op_from_name(op_name):
    """
    The operator function for a given op name.

    Parameters
    ----------
    op_name : str
        The op name, in form of "add" or "__add__".

    Returns
    -------
    function
        A function performing the operation.
    """
    # 0 MAKE_CELL                3 (rop)
    # 418           2 RESUME                   0
    # 432           4 LOAD_FAST                0 (op_name)
    # 6 LOAD_METHOD              0 (strip)
    # 28 LOAD_CONST               1 ('_')
    # 30 PRECALL                  1
    # 34 CALL                     1
    # 44 STORE_FAST               1 (short_opname)
    # 433          46 NOP
    # 434          48 LOAD_GLOBAL              3 (NULL + getattr)
    # 60 LOAD_GLOBAL              4 (operator)
    # 72 LOAD_FAST                1 (short_opname)
    # 74 PRECALL                  2
    # 78 CALL                     2
    # 88 STORE_FAST               2 (op)
    # 90 JUMP_FORWARD            50 (to 192)
    # >>   92 PUSH_EXC_INFO
    # 435          94 LOAD_GLOBAL              6 (AttributeError)
    # 106 CHECK_EXC_MATCH
    # 108 POP_JUMP_FORWARD_IF_FALSE    37 (to 184)
    # 110 POP_TOP
    # 437         112 LOAD_GLOBAL              3 (NULL + getattr)
    # 124 LOAD_GLOBAL              4 (operator)
    # 136 LOAD_FAST                1 (short_opname)
    # 138 LOAD_CONST               2 (1)
    # 140 LOAD_CONST               3 (None)
    # 142 BUILD_SLICE              2
    # 144 BINARY_SUBSCR
    # 154 PRECALL                  2
    # 158 CALL                     2
    # 168 STORE_DEREF              3 (rop)
    # 438         170 LOAD_CLOSURE             3 (rop)
    # 172 BUILD_TUPLE              1
    # 174 LOAD_CONST               4 (<code object <lambda> at 0x000001EBD7E41290, file "pandas\_testing\__init__.py", line 438>)
    # 176 MAKE_FUNCTION            8 (closure)
    # 178 STORE_FAST               2 (op)
    # 180 POP_EXCEPT
    # 182 JUMP_FORWARD             4 (to 192)
    # 435     >>  184 RERAISE                  0
    # >>  186 COPY                     3
    # 188 POP_EXCEPT
    # 190 RERAISE                  1
    # 440     >>  192 LOAD_FAST                2 (op)
    # 194 RETURN_VALUE
    # ExceptionTable:
    # 48 to 88 -> 92 [0]
    # 92 to 178 -> 186 [1] lasti
    # 184 to 184 -> 186 [1] lasti
    # Disassembly of <code object <lambda> at 0x000001EBD7E41290, file "pandas\_testing\__init__.py", line 438>:
    # 0 COPY_FREE_VARS           1
    # 438           2 RESUME                   0
    # 4 PUSH_NULL
    # 6 LOAD_DEREF               2 (rop)
    # 8 LOAD_FAST                1 (y)
    # 10 LOAD_FAST                0 (x)
    # 12 PRECALL                  2
    # 16 CALL                     2
    # 26 RETURN_VALUE

def getitem(x):
    # 447           0 RESUME                   0
    # 448           2 LOAD_FAST                0 (x)
    # 4 RETURN_VALUE

def setitem(x):
    # 451           0 RESUME                   0
    # 452           2 LOAD_FAST                0 (x)
    # 4 RETURN_VALUE

def loc(x):
    # 455           0 RESUME                   0
    # 456           2 LOAD_FAST                0 (x)
    # 4 LOAD_ATTR                0 (loc)
    # 14 RETURN_VALUE

def iloc(x):
    # 459           0 RESUME                   0
    # 460           2 LOAD_FAST                0 (x)
    # 4 LOAD_ATTR                0 (iloc)
    # 14 RETURN_VALUE

def at(x):
    # 463           0 RESUME                   0
    # 464           2 LOAD_FAST                0 (x)
    # 4 LOAD_ATTR                0 (at)
    # 14 RETURN_VALUE

def iat(x):
    # 467           0 RESUME                   0
    # 468           2 LOAD_FAST                0 (x)
    # 4 LOAD_ATTR                0 (iat)
    # 14 RETURN_VALUE

def get_finest_unit(left, right):
    """
    Find the higher of two datetime64 units.
    """
    # 476           0 RESUME                   0
    # 480           2 LOAD_GLOBAL              0 (_UNITS)
    # 14 LOAD_METHOD              1 (index)
    # 36 LOAD_FAST                0 (left)
    # 38 PRECALL                  1
    # 42 CALL                     1
    # 52 LOAD_GLOBAL              0 (_UNITS)
    # 64 LOAD_METHOD              1 (index)
    # 86 LOAD_FAST                1 (right)
    # 88 PRECALL                  1
    # 92 CALL                     1
    # 102 COMPARE_OP               5 (>=)
    # 108 POP_JUMP_FORWARD_IF_FALSE     2 (to 114)
    # 481         110 LOAD_FAST                0 (left)
    # 112 RETURN_VALUE
    # 482     >>  114 LOAD_FAST                1 (right)
    # 116 RETURN_VALUE

def shares_memory(left, right):
    """
    Pandas-compat for np.shares_memory.
    """
    # 485           0 RESUME                   0
    # 489           2 LOAD_GLOBAL              1 (NULL + isinstance)
    # 14 LOAD_FAST                0 (left)
    # 16 LOAD_GLOBAL              2 (np)
    # 28 LOAD_ATTR                2 (ndarray)
    # 38 PRECALL                  2
    # 42 CALL                     2
    # 52 POP_JUMP_FORWARD_IF_FALSE    47 (to 148)
    # 54 LOAD_GLOBAL              1 (NULL + isinstance)
    # 66 LOAD_FAST                1 (right)
    # 68 LOAD_GLOBAL              2 (np)
    # 80 LOAD_ATTR                2 (ndarray)
    # 90 PRECALL                  2
    # 94 CALL                     2
    # 104 POP_JUMP_FORWARD_IF_FALSE    21 (to 148)
    # 490         106 LOAD_GLOBAL              3 (NULL + np)
    # 118 LOAD_ATTR                3 (shares_memory)
    # 128 LOAD_FAST                0 (left)
    # 130 LOAD_FAST                1 (right)
    # 132 PRECALL                  2
    # 136 CALL                     2
    # 146 RETURN_VALUE
    # 491     >>  148 LOAD_GLOBAL              1 (NULL + isinstance)
    # 160 LOAD_FAST                0 (left)
    # 162 LOAD_GLOBAL              2 (np)
    # 174 LOAD_ATTR                2 (ndarray)
    # 184 PRECALL                  2
    # 188 CALL                     2
    # 198 POP_JUMP_FORWARD_IF_FALSE    16 (to 232)
    # 493         200 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 212 LOAD_FAST                1 (right)
    # 214 LOAD_FAST                0 (left)
    # 216 PRECALL                  2
    # 220 CALL                     2
    # 230 RETURN_VALUE
    # 495     >>  232 LOAD_GLOBAL              1 (NULL + isinstance)
    # 244 LOAD_FAST                0 (left)
    # 246 LOAD_GLOBAL              8 (RangeIndex)
    # 258 PRECALL                  2
    # 262 CALL                     2
    # 272 POP_JUMP_FORWARD_IF_FALSE     2 (to 278)
    # 496         274 LOAD_CONST               1 (False)
    # 276 RETURN_VALUE
    # 497     >>  278 LOAD_GLOBAL              1 (NULL + isinstance)
    # 290 LOAD_FAST                0 (left)
    # 292 LOAD_GLOBAL             10 (MultiIndex)
    # 304 PRECALL                  2
    # 308 CALL                     2
    # 318 POP_JUMP_FORWARD_IF_FALSE    21 (to 362)
    # 498         320 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 332 LOAD_FAST                0 (left)
    # 334 LOAD_ATTR                6 (_codes)
    # 344 LOAD_FAST                1 (right)
    # 346 PRECALL                  2
    # 350 CALL                     2
    # 360 RETURN_VALUE
    # 499     >>  362 LOAD_GLOBAL              1 (NULL + isinstance)
    # 374 LOAD_FAST                0 (left)
    # 376 LOAD_GLOBAL             14 (Index)
    # 388 LOAD_GLOBAL             16 (Series)
    # 400 BUILD_TUPLE              2
    # 402 PRECALL                  2
    # 406 CALL                     2
    # 416 POP_JUMP_FORWARD_IF_FALSE    75 (to 568)
    # 500         418 LOAD_GLOBAL              1 (NULL + isinstance)
    # 430 LOAD_FAST                1 (right)
    # 432 LOAD_GLOBAL             14 (Index)
    # 444 LOAD_GLOBAL             16 (Series)
    # 456 BUILD_TUPLE              2
    # 458 PRECALL                  2
    # 462 CALL                     2
    # 472 POP_JUMP_FORWARD_IF_FALSE    26 (to 526)
    # 501         474 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 486 LOAD_FAST                0 (left)
    # 488 LOAD_ATTR                9 (_values)
    # 498 LOAD_FAST                1 (right)
    # 500 LOAD_ATTR                9 (_values)
    # 510 PRECALL                  2
    # 514 CALL                     2
    # 524 RETURN_VALUE
    # 502     >>  526 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 538 LOAD_FAST                0 (left)
    # 540 LOAD_ATTR                9 (_values)
    # 550 LOAD_FAST                1 (right)
    # 552 PRECALL                  2
    # 556 CALL                     2
    # 566 RETURN_VALUE
    # 504     >>  568 LOAD_GLOBAL              1 (NULL + isinstance)
    # 580 LOAD_FAST                0 (left)
    # 582 LOAD_GLOBAL             20 (NDArrayBackedExtensionArray)
    # 594 PRECALL                  2
    # 598 CALL                     2
    # 608 POP_JUMP_FORWARD_IF_FALSE    21 (to 652)
    # 505         610 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 622 LOAD_FAST                0 (left)
    # 624 LOAD_ATTR               11 (_ndarray)
    # 634 LOAD_FAST                1 (right)
    # 636 PRECALL                  2
    # 640 CALL                     2
    # 650 RETURN_VALUE
    # 506     >>  652 LOAD_GLOBAL              1 (NULL + isinstance)
    # 664 LOAD_FAST                0 (left)
    # 666 LOAD_GLOBAL             24 (pd)
    # 678 LOAD_ATTR               13 (core)
    # 688 LOAD_ATTR               14 (arrays)
    # 698 LOAD_ATTR               15 (SparseArray)
    # 708 PRECALL                  2
    # 712 CALL                     2
    # 722 POP_JUMP_FORWARD_IF_FALSE    21 (to 766)
    # 507         724 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 736 LOAD_FAST                0 (left)
    # 738 LOAD_ATTR               16 (sp_values)
    # 748 LOAD_FAST                1 (right)
    # 750 PRECALL                  2
    # 754 CALL                     2
    # 764 RETURN_VALUE
    # 508     >>  766 LOAD_GLOBAL              1 (NULL + isinstance)
    # 778 LOAD_FAST                0 (left)
    # 780 LOAD_GLOBAL             24 (pd)
    # 792 LOAD_ATTR               13 (core)
    # 802 LOAD_ATTR               14 (arrays)
    # 812 LOAD_ATTR               17 (IntervalArray)
    # 822 PRECALL                  2
    # 826 CALL                     2
    # 836 POP_JUMP_FORWARD_IF_FALSE    42 (to 922)
    # 509         838 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 850 LOAD_FAST                0 (left)
    # 852 LOAD_ATTR               18 (_left)
    # 862 LOAD_FAST                1 (right)
    # 864 PRECALL                  2
    # 868 CALL                     2
    # 878 JUMP_IF_TRUE_OR_POP     20 (to 920)
    # 880 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 892 LOAD_FAST                0 (left)
    # 894 LOAD_ATTR               19 (_right)
    # 904 LOAD_FAST                1 (right)
    # 906 PRECALL                  2
    # 910 CALL                     2
    # >>  920 RETURN_VALUE
    # 511     >>  922 LOAD_GLOBAL              1 (NULL + isinstance)
    # 934 LOAD_FAST                0 (left)
    # 936 LOAD_GLOBAL             40 (ArrowExtensionArray)
    # 948 PRECALL                  2
    # 952 CALL                     2
    # 962 POP_JUMP_FORWARD_IF_FALSE   162 (to 1288)
    # 512         964 LOAD_GLOBAL              1 (NULL + isinstance)
    # 976 LOAD_FAST                1 (right)
    # 978 LOAD_GLOBAL             40 (ArrowExtensionArray)
    # 990 PRECALL                  2
    # 994 CALL                     2
    # 1004 POP_JUMP_FORWARD_IF_FALSE   120 (to 1246)
    # 514        1006 LOAD_FAST                0 (left)
    # 1008 LOAD_ATTR               21 (_pa_array)
    # 1018 STORE_FAST               2 (left_pa_data)
    # 515        1020 LOAD_FAST                1 (right)
    # 1022 LOAD_ATTR               21 (_pa_array)
    # 1032 STORE_FAST               3 (right_pa_data)
    # 516        1034 LOAD_FAST                2 (left_pa_data)
    # 1036 LOAD_METHOD             22 (chunk)
    # 1058 LOAD_CONST               2 (0)
    # 1060 PRECALL                  1
    # 1064 CALL                     1
    # 1074 LOAD_METHOD             23 (buffers)
    # 1096 PRECALL                  0
    # 1100 CALL                     0
    # 1110 LOAD_CONST               3 (1)
    # 1112 BINARY_SUBSCR
    # 1122 STORE_FAST               4 (left_buf1)
    # 517        1124 LOAD_FAST                3 (right_pa_data)
    # 1126 LOAD_METHOD             22 (chunk)
    # 1148 LOAD_CONST               2 (0)
    # 1150 PRECALL                  1
    # 1154 CALL                     1
    # 1164 LOAD_METHOD             23 (buffers)
    # 1186 PRECALL                  0
    # 1190 CALL                     0
    # 1200 LOAD_CONST               3 (1)
    # 1202 BINARY_SUBSCR
    # 1212 STORE_FAST               5 (right_buf1)
    # 518        1214 LOAD_FAST                4 (left_buf1)
    # 1216 LOAD_ATTR               24 (address)
    # 1226 LOAD_FAST                5 (right_buf1)
    # 1228 LOAD_ATTR               24 (address)
    # 1238 COMPARE_OP               2 (==)
    # 1244 RETURN_VALUE
    # 522     >> 1246 LOAD_GLOBAL              3 (NULL + np)
    # 1258 LOAD_ATTR                3 (shares_memory)
    # 1268 LOAD_FAST                0 (left)
    # 1270 LOAD_FAST                1 (right)
    # 1272 PRECALL                  2
    # 1276 CALL                     2
    # 1286 RETURN_VALUE
    # 524     >> 1288 LOAD_GLOBAL              1 (NULL + isinstance)
    # 1300 LOAD_FAST                0 (left)
    # 1302 LOAD_GLOBAL             50 (BaseMaskedArray)
    # 1314 PRECALL                  2
    # 1318 CALL                     2
    # 1328 POP_JUMP_FORWARD_IF_FALSE    83 (to 1496)
    # 1330 LOAD_GLOBAL              1 (NULL + isinstance)
    # 1342 LOAD_FAST                1 (right)
    # 1344 LOAD_GLOBAL             50 (BaseMaskedArray)
    # 1356 PRECALL                  2
    # 1360 CALL                     2
    # 1370 POP_JUMP_FORWARD_IF_FALSE    62 (to 1496)
    # 527        1372 LOAD_GLOBAL              3 (NULL + np)
    # 1384 LOAD_ATTR                3 (shares_memory)
    # 1394 LOAD_FAST                0 (left)
    # 1396 LOAD_ATTR               26 (_data)
    # 1406 LOAD_FAST                1 (right)
    # 1408 LOAD_ATTR               26 (_data)
    # 1418 PRECALL                  2
    # 1422 CALL                     2
    # 1432 JUMP_IF_TRUE_OR_POP     30 (to 1494)
    # 1434 LOAD_GLOBAL              3 (NULL + np)
    # 1446 LOAD_ATTR                3 (shares_memory)
    # 528        1456 LOAD_FAST                0 (left)
    # 1458 LOAD_ATTR               27 (_mask)
    # 1468 LOAD_FAST                1 (right)
    # 1470 LOAD_ATTR               27 (_mask)
    # 527        1480 PRECALL                  2
    # 1484 CALL                     2
    # >> 1494 RETURN_VALUE
    # 531     >> 1496 LOAD_GLOBAL              1 (NULL + isinstance)
    # 1508 LOAD_FAST                0 (left)
    # 1510 LOAD_GLOBAL             56 (DataFrame)
    # 1522 PRECALL                  2
    # 1526 CALL                     2
    # 1536 POP_JUMP_FORWARD_IF_FALSE    68 (to 1674)
    # 1538 LOAD_GLOBAL             59 (NULL + len)
    # 1550 LOAD_FAST                0 (left)
    # 1552 LOAD_ATTR               30 (_mgr)
    # 1562 LOAD_ATTR               31 (blocks)
    # 1572 PRECALL                  1
    # 1576 CALL                     1
    # 1586 LOAD_CONST               3 (1)
    # 1588 COMPARE_OP               2 (==)
    # 1594 POP_JUMP_FORWARD_IF_FALSE    39 (to 1674)
    # 532        1596 LOAD_FAST                0 (left)
    # 1598 LOAD_ATTR               30 (_mgr)
    # 1608 LOAD_ATTR               31 (blocks)
    # 1618 LOAD_CONST               2 (0)
    # 1620 BINARY_SUBSCR
    # 1630 LOAD_ATTR               32 (values)
    # 1640 STORE_FAST               6 (arr)
    # 533        1642 LOAD_GLOBAL              7 (NULL + shares_memory)
    # 1654 LOAD_FAST                6 (arr)
    # 1656 LOAD_FAST                1 (right)
    # 1658 PRECALL                  2
    # 1662 CALL                     2
    # 1672 RETURN_VALUE
    # 535     >> 1674 LOAD_GLOBAL             67 (NULL + NotImplementedError)
    # 1686 LOAD_GLOBAL             69 (NULL + type)
    # 1698 LOAD_FAST                0 (left)
    # 1700 PRECALL                  1
    # 1704 CALL                     1
    # 1714 LOAD_GLOBAL             69 (NULL + type)
    # 1726 LOAD_FAST                1 (right)
    # 1728 PRECALL                  1
    # 1732 CALL                     1
    # 1742 PRECALL                  2
    # 1746 CALL                     2
    # 1756 RAISE_VARARGS            1
