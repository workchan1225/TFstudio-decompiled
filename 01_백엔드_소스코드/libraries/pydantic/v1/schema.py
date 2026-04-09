# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: schema.pyc (Python 3.11)

import re
import warnings
from collections import defaultdict
from dataclasses import is_dataclass
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from enum import Enum
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, ForwardRef, FrozenSet, Generic, Iterable, List, Optional, Pattern, Sequence, Set, Tuple, Type, TypeVar, Union, cast
from uuid import UUID
from typing_extensions import Annotated, Literal
from pydantic.v1.fields import MAPPING_LIKE_SHAPES, SHAPE_DEQUE, SHAPE_FROZENSET, SHAPE_GENERIC, SHAPE_ITERABLE, SHAPE_LIST, SHAPE_SEQUENCE, SHAPE_SET, SHAPE_SINGLETON, SHAPE_TUPLE, SHAPE_TUPLE_ELLIPSIS, FieldInfo, ModelField
from pydantic.v1.json import pydantic_encoder
from pydantic.v1.networks import AnyUrl, EmailStr
from pydantic.v1.types import ConstrainedDecimal, ConstrainedFloat, ConstrainedFrozenSet, ConstrainedInt, ConstrainedList, ConstrainedSet, ConstrainedStr, SecretBytes, SecretStr, StrictBytes, StrictStr, conbytes, condecimal, confloat, confrozenset, conint, conlist, conset, constr
from pydantic.v1.typing import all_literal_values, get_args, get_origin, get_sub_types, is_callable_type, is_literal_type, is_namedtuple, is_none_type, is_union
from pydantic.v1.utils import ROOT_KEY, get_model, lenient_issubclass
if TYPE_CHECKING:
    from pydantic.v1.dataclasses import Dataclass
    from pydantic.v1.main import BaseModel
default_prefix = '#/definitions/'
default_ref_template = '#/definitions/{model}'
TypeModelOrEnum = Union[(Type['BaseModel'], Type[Enum])]
TypeModelSet = Set[TypeModelOrEnum]

def _apply_modify_schema(modify_schema = None, field = None, field_schema = None):
    signature = signature
    import inspect
    sig = signature(modify_schema)
    args = set(sig.parameters.keys())
    if 'field' in args or 'kwargs' in args:
        modify_schema(field_schema, field = field)
        return None
    modify_schema(field_schema)


def schema(models = None, *, by_alias, title, description, ref_prefix, ref_template):
    '''
    Process a list of models and generate a single JSON Schema with all of them defined in the ``definitions``
    top-level JSON key, including their sub-models.

    :param models: a list of models to include in the generated JSON Schema
    :param by_alias: generate the schemas using the aliases defined, if any
    :param title: title for the generated schema that includes the definitions
    :param description: description for the generated schema
    :param ref_prefix: the JSON Pointer prefix for schema references with ``$ref``, if None, will be set to the
      default of ``#/definitions/``. Update it if you want the schemas to reference the definitions somewhere
      else, e.g. for OpenAPI use ``#/components/schemas/``. The resulting generated schemas will still be at the
      top-level key ``definitions``, so you can extract them from there. But all the references will have the set
      prefix.
    :param ref_template: Use a ``string.format()`` template for ``$ref`` instead of a prefix. This can be useful
      for references that cannot be represented by ``ref_prefix`` such as a definition stored in another file. For
      a sibling json file in a ``/schemas`` directory use ``"/schemas/${model}.json#"``.
    :return: dict with the JSON Schema with a ``definitions`` top-level key including the schema definitions for
      the models and sub-models passed in ``models``.
    '''
    clean_models = models()
    flat_models = get_flat_models_from_models(clean_models)
    model_name_map = get_model_name_map(flat_models)
    definitions = { }
    output_schema = { }
    if title:
        output_schema['title'] = title
    if description:
        output_schema['description'] = description
    for model in clean_models:
        (m_schema, m_definitions, m_nested_models) = model_process_schema(model, by_alias = by_alias, model_name_map = model_name_map, ref_prefix = ref_prefix, ref_template = ref_template)
        definitions.update(m_definitions)
        model_name = model_name_map[model]
        definitions[model_name] = m_schema
        if definitions:
            output_schema['definitions'] = definitions
    return output_schema


def model_schema(model = None, by_alias = None, ref_prefix = None, ref_template = (True, None, default_ref_template)):
    '''
    Generate a JSON Schema for one model. With all the sub-models defined in the ``definitions`` top-level
    JSON key.

    :param model: a Pydantic model (a class that inherits from BaseModel)
    :param by_alias: generate the schemas using the aliases defined, if any
    :param ref_prefix: the JSON Pointer prefix for schema references with ``$ref``, if None, will be set to the
      default of ``#/definitions/``. Update it if you want the schemas to reference the definitions somewhere
      else, e.g. for OpenAPI use ``#/components/schemas/``. The resulting generated schemas will still be at the
      top-level key ``definitions``, so you can extract them from there. But all the references will have the set
      prefix.
    :param ref_template: Use a ``string.format()`` template for ``$ref`` instead of a prefix. This can be useful for
      references that cannot be represented by ``ref_prefix`` such as a definition stored in another file. For a
      sibling json file in a ``/schemas`` directory use ``"/schemas/${model}.json#"``.
    :return: dict with the JSON Schema for the passed ``model``
    '''
    model = get_model(model)
    flat_models = get_flat_models_from_model(model)
    model_name_map = get_model_name_map(flat_models)
    model_name = model_name_map[model]
    (m_schema, m_definitions, nested_models) = model_process_schema(model, by_alias = by_alias, model_name_map = model_name_map, ref_prefix = ref_prefix, ref_template = ref_template)
    if model_name in nested_models:
        m_definitions[model_name] = m_schema
        m_schema = get_schema_ref(model_name, ref_prefix, ref_template, False)
    if m_definitions:
        m_schema.update({
            'definitions': m_definitions })
    return m_schema


def get_field_info_schema(field = None, schema_overrides = None):
    schema_ = { }
    if not field.field_info.title or lenient_issubclass(field.type_, Enum):
        if not field.field_info.title:
            schema_['title'] = field.alias.title().replace('_', ' ')
            if field.field_info.title:
                schema_overrides = True
    if field.field_info.description:
        schema_['description'] = field.field_info.description
        schema_overrides = True
# WARNING: Decompyle incomplete


def field_schema(field = None, *, by_alias, model_name_map, ref_prefix, ref_template, known_models):
