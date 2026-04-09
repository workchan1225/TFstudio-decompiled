# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functional_validators.pyc (Python 3.11)

__doc__ = 'This module contains related classes and functions for validation.'
from __future__ import annotations as _annotations
import dataclasses
import sys
import warnings
from functools import partialmethod
from types import FunctionType
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, TypeVar, Union, cast, overload
from pydantic_core import PydanticUndefined, core_schema
from typing_extensions import Self, TypeAlias
from _internal import _decorators, _generics, _internal_dataclass
from annotated_handlers import GetCoreSchemaHandler
from errors import PydanticUserError
from version import version_short
from warnings import ArbitraryTypeWarning, PydanticDeprecatedSince212
if sys.version_info < (3, 11):
    from typing_extensions import Protocol
else:
    from typing import Protocol
_inspect_validator = _decorators.inspect_validator
# WARNING: Decompyle incomplete
