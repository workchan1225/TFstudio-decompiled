# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

import warnings
from abc import ABCMeta
from copy import deepcopy
from enum import Enum
from functools import partial
from pathlib import Path
from types import FunctionType, prepare_class, resolve_bases
from typing import TYPE_CHECKING, AbstractSet, Any, Callable, ClassVar, Dict, List, Mapping, Optional, Tuple, Type, TypeVar, Union, cast, no_type_check, overload
from typing_extensions import dataclass_transform
from pydantic.v1.class_validators import ValidatorGroup, extract_root_validators, extract_validators, inherit_validators
from pydantic.v1.config import BaseConfig, Extra, inherit_config, prepare_config
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import ConfigError, DictError, ExtraError, MissingError
from pydantic.v1.fields import MAPPING_LIKE_SHAPES, Field, ModelField, ModelPrivateAttr, PrivateAttr, Undefined, is_finalvar_with_default_val
from pydantic.v1.json import custom_pydantic_encoder, pydantic_encoder
from pydantic.v1.parse import Protocol, load_file, load_str_bytes
from pydantic.v1.schema import default_ref_template, model_schema
from pydantic.v1.types import PyObject, StrBytes
from pydantic.v1.typing import AnyCallable, get_args, get_origin, is_classvar, is_namedtuple, is_union, resolve_annotations, update_model_forward_refs
from pydantic.v1.utils import DUNDER_ATTRIBUTES, ROOT_KEY, ClassAttribute, GetterDict, Representation, ValueItems, generate_model_signature, is_valid_field, is_valid_private_name, lenient_issubclass, sequence_like, smart_deepcopy, unique_list, validate_field_name
if TYPE_CHECKING:
    from inspect import Signature
    from pydantic.v1.class_validators import ValidatorListDict
    from pydantic.v1.types import ModelOrDc
    from pydantic.v1.typing import AbstractSetIntStr, AnyClassMethod, CallableGenerator, DictAny, DictStrAny, MappingIntStrAny, ReprArgs, SetStr, TupleGenerator
    Model = TypeVar('Model', bound = 'BaseModel')
__all__ = ('BaseModel', 'create_model', 'validate_model')
_T = TypeVar('_T')

def validate_custom_root_type(fields = None):
    if len(fields) > 1:
        raise ValueError(f'''{ROOT_KEY} cannot be mixed with other fields''')


def generate_hash_function(frozen = None):
    
    def hash_function(self_ = None):
        return hash(self_.__class__) + hash(tuple(self_.__dict__.values()))

    return hash_function if frozen else None

ANNOTATED_FIELD_UNTOUCHED_TYPES: Tuple[(Any, ...)] = (property, type, classmethod, staticmethod)
UNTOUCHED_TYPES: Tuple[(Any, ...)] = (FunctionType,) + ANNOTATED_FIELD_UNTOUCHED_TYPES
_is_base_model_class_defined = False
ModelMetaclass = <NODE:12>()
object_setattr = object.__setattr__

def BaseModel():
    '''BaseModel'''
    if TYPE_CHECKING:
        __fields__: ClassVar[Dict[(str, ModelField)]] = { }
        __include_fields__: ClassVar[Optional[Mapping[(str, Any)]]] = None
        __exclude_fields__: ClassVar[Optional[Mapping[(str, Any)]]] = None
        __post_root_validators__: ClassVar[List[Tuple[(bool, AnyCallable)]]] = { }
        __config__: ClassVar[Type[BaseConfig]] = BaseConfig
        
        __json_encoder__: ClassVar[Callable[([
            Any], Any)]] = lambda x: x
        __schema_cache__: ClassVar['DictAny'] = { }
        __class_vars__: ClassVar[SetStr] = False
        __fields_set__: ClassVar[SetStr] = set()
    Config = BaseConfig
    __slots__ = ('__dict__', '__fields_set__')
    __doc__ = ''
    
    def __init__(__pydantic_self__ = None, **data):
        '''
        Create a new model by parsing and validating input data from keyword arguments.

        Raises ValidationError if the input data cannot be parsed to form a valid model.
        '''
        (values, fields_set, validation_error) = validate_model(__pydantic_self__.__class__, data)
        if validation_error:
            raise validation_error
        
        try:
            object_setattr(__pydantic_self__, '__dict__', values)
        except TypeError:
            e = None
            raise TypeError('Model values must be a dict; you may not have returned a dictionary from a root validator'), e
            e = None
            del e

        object_setattr(__pydantic_self__, '__fields_set__', fields_set)
        __pydantic_self__._init_private_attributes()

    __setattr__ = (lambda self, name, value: pass# WARNING: Decompyle incomplete
)()
    
    def __getstate__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __setstate__(self = None, state = None):
        object_setattr(self, '__dict__', state['__dict__'])
        object_setattr(self, '__fields_set__', state['__fields_set__'])
        for name, value in state.get('__private_attribute_values__', { }).items():
            object_setattr(self, name, value)
            return None

    
    def _init_private_attributes(self = None):
        for name, private_attr in self.__private_attributes__.items():
            default = private_attr.get_default()
            if default is not Undefined:
                object_setattr(self, name, default)
            return None

    
    def dict(self = None, *, include, exclude, by_alias, skip_defaults, exclude_unset, exclude_defaults, exclude_none):
        '''
        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def json(self = None, *, include, exclude, by_alias, skip_defaults, exclude_unset, exclude_defaults, exclude_none, encoder, models_as_dict, **dumps_kwargs):
        '''
        Generate a JSON representation of the model, `include` and `exclude` arguments as per `dict()`.

        `encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.
        '''
        pass
    # WARNING: Decompyle incomplete

    _enforce_dict_if_root = (lambda cls = None, obj = None:
