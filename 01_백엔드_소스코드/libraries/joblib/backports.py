# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backports.pyc (Python 3.11)

'''
Backports of fixes for joblib dependencies
'''
import os
import re
import time
from multiprocessing import util
from os.path import basename

class Version:
    '''Backport from deprecated distutils

    We maintain this backport to avoid introducing a new dependency on
    `packaging`.

    We might rexplore this choice in the future if all major Python projects
    introduce a dependency on packaging anyway.
    '''
    
    def __init__(self, vstring = (None,)):
        if vstring:
            self.parse(vstring)
            return None

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s} (\'{str(self)!s}\')'''

    
    def __eq__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return None == 0

    
    def __lt__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return None < 0

    
    def __le__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return None <= 0

    
    def __gt__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return None > 0

    
    def __ge__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return None >= 0



class LooseVersion(Version):
    '''Backport from deprecated distutils

    We maintain this backport to avoid introducing a new dependency on
    `packaging`.

    We might rexplore this choice in the future if all major Python projects
    introduce a dependency on packaging anyway.
    '''
    component_re = re.compile('(\\d+ | [a-z]+ | \\.)', re.VERBOSE)
    
    def __init__(self, vstring = (None,)):
        if vstring:
            self.parse(vstring)
            return None

    
    def parse(self, vstring):
        self.vstring = vstring
        components = self.component_re.split(vstring)()
        for i, obj in enumerate(components):
            components[i] = int(obj)
            except ValueError:
                continue
            self.version = components
            return None

    
    def __str__(self):
        return self.vstring

    
    def __repr__(self):
        return "LooseVersion ('%s')" % str(self)

    
    def _cmp(self, other):
        if isinstance(other, str):
            other = LooseVersion(other)
        elif not isinstance(other, LooseVersion):
            return NotImplemented
        if self.version == other.version:
            return 0
        if None.version < other.version:
            return -1
        if None.version > other.version:
            return 1



try:
    import numpy as np
    
    def make_memmap(filename, dtype, mode, offset, shape, order, unlink_on_gc_collect = ('uint8', 'r+', 0, None, 'C', False)):
        '''Custom memmap constructor compatible with numpy.memmap.

        This function:
        - is a backport the numpy memmap offset fix (See
          https://github.com/numpy/numpy/pull/8443 for more details.
          The numpy fix is available starting numpy 1.13)
        - adds ``unlink_on_gc_collect``, which specifies  explicitly whether
          the process re-constructing the memmap owns a reference to the
          underlying file. If set to True, it adds a finalizer to the
          newly-created memmap that sends a maybe_unlink request for the
          memmaped file to resource_tracker.
        '''
        util.debug('[MEMMAP READ] creating a memmap (shape {}, filename {}, pid {})'.format(shape, basename(filename), os.getpid()))
        mm = np.memmap(filename, dtype = dtype, mode = mode, offset = offset, shape = shape, order = order)
        if LooseVersion(np.__version__) < '1.13':
            mm.offset = offset
        if unlink_on_gc_collect:
            add_maybe_unlink_finalizer = add_maybe_unlink_finalizer
            import _memmapping_reducer
            add_maybe_unlink_finalizer(mm)
        return mm

except ImportError:
    
    def make_memmap(filename, dtype, mode, offset, shape, order, unlink_on_gc_collect = ('uint8', 'r+', 0, None, 'C', False)):
        raise NotImplementedError("'joblib.backports.make_memmap' should not be used if numpy is not installed.")


if os.name == 'nt':
    access_denied_errors = (5, 13)
    from os import replace
    
    def concurrency_safe_rename(src, dst):
        '''Renames ``src`` into ``dst`` overwriting ``dst`` if it exists.

        On Windows os.replace can yield permission errors if executed by two
        different processes.
        '''
        max_sleep_time = 1
        total_sleep_time = 0
        sleep_time = 0.001
    # WARNING: Decompyle incomplete

    return None
from os import replace as concurrency_safe_rename
