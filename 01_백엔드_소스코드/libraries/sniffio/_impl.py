# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from contextvars import ContextVar
from typing import Optional
import sys
import threading
current_async_library_cvar = ContextVar('current_async_library_cvar', default = None)

class _ThreadLocal(threading.local):
    name = None

thread_local = _ThreadLocal()

class AsyncLibraryNotFoundError(RuntimeError):
    pass


def current_async_library():
    '''Detect which async library is currently running.

    The following libraries are currently supported:

    ================   ===========  ============================
    Library             Requires     Magic string
    ================   ===========  ============================
    **Trio**            Trio v0.6+   ``"trio"``
    **Curio**           -            ``"curio"``
    **asyncio**                      ``"asyncio"``
    **Trio-asyncio**    v0.8.2+     ``"trio"`` or ``"asyncio"``,
                                    depending on current mode
    ================   ===========  ============================

    Returns:
      A string like ``"trio"``.

    Raises:
      AsyncLibraryNotFoundError: if called from synchronous context,
        or if the current async library was not recognized.

    Examples:

        .. code-block:: python3

           from sniffio import current_async_library

           async def generic_sleep(seconds):
               library = current_async_library()
               if library == "trio":
                   import trio
                   await trio.sleep(seconds)
               elif library == "asyncio":
                   import asyncio
                   await asyncio.sleep(seconds)
               # ... and so on ...
               else:
                   raise RuntimeError(f"Unsupported library {library!r}")

    '''
    value = thread_local.name
# WARNING: Decompyle incomplete
