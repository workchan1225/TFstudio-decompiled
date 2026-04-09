# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing.pyc (Python 3.11)

'''
The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs.

Among other things, the module includes the following:
* Generic, Protocol, and internal machinery to support generic aliases.
  All subscripted types like X[int], Union[int, str] are generic aliases.
* Various "special forms" that have unique meanings in type annotations:
  NoReturn, Never, ClassVar, Self, Concatenate, Unpack, and others.
* Classes whose instances can be type arguments to generic classes and functions:
  TypeVar, ParamSpec, TypeVarTuple.
* Public helper functions: get_type_hints, overload, cast, final, and others.
* Several protocols to support duck-typing:
  SupportsFloat, SupportsIndex, SupportsAbs, and others.
* Special types: NewType, NamedTuple, TypedDict.
* Deprecated wrapper submodules for re and io related types.
* Deprecated aliases for builtin types and collections.abc ABCs.

Any name not present in __all__ is an implementation detail
that may be changed without notice. Use at your own risk!
'''
from abc import abstractmethod, ABCMeta
import collections
from collections import defaultdict
import collections.abc as collections
import contextlib
import functools
import operator
import re as stdlib_re
import sys
import types
import warnings
from types import WrapperDescriptorType, MethodWrapperType, MethodDescriptorType, GenericAlias

try:
    from _typing import _idfunc
except ImportError:
    
    def _idfunc(_, x):
        return x


__all__ = [
    'Annotated',
    'Any',
    'Callable',
    'ClassVar',
    'Concatenate',
    'Final',
    'ForwardRef',
    'Generic',
    'Literal',
    'Optional',
    'ParamSpec',
    'Protocol',
    'Tuple',
    'Type',
    'TypeVar',
    'TypeVarTuple',
    'Union',
    'AbstractSet',
    'ByteString',
    'Container',
    'ContextManager',
    'Hashable',
    'ItemsView',
    'Iterable',
    'Iterator',
    'KeysView',
    'Mapping',
    'MappingView',
    'MutableMapping',
    'MutableSequence',
    'MutableSet',
    'Sequence',
    'Sized',
    'ValuesView',
    'Awaitable',
    'AsyncIterator',
    'AsyncIterable',
    'Coroutine',
    'Collection',
    'AsyncGenerator',
    'AsyncContextManager',
    'Reversible',
    'SupportsAbs',
    'SupportsBytes',
    'SupportsComplex',
    'SupportsFloat',
    'SupportsIndex',
    'SupportsInt',
    'SupportsRound',
    'ChainMap',
    'Counter',
    'Deque',
    'Dict',
    'DefaultDict',
    'List',
    'OrderedDict',
    'Set',
    'FrozenSet',
    'NamedTuple',
    'TypedDict',
    'Generator',
    'BinaryIO',
    'IO',
    'Match',
    'Pattern',
    'TextIO',
    'AnyStr',
    'assert_type',
    'assert_never',
    'cast',
    'clear_overloads',
    'dataclass_transform',
    'final',
    'get_args',
    'get_origin',
    'get_overloads',
    'get_type_hints',
    'is_typeddict',
    'LiteralString',
    'Never',
    'NewType',
    'no_type_check',
    'no_type_check_decorator',
    'NoReturn',
    'NotRequired',
    'overload',
    'ParamSpecArgs',
    'ParamSpecKwargs',
    'Required',
    'reveal_type',
    'runtime_checkable',
    'Self',
    'Text',
    'TYPE_CHECKING',
    'TypeAlias',
    'TypeGuard',
    'Unpack']

def _type_convert(arg = None, module = (None,), *, allow_special_forms):
    '''For converting None to type(None), and strings to ForwardRef.'''
    pass
# WARNING: Decompyle incomplete


def _type_check(arg, msg = None, is_argument = (True, None), module = {
    'allow_special_forms': False }, *, allow_special_forms):
    '''Check that the argument is a type, and return it (internal helper).

    As a special case, accept None and return type(None) instead. Also wrap strings
    into ForwardRef instances. Consider several corner cases, for example plain
    special forms like Union are not valid, while Union[int, str] is OK, etc.
    The msg argument is a human-readable error message, e.g.::

        "Union[arg, ...]: arg should be a type."

    We append the repr() of the actual value (truncated to 100 chars).
    '''
    invalid_generic_forms = (Generic, Protocol)
    if not allow_special_forms:
        invalid_generic_forms += (ClassVar,)
        if is_argument:
            invalid_generic_forms += (Final,)
    arg = _type_convert(arg, module = module, allow_special_forms = allow_special_forms)
    if isinstance(arg, _GenericAlias) and arg.__origin__ in invalid_generic_forms:
        raise TypeError(f'''{arg} is not valid as type argument''')
    if arg in (Any, LiteralString, NoReturn, Never, Self, TypeAlias):
        return arg
    if None and arg in (ClassVar, Final):
        return arg
    if None(arg, _SpecialForm) or arg in (Generic, Protocol):
        raise TypeError(f'''Plain {arg} is not valid as type argument''')
    if type(arg) is tuple:
        raise TypeError(f'''{msg} Got {arg!r:.100}.''')
    return arg


def _is_param_expr(arg):
    if not arg is ...:
        pass
    return isinstance(arg, (tuple, list, ParamSpec, _ConcatenateGenericAlias))


def _should_unflatten_callable_args(typ, args):
