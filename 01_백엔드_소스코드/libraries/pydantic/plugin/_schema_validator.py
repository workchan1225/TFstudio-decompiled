# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _schema_validator.pyc (Python 3.11)

'''Pluggable schema validator for pydantic.'''
from __future__ import annotations
import functools
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Callable, Literal, TypeVar
from pydantic_core import CoreConfig, CoreSchema, SchemaValidator, ValidationError
from typing_extensions import ParamSpec
if TYPE_CHECKING:
    from  import BaseValidateHandlerProtocol, PydanticPluginProtocol, SchemaKind, SchemaTypePath
P = ParamSpec('P')
R = TypeVar('R')
Event = Literal[('on_validate_python', 'on_validate_json', 'on_validate_strings')]
events: 'list[Event]' = list(Event.__args__)

def create_schema_validator(schema, schema_type, schema_type_module = None, schema_type_name = None, schema_kind = None, config = (None, None), plugin_settings = ('schema', 'CoreSchema', 'schema_type', 'Any', 'schema_type_module', 'str', 'schema_type_name', 'str', 'schema_kind', 'SchemaKind', 'config', 'CoreConfig | None', 'plugin_settings', 'dict[str, Any] | None', 'return', 'SchemaValidator | PluggableSchemaValidator')):
