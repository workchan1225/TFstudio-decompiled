# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _generate_schema.pyc (Python 3.11)

'''Convert python types to pydantic-core schema.'''
from __future__ import annotations as _annotations
import collections.abc as collections
import dataclasses
import datetime
import inspect
import os
import pathlib
import re
import sys
import typing
import warnings
from collections.abc import Generator, Iterable, Iterator, Mapping
from contextlib import contextmanager
from copy import copy
from decimal import Decimal
from enum import Enum
from fractions import Fraction
from functools import partial
from inspect import Parameter, _ParameterKind, signature
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from itertools import chain
from operator import attrgetter
from types import FunctionType, GenericAlias, LambdaType, MethodType
from typing import TYPE_CHECKING, Any, Callable, Final, ForwardRef, Literal, TypeVar, Union, cast, overload
from uuid import UUID
from zoneinfo import ZoneInfo
import typing_extensions
from pydantic_core import MISSING, CoreSchema, MultiHostUrl, PydanticCustomError, PydanticSerializationUnexpectedValue, PydanticUndefined, Url, core_schema, to_jsonable_python
from typing_extensions import TypeAlias, TypeAliasType, get_args, get_origin, is_typeddict
from typing_inspection import typing_objects
from typing_inspection.introspection import AnnotationSource, get_literal_values, is_union_origin
from aliases import AliasChoices, AliasPath
from annotated_handlers import GetCoreSchemaHandler, GetJsonSchemaHandler
from config import ConfigDict, JsonDict, JsonEncoder, JsonSchemaExtraCallable
from errors import PydanticSchemaGenerationError, PydanticUndefinedAnnotation, PydanticUserError
from functional_validators import AfterValidator, BeforeValidator, FieldValidatorModes, PlainValidator, WrapValidator
from json_schema import JsonSchemaValue
from version import version_short
from warnings import ArbitraryTypeWarning, PydanticDeprecatedSince20, TypedDictExtraConfigWarning, UnsupportedFieldAttributeWarning
from  import _decorators, _discriminated_union, _known_annotated_metadata, _repr, _typing_extra
from _config import ConfigWrapper, ConfigWrapperStack
from _core_metadata import CoreMetadata, update_core_metadata
from _core_utils import get_ref, get_type_ref, is_list_like_schema_with_items_schema
from _decorators import Decorator, DecoratorInfos, FieldSerializerDecoratorInfo, FieldValidatorDecoratorInfo, ModelSerializerDecoratorInfo, ModelValidatorDecoratorInfo, RootValidatorDecoratorInfo, ValidatorDecoratorInfo, get_attribute_from_bases, inspect_field_serializer, inspect_model_serializer, inspect_validator
from _docs_extraction import extract_docstrings_from_cls
from _fields import collect_dataclass_fields, rebuild_dataclass_fields, rebuild_model_fields, takes_validated_data_argument, update_field_from_config
from _forward_ref import PydanticRecursiveRef
from _generics import get_standard_typevars_map, replace_types
from _import_utils import import_cached_base_model, import_cached_field_info
from _mock_val_ser import MockCoreSchema
from _namespace_utils import NamespacesTuple, NsResolver
from _schema_gather import MissingDefinitionError, gather_schemas_for_cleaning
from _schema_generation_shared import CallbackGetCoreSchemaHandler
from _utils import lenient_issubclass, smart_deepcopy
if TYPE_CHECKING:
    from fields import ComputedFieldInfo, FieldInfo
    from main import BaseModel
    from types import Discriminator
    from _dataclasses import StandardDataclass
    from _schema_generation_shared import GetJsonSchemaFunction
_SUPPORTS_TYPEDDICT = sys.version_info >= (3, 12)
FieldDecoratorInfo = Union[(ValidatorDecoratorInfo, FieldValidatorDecoratorInfo, FieldSerializerDecoratorInfo)]
FieldDecoratorInfoType = TypeVar('FieldDecoratorInfoType', bound = FieldDecoratorInfo)
AnyFieldDecorator = Union[(Decorator[ValidatorDecoratorInfo], Decorator[FieldValidatorDecoratorInfo], Decorator[FieldSerializerDecoratorInfo])]
ModifyCoreSchemaWrapHandler: 'TypeAlias' = GetCoreSchemaHandler
GetCoreSchemaFunction: 'TypeAlias' = Callable[([
    Any,
    ModifyCoreSchemaWrapHandler], core_schema.CoreSchema)]
ParametersCallback: 'TypeAlias' = "Callable[[int, str, Any], Literal['skip'] | None]"
TUPLE_TYPES: 'list[type]' = [
    typing.Tuple,
    tuple]
LIST_TYPES: 'list[type]' = [
    typing.List,
    list,
    collections.abc.MutableSequence]
SET_TYPES: 'list[type]' = [
    typing.Set,
    set,
    collections.abc.MutableSet]
FROZEN_SET_TYPES: 'list[type]' = [
    typing.FrozenSet,
    frozenset,
    collections.abc.Set]
DICT_TYPES: 'list[type]' = [
    typing.Dict,
    dict]
IP_TYPES: 'list[type]' = [
    IPv4Address,
    IPv4Interface,
    IPv4Network,
    IPv6Address,
    IPv6Interface,
    IPv6Network]
SEQUENCE_TYPES: 'list[type]' = [
    typing.Sequence,
    collections.abc.Sequence]
ITERABLE_TYPES: 'list[type]' = [
    typing.Iterable,
    collections.abc.Iterable,
    typing.Generator,
    collections.abc.Generator]
TYPE_TYPES: 'list[type]' = [
    typing.Type,
    type]
PATTERN_TYPES: 'list[type]' = [
    typing.Pattern,
    re.Pattern]
PATH_TYPES: 'list[type]' = [
    os.PathLike,
    pathlib.Path,
    pathlib.PurePath,
    pathlib.PosixPath,
    pathlib.PurePosixPath,
    pathlib.PureWindowsPath]
MAPPING_TYPES = [
    typing.Mapping,
    typing.MutableMapping,
    collections.abc.Mapping,
    collections.abc.MutableMapping,
    collections.OrderedDict,
    typing_extensions.OrderedDict,
    typing.DefaultDict,
    collections.defaultdict]
COUNTER_TYPES = [
    collections.Counter,
    typing.Counter]
DEQUE_TYPES: 'list[type]' = [
    collections.deque,
    typing.Deque]
ValidateCallSupportedTypes = Union[(LambdaType, FunctionType, MethodType, partial)]
VALIDATE_CALL_SUPPORTED_TYPES = get_args(ValidateCallSupportedTypes)
UNSUPPORTED_STANDALONE_FIELDINFO_ATTRIBUTES: 'list[tuple[str, Any]]' = [
    ('alias', None),
    ('validation_alias', None),
    ('serialization_alias', None),
    ('default', PydanticUndefined),
    ('default_factory', None),
    ('exclude', None),
    ('deprecated', None),
    ('repr', True),
    ('validate_default', None),
    ('frozen', None),
    ('init', None),
    ('init_var', None),
    ('kw_only', None)]
_mode_to_validator: 'dict[FieldValidatorModes, type[BeforeValidator | AfterValidator | PlainValidator | WrapValidator]]' = {
    'before': BeforeValidator,
    'after': AfterValidator,
    'plain': PlainValidator,
    'wrap': WrapValidator }

def check_validator_fields_against_field_name(info = None, field = None):
