# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _signals.pyc (Python 3.11)

from __future__ import annotations
import signal
from collections import OrderedDict
from contextlib import contextmanager
from typing import TYPE_CHECKING
import trio
from _util import ConflictDetector, is_main_thread
if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Callable, Generator, Iterable
    from types import FrameType
    from typing_extensions import Self
_signal_handler = (lambda signals = None, handler = None: pass# WARNING: Decompyle incomplete
)()

class SignalReceiver:
    
    def __init__(self = None):
        self._pending = OrderedDict()
        self._lot = trio.lowlevel.ParkingLot()
        self._conflict_detector = ConflictDetector('only one task can iterate on a signal receiver at a time')
        self._closed = False

    
    def _add(self = None, signum = None):
        if self._closed:
            signal.raise_signal(signum)
            return None
        self._pending[signum] = None
        self._lot.unpark()

    
    def _redeliver_remaining(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete



def get_pending_signal_count(rec = None):
    '''Helper for tests, not public or otherwise used.'''
    pass
# WARNING: Decompyle incomplete

open_signal_receiver = (lambda : pass# WARNING: Decompyle incomplete
)()
