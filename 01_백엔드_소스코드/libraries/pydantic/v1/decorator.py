# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decorator.pyc (Python 3.11)

from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Mapping, Optional, Tuple, Type, TypeVar, Union, overload
from pydantic.v1 import validator
from pydantic.v1.config import Extra
from pydantic.v1.errors import ConfigError
from pydantic.v1.main import BaseModel, create_model
from pydantic.v1.typing import get_all_type_hints
from pydantic.v1.utils import to_camel
__all__ = ('validate_arguments',)
if TYPE_CHECKING:
    from pydantic.v1.typing import AnyCallable
    AnyCallableT = TypeVar('AnyCallableT', bound = AnyCallable)
    ConfigType = Union[(None, Type[Any], Dict[(str, Any)])]
validate_arguments = (lambda func = None, *, config: pass)()
validate_arguments = (lambda func = None: pass)()

def validate_arguments(func = None, *, config):
    '''
    Decorator to validate the arguments passed to a function.
    '''
    pass
# WARNING: Decompyle incomplete

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
            raise ConfigError(f'''"{ALT_V_ARGS}", "{ALT_V_KWARGS}", "{V_POSITIONAL_ONLY_NAME}" and "{V_DUPLICATE_KWARGS}" are not permitted as argument names when using the "{validate_arguments.__name__}" decorator''')
        self.raw_function = function
        self.arg_mapping = { }
        self.positional_only_args = set()
        self.v_args_name = 'args'
        self.v_kwargs_name = 'kwargs'
        type_hints = get_all_type_hints(function)
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

    
    def create_model(self, fields = None, takes_args = None, takes_kwargs = None, config = ('fields', Dict[(str, Any)], 'takes_args', bool, 'takes_kwargs', bool, 'config', 'ConfigType', 'return', None)):
        pass
    # WARNING: Decompyle incomplete
