# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry_base.pyc (Python 3.11)

'''Shared classes and functions for retrying requests.

:class:`_BaseRetry` is the base class for :class:`Retry`,
:class:`AsyncRetry`, :class:`StreamingRetry`, and :class:`AsyncStreamingRetry`.
'''
from __future__ import annotations
import logging
import random
import time
from enum import Enum
from typing import Any, Callable, Optional, Iterator, TYPE_CHECKING
import requests.exceptions as requests
from google.api_core import exceptions
from google.auth import exceptions as auth_exceptions
if TYPE_CHECKING:
    import sys
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self
_DEFAULT_INITIAL_DELAY = 1
_DEFAULT_MAXIMUM_DELAY = 60
_DEFAULT_DELAY_MULTIPLIER = 2
_DEFAULT_DEADLINE = 120
_LOGGER = logging.getLogger('google.api_core.retry')

def if_exception_type(*exception_types):
    '''Creates a predicate to check if the exception is of a given type.

    Args:
        exception_types (Sequence[:func:`type`]): The exception types to check
            for.

    Returns:
        Callable[Exception]: A predicate that returns True if the provided
            exception is of the given type(s).
    '''
    pass
# WARNING: Decompyle incomplete

if_transient_error = if_exception_type(exceptions.InternalServerError, exceptions.TooManyRequests, exceptions.ServiceUnavailable, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, auth_exceptions.TransportError)

def exponential_sleep_generator(initial = None, maximum = None, multiplier = None):
    '''Generates sleep intervals based on the exponential back-off algorithm.

    This implements the `Truncated Exponential Back-off`_ algorithm.

    .. _Truncated Exponential Back-off:
        https://cloud.google.com/storage/docs/exponential-backoff

    Args:
        initial (float): The minimum amount of time to delay. This must
            be greater than 0.
        maximum (float): The maximum amount of time to delay.
        multiplier (float): The multiplier applied to the delay.

    Yields:
        float: successive sleep intervals.
    '''
    pass
# WARNING: Decompyle incomplete


class RetryFailureReason(Enum):
    '''
    The cause of a failed retry, used when building exceptions
    '''
    TIMEOUT = 0
    NON_RETRYABLE_ERROR = 1


def build_retry_error(exc_list = None, reason = None, timeout_val = None, **kwargs):
    '''
    Default exception_factory implementation.

    Returns a RetryError if the failure is due to a timeout, otherwise
    returns the last exception encountered.

    Args:
      - exc_list: list of exceptions that occurred during the retry
      - reason: reason for the retry failure.
            Can be TIMEOUT or NON_RETRYABLE_ERROR
      - timeout_val: the original timeout value for the retry (in seconds), for use in the exception message

    Returns:
      - tuple: a tuple of the exception to be raised, and the cause exception if any
    '''
    pass
# WARNING: Decompyle incomplete


def _retry_error_helper(exc, deadline, sleep_iterator, error_list, predicate_fn = None, on_error_fn = None, exc_factory_fn = None, original_timeout = ('exc', 'Exception', 'deadline', 'float | None', 'sleep_iterator', 'Iterator[float]', 'error_list', 'list[Exception]', 'predicate_fn', 'Callable[[Exception], bool]', 'on_error_fn', 'Callable[[Exception], None] | None', 'exc_factory_fn', 'Callable[[list[Exception], RetryFailureReason, float | None], tuple[Exception, Exception | None]]', 'original_timeout', 'float | None', 'return', 'float')):
    '''
    Shared logic for handling an error for all retry implementations

    - Raises an error on timeout or non-retryable error
    - Calls on_error_fn if provided
    - Logs the error

    Args:
       - exc: the exception that was raised
       - deadline: the deadline for the retry, calculated as a diff from time.monotonic()
       - sleep_iterator: iterator to draw the next backoff value from
       - error_list: the list of exceptions that have been raised so far
       - predicate_fn: takes `exc` and returns true if the operation should be retried
       - on_error_fn: callback to execute when a retryable error occurs
       - exc_factory_fn: callback used to build the exception to be raised on terminal failure
       - original_timeout_val: the original timeout value for the retry (in seconds),
           to be passed to the exception factory for building an error message
    Returns:
        - the sleep value chosen before the next attempt
    '''
    error_list.append(exc)
    if not predicate_fn(exc):
        (final_exc, source_exc) = exc_factory_fn(error_list, RetryFailureReason.NON_RETRYABLE_ERROR, original_timeout)
        raise final_exc, source_exc
