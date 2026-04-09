# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry.pyc (Python 3.11)

import abc
import re
import typing
if typing.TYPE_CHECKING:
    from tenacity import RetryCallState

class retry_base(abc.ABC):
    '''Abstract base class for retry strategies.'''
    __call__ = (lambda self = None, retry_state = None: pass)()
    
    def __and__(self = None, other = None):
        return other.__rand__(self)

    
    def __rand__(self = None, other = None):
        return retry_all(other, self)

    
    def __or__(self = None, other = None):
        return other.__ror__(self)

    
    def __ror__(self = None, other = None):
        return retry_any(other, self)


RetryBaseT = typing.Union[(retry_base, typing.Callable[([
    'RetryCallState'], bool)])]

class _retry_never(retry_base):
    '''Retry strategy that never rejects any result.'''
    
    def __call__(self = None, retry_state = None):
        return False


retry_never = _retry_never()

class _retry_always(retry_base):
    '''Retry strategy that always rejects any result.'''
    
    def __call__(self = None, retry_state = None):
        return True


retry_always = _retry_always()

class retry_if_exception(retry_base):
    '''Retry strategy that retries if an exception verifies a predicate.'''
    
    def __init__(self = None, predicate = None):
        self.predicate = predicate

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_if_exception_type(retry_if_exception):
    pass
# WARNING: Decompyle incomplete


class retry_if_not_exception_type(retry_if_exception):
    pass
# WARNING: Decompyle incomplete


class retry_unless_exception_type(retry_if_exception):
    pass
# WARNING: Decompyle incomplete


class retry_if_exception_cause_type(retry_base):
    '''Retries if any of the causes of the raised exception is of one or more types.

    The check on the type of the cause of the exception is done recursively (until finding
    an exception in the chain that has no `__cause__`)
    '''
    
    def __init__(self = None, exception_types = None):
        self.exception_cause_types = exception_types

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_if_result(retry_base):
    '''Retries if the result verifies a predicate.'''
    
    def __init__(self = None, predicate = None):
        self.predicate = predicate

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_if_not_result(retry_base):
    '''Retries if the result refutes a predicate.'''
    
    def __init__(self = None, predicate = None):
        self.predicate = predicate

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_if_exception_message(retry_if_exception):
    pass
# WARNING: Decompyle incomplete


class retry_if_not_exception_message(retry_if_exception_message):
    pass
# WARNING: Decompyle incomplete


class retry_any(retry_base):
    '''Retries if any of the retries condition is valid.'''
    
    def __init__(self = None, *retries):
        self.retries = retries

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class retry_all(retry_base):
    '''Retries if all the retries condition are valid.'''
    
    def __init__(self = None, *retries):
        self.retries = retries

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete
