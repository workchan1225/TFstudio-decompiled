# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tasks.pyc (Python 3.11)

from __future__ import annotations
import sys
from abc import ABCMeta, abstractmethod
from collections.abc import Awaitable, Callable
from types import TracebackType
from typing import TYPE_CHECKING, Any, Protocol, overload
if sys.version_info >= (3, 13):
    from typing import TypeVar
else:
    from typing_extensions import TypeVar
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from typing_extensions import TypeVarTuple, Unpack
if TYPE_CHECKING:
    from _core._tasks import CancelScope
T_Retval = TypeVar('T_Retval')
T_contra = TypeVar('T_contra', contravariant = True, default = None)
PosArgsT = TypeVarTuple('PosArgsT')

def TaskStatus():
    '''TaskStatus'''
    started = (lambda self = None: pass)()
    started = (lambda self = None, value = None: pass)()
    
    def started(self = None, value = None):
        '''
        Signal that the task has started.

        :param value: object passed back to the starter of the task
        '''
        pass


TaskStatus = <NODE:27>(TaskStatus, 'TaskStatus', Protocol[T_contra])

def TaskGroup():
    '''TaskGroup'''
    cancel_scope: 'CancelScope' = "\n    Groups several asynchronous tasks together.\n\n    :ivar cancel_scope: the cancel scope inherited by all child tasks\n    :vartype cancel_scope: CancelScope\n\n    .. note:: On asyncio, support for eager task factories is considered to be\n        **experimental**. In particular, they don't follow the usual semantics of new\n        tasks being scheduled on the next iteration of the event loop, and may thus\n        cause unexpected behavior in code that wasn't written with such semantics in\n        mind.\n    "
    start_soon = (lambda self = None, func = None, *, name, args = None: pass)()
    start = (lambda self = None, func = None, *, name, args = None: pass# WARNING: Decompyle incomplete
)()
    __aenter__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __aexit__ = (lambda self = None, exc_type = None, exc_val = abstractmethod, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool'): pass# WARNING: Decompyle incomplete
)()

TaskGroup = <NODE:27>(TaskGroup, 'TaskGroup', metaclass = ABCMeta)
