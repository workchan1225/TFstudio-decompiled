# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: copy_internals.pyc (Python 3.11)

from __future__ import annotations as _annotations
import typing
from copy import deepcopy
from enum import Enum
from typing import Any
import typing_extensions
from _internal import _model_construction, _typing_extra, _utils
if typing.TYPE_CHECKING:
    from  import BaseModel
    from _internal._utils import AbstractSetIntStr, MappingIntStrAny
    AnyClassMethod = classmethod[(Any, Any, Any)]
    TupleGenerator = typing.Generator[(tuple[(str, Any)], None, None)]
    Model = typing.TypeVar('Model', bound = 'BaseModel')
    IncEx: 'typing_extensions.TypeAlias' = 'set[int] | set[str] | dict[int, Any] | dict[str, Any] | None'
_object_setattr = _model_construction.object_setattr

def _iter(self, to_dict, by_alias, include = None, exclude = None, exclude_unset = None, exclude_defaults = (False, False, None, None, False, False, False), exclude_none = ('self', 'BaseModel', 'to_dict', 'bool', 'by_alias', 'bool', 'include', 'AbstractSetIntStr | MappingIntStrAny | None', 'exclude', 'AbstractSetIntStr | MappingIntStrAny | None', 'exclude_unset', 'bool', 'exclude_defaults', 'bool', 'exclude_none', 'bool', 'return', 'TupleGenerator')):
    pass
# WARNING: Decompyle incomplete


def _copy_and_set_values(self = None, values = None, fields_set = None, extra = (None, None), private = ('self', 'Model', 'values', 'dict[str, Any]', 'fields_set', 'set[str]', 'extra', 'dict[str, Any] | None', 'private', 'dict[str, Any] | None', 'deep', 'bool', 'return', 'Model'), *, deep):
    if deep:
        values = deepcopy(values)
        extra = deepcopy(extra)
        private = deepcopy(private)
    cls = self.__class__
    m = cls.__new__(cls)
    _object_setattr(m, '__dict__', values)
    _object_setattr(m, '__pydantic_extra__', extra)
    _object_setattr(m, '__pydantic_fields_set__', fields_set)
    _object_setattr(m, '__pydantic_private__', private)
    return m

_get_value = (lambda cls, v, to_dict, by_alias, include, exclude = None, exclude_unset = None, exclude_defaults = typing.no_type_check, exclude_none = ('cls', 'type[BaseModel]', 'v', 'Any', 'to_dict', 'bool', 'by_alias', 'bool', 'include', 'AbstractSetIntStr | MappingIntStrAny | None', 'exclude', 'AbstractSetIntStr | MappingIntStrAny | None', 'exclude_unset', 'bool', 'exclude_defaults', 'bool', 'exclude_none', 'bool', 'return', 'Any'): pass# WARNING: Decompyle incomplete
)()

def _calculate_keys(self = None, include = None, exclude = None, exclude_unset = (None,), update = ('self', 'BaseModel', 'include', 'MappingIntStrAny | None', 'exclude', 'MappingIntStrAny | None', 'exclude_unset', 'bool', 'update', 'dict[str, Any] | None', 'return', 'typing.AbstractSet[str] | None')):
    pass
# WARNING: Decompyle incomplete
