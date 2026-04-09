# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: schema_repair.pyc (Python 3.11)

from __future__ import annotations
import copy
import importlib
import re
from types import ModuleType
from typing import Any, Literal, cast
from utils.constants import MISSING_VALUE, JSONReturnType, MissingValueType
SchemaRepairMode = Literal[('standard', 'salvage')]
SUPPORTED_SCHEMA_REPAIR_MODES: 'tuple[SchemaRepairMode, ...]' = ('standard', 'salvage')

class SchemaDefinitionError(ValueError):
    '''Raised when schema metadata is invalid or unsupported.'''
    pass


def normalize_schema_repair_mode(mode = None):
    pass
# WARNING: Decompyle incomplete


def _require_jsonschema():
    
    try:
        return importlib.import_module('jsonschema')
    except ImportError:
        exc = None
        raise ValueError('jsonschema is required when using schema-aware repair.'), exc
        exc = None
        del exc



def _require_pydantic():
    
    try:
        return importlib.import_module('pydantic')
    except ImportError:
        exc = None
        raise ValueError('pydantic is required when using schema models.'), exc
        exc = None
        del exc



def load_schema_model(path = None):
    if ':' not in path:
        raise ValueError("Schema model must be in the form 'module:ClassName'.")
    (module_name, class_name) = path.split(':', 1)
    module = importlib.import_module(module_name)
    model = module.__dict__.get(class_name)
# WARNING: Decompyle incomplete


def normalize_missing_values(value = None):
    if value is MISSING_VALUE or isinstance(value, MissingValueType):
        return ''
# WARNING: Decompyle incomplete


def schema_from_input(schema = None):
    if isinstance(schema, dict):
        return schema
    if None is True or schema is False:
        return schema
# WARNING: Decompyle incomplete


