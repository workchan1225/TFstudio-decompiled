# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
from multiprocessing import synchronize
from context import get_context

def _make_name():
    return f'''/loky-{os.getpid()}-{next(synchronize.SemLock._rand)}'''

synchronize.SemLock._make_name = staticmethod(_make_name)
__all__ = [
    'get_context']
