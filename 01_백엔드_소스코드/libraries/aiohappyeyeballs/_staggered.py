# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _staggered.pyc (Python 3.11)

import asyncio
import contextlib
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Iterable, List, Optional, Set, Tuple, TypeVar, Union
_T = TypeVar('_T')
RE_RAISE_EXCEPTIONS = (SystemExit, KeyboardInterrupt)

def _set_result(wait_next = None):
    '''Set the result of a future if it is not already done.'''
    if not wait_next.done():
        wait_next.set_result(None)
        return None


async def _wait_one(futures = None, loop = None):
    '''Wait for the first future to complete.'''
    pass
# WARNING: Decompyle incomplete


async def staggered_race(coro_fns = None, delay = None, *, loop):
    """
    Run coroutines with staggered start times and take the first to finish.

    This method takes an iterable of coroutine functions. The first one is
    started immediately. From then on, whenever the immediately preceding one
    fails (raises an exception), or when *delay* seconds has passed, the next
    coroutine is started. This continues until one of the coroutines complete
    successfully, in which case all others are cancelled, or until all
    coroutines fail.

    The coroutines provided should be well-behaved in the following way:

    * They should only ``return`` if completed successfully.

    * They should always raise an exception if they did not complete
      successfully. In particular, if they handle cancellation, they should
      probably reraise, like this::

        try:
            # do work
        except asyncio.CancelledError:
            # undo partially completed work
            raise

    Args:
    ----
        coro_fns: an iterable of coroutine functions, i.e. callables that
            return a coroutine object when called. Use ``functools.partial`` or
            lambdas to pass arguments.

        delay: amount of time, in seconds, between starting coroutines. If
            ``None``, the coroutines will run sequentially.

        loop: the event loop to use. If ``None``, the running loop is used.

    Returns:
    -------
        tuple *(winner_result, winner_index, exceptions)* where

        - *winner_result*: the result of the winning coroutine, or ``None``
          if no coroutines won.

        - *winner_index*: the index of the winning coroutine in
          ``coro_fns``, or ``None`` if no coroutines won. If the winning
          coroutine may return None on success, *winner_index* can be used
          to definitively determine whether any coroutine won.

        - *exceptions*: list of exceptions returned by the coroutines.
          ``len(exceptions)`` is equal to the number of coroutines actually
          started, and the order is the same as in ``coro_fns``. The winning
          coroutine's entry is ``None``.

    """
    pass
# WARNING: Decompyle incomplete
