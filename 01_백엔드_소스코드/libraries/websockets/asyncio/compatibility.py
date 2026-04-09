# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compatibility.pyc (Python 3.11)

from __future__ import annotations
import sys
__all__ = [
    'TimeoutError',
    'aiter',
    'anext',
    'asyncio_timeout',
    'asyncio_timeout_at']
if sys.version_info[:2] >= (3, 11):
    TimeoutError = TimeoutError
    aiter = aiter
    anext = anext
    from asyncio import timeout as asyncio_timeout, timeout_at as asyncio_timeout_at
    return None
from asyncio import TimeoutError

def aiter(async_iterable):
    return type(async_iterable).__aiter__(async_iterable)


async def anext(async_iterator):
    pass
# WARNING: Decompyle incomplete

from async_timeout import timeout as asyncio_timeout, timeout_at as asyncio_timeout_at
