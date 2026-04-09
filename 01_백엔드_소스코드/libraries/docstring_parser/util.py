# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

__doc__ = 'Utility functions for working with docstrings.'
import typing as T
from collections import ChainMap
from inspect import Signature
from itertools import chain
from common import DocstringMeta, DocstringParam, DocstringReturns, DocstringStyle, RenderingStyle
from parser import compose, parse
_Func = T.Callable[(..., T.Any)]
# WARNING: Decompyle incomplete
