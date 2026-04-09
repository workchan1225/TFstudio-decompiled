# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _sync.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import functools
from typing import TypeVar, Callable, Awaitable
from typing_extensions import ParamSpec
import anyio
import sniffio
import anyio.to_thread as anyio
T_Retval = TypeVar('T_Retval')
T_ParamSpec = ParamSpec('T_ParamSpec')

async def to_thread(func = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def asyncify(function = None):
    '''
    Take a blocking function and create an async one that receives the same
    positional and keyword arguments.

    Usage:

    ```python
    def blocking_func(arg1, arg2, kwarg1=None):
        # blocking code
        return result


    result = asyncify(blocking_function)(arg1, arg2, kwarg1=value1)
    ```

    ## Arguments

    `function`: a blocking regular callable (e.g. a function)

    ## Return

    An async function that takes the same positional and keyword arguments as the
    original one, that when called runs the same original function in a thread worker
    and returns the result.
    '''
    pass
# WARNING: Decompyle incomplete
