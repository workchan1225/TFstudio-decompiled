# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: validate_call_decorator.pyc (Python 3.11)

'''Decorator for validating function calls.'''
from __future__ import annotations as _annotations
import inspect
from functools import partial
from types import BuiltinFunctionType
from typing import TYPE_CHECKING, Any, Callable, TypeVar, cast, overload
from _internal import _generate_schema, _typing_extra, _validate_call
from errors import PydanticUserError
__all__ = ('validate_call',)
if TYPE_CHECKING:
    from config import ConfigDict
    AnyCallableT = TypeVar('AnyCallableT', bound = Callable[(..., Any)])
_INVALID_TYPE_ERROR_CODE = 'validate-call-type'

def _check_function_type(function = None):
    '''Check if the input function is a supported type for `validate_call`.'''
    pass
# WARNING: Decompyle incomplete

validate_call = (lambda *: pass)()
validate_call = (lambda func = None: pass)()

def validate_call(func = None, *, config, validate_return):
    '''!!! abstract "Usage Documentation"
        [Validation Decorator](../concepts/validation_decorator.md)

    Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.

    Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.

    Args:
        func: The function to be decorated.
        config: The configuration dictionary.
        validate_return: Whether to validate the return value.

    Returns:
        The decorated function.
    '''
    pass
# WARNING: Decompyle incomplete
