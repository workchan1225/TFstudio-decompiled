# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pydantic.pyc (Python 3.11)

from __future__ import annotations
import inspect
from typing import Any, TypeVar
from typing_extensions import TypeGuard
import pydantic
from _types import NOT_GIVEN
from _utils import is_dict as _is_dict, is_list
from _compat import PYDANTIC_V1, model_json_schema
_T = TypeVar('_T')

def to_strict_json_schema(model = None):
    if inspect.isclass(model) and is_basemodel_type(model):
        schema = model_json_schema(model)
    elif PYDANTIC_V1 and isinstance(model, pydantic.TypeAdapter):
        schema = model.json_schema()
    else:
        raise TypeError(f'''Non BaseModel types are only supported with Pydantic v2 - {model}''')
    return _ensure_strict_json_schema(schema, path = (), root = schema)


def _ensure_strict_json_schema(json_schema = None, *, path, root):
    '''Mutates the given JSON schema to ensure it conforms to the `strict` standard
    that the API expects.
    '''
    pass
# WARNING: Decompyle incomplete


def resolve_ref(*, root, ref):
    if not ref.startswith('#/'):
        raise ValueError(f'''Unexpected $ref format {ref!r}; Does not start with #/''')
    path = ref[2:].split('/')
    resolved = root
# WARNING: Decompyle incomplete


def is_basemodel_type(typ = None):
    if not inspect.isclass(typ):
        return False
    return None(typ, pydantic.BaseModel)


def is_dataclass_like_type(typ = None):
    '''Returns True if the given type likely used `@pydantic.dataclass`'''
    return hasattr(typ, '__pydantic_config__')


def is_dict(obj = None):
    return _is_dict(obj)


def has_more_than_n_keys(obj = None, n = None):
    i = 0
    for _ in obj.keys():
        i += 1
        if i > n:
            return True
        return False
