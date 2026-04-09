# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _transform.pyc (Python 3.11)

from __future__ import annotations
import inspect
from typing import Any, Literal, Optional, cast
from typing_extensions import assert_never
import pydantic
from _utils import is_list
SupportedTypes = Literal[('object', 'array', 'string', 'integer', 'number', 'boolean', 'null')]
SupportedStringFormats = {
    'date-time',
    'uri',
    'date',
    'ipv4',
    'ipv6',
    'time',
    'uuid',
    'email',
    'duration',
    'hostname'}

def get_transformed_string(schema = None):
    '''Transforms a JSON schema of type string to ensure it conforms to the API\'s expectations.

    Specifically, it ensures that if the schema is of type "string" and does not already
    specify a "format", it sets the format to "text".

    Args:
        schema: The original JSON schema.

    Returns:
        The transformed JSON schema.
    '''
    if schema.get('type') == 'string' and 'format' not in schema:
        schema['format'] = 'text'
    return schema


def transform_schema(json_schema = None):
    '''
    Transforms a JSON schema to ensure it conforms to the API\'s expectations.

    Args:
        json_schema (Dict[str, Any]): The original JSON schema.

    Returns:
        The transformed JSON schema.

    Examples:
        >>> transform_schema(
        ...     {
        ...         "type": "integer",
        ...         "minimum": 1,
        ...         "maximum": 10,
        ...         "description": "A number",
        ...     }
        ... )
        {\'type\': \'integer\', \'description\': \'A number

{minimum: 1, maximum: 10}\'}
    '''
    if inspect.isclass(json_schema) and issubclass(json_schema, pydantic.BaseModel):
        json_schema = json_schema.model_json_schema()
    strict_schema = { }
# WARNING: Decompyle incomplete
