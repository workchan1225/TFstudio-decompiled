# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shared.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import numba
if TYPE_CHECKING:
    import numpy as np
is_monotonic_increasing = (lambda bounds = None: n = len(bounds)if n < 2:
Trueprev = None[0]for i in range(1, n):
cur = bounds[i]if cur < prev:
Falseprev = NoneTrue)()
