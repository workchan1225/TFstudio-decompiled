# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pathlib.pyc (Python 3.11)

from __future__ import annotations
import atexit
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
import contextlib
from enum import Enum
from errno import EBADF
from errno import ELOOP
from errno import ENOENT
from errno import ENOTDIR
import fnmatch
from functools import partial
from importlib.machinery import ModuleSpec
from importlib.machinery import PathFinder
import importlib.util as importlib
import itertools
import os
from os.path import expanduser
from os.path import expandvars
from os.path import isabs
from os.path import sep
from pathlib import Path
from pathlib import PurePath
from posixpath import sep as posix_sep
import shutil
import sys
import types
from types import ModuleType
from typing import Any
from typing import TypeVar
import uuid
import warnings
from _pytest.compat import assert_never
from _pytest.outcomes import skip
from _pytest.warning_types import PytestWarning
if sys.version_info < (3, 11):
    from importlib._bootstrap_external import _NamespaceLoader as NamespaceLoader
else:
    from importlib.machinery import NamespaceLoader
LOCK_TIMEOUT = 259200
_AnyPurePath = TypeVar('_AnyPurePath', bound = PurePath)
_IGNORED_ERRORS = (ENOENT, ENOTDIR, EBADF, ELOOP)
_IGNORED_WINERRORS = (21, 1921)

def _ignore_error(exception = None):
