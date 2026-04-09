# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hostfxr_errors.pyc (Python 3.11)

from typing import Optional
from clr_error import ClrError
__all__ = [
    'get_hostfxr_error']

def get_hostfxr_error(hresult = None):
    if hresult in HOSTFXR_ERRORS:
        return ClrError(hresult, HOSTFXR_ERRORS[hresult])

# WARNING: Decompyle incomplete
