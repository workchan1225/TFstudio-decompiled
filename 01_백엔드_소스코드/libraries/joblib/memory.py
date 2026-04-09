# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: memory.pyc (Python 3.11)

"""
A context object for caching a function's return value each time it
is called with the same input arguments.

"""
import asyncio
import datetime
import functools
import inspect
import logging
import os
import pathlib
import pydoc
import re
import textwrap
import time
import tokenize
import traceback
import warnings
import weakref
from  import hashing
from _store_backends import CacheWarning, FileSystemStoreBackend, StoreBackendBase
from func_inspect import filter_args, format_call, format_signature, get_func_code, get_func_name
from logger import Logger, format_time, pformat
FIRST_LINE_TEXT = '# first line:'

def extract_first_line(func_code):
    '''Extract the first line information from the function code
    text if available.
    '''
    if func_code.startswith(FIRST_LINE_TEXT):
        func_code = func_code.split('\n')
        first_line = int(func_code[0][len(FIRST_LINE_TEXT):])
        func_code = '\n'.join(func_code[1:])
    else:
        first_line = -1
    return (func_code, first_line)


class JobLibCollisionWarning(UserWarning):
    '''Warn that there might be a collision between names of functions.'''
    pass

_STORE_BACKENDS = {
    'local': FileSystemStoreBackend }

def register_store_backend(backend_name, backend):
    """Extend available store backends.

    The Memory, MemorizeResult and MemorizeFunc objects are designed to be
    agnostic to the type of store used behind. By default, the local file
    system is used but this function gives the possibility to extend joblib's
    memory pattern with other types of storage such as cloud storage (S3, GCS,
    OpenStack, HadoopFS, etc) or blob DBs.

    Parameters
    ----------
    backend_name: str
        The name identifying the store backend being registered. For example,
        'local' is used with FileSystemStoreBackend.
    backend: StoreBackendBase subclass
        The name of a class that implements the StoreBackendBase interface.

    """
    if not isinstance(backend_name, str):
        raise ValueError("Store backend name should be a string, '{0}' given.".format(backend_name))
# WARNING: Decompyle incomplete


def _store_backend_factory(backend, location, verbose, backend_options = (0, None)):
    '''Return the correct store object for the given location.'''
    pass
# WARNING: Decompyle incomplete


def _build_func_identifier(func):
    '''Build a roughly unique identifier for the cached function.'''
    (modules, funcname) = get_func_name(func)
# WARNING: Decompyle incomplete

_FUNCTION_HASHES = weakref.WeakKeyDictionary()

