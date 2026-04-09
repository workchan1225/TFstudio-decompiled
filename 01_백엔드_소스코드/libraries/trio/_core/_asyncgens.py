# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _asyncgens.pyc (Python 3.11)

from __future__ import annotations
import logging
import sys
import warnings
import weakref
from typing import TYPE_CHECKING, NoReturn, TypeVar
import attrs
from  import _core
from _util import name_asyncgen
from  import _run
ASYNCGEN_LOGGER = logging.getLogger('trio.async_generator_errors')
if TYPE_CHECKING:
    from collections.abc import Callable
    from types import AsyncGeneratorType
    from typing_extensions import ParamSpec
    _P = ParamSpec('_P')
    _WEAK_ASYNC_GEN_SET = weakref.WeakSet[AsyncGeneratorType[(object, NoReturn)]]
    _ASYNC_GEN_SET = set[AsyncGeneratorType[(object, NoReturn)]]
else:
    _WEAK_ASYNC_GEN_SET = weakref.WeakSet
    _ASYNC_GEN_SET = set
_R = TypeVar('_R')
_call_without_ki_protection = (lambda f = None: pass# WARNING: Decompyle incomplete
)()
AsyncGenerators = <NODE:12>()
