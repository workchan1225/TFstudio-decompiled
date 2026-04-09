# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _path.pyc (Python 3.11)

from __future__ import annotations
import os
import pathlib
import sys
from functools import partial, update_wrapper
from inspect import cleandoc
from typing import IO, TYPE_CHECKING, Any, BinaryIO, ClassVar, Concatenate, Literal, TypeVar, overload
from trio._file_io import AsyncIOWrapper, wrap_file
from trio._util import final
from trio.to_thread import run_sync
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Iterable
    from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
    from _typeshed import OpenBinaryMode, OpenBinaryModeReading, OpenBinaryModeUpdating, OpenBinaryModeWriting, OpenTextMode
    from typing_extensions import ParamSpec, Self
    P = ParamSpec('P')
    PathT = TypeVar('PathT', bound = 'Path')
    T = TypeVar('T')

def _wraps_async(wrapped = None):
    pass
# WARNING: Decompyle incomplete


def _wrap_method(fn = None):
    pass
# WARNING: Decompyle incomplete


def _wrap_method_path(fn = None):
    pass
# WARNING: Decompyle incomplete


def _wrap_method_path_iterable(fn = None):
    pass
# WARNING: Decompyle incomplete


class Path(pathlib.PurePath):
    pass
# WARNING: Decompyle incomplete

if Path.relative_to.__doc__:
    Path.relative_to.__doc__ = Path.relative_to.__doc__.replace(' `..` ', ' ``..`` ')
PosixPath = <NODE:12>()
WindowsPath = <NODE:12>()
