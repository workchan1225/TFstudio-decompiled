# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''!!! abstract "Usage Documentation"
    [Build a Plugin](../concepts/plugins.md#build-a-plugin)

Plugin interface for Pydantic plugins, and related types.
'''
from __future__ import annotations
from typing import Any, Callable, Literal, NamedTuple
from pydantic_core import CoreConfig, CoreSchema, ValidationError
from typing_extensions import Protocol, TypeAlias
from pydantic.config import ExtraValues
__all__ = ('PydanticPluginProtocol', 'BaseValidateHandlerProtocol', 'ValidatePythonHandlerProtocol', 'ValidateJsonHandlerProtocol', 'ValidateStringsHandlerProtocol', 'NewSchemaReturns', 'SchemaTypePath', 'SchemaKind')
NewSchemaReturns: 'TypeAlias' = 'tuple[ValidatePythonHandlerProtocol | None, ValidateJsonHandlerProtocol | None, ValidateStringsHandlerProtocol | None]'

class SchemaTypePath(NamedTuple):
    name: 'str' = 'Path defining where `schema_type` was defined, or where `TypeAdapter` was called.'

SchemaKind: 'TypeAlias' = Literal[('BaseModel', 'TypeAdapter', 'dataclass', 'create_model', 'validate_call')]

class PydanticPluginProtocol(Protocol):
    '''Protocol defining the interface for Pydantic plugins.'''
    
    def new_schema_validator(self, schema, schema_type, schema_type_path = None, schema_kind = None, config = None, plugin_settings = ('schema', 'CoreSchema', 'schema_type', 'Any', 'schema_type_path', 'SchemaTypePath', 'schema_kind', 'SchemaKind', 'config', 'CoreConfig | None', 'plugin_settings', 'dict[str, object]', 'return', 'tuple[ValidatePythonHandlerProtocol | None, ValidateJsonHandlerProtocol | None, ValidateStringsHandlerProtocol | None]')):
        '''This method is called for each plugin every time a new [`SchemaValidator`][pydantic_core.SchemaValidator]
        is created.

        It should return an event handler for each of the three validation methods, or `None` if the plugin does not
        implement that method.

        Args:
            schema: The schema to validate against.
            schema_type: The original type which the schema was created from, e.g. the model class.
            schema_type_path: Path defining where `schema_type` was defined, or where `TypeAdapter` was called.
            schema_kind: The kind of schema to validate against.
            config: The config to use for validation.
            plugin_settings: Any plugin settings.

        Returns:
            A tuple of optional event handlers for each of the three validation methods -
                `validate_python`, `validate_json`, `validate_strings`.
        '''
        raise NotImplementedError('Pydantic plugins should implement `new_schema_validator`.')



class BaseValidateHandlerProtocol(Protocol):
    on_enter: 'Callable[..., None]' = "Base class for plugin callbacks protocols.\n\n    You shouldn't implement this protocol directly, instead use one of the subclasses with adds the correctly\n    typed `on_error` method.\n    "
    
    def on_success(self = None, result = None):
        '''Callback to be notified of successful validation.

        Args:
            result: The result of the validation.
        '''
        pass

    
    def on_error(self = None, error = None):
        '''Callback to be notified of validation errors.

        Args:
            error: The validation error.
        '''
        pass

    
    def on_exception(self = None, exception = None):
        '''Callback to be notified of validation exceptions.

        Args:
            exception: The exception raised during validation.
        '''
        pass



class ValidatePythonHandlerProtocol(Protocol, BaseValidateHandlerProtocol):
    '''Event handler for `SchemaValidator.validate_python`.'''
    
    def on_enter(self = None, input = None, *, strict, extra, from_attributes, context, self_instance, by_alias, by_name):
        """Callback to be notified of validation start, and create an instance of the event handler.

        Args:
            input: The input to be validated.
            strict: Whether to validate the object in strict mode.
            extra: Whether to ignore, allow, or forbid extra data during model validation.
            from_attributes: Whether to validate objects as inputs by extracting attributes.
            context: The context to use for validation, this is passed to functional validators.
            self_instance: An instance of a model to set attributes on from validation, this is used when running
                validation from the `__init__` method of a model.
            by_alias: Whether to use the field's alias to match the input data to an attribute.
            by_name: Whether to use the field's name to match the input data to an attribute.
        """
        pass



class ValidateJsonHandlerProtocol(Protocol, BaseValidateHandlerProtocol):
    '''Event handler for `SchemaValidator.validate_json`.'''
    
    def on_enter(self = None, input = None, *, strict, extra, context, self_instance, by_alias, by_name):
        """Callback to be notified of validation start, and create an instance of the event handler.

        Args:
            input: The JSON data to be validated.
            strict: Whether to validate the object in strict mode.
            extra: Whether to ignore, allow, or forbid extra data during model validation.
            context: The context to use for validation, this is passed to functional validators.
            self_instance: An instance of a model to set attributes on from validation, this is used when running
                validation from the `__init__` method of a model.
            by_alias: Whether to use the field's alias to match the input data to an attribute.
            by_name: Whether to use the field's name to match the input data to an attribute.
        """
        pass


StringInput: 'TypeAlias' = 'dict[str, StringInput]'

class ValidateStringsHandlerProtocol(Protocol, BaseValidateHandlerProtocol):
    '''Event handler for `SchemaValidator.validate_strings`.'''
    
    def on_enter(self = None, input = None, *, strict, extra, context, by_alias, by_name):
        """Callback to be notified of validation start, and create an instance of the event handler.

        Args:
            input: The string data to be validated.
            strict: Whether to validate the object in strict mode.
            extra: Whether to ignore, allow, or forbid extra data during model validation.
            context: The context to use for validation, this is passed to functional validators.
            by_alias: Whether to use the field's alias to match the input data to an attribute.
            by_name: Whether to use the field's name to match the input data to an attribute.
        """
        pass
