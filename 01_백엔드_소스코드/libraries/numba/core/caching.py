# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: caching.pyc (Python 3.11)

'''
Caching mechanism for compiled functions.
'''
from abc import ABCMeta, abstractmethod
import contextlib
import errno
import hashlib
import importlib
import inspect
import itertools
from math import floor
import os
import pickle
import sys
import tempfile
import uuid
import warnings
from numba.misc.appdirs import AppDirs
import zipfile
from pathlib import Path
import numba
from numba.core.errors import NumbaWarning
from numba.core.base import BaseContext
from numba.core.codegen import CodeLibrary
from numba.core.compiler import CompileResult
from numba.core import config, compiler
from numba.core.serialize import dumps

def _cache_log(msg, *args):
    if config.DEBUG_CACHE:
        msg = msg % args
        print(msg)
        return None


def _Cache():
    '''_Cache'''
    cache_path = (lambda self: pass)()()
    load_overload = (lambda self, sig, target_context: pass)()
    save_overload = (lambda self, sig, data: pass)()
    enable = (lambda self: pass)()
    disable = (lambda self: pass)()
    flush = (lambda self: pass)()

_Cache = <NODE:27>(_Cache, '_Cache', metaclass = ABCMeta)

class NullCache(_Cache):
    cache_path = (lambda self: pass)()
    
    def load_overload(self, sig, target_context):
        pass

    
    def save_overload(self, sig, cres):
        pass

    
    def enable(self):
        pass

    
    def disable(self):
        pass

    
    def flush(self):
        pass



def _CacheLocator():
    '''_CacheLocator'''
    __doc__ = '\n    A filesystem locator for caching a given function.\n    '
    
    def ensure_cache_path(self):
        path = self.get_cache_path()
        os.makedirs(path, exist_ok = True)
        tempfile.TemporaryFile(dir = path).close()

    get_cache_path = (lambda self: pass)()
    get_source_stamp = (lambda self: pass)()
    get_disambiguator = (lambda self: pass)()
    from_function = (lambda cls, py_func, py_file: raise NotImplementedError)()
    get_suitable_cache_subpath = (lambda cls, py_file: path = os.path.abspath(py_file)subpath = os.path.dirname(path)parentdir = os.path.split(subpath)[-1]hashed = hashlib.sha1(subpath.encode()).hexdigest()'_'.join([
parentdir,
hashed]))()

_CacheLocator = <NODE:27>(_CacheLocator, '_CacheLocator', metaclass = ABCMeta)

class _SourceFileBackedLocatorMixin(object):
    '''
    A cache locator mixin for functions which are backed by a well-known
    Python source file.
    '''
    
    def get_source_stamp(self):
        if getattr(sys, 'frozen', False):
            st = os.stat(sys.executable)
        else:
            st = os.stat(self._py_file)
        return (st.st_mtime, st.st_size)

    
    def get_disambiguator(self):
        return str(self._lineno)

    from_function = (lambda cls, py_func, py_file: if not os.path.exists(py_file):
Noneself = cls(py_func, py_file)try:
self.ensure_cache_path()except OSError:
Noneself)()


class UserProvidedCacheLocator(_CacheLocator, _SourceFileBackedLocatorMixin):
    pass
# WARNING: Decompyle incomplete


class InTreeCacheLocator(_CacheLocator, _SourceFileBackedLocatorMixin):
    '''
    A locator for functions backed by a regular Python module with a
    writable __pycache__ directory.
    '''
    
    def __init__(self, py_func, py_file):
        self._py_file = py_file
        self._lineno = py_func.__code__.co_firstlineno
        self._cache_path = os.path.join(os.path.dirname(self._py_file), '__pycache__')

    
    def get_cache_path(self):
        return self._cache_path



class InTreeCacheLocatorFsAgnostic(InTreeCacheLocator):
    pass
# WARNING: Decompyle incomplete