class MemorizedResult(Logger):
    """Object representing a cached value.

    Attributes
    ----------
    location: str
        The location of joblib cache. Depends on the store backend used.

    func: function or str
        function whose output is cached. The string case is intended only for
        instantiation based on the output of repr() on another instance.
        (namely eval(repr(memorized_instance)) works).

    argument_hash: str
        hash of the function arguments.

    backend: str
        Type of store backend for reading/writing cache files.
        Default is 'local'.

    mmap_mode: {None, 'r+', 'r', 'w+', 'c'}
        The memmapping mode used when loading from cache numpy arrays. See
        numpy.load for the meaning of the different values.

    verbose: int
        verbosity level (0 means no message).

    timestamp, metadata: string
        for internal use only.
    """
    
    def __init__(self, location, call_id, backend, mmap_mode, verbose, timestamp, metadata = ('local', None, 0, None, None)):
        Logger.__init__(self)
        self._call_id = call_id
        self.store_backend = _store_backend_factory(backend, location, verbose = verbose)
        self.mmap_mode = mmap_mode
    # WARNING: Decompyle incomplete

    func = (lambda self: self.func_id)()
    func_id = (lambda self: self._call_id[0])()
    args_id = (lambda self: self._call_id[1])()
    
    def get(self):
        '''Read value from cache and return it.'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        '''Clear value from cache'''
        self.store_backend.clear_item(self._call_id)

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['timestamp'] = None
        return state



class NotMemorizedResult(object):
    '''Class representing an arbitrary value.

    This class is a replacement for MemorizedResult when there is no cache.
    '''
    __slots__ = ('value', 'valid')
    
    def __init__(self, value):
        self.value = value
        self.valid = True

    
    def get(self):
        if self.valid:
            return self.value
        raise None('No value stored.')

    
    def clear(self):
        self.valid = False
        self.value = None

    
    def __repr__(self):
        if self.valid:
            return '{class_name}({value})'.format(class_name = self.__class__.__name__, value = pformat(self.value))
        return None.__class__.__name__ + ' with no value'

    
    def __getstate__(self):
        return {
            'valid': self.valid,
            'value': self.value }

    
    def __setstate__(self, state):
        self.valid = state['valid']
        self.value = state['value']



class NotMemorizedFunc(object):
    '''No-op object decorating a function.

    This class replaces MemorizedFunc when there is no cache. It provides an
    identical API but does not write anything on disk.

    Attributes
    ----------
    func: callable
        Original undecorated function.
    '''
    
    def __init__(self, func):
        self.func = func

    
    def __call__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def call_and_shelve(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '{0}(func={1})'.format(self.__class__.__name__, self.func)

    
    def clear(self, warn = (True,)):
        pass

    
    def call(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def check_call_in_cache(self, *args, **kwargs):
        return False



class AsyncNotMemorizedFunc(NotMemorizedFunc):
    
    async def call_and_shelve(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class MemorizedFunc(Logger):
    """Callable object decorating a function for caching its return value
    each time it is called.

    Methods are provided to inspect the cache or clean it.

    Attributes
    ----------
    func: callable
        The original, undecorated, function.

    location: string
        The location of joblib cache. Depends on the store backend used.

    backend: str
        Type of store backend for reading/writing cache files.
        Default is 'local', in which case the location is the path to a
        disk storage.

    ignore: list or None
        List of variable names to ignore when choosing whether to
        recompute.

    mmap_mode: {None, 'r+', 'r', 'w+', 'c'}
        The memmapping mode used when loading from cache
        numpy arrays. See numpy.load for the meaning of the different
        values.

    compress: boolean, or integer
        Whether to zip the stored data on disk. If an integer is
        given, it should be between 1 and 9, and sets the amount
        of compression. Note that compressed arrays cannot be
        read by memmapping.

    verbose: int, optional
        The verbosity flag, controls messages that are issued as
        the function is evaluated.

    cache_validation_callback: callable, optional
        Callable to check if a result in cache is valid or is to be recomputed.
        When the function is called with arguments for which a cache exists,
        the callback is called with the cache entry's metadata as its sole
        argument. If it returns True, the cached result is returned, else the
        cache for these arguments is cleared and the result is recomputed.
    """
    
    def __init__(self, func, location, backend, ignore, mmap_mode, compress, verbose, timestamp, cache_validation_callback = ('local', None, None, False, 1, None, None)):
        Logger.__init__(self)
        self.mmap_mode = mmap_mode
        self.compress = compress
        self.func = func
        self.cache_validation_callback = cache_validation_callback
        self.func_id = _build_func_identifier(func)
    # WARNING: Decompyle incomplete

    
    def _is_in_cache_and_valid(self, call_id):
        '''Check if the function call is cached and valid for given arguments.

        - Compare the function code with the one from the cached function,
        asserting if it has changed.
        - Check if the function call is present in the cache.
        - Call `cache_validation_callback` for user define cache validation.

        Returns True if the function call is in cache and can be used, and
        returns False otherwise.
        '''
        if not self._check_previous_func_code(stacklevel = 4):
            return False
        if not None.store_backend.contains_item(call_id):
            return False
        metadata = None.store_backend.get_metadata(call_id)
    # WARNING: Decompyle incomplete

    
    def _cached_call(self, args, kwargs, shelving):
        '''Call wrapped function and cache result, or read cache if available.

        This function returns the wrapped function output or a reference to
        the cached result.

        Arguments:
        ----------

        args, kwargs: list and dict
            input arguments for wrapped function

        shelving: bool
            True when called via the call_and_shelve function.


        Returns
        -------
        output: Output of the wrapped function if shelving is false, or a
            MemorizedResult reference to the value if shelving is true.
        metadata: dict containing the metadata associated with the call.
        '''
        pass
    # WARNING: Decompyle incomplete

    func_code_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def call_and_shelve(self, *args, **kwargs):
        '''Call wrapped function, cache result and return a reference.

        This method returns a reference to the cached result instead of the
        result itself. The reference object is small and picklable, allowing
        to send or store it easily. Call .get() on reference object to get
        result.

        Returns
        -------
        cached_result: MemorizedResult or NotMemorizedResult
            reference to the value returned by the wrapped function. The
            class "NotMemorizedResult" is used when there is no cache
            activated (e.g. location=None in Memory).
        '''
        return self._cached_call(args, kwargs, shelving = True)[0]

    
    def __call__(self, *args, **kwargs):
        return self._cached_call(args, kwargs, shelving = False)[0]

    
    def __getstate__(self):
        _ = self.func_code_info
        state = self.__dict__.copy()
        state['timestamp'] = None
        state['_func_code_id'] = None
        return state

    
    def check_call_in_cache(self, *args, **kwargs):
        '''Check if the function call is cached and valid for given arguments.

        Does not call the function or do any work besides function inspection
        and argument hashing.

        - Compare the function code with the one from the cached function,
          asserting if it has changed.
        - Check if the function call is present in the cache.
        - Call `cache_validation_callback` for user define cache validation.

        Returns
        -------
        is_call_in_cache: bool
            Whether or not the function call is in cache and can be used.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_args_id(self, *args, **kwargs):
        '''Return the input parameter hash of a result.'''
        return hashing.hash(filter_args(self.func, self.ignore, args, kwargs), coerce_mmap = self.mmap_mode is not None)

    
    def _hash_func(self):
        '''Hash a function to key the online cache'''
        func_code_h = hash(getattr(self.func, '__code__', None))
        return (id(self.func), hash(self.func), func_code_h)

    
    def _write_func_code(self, func_code, first_line):
        '''Write the function code and the filename to a file.'''
        func_code = '%s %i\n%s' % (FIRST_LINE_TEXT, first_line, func_code)
        self.store_backend.store_cached_func_code([
            self.func_id], func_code)
        if hasattr(self.func, '__name__'):
            is_named_callable = self.func.__name__ != '<lambda>'
            if is_named_callable:
                func_hash = self._hash_func()
                
                try:
                    _FUNCTION_HASHES[self.func] = func_hash
                    return None
                except TypeError:
                    return None
                    return None


    
    def _check_previous_func_code(self, stacklevel = (2,)):
        '''
        stacklevel is the depth a which this function is called, to
        issue useful warnings to the user.
        '''
        
        try:
            if self.func in _FUNCTION_HASHES:
                func_hash = self._hash_func()
                if func_hash == _FUNCTION_HASHES[self.func]:
                    return True
                except TypeError:
                    pass
                (func_code, source_file, first_line) = self.func_code_info
                
                try:
                    (old_func_code, old_first_line) = extract_first_line(self.store_backend.get_cached_func_code([
                        self.func_id]))
                except (IOError, OSError):
                    self._write_func_code(func_code, first_line)
                    return False

                if old_func_code == func_code:
                    return True
                (_, func_name) = None(self.func, resolv_alias = False, win_characters = False)
                if not  == old_first_line, first_line or old_first_line, first_line == -1:
                    pass
                

        if func_name == '<lambda>':
            if not first_line == -1:
                pass
            else:
                func_name = '{0} ({1}:{2})'.format(func_name, source_file, first_line)
            warnings.warn(JobLibCollisionWarning("Cannot detect name collisions for function '{0}'".format(func_description)), stacklevel = stacklevel)
    # WARNING: Decompyle incomplete

    
    def clear(self, warn = (True,)):
        """Empty the function's cache."""
        func_id = self.func_id
        if self._verbose > 0 and warn:
            self.warn('Clearing function cache identified by %s' % func_id)
        self.store_backend.clear_path([
            func_id])
        (func_code, _, first_line) = self.func_code_info
        self._write_func_code(func_code, first_line)

    
    def call(self, *args, **kwargs):
        '''Force the execution of the function with the given arguments.

        The output values will be persisted, i.e., the cache will be updated
        with any new values.

        Parameters
        ----------
        *args: arguments
            The arguments.
        **kwargs: keyword arguments
            Keyword arguments.

        Returns
        -------
        output : object
            The output of the function call.
        metadata : dict
            The metadata associated with the call.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _call(self, call_id, args, kwargs, shelving = (False,)):
        self._before_call(args, kwargs)
        start_time = time.time()
    # WARNING: Decompyle incomplete

    
    def _before_call(self, args, kwargs):
        if self._verbose > 0:
            print(format_call(self.func, args, kwargs))
            return None

    
    def _after_call(self, call_id, args, kwargs, shelving, output, start_time):
        self.store_backend.dump_item(call_id, output, verbose = self._verbose)
        duration = time.time() - start_time
        if self._verbose > 0:
            self._print_duration(duration)
        metadata = self._persist_input(duration, call_id, args, kwargs)
        if shelving:
            return (self._get_memorized_result(call_id, metadata), metadata)
    # WARNING: Decompyle incomplete

    
    def _persist_input(self, duration, call_id, args, kwargs, this_duration_limit = (0.5,)):
        '''Save a small summary of the call using json format in the
        output directory.

        output_dir: string
            directory where to write metadata.

        duration: float
            time taken by hashing input arguments, calling the wrapped
            function and persisting its output.

        args, kwargs: list and dict
            input arguments for wrapped function

        this_duration_limit: float
            Max execution time for this function before issuing a warning.
        '''
        start_time = time.time()
        argument_dict = filter_args(self.func, self.ignore, args, kwargs)
        input_repr = (lambda .0: pass# WARNING: Decompyle incomplete
)(argument_dict.items()())
        metadata = {
            'duration': duration,
            'input_args': input_repr,
            'time': start_time }
        self.store_backend.store_metadata(call_id, metadata)
        this_duration = time.time() - start_time
        if this_duration > this_duration_limit:
            warnings.warn('Persisting input arguments took %.2fs to run.If this happens often in your code, it can cause performance problems (results will be correct in all cases). The reason for this is probably some large input arguments for a wrapped function.' % this_duration, stacklevel = 5)
        return metadata

    
    def _get_memorized_result(self, call_id, metadata = (None,)):
        return MemorizedResult(self.store_backend, call_id, metadata = metadata, timestamp = self.timestamp, verbose = self._verbose - 1)

    
    def _load_item(self, call_id, metadata = (None,)):
        return self.store_backend.load_item(call_id, metadata = metadata, timestamp = self.timestamp, verbose = self._verbose)

    
    def _print_duration(self, duration, context = ('',)):
        (_, name) = get_func_name(self.func)
        msg = f'''{name} {context}- {format_time(duration)}'''
        print(max(0, 80 - len(msg)) * '_' + msg)

    
    def __repr__(self):
        return '{class_name}(func={func}, location={location})'.format(class_name = self.__class__.__name__, func = self.func, location = self.store_backend.location)



class AsyncMemorizedFunc(MemorizedFunc):
    pass
# WARNING: Decompyle incomplete


class Memory(Logger):
    """A context object for caching a function's return value each time it
    is called with the same input arguments.

    All values are cached on the filesystem, in a deep directory
    structure.

    Read more in the :ref:`User Guide <memory>`.

    Parameters
    ----------
    location: str, pathlib.Path or None
        The path of the base directory to use as a data store
        or None. If None is given, no caching is done and
        the Memory object is completely transparent. This option
        replaces cachedir since version 0.12.

    backend: str, optional, default='local'
        Type of store backend for reading/writing cache files.
        The 'local' backend is using regular filesystem operations to
        manipulate data (open, mv, etc) in the backend.

    mmap_mode: {None, 'r+', 'r', 'w+', 'c'}, optional
        The memmapping mode used when loading from cache
        numpy arrays. See numpy.load for the meaning of the
        arguments.

    compress: boolean, or integer, optional
        Whether to zip the stored data on disk. If an integer is
        given, it should be between 1 and 9, and sets the amount
        of compression. Note that compressed arrays cannot be
        read by memmapping.

    verbose: int, optional
        Verbosity flag, controls the debug messages that are issued
        as functions are evaluated.

    backend_options: dict, optional
        Contains a dictionary of named parameters used to configure
        the store backend.
    """
    
    def __init__(self, location, backend, mmap_mode, compress, verbose, backend_options = (None, 'local', None, False, 1, None)):
        Logger.__init__(self)
        self._verbose = verbose
        self.mmap_mode = mmap_mode
        self.timestamp = time.time()
        self.backend = backend
        self.compress = compress
    # WARNING: Decompyle incomplete

    
    def cache(self, func, ignore, verbose, mmap_mode, cache_validation_callback = (None, None, None, False, None)):
        """Decorates the given function func to only compute its return
        value for input arguments not cached on disk.

        Parameters
        ----------
        func: callable, optional
            The function to be decorated
        ignore: list of strings
            A list of arguments name to ignore in the hashing
        verbose: integer, optional
            The verbosity mode of the function. By default that
            of the memory object is used.
        mmap_mode: {None, 'r+', 'r', 'w+', 'c'}, optional
            The memmapping mode used when loading from cache
            numpy arrays. See numpy.load for the meaning of the
            arguments. By default that of the memory object is used.
        cache_validation_callback: callable, optional
            Callable to validate whether or not the cache is valid. When
            the cached function is called with arguments for which a cache
            exists, this callable is called with the metadata of the cached
            result as its sole argument. If it returns True, then the
            cached result is returned, else the cache for these arguments
            is cleared and recomputed.

        Returns
        -------
        decorated_func: MemorizedFunc object
            The returned object is a MemorizedFunc object, that is
            callable (behaves like a function), but offers extra
            methods for cache lookup and management. See the
            documentation for :class:`joblib.memory.MemorizedFunc`.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self, warn = (True,)):
        '''Erase the complete cache directory.'''
        if warn:
            self.warn('Flushing completely the cache')
    # WARNING: Decompyle incomplete

    
    def reduce_size(self, bytes_limit, items_limit, age_limit = (None, None, None)):
        '''Remove cache elements to make the cache fit its limits.

        The limitation can impose that the cache size fits in ``bytes_limit``,
        that the number of cache items is no more than ``items_limit``, and
        that all files in cache are not older than ``age_limit``.

        Parameters
        ----------
        bytes_limit: int | str, optional
            Limit in bytes of the size of the cache. By default, the size of
            the cache is unlimited. When reducing the size of the cache,
            ``joblib`` keeps the most recently accessed items first. If a
            str is passed, it is converted to a number of bytes using units
            { K | M | G} for kilo, mega, giga.

        items_limit: int, optional
            Number of items to limit the cache to.  By default, the number of
            items in the cache is unlimited.  When reducing the size of the
            cache, ``joblib`` keeps the most recently accessed items first.

        age_limit: datetime.timedelta, optional
            Maximum age of items to limit the cache to.  When reducing the size
            of the cache, any items last accessed more than the given length of
            time ago are deleted. Example: to remove files older than 5 days,
            use datetime.timedelta(days=5). Negative timedelta are not
            accepted.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def eval(self, func, *args, **kwargs):
        '''Eval function func with arguments `*args` and `**kwargs`,
        in the context of the memory.

        This method works similarly to the builtin `apply`, except
        that the function is called only if the cache is not
        up to date.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        """We don't store the timestamp when pickling, to avoid the hash
        depending from it.
        """
        state = self.__dict__.copy()
        state['timestamp'] = None
        return state



def expires_after(days, seconds, microseconds, milliseconds, minutes, hours, weeks = (0, 0, 0, 0, 0, 0, 0)):
    '''Helper cache_validation_callback to force recompute after a duration.

    Parameters
    ----------
    days, seconds, microseconds, milliseconds, minutes, hours, weeks: numbers
        argument passed to a timedelta.
    '''
    pass
# WARNING: Decompyle incomplete
