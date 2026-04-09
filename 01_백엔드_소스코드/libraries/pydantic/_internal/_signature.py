# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _signature.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
from inspect import Parameter, Signature, signature
from typing import TYPE_CHECKING, Any, Callable
from pydantic_core import PydanticUndefined
from _utils import is_valid_identifier
if TYPE_CHECKING:
    from config import ExtraValues
    from fields import FieldInfo

class _HAS_DEFAULT_FACTORY_CLASS:
    
    def __repr__(self):
        return '<factory>'


_HAS_DEFAULT_FACTORY = _HAS_DEFAULT_FACTORY_CLASS()

def _field_name_for_signature(field_name = None, field_info = None):
    '''Extract the correct name to use for the field when generating a signature.

    Assuming the field has a valid alias, this will return the alias. Otherwise, it will return the field name.
    First priority is given to the alias, then the validation_alias, then the field name.

    Args:
        field_name: The name of the field
        field_info: The corresponding FieldInfo object.

    Returns:
        The correct name to use when generating a signature.
    '''
    if isinstance(field_info.alias, str) and is_valid_identifier(field_info.alias):
        return field_info.alias
    if None(field_info.validation_alias, str) and is_valid_identifier(field_info.validation_alias):
        return field_info.validation_alias


def _process_param_defaults(param = None):
    '''Modify the signature for a parameter in a dataclass where the default value is a FieldInfo instance.

    Args:
        param (Parameter): The parameter

    Returns:
        Parameter: The custom processed parameter
    '''
    FieldInfo = FieldInfo
    import fields
    param_default = param.default
    if isinstance(param_default, FieldInfo):
        annotation = param.annotation
        if annotation == 'Any':
            annotation = Any
        default = param_default.default
        if default is PydanticUndefined:
            if param_default.default_factory is PydanticUndefined:
                default = Signature.empty
            else:
                default = dataclasses._HAS_DEFAULT_FACTORY
        return param.replace(annotation = annotation, name = _field_name_for_signature(param.name, param_default), default = default)


def _generate_signature_parameters(init = None, fields = None, validate_by_name = None, extra = ('init', 'Callable[..., None]', 'fields', 'dict[str, FieldInfo]', 'validate_by_name', 'bool', 'extra', 'ExtraValues | None', 'return', 'dict[str, Parameter]')):
    '''Generate a mapping of parameter names to Parameter objects for a pydantic BaseModel or dataclass.'''
    islice = islice
    import itertools
    present_params = signature(init).parameters.values()
    merged_params = { }
    var_kw = None
    use_var_kw = False
# WARNING: Decompyle incomplete


def generate_pydantic_signature(init = None, fields = None, validate_by_name = None, extra = (False,), is_dataclass = ('init', 'Callable[..., None]', 'fields', 'dict[str, FieldInfo]', 'validate_by_name', 'bool', 'extra', 'ExtraValues | None', 'is_dataclass', 'bool', 'return', 'Signature')):
    '''Generate signature for a pydantic BaseModel or dataclass.

    Args:
        init: The class init.
        fields: The model fields.
        validate_by_name: The `validate_by_name` value of the config.
        extra: The `extra` value of the config.
        is_dataclass: Whether the model is a dataclass.

    Returns:
        The dataclass/BaseModel subclass signature.
    '''
    merged_params = _generate_signature_parameters(init, fields, validate_by_name, extra)
    if is_dataclass:
        merged_params = merged_params.items()()
    return Signature(parameters = list(merged_params.values()), return_annotation = None)
