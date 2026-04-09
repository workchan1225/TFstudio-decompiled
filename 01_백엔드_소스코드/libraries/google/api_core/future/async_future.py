# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_future.pyc (Python 3.11)

'''AsyncIO implementation of the abstract base Future class.'''
import asyncio
from google.api_core import exceptions
from google.api_core import retry
from google.api_core import retry_async
from google.api_core.future import base

class _OperationNotComplete(Exception):
    '''Private exception used for polling via retry.'''
    pass

RETRY_PREDICATE = retry.if_exception_type(_OperationNotComplete, exceptions.TooManyRequests, exceptions.InternalServerError, exceptions.BadGateway)
DEFAULT_RETRY = retry_async.AsyncRetry(predicate = RETRY_PREDICATE)

class AsyncFuture(base.Future):
    pass
# WARNING: Decompyle incomplete
