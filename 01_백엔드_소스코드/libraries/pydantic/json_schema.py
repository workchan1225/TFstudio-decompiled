# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json_schema.pyc (Python 3.11)

__doc__ = '!!! abstract "Usage Documentation"\n    [JSON Schema](../concepts/json_schema.md)\n\nThe `json_schema` module contains classes and functions to allow the way [JSON Schema](https://json-schema.org/)\nis generated to be customized.\n\nIn general you shouldn\'t need to use this module directly; instead, you can use\n[`BaseModel.model_json_schema`][pydantic.BaseModel.model_json_schema] and\n[`TypeAdapter.json_schema`][pydantic.TypeAdapter.json_schema].\n'
from __future__ import annotations as _annotations
import dataclasses
import inspect
import math
import os
import re
import warnings
from collections import Counter, defaultdict
from collections.abc import Hashable, Iterable, Sequence
from copy import deepcopy
from enum import Enum
from re import Pattern
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, NewType, TypeVar, Union, cast, overload
import pydantic_core
from pydantic_core import MISSING, CoreSchema, PydanticOmit, core_schema, to_jsonable_python
from pydantic_core.core_schema import ComputedField
from typing_extensions import TypeAlias, assert_never, deprecated, final
from typing_inspection.introspection import get_literal_values
from pydantic.warnings import PydanticDeprecatedSince26, PydanticDeprecatedSince29
from _internal import _config, _core_metadata, _core_utils, _decorators, _internal_dataclass, _mock_val_ser, _schema_generation_shared
from annotated_handlers import GetJsonSchemaHandler
from config import JsonDict, JsonValue
from errors import PydanticInvalidForJsonSchema, PydanticSchemaGenerationError, PydanticUserError
if TYPE_CHECKING:
    from  import ConfigDict
    from _internal._core_utils import CoreSchemaField, CoreSchemaOrField
    from _internal._dataclasses import PydanticDataclass
    from _internal._schema_generation_shared import GetJsonSchemaFunction
    from main import BaseModel
CoreSchemaOrFieldType = Literal[(core_schema.CoreSchemaType, core_schema.CoreSchemaFieldType)]
JsonSchemaValue = dict[(str, Any)]
JsonSchemaMode = Literal[('validation', 'serialization')]
_MODE_TITLE_MAPPING: 'dict[JsonSchemaMode, str]' = {
    'validation': 'Input',
    'serialization': 'Output' }
JsonSchemaWarningKind = Literal[('skipped-choice', 'non-serializable-default', 'skipped-discriminator')]

class PydanticJsonSchemaWarning(UserWarning):
    '''This class is used to emit warnings produced during JSON schema generation.
    See the [`GenerateJsonSchema.emit_warning`][pydantic.json_schema.GenerateJsonSchema.emit_warning] and
    [`GenerateJsonSchema.render_warning_message`][pydantic.json_schema.GenerateJsonSchema.render_warning_message]
    methods for more details; these can be overridden to control warning behavior.
    '''
    pass

NoDefault = object()
DEFAULT_REF_TEMPLATE = '#/$defs/{model}'
CoreRef = NewType('CoreRef', str)
DefsRef = NewType('DefsRef', str)
JsonRef = NewType('JsonRef', str)
CoreModeRef = tuple[(CoreRef, JsonSchemaMode)]
JsonSchemaKeyT = TypeVar('JsonSchemaKeyT', bound = Hashable)
_PRIMITIVE_JSON_SCHEMA_TYPES = ('string', 'boolean', 'null', 'integer', 'number')
# WARNING: Decompyle incomplete
