# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _validate_call.pyc (Python 3.11)

from __future__ import annotations as _annotations
import functools
import inspect
from collections.abc import Awaitable
from functools import partial
from typing import Any, Callable
import pydantic_core
from config import ConfigDict
from plugin._schema_validator import create_schema_validator
from _config import ConfigWrapper
from _generate_schema import GenerateSchema, ValidateCallSupportedTypes
from _namespace_utils import MappingNamespace, NsResolver, ns_for_function

def extract_function_name(func = None):
    '''Extract the name of a `ValidateCallSupportedTypes` object.'''
    return f'''partial({func.func.__name__})''' if isinstance(func, functools.partial) else func.__name__


def extract_function_qualname(func = None):
    '''Extract the qualname of a `ValidateCallSupportedTypes` object.'''
    return f'''partial({func.func.__qualname__})''' if isinstance(func, functools.partial) else func.__qualname__


def update_wrapper_attributes(wrapped = None, wrapper = None):
    '''Update the `wrapper` function with the attributes of the `wrapped` function. Return the updated function.'''
    pass
# WARNING: Decompyle incomplete


class ValidateCallWrapper:
    '''This is a wrapper around a function that validates the arguments passed to it, and optionally the return value.'''
    __slots__ = ('function', 'validate_return', 'schema_type', 'module', 'qualname', 'ns_resolver', 'config_wrapper', '__pydantic_complete__', '__pydantic_validator__', '__return_pydantic_validator__')
    
    def __init__(self, function = None, config = None, validate_return = None, parent_namespace = ('function', 'ValidateCallSupportedTypes', 'config', 'ConfigDict | None', 'validate_return', 'bool', 'parent_namespace', 'MappingNamespace | None', 'return', 'None')):
        self.function = function
        self.validate_return = validate_return
        if isinstance(function, partial):
            self.schema_type = function.func
            self.module = function.func.__module__
        else:
            self.schema_type = function
            self.module = function.__module__
        self.qualname = extract_function_qualname(function)
        self.ns_resolver = NsResolver(namespaces_tuple = ns_for_function(self.schema_type, parent_namespace = parent_namespace))
        self.config_wrapper = ConfigWrapper(config)
        if not self.config_wrapper.defer_build:
            self._create_validators()
            return None
        self.__pydantic_complete__ = None

    
    def _create_validators(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, *args, **kwargs):
        if not self.__pydantic_complete__:
            self._create_validators()
        res = self.__pydantic_validator__.validate_python(pydantic_core.ArgsKwargs(args, kwargs))
        if self.__return_pydantic_validator__:
            return self.__return_pydantic_validator__(res)
