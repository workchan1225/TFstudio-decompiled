# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fuse.pyc (Python 3.11)

import argparse
import logging
import os
import stat
import threading
import time
from errno import EIO, ENOENT
from fuse import FUSE, FuseOSError, LoggingMixIn, Operations
from fsspec import __version__
from fsspec.core import url_to_fs
logger = logging.getLogger('fsspec.fuse')

class FUSEr(Operations):
    
    def __init__(self, fs, path, ready_file = (False,)):
        self.fs = fs
        self.cache = { }
        self.root = path.rstrip('/') + '/'
        self.counter = 0
        logger.info('Starting FUSE at %s', path)
        self._ready_file = ready_file

    
    def getattr(self, path, fh = (None,)):
        logger.debug('getattr %s', path)
        if self._ready_file and path in ('/.fuse_ready', '.fuse_ready'):
            return {
                'type': 'file',
                'st_size': 5 }
        path = None.join([
            self.root,
            path.lstrip('/')]).rstrip('/')
        
        try:
            info = self.fs.info(path)
        except FileNotFoundError:
            exc = None
            raise FuseOSError(ENOENT), exc
            exc = None
            del exc

        data = {
            'st_uid': info.get('uid', 1000),
            'st_gid': info.get('gid', 1000) }
        perm = info.get('mode', 511)
        if info['type'] != 'file':
            data['st_mode'] = stat.S_IFDIR | perm
            data['st_size'] = 0
            data['st_blksize'] = 0
        else:
            data['st_mode'] = stat.S_IFREG | perm
            data['st_size'] = info['size']
            data['st_blksize'] = 5242880
            data['st_nlink'] = 1
        data['st_atime'] = info['atime'] if 'atime' in info else time.time()
        data['st_ctime'] = info['ctime'] if 'ctime' in info else time.time()
        data['st_mtime'] = info['mtime'] if 'mtime' in info else time.time()
        return data

    
    def readdir(self, path, fh):
        logger.debug('readdir %s', path)
        path = ''.join([
            self.root,
            path.lstrip('/')])
        files = self.fs.ls(path, False)
        files = files()
        return [
            '.',
            '..'] + files

    
    def mkdir(self, path, mode):
        path = ''.join([
            self.root,
            path.lstrip('/')])
        self.fs.mkdir(path)
        return 0

    
    def rmdir(self, path):
        path = ''.join([
            self.root,
            path.lstrip('/')])
        self.fs.rmdir(path)
        return 0

    
    def read(self, path, size, offset, fh):
        logger.debug('read %s', (path, size, offset))
        if self._ready_file and path in ('/.fuse_ready', '.fuse_ready'):
            return b'ready'
        f = None.cache[fh]
        f.seek(offset)
        out = f.read(size)
        return out

    
    def write(self, path, data, offset, fh):
        logger.debug('write %s', (path, offset))
        f = self.cache[fh]
        f.seek(offset)
        f.write(data)
        return len(data)

    
    def create(self, path, flags, fi = (None,)):
        logger.debug('create %s', (path, flags))
        fn = ''.join([
            self.root,
            path.lstrip('/')])
        self.fs.touch(fn)
        f = self.fs.open(fn, 'wb')
        self.cache[self.counter] = f
        return self.counter - 1

    
    def open(self, path, flags):
        logger.debug('open %s', (path, flags))
        fn = ''.join([
            self.root,
            path.lstrip('/')])
        if flags % 2 == 0:
            mode = 'rb'
        else:
            mode = 'wb'
        self.cache[self.counter] = self.fs.open(fn, mode)
        return self.counter - 1

    
    def truncate(self, path, length, fh = (None,)):
        fn = ''.join([
            self.root,
            path.lstrip('/')])
        if length != 0:
            raise NotImplementedError
        self.fs.touch(fn)

    
    def unlink(self, path):
        fn = ''.join([
            self.root,
            path.lstrip('/')])
        
        try:
            self.fs.rm(fn, False)
            return None
        except (OSError, FileNotFoundError):
            exc = None
            raise FuseOSError(EIO), exc
            exc = None
            del exc


    
    def release(self, path, fh):
