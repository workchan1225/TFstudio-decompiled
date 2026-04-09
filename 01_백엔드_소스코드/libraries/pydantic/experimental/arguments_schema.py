# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arguments_schema.pyc (Python 3.11)

'''Experimental module exposing a function to generate a core schema that validates callable arguments.'''
from __future__ import annotations
from collections.abc import Callable
from typing import Any, Literal
from pydantic_core import CoreSchema
from pydantic import ConfigDict
from pydantic._internal import _config, _generate_schema, _namespace_utils

def generate_arguments_schema(func = None, schema_type = None, parameters_callback = None, config = ('arguments-v3', None, None)):
    """Generate the schema for the arguments of a function.

    Args:
        func: The function to generate the schema for.
        schema_type: The type of schema to generate.
        parameters_callback: A callable that will be invoked for each parameter. The callback
            should take three required arguments: the index, the name and the type annotation
            (or [`Parameter.empty`][inspect.Parameter.empty] if not annotated) of the parameter.
            The callback can optionally return `'skip'`, so that the parameter gets excluded
            from the resulting schema.
        config: The configuration to use.

    Returns:
        The generated schema.
    """
    generate_schema = _generate_schema.GenerateSchema(_config.ConfigWrapper(config), ns_resolver = _namespace_utils.NsResolver(namespaces_tuple = _namespace_utils.ns_for_function(func)))
    if schema_type == 'arguments':
        schema = generate_schema._arguments_schema(func, parameters_callback)
    else:
        schema = generate_schema._arguments_v3_schema(func, parameters_callback)
    return generate_schema.clean_schema(schema)
