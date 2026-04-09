# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler_lock.pyc (Python 3.11)

import threading
import functools

event
<NODE:12> = None
global_compiler_lock = _CompilerLock()

def require_global_compiler_lock():
    '''Sentry that checks the global_compiler_lock is acquired.
    '''
    pass
# WARNING: Decompyle incomplete
