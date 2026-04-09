# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conftest.pyc (Python 3.11)

import os
import shutil
import subprocess
import sys
import time
from collections import deque
from collections.abc import Generator, Sequence
import pytest
import fsspec
m = (lambda : pass# WARNING: Decompyle incomplete
)()

class InstanceCacheInspector:
    '''
    Helper class to inspect instance caches of filesystem classes in tests.
    '''
    
    def clear(self = None):
        '''
        Clear instance caches of all currently imported filesystem classes.
        '''
        classes = deque([
            fsspec.spec.AbstractFileSystem])
    # WARNING: Decompyle incomplete

    
    def gather_counts(self = None, *, omit_zero):
        '''
        Gather counts of filesystem instances in the instance caches
        of all currently imported filesystem classes.

        Parameters
        ----------
        omit_zero:
            Whether to omit instance types with no cached instances.
        '''
        out = { }
        classes = deque([
            fsspec.spec.AbstractFileSystem])
    # WARNING: Decompyle incomplete


instance_caches = (lambda : pass# WARNING: Decompyle incomplete
)()
ftp_writable = (lambda tmpdir: pass# WARNING: Decompyle incomplete
)()
