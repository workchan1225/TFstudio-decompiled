# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Union, Generic, TypeVar, Callable, cast, overload
from datetime import date, datetime
from typing_extensions import Self, Literal
import pydantic
from pydantic.fields import FieldInfo
from _types import IncEx, StrBytesIntFloat
_T = TypeVar('_T')
_ModelT = TypeVar('_ModelT', bound = pydantic.BaseModel)
PYDANTIC_V1 = pydantic.VERSION.startswith('1.')
if TYPE_CHECKING:
    
    def parse_date(value = None):
        pass

    
    def parse_datetime(value = None):
        pass

    
    def get_args(t = None):
        pass

    
    def is_union(tp = None):
        pass

    
    def get_origin(t = None):
        pass

    
    def is_literal_type(type_ = None):
        pass

    
    def is_typeddict(type_ = None):
        pass

elif PYDANTIC_V1:
    from pydantic.typing import get_args, is_union, get_origin, is_typeddict, is_literal_type
    from pydantic.datetime_parse import parse_date, parse_datetime
else:
    from _utils import get_args, is_union, get_origin, parse_date, is_typeddict, parse_datetime, is_literal_type
if TYPE_CHECKING:
    from pydantic import ConfigDict
elif PYDANTIC_V1:
    ConfigDict = None
else:
    from pydantic import ConfigDict

def parse_obj(model = None, value = None):
    if PYDANTIC_V1:
        return cast(_ModelT, model.parse_obj(value))
    return None.model_validate(value)


def field_is_required(field = None):
    if PYDANTIC_V1:
        return field.required
    return None.is_required()


def field_get_default(field = None):
    value = field.get_default()
    if PYDANTIC_V1:
        return value
    PydanticUndefined = PydanticUndefined
    import pydantic_core
    if value == PydanticUndefined:
        return None


def field_outer_type(field = None):
    if PYDANTIC_V1:
        return field.outer_type_
    return None.annotation


def get_model_config(model = None):
    if PYDANTIC_V1:
        return model.__config__
    return None.model_config


def get_model_fields(model = None):
    if PYDANTIC_V1:
        return model.__fields__
    return None.model_fields


def model_copy(model = None, *, deep):
    if PYDANTIC_V1:
        return model.copy(deep = deep)
    return None.model_copy(deep = deep)


def model_json(model = None, *, indent):
    if PYDANTIC_V1:
        return model.json(indent = indent)
    return None.model_dump_json(indent = indent)


def model_parse_json(model = None, data = None):
    if PYDANTIC_V1:
        return model.parse_raw(data)
    return None.model_validate_json(data)


def model_dump(model = None, *, exclude, exclude_unset, exclude_defaults, warnings, mode):
    if PYDANTIC_V1 or hasattr(model, 'model_dump'):
        return model.model_dump(mode = mode, exclude = exclude, exclude_unset = exclude_unset, exclude_defaults = exclude_defaults, warnings = True if PYDANTIC_V1 else warnings)
    return None('dict[str, Any]', model.dict(exclude = exclude, exclude_unset = exclude_unset, exclude_defaults = exclude_defaults))


def model_parse(model = None, data = None):
    if PYDANTIC_V1:
        return model.parse_obj(data)
    return None.model_validate(data)

if TYPE_CHECKING:
    
    class GenericModel(pydantic.BaseModel):
        pass

elif PYDANTIC_V1:
    import pydantic.generics as pydantic
    
    class GenericModel(pydantic.BaseModel, pydantic.generics.GenericModel):
        pass

else:
    
    class GenericModel(pydantic.BaseModel):
        pass

if TYPE_CHECKING:
    cached_property = property
    
    def typed_cached_property():
        '''typed_cached_property'''
        attrname: 'str | None' = 'typed_cached_property'
        
        def __init__(self = None, func = None):
            pass

        __get__ = (lambda self = None, instance = None, owner = overload: pass)()
        __get__ = (lambda self = None, instance = None, owner = overload: pass)()
        
        def __get__(self = None, instance = None, owner = None):
            raise NotImplementedError()

        
        def __set_name__(self = None, owner = None, name = None):
            pass

        
        def __set__(self = None, instance = None, value = None):
            pass


    typed_cached_property = <NODE:27>(typed_cached_property, 'typed_cached_property', Generic[_T])
    return None
from functools import cached_property
typed_cached_property = cached_property
