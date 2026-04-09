# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _decorators.pyc (Python 3.11)

__doc__ = 'Logic related to validators applied to models etc. via the `@field_validator` and `@model_validator` decorators.'
from __future__ import annotations as _annotations
import sys
import types
from collections import deque
from collections.abc import Iterable
from dataclasses import dataclass, field
from functools import cached_property, partial, partialmethod
from inspect import Parameter, Signature, isdatadescriptor, ismethoddescriptor, signature
from itertools import islice
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Generic, Literal, TypeVar, Union
from pydantic_core import PydanticUndefined, PydanticUndefinedType, core_schema
from typing_extensions import TypeAlias, is_typeddict
from errors import PydanticUserError
from _core_utils import get_type_ref
from _internal_dataclass import slots_true
from _namespace_utils import GlobalsNamespace, MappingNamespace
from _typing_extra import get_function_type_hints
from _utils import can_be_positional
if TYPE_CHECKING:
    from fields import ComputedFieldInfo
    from functional_validators import FieldValidatorModes
    from _config import ConfigWrapper
# WARNING: Decompyle incomplete
