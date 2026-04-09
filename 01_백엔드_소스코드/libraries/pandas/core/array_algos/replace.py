# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: replace.pyc (Python 3.11)

'''
Methods used by Block.replace and related methods.
'''
from __future__ import annotations
import operator
import re
from re import Pattern
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas.core.dtypes.common import is_bool, is_re, is_re_compilable
from pandas.core.dtypes.missing import isna
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Scalar, npt

def should_use_regex(regex = None, to_replace = None):
