# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expanding.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Concatenate, Literal, Self, final, overload
from pandas.util._decorators import set_module
from pandas.core.indexers.objects import BaseIndexer, ExpandingIndexer, GroupbyIndexer
from pandas.core.window.rolling import BaseWindowGroupby, RollingAndExpandingMixin
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import P, QuantileInterpolation, T, WindowingRankType
    from pandas import DataFrame, Series
    from pandas.core.generic import NDFrame
Expanding = <NODE:12>()
ExpandingGroupby = <NODE:12>()
