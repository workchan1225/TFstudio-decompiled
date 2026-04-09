# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stop.pyc (Python 3.11)

import abc
import typing
from tenacity import _utils
if typing.TYPE_CHECKING:
    import threading
    from tenacity import RetryCallState

class stop_base(abc.ABC):
    '''Abstract base class for stop strategies.'''
    __call__ = (lambda self = None, retry_state = None: pass)()
    
    def __and__(self = None, other = None):
        return stop_all(self, other)

    
    def __or__(self = None, other = None):
        return stop_any(self, other)


StopBaseT = typing.Union[(stop_base, typing.Callable[([
    'RetryCallState'], bool)])]

class stop_any(stop_base):
    '''Stop if any of the stop condition is valid.'''
    
    def __init__(self = None, *stops):
        self.stops = stops

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class stop_all(stop_base):
    '''Stop if all the stop conditions are valid.'''
    
    def __init__(self = None, *stops):
        self.stops = stops

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class _stop_never(stop_base):
    '''Never stop.'''
    
    def __call__(self = None, retry_state = None):
        return False


stop_never = _stop_never()

class stop_when_event_set(stop_base):
    '''Stop when the given event is set.'''
    
    def __init__(self = None, event = None):
        self.event = event

    
    def __call__(self = None, retry_state = None):
        return self.event.is_set()



class stop_after_attempt(stop_base):
    '''Stop when the previous attempt >= max_attempt.'''
    
    def __init__(self = None, max_attempt_number = None):
        self.max_attempt_number = max_attempt_number

    
    def __call__(self = None, retry_state = None):
        return retry_state.attempt_number >= self.max_attempt_number



class stop_after_delay(stop_base):
    '''
    Stop when the time from the first attempt >= limit.

    Note: `max_delay` will be exceeded, so when used with a `wait`, the actual total delay will be greater
    than `max_delay` by some of the final sleep period before `max_delay` is exceeded.

    If you need stricter timing with waits, consider `stop_before_delay` instead.
    '''
    
    def __init__(self = None, max_delay = None):
        self.max_delay = _utils.to_seconds(max_delay)

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class stop_before_delay(stop_base):
    '''
    Stop right before the next attempt would take place after the time from the first attempt >= limit.

    Most useful when you are using with a `wait` function like wait_random_exponential, but need to make
    sure that the max_delay is not exceeded.
    '''
    
    def __init__(self = None, max_delay = None):
        self.max_delay = _utils.to_seconds(max_delay)

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete
