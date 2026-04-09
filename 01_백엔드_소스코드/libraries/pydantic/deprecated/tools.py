# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tools.pyc (Python 3.11)

from __future__ import annotations
import json
import warnings
from typing import TYPE_CHECKING, Any, Callable, TypeVar, Union
from typing_extensions import deprecated
from json_schema import DEFAULT_REF_TEMPLATE, GenerateJsonSchema
from type_adapter import TypeAdapter
from warnings import PydanticDeprecatedSince20
if not TYPE_CHECKING:
    DeprecationWarning = PydanticDeprecatedSince20
__all__ = ('parse_obj_as', 'schema_of', 'schema_json_of')
NameFactory = Union[(str, Callable[([
    type[Any]], str)])]
T = TypeVar('T')
parse_obj_as = (lambda type_ = None, obj = None, type_name = deprecated('`parse_obj_as` is deprecated. Use `pydantic.TypeAdapter.validate_python` instead.', category = None): warnings.warn('`parse_obj_as` is deprecated. Use `pydantic.TypeAdapter.validate_python` instead.', category = PydanticDeprecatedSince20, stacklevel = 2)# WARNING: Decompyle incomplete
)()
schema_of = (lambda type_ = None, *, title: warnings.warn('`schema_of` is deprecated. Use `pydantic.TypeAdapter.json_schema` instead.', category = PydanticDeprecatedSince20, stacklevel = 2)res = TypeAdapter(type_).json_schema(by_alias = by_alias, schema_generator = schema_generator, ref_template = ref_template)# WARNING: Decompyle incomplete
)()
schema_json_of = (lambda type_ = None, *, title: warnings.warn('`schema_json_of` is deprecated. Use `pydantic.TypeAdapter.json_schema` instead.', category = PydanticDeprecatedSince20, stacklevel = 2)# WARNING: Decompyle incomplete
)()
