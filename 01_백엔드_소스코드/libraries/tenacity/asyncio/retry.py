# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry.pyc (Python 3.11)

import abc
import typing
from tenacity import _utils
from tenacity import retry_base
if typing.TYPE_CHECKING:
    from tenacity import RetryCallState

class async_retry_base(retry_base):
    '''Abstract base class for async retry strategies.'''
    __call__ = (lambda self = None, retry_state = None: pass# WARNING: Decompyle incomplete
)()
    
    def __and__(self = None, other = None):
        return retry_all(self, other)

    
    def __rand__(self = None, other = None):
        return retry_all(other, self)

    
    def __or__(self = None, other = None):
        return retry_any(self, other)

    
    def __ror__(self = None, other = None):
        return retry_any(other, self)


RetryBaseT = typing.Union[(async_retry_base, typing.Callable[([
    'RetryCallState'], typing.Awaitable[bool])])]

class retry_if_exception(async_retry_base):
    '''Retry strategy that retries if an exception verifies a predicate.'''
    
    def __init__(self = None, predicate = None):
        self.predicate = predicate

    
    async def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_if_result(async_retry_base):
    '''Retries if the result verifies a predicate.'''
    
    def __init__(self = None, predicate = None):
        self.predicate = predicate

    
    async def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_any(async_retry_base):
    '''Retries if any of the retries condition is valid.'''
    
    def __init__(self = None, *retries):
        self.retries = retries

    
    async def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_all(async_retry_base):
    '''Retries if all the retries condition are valid.'''
    
    def __init__(self = None, *retries):
        self.retries = retries

    
    async def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete
