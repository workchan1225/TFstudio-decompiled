# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libarchive.pyc (Python 3.11)

from contextlib import contextmanager
from ctypes import CFUNCTYPE, POINTER, c_int, c_longlong, c_void_p, cast, create_string_buffer
import libarchive
from libarchive.ffi import ffi
from fsspec import open_files
from fsspec.archive import AbstractArchiveFileSystem
from fsspec.implementations.memory import MemoryFile
from fsspec.utils import DEFAULT_BLOCK_SIZE
SEEK_CALLBACK = CFUNCTYPE(c_longlong, c_int, c_void_p, c_longlong, c_int)
read_set_seek_callback = ffi.ffi('read_set_seek_callback', [
    ffi.c_archive_p,
    SEEK_CALLBACK], c_int, ffi.check_int)
new_api = hasattr(ffi, 'NO_OPEN_CB')
custom_reader = (lambda file, format_name, filter_name, block_size = ('all', 'all', ffi.page_size): pass# WARNING: Decompyle incomplete
)()

class LibArchiveFileSystem(AbstractArchiveFileSystem):
    pass
# WARNING: Decompyle incomplete