class UserWideCacheLocator(_CacheLocator, _SourceFileBackedLocatorMixin):
    '''
    A locator for functions backed by a regular Python module or a
    frozen executable, cached into a user-wide cache directory.
    '''
    
    def __init__(self, py_func, py_file):
        self._py_file = py_file
        self._lineno = py_func.__code__.co_firstlineno
        appdirs = AppDirs(appname = 'numba', appauthor = False)
        cache_dir = appdirs.user_cache_dir
        cache_subpath = self.get_suitable_cache_subpath(py_file)
        self._cache_path = os.path.join(cache_dir, cache_subpath)

    
    def get_cache_path(self):
        return self._cache_path

    from_function = (lambda cls, py_func, py_file: if not os.path.exists(py_file) and getattr(sys, 'frozen', False):
Noneself = cls(py_func, py_file)try:
self.ensure_cache_path()except OSError:
Noneself)()


class IPythonCacheLocator(_CacheLocator):
    '''
    A locator for functions entered at the IPython prompt (notebook or other).
    '''
    
    def __init__(self, py_func, py_file):
        self._py_file = py_file
        source = inspect.getsource(py_func)
        if isinstance(source, bytes):
            self._bytes_source = source
            return None
        self._bytes_source = None.encode('utf-8')

    
    def get_cache_path(self):
        
        try:
            get_ipython_cache_dir = get_ipython_cache_dir
            import IPython.paths
        except ImportError:
            get_ipython_cache_dir = get_ipython_cache_dir
            import IPython.utils.path

        return os.path.join(get_ipython_cache_dir(), 'numba_cache')

    
    def get_source_stamp(self):
        return hashlib.sha256(self._bytes_source).hexdigest()

    
    def get_disambiguator(self):
        firstlines = b''.join(self._bytes_source.splitlines(True)[:2])
        return hashlib.sha256(firstlines).hexdigest()[:10]

    from_function = (lambda cls, py_func, py_file: if not py_file.startswith('<ipython-') and os.path.basename(os.path.dirname(py_file)).startswith('ipykernel_'):
Noneself = cls(py_func, py_file)try:
self.ensure_cache_path()except OSError:
Noneself)()


class ZipCacheLocator(_CacheLocator, _SourceFileBackedLocatorMixin):
    '''
    A locator for functions backed by Python modules within a zip archive.
    '''
    
    def __init__(self, py_func, py_file):
        self._py_file = py_file
        self._lineno = py_func.__code__.co_firstlineno
        (self._zip_path, self._internal_path) = self._split_zip_path(py_file)
        appdirs = AppDirs(appname = 'numba', appauthor = False)
        cache_dir = appdirs.user_cache_dir
        cache_subpath = self.get_suitable_cache_subpath(py_file)
        self._cache_path = os.path.join(cache_dir, cache_subpath)

    _split_zip_path = (lambda py_file: path = Path(py_file)# WARNING: Decompyle incomplete
)()
    
    def get_cache_path(self):
        return self._cache_path

    
    def get_source_stamp(self):
        st = os.stat(self._zip_path)
        return (st.st_mtime, st.st_size)

    from_function = (lambda cls, py_func, py_file: if '.zip' not in py_file:
Nonecls(py_func, py_file))()


def CacheImpl():
    '''CacheImpl'''
    __doc__ = '\n    Provides the core machinery for caching.\n    - implement how to serialize and deserialize the data in the cache.\n    - control the filename of the cache.\n    - provide the cache locator\n    '
    _locator_classes = [
        UserProvidedCacheLocator,
        InTreeCacheLocator,
        UserWideCacheLocator,
        IPythonCacheLocator,
        ZipCacheLocator]
    
    def __init__(self, py_func):
        self._lineno = py_func.__code__.co_firstlineno
        
        try:
            qualname = py_func.__qualname__
        except AttributeError:
            qualname = py_func.__name__

    # WARNING: Decompyle incomplete

    
    def get_filename_base(self, fullname, abiflags):
        fixed_fullname = fullname.replace('<', '').replace('>', '')
        fmt = '%s-%s.py%d%d%s'
        return fmt % (fixed_fullname, self.locator.get_disambiguator(), sys.version_info[0], sys.version_info[1], abiflags)

    filename_base = (lambda self: self._filename_base)()
    locator = (lambda self: self._locator)()
    reduce = (lambda self, data: pass)()
    rebuild = (lambda self, target_context, reduced_data: pass)()
    check_cachable = (lambda self, data: pass)()

