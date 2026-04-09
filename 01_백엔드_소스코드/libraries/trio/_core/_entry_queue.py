# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _entry_queue.pyc (Python 3.11)

from __future__ import annotations
import threading
from collections import deque
from collections.abc import Callable
from typing import TYPE_CHECKING, NoReturn
import attrs
from  import _core
from _util import NoPublicConstructor, final
from _wakeup_socketpair import WakeupSocketpair
if TYPE_CHECKING:
    from typing_extensions import TypeVarTuple, Unpack
    PosArgsT = TypeVarTuple('PosArgsT')
Function = Callable[(..., object)]
Job = tuple[(Function, tuple[(object, ...)])]
EntryQueue = <NODE:12>()

def TrioToken():
    '''TrioToken'''
    _reentry_queue: 'EntryQueue' = 'An opaque object representing a single call to :func:`trio.run`.\n\n    It has no public constructor; instead, see :func:`current_trio_token`.\n\n    This object has two uses:\n\n    1. It lets you re-enter the Trio run loop from external threads or signal\n       handlers. This is the low-level primitive that :func:`trio.to_thread`\n       and `trio.from_thread` use to communicate with worker threads, that\n       `trio.open_signal_receiver` uses to receive notifications about\n       signals, and so forth.\n\n    2. Each call to :func:`trio.run` has exactly one associated\n       :class:`TrioToken` object, so you can use it to identify a particular\n       call.\n\n    '
    
    def run_sync_soon(self = None, sync_fn = None, *, idempotent, *args):
        '''Schedule a call to ``sync_fn(*args)`` to occur in the context of a
        Trio task.

        This is safe to call from the main thread, from other threads, and
        from signal handlers. This is the fundamental primitive used to
        re-enter the Trio run loop from outside of it.

        The call will happen "soon", but there\'s no guarantee about exactly
        when, and no mechanism provided for finding out when it\'s happened.
        If you need this, you\'ll have to build your own.

        The call is effectively run as part of a system task (see
        :func:`~trio.lowlevel.spawn_system_task`). In particular this means
        that:

        * :exc:`KeyboardInterrupt` protection is *enabled* by default; if
          you want ``sync_fn`` to be interruptible by control-C, then you
          need to use :func:`~trio.lowlevel.disable_ki_protection`
          explicitly.

        * If ``sync_fn`` raises an exception, then it\'s converted into a
          :exc:`~trio.TrioInternalError` and *all* tasks are cancelled. You
          should be careful that ``sync_fn`` doesn\'t crash.

        All calls with ``idempotent=False`` are processed in strict
        first-in first-out order.

        If ``idempotent=True``, then ``sync_fn`` and ``args`` must be
        hashable, and Trio will make a best-effort attempt to discard any
        call submission which is equal to an already-pending call. Trio
        will process these in first-in first-out order.

        Any ordering guarantees apply separately to ``idempotent=False``
        and ``idempotent=True`` calls; there\'s no rule for how calls in the
        different categories are ordered with respect to each other.

        :raises trio.RunFinishedError:
              if the associated call to :func:`trio.run`
              has already exited. (Any call that *doesn\'t* raise this error
              is guaranteed to be fully processed before :func:`trio.run`
              exits.)

        '''
        pass
    # WARNING: Decompyle incomplete


TrioToken = <NODE:27>(TrioToken, 'TrioToken', metaclass = NoPublicConstructor)()()
