# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing_extra.pyc (Python 3.11)

"""Logic for interacting with type annotations, mostly extensions, shims and hacks to wrap Python's typing module."""
from __future__ import annotations
import collections.abc as collections
import re
import sys
import types
import typing
from functools import partial
from typing import TYPE_CHECKING, Any, Callable, cast
import typing_extensions
from typing_extensions import deprecated, get_args, get_origin
from typing_inspection import typing_objects
from typing_inspection.introspection import is_union_origin
from pydantic.version import version_short
from _namespace_utils import GlobalsNamespace, MappingNamespace, NsResolver, get_module_ns_of
if sys.version_info < (3, 10):
    NoneType = type(None)
    EllipsisType = type(Ellipsis)
else:
    from types import EllipsisType
    from types import NoneType
if sys.version_info >= (3, 14):
    import annotationlib
if TYPE_CHECKING:
    from pydantic import BaseModel
_t_annotated = typing.Annotated
_te_annotated = typing_extensions.Annotated

def is_annotated(tp = None):
