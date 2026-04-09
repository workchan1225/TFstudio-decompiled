# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nap.pyc (Python 3.11)

import time
import typing
if typing.TYPE_CHECKING:
    import threading

def sleep(seconds = None):
    '''
    Sleep strategy that delays execution for a given number of seconds.

    This is the default strategy, and may be mocked out for unit testing.
    '''
    time.sleep(seconds)


class sleep_using_event:
    '''Sleep strategy that waits on an event to be set.'''
    
    def __init__(self = None, event = None):
        self.event = event

    
    def __call__(self = None, timeout = None):
        self.event.wait(timeout = timeout)
