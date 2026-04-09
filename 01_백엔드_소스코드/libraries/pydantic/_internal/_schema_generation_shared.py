# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _schema_generation_shared.pyc (Python 3.11)

'''Types and utility functions used by various other internal tools.'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Literal
from pydantic_core import core_schema
from annotated_handlers import GetCoreSchemaHandler, GetJsonSchemaHandler
if TYPE_CHECKING:
    from json_schema import GenerateJsonSchema, JsonSchemaValue
    from _core_utils import CoreSchemaOrField
    from _generate_schema import GenerateSchema
    from _namespace_utils import NamespacesTuple
    GetJsonSchemaFunction = Callable[([
        CoreSchemaOrField,
        GetJsonSchemaHandler], JsonSchemaValue)]
    HandlerOverride = Callable[([
        CoreSchemaOrField], JsonSchemaValue)]

class GenerateJsonSchemaHandler(GetJsonSchemaHandler):
    """JsonSchemaHandler implementation that doesn't do ref unwrapping by default.

    This is used for any Annotated metadata so that we don't end up with conflicting
    modifications to the definition schema.

    Used internally by Pydantic, please do not rely on this implementation.
    See `GetJsonSchemaHandler` for the handler API.
    """
    
    def __init__(self = None, generate_json_schema = None, handler_override = None):
