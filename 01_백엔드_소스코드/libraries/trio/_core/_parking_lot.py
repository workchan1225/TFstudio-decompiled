# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parking_lot.pyc (Python 3.11)

from __future__ import annotations
import inspect
import math
from collections import OrderedDict
from typing import TYPE_CHECKING
import attrs
import outcome
from  import _core
from _util import final
if TYPE_CHECKING:
    from collections.abc import Iterator
    from _run import Task
GLOBAL_PARKING_LOT_BREAKER: 'dict[Task, list[ParkingLot]]' = { }

def add_parking_lot_breaker(task = None, lot = None):
    '''Register a task as a breaker for a lot. See :meth:`ParkingLot.break_lot`.

    raises:
      trio.BrokenResourceError: if the task has already exited.
    '''
    if inspect.getcoroutinestate(task.coro) == inspect.CORO_CLOSED:
        raise _core._exceptions.BrokenResourceError('Attempted to add already exited task as lot breaker.')
    if task not in GLOBAL_PARKING_LOT_BREAKER:
        GLOBAL_PARKING_LOT_BREAKER[task] = [
            lot]
        return None
    None[task].append(lot)


def remove_parking_lot_breaker(task = None, lot = None):
    '''Deregister a task as a breaker for a lot. See :meth:`ParkingLot.break_lot`'''
    
    try:
        GLOBAL_PARKING_LOT_BREAKER[task].remove(lot)
    except (KeyError, ValueError):
        raise RuntimeError('Attempted to remove task as breaker for a lot it is not registered for'), None

    if not GLOBAL_PARKING_LOT_BREAKER[task]:
        del GLOBAL_PARKING_LOT_BREAKER[task]
        return None

ParkingLotStatistics = <NODE:12>()
ParkingLot = <NODE:12>()()
