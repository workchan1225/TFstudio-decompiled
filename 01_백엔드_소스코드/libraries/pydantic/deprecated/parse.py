# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse.pyc (Python 3.11)

from __future__ import annotations
import json
import pickle
import warnings
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable
from typing_extensions import deprecated
from warnings import PydanticDeprecatedSince20
if not TYPE_CHECKING:
    DeprecationWarning = PydanticDeprecatedSince20

class Protocol(Enum, str):
    json = 'json'
    pickle = 'pickle'

load_str_bytes = (lambda b = None, *, content_type: warnings.warn('`load_str_bytes` is deprecated.', category = PydanticDeprecatedSince20, stacklevel = 2)# WARNING: Decompyle incomplete
)()
load_file = (lambda path = None, *, content_type: warnings.warn('`load_file` is deprecated.', category = PydanticDeprecatedSince20, stacklevel = 2)path = Path(path)b = path.read_bytes()# WARNING: Decompyle incomplete
)()
