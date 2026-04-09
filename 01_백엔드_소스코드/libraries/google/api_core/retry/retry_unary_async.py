# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry_unary_async.pyc (Python 3.11)

'''Helpers for retrying coroutine functions with exponential back-off.

The :class:`AsyncRetry` decorator shares most functionality and behavior with
:class:`Retry`, but supports coroutine functions. Please refer to description
of :class:`Retry` for more details.

By default, this decorator will retry transient
API errors (see :func:`if_transient_error`). For example:

.. code-block:: python

    @retry_async.AsyncRetry()
    async def call_flaky_rpc():
        return await client.flaky_rpc()

    # Will retry flaky_rpc() if it raises transient API errors.
    result = await call_flaky_rpc()

You can pass a custom predicate to retry on different exceptions, such as
waiting for an eventually consistent item to be available:

.. code-block:: python

    @retry_async.AsyncRetry(predicate=retry_async.if_exception_type(exceptions.NotFound))
    async def check_if_exists():
        return await client.does_thing_exist()

    is_available = await check_if_exists()

Some client library methods apply retry automatically. These methods can accept
a ``retry`` parameter that allows you to configure the behavior:

.. code-block:: python

    my_retry = retry_async.AsyncRetry(timeout=60)
    result = await client.some_method(retry=my_retry)

'''
from __future__ import annotations
import asyncio
import time
import functools
from typing import Awaitable, Any, Callable, Iterable, TypeVar, TYPE_CHECKING
from google.api_core.retry.retry_base import _BaseRetry
from google.api_core.retry.retry_base import _retry_error_helper
from google.api_core.retry.retry_base import exponential_sleep_generator
from google.api_core.retry.retry_base import build_retry_error
from google.api_core.retry.retry_base import RetryFailureReason
from google.api_core.retry.retry_base import if_exception_type
from google.api_core.retry.retry_base import if_transient_error
if TYPE_CHECKING:
    import sys
    if sys.version_info >= (3, 10):
        from typing import ParamSpec
    else:
        from typing_extensions import ParamSpec
    _P = ParamSpec('_P')
    _R = TypeVar('_R')
_DEFAULT_INITIAL_DELAY = 1
_DEFAULT_MAXIMUM_DELAY = 60
_DEFAULT_DELAY_MULTIPLIER = 2
_DEFAULT_DEADLINE = 120
_DEFAULT_TIMEOUT = 120

async def retry_target(target, predicate = None, sleep_generator = None, timeout = None, on_error = (None, None, build_retry_error), exception_factory = ('target', 'Callable[[], Awaitable[_R]]', 'predicate', 'Callable[[Exception], bool]', 'sleep_generator', 'Iterable[float]', 'timeout', 'float | None', 'on_error', 'Callable[[Exception], None] | None', 'exception_factory', 'Callable[[list[Exception], RetryFailureReason, float | None], tuple[Exception, Exception | None]]'), **kwargs):
    """Await a coroutine and retry if it fails.

    This is the lowest-level retry helper. Generally, you'll use the
    higher-level retry helper :class:`Retry`.

    Args:
        target(Callable[[], Any]): The function to call and retry. This must be a
            nullary function - apply arguments with `functools.partial`.
        predicate (Callable[Exception]): A callable used to determine if an
            exception raised by the target should be considered retryable.
            It should return True to retry or False otherwise.
        sleep_generator (Iterable[float]): An infinite iterator that determines
            how long to sleep between retries.
        timeout (Optional[float]): How long to keep retrying the target, in seconds.
            Note: timeout is only checked before initiating a retry, so the target may
            run past the timeout value as long as it is healthy.
        on_error (Optional[Callable[Exception]]): If given, the on_error
            callback will be called with each retryable exception raised by the
            target. Any error raised by this function will *not* be caught.
        exception_factory: A function that is called when the retryable reaches
            a terminal failure state, used to construct an exception to be raised.
            It takes a list of all exceptions encountered, a retry.RetryFailureReason
            enum indicating the failure cause, and the original timeout value
            as arguments. It should return a tuple of the exception to be raised,
            along with the cause exception if any. The default implementation will raise
            a RetryError on timeout, or the last exception encountered otherwise.
        deadline (float): DEPRECATED use ``timeout`` instead. For backward
            compatibility, if set it will override the ``timeout`` parameter.

    Returns:
        Any: the return value of the target function.

    Raises:
        ValueError: If the sleep generator stops yielding values.
        Exception: a custom exception specified by the exception_factory if provided.
            If no exception_factory is provided:
                google.api_core.RetryError: If the timeout is exceeded while retrying.
                Exception: If the target raises an error that isn't retryable.
    """
    pass
# WARNING: Decompyle incomplete


class AsyncRetry(_BaseRetry):
    '''Exponential retry decorator for async coroutines.

    This class is a decorator used to add exponential back-off retry behavior
    to an RPC call.

    Although the default behavior is to retry transient API errors, a
    different predicate can be provided to retry other exceptions.

    Args:
        predicate (Callable[Exception]): A callable that should return ``True``
            if the given exception is retryable.
        initial (float): The minimum amount of time to delay in seconds. This
            must be greater than 0.
        maximum (float): The maximum amount of time to delay in seconds.
        multiplier (float): The multiplier applied to the delay.
        timeout (Optional[float]): How long to keep retrying in seconds.
            Note: timeout is only checked before initiating a retry, so the target may
            run past the timeout value as long as it is healthy.
        on_error (Optional[Callable[Exception]]): A function to call while processing
            a retryable exception. Any error raised by this function will
            *not* be caught.
        deadline (float): DEPRECATED use ``timeout`` instead. If set it will
        override ``timeout`` parameter.
    '''
    
    def __call__(self = None, func = None, on_error = None):
        '''Wrap a callable with retry behavior.

        Args:
            func (Callable): The callable or stream to add retry behavior to.
            on_error (Optional[Callable[Exception]]): If given, the
                on_error callback will be called with each retryable exception
                raised by the wrapped function. Any error raised by this
                function will *not* be caught. If on_error was specified in the
                constructor, this value will be ignored.

        Returns:
            Callable: A callable that will invoke ``func`` with retry
                behavior.
        '''
        pass
    # WARNING: Decompyle incomplete