# WARNING: Decompyle incomplete


class _BaseRetry(object):
    '''
    Base class for retry configuration objects. This class is intended to capture retry
    and backoff configuration that is common to both synchronous and asynchronous retries,
    for both unary and streaming RPCs. It is not intended to be instantiated directly,
    but rather to be subclassed by the various retry configuration classes.
    '''
    
    def __init__(self, predicate, initial = None, maximum = None, multiplier = None, timeout = (if_transient_error, _DEFAULT_INITIAL_DELAY, _DEFAULT_MAXIMUM_DELAY, _DEFAULT_DELAY_MULTIPLIER, _DEFAULT_DEADLINE, None), on_error = ('predicate', 'Callable[[Exception], bool]', 'initial', 'float', 'maximum', 'float', 'multiplier', 'float', 'timeout', 'Optional[float]', 'on_error', 'Optional[Callable[[Exception], Any]]', 'kwargs', 'Any', 'return', 'None'), **kwargs):
        self._predicate = predicate
        self._initial = initial
        self._multiplier = multiplier
        self._maximum = maximum
        self._timeout = kwargs.get('deadline', timeout)
        self._deadline = self._timeout
        self._on_error = on_error

    
    def __call__(self = None, *args, **kwargs):
        raise NotImplementedError('Not implemented in base class')

    deadline = (lambda self = None: self._timeout)()
    timeout = (lambda self = None: self._timeout)()
    
    def with_deadline(self = None, deadline = None):
        '''Return a copy of this retry with the given timeout.

        DEPRECATED: use :meth:`with_timeout` instead. Refer to the ``Retry`` class
        documentation for details.

        Args:
            deadline (float|None): How long to keep retrying, in seconds. If None,
                no timeout is enforced.

        Returns:
            Retry: A new retry instance with the given timeout.
        '''
        return self.with_timeout(deadline)

    
    def with_timeout(self = None, timeout = None):
        '''Return a copy of this retry with the given timeout.

        Args:
            timeout (float): How long to keep retrying, in seconds. If None,
                no timeout will be enforced.

        Returns:
            Retry: A new retry instance with the given timeout.
        '''
        return type(self)(predicate = self._predicate, initial = self._initial, maximum = self._maximum, multiplier = self._multiplier, timeout = timeout, on_error = self._on_error)

    
    def with_predicate(self = None, predicate = None):
        '''Return a copy of this retry with the given predicate.

        Args:
            predicate (Callable[Exception]): A callable that should return
                ``True`` if the given exception is retryable.

        Returns:
            Retry: A new retry instance with the given predicate.
        '''
        return type(self)(predicate = predicate, initial = self._initial, maximum = self._maximum, multiplier = self._multiplier, timeout = self._timeout, on_error = self._on_error)

    
    def with_delay(self = None, initial = None, maximum = None, multiplier = (None, None, None)):
        '''Return a copy of this retry with the given delay options.

        Args:
            initial (float): The minimum amount of time to delay (in seconds). This must
                be greater than 0. If None, the current value is used.
            maximum (float): The maximum amount of time to delay (in seconds). If None, the
                current value is used.
            multiplier (float): The multiplier applied to the delay. If None, the current
                value is used.

        Returns:
            Retry: A new retry instance with the given delay options.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return '<{} predicate={}, initial={:.1f}, maximum={:.1f}, multiplier={:.1f}, timeout={}, on_error={}>'.format(type(self).__name__, self._predicate, self._initial, self._maximum, self._multiplier, self._timeout, self._on_error)
