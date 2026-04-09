# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arrow.pyc (Python 3.11)

import errno
import io
import os
import secrets
import shutil
from contextlib import suppress
from functools import cached_property, wraps
from urllib.parse import parse_qs
from fsspec.spec import AbstractFileSystem
from fsspec.utils import get_package_version_without_import, infer_storage_options, mirror_from, tokenize

def wrap_exceptions(func):
    pass
# WARNING: Decompyle incomplete

PYARROW_VERSION = None

class ArrowFSWrapper(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete

ArrowFile = <NODE:12>()

class HadoopFileSystem(ArrowFSWrapper):
    pass
# WARNING: Decompyle incomplete
