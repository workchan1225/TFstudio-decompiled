# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tasks.pyc (Python 3.11)

from __future__ import annotations
import math
from collections.abc import Generator
from contextlib import contextmanager
from types import TracebackType
from abc._tasks import TaskGroup, TaskStatus
from _eventloop import get_async_backend

def _IgnoredTaskStatus():
    '''_IgnoredTaskStatus'''
    
    def started(self = None, value = None):
        pass


_IgnoredTaskStatus = <NODE:27>(_IgnoredTaskStatus, '_IgnoredTaskStatus', TaskStatus[object])
TASK_STATUS_IGNORED = _IgnoredTaskStatus()

class CancelScope:
    '''
    Wraps a unit of work that can be made separately cancellable.

    :param deadline: The time (clock value) when this scope is cancelled automatically
    :param shield: ``True`` to shield the cancel scope from external cancellation
    '''
    
    def __new__(cls = None, *, deadline, shield):
        return get_async_backend().create_cancel_scope(shield = shield, deadline = deadline)

    
    def cancel(self = None, reason = None):
        '''
        Cancel this scope immediately.

        :param reason: a message describing the reason for the cancellation

        '''
        raise NotImplementedError

    deadline = (lambda self = None: raise NotImplementedError)()
    deadline = (lambda self = None, value = None: raise NotImplementedError)()
    cancel_called = (lambda self = None: raise NotImplementedError)()
    cancelled_caught = (lambda self = None: raise NotImplementedError)()
    shield = (lambda self = None: raise NotImplementedError)()
    shield = (lambda self = None, value = None: raise NotImplementedError)()
    
    def __enter__(self = None):
        raise NotImplementedError

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool')):
        raise NotImplementedError


fail_after = (lambda delay = None, shield = None: pass# WARNING: Decompyle incomplete
)()

def move_on_after(delay = None, shield = None):
    '''
    Create a cancel scope with a deadline that expires after the given delay.

    :param delay: maximum allowed time (in seconds) before exiting the context block, or
        ``None`` to disable the timeout
    :param shield: ``True`` to shield the cancel scope from external cancellation
    :return: a cancel scope

    '''
    pass
# WARNING: Decompyle incomplete


def current_effective_deadline():
    """
    Return the nearest deadline among all the cancel scopes effective for the current
    task.

    :return: a clock value from the event loop's internal clock (or ``float('inf')`` if
        there is no deadline in effect, or ``float('-inf')`` if the current scope has
        been cancelled)
    :rtype: float

    """
    return get_async_backend().current_effective_deadline()


def create_task_group():
    '''
    Create a task group.

    :return: a task group

    '''
    return get_async_backend().create_task_group()
