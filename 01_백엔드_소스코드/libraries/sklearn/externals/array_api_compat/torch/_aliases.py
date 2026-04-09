# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _aliases.pyc (Python 3.11)

from __future__ import annotations
from functools import reduce as _reduce, wraps as _wraps
from builtins import all as _builtin_all, any as _builtin_any
from typing import Any, List, Optional, Sequence, Tuple, Union, Literal
import torch
from _internal import get_xp
from common import _aliases
from common._typing import NestedSequence, SupportsBufferProtocol
from _info import __array_namespace_info__
from _typing import Array, Device, DType
_int_dtypes = {
    torch.uint8,
    torch.int8,
    torch.int16,
    torch.int32,
    torch.int64}

try:
    _int_dtypes |= {
        torch.uint16,
        torch.uint32,
        torch.uint64}
except AttributeError:
    pass

# WARNING: Decompyle incomplete
