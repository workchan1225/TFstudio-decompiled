# Source: bytecode disassembly (fallback)
# Quality: MEDIUM - structure + bytecode
# Original: pandas\core\config_init.py

"""
This module is imported from the pandas package __init__.py file
in order to ensure that the core.config options registered here will
be available as soon as the user loads the package. if register_option
is invoked inside specific modules, they will not be registered until that
module is imported, which may or may not be a problem.

If you need to make sure options are available even before a certain
module is imported, register them here rather than in the module.

"""

from __future__ import annotations
from collections.abc import Callable
import os
from typing import Any
from pandas._config.config import _config
from pandas._config.config import is_bool
from pandas.errors import Pandas4Warning

def use_bottleneck_cb(key):
    # 43           0 RESUME                   0
    # 44           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('nanops',))
    # 6 IMPORT_NAME              0 (pandas.core)
    # 8 IMPORT_FROM              1 (nanops)
    # 10 STORE_FAST               1 (nanops)
    # 12 POP_TOP
    # 46          14 LOAD_FAST                1 (nanops)
    # 16 LOAD_METHOD              2 (set_use_bottleneck)
    # 38 LOAD_GLOBAL              7 (NULL + cf)
    # 50 LOAD_ATTR                4 (get_option)
    # 60 LOAD_FAST                0 (key)
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 POP_TOP
    # 92 LOAD_CONST               0 (None)
    # 94 RETURN_VALUE

def use_numexpr_cb(key):
    # 57           0 RESUME                   0
    # 58           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('expressions',))
    # 6 IMPORT_NAME              0 (pandas.core.computation)
    # 8 IMPORT_FROM              1 (expressions)
    # 10 STORE_FAST               1 (expressions)
    # 12 POP_TOP
    # 60          14 LOAD_FAST                1 (expressions)
    # 16 LOAD_METHOD              2 (set_use_numexpr)
    # 38 LOAD_GLOBAL              7 (NULL + cf)
    # 50 LOAD_ATTR                4 (get_option)
    # 60 LOAD_FAST                0 (key)
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 POP_TOP
    # 92 LOAD_CONST               0 (None)
    # 94 RETURN_VALUE

def use_numba_cb(key):
    # 71           0 RESUME                   0
    # 72           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('numba_',))
    # 6 IMPORT_NAME              0 (pandas.core.util)
    # 8 IMPORT_FROM              1 (numba_)
    # 10 STORE_FAST               1 (numba_)
    # 12 POP_TOP
    # 74          14 LOAD_FAST                1 (numba_)
    # 16 LOAD_METHOD              2 (set_use_numba)
    # 38 LOAD_GLOBAL              7 (NULL + cf)
    # 50 LOAD_ATTR                4 (get_option)
    # 60 LOAD_FAST                0 (key)
    # 62 PRECALL                  1
    # 66 CALL                     1
    # 76 PRECALL                  1
    # 80 CALL                     1
    # 90 POP_TOP
    # 92 LOAD_CONST               0 (None)
    # 94 RETURN_VALUE

def table_schema_cb(key):
    # 290           0 RESUME                   0
    # 291           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('enable_data_resource_formatter',))
    # 6 IMPORT_NAME              0 (pandas.io.formats.printing)
    # 8 IMPORT_FROM              1 (enable_data_resource_formatter)
    # 10 STORE_FAST               1 (enable_data_resource_formatter)
    # 12 POP_TOP
    # 293          14 PUSH_NULL
    # 16 LOAD_FAST                1 (enable_data_resource_formatter)
    # 18 LOAD_GLOBAL              5 (NULL + cf)
    # 30 LOAD_ATTR                3 (get_option)
    # 40 LOAD_FAST                0 (key)
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 56 PRECALL                  1
    # 60 CALL                     1
    # 70 POP_TOP
    # 72 LOAD_CONST               0 (None)
    # 74 RETURN_VALUE