class SchemaRepairer:
    
    def __init__(self = None, schema = None, log = None, schema_repair_mode = ('standard',)):
        self.root_schema = schema
        self.log = log
        self.schema_repair_mode = normalize_schema_repair_mode(schema_repair_mode)

    
    def _log(self = None, text = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def validate(self = None, value = None, schema = None):
        schema = self.resolve_schema(schema)
        if schema is True:
            return None
        if None is False:
            raise ValueError('Schema does not allow any values.')
        schema_for_validation = self._prepare_schema_for_validation(schema)
        jsonschema = _require_jsonschema()
        validator_cls = jsonschema.validators.validator_for(schema_for_validation)
        validator = validator_cls(schema_for_validation)
        errors = sorted(validator.iter_errors(value), key = (lambda e: e.path))
        if errors:
            raise ValueError(errors[0].message)

    
    def resolve_schema(self = None, schema = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_object_schema(self = None, schema = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_array_schema(self = None, schema = None):
        schema = self.resolve_schema(schema)
        if not isinstance(schema, dict):
            return False
        schema_type = None.get('type')
        if schema_type == 'array':
            return True
        if None(schema_type, list) and 'array' in schema_type:
            return True
        return None in schema

    
    def repair_value(self = None, value = None, schema = None, path = ('value', 'Any', 'schema', 'dict[str, Any] | bool | None', 'path', 'str', 'return', 'JSONReturnType')):
        '''Apply schema rules to a parsed value, including unions, coercions, and defaults.'''
        schema = self.resolve_schema(schema)
        if schema is True:
            return normalize_missing_values(value)
        if None is False:
            raise ValueError('Schema does not allow any values.')
        if not schema:
            return normalize_missing_values(value)
        if None is MISSING_VALUE:
            return self._fill_missing(schema, path)
    # WARNING: Decompyle incomplete

    
    def _repair_union(self = None, value = None, schemas = None, path = ('value', 'Any', 'schemas', 'list[dict[str, Any] | bool]', 'path', 'str', 'return', 'JSONReturnType')):
        last_error = None
        for subschema in schemas:
            candidate = self.repair_value(copy.deepcopy(value), subschema, path)
            self.validate(candidate, subschema)
            
            return None, candidate
            except ValueError:
                exc = None
                exc = None
                del exc
                continue
                exc = None
                del exc
            if last_error:
                raise ValueError(str(last_error)), last_error
            raise ValueError('No schema matched the value.')

    
    def _repair_type_union(self, value = None, types = None, schema = None, path = ('value', 'Any', 'types', 'list[str]', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'JSONReturnType')):
        last_error = None
        for schema_type in types:
            candidate = self._repair_by_type(value, schema_type, schema, path)
            
            return None, self._apply_enum_const(candidate, schema, path)
            except ValueError:
                exc = None
                exc = None
                del exc
                continue
                exc = None
                del exc
            if last_error:
                raise ValueError(str(last_error)), last_error
            raise ValueError('No schema type matched the value.')

    
    def _repair_by_type(self, value = None, schema_type = None, schema = None, path = ('value', 'Any', 'schema_type', 'str', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'JSONReturnType')):
        if schema_type == 'array':
            return self._repair_array(value, schema, path)
        if None == 'object':
            return self._repair_object(value, schema, path)
        return None._coerce_scalar(value, schema_type, path)

    
    def _repair_array(self = None, value = None, schema = None, path = ('value', 'Any', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'JSONReturnType')):
        pass
    # WARNING: Decompyle incomplete

    
    def _repair_object(self = None, value = None, schema = None, path = ('value', 'Any', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'JSONReturnType')):
        pass
    # WARNING: Decompyle incomplete

    
    def _map_list_to_object(self = None, value = None, schema = None, path = ('value', 'list[Any]', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'dict[str, JSONReturnType] | None')):
        properties = schema.get('properties')
        if not isinstance(properties, dict) or properties:
            return None
        keys = None(properties.keys())
        if len(value) != len(keys):
            return None
        mapped = None
        for idx, key in enumerate(keys):
            key_path = f'''{path}.{key}'''
            mapped[key] = self.repair_value(value[idx], properties[key], key_path)
            except SchemaDefinitionError:
                raise 
            except ValueError:
                return None
            self._log('Mapped array to object by schema property order', path)
            return mapped

    
    def _fill_missing(self = None, schema = None, path = None):
        if 'const' in schema:
            self._log('Filled missing value with const', path)
            return self._copy_json_value(schema['const'], path, 'const')
        if None in schema:
            enum_values = schema['enum']
            if not enum_values:
                raise ValueError(f'''Enum at {path} has no values.''')
            self._log('Filled missing value with first enum value', path)
            return self._copy_json_value(enum_values[0], path, 'enum')
        if None in schema:
            self._log('Filled missing value with default', path)
            return self._copy_json_value(schema['default'], path, 'default')
        expected_type = None.get('type')
    # WARNING: Decompyle incomplete

    
    def _coerce_scalar(self = None, value = None, schema_type = None, path = ('value', 'Any', 'schema_type', 'str', 'path', 'str', 'return', 'JSONReturnType')):
        if schema_type == 'string':
            if isinstance(value, str):
                return value
            if not None(value, (int, float)) and isinstance(value, bool):
                self._log('Coerced number to string', path)
                return str(value)
            raise None(f'''Expected string at {path}.''')
    # WARNING: Decompyle incomplete

    
    def _apply_enum_const(self = None, value = None, schema = None, path = ('value', 'JSONReturnType', 'schema', 'dict[str, Any]', 'path', 'str', 'return', 'JSONReturnType')):
        if 'const' in schema and value != schema['const']:
            raise ValueError(f'''Value at {path} does not match const.''')
        if 'enum' in schema and value not in schema['enum']:
            raise ValueError(f'''Value at {path} does not match enum.''')
        return value

    
    def _resolve_ref(self = None, ref = None):
        if not ref.startswith('#/'):
            raise SchemaDefinitionError(f'''Unsupported $ref: {ref}''')
        parts = ref.lstrip('#/').split('/')
        current = self.root_schema
        for part in parts:
            resolved_part = part.replace('~1', '/').replace('~0', '~')
            if isinstance(current, dict) or resolved_part not in current:
                raise SchemaDefinitionError(f'''Unresolvable $ref: {ref}''')
            current = current[resolved_part]
            if isinstance(current, dict):
                return current
            if None is True:
                return True
            if None is False:
                return False
            raise None(f'''Unresolvable $ref: {ref}''')

    
    def _copy_json_value(self = None, value = None, path = None, label = ('value', 'Any', 'path', 'str', 'label', 'str', 'return', 'JSONReturnType')):
        pass
    # WARNING: Decompyle incomplete

    
    def _prepare_schema_for_validation(self = None, schema = None):
        pass
    # WARNING: Decompyle incomplete
