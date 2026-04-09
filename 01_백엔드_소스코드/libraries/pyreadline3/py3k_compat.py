# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py3k_compat.pyc (Python 3.11)

import sys
from collections.abc import Callable
from typing import Any, Dict, Optional
is_ironpython = 'IronPython' in sys.version

def is_callable(x = None):
    return isinstance(x, Callable)


def execfile(fname = None, glob = None, loc = None):
    pass
# WARNING: Decompyle incomplete
