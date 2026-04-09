# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

'''Python version compatibility code and random general utilities.'''
from __future__ import annotations
from collections.abc import Callable
import enum
import functools
import inspect
from inspect import Parameter
from inspect import Signature
import os
from pathlib import Path
import sys
from typing import Any
from typing import Final
from typing import NoReturn
import py
if sys.version_info >= (3, 14):
    from annotationlib import Format
LEGACY_PATH = py.path.local

def legacy_path(path = None):
    '''Internal wrapper to prepare lazy proxies for legacy_path instances'''
    return LEGACY_PATH(path)


class NotSetType(enum.Enum):
    token = 0

NOTSET: 'Final' = NotSetType.token

def iscoroutinefunction(func = None):