def is_terminal():
    """
    Detect if Python is running in a terminal.

    Returns True if Python is running in a terminal or False if not.
    """
    # 296           0 RESUME                   0
    # 302           2 NOP
    # 304           4 LOAD_GLOBAL              1 (NULL + get_ipython)
    # 16 PRECALL                  0
    # 20 CALL                     0
    # 30 STORE_FAST               0 (ip)
    # 308          32 LOAD_GLOBAL              3 (NULL + hasattr)
    # 44 LOAD_FAST                0 (ip)
    # 46 LOAD_CONST               1 ('kernel')
    # 48 PRECALL                  2
    # 52 CALL                     2
    # 62 POP_JUMP_FORWARD_IF_FALSE     2 (to 68)
    # 309          64 LOAD_CONST               2 (False)
    # 66 RETURN_VALUE
    # 311     >>   68 LOAD_CONST               3 (True)
    # 70 RETURN_VALUE
    # >>   72 PUSH_EXC_INFO
    # 305          74 LOAD_GLOBAL              4 (NameError)
    # 86 CHECK_EXC_MATCH
    # 88 POP_JUMP_FORWARD_IF_FALSE     4 (to 98)
    # 90 POP_TOP
    # 306          92 POP_EXCEPT
    # 94 LOAD_CONST               3 (True)
    # 96 RETURN_VALUE
    # 305     >>   98 RERAISE                  0
    # >>  100 COPY                     3
    # 102 POP_EXCEPT
    # 104 RERAISE                  1
    # ExceptionTable:
    # 4 to 30 -> 72 [0]
    # 72 to 90 -> 100 [1] lasti
    # 98 to 98 -> 100 [1] lasti

def is_valid_string_storage(value):
    # 467           0 RESUME                   0
    # 468           2 BUILD_LIST               0
    # 4 LOAD_CONST               1 (('auto', 'python', 'pyarrow'))
    # 6 LIST_EXTEND              1
    # 8 STORE_FAST               1 (legal_values)
    # 469          10 LOAD_FAST                0 (value)
    # 12 LOAD_FAST                1 (legal_values)
    # 14 CONTAINS_OP              1
    # 16 POP_JUMP_FORWARD_IF_FALSE    17 (to 52)
    # 470          18 LOAD_CONST               2 ('Value must be one of python|pyarrow')
    # 20 STORE_FAST               2 (msg)
    # 471          22 LOAD_GLOBAL              1 (NULL + ValueError)
    # 34 LOAD_FAST                2 (msg)
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 RAISE_VARARGS            1
    # 469     >>   52 LOAD_CONST               0 (None)
    # 54 RETURN_VALUE

def register_plotting_backend_cb(key):
    # 622           0 RESUME                   0
    # 623           2 LOAD_FAST                0 (key)
    # 4 LOAD_CONST               1 ('matplotlib')
    # 6 COMPARE_OP               2 (==)
    # 12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
    # 625          14 LOAD_CONST               0 (None)
    # 16 RETURN_VALUE
    # 626     >>   18 LOAD_CONST               2 (0)
    # 20 LOAD_CONST               3 (('_get_plot_backend',))
    # 22 IMPORT_NAME              0 (pandas.plotting._core)
    # 24 IMPORT_FROM              1 (_get_plot_backend)
    # 26 STORE_FAST               1 (_get_plot_backend)
    # 28 POP_TOP
    # 628          30 PUSH_NULL
    # 32 LOAD_FAST                1 (_get_plot_backend)
    # 34 LOAD_FAST                0 (key)
    # 36 PRECALL                  1
    # 40 CALL                     1
    # 50 POP_TOP
    # 52 LOAD_CONST               0 (None)
    # 54 RETURN_VALUE

def register_converter_cb(key):
    # 648           0 RESUME                   0
    # 649           2 LOAD_CONST               1 (0)
    # 4 LOAD_CONST               2 (('deregister_matplotlib_converters', 'register_matplotlib_converters'))
    # 6 IMPORT_NAME              0 (pandas.plotting)
    # 8 IMPORT_FROM              1 (deregister_matplotlib_converters)
    # 10 STORE_FAST               1 (deregister_matplotlib_converters)
    # 12 IMPORT_FROM              2 (register_matplotlib_converters)
    # 14 STORE_FAST               2 (register_matplotlib_converters)
    # 16 POP_TOP
    # 654          18 LOAD_GLOBAL              7 (NULL + cf)
    # 30 LOAD_ATTR                4 (get_option)
    # 40 LOAD_FAST                0 (key)
    # 42 PRECALL                  1
    # 46 CALL                     1
    # 56 POP_JUMP_FORWARD_IF_FALSE    12 (to 82)
    # 655          58 PUSH_NULL
    # 60 LOAD_FAST                2 (register_matplotlib_converters)
    # 62 PRECALL                  0
    # 66 CALL                     0
    # 76 POP_TOP
    # 78 LOAD_CONST               0 (None)
    # 80 RETURN_VALUE
    # 657     >>   82 PUSH_NULL
    # 84 LOAD_FAST                1 (deregister_matplotlib_converters)
    # 86 PRECALL                  0
    # 90 CALL                     0
    # 100 POP_TOP
    # 102 LOAD_CONST               0 (None)
    # 104 RETURN_VALUE
