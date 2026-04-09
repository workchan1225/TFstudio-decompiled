# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spec.pyc (Python 3.11)

from __future__ import annotations
import io
import json
import logging
import os
import threading
import warnings
import weakref
from errno import ESPIPE
from glob import has_magic
from hashlib import sha256
from typing import Any, ClassVar
from callbacks import DEFAULT_CALLBACK
from config import apply_config, conf
from dircache import DirCache
from transaction import Transaction
from utils import _unstrip_protocol, glob_translate, isfilelike, other_paths, read_block, stringify_path, tokenize
logger = logging.getLogger('fsspec')

def make_instance(cls, args, kwargs):
    pass
# WARNING: Decompyle incomplete


class _Cached(type):
    pass
# WARNING: Decompyle incomplete


def AbstractFileSystem():
    '''AbstractFileSystem'''
    __doc__ = '\n    An abstract super-class for pythonic file-systems\n\n    Implementations are expected to be compatible with or, better, subclass\n    from here.\n    '
    cachable = True
    _cached = False
    blocksize = 4194304
    sep = '/'
    protocol: 'ClassVar[str | tuple[str, ...]]' = 'abstract'
    _latest = None
    async_impl = False
    mirror_sync_methods = False
    root_marker = ''
    transaction_type = Transaction
    _extra_tokenize_attributes = ()
    storage_options: 'dict[str, Any]' = ()
    
    def __init__(self, *args, **storage_options):
        '''Create and configure file-system instance

        Instances may be cachable, so if similar enough arguments are seen
        a new instance is not required. The token attribute exists to allow
        implementations to cache instances if they wish.

        A reasonable default should be provided if there are no arguments.

        Subclasses should call this method.

        Parameters
        ----------
        use_listings_cache, listings_expiry_time, max_paths:
            passed to ``DirCache``, if the implementation supports
            directory listing caching. Pass use_listings_cache=False
            to disable such caching.
        skip_instance_cache: bool
            If this is a cachable implementation, pass True here to force
            creating a new instance even if a matching instance exists, and prevent
            storing this instance.
        asynchronous: bool
        loop: asyncio-compatible IOLoop or None
        '''
        if self._cached:
            return None
        self._cached = None
        self._intrans = False
        self._transaction = None
        self._invalidated_caches_in_transaction = []
    # WARNING: Decompyle incomplete

    fsid = (lambda self: raise NotImplementedError)()
    _fs_token = (lambda self: self._fs_token_)()
    
    def __dask_tokenize__(self):
        return self._fs_token

    
    def __hash__(self):
        return int(self._fs_token, 16)

    
    def __eq__(self, other):
