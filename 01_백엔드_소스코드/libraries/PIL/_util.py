# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

from __future__ import annotations
import os
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any, NoReturn, TypeGuard
    from _typing import StrOrBytesPath

def is_path(f = None):
    return isinstance(f, (bytes, str, os.PathLike))


class DeferredError:
    
    def __init__(self = None, ex = None):
        self.ex = ex

    
    def __getattr__(self = None, elt = None):
        raise self.ex

    new = (lambda ex = None: DeferredError(ex))()
