# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

'''Logic for creating models.'''
from __future__ import annotations as _annotations
import operator
import sys
import types
import warnings
from collections.abc import Generator, Mapping
from copy import copy, deepcopy
from functools import cached_property
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Dict, Generic, Literal, TypeVar, Union, cast, overload
import pydantic_core
import typing_extensions
from pydantic_core import PydanticUndefined, ValidationError
from typing_extensions import Self, TypeAlias, Unpack
from  import PydanticDeprecatedSince20, PydanticDeprecatedSince211
from _internal import _config, _decorators, _fields, _forward_ref, _generics, _mock_val_ser, _model_construction, _namespace_utils, _repr, _typing_extra, _utils
from _migration import getattr_migration
from aliases import AliasChoices, AliasPath
from annotated_handlers import GetCoreSchemaHandler, GetJsonSchemaHandler
from config import ConfigDict, ExtraValues
from errors import PydanticUndefinedAnnotation, PydanticUserError
from json_schema import DEFAULT_REF_TEMPLATE, GenerateJsonSchema, JsonSchemaMode, JsonSchemaValue, model_json_schema
from plugin._schema_validator import PluggableSchemaValidator
if TYPE_CHECKING:
    from inspect import Signature
    from pathlib import Path
    from pydantic_core import CoreSchema, SchemaSerializer, SchemaValidator
    from _internal._namespace_utils import MappingNamespace
    from _internal._utils import AbstractSetIntStr, MappingIntStrAny
    from deprecated.parse import Protocol as DeprecatedParseProtocol
    from fields import ComputedFieldInfo, FieldInfo, ModelPrivateAttr
__all__ = ('BaseModel', 'create_model')
TupleGenerator: 'TypeAlias' = Generator[(tuple[(str, Any)], None, None)]
IncEx: 'TypeAlias' = Union[(set[int], set[str], Mapping[(int, Union[('IncEx', bool)])], Mapping[(str, Union[('IncEx', bool)])])]
_object_setattr = _model_construction.object_setattr

def _check_frozen(model_cls = None, name = None, value = None):
    if model_cls.model_config.get('frozen'):
        error_type = 'frozen_instance'
    elif getattr(model_cls.__pydantic_fields__.get(name), 'frozen', False):
        error_type = 'frozen_field'
    else:
        return None
    raise None.from_exception_data(model_cls.__name__, [
        {
            'type': error_type,
            'loc': (name,),
            'input': value }])


def _model_field_setattr_handler(model = None, name = None, val = None):
    model.__dict__[name] = val
    model.__pydantic_fields_set__.add(name)


def _private_setattr_handler(model = None, name = None, val = None):
    pass
# WARNING: Decompyle incomplete

_SIMPLE_SETATTR_HANDLERS: 'Mapping[str, Callable[[BaseModel, str, Any], None]]' = {
    'model_field': _model_field_setattr_handler,
    'validate_assignment': (lambda model, name, val: model.__pydantic_validator__.validate_assignment(model, name, val)),
    'private': _private_setattr_handler,
    'cached_property': (lambda model, name, val: model.__dict__.__setitem__(name, val)),
    'extra_known': (lambda model, name, val: _object_setattr(model, name, val)) }

def BaseModel():
    '''BaseModel'''
    pass
# WARNING: Decompyle incomplete

BaseModel = <NODE:27>(BaseModel, 'BaseModel', metaclass = _model_construction.ModelMetaclass)
ModelT = TypeVar('ModelT', bound = BaseModel)
create_model = (lambda model_name = None, *, __config__: pass)()
create_model = (lambda model_name = None, *, __config__: pass)()

def create_model(model_name = None, *, __config__, __doc__, __base__, __module__, __validators__, __cls_kwargs__, __qualname__, **field_definitions):
    '''!!! abstract "Usage Documentation"
        [Dynamic Model Creation](../concepts/models.md#dynamic-model-creation)

    Dynamically creates and returns a new Pydantic model, in other words, `create_model` dynamically creates a
    subclass of [`BaseModel`][pydantic.BaseModel].

    !!! warning
        This function may execute arbitrary code contained in field annotations, if string references need to be evaluated.

        See [Security implications of introspecting annotations](https://docs.python.org/3/library/annotationlib.html#annotationlib-security) for more information.

    Args:
        model_name: The name of the newly created model.
        __config__: The configuration of the new model.
        __doc__: The docstring of the new model.
        __base__: The base class or classes for the new model.
        __module__: The name of the module that the model belongs to;
            if `None`, the value is taken from `sys._getframe(1)`
        __validators__: A dictionary of methods that validate fields. The keys are the names of the validation methods to
            be added to the model, and the values are the validation methods themselves. You can read more about functional
            validators [here](https://docs.pydantic.dev/2.9/concepts/validators/#field-validators).
        __cls_kwargs__: A dictionary of keyword arguments for class creation, such as `metaclass`.
        __qualname__: The qualified name of the newly created model.
        **field_definitions: Field definitions of the new model. Either:

            - a single element, representing the type annotation of the field.
            - a two-tuple, the first element being the type and the second element the assigned value
              (either a default or the [`Field()`][pydantic.Field] function).

    Returns:
        The new [model][pydantic.BaseModel].

    Raises:
        PydanticUserError: If `__base__` and `__config__` are both passed.
    '''
    pass
# WARNING: Decompyle incomplete

__getattr__ = getattr_migration(__name__)
