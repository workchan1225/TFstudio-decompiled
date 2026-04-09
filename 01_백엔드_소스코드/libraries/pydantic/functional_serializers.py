# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functional_serializers.pyc (Python 3.11)

__doc__ = 'This module contains related classes and functions for serialization.'
from __future__ import annotations
import dataclasses
from functools import partial, partialmethod
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, TypeVar, overload
from pydantic_core import PydanticUndefined, core_schema
from pydantic_core.core_schema import SerializationInfo, SerializerFunctionWrapHandler, WhenUsed
from typing_extensions import TypeAlias
from  import PydanticUndefinedAnnotation
from _internal import _decorators, _internal_dataclass
from annotated_handlers import GetCoreSchemaHandler
# WARNING: Decompyle incomplete
