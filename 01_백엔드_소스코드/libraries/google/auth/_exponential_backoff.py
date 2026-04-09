# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exponential_backoff.pyc (Python 3.11)

import asyncio
import random
import time
from google.auth import exceptions
_DEFAULT_RETRY_TOTAL_ATTEMPTS = 3
_DEFAULT_INITIAL_INTERVAL_SECONDS = 1
_DEFAULT_RANDOMIZATION_FACTOR = 0.1
_DEFAULT_MULTIPLIER = 2

class _BaseExponentialBackoff:
    '''An exponential backoff iterator base class.

    Args:
        total_attempts Optional[int]:
            The maximum amount of retries that should happen.
            The default value is 3 attempts.
        initial_wait_seconds Optional[int]:
            The amount of time to sleep in the first backoff. This parameter
            should be in seconds.
            The default value is 1 second.
        randomization_factor Optional[float]:
            The amount of jitter that should be in each backoff. For example,
            a value of 0.1 will introduce a jitter range of 10% to the
            current backoff period.
            The default value is 0.1.
        multiplier Optional[float]:
            The backoff multipler. This adjusts how much each backoff will
            increase. For example a value of 2.0 leads to a 200% backoff
            on each attempt. If the initial_wait is 1.0 it would look like
            this sequence [1.0, 2.0, 4.0, 8.0].
            The default value is 2.0.
    '''
    
    def __init__(self, total_attempts, initial_wait_seconds, randomization_factor, multiplier = (_DEFAULT_RETRY_TOTAL_ATTEMPTS, _DEFAULT_INITIAL_INTERVAL_SECONDS, _DEFAULT_RANDOMIZATION_FACTOR, _DEFAULT_MULTIPLIER)):
        if total_attempts < 1:
            raise exceptions.InvalidValue(f'''total_attempts must be greater than or equal to 1 but was {total_attempts}''')
        self._total_attempts = total_attempts
        self._initial_wait_seconds = initial_wait_seconds
        self._current_wait_in_seconds = self._initial_wait_seconds
        self._randomization_factor = randomization_factor
        self._multiplier = multiplier
        self._backoff_count = 0

    total_attempts = (lambda self: self._total_attempts)()
    backoff_count = (lambda self: self._backoff_count)()
    
    def _reset(self):
        self._backoff_count = 0
        self._current_wait_in_seconds = self._initial_wait_seconds

    
    def _calculate_jitter(self):
        jitter_variance = self._current_wait_in_seconds * self._randomization_factor
        jitter = random.uniform(self._current_wait_in_seconds - jitter_variance, self._current_wait_in_seconds + jitter_variance)
        return jitter



class ExponentialBackoff(_BaseExponentialBackoff):
    pass
# WARNING: Decompyle incomplete


class AsyncExponentialBackoff(_BaseExponentialBackoff):
    pass
# WARNING: Decompyle incomplete
