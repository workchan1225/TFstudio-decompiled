# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generic.pyc (Python 3.11)

from __future__ import annotations
import inspect
import logging
import os
import shutil
import uuid
from asyn import AsyncFileSystem, _run_coros_in_chunks, sync_wrapper
from callbacks import DEFAULT_CALLBACK
from core import filesystem, get_filesystem_class, split_protocol, url_to_fs
_generic_fs = { }
logger = logging.getLogger('fsspec.generic')

def set_generic_fs(protocol, **storage_options):
    '''Populate the dict used for method=="generic" lookups'''
    pass
# WARNING: Decompyle incomplete


def _resolve_fs(url, method, protocol, storage_options = (None, None)):
    '''Pick instance of backend FS'''
    url = url[0] if isinstance(url, (list, tuple)) else url
# WARNING: Decompyle incomplete


def rsync(source, destination, delete_missing, source_field, dest_field, update_cond, inst_kwargs, fs = (False, 'size', 'size', 'different', None, None), **kwargs):
    '''Sync files between two directory trees

    (experimental)

    Parameters
    ----------
    source: str
        Root of the directory tree to take files from. This must be a directory, but
        do not include any terminating "/" character
    destination: str
        Root path to copy into. The contents of this location should be
        identical to the contents of ``source`` when done. This will be made a
        directory, and the terminal "/" should not be included.
    delete_missing: bool
        If there are paths in the destination that don\'t exist in the
        source and this is True, delete them. Otherwise, leave them alone.
    source_field: str | callable
        If ``update_field`` is "different", this is the key in the info
        of source files to consider for difference. Maybe a function of the
        info dict.
    dest_field: str | callable
        If ``update_field`` is "different", this is the key in the info
        of destination files to consider for difference. May be a function of
        the info dict.
    update_cond: "different"|"always"|"never"
        If "always", every file is copied, regardless of whether it exists in
        the destination. If "never", files that exist in the destination are
        not copied again. If "different" (default), only copy if the info
        fields given by ``source_field`` and ``dest_field`` (usually "size")
        are different. Other comparisons may be added in the future.
    inst_kwargs: dict|None
        If ``fs`` is None, use this set of keyword arguments to make a
        GenericFileSystem instance
    fs: GenericFileSystem|None
        Instance to use if explicitly given. The instance defines how to
        to make downstream file system instances from paths.

    Returns
    -------
    dict of the copy operations that were performed, {source: destination}
    '''
    pass
# WARNING: Decompyle incomplete


class GenericFileSystem(AsyncFileSystem):
    pass
# WARNING: Decompyle incomplete


async def copy_file_op(fs1, url1, fs2, url2, tempdir, batch_size, on_error = (None, 20, 'ignore')):
    pass
# WARNING: Decompyle incomplete


async def _copy_file_op(fs1, url1, fs2, url2, local, on_error = ('ignore',)):
    pass
# WARNING: Decompyle incomplete


async def maybe_await(cor):
    pass
# WARNING: Decompyle incomplete
