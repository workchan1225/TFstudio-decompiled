# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: from_thread.pyc (Python 3.11)

'''
This namespace represents special functions that can call back into Trio from
an external thread by means of a Trio Token present in Thread Local Storage
'''
from _threads import from_thread_check_cancelled as check_cancelled, from_thread_run as run, from_thread_run_sync as run_sync
__all__ = [
    'check_cancelled',
    'run',
    'run_sync']
