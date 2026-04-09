# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: future.pyc (Python 3.11)

"""A Future interface.

Python doesn't have a Future interface in its standard library. In the absence
of such a standard, three separate, incompatible implementations
(concurrent.futures.Future, ndb.Future, and asyncio.Future) have appeared. This
interface attempts to be as compatible as possible with
concurrent.futures.Future. From ndb.Future it adopts a traceback-object accessor
method.

Unlike the concrete and implemented Future classes listed above, the Future
class defined in this module is an entirely abstract interface that anyone may
implement and use.

The one known incompatibility between this interface and the interface of
concurrent.futures.Future is that this interface defines its own CancelledError
and TimeoutError exceptions rather than raising the implementation-private
concurrent.futures._base.CancelledError and the
built-in-but-only-in-3.3-and-later TimeoutError.
"""
import abc

class TimeoutError(Exception):
    '''Indicates that a particular call timed out.'''
    pass


class CancelledError(Exception):
    '''Indicates that the computation underlying a Future was cancelled.'''
    pass


class Future(abc.ABC):
    '''A representation of a computation in another control flow.

    Computations represented by a Future may be yet to be begun, may be ongoing,
    or may have already completed.
    '''
    cancel = (lambda self: raise NotImplementedError())()
    cancelled = (lambda self: raise NotImplementedError())()
    running = (lambda self: raise NotImplementedError())()
    done = (lambda self: raise NotImplementedError())()
    result = (lambda self, timeout = (None,): raise NotImplementedError())()
    exception = (lambda self, timeout = (None,): raise NotImplementedError())()
    traceback = (lambda self, timeout = (None,): raise NotImplementedError())()
    add_done_callback = (lambda self, fn: raise NotImplementedError())()
