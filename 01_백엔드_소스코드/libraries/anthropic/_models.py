# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _models.pyc (Python 3.11)

from __future__ import annotations
import os
import inspect
import weakref
from typing import TYPE_CHECKING, Any, Type, Union, Generic, TypeVar, Callable, Optional, cast
from datetime import date, datetime
from typing_extensions import List, Unpack, Literal, ClassVar, Protocol, Required, ParamSpec, TypedDict, TypeGuard, final, override, runtime_checkable
import pydantic
from pydantic.fields import FieldInfo
from _types import Body, IncEx, Query, ModelT, Headers, Timeout, NotGiven, AnyMapping, HttpxRequestFiles
from _utils import PropertyInfo, is_list, is_given, json_safe, lru_cache, is_mapping, parse_date, coerce_boolean, parse_datetime, strip_not_given, extract_type_arg, is_annotated_type, is_type_alias_type, strip_annotated_type
from _compat import PYDANTIC_V1, ConfigDict, GenericModel as BaseGenericModel, get_args, is_union, parse_obj, get_origin, is_literal_type, get_model_config, get_model_fields, field_get_default
from _constants import RAW_RESPONSE_HEADER
if TYPE_CHECKING:
    from pydantic_core.core_schema import ModelField, ModelSchema, LiteralSchema, ModelFieldsSchema
__all__ = [
    'BaseModel',
    'GenericModel']
_T = TypeVar('_T')
_BaseModelT = TypeVar('_BaseModelT', bound = 'BaseModel')
P = ParamSpec('P')
_ConfigProtocol = <NODE:12>()

class BaseModel(pydantic.BaseModel):
    pass
# WARNING: Decompyle incomplete


def _construct_field(value = None, field = runtime_checkable, key = None):
    pass
# WARNING: Decompyle incomplete


def _get_extra_fields_type(cls = None):
