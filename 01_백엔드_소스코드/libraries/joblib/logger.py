# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

'''
Helpers for logging.

This module needs much love to become useful.
'''
from __future__ import print_function
import logging
import os
import pprint
import shutil
import sys
import time
from disk import mkdirp

def _squeeze_time(t):
    '''Remove .1s to the time under Windows: this is the time it take to
    stat files. This is needed to make results similar to timings under
    Unix, for tests
    '''
    if sys.platform.startswith('win'):
        return max(0, t - 0.1)


def format_time(t):
    t = _squeeze_time(t)
    return '%.1fs, %.1fmin' % (t, t / 60)


def short_format_time(t):
    t = _squeeze_time(t)
    if t > 60:
        return '%4.1fmin' % t / 60
    return None % t


def pformat(obj, indent, depth = (0, 3)):
    if 'numpy' in sys.modules:
        import numpy as np
        print_options = np.get_printoptions()
        np.set_printoptions(precision = 6, threshold = 64, edgeitems = 1)
    else:
        print_options = None
    out = pprint.pformat(obj, depth = depth, indent = indent)
# WARNING: Decompyle incomplete


class Logger(object):
    '''Base class for logging messages.'''
    
    def __init__(self, depth, name = (3, None)):
        '''
        Parameters
        ----------
        depth: int, optional
            The depth of objects printed.
        name: str, optional
            The namespace to log to. If None, defaults to joblib.
        '''
        self.depth = depth
        self._name = name if name else 'joblib'

    
    def warn(self, msg):
        logging.getLogger(self._name).warning(f'''[{self!s}]: {msg!s}''')

    
    def info(self, msg):
        logging.info(f'''[{self!s}]: {msg!s}''')

    
    def debug(self, msg):
        logging.getLogger(self._name).debug(f'''[{self!s}]: {msg!s}''')

    
    def format(self, obj, indent = (0,)):
        '''Return the formatted representation of the object.'''
        return pformat(obj, indent = indent, depth = self.depth)



class PrintTime(object):
    '''Print and log messages while keeping track of time.'''
    
    def __init__(self, logfile, logdir = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, msg, total = ('', False)):
        '''Print the time elapsed between the last call and the current
        call, with an optional message.
        '''
        if not total:
            time_lapse = time.time() - self.last_time
            full_msg = f'''{msg!s}: {format_time(time_lapse)!s}'''
        else:
            time_lapse = time.time() - self.start_time
            full_msg = '%s: %.2fs, %.1f min' % (msg, time_lapse, time_lapse / 60)
        print(full_msg, file = sys.stderr)
    # WARNING: Decompyle incomplete
