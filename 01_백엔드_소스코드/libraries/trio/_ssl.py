# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ssl.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import operator as _operator
import ssl as _stdlib_ssl
from enum import Enum as _Enum
from typing import TYPE_CHECKING, Any, ClassVar, Final as TFinal, Generic, TypeVar
import trio
from  import _sync
from _highlevel_generic import aclose_forcefully
from _util import ConflictDetector, final
from abc import Listener, Stream
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
    from typing_extensions import TypeVarTuple, Unpack
    Ts = TypeVarTuple('Ts')
T = TypeVar('T')
STARTING_RECEIVE_SIZE: 'TFinal' = 16384

def _is_eof(exc = None):
