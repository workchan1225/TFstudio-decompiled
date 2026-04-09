# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
import types
from collections.abc import MutableSequence
from functools import total_ordering
__version__ = '1.8.0'
__all__ = ('FrozenList', 'PyFrozenList')
NO_EXTENSIONS = bool(os.environ.get('FROZENLIST_NO_EXTENSIONS'))
FrozenList = <NODE:12>()
PyFrozenList = FrozenList
if not NO_EXTENSIONS:
    
    try:
        from _frozenlist import FrozenList as CFrozenList
        FrozenList = CFrozenList
        return None
    except ImportError:
        return None
        return None
