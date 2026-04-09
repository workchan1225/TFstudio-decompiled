# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _wait_for_object.pyc (Python 3.11)

from __future__ import annotations
import math
import trio
from _core._windows_cffi import CData, ErrorCodes, _handle, ffi, handle_array, kernel32, raise_winerror

async def WaitForSingleObject(obj = None):
    '''Async and cancellable variant of WaitForSingleObject. Windows only.

    Args:
      handle: A Win32 handle, as a Python integer.

    Raises:
      OSError: If the handle is invalid, e.g. when it is already closed.

    '''
    pass
# WARNING: Decompyle incomplete


def WaitForMultipleObjects_sync(*handles):
    '''Wait for any of the given Windows handles to be signaled.'''
    n = len(handles)
    handle_arr = handle_array(n)
    for i in range(n):
        handle_arr[i] = handles[i]
        timeout = 0xFFFFFFFF
        retcode = kernel32.WaitForMultipleObjects(n, handle_arr, False, timeout)
        if retcode == ErrorCodes.WAIT_FAILED:
            raise_winerror()
            return None
        return None
