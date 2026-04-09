# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: memory.pyc (Python 3.11)

from __future__ import annotations
import logging
from datetime import datetime, timezone
from errno import ENOTEMPTY
from io import BytesIO
from pathlib import PurePath, PureWindowsPath
from typing import Any, ClassVar
from fsspec import AbstractFileSystem
from fsspec.implementations.local import LocalFileSystem
from fsspec.utils import stringify_path
logger = logging.getLogger('fsspec.memoryfs')

class MemoryFileSystem(AbstractFileSystem):
    '''A filesystem based on a dict of BytesIO objects

    This is a global filesystem so instances of this class all point to the same
    in memory filesystem.
    '''
    store: 'ClassVar[dict[str, Any]]' = { }
    pseudo_dirs = [
        '']
    protocol = 'memory'
    root_marker = '/'
    _strip_protocol = (lambda cls, path: if isinstance(path, PurePath):
if isinstance(path, PureWindowsPath):
LocalFileSystem._strip_protocol(path)path = None(path)path = path.removeprefix('memory://')if '::' in path or '://' in path:
path.rstrip('/')path = None.lstrip('/').rstrip('/')'/' + path if path else '')()
    
    def ls(self, path, detail = (True,), **kwargs):
        path = self._strip_protocol(path)
        if path in self.store:
            if not detail:
                return [
                    path]
            return [
                {
                    'name': None,
                    'size': self.store[path].size,
                    'type': 'file',
                    'created': self.store[path].created.timestamp() }]
        paths = None()
        starter = path + '/'
        out = []
        for p2 in tuple(self.store):
            if p2.startswith(starter):
                if '/' not in p2[len(starter):]:
                    out.append({
                        'name': p2,
                        'size': self.store[p2].size,
                        'type': 'file',
                        'created': self.store[p2].created.timestamp() })
                    continue
                if len(p2) > len(starter):
                    ppath = starter + p2[len(starter):].split('/', 1)[0]
                    if ppath not in paths:
                        if not out:
                            out = []
                            out.append({
                                'name': ppath,
                                'size': 0,
                                'type': 'directory' })
                            paths.add(ppath)
                            continue
                            for p2 in self.pseudo_dirs:
                                if p2.startswith(starter):
                                    if '/' not in p2[len(starter):]:
                                        if p2 not in paths:
                                            out.append({
                                                'name': p2,
                                                'size': 0,
                                                'type': 'directory' })
                                            paths.add(p2)
                                        continue
                                    ppath = starter + p2[len(starter):].split('/', 1)[0]
                                    if ppath not in paths:
                                        out.append({
                                            'name': ppath,
                                            'size': 0,
                                            'type': 'directory' })
                                        paths.add(ppath)
                                if not out:
                                    if path in self.pseudo_dirs:
                                        return []
                                    raise None(path)
                                if detail:
                                    return out
                                return (lambda .0: [ f['name'] for f in .0 ])(out())

    
    def mkdir(self, path, create_parents = (True,), **kwargs):
        path = self._strip_protocol(path)
        if path in self.store or path in self.pseudo_dirs:
            raise FileExistsError(path)
        if self._parent(path).strip('/') and self.isfile(self._parent(path)):
            raise NotADirectoryError(self._parent(path))
    # WARNING: Decompyle incomplete

    
    def makedirs(self, path, exist_ok = (False,)):
        
        try:
            self.mkdir(path, create_parents = True)
            return None
        except FileExistsError:
            if not exist_ok:
                raise 
            return None


    
    def pipe_file(self, path, value, mode = ('overwrite',), **kwargs):
        '''Set the bytes of given file

        Avoids copies of the data if possible
        '''
        mode = 'xb' if mode == 'create' else 'wb'
        self.open(path, mode = mode, data = value)

    
    def rmdir(self, path):
        path = self._strip_protocol(path)
        if path == '':
            return None
        if None in self.pseudo_dirs:
            if not self.ls(path):
                self.pseudo_dirs.remove(path)
                return None
            raise None(ENOTEMPTY, 'Directory not empty', path)
        raise FileNotFoundError(path)

    
    def info(self, path, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _open(self, path, mode, block_size, autocommit, cache_options = ('rb', None, True, None), **kwargs):
        path = self._strip_protocol(path)
        if 'x' in mode and self.exists(path):
            raise FileExistsError
        if path in self.pseudo_dirs:
            raise IsADirectoryError(path)
        parent = path
    # WARNING: Decompyle incomplete

    
    def cp_file(self, path1, path2, **kwargs):
        path1 = self._strip_protocol(path1)
        path2 = self._strip_protocol(path2)
        if self.isfile(path1):
            self.store[path2] = MemoryFile(self, path2, self.store[path1].getvalue())
            return None
        if None.isdir(path1):
            if path2 not in self.pseudo_dirs:
                self.pseudo_dirs.append(path2)
                return None
            return None
        raise None(path1)

    
    def cat_file(self, path, start, end = (None, None), **kwargs):
        logger.debug('cat: %s', path)
        path = self._strip_protocol(path)
        
        try:
            return bytes(self.store[path].getbuffer()[start:end])
        except KeyError:
            e = None
            raise FileNotFoundError(path), e
            e = None
            del e


    
    def _rm(self, path):
        path = self._strip_protocol(path)
        
        try:
            del self.store[path]
            return None
        except KeyError:
            e = None
            raise FileNotFoundError(path), e
            e = None
            del e


    
    def modified(self, path):
        path = self._strip_protocol(path)
        
        try:
            return self.store[path].modified
        except KeyError:
            e = None
            raise FileNotFoundError(path), e
            e = None
            del e


    
    def created(self, path):
        path = self._strip_protocol(path)
        
        try:
            return self.store[path].created
        except KeyError:
            e = None
            raise FileNotFoundError(path), e
            e = None
            del e


    
    def isfile(self, path):
        path = self._strip_protocol(path)
        return path in self.store

    
    def rm(self, path, recursive, maxdepth = (False, None)):
        pass
    # WARNING: Decompyle incomplete



class MemoryFile(BytesIO):
    pass
# WARNING: Decompyle incomplete
