# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multiproc.pyc (Python 3.11)

'''Monkey-patching to add multiprocessing support for coverage.py'''
from __future__ import annotations
import multiprocessing
import multiprocessing.process as multiprocessing
import os
import os.path as os
import sys
import traceback
from typing import Any
from coverage.debug import DebugControl
PATCHED_MARKER = '_coverage$patched'
OriginalProcess = multiprocessing.process.BaseProcess
original_bootstrap = OriginalProcess._bootstrap

class ProcessWithCoverage(OriginalProcess):
    '''A replacement for multiprocess.Process that starts coverage.'''
    
    def _bootstrap(self, *args, **kwargs):
        '''Wrapper around _bootstrap to start coverage.'''
        debug = None
    # WARNING: Decompyle incomplete



class Stowaway:
    '''An object to pickle, so when it is unpickled, it can apply the monkey-patch.'''
    
    def __init__(self = None, rcfile = None):
        self.rcfile = rcfile

    
    def __getstate__(self = None):
        return {
            'rcfile': self.rcfile }

    
    def __setstate__(self = None, state = None):
        patch_multiprocessing(state['rcfile'])



def patch_multiprocessing(rcfile = None):
    '''Monkey-patch the multiprocessing module.

    This enables coverage measurement of processes started by multiprocessing.
    This involves aggressive monkey-patching.

    `rcfile` is the path to the rcfile being used.

    '''
    pass
# WARNING: Decompyle incomplete
