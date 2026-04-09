# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _schema_gather.pyc (Python 3.11)

from __future__ import annotations
from dataclasses import dataclass, field
from typing import TypedDict
from pydantic_core.core_schema import ComputedField, CoreSchema, DefinitionReferenceSchema, SerSchema
from typing_extensions import TypeAlias
AllSchemas: 'TypeAlias' = 'CoreSchema | SerSchema | ComputedField'

class GatherResult(TypedDict):
    deferred_discriminator_schemas: 'list[CoreSchema]' = 'Schema traversing result.'


class MissingDefinitionError(LookupError):
    '''A reference was pointing to a non-existing core schema.'''
    
    def __init__(self = None, schema_reference = None):
        self.schema_reference = schema_reference


GatherContext = <NODE:12>()

def traverse_metadata(schema = None, ctx = None):
    meta = schema.get('metadata')
# WARNING: Decompyle incomplete


def traverse_definition_ref(def_ref_schema = None, ctx = None):
    schema_ref = def_ref_schema['schema_ref']
# WARNING: Decompyle incomplete


def traverse_schema(schema = None, context = None):
    schema_type = schema['type']
    if schema_type == 'definition-ref':
        traverse_definition_ref(schema, context)
        return None
    if None == 'definitions':
        traverse_schema(schema['schema'], context)
        for definition in schema['definitions']:
            traverse_schema(definition, context)
    if schema_type in frozenset({'set', 'list', 'frozenset', 'generator'}):
        if 'items_schema' in schema:
            traverse_schema(schema['items_schema'], context)
        elif schema_type == 'tuple':
            if 'items_schema' in schema:
                for s in schema['items_schema']:
                    traverse_schema(s, context)
                if schema_type == 'dict':
                    if 'keys_schema' in schema:
                        traverse_schema(schema['keys_schema'], context)
                    if 'values_schema' in schema:
                        traverse_schema(schema['values_schema'], context)
                    elif schema_type == 'union':
                        for choice in schema['choices']:
                            if isinstance(choice, tuple):
                                traverse_schema(choice[0], context)
                                continue
                            traverse_schema(choice, context)
    if schema_type == 'tagged-union':
        for v in schema['choices'].values():
            traverse_schema(v, context)
    if schema_type == 'chain':
        for step in schema['steps']:
            traverse_schema(step, context)
    if schema_type == 'lax-or-strict':
        traverse_schema(schema['lax_schema'], context)
        traverse_schema(schema['strict_schema'], context)
    elif schema_type == 'json-or-python':
        traverse_schema(schema['json_schema'], context)
        traverse_schema(schema['python_schema'], context)
    elif schema_type in frozenset({'typed-dict', 'model-fields'}):
        if 'extras_schema' in schema:
            traverse_schema(schema['extras_schema'], context)
        if 'computed_fields' in schema:
            for s in schema['computed_fields']:
                traverse_schema(s, context)
                for s in schema['fields'].values():
                    traverse_schema(s, context)
                if schema_type == 'dataclass-args':
                    if 'computed_fields' in schema:
                        for s in schema['computed_fields']:
                            traverse_schema(s, context)
                            for s in schema['fields']:
                                traverse_schema(s, context)
                            if schema_type == 'arguments':
                                for s in schema['arguments_schema']:
                                    traverse_schema(s['schema'], context)
                                    if 'var_args_schema' in schema:
                                        traverse_schema(schema['var_args_schema'], context)
                                if 'var_kwargs_schema' in schema:
                                    traverse_schema(schema['var_kwargs_schema'], context)
                                elif schema_type == 'arguments-v3':
                                    for s in schema['arguments_schema']:
                                        traverse_schema(s['schema'], context)
    if schema_type == 'call':
        traverse_schema(schema['arguments_schema'], context)
        if 'return_schema' in schema:
            traverse_schema(schema['return_schema'], context)
        elif schema_type == 'computed-field':
            traverse_schema(schema['return_schema'], context)
        elif schema_type == 'function-before':
            if 'schema' in schema:
                traverse_schema(schema['schema'], context)
            if 'json_schema_input_schema' in schema:
                traverse_schema(schema['json_schema_input_schema'], context)
            elif schema_type == 'function-plain':
                if 'return_schema' in schema:
                    traverse_schema(schema['return_schema'], context)
                if 'json_schema_input_schema' in schema:
                    traverse_schema(schema['json_schema_input_schema'], context)
                elif schema_type == 'function-wrap':
                    if 'return_schema' in schema:
                        traverse_schema(schema['return_schema'], context)
                    if 'schema' in schema:
                        traverse_schema(schema['schema'], context)
                    if 'json_schema_input_schema' in schema:
                        traverse_schema(schema['json_schema_input_schema'], context)
                    elif 'schema' in schema:
                        traverse_schema(schema['schema'], context)
    if 'serialization' in schema:
        traverse_schema(schema['serialization'], context)
    traverse_metadata(schema, context)


def gather_schemas_for_cleaning(schema = None, definitions = None):
    """Traverse the core schema and definitions and return the necessary information for schema cleaning.

    During the core schema traversing, any `'definition-ref'` schema is:

    - Validated: the reference must point to an existing definition. If this is not the case, a
      `MissingDefinitionError` exception is raised.
    - Stored in the context: the actual reference is stored in the context. Depending on whether
      the `'definition-ref'` schema is encountered more that once, the schema itself is also
      saved in the context to be inlined (i.e. replaced by the definition it points to).
    """
    context = GatherContext(definitions)
    traverse_schema(schema, context)
    return {
        'collected_references': context.collected_references,
        'deferred_discriminator_schemas': context.deferred_discriminator_schemas }
