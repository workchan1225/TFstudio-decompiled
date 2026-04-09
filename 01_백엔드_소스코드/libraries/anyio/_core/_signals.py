# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _signals.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import AsyncIterator
from contextlib import AbstractContextManager
from signal import Signals
from _eventloop import get_async_backend

def open_signal_receiver(*signals):
    '''
    Start receiving operating system signals.

    :param signals: signals to receive (e.g. ``signal.SIGINT``)
    :return: an asynchronous context manager for an asynchronous iterator which yields
        signal numbers

    .. warning:: Windows does not support signals natively so it is best to avoid
        relying on this in cross-platform applications.

    .. warning:: On asyncio, this permanently replaces any previous signal handler for
        the given signals, as set via :meth:`~asyncio.loop.add_signal_handler`.

    '''
    pass
# WARNING: Decompyle incomplete
