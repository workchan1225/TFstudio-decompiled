# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tools.pyc (Python 3.11)

import json
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Optional, Type, TypeVar, Union
from pydantic.v1.parse import Protocol, load_file, load_str_bytes
from pydantic.v1.types import StrBytes
from pydantic.v1.typing import display_as_type
__all__ = ('parse_file_as', 'parse_obj_as', 'parse_raw_as', 'schema_of', 'schema_json_of')
NameFactory = Union[(str, Callable[([
    Type[Any]], str)])]
if TYPE_CHECKING:
    from pydantic.v1.typing import DictStrAny

def _generate_parsing_type_name(type_ = None):
    return f'''ParsingModel[{display_as_type(type_)}]'''

_get_parsing_type = (lambda type_ = None, *, type_name: create_model = create_modelimport pydantic.v1.main# WARNING: Decompyle incomplete
)()
T = TypeVar('T')

def parse_obj_as(type_ = None, obj = None, *, type_name):
    model_type = _get_parsing_type(type_, type_name = type_name)
    return model_type(__root__ = obj).__root__


def parse_file_as(type_ = None, path = None, *, content_type, encoding, proto, allow_pickle, json_loads, type_name):
    obj = load_file(path, proto = proto, content_type = content_type, encoding = encoding, allow_pickle = allow_pickle, json_loads = json_loads)
    return parse_obj_as(type_, obj, type_name = type_name)


def parse_raw_as(type_ = None, b = None, *, content_type, encoding, proto, allow_pickle, json_loads, type_name):
    obj = load_str_bytes(b, proto = proto, content_type = content_type, encoding = encoding, allow_pickle = allow_pickle, json_loads = json_loads)
    return parse_obj_as(type_, obj, type_name = type_name)


def schema_of(type_ = None, *, title, **schema_kwargs):
    '''Generate a JSON schema (as dict) for the passed model or dynamically generated one'''
    pass
# WARNING: Decompyle incomplete


def schema_json_of(type_ = None, *, title, **schema_json_kwargs):
    '''Generate a JSON schema (as JSON) for the passed model or dynamically generated one'''
    pass
# WARNING: Decompyle incomplete
