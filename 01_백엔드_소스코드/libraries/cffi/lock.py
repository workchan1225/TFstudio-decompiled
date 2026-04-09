# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lock.pyc (Python 3.11)

import sys
if sys.version_info < (3,):
    
    try:
        from thread import allocate_lock
        return None
    except ImportError:
        from dummy_thread import allocate_lock
        return None
        
        try:
            from _thread import allocate_lock
            return None
        except ImportError:
            from _dummy_thread import allocate_lock
            return None
