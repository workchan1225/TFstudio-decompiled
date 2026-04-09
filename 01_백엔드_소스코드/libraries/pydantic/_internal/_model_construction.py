# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _model_construction.pyc (Python 3.11)

'''Private logic for creating models.'''
from __future__ import annotations as _annotations
import operator
import sys
import typing
import warnings
import weakref
from abc import ABCMeta
from functools import cache, partial, wraps
from types import FunctionType
from typing import TYPE_CHECKING, Any, Callable, Generic, Literal, NoReturn, TypeVar, cast
from pydantic_core import PydanticUndefined, SchemaSerializer
from typing_extensions import TypeAliasType, dataclass_transform, deprecated, get_args, get_origin
from typing_inspection import typing_objects
from errors import PydanticUndefinedAnnotation, PydanticUserError
from plugin._schema_validator import create_schema_validator
from warnings import GenericBeforeBaseModelWarning, PydanticDeprecatedSince20
from _config import ConfigWrapper
from _decorators import DecoratorInfos, PydanticDescriptorProxy, get_attribute_from_bases, unwrap_wrapped_function
from _fields import collect_model_fields, is_valid_field_name, is_valid_privateattr_name, rebuild_model_fields
from _generate_schema import GenerateSchema, InvalidSchemaError
from _generics import PydanticGenericMetadata, get_model_typevars_map
from _import_utils import import_cached_base_model, import_cached_field_info
from _mock_val_ser import set_model_mocks
from _namespace_utils import NsResolver
from _signature import generate_pydantic_signature
from _typing_extra import _make_forward_ref, eval_type_backport, is_classvar_annotation, parent_frame_namespace
from _utils import LazyClassAttribute, SafeGetItemProxy
if TYPE_CHECKING:
    from fields import Field as PydanticModelField
    from fields import FieldInfo, ModelPrivateAttr
    from fields import PrivateAttr as PydanticModelPrivateAttr
    from main import BaseModel
else:
    PydanticModelField = object()
    PydanticModelPrivateAttr = object()
object_setattr = object.__setattr__

class _ModelNamespaceDict(dict):
    pass
# WARNING: Decompyle incomplete


def NoInitField(*, init):
    '''Only for typing purposes. Used as default value of `__pydantic_fields_set__`,
    `__pydantic_extra__`, `__pydantic_private__`, so they could be ignored when
    synthesizing the `__init__` signature.
    '''
    pass

_T = TypeVar('_T')
ModelMetaclass = <NODE:12>()

def init_private_attributes(self = None, context = None):
    """This function is meant to behave like a BaseModel method to initialise private attributes.

    It takes context as an argument since that's what pydantic-core passes when calling it.

    Args:
        self: The BaseModel instance.
        context: The context.
    """
    pass
# WARNING: Decompyle incomplete


def get_model_post_init(namespace = None, bases = None):
    '''Get the `model_post_init` method from the namespace or the class bases, or `None` if not defined.'''
    if 'model_post_init' in namespace:
        return namespace['model_post_init']
    BaseModel = None()
    model_post_init = get_attribute_from_bases(bases, 'model_post_init')
    if model_post_init is not BaseModel.model_post_init:
        return model_post_init


def inspect_namespace(namespace, raw_annotations = None, ignored_types = None, base_class_vars = None, base_class_fields = ('namespace', 'dict[str, Any]', 'raw_annotations', 'dict[str, Any]', 'ignored_types', 'tuple[type[Any], ...]', 'base_class_vars', 'set[str]', 'base_class_fields', 'set[str]', 'return', 'dict[str, ModelPrivateAttr]')):
    '''Iterate over the namespace and:
    * gather private attributes
    * check for items which look like fields but are not (e.g. have no annotation) and warn.

    Args:
        namespace: The attribute dictionary of the class to be created.
        raw_annotations: The (non-evaluated) annotations of the model.
        ignored_types: A tuple of ignore types.
        base_class_vars: A set of base class class variables.
        base_class_fields: A set of base class fields.

    Returns:
        A dict contains private attributes info.

    Raises:
        TypeError: If there is a `__root__` field in model.
        NameError: If private attribute name is invalid.
        PydanticUserError:
            - If a field does not have a type annotation.
            - If a field on base class was overridden by a non-annotated attribute.
    '''
    pass
# WARNING: Decompyle incomplete


def set_default_hash_func(cls = None, bases = None):
    base_hash_func = get_attribute_from_bases(bases, '__hash__')
    new_hash_func = make_hash_func(cls)
    if base_hash_func in {
        None,
        object.__hash__} or getattr(base_hash_func, '__code__', None) == new_hash_func.__code__:
        cls.__hash__ = new_hash_func
        return None


