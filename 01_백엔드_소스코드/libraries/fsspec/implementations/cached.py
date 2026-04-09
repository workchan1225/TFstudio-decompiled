# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cached.pyc (Python 3.11)

from __future__ import annotations
import inspect
import logging
import os
import tempfile
import time
import weakref
from collections.abc import Callable
from shutil import rmtree
from typing import TYPE_CHECKING, Any, ClassVar
from fsspec import filesystem
from fsspec.callbacks import DEFAULT_CALLBACK
from fsspec.compression import compr
from fsspec.core import BaseCache, MMapCache
from fsspec.exceptions import BlocksizeMismatchError
from fsspec.implementations.cache_mapper import create_cache_mapper
from fsspec.implementations.cache_metadata import CacheMetadata
from fsspec.implementations.chained import ChainedFileSystem
from fsspec.implementations.local import LocalFileSystem
from fsspec.spec import AbstractBufferedFile
from fsspec.transaction import Transaction
from fsspec.utils import infer_compression
if TYPE_CHECKING:
    from fsspec.implementations.cache_mapper import AbstractCacheMapper
logger = logging.getLogger('fsspec.cached')

class WriteCachedTransaction(Transaction):
    
    def complete(self, commit = (True,)):
        rpaths = self.files()
        lpaths = self.files()
        if commit:
            self.fs.put(lpaths, rpaths)
        self.files.clear()
        self.fs._intrans = False
        self.fs._transaction = None
        self.fs = None



class CachingFileSystem(ChainedFileSystem):
    pass
# WARNING: Decompyle incomplete


class WholeFileCacheFileSystem(CachingFileSystem):
    '''Caches whole remote files on first access

    This class is intended as a layer over any other file system, and
    will make a local copy of each file accessed, so that all subsequent
    reads are local. This is similar to ``CachingFileSystem``, but without
    the block-wise functionality and so can work even when sparse files
    are not allowed. See its docstring for definition of the init
    arguments.

    The class still needs access to the remote store for listing files,
    and may refresh cached files.
    '''
    protocol = 'filecache'
    local_file = True
    
    def open_many(self, open_files, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def commit_many(self, open_files):
        
        def <listcomp>(.0):
            return [ f.path for f in .0 ]

        open_files()(<listcomp>, open_files())
        open_files()
        for f in open_files:
            os.remove(f.name)
            except FileNotFoundError:
                (lambda .0: [ f.fn for f in .0 ])
                continue
            self._cache_size = None
            return None

    
    def _make_local_details(self, path):
        hash = self._mapper(path)
        fn = os.path.join(self.storage[-1], hash)
        detail = {
            'original': path,
            'fn': hash,
            'blocks': True,
            'time': time.time(),
            'uid': self.fs.ukey(path) }
        self._metadata.update_file(path, detail)
        logger.debug('Copying %s to local cache', path)
        return fn

    
    def cat(self, path, recursive, on_error, callback = (False, 'raise', DEFAULT_CALLBACK), **kwargs):
        paths = self.expand_path(path, recursive = recursive, maxdepth = kwargs.get('maxdepth'))
        getpaths = []
        storepaths = []
        fns = []
        out = { }
        for p in paths.copy():
            detail = self._check_file(p)
            if not detail:
                fn = self._make_local_details(p)
                getpaths.append(p)
                storepaths.append(fn)
            elif isinstance(detail, tuple):
                pass
            
            (detail, fn) = (None, detail)
            fns.append(fn)
            except Exception:
                e = None
                if on_error == 'raise':
                    raise 
                if on_error == 'return':
                    out[p] = e
                paths.remove(p)
                e = None
                del e
                continue
                e = None
                del e
            if getpaths:
                self.fs.get(getpaths, storepaths)
                self.save_cache()
        callback.set_size(len(paths))
        for p, fn in zip(paths, fns):
            f = open(fn, 'rb')
            out[p] = f.read()
            None(None, None)
        with None:
            if not None:
                pass
        callback.relative_update(1)
        continue
        if isinstance(path, str) and len(paths) == 1 and recursive is False:
            out = out[paths[0]]
        return out

    
    def _open(self, path, mode = ('rb',), **kwargs):
        path = self._strip_protocol(path)
    # WARNING: Decompyle incomplete



class SimpleCacheFileSystem(WholeFileCacheFileSystem):
    pass
# WARNING: Decompyle incomplete


class LocalTempFile:
    '''A temporary local file, which will be uploaded on commit'''
    
    def __init__(self, fs, path, fn, mode, autocommit, seek = ('wb', True, 0), **kwargs):
        self.fn = fn
        self.fh = open(fn, mode)
        self.mode = mode
        if seek:
            self.fh.seek(seek)
        self.path = path
        self.size = None
        self.fs = fs
        self.closed = False
        self.autocommit = autocommit
        self.kwargs = kwargs

    
    def __reduce__(self):
        return (LocalTempFile, (self.fs, self.path, self.fn, 'r+b', self.autocommit, self.tell()))

    
    def __enter__(self):
        return self.fh

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    
    def close(self):
        if self.closed:
            return None
        None.fh.close()
        self.closed = True
        if self.autocommit:
            self.commit()
            return None

    
    def discard(self):
        self.fh.close()
        os.remove(self.fn)

    
    def commit(self):
        pass
    # WARNING: Decompyle incomplete

    name = (lambda self: self.fn)()
    
    def __repr__(self = None):
        return f'''LocalTempFile: {self.path}'''

    
    def __getattr__(self, item):
        return getattr(self.fh, item)
