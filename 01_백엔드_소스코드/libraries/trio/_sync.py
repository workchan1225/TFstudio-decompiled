# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _sync.pyc (Python 3.11)

from __future__ import annotations
import math
from typing import TYPE_CHECKING, Literal, Protocol, TypeVar
import attrs
import trio
from  import _core
from _core import Abort, ParkingLot, RaiseCancelT, add_parking_lot_breaker, enable_ki_protection, remove_parking_lot_breaker
from _deprecate import warn_deprecated
from _util import final
if TYPE_CHECKING:
    from collections.abc import Callable
    from types import TracebackType
    from typing_extensions import deprecated
    from _core import Task
    from _core._parking_lot import ParkingLotStatistics
else:
    T = TypeVar('T')
    
    def deprecated(message = None, *, category, stacklevel):
        
        def wrapper(f = None):
            return f

        return wrapper

EventStatistics = <NODE:12>()
Event = <NODE:12>()()

class _HasAcquireRelease(Protocol):
    """Only classes with acquire() and release() can use the mixin's implementations."""
    
    async def acquire(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def release(self = None):
        pass



class AsyncContextManagerMixin:
    __aenter__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __aexit__ = (lambda self = None, exc_type = None, exc_value = enable_ki_protection, traceback = ('self', '_HasAcquireRelease', 'exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

CapacityLimiterStatistics = <NODE:12>()
CapacityLimiter = <NODE:12>()
Semaphore = <NODE:12>()
LockStatistics = <NODE:12>()
_LockImpl = <NODE:12>()
Lock = <NODE:12>()
StrictFIFOLock = <NODE:12>()
ConditionStatistics = <NODE:12>()
Condition = <NODE:12>()
