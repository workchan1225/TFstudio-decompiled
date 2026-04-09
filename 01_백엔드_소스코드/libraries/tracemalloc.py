# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tracemalloc.pyc (Python 3.11)

from collections.abc import Sequence, Iterable
from functools import total_ordering
import fnmatch
import linecache
import os.path as os
import pickle
from _tracemalloc import *
from _tracemalloc import _get_object_traceback, _get_traces

def _format_size(size, sign):
    for unit in ('B', 'KiB', 'MiB', 'GiB', 'TiB'):
        if abs(size) < 100 and unit != 'B':
            if sign:
                
                return None, '%+.1f %s' % (size, unit)
            
            return None, None % (size, unit)
        if None(size) < 10240 or unit == 'TiB':
            if sign:
                
                return None, '%+.0f %s' % (size, unit)
            
            return None, None % (size, unit)
        return None


class Statistic:
    '''
    Statistic difference on memory allocations between two Snapshot instance.
    '''
    __slots__ = ('traceback', 'size', 'count')
    
    def __init__(self, traceback, size, count):
        self.traceback = traceback
        self.size = size
        self.count = count

    
    def __hash__(self):
        return hash((self.traceback, self.size, self.count))

    
    def __eq__(self, other):
