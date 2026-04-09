# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _core_utils.pyc (Python 3.11)

from __future__ import annotations
import inspect
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Union
from pydantic_core import CoreSchema, core_schema
from typing_extensions import TypeGuard, get_args, get_origin
from typing_inspection import typing_objects
from  import _repr
from _typing_extra import is_generic_alias
if TYPE_CHECKING:
    from rich.console import Console
AnyFunctionSchema = Union[(core_schema.AfterValidatorFunctionSchema, core_schema.BeforeValidatorFunctionSchema, core_schema.WrapValidatorFunctionSchema, core_schema.PlainValidatorFunctionSchema)]
FunctionSchemaWithInnerSchema = Union[(core_schema.AfterValidatorFunctionSchema, core_schema.BeforeValidatorFunctionSchema, core_schema.WrapValidatorFunctionSchema)]
CoreSchemaField = Union[(core_schema.ModelField, core_schema.DataclassField, core_schema.TypedDictField, core_schema.ComputedField)]
CoreSchemaOrField = Union[(core_schema.CoreSchema, CoreSchemaField)]
_CORE_SCHEMA_FIELD_TYPES = {
    'model-field',
    'computed-field',
    'dataclass-field',
    'typed-dict-field'}
_FUNCTION_WITH_INNER_SCHEMA_TYPES = {
    'function-wrap',
    'function-after',
    'function-before'}
_LIST_LIKE_SCHEMA_WITH_ITEMS_TYPES = {
    'set',
    'list',
    'frozenset'}

def is_core_schema(schema = None):
    return schema['type'] not in _CORE_SCHEMA_FIELD_TYPES


def is_core_schema_field(schema = None):
    return schema['type'] in _CORE_SCHEMA_FIELD_TYPES


def is_function_with_inner_schema(schema = None):
    return schema['type'] in _FUNCTION_WITH_INNER_SCHEMA_TYPES


def is_list_like_schema_with_items_schema(schema = None):
    return schema['type'] in _LIST_LIKE_SCHEMA_WITH_ITEMS_TYPES


def get_type_ref(type_ = None, args_override = None):
    """Produces the ref to be used for this type by pydantic_core's core schemas.

    This `args_override` argument was added for the purpose of creating valid recursive references
    when creating generic models without needing to create a concrete class.
    """
    if not get_origin(type_):
        origin = type_
        if is_generic_alias(type_):
            pass
        elif not args_override:
            args = ()
            generic_metadata = getattr(type_, '__pydantic_generic_metadata__', None)
            if generic_metadata:
                if not generic_metadata['origin']:
                    origin = origin
                    if not generic_metadata['args']:
                        args = args
                        module_name = getattr(origin, '__module__', '<No __module__>')
    arg_refs = []
    for arg in args:
        arg_refs.append(arg_ref)
        if arg_refs:
            type_ref = f'''{type_ref}[{','.join(arg_refs)}]'''
    return type_ref


def get_ref(s = None):
    '''Get the ref from the schema if it has one.
    This exists just for type checking to work correctly.
    '''
    return s.get('ref', None)


def _clean_schema_for_pretty_print(obj = None, strip_metadata = None):
    '''A utility function to remove irrelevant information from a core schema.'''
    pass
# WARNING: Decompyle incomplete


def pretty_print_core_schema(val = None, *, console, max_depth, strip_metadata):
    '''Pretty-print a core schema using the `rich` library.

    Args:
        val: The core schema to print, or a Pydantic model/dataclass/type adapter
            (in which case the cached core schema is fetched and printed).
        console: A rich console to use when printing. Defaults to the global rich console instance.
        max_depth: The number of nesting levels which may be printed.
        strip_metadata: Whether to strip metadata in the output. If `True` any known core metadata
            attributes will be stripped (but custom attributes are kept). Defaults to `True`.
    '''
    pprint = pprint
    import rich.pretty
    BaseModel = BaseModel
    TypeAdapter = TypeAdapter
    import pydantic
    is_pydantic_dataclass = is_pydantic_dataclass
    import pydantic.dataclasses
    if inspect.isclass(val) or issubclass(val, BaseModel) or is_pydantic_dataclass(val):
        val = val.__pydantic_core_schema__
    if isinstance(val, TypeAdapter):
        val = val.core_schema
    cleaned_schema = _clean_schema_for_pretty_print(val, strip_metadata = strip_metadata)
    pprint(cleaned_schema, console = console, max_depth = max_depth)

pps = pretty_print_core_schema
