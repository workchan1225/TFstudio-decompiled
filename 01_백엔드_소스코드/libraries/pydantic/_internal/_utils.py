# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

'''Bucket of reusable internal utilities.

This should be reduced as much as possible with functions only used in one place, moved to that place.
'''
from __future__ import annotations as _annotations
import dataclasses
import keyword
import sys
import warnings
import weakref
from collections import OrderedDict, defaultdict, deque
from collections.abc import Callable, Iterable, Mapping
from collections.abc import Set as AbstractSet
from copy import deepcopy
from functools import cached_property
from inspect import Parameter
from itertools import zip_longest
from types import BuiltinFunctionType, CodeType, FunctionType, GeneratorType, LambdaType, ModuleType
from typing import TYPE_CHECKING, Any, Generic, TypeVar, overload
from pydantic_core import MISSING
from typing_extensions import TypeAlias, TypeGuard, deprecated
from pydantic import PydanticDeprecatedSince211
from  import _repr, _typing_extra
from _import_utils import import_cached_base_model
if TYPE_CHECKING:
    MappingIntStrAny: 'TypeAlias' = Mapping[(int, Any)] | Mapping[(str, Any)]
    AbstractSetIntStr: 'TypeAlias' = AbstractSet[int] | AbstractSet[str]
    from main import BaseModel
IMMUTABLE_NON_COLLECTIONS_TYPES: 'set[type[Any]]' = {
    int,
    float,
    complex,
    str,
    bool,
    bytes,
    type,
    _typing_extra.NoneType,
    FunctionType,
    BuiltinFunctionType,
    LambdaType,
    weakref.ref,
    CodeType,
    ModuleType,
    NotImplemented.__class__,
    Ellipsis.__class__}
BUILTIN_COLLECTIONS: 'set[type[Any]]' = {
    list,
    set,
    tuple,
    frozenset,
    dict,
    OrderedDict,
    defaultdict,
    deque}

def can_be_positional(param = None):
    '''Return whether the parameter accepts a positional argument.

    ```python {test="skip" lint="skip"}
    def func(a, /, b, *, c):
        pass

    params = inspect.signature(func).parameters
    can_be_positional(params[\'a\'])
    #> True
    can_be_positional(params[\'b\'])
    #> True
    can_be_positional(params[\'c\'])
    #> False
    ```
    '''
    return param.kind in (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD)


def sequence_like(v = None):
    return isinstance(v, (list, tuple, set, frozenset, GeneratorType, deque))


def lenient_isinstance(o = None, class_or_tuple = None):
    
    try:
        return isinstance(o, class_or_tuple)
    except TypeError:
        return False



def lenient_issubclass(cls = None, class_or_tuple = None):
    
    try:
        if isinstance(cls, type):
            return issubclass(cls, class_or_tuple)
        except TypeError:
            if isinstance(cls, _typing_extra.WithArgsTypes):
                return False



def is_model_class(cls = None):
