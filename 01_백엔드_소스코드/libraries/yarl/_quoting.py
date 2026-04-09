# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _quoting.pyc (Python 3.11)

import os
import sys
from typing import TYPE_CHECKING
__all__ = ('_Quoter', '_Unquoter')
NO_EXTENSIONS = bool(os.environ.get('YARL_NO_EXTENSIONS'))
if sys.implementation.name != 'cpython':
    NO_EXTENSIONS = True
if TYPE_CHECKING or NO_EXTENSIONS:
    from _quoting_py import _Quoter, _Unquoter
    return None

try:
    from _quoting_c import _Quoter, _Unquoter
    return None
except ImportError:
    from _quoting_py import _Quoter, _Unquoter
    return None
