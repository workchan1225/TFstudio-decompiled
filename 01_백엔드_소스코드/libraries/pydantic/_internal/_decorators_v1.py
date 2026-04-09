# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _decorators_v1.pyc (Python 3.11)

'''Logic for V1 validators, e.g. `@validator` and `@root_validator`.'''
from __future__ import annotations as _annotations
from inspect import Parameter, signature
from typing import Any, Union, cast
from pydantic_core import core_schema
from typing_extensions import Protocol
from errors import PydanticUserError
from _utils import can_be_positional

class V1OnlyValueValidator(Protocol):
    '''A simple validator, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1OnlyValueValidator__value = None):
        pass



class V1ValidatorWithValues(Protocol):
    '''A validator with `values` argument, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1ValidatorWithValues__value = None, values = None):
        pass



class V1ValidatorWithValuesKwOnly(Protocol):
    '''A validator with keyword only `values` argument, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1ValidatorWithValuesKwOnly__value = None, *, values):
        pass



class V1ValidatorWithKwargs(Protocol):
    '''A validator with `kwargs` argument, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1ValidatorWithKwargs__value = None, **kwargs):
        pass



class V1ValidatorWithValuesAndKwargs(Protocol):
    '''A validator with `values` and `kwargs` arguments, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1ValidatorWithValuesAndKwargs__value = None, values = None, **kwargs):
        pass


V1Validator = Union[(V1ValidatorWithValues, V1ValidatorWithValuesKwOnly, V1ValidatorWithKwargs, V1ValidatorWithValuesAndKwargs)]

def can_be_keyword(param = None):
    return param.kind in (Parameter.POSITIONAL_OR_KEYWORD, Parameter.KEYWORD_ONLY)


def make_generic_v1_field_validator(validator = None):
    '''Wrap a V1 style field validator for V2 compatibility.

    Args:
        validator: The V1 style field validator.

    Returns:
        A wrapped V2 style field validator.

    Raises:
        PydanticUserError: If the signature is not supported or the parameters are
            not available in Pydantic V2.
    '''
    pass
# WARNING: Decompyle incomplete

RootValidatorValues = dict[(str, Any)]
RootValidatorFieldsTuple = tuple[(Any, ...)]

class V1RootValidatorFunction(Protocol):
    '''A simple root validator, supported for V1 validators and V2 validators.'''
    
    def __call__(self = None, _V1RootValidatorFunction__values = None):
        pass



class V2CoreBeforeRootValidator(Protocol):
    """V2 validator with mode='before'."""
    
    def __call__(self = None, _V2CoreBeforeRootValidator__values = None, _V2CoreBeforeRootValidator__info = None):
        pass



class V2CoreAfterRootValidator(Protocol):
    """V2 validator with mode='after'."""
    
    def __call__(self = None, _V2CoreAfterRootValidator__fields_tuple = None, _V2CoreAfterRootValidator__info = None):
        pass



def make_v1_generic_root_validator(validator = None, pre = None):
    '''Wrap a V1 style root validator for V2 compatibility.

    Args:
        validator: The V1 style field validator.
        pre: Whether the validator is a pre validator.

    Returns:
        A wrapped V2 style validator.
    '''
    pass
# WARNING: Decompyle incomplete