CacheImpl = <NODE:27>(CacheImpl, 'CacheImpl', metaclass = ABCMeta)

class CompileResultCacheImpl(CacheImpl):
    '''
    Implements the logic to cache CompileResult objects.
    '''
    
    def reduce(self, cres):
        '''
        Returns a serialized CompileResult
        '''
        return cres._reduce()

    
    def rebuild(self, target_context, payload):
        '''
        Returns the unserialized CompileResult
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def check_cachable(self, cres):
        '''
        Check cachability of the given compile result.
        '''
        cannot_cache = None
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(cres.lifted()):
            cannot_cache = 'as it uses lifted code'
        elif cres.library.has_dynamic_globals:
            cannot_cache = 'as it uses dynamic globals (such as ctypes pointers and large global arrays)'
        if cannot_cache:
            msg = f'''Cannot cache compiled function "{cres.fndesc.qualname.split('.')[-1]!s}" {cannot_cache!s}'''
            warnings.warn_explicit(msg, NumbaWarning, self._locator._py_file, self._lineno)
            return False
        return any



class CodeLibraryCacheImpl(CacheImpl):
    pass
# WARNING: Decompyle incomplete


class IndexDataCacheFile(object):
    '''
    Implements the logic for the index file and data file used by a cache.
    '''
    
    def __init__(self, cache_path, filename_base, source_stamp):
        self._cache_path = cache_path
        self._index_name = f'''{filename_base!s}.nbi'''
        self._index_path = os.path.join(self._cache_path, self._index_name)
        self._data_name_pattern = f'''{filename_base!s}.{{number:d}}.nbc'''
        self._source_stamp = source_stamp
        self._version = numba.__version__

    
    def flush(self):
        self._save_index({ })

    
    def save(self, key, data):
        '''
        Save a new cache entry with *key* and *data*.
        '''
        overloads = self._load_index()
        
        try:
            data_name = overloads[key]
        except KeyError:
            existing = set(overloads.values())
            for i in itertools.count(1):
                data_name = self._data_name(i)
                if data_name not in existing:
                    pass
                
                overloads[key] = data_name
                self._save_index(overloads)

        self._save_data(data_name, data)

    
    def load(self, key):
        '''
        Load a cache entry with *key*.
        '''
        overloads = self._load_index()
        data_name = overloads.get(key)
    # WARNING: Decompyle incomplete

    
    def _load_index(self):
        '''
        Load the cache index and return it as a dictionary (possibly
        empty if cache is empty or obsolete).
        '''
        
        try:
            f = open(self._index_path, 'rb')
            version = pickle.load(f)
            data = f.read()
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            pass
                        except FileNotFoundError:
                            return 

                        if version != self._version:
                            return { }
                        (stamp, overloads) = None.loads(data)
                        _cache_log('[cache] index loaded from %r', self._index_path)
                        if stamp != self._source_stamp:
                            return { }
                        return None




    
    def _save_index(self, overloads):
        data = (self._source_stamp, overloads)
        data = self._dump(data)
        f = self._open_for_write(self._index_path)
        pickle.dump(self._version, f, protocol = -1)
        f.write(data)
        None(None, None)

    
    def _load_data(self, name):
        path = self._data_path(name)
        f = open(path, 'rb')
        data = f.read()
        None(None, None)

    
    def _save_data(self, name, data):
        data = self._dump(data)
        path = self._data_path(name)
        f = self._open_for_write(path)
        f.write(data)
        None(None, None)

    
    def _data_name(self, number):
        return self._data_name_pattern.format(number = number)

    
    def _data_path(self, name):
        return os.path.join(self._cache_path, name)

    
    def _dump(self, obj):
        return dumps(obj)

    _open_for_write = (lambda self, filepath: pass# WARNING: Decompyle incomplete
)()


class Cache(_Cache):
    '''
    A per-function compilation cache.  The cache saves data in separate
    data files and maintains information in an index file.

    There is one index file per function and Python version
    ("function_name-<lineno>.pyXY.nbi") which contains a mapping of
    signatures and architectures to data files.
    It is prefixed by a versioning key and a timestamp of the Python source
    file containing the function.

    There is one data file ("function_name-<lineno>.pyXY.<number>.nbc")
    per function, function signature, target architecture and Python version.

    Separate index and data files per Python version avoid pickle
    compatibility problems.

    Note:
    This contains the driver logic only.  The core logic is provided
    by a subclass of ``CacheImpl`` specified as *_impl_class* in the subclass.
    '''
    _impl_class = None
    
    def __init__(self, py_func):
        self._name = repr(py_func)
        self._py_func = py_func
        self._impl = self._impl_class(py_func)
        self._cache_path = self._impl.locator.get_cache_path()
        source_stamp = self._impl.locator.get_source_stamp()
        filename_base = self._impl.filename_base
        self._cache_file = IndexDataCacheFile(cache_path = self._cache_path, filename_base = filename_base, source_stamp = source_stamp)
        self.enable()

    
    def __repr__(self):
        return f'''<{self.__class__.__name__!s} py_func={self._name!r}>'''

    cache_path = (lambda self: self._cache_path)()
    
    def enable(self):
        self._enabled = True

    
    def disable(self):
        self._enabled = False

    
    def flush(self):
        self._cache_file.flush()

    
    def load_overload(self, sig, target_context):
        '''
        Load and recreate the cached object for the given signature,
        using the *target_context*.
        '''
        target_context.refresh()
        self._guard_against_spurious_io_errors()
        None(None, None)
        return 
        with None:
            if not None, self._load_overload(sig, target_context):
                pass

    
    def _load_overload(self, sig, target_context):
        if not self._enabled:
            return None
        key = None._index_key(sig, target_context.codegen())
        data = self._cache_file.load(key)
    # WARNING: Decompyle incomplete

    
    def save_overload(self, sig, data):
        '''
        Save the data for the given signature in the cache.
        '''
        self._guard_against_spurious_io_errors()
        self._save_overload(sig, data)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _save_overload(self, sig, data):
        if not self._enabled:
            return None
        if not None._impl.check_cachable(data):
            return None
        None._impl.locator.ensure_cache_path()
        key = self._index_key(sig, data.codegen)
        data = self._impl.reduce(data)
        self._cache_file.save(key, data)

    _guard_against_spurious_io_errors = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _index_key(self, sig, codegen):
        '''
        Compute index key for the given signature and codegen.
        It includes a description of the OS, target architecture and hashes of
        the bytecode for the function and, if the function has a __closure__,
        a hash of the cell_contents.
        '''
        codebytes = self._py_func.__code__.co_code
    # WARNING: Decompyle incomplete



class FunctionCache(Cache):
    '''
    Implements Cache that saves and loads CompileResult objects.
    '''
    _impl_class = CompileResultCacheImpl

_lib_cache_prefixes = set([
    ''])

def make_library_cache(prefix):
    '''
    Create a Cache class for additional compilation features to cache their
    result for reuse.  The cache is saved in filename pattern like
    in ``FunctionCache`` but with additional *prefix* as specified.
    '''
    pass
# WARNING: Decompyle incomplete
