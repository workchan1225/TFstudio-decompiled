# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference.pyc (Python 3.11)

import base64
import collections
import io
import itertools
import logging
import math
import os
from functools import lru_cache
from itertools import chain
from typing import TYPE_CHECKING, Literal
import fsspec.core as fsspec
from fsspec.spec import AbstractBufferedFile

try:
    import ujson as json
except ImportError:
    if not TYPE_CHECKING:
        import json

from fsspec.asyn import AsyncFileSystem
from fsspec.callbacks import DEFAULT_CALLBACK
from fsspec.core import filesystem, open, split_protocol
from fsspec.implementations.asyn_wrapper import AsyncFileSystemWrapper
from fsspec.utils import isfilelike, merge_offset_ranges, other_paths
logger = logging.getLogger('fsspec.reference')

class ReferenceNotReachable(RuntimeError):
    pass
# WARNING: Decompyle incomplete


def _first(d):
    return next(iter(d.values()))


def _prot_in_references(path, references):
    ref = references.get(path)
    if isinstance(ref, (list, tuple)) or isinstance(ref[0], str):
        return split_protocol(ref[0])[0] if ref[0] else ref[0]
    return None


def _protocol_groups(paths, references):
    if isinstance(paths, str):
        return {
            _prot_in_references(paths, references): [
                paths] }
    out = None
    for path in paths:
        protocol = _prot_in_references(path, references)
        out.setdefault(protocol, []).append(path)
        return out


class RefsValuesView(collections.abc.ValuesView):
    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete



class RefsItemsView(collections.abc.ItemsView):
    
    def __iter__(self):
        return zip(self._mapping.keys(), self._mapping.values())



def ravel_multi_index(idx, sizes):
    val = 0
    mult = 1
    for i, s in zip(idx[::-1], sizes[::-1]):
        val += i * mult
        mult *= s
        return val


class LazyReferenceMapper(collections.abc.MutableMapping):
    """This interface can be used to read/write references from Parquet stores.
    It is not intended for other types of references.
    It can be used with Kerchunk's MultiZarrToZarr method to combine
    references into a parquet store.
    Examples of this use-case can be found here:
    https://fsspec.github.io/kerchunk/advanced.html?highlight=parquet#parquet-storage"""
    np = (lambda self: import numpy as npnp)()
    pd = (lambda self: import pandas as pdpd)()
    
    def __init__(self, root, fs = None, out_root = property, cache_size = property, categorical_threshold = (None, None, 128, 10, 'fastparquet'), engine = ('engine', Literal[('fastparquet', 'pyarrow')])):
        '''

        This instance will be writable, storing changes in memory until full partitions
        are accumulated or .flush() is called.

        To create an empty lazy store, use .create()

        Parameters
        ----------
        root : str
            Root of parquet store
        fs : fsspec.AbstractFileSystem
            fsspec filesystem object, default is local filesystem.
        cache_size : int, default=128
            Maximum size of LRU cache, where cache_size*record_size denotes
            the total number of references that can be loaded in memory at once.
        categorical_threshold : int
            Encode urls as pandas.Categorical to reduce memory footprint if the ratio
            of the number of unique urls to total number of refs for each variable
            is greater than or equal to this number. (default 10)
        engine: Literal["fastparquet","pyarrow"]
            Engine choice for reading parquet files. (default is "fastparquet")
        '''
        self.root = root
        self.chunk_sizes = { }
        self.cat_thresh = categorical_threshold
        self.engine = engine
        self.cache_size = cache_size
        self.url = self.root + '/{field}/refs.{record}.parq'
    # WARNING: Decompyle incomplete

    
    def __getattr__(self, item):
        if item in ('_items', 'record_size', 'zmetadata'):
            self.setup()
            return self.__dict__[item]
        raise None(item)

    
    def setup(self):
        pass
    # WARNING: Decompyle incomplete

    create = (lambda root, storage_options, fs, record_size = (None, None, 10000): met = {
'metadata': { },
'record_size': record_size }# WARNING: Decompyle incomplete
)()
    listdir = (lambda self: dirs = self.zmetadata()set(dirs))()
    
    def ls(self, path, detail = ('', True)):
        '''Shortcut file listings'''
        pass
    # WARNING: Decompyle incomplete

    
    def _load_one_key(self, key):
        '''Get the reference for one key

        Returns bytes, one-element list or three-element list.
        '''
        pass
    # WARNING: Decompyle incomplete

    _key_to_record = (lambda self, key:
