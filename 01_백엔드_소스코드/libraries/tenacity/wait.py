# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wait.pyc (Python 3.11)

import abc
import random
import typing
from tenacity import _utils
if typing.TYPE_CHECKING:
    from tenacity import RetryCallState

class wait_base(abc.ABC):
    '''Abstract base class for wait strategies.'''
    __call__ = (lambda self = None, retry_state = None: pass)()
    
    def __add__(self = None, other = None):
        return wait_combine(self, other)

    
    def __radd__(self = None, other = None):
        if other == 0:
            return self
        return None.__add__(other)


WaitBaseT = typing.Union[(wait_base, typing.Callable[([
    'RetryCallState'], typing.Union[(float, int)])])]

class wait_fixed(wait_base):
    '''Wait strategy that waits a fixed amount of time between each retry.'''
    
    def __init__(self = None, wait = None):
        self.wait_fixed = _utils.to_seconds(wait)

    
    def __call__(self = None, retry_state = None):
        return self.wait_fixed



class wait_none(wait_fixed):
    pass
# WARNING: Decompyle incomplete


class wait_random(wait_base):
    '''Wait strategy that waits a random amount of time between min/max.'''
    
    def __init__(self = None, min = None, max = None):
        self.wait_random_min = _utils.to_seconds(min)
        self.wait_random_max = _utils.to_seconds(max)

    
    def __call__(self = None, retry_state = None):
        return self.wait_random_min + random.random() * (self.wait_random_max - self.wait_random_min)



class wait_combine(wait_base):
    '''Combine several waiting strategies.'''
    
    def __init__(self = None, *strategies):
        self.wait_funcs = strategies

    
    def __call__(self = None, retry_state = None):
        pass
    # WARNING: Decompyle incomplete



class wait_chain(wait_base):
    '''Chain two or more waiting strategies.

    If all strategies are exhausted, the very last strategy is used
    thereafter.

    For example::

        @retry(wait=wait_chain(*[wait_fixed(1) for i in range(3)] +
                               [wait_fixed(2) for j in range(5)] +
                               [wait_fixed(5) for k in range(4)))
        def wait_chained():
            print("Wait 1s for 3 attempts, 2s for 5 attempts and 5s
                   thereafter.")
    '''
    
    def __init__(self = None, *strategies):
        self.strategies = strategies

    
    def __call__(self = None, retry_state = None):
        wait_func_no = min(max(retry_state.attempt_number, 1), len(self.strategies))
        wait_func = self.strategies[wait_func_no - 1]
        return wait_func(retry_state = retry_state)



class wait_incrementing(wait_base):
    '''Wait an incremental amount of time after each attempt.

    Starting at a starting value and incrementing by a value for each attempt
    (and restricting the upper limit to some maximum value).
    '''
    
    def __init__(self = None, start = None, increment = None, max = (0, 100, _utils.MAX_WAIT)):
        self.start = _utils.to_seconds(start)
        self.increment = _utils.to_seconds(increment)
        self.max = _utils.to_seconds(max)

    
    def __call__(self = None, retry_state = None):
        result = self.start + self.increment * (retry_state.attempt_number - 1)
        return max(0, min(result, self.max))



class wait_exponential(wait_base):
    '''Wait strategy that applies exponential backoff.

    It allows for a customized multiplier and an ability to restrict the
    upper and lower limits to some maximum and minimum value.

    The intervals are fixed (i.e. there is no jitter), so this strategy is
    suitable for balancing retries against latency when a required resource is
    unavailable for an unknown duration, but *not* suitable for resolving
    contention between multiple processes for a shared resource. Use
    wait_random_exponential for the latter case.
    '''
    
    def __init__(self = None, multiplier = None, max = None, exp_base = (1, _utils.MAX_WAIT, 2, 0), min = ('multiplier', typing.Union[(int, float)], 'max', _utils.time_unit_type, 'exp_base', typing.Union[(int, float)], 'min', _utils.time_unit_type, 'return', None)):
        self.multiplier = multiplier
        self.min = _utils.to_seconds(min)
        self.max = _utils.to_seconds(max)
        self.exp_base = exp_base

    
    def __call__(self = None, retry_state = None):
        
        try:
            exp = self.exp_base ** (retry_state.attempt_number - 1)
            result = self.multiplier * exp
        except OverflowError:
            return 

        return max(max(0, self.min), min(result, self.max))



class wait_random_exponential(wait_exponential):
    pass
# WARNING: Decompyle incomplete


class wait_exponential_jitter(wait_base):
    '''Wait strategy that applies exponential backoff and jitter.

    It allows for a customized initial wait, maximum wait and jitter.

    This implements the strategy described here:
    https://cloud.google.com/storage/docs/retry-strategy

    The wait time is min(initial * 2**n + random.uniform(0, jitter), maximum)
    where n is the retry count.
    '''
    
    def __init__(self = None, initial = None, max = None, exp_base = (1, _utils.MAX_WAIT, 2, 1), jitter = ('initial', float, 'max', float, 'exp_base', float, 'jitter', float, 'return', None)):
        self.initial = initial
        self.max = max
        self.exp_base = exp_base
        self.jitter = jitter

    
    def __call__(self = None, retry_state = None):
        jitter = random.uniform(0, self.jitter)
        
        try:
            exp = self.exp_base ** (retry_state.attempt_number - 1)
            result = self.initial * exp + jitter
        except OverflowError:
            result = self.max

        return max(0, min(result, self.max))
