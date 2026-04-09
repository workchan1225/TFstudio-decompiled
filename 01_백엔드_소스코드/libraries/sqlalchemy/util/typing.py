# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing.pyc (Python 3.11)

from __future__ import annotations
import builtins
from collections import deque
from collections.abc import abc as collections_abc
import re
import sys
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import ForwardRef
from typing import Generic
from typing import Iterable
from typing import Mapping
from typing import NewType
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import typing_extensions
from  import compat
from typing_extensions import Annotated
from typing_extensions import Concatenate
from typing_extensions import dataclass_transform
from typing_extensions import Final
from typing_extensions import final
from typing_extensions import get_args
from typing_extensions import get_origin
from typing_extensions import Literal
from typing_extensions import NotRequired
from typing_extensions import ParamSpec
from typing_extensions import Protocol
from typing_extensions import SupportsIndex
from typing_extensions import TypeAlias
from typing_extensions import TypedDict
from typing_extensions import TypeGuard
from typing_extensions import Self
from typing_extensions import TypeAliasType
from typing_extensions import Never
from typing_extensions import LiteralString
_T = TypeVar('_T', bound = Any)
_KT = TypeVar('_KT')
_KT_co = TypeVar('_KT_co', covariant = True)
_KT_contra = TypeVar('_KT_contra', contravariant = True)
_VT = TypeVar('_VT')
_VT_co = TypeVar('_VT_co', covariant = True)
if compat.py310:
    from types import NoneType
else:
    NoneType = type(None)

def is_fwd_none(typ = None):
