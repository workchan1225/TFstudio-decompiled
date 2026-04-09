# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageMode.pyc (Python 3.11)

from __future__ import annotations
import sys
from functools import lru_cache
from typing import NamedTuple

class ModeDescriptor(NamedTuple):
    typestr: 'str' = 'Wrapper for mode strings.'
    
    def __str__(self = None):
        return self.mode


getmode = (lambda mode = None: endian = '<' if sys.byteorder == 'little' else '>'# WARNING: Decompyle incomplete
)()
