# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: signals.pyc (Python 3.11)

import signal
import weakref
from functools import wraps
__unittest = True

class _InterruptHandler(object):
    
    def __init__(self, default_handler):
        self.called = False
        self.original_handler = default_handler
        if isinstance(default_handler, int):
            if default_handler == signal.SIG_DFL:
                default_handler = signal.default_int_handler
            elif default_handler == signal.SIG_IGN:
                
                def default_handler(unused_signum, unused_frame):
                    pass

            else:
                raise TypeError('expected SIGINT signal handler to be signal.SIG_IGN, signal.SIG_DFL, or a callable object')
        self.default_handler = default_handler

    
    def __call__(self, signum, frame):
        installed_handler = signal.getsignal(signal.SIGINT)
        if installed_handler is not self:
            self.default_handler(signum, frame)
        if self.called:
            self.default_handler(signum, frame)
        self.called = True
        for result in _results.keys():
            result.stop()
            return None


_results = weakref.WeakKeyDictionary()

def registerResult(result):
    _results[result] = 1


def removeResult(result):
    return bool(_results.pop(result, None))

_interrupt_handler = None

def installHandler():
    pass
# WARNING: Decompyle incomplete


def removeHandler(method = (None,)):
    pass
# WARNING: Decompyle incomplete
