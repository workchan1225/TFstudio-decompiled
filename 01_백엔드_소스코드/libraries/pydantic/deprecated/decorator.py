# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decorator.pyc (Python 3.11)

import warnings
from collections.abc import Mapping
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Optional, TypeVar, Union, overload
from typing_extensions import deprecated
from _internal import _config, _typing_extra
from alias_generators import to_pascal
from errors import PydanticUserError
from functional_validators import field_validator
from main import BaseModel, create_model
from warnings import PydanticDeprecatedSince20
if not TYPE_CHECKING:
    DeprecationWarning = PydanticDeprecatedSince20
__all__ = ('validate_arguments',)
if TYPE_CHECKING:
    AnyCallable = Callable[(..., Any)]
    AnyCallableT = TypeVar('AnyCallableT', bound = AnyCallable)
    ConfigType = Union[(None, type[Any], dict[(str, Any)])]
validate_arguments = (lambda func = None, *, config: pass)()
validate_arguments = (lambda func = None: pass)()
validate_arguments = (lambda func = None, *, config: pass# WARNING: Decompyle incomplete
)()
ALT_V_ARGS = 'v__args'
ALT_V_KWARGS = 'v__kwargs'
V_POSITIONAL_ONLY_NAME = 'v__positional_only'
V_DUPLICATE_KWARGS = 'v__duplicate_kwargs'

class ValidatedFunction:
    
    def __init__(self = None, function = None, config = None):
        Parameter = Parameter
        signature = signature
        import inspect
        parameters = signature(function).parameters
        if parameters.keys() & {
            ALT_V_ARGS,
            ALT_V_KWARGS,
            V_POSITIONAL_ONLY_NAME,
            V_DUPLICATE_KWARGS}:
            raise PydanticUserError(f'''"{ALT_V_ARGS}", "{ALT_V_KWARGS}", "{V_POSITIONAL_ONLY_NAME}" and "{V_DUPLICATE_KWARGS}" are not permitted as argument names when using the "{validate_arguments.__name__}" decorator''', code = None)
        self.raw_function = function
        self.arg_mapping = { }
        self.positional_only_args = set()
        self.v_args_name = 'args'
        self.v_kwargs_name = 'kwargs'
        type_hints = _typing_extra.get_type_hints(function, include_extras = True)
        takes_args = False
        takes_kwargs = False
        fields = { }
    # WARNING: Decompyle incomplete

    
    def init_model_instance(self = None, *args, **kwargs):
        values = self.build_values(args, kwargs)
    # WARNING: Decompyle incomplete

    
    def call(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def build_values(self = None, args = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def execute(self = None, m = None):
        pass
    # WARNING: Decompyle incomplete

    
    def create_model(self, fields = None, takes_args = None, takes_kwargs = None, config = ('fields', dict[(str, Any)], 'takes_args', bool, 'takes_kwargs', bool, 'config', 'ConfigType', 'return', None)):
        pass
    # WARNING: Decompyle incomplete
