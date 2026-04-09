# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import sys as _sys
from typing import Any as _Any
from typing_extensions import Sentinel
from _pydantic_core import ArgsKwargs, MultiHostUrl, PydanticCustomError, PydanticKnownError, PydanticOmit, PydanticSerializationError, PydanticSerializationUnexpectedValue, PydanticUndefined, PydanticUndefinedType, PydanticUseDefault, SchemaError, SchemaSerializer, SchemaValidator, Some, TzInfo, Url, ValidationError, __version__, from_json, to_json, to_jsonable_python
from core_schema import CoreConfig, CoreSchema, CoreSchemaType, ErrorType
if _sys.version_info < (3, 11):
    from typing_extensions import NotRequired as _NotRequired
else:
    from typing import NotRequired as _NotRequired
if _sys.version_info < (3, 12):
    from typing_extensions import TypedDict as _TypedDict
else:
    from typing import TypedDict as _TypedDict
__all__ = [
    '__version__',
    'UNSET',
    'CoreConfig',
    'CoreSchema',
    'CoreSchemaType',
    'SchemaValidator',
    'SchemaSerializer',
    'Some',
    'Url',
    'MultiHostUrl',
    'ArgsKwargs',
    'PydanticUndefined',
    'PydanticUndefinedType',
    'SchemaError',
    'ErrorDetails',
    'InitErrorDetails',
    'ValidationError',
    'PydanticCustomError',
    'PydanticKnownError',
    'PydanticOmit',
    'PydanticUseDefault',
    'PydanticSerializationError',
    'PydanticSerializationUnexpectedValue',
    'TzInfo',
    'to_json',
    'from_json',
    'to_jsonable_python']

class ErrorDetails(_TypedDict):
    url: '_NotRequired[str]' = 'ErrorDetails'


class InitErrorDetails(_TypedDict):
    ctx: '_NotRequired[dict[str, _Any]]' = 'InitErrorDetails'


class ErrorTypeInfo(_TypedDict):
    example_context: 'dict[str, _Any] | None' = '\n    Gives information about errors.\n    '


class MultiHostHost(_TypedDict):
    port: 'int | None' = '\n    A host part of a multi-host URL.\n    '

MISSING = Sentinel('MISSING')
