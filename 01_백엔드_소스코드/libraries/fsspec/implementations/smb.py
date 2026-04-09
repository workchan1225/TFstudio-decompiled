# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: smb.pyc (Python 3.11)

'''
This module contains SMBFileSystem class responsible for handling access to
Windows Samba network shares by using package smbprotocol
'''
import datetime
import re
import uuid
from stat import S_ISDIR, S_ISLNK
import smbclient
import smbprotocol.exceptions as smbprotocol
from  import AbstractFileSystem
from utils import infer_storage_options

class SMBFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


def _as_unc_path(host, path):
    rpath = path.replace('/', '\\')
    unc = f'''\\\\{host}{rpath}'''
    return unc


def _as_temp_path(host, path, temppath):
    share = path.split('/')[1]
    temp_file = f'''/{share}{temppath}/{uuid.uuid4()}'''
    unc = _as_unc_path(host, temp_file)
    return unc


def _share_has_path(path):
    parts = path.count('/')
    if path.endswith('/'):
        return parts > 2
    return None > 1


class SMBFileOpener:
    '''writes to remote temporary file, move on commit'''
    
    def __init__(self, path, temp, mode, port, block_size = (445, -1), **kwargs):
        self.path = path
        self.temp = temp
        self.mode = mode
        self.block_size = block_size
        self.kwargs = kwargs
        self.smbfile = None
        self._incontext = False
        self.port = port
        self._open()

    
    def _open(self):
        pass
    # WARNING: Decompyle incomplete

    
    def commit(self):
        '''Move temp file to definitive on success.'''
        smbclient.replace(self.temp, self.path, port = self.port)

    
    def discard(self):
        '''Remove the temp file on failure.'''
        smbclient.remove(self.temp, port = self.port)

    
    def __fspath__(self):
        return self.path

    
    def __iter__(self):
        return self.smbfile.__iter__()

    
    def __getattr__(self, item):
        return getattr(self.smbfile, item)

    
    def __enter__(self):
        self._incontext = True
        return self.smbfile.__enter__()

    
    def __exit__(self, exc_type, exc_value, traceback):
        self._incontext = False
        self.smbfile.__exit__(exc_type, exc_value, traceback)
