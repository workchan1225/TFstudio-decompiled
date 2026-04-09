# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

from __future__ import annotations
import os
import re
import inspect
import functools
from typing import Any, Tuple, Mapping, TypeVar, Callable, Iterable, Sequence, cast, overload
from pathlib import Path
from datetime import date, datetime
from typing_extensions import TypeGuard
import sniffio
from _types import Omit, NotGiven, FileTypes, HeadersLike
_T = TypeVar('_T')
_TupleT = TypeVar('_TupleT', bound = Tuple[(object, ...)])
_MappingT = TypeVar('_MappingT', bound = Mapping[(str, object)])
_SequenceT = TypeVar('_SequenceT', bound = Sequence[object])
CallableT = TypeVar('CallableT', bound = Callable[(..., Any)])

def flatten(t = None):
    return t()


def extract_files(query = None, *, paths):
    """Recursively extract files from the given dictionary based on specified paths.

    A path may look like this ['foo', 'files', '<array>', 'data'].

    Note: this mutates the given dictionary.
    """
    files = []
    for path in paths:
        files.extend(_extract_items(query, path, index = 0, flattened_key = None))
        return files


def _extract_items(obj = None, path = None, *, index, flattened_key):
    pass
# WARNING: Decompyle incomplete


def is_given(obj = None):
