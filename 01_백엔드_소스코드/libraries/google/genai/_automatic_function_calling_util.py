# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _automatic_function_calling_util.pyc (Python 3.11)

import inspect
import sys
import types as builtin_types
import typing
from typing import _GenericAlias, Any, Callable, get_args, get_origin, Literal, Optional, Union
import pydantic
from  import _extra_utils
from  import types
if sys.version_info >= (3, 10):
    VersionedUnionType = builtin_types.UnionType
else:
    VersionedUnionType = typing._UnionGenericAlias
__all__ = [
    '_py_builtin_type_to_schema_type',
    '_raise_for_unsupported_param',
    '_handle_params_as_deferred_annotations',
    '_add_unevaluated_items_to_fixed_len_tuple_schema',
    '_is_builtin_primitive_or_compound',
    '_is_default_value_compatible',
    '_parse_schema_from_parameter',
    '_get_required_fields']
_py_builtin_type_to_schema_type = {
    None: types.Type.NULL,
    dict: types.Type.OBJECT,
    list: types.Type.ARRAY,
    bool: types.Type.BOOLEAN,
    float: types.Type.NUMBER,
    int: types.Type.INTEGER,
    str: types.Type.STRING }

def _raise_for_unsupported_param(param = None, func_name = None, exception = None):
    raise ValueError(f'''Failed to parse the parameter {param} of function {func_name} for automatic function calling.Automatic function calling works best with simpler function signature schema, consider manually parsing your function declaration for function {func_name}.'''), exception


def _handle_params_as_deferred_annotations(param = None, annotation_under_future = None, name = None):
    '''Catches the case when type hints are stored as strings.'''
    if isinstance(param.annotation, str):
        param = param.replace(annotation = annotation_under_future[name])
    return param


def _add_unevaluated_items_to_fixed_len_tuple_schema(json_schema = None):
    if json_schema.get('maxItems') and json_schema.get('prefixItems') and len(json_schema['prefixItems']) == json_schema['maxItems'] and json_schema.get('type') == 'array':
        json_schema['unevaluatedItems'] = False
    return json_schema


def _is_builtin_primitive_or_compound(annotation = None):
    return annotation in _py_builtin_type_to_schema_type.keys()


def _is_default_value_compatible(default_value = None, annotation = None):
    pass
# WARNING: Decompyle incomplete


def _parse_schema_from_parameter(api_option = None, param = None, func_name = None):
    '''parse schema from parameter.

  from the simplest case to the most complex case.
  '''
    schema = types.Schema()
    default_value_error_msg = f'''Default value {param.default} of parameter {param} of function {func_name} is not compatible with the parameter annotation {param.annotation}.'''
    if _is_builtin_primitive_or_compound(param.annotation):
        if param.default is not inspect.Parameter.empty:
            if not _is_default_value_compatible(param.default, param.annotation):
                raise ValueError(default_value_error_msg)
            schema.default = param.default
        schema.type = _py_builtin_type_to_schema_type[param.annotation]
        return schema
# WARNING: Decompyle incomplete


def _get_required_fields(schema = None):
