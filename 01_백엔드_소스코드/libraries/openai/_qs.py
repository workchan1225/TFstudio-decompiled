# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _qs.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, List, Tuple, Union, Mapping, TypeVar
from urllib.parse import parse_qs, urlencode
from typing_extensions import Literal, get_args
from _types import NotGiven, not_given
from _utils import flatten
_T = TypeVar('_T')
ArrayFormat = Literal[('comma', 'repeat', 'indices', 'brackets')]
NestedFormat = Literal[('dots', 'brackets')]
PrimitiveData = Union[(str, int, float, bool, None)]
Data = Union[(PrimitiveData, List[Any], Tuple[Any], 'Mapping[str, Any]')]
Params = Mapping[(str, Data)]

class Querystring:
    nested_format: 'NestedFormat' = 'Querystring'
    
    def __init__(self = None, *, array_format, nested_format):
        self.array_format = array_format
        self.nested_format = nested_format

    
    def parse(self = None, query = None):
        return parse_qs(query)

    
    def stringify(self = None, params = None, *, array_format, nested_format):
        return urlencode(self.stringify_items(params, array_format = array_format, nested_format = nested_format))

    
    def stringify_items(self = None, params = None, *, array_format, nested_format):
        pass
    # WARNING: Decompyle incomplete

    
    def _stringify_item(self = None, key = None, value = None, opts = ('key', 'str', 'value', 'Data', 'opts', 'Options', 'return', 'list[tuple[str, str]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _primitive_value_to_str(self = None, value = None):
        if value is True:
            return 'true'
        if None is False:
            return 'false'
    # WARNING: Decompyle incomplete


_qs = Querystring()
parse = _qs.parse
stringify = _qs.stringify
stringify_items = _qs.stringify_items

class Options:
    nested_format: 'NestedFormat' = 'Options'
    
    def __init__(self = None, qs = None, *, array_format, nested_format):
        self.array_format = qs.array_format if isinstance(array_format, NotGiven) else array_format
        self.nested_format = qs.nested_format if isinstance(nested_format, NotGiven) else nested_format
