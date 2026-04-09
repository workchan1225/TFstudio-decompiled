# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _timeouts.pyc (Python 3.11)

from __future__ import annotations
import math
import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING, NoReturn
import trio
if TYPE_CHECKING:
    from collections.abc import Generator

def move_on_at(deadline = None, *, shield):
    '''Use as a context manager to create a cancel scope with the given
    absolute deadline.

    Args:
      deadline (float): The deadline.
      shield (bool): Initial value for the `~trio.CancelScope.shield` attribute
          of the newly created cancel scope.

    Raises:
      ValueError: if deadline is NaN.

    '''
    return trio.CancelScope(deadline = deadline, shield = shield)


def move_on_after(seconds = None, *, shield):
    '''Use as a context manager to create a cancel scope whose deadline is
    set to now + *seconds*.

    The deadline of the cancel scope is calculated upon entering.

    Args:
      seconds (float): The timeout.
      shield (bool): Initial value for the `~trio.CancelScope.shield` attribute
          of the newly created cancel scope.

    Raises:
      ValueError: if ``seconds`` is less than zero or NaN.

    '''
    if seconds < 0:
        raise ValueError('`seconds` must be non-negative')
    if math.isnan(seconds):
        raise ValueError('`seconds` must not be NaN')
    return trio.CancelScope(shield = shield, relative_deadline = seconds)


async def sleep_forever():
    '''Pause execution of the current task forever (or until cancelled).

    Equivalent to calling ``await sleep(math.inf)``, except that if manually
    rescheduled this will raise a `RuntimeError`.

    Raises:
      RuntimeError: if rescheduled

    '''
    pass
# WARNING: Decompyle incomplete


async def sleep_until(deadline = None):
    """Pause execution of the current task until the given time.

    The difference between :func:`sleep` and :func:`sleep_until` is that the
    former takes a relative time and the latter takes an absolute time
    according to Trio's internal clock (as returned by :func:`current_time`).

    Args:
        deadline (float): The time at which we should wake up again. May be in
            the past, in which case this function executes a checkpoint but
            does not block.

    Raises:
      ValueError: if deadline is NaN.

    """
    pass
# WARNING: Decompyle incomplete


async def sleep(seconds = None):
    '''Pause execution of the current task for the given number of seconds.

    Args:
        seconds (float): The number of seconds to sleep. May be zero to
            insert a checkpoint without actually blocking.

    Raises:
        ValueError: if *seconds* is negative or NaN.

    '''
    pass
# WARNING: Decompyle incomplete


class TooSlowError(Exception):
    '''Raised by :func:`fail_after` and :func:`fail_at` if the timeout
    expires.

    '''
    pass

fail_at = (lambda deadline = None, *, shield: pass# WARNING: Decompyle incomplete
)()
fail_after = (lambda seconds = None, *, shield: pass# WARNING: Decompyle incomplete
)()
if 'sphinx.ext.autodoc' in sys.modules:
    import inspect
    for c in (fail_at, fail_after):
        c.__signature__ = inspect.Signature.from_callable(c).replace(return_annotation = trio.CancelScope)
        return None
        return None
