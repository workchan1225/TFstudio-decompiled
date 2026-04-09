# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing.pyc (Python 3.11)

import functools
import operator
import sys
import typing
from collections.abc import Callable
from os import PathLike
from typing import TYPE_CHECKING, AbstractSet, Any, Callable as TypingCallable, ClassVar, Dict, ForwardRef, Generator, Iterable, List, Mapping, NewType, Optional, Sequence, Set, Tuple, Type, TypeVar, Union, _eval_type, cast, get_type_hints
from typing_extensions import Annotated, Final, Literal, NotRequired as TypedDictNotRequired, Required as TypedDictRequired

try:
    from typing import _TypingBase as typing_base
except ImportError:
    from typing import _Final as typing_base


try:
    from typing import GenericAlias as TypingGenericAlias
except ImportError:
    TypingGenericAlias = ()


try:
    from types import UnionType as TypesUnionType
except ImportError:
    TypesUnionType = ()

if sys.version_info < (3, 9):
    
    def evaluate_forwardref(type_ = None, globalns = None, localns = None):
        return type_._evaluate(globalns, localns)

elif sys.version_info < (3, 12, 4):
    
    def evaluate_forwardref(type_ = None, globalns = None, localns = None):
        return cast(Any, type_)._evaluate(globalns, localns, recursive_guard = set())

else:
    
    def evaluate_forwardref(type_ = None, globalns = None, localns = None):
        return cast(Any, type_)._evaluate(globalns, localns, type_params = (), recursive_guard = set())

if sys.version_info < (3, 9):
    get_all_type_hints = get_type_hints
else:
    
    def get_all_type_hints(obj = None, globalns = None, localns = None):
        return get_type_hints(obj, globalns, localns, include_extras = True)

_T = TypeVar('_T')
AnyCallable = TypingCallable[(..., Any)]
NoArgAnyCallable = TypingCallable[([], Any)]
AnyArgTCallable = TypingCallable[(..., _T)]
AnnotatedTypeNames = {
    'AnnotatedMeta',
    '_AnnotatedAlias'}
LITERAL_TYPES: Set[Any] = {
    Literal}
if hasattr(typing, 'Literal'):
    LITERAL_TYPES.add(typing.Literal)
if sys.version_info < (3, 8):
    
    def get_origin(t = None):
        if type(t).__name__ in AnnotatedTypeNames:
            return cast(Type[Any], Annotated)
        return None(t, '__origin__', None)

else:
    from typing import get_origin as _typing_get_origin
    
    def get_origin(tp = None):
