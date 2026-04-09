# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polling.pyc (Python 3.11)

'''Abstract and helper bases for Future implementations.'''
import abc
import concurrent.futures as concurrent
from google.api_core import exceptions
from google.api_core import retry as retries
from google.api_core.future import _helpers
from google.api_core.future import base

class _OperationNotComplete(Exception):
    '''Private exception used for polling via retry.'''
    pass

RETRY_PREDICATE = retries.if_exception_type(_OperationNotComplete, exceptions.TooManyRequests, exceptions.InternalServerError, exceptions.BadGateway, exceptions.ServiceUnavailable)
DEFAULT_RETRY = retries.Retry(predicate = RETRY_PREDICATE)
POLLING_PREDICATE = retries.if_exception_type(_OperationNotComplete)
DEFAULT_POLLING = retries.Retry(predicate = POLLING_PREDICATE, initial = 1, maximum = 20, multiplier = 1.5, timeout = 900)

class PollingFuture(base.Future):
    pass
# WARNING: Decompyle incomplete