def make_hash_func(cls = None):
    pass
# WARNING: Decompyle incomplete


def set_model_fields(cls = None, config_wrapper = None, ns_resolver = None):
    '''Collect and set `cls.__pydantic_fields__` and `cls.__class_vars__`.

    Args:
        cls: BaseModel or dataclass.
        config_wrapper: The config wrapper instance.
        ns_resolver: Namespace resolver to use when getting model annotations.
    '''
    typevars_map = get_model_typevars_map(cls)
    (fields, class_vars) = collect_model_fields(cls, config_wrapper, ns_resolver, typevars_map = typevars_map)
    cls.__pydantic_fields__ = fields
    cls.__class_vars__.update(class_vars)
# WARNING: Decompyle incomplete


def complete_model_class(cls = None, config_wrapper = None, ns_resolver = None, *, raise_errors, call_on_complete_hook, create_model_module):
    '''Finish building a model class.

    This logic must be called after class has been created since validation functions must be bound
    and `get_type_hints` requires a class object.

    Args:
        cls: BaseModel or dataclass.
        config_wrapper: The config wrapper instance.
        ns_resolver: The namespace resolver instance to use during schema building.
        raise_errors: Whether to raise errors.
        call_on_complete_hook: Whether to call the `__pydantic_on_complete__` hook.
        create_model_module: The module of the class to be created, if created by `create_model`.

    Returns:
        `True` if the model is successfully completed, else `False`.

    Raises:
        PydanticUndefinedAnnotation: If `PydanticUndefinedAnnotation` occurs in`__get_pydantic_core_schema__`
            and `raise_errors=True`.
    '''
    typevars_map = get_model_typevars_map(cls)
# WARNING: Decompyle incomplete


def set_deprecated_descriptors(cls = None):
    '''Set data descriptors on the class for deprecated fields.'''
    pass
# WARNING: Decompyle incomplete


class _DeprecatedFieldDescriptor:
    field_name: 'str' = 'Read-only data descriptor used to emit a runtime deprecation warning before accessing a deprecated field.\n\n    Attributes:\n        msg: The deprecation message to be emitted.\n        wrapped_property: The property instance if the deprecated field is a computed field, or `None`.\n        field_name: The name of the field being deprecated.\n    '
    
    def __init__(self = None, msg = None, wrapped_property = None):
        self.msg = msg
        self.wrapped_property = wrapped_property

    
    def __set_name__(self = None, cls = None, name = None):
        self.field_name = name

    
    def __get__(self = None, obj = None, obj_type = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, obj = None, value = None):
        raise AttributeError(self.field_name)



class _PydanticWeakRef:
    '''Wrapper for `weakref.ref` that enables `pickle` serialization.

    Cloudpickle fails to serialize `weakref.ref` objects due to an arcane error related
    to abstract base classes (`abc.ABC`). This class works around the issue by wrapping
    `weakref.ref` instead of subclassing it.

    See https://github.com/pydantic/pydantic/issues/6763 for context.

    Semantics:
        - If not pickled, behaves the same as a `weakref.ref`.
        - If pickled along with the referenced object, the same `weakref.ref` behavior
          will be maintained between them after unpickling.
        - If pickled without the referenced object, after unpickling the underlying
          reference will be cleared (`__call__` will always return `None`).
    '''
    
    def __init__(self = None, obj = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce__(self = None):
        return (_PydanticWeakRef, (self(),))



def build_lenient_weakvaluedict(d = None):
    """Takes an input dictionary, and produces a new value that (invertibly) replaces the values with weakrefs.

    We can't just use a WeakValueDictionary because many types (including int, str, etc.) can't be stored as values
    in a WeakValueDictionary.

    The `unpack_lenient_weakvaluedict` function can be used to reverse this operation.
    """
    pass
# WARNING: Decompyle incomplete


def unpack_lenient_weakvaluedict(d = None):
    '''Inverts the transform performed by `build_lenient_weakvaluedict`.'''
    pass
# WARNING: Decompyle incomplete

default_ignored_types = (lambda : ComputedFieldInfo = ComputedFieldInfoimport fieldsignored_types = [
FunctionType,
property,
classmethod,
staticmethod,
PydanticDescriptorProxy,
ComputedFieldInfo,
TypeAliasType]if sys.version_info >= (3, 12):
ignored_types.append(typing.TypeAliasType)tuple(ignored_types))()
