# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _memmapping_reducer.pyc (Python 3.11)

'''
Reducer using memory mapping for numpy arrays
'''
import atexit
import errno
import os
import stat
import tempfile
import threading
import time
import warnings
import weakref
from mmap import mmap
from multiprocessing import util
from pickle import HIGHEST_PROTOCOL, PicklingError, dumps, loads, whichmodule
from uuid import uuid4

try:
    WindowsError
except NameError:
    WindowsError = type(None)


try:
    import numpy as np
    from numpy.lib.stride_tricks import as_strided
except ImportError:
    np = None

from backports import make_memmap
from disk import delete_folder
from externals.loky.backend import resource_tracker
from numpy_pickle import dump, load, load_temporary_memmap
SYSTEM_SHARED_MEM_FS = '/dev/shm'
SYSTEM_SHARED_MEM_FS_MIN_SIZE = int(2e+09)
FOLDER_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
FILE_PERMISSIONS = stat.S_IRUSR | stat.S_IWUSR
JOBLIB_MMAPS = set()

def _log_and_unlink(filename):
    _resource_tracker = _resource_tracker
    import externals.loky.backend.resource_tracker
    util.debug('[FINALIZER CALL] object mapping to {} about to be deleted, decrementing the refcount of the file (pid: {})'.format(os.path.basename(filename), os.getpid()))
    _resource_tracker.maybe_unlink(filename, 'file')


def add_maybe_unlink_finalizer(memmap):
    util.debug('[FINALIZER ADD] adding finalizer to {} (id {}, filename {}, pid  {})'.format(type(memmap), id(memmap), os.path.basename(memmap.filename), os.getpid()))
    weakref.finalize(memmap, _log_and_unlink, memmap.filename)


def unlink_file(filename):
    '''Wrapper around os.unlink with a retry mechanism.

    The retry mechanism has been implemented primarily to overcome a race
    condition happening during the finalizer of a np.memmap: when a process
    holding the last reference to a mmap-backed np.memmap/np.array is about to
    delete this array (and close the reference), it sends a maybe_unlink
    request to the resource_tracker. This request can be processed faster than
    it takes for the last reference of the memmap to be closed, yielding (on
    Windows) a PermissionError in the resource_tracker loop.
    '''
    NUM_RETRIES = 10
    for retry_no in range(1, NUM_RETRIES + 1):
        os.unlink(filename)
        return None
        except PermissionError:
            util.debug('[ResourceTracker] tried to unlink {}, got PermissionError'.format(filename))
            if retry_no == NUM_RETRIES:
                raise 
            time.sleep(0.2)
            continue
        except FileNotFoundError:
            continue
        return None

resource_tracker._CLEANUP_FUNCS['file'] = unlink_file

class _WeakArrayKeyMap:
    '''A variant of weakref.WeakKeyDictionary for unhashable numpy arrays.

    This datastructure will be used with numpy arrays as obj keys, therefore we
    do not use the __get__ / __set__ methods to avoid any conflict with the
    numpy fancy indexing syntax.
    '''
    
    def __init__(self):
        self._data = { }

    
    def get(self, obj):
        (ref, val) = self._data[id(obj)]
        if ref() is not obj:
            raise KeyError(obj)
        return val

    
    def set(self, obj, value):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        raise PicklingError('_WeakArrayKeyMap is not pickleable')



def _get_backing_memmap(a):
    '''Recursively look up the original np.memmap instance base if any.'''
    b = getattr(a, 'base', None)
# WARNING: Decompyle incomplete


def _get_temp_dir(pool_folder_name, temp_folder = (None,)):
    '''Get the full path to a subfolder inside the temporary folder.

    Parameters
    ----------
    pool_folder_name : str
        Sub-folder name used for the serialization of a pool instance.

    temp_folder: str, optional
        Folder to be used by the pool for memmapping large arrays
        for sharing memory with worker processes. If None, this will try in
        order:

        - a folder pointed by the JOBLIB_TEMP_FOLDER environment
          variable,
        - /dev/shm if the folder exists and is writable: this is a
          RAMdisk filesystem available by default on modern Linux
          distributions,
        - the default system temporary folder that can be
          overridden with TMP, TMPDIR or TEMP environment
          variables, typically /tmp under Unix operating systems.

    Returns
    -------
    pool_folder : str
       full path to the temporary folder
    use_shared_mem : bool
       whether the temporary folder is written to the system shared memory
       folder or some other temporary folder.
    '''
    use_shared_mem = False
# WARNING: Decompyle incomplete


def has_shareable_memory(a):
    '''Return True if a is backed by some mmap buffer directly or not.'''
    return _get_backing_memmap(a) is not None


def _strided_from_memmap(filename, dtype, mode, offset, order, shape, strides, total_buffer_len, unlink_on_gc_collect):
    '''Reconstruct an array view on a memory mapped file.'''
    if mode == 'w+':
        mode = 'r+'
# WARNING: Decompyle incomplete


