# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tar.pyc (Python 3.11)

import logging
import tarfile
import fsspec
from fsspec.archive import AbstractArchiveFileSystem
from fsspec.compression import compr
from fsspec.utils import infer_compression
typemap = {
    b'0': 'file',
    b'5': 'directory' }
logger = logging.getLogger('tar')

class TarFileSystem(AbstractArchiveFileSystem):
    pass
# WARNING: Decompyle incomplete
