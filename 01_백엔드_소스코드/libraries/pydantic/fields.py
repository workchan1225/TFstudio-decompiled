# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fields.pyc (Python 3.11)

__doc__ = 'Defining fields on models.'
from __future__ import annotations as _annotations
import dataclasses
import inspect
import re
import sys
from collections.abc import Callable, Mapping
from copy import copy
from dataclasses import Field as DataclassField
from functools import cached_property
from typing import TYPE_CHECKING, Annotated, Any, ClassVar, Literal, TypeVar, cast, final, overload
from warnings import warn
import annotated_types
import typing_extensions
from pydantic_core import MISSING, PydanticUndefined
from typing_extensions import Self, TypeAlias, TypedDict, Unpack, deprecated
from typing_inspection import typing_objects
from typing_inspection.introspection import UNKNOWN, AnnotationSource, ForbiddenQualifier, Qualifier, inspect_annotation
from  import types
from _internal import _decorators, _fields, _generics, _internal_dataclass, _repr, _typing_extra, _utils
from _internal._namespace_utils import GlobalsNamespace, MappingNamespace
from aliases import AliasChoices, AliasGenerator, AliasPath
from config import JsonDict
from errors import PydanticForbiddenQualifier, PydanticUserError
from json_schema import PydanticJsonSchemaWarning
from warnings import PydanticDeprecatedSince20
if TYPE_CHECKING:
    from _internal._config import ConfigWrapper
    from _internal._repr import ReprArgs
__all__ = ('Field', 'FieldInfo', 'PrivateAttr', 'computed_field')
_Unset: 'Any' = PydanticUndefined
if sys.version_info >= (3, 13):
    import warnings
    Deprecated: 'TypeAlias' = warnings.deprecated | deprecated
else:
    Deprecated: 'TypeAlias' = deprecated

def _FromFieldInfoInputs():
    '''_FromFieldInfoInputs'''
    fail_fast: 'bool | None' = 'This class exists solely to add type checking for the `**kwargs` in `FieldInfo.from_field`.'

_FromFieldInfoInputs = <NODE:27>(_FromFieldInfoInputs, '_FromFieldInfoInputs', TypedDict, total = False)

def _FieldInfoInputs():
    '''_FieldInfoInputs'''
    default: 'Any' = 'This class exists solely to add type checking for the `**kwargs` in `FieldInfo.__init__`.'

_FieldInfoInputs = <NODE:27>(_FieldInfoInputs, '_FieldInfoInputs', _FromFieldInfoInputs, total = False)

def _FieldInfoAsDict():
    '''_FieldInfoAsDict'''
    attributes: 'dict[str, Any]' = '_FieldInfoAsDict'

_FieldInfoAsDict = <NODE:27>(_FieldInfoAsDict, '_FieldInfoAsDict', TypedDict, closed = True)
FieldInfo = <NODE:12>()

class _EmptyKwargs(TypedDict):
    '''This class exists solely to ensure that type checking warns about passing `**extra` in `Field`.'''
    pass

# WARNING: Decompyle incomplete
