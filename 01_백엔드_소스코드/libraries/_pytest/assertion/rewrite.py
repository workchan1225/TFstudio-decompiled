# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rewrite.pyc (Python 3.11)

__doc__ = 'Rewrite assertion AST to produce nice error messages.'
from __future__ import annotations
import ast
from collections import defaultdict
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence
import errno
import functools
import importlib.abc as importlib
import importlib.machinery as importlib
import importlib.util as importlib
import io
import itertools
import marshal
import os
from pathlib import Path
from pathlib import PurePath
import struct
import sys
import tokenize
import types
from typing import IO
from typing import TYPE_CHECKING
if sys.version_info >= (3, 12):
    from importlib.resources.abc import TraversableResources
else:
    from importlib.abc import TraversableResources
if sys.version_info < (3, 11):
    from importlib.readers import FileReader
else:
    from importlib.resources.readers import FileReader
from _pytest._io.saferepr import DEFAULT_REPR_MAX_SIZE
from _pytest._io.saferepr import saferepr
from _pytest._io.saferepr import saferepr_unlimited
from _pytest._version import version
from _pytest.assertion import util
from _pytest.config import Config
from _pytest.fixtures import FixtureFunctionDefinition
from _pytest.main import Session
from _pytest.pathlib import absolutepath
from _pytest.pathlib import fnmatch_ex
from _pytest.stash import StashKey
from _pytest.assertion.util import format_explanation as _format_explanation
if TYPE_CHECKING:
    from _pytest.assertion import AssertionState

class Sentinel:
    pass

assertstate_key = StashKey['AssertionState']()
PYTEST_TAG = f'''{sys.implementation.cache_tag}-pytest-{version}'''
# WARNING: Decompyle incomplete
