# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _store_backends.pyc (Python 3.11)

'''Storage providers backends for Memory caching.'''
import collections
import datetime
import json
import operator
import os
import os.path as os
import re
import shutil
import threading
import time
import uuid
import warnings
from abc import ABCMeta, abstractmethod
from pickle import PicklingError
from  import numpy_pickle
from backports import concurrency_safe_rename
from disk import memstr_to_bytes, mkdirp, rm_subdirs
from logger import format_time
CacheItemInfo = collections.namedtuple('CacheItemInfo', 'path size last_access')

class CacheWarning(Warning):
    '''Warning to capture dump failures except for PicklingError.'''
    pass


def concurrency_safe_write(object_to_write, filename, write_func):
    '''Writes an object into a unique file in a concurrency-safe way.'''
    thread_id = id(threading.current_thread())
    temporary_filename = f'''{filename}.{uuid.uuid4().hex}-{os.getpid()}-{thread_id}'''
    write_func(object_to_write, temporary_filename)
    return temporary_filename


def StoreBackendBase():
    '''StoreBackendBase'''
    __doc__ = 'Helper Abstract Base Class which defines all methods that\n    a StorageBackend must implement.'
    location = None
    _open_item = (lambda self, f, mode: pass)()
    _item_exists = (lambda self, location: pass)()
    _move_item = (lambda self, src, dst: pass)()
    create_location = (lambda self, location: pass)()
    clear_location = (lambda self, location: pass)()
    get_items = (lambda self: pass)()
    configure = (lambda self, location, verbose, backend_options = (0, dict()): pass)()

StoreBackendBase = <NODE:27>(StoreBackendBase, 'StoreBackendBase', metaclass = ABCMeta)

class StoreBackendMixin(object):
    '''Class providing all logic for managing the store in a generic way.

    The StoreBackend subclass has to implement 3 methods: create_location,
    clear_location and configure. The StoreBackend also has to provide
    a private _open_item, _item_exists and _move_item methods. The _open_item
    method has to have the same signature as the builtin open and return a
    file-like object.
    '''
    
    def load_item(self, call_id, verbose, timestamp, metadata = (1, None, None)):
        '''Load an item from the store given its id as a list of str.'''
        pass
    # WARNING: Decompyle incomplete

    
    def dump_item(self, call_id, item, verbose = (1,)):
        '''Dump an item in the store at the id given as a list of str.'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear_item(self, call_id):
        '''Clear the item at the id, given as a list of str.'''
        pass
    # WARNING: Decompyle incomplete

    
    def contains_item(self, call_id):
        '''Check if there is an item at the id, given as a list of str.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_item_info(self, call_id):
        '''Return information about item.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_metadata(self, call_id):
        '''Return actual metadata of an item.'''
        pass
    # WARNING: Decompyle incomplete

    
    def store_metadata(self, call_id, metadata):
        '''Store metadata of a computation.'''
        pass
    # WARNING: Decompyle incomplete

    
    def contains_path(self, call_id):
        '''Check cached function is available in store.'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear_path(self, call_id):
        '''Clear all items with a common path in the store.'''
        pass
    # WARNING: Decompyle incomplete

    
    def store_cached_func_code(self, call_id, func_code = (None,)):
        '''Store the code of the cached function.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_cached_func_code(self, call_id):
        '''Store the code of the cached function.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_cached_func_info(self, call_id):
        '''Return information related to the cached function if it exists.'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        '''Clear the whole store content.'''
        self.clear_location(self.location)

    
    def enforce_store_limits(self, bytes_limit, items_limit, age_limit = (None, None)):
        """
        Remove the store's oldest files to enforce item, byte, and age limits.
        """
        items_to_delete = self._get_items_to_delete(bytes_limit, items_limit, age_limit)
        for item in items_to_delete:
            if self.verbose > 10:
                print('Deleting item {0}'.format(item))
            self.clear_location(item.path)
            except OSError:
                continue
            return None

    
    def _get_items_to_delete(self, bytes_limit, items_limit, age_limit = (None, None)):
        '''
        Get items to delete to keep the store under size, file, & age limits.
        '''
        if isinstance(bytes_limit, str):
            bytes_limit = memstr_to_bytes(bytes_limit)
        items = self.get_items()
        if not items:
            return []
        size = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
    # WARNING: Decompyle incomplete

    
    def _concurrency_safe_write(self, to_write, filename, write_func):
        '''Writes an object into a file in a concurrency-safe way.'''
        temporary_filename = concurrency_safe_write(to_write, filename, write_func)
        self._move_item(temporary_filename, filename)

    
    def __repr__(self):
        '''Printable representation of the store location.'''
        return '{class_name}(location="{location}")'.format(class_name = self.__class__.__name__, location = self.location)



class FileSystemStoreBackend(StoreBackendMixin, StoreBackendBase):
    '''A StoreBackend used with local or network file systems.'''
    _open_item = staticmethod(open)
    _item_exists = staticmethod(os.path.exists)
    _move_item = staticmethod(concurrency_safe_rename)
    
    def clear_location(self, location):
        '''Delete location on store.'''
        if location == self.location:
            rm_subdirs(location)
            return None
        None.rmtree(location, ignore_errors = True)

    
    def create_location(self, location):
        '''Create object location on store'''
        mkdirp(location)

    
    def get_items(self):
        '''Returns the whole list of items available in the store.'''
        pass
    # WARNING: Decompyle incomplete

    
    def configure(self, location, verbose, backend_options = (1, None)):
        """Configure the store backend.

        For this backend, valid store options are 'compress' and 'mmap_mode'
        """
        pass
    # WARNING: Decompyle incomplete
