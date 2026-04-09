# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mock_val_ser.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING, Any, Callable, Generic, Literal, TypeVar, Union
from pydantic_core import CoreSchema, SchemaSerializer, SchemaValidator
from errors import PydanticErrorCodes, PydanticUserError
from plugin._schema_validator import PluggableSchemaValidator
if TYPE_CHECKING:
    from dataclasses import PydanticDataclass
    from main import BaseModel
    from type_adapter import TypeAdapter
ValSer = TypeVar('ValSer', bound = Union[(SchemaValidator, PluggableSchemaValidator, SchemaSerializer)])
T = TypeVar('T')

def MockCoreSchema():
    '''MockCoreSchema'''
    __doc__ = "Mocker for `pydantic_core.CoreSchema` which optionally attempts to\n    rebuild the thing it's mocking when one of its methods is accessed and raises an error if that fails.\n    "
    __slots__ = ('_error_message', '_code', '_attempt_rebuild', '_built_memo')
    
    def __init__(self = None, error_message = None, *, code, attempt_rebuild):
        self._error_message = error_message
        self._code = code
        self._attempt_rebuild = attempt_rebuild
        self._built_memo = None

    
    def __getitem__(self = None, key = None):
        return self._get_built().__getitem__(key)

    
    def __len__(self = None):
        return self._get_built().__len__()

    
    def __iter__(self = None):
        return self._get_built().__iter__()

    
    def _get_built(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def rebuild(self = None):
        self._built_memo = None
    # WARNING: Decompyle incomplete


MockCoreSchema = <NODE:27>(MockCoreSchema, 'MockCoreSchema', Mapping[(str, Any)])

def MockValSer():
    '''MockValSer'''
    __doc__ = "Mocker for `pydantic_core.SchemaValidator` or `pydantic_core.SchemaSerializer` which optionally attempts to\n    rebuild the thing it's mocking when one of its methods is accessed and raises an error if that fails.\n    "
    __slots__ = ('_error_message', '_code', '_val_or_ser', '_attempt_rebuild')
    
    def __init__(self = None, error_message = None, *, code, val_or_ser, attempt_rebuild):
        self._error_message = error_message
        self._val_or_ser = SchemaValidator if val_or_ser == 'validator' else SchemaSerializer
        self._code = code
        self._attempt_rebuild = attempt_rebuild

    
    def __getattr__(self = None, item = None):
        __tracebackhide__ = True
    # WARNING: Decompyle incomplete

    
    def rebuild(self = None):
        pass
    # WARNING: Decompyle incomplete


MockValSer = <NODE:27>(MockValSer, 'MockValSer', Generic[ValSer])

def set_type_adapter_mocks(adapter = None):
    '''Set `core_schema`, `validator` and `serializer` to mock core types on a type adapter instance.

    Args:
        adapter: The type adapter instance to set the mocks on
    '''
    pass
# WARNING: Decompyle incomplete


def set_model_mocks(cls = None, undefined_name = None):
    '''Set `__pydantic_core_schema__`, `__pydantic_validator__` and `__pydantic_serializer__` to mock core types on a model.

    Args:
        cls: The model class to set the mocks on
        undefined_name: Name of the undefined thing, used in error messages
    '''
    pass
# WARNING: Decompyle incomplete


def set_dataclass_mocks(cls = None, undefined_name = None):
    '''Set `__pydantic_validator__` and `__pydantic_serializer__` to `MockValSer`s on a dataclass.

    Args:
        cls: The model class to set the mocks on
        undefined_name: Name of the undefined thing, used in error messages
    '''
    pass
# WARNING: Decompyle incomplete
