# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _checkpoints.pyc (Python 3.11)

from __future__ import annotations
from contextlib import AbstractContextManager, contextmanager
from typing import TYPE_CHECKING
from  import _core
if TYPE_CHECKING:
    from collections.abc import Generator
_assert_yields_or_not = (lambda expected = None: pass# WARNING: Decompyle incomplete
)()

def assert_checkpoints():
    """Use as a context manager to check that the code inside the ``with``
    block either exits with an exception or executes at least one
    :ref:`checkpoint <checkpoints>`.

    Raises:
      AssertionError: if no checkpoint was executed.

    Example:
      Check that :func:`trio.sleep` is a checkpoint, even if it doesn't
      block::

         with trio.testing.assert_checkpoints():
             await trio.sleep(0)

    """
    __tracebackhide__ = True
    return _assert_yields_or_not(True)


def assert_no_checkpoints():
    '''Use as a context manager to check that the code inside the ``with``
    block does not execute any :ref:`checkpoints <checkpoints>`.

    Raises:
      AssertionError: if a checkpoint was executed.

    Example:
      Synchronous code never contains any checkpoints, but we can double-check
      that::

         send_channel, receive_channel = trio.open_memory_channel(10)
         with trio.testing.assert_no_checkpoints():
             send_channel.send_nowait(None)

    '''
    __tracebackhide__ = True
    return _assert_yields_or_not(False)