def _reduce_memmap_backed(a, m):
    '''Pickling reduction for memmap backed arrays.

    a is expected to be an instance of np.ndarray (or np.memmap)
    m is expected to be an instance of np.memmap on the top of the ``base``
    attribute ancestry of a. ``m.base`` should be the real python mmap object.
    '''
    util.debug('[MEMMAP REDUCE] reducing a memmap-backed array (shape, {}, pid: {})'.format(a.shape, os.getpid()))
    
    try:
        byte_bounds = byte_bounds
        import numpy.lib.array_utils
    except (ModuleNotFoundError, ImportError):
        byte_bounds = byte_bounds
        import numpy

    (a_start, a_end) = byte_bounds(a)
    m_start = byte_bounds(m)[0]
    offset = a_start - m_start
    offset += m.offset
    if m.ndim > 1 and m.flags['F_CONTIGUOUS']:
        order = 'F'
    else:
        order = 'C'
    if a.flags['F_CONTIGUOUS'] or a.flags['C_CONTIGUOUS']:
        strides = None
        total_buffer_len = None
    else:
        strides = a.strides
        total_buffer_len = (a_end - a_start) // a.itemsize
    return (_strided_from_memmap, (m.filename, a.dtype, m.mode, offset, order, a.shape, strides, total_buffer_len, False))


def reduce_array_memmap_backward(a):
    '''reduce a np.array or a np.memmap from a child process'''
    m = _get_backing_memmap(a)
    if isinstance(m, np.memmap) and m.filename not in JOBLIB_MMAPS:
        return _reduce_memmap_backed(a, m)
    return (None, (dumps(np.asarray(a), protocol = HIGHEST_PROTOCOL),))


class ArrayMemmapForwardReducer(object):
    """Reducer callable to dump large arrays to memmap files.

    Parameters
    ----------
    max_nbytes: int
        Threshold to trigger memmapping of large arrays to files created
        a folder.
    temp_folder_resolver: callable
        An callable in charge of resolving a temporary folder name where files
        for backing memmapped arrays are created.
    mmap_mode: 'r', 'r+' or 'c'
        Mode for the created memmap datastructure. See the documentation of
        numpy.memmap for more details. Note: 'w+' is coerced to 'r+'
        automatically to avoid zeroing the data on unpickling.
    verbose: int, optional, 0 by default
        If verbose > 0, memmap creations are logged.
        If verbose > 1, both memmap creations, reuse and array pickling are
        logged.
    prewarm: bool, optional, False by default.
        Force a read on newly memmapped array to make sure that OS pre-cache it
        memory. This can be useful to avoid concurrent disk access when the
        same data array is passed to different worker processes.
    """
    
    def __init__(self, max_nbytes, temp_folder_resolver, mmap_mode, unlink_on_gc_collect, verbose, prewarm = (0, True)):
        self._max_nbytes = max_nbytes
        self._temp_folder_resolver = temp_folder_resolver
        self._mmap_mode = mmap_mode
        self.verbose = int(verbose)
        if prewarm == 'auto':
            self._prewarm = not self._temp_folder.startswith(SYSTEM_SHARED_MEM_FS)
        else:
            self._prewarm = prewarm
        self._prewarm = prewarm
        self._memmaped_arrays = _WeakArrayKeyMap()
        self._temporary_memmaped_filenames = set()
        self._unlink_on_gc_collect = unlink_on_gc_collect

    _temp_folder = (lambda self: self._temp_folder_resolver())()
    
    def __reduce__(self):
        args = (self._max_nbytes, None, self._mmap_mode, self._unlink_on_gc_collect)
        kwargs = {
            'verbose': self.verbose,
            'prewarm': self._prewarm }
        return (ArrayMemmapForwardReducer, args, kwargs)

    
    def __call__(self, a):
        m = _get_backing_memmap(a)
    # WARNING: Decompyle incomplete



def get_memmapping_reducers(forward_reducers, backward_reducers, temp_folder_resolver, max_nbytes, mmap_mode, verbose, prewarm, unlink_on_gc_collect = (None, None, None, 1e+06, 'r', 0, False, True), **kwargs):
    '''Construct a pair of memmapping reducer linked to a tmpdir.

    This function manage the creation and the clean up of the temporary folders
    underlying the memory maps and should be use to get the reducers necessary
    to construct joblib pool or executor.
    '''
    pass
# WARNING: Decompyle incomplete


class TemporaryResourcesManager(object):
    '''Stateful object able to manage temporary folder and pickles

    It exposes:
    - a per-context folder name resolving API that memmap-based reducers will
      rely on to know where to pickle the temporary memmaps
    - a temporary file/folder management API that internally uses the
      resource_tracker.
    '''
    
    def __init__(self, temp_folder_root, context_id = (None, None)):
        self._current_temp_folder = None
        self._temp_folder_root = temp_folder_root
        self._use_shared_mem = None
        self._cached_temp_folders = dict()
        self._id = uuid4().hex
        self._finalizers = { }
    # WARNING: Decompyle incomplete

    
    def set_current_context(self, context_id):
        self._current_context_id = context_id
        self.register_new_context(context_id)

    
    def register_new_context(self, context_id):
        if context_id in self._cached_temp_folders:
            return None
        new_folder_name = None.format(os.getpid(), self._id, context_id)
        (new_folder_path, _) = _get_temp_dir(new_folder_name, self._temp_folder_root)
        self.register_folder_finalizer(new_folder_path, context_id)
        self._cached_temp_folders[context_id] = new_folder_path

    
    def resolve_temp_folder_name(self):
        '''Return a folder name specific to the currently activated context'''
        return self._cached_temp_folders[self._current_context_id]

    
    def register_folder_finalizer(self, pool_subfolder, context_id):
        pass
    # WARNING: Decompyle incomplete

    
    def _clean_temporary_resources(self, context_id, force, allow_non_empty = (None, False, False)):
        '''Clean temporary resources created by a process-based pool'''
        pass
    # WARNING: Decompyle incomplete
