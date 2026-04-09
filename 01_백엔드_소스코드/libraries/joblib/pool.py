# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pool.pyc (Python 3.11)

'''Custom implementation of multiprocessing.Pool with custom pickler.

This module provides efficient ways of working with data stored in
shared memory with numpy.memmap arrays without inducing any memory
copy between the parent and child processes.

This module should not be imported if multiprocessing is not
available as it implements subclasses of multiprocessing Pool
that uses a custom alternative to SimpleQueue.

'''
import copyreg
import sys
import warnings
from time import sleep

try:
    WindowsError
except NameError:
    WindowsError = type(None)

from io import BytesIO
from multiprocessing.pool import Pool
from pickle import HIGHEST_PROTOCOL, Pickler
from _memmapping_reducer import TemporaryResourcesManager, get_memmapping_reducers
from _multiprocessing_helpers import assert_spawning, mp

try:
    import numpy as np
except ImportError:
    np = None


class CustomizablePickler(Pickler):
    '''Pickler that accepts custom reducers.

    TODO python2_drop : can this be simplified ?

    HIGHEST_PROTOCOL is selected by default as this pickler is used
    to pickle ephemeral datastructures for interprocess communication
    hence no backward compatibility is required.

    `reducers` is expected to be a dictionary with key/values
    being `(type, callable)` pairs where `callable` is a function that
    give an instance of `type` will return a tuple `(constructor,
    tuple_of_objects)` to rebuild an instance out of the pickled
    `tuple_of_objects` as would return a `__reduce__` method. See the
    standard library documentation on pickling for more details.

    '''
    
    def __init__(self, writer, reducers, protocol = (None, HIGHEST_PROTOCOL)):
        Pickler.__init__(self, writer, protocol = protocol)
    # WARNING: Decompyle incomplete

    
    def register(self, type, reduce_func):
        '''Attach a reducer function to a given type in the dispatch table.'''
        pass
    # WARNING: Decompyle incomplete



class CustomizablePicklingQueue(object):
    '''Locked Pipe implementation that uses a customizable pickler.

    This class is an alternative to the multiprocessing implementation
    of SimpleQueue in order to make it possible to pass custom
    pickling reducers, for instance to avoid memory copy when passing
    memory mapped datastructures.

    `reducers` is expected to be a dict with key / values being
    `(type, callable)` pairs where `callable` is a function that, given an
    instance of `type`, will return a tuple `(constructor, tuple_of_objects)`
    to rebuild an instance out of the pickled `tuple_of_objects` as would
    return a `__reduce__` method.

    See the standard library documentation on pickling for more details.
    '''
    
    def __init__(self, context, reducers = (None,)):
        self._reducers = reducers
        (self._reader, self._writer) = context.Pipe(duplex = False)
        self._rlock = context.Lock()
        if sys.platform == 'win32':
            self._wlock = None
        else:
            self._wlock = context.Lock()
        self._make_methods()

    
    def __getstate__(self):
        assert_spawning(self)
        return (self._reader, self._writer, self._rlock, self._wlock, self._reducers)

    
    def __setstate__(self, state):
        (self._reader, self._writer, self._rlock, self._wlock, self._reducers) = state
        self._make_methods()

    
    def empty(self):
        return not self._reader.poll()

    
    def _make_methods(self):
        pass
    # WARNING: Decompyle incomplete



class PicklingPool(Pool):
    pass
# WARNING: Decompyle incomplete


class MemmappingPool(PicklingPool):
    pass
# WARNING: Decompyle incomplete
