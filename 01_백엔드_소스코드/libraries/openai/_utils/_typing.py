# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
import sys
import typing
import typing_extensions
from typing import Any, TypeVar, Iterable, cast
from collections import abc as _c_abc
from typing_extensions import TypeIs, Required, Annotated, get_args, get_origin
from _utils import lru_cache
from _types import InheritsGeneric
from _compat import is_union as _is_union

def is_annotated_type(typ = None):
    return get_origin(typ) == Annotated


def is_list_type(typ = None):
