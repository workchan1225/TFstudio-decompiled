# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing_extensions.pyc (Python 3.11)

import abc
import builtins
import collections
import collections.abc as collections
import contextlib
import enum
import functools
import inspect
import io
import keyword
import operator
import sys
import types as _types
import typing
import warnings
if sys.version_info >= (3, 14):
    import annotationlib
__all__ = [
    'Any',
    'ClassVar',
    'Concatenate',
    'Final',
    'LiteralString',
    'ParamSpec',
    'ParamSpecArgs',
    'ParamSpecKwargs',
    'Self',
    'Type',
    'TypeVar',
    'TypeVarTuple',
    'Unpack',
    'Awaitable',
    'AsyncIterator',
    'AsyncIterable',
    'Coroutine',
    'AsyncGenerator',
    'AsyncContextManager',
    'Buffer',
    'ChainMap',
    'ContextManager',
    'Counter',
    'Deque',
    'DefaultDict',
    'NamedTuple',
    'OrderedDict',
    'TypedDict',
    'SupportsAbs',
    'SupportsBytes',
    'SupportsComplex',
    'SupportsFloat',
    'SupportsIndex',
    'SupportsInt',
    'SupportsRound',
    'Reader',
    'Writer',
    'Annotated',
    'assert_never',
    'assert_type',
    'clear_overloads',
    'dataclass_transform',
    'deprecated',
    'disjoint_base',
    'Doc',
    'evaluate_forward_ref',
    'get_overloads',
    'final',
    'Format',
    'get_annotations',
    'get_args',
    'get_origin',
    'get_original_bases',
    'get_protocol_members',
    'get_type_hints',
    'IntVar',
    'is_protocol',
    'is_typeddict',
    'Literal',
    'NewType',
    'overload',
    'override',
    'Protocol',
    'Sentinel',
    'reveal_type',
    'runtime',
    'runtime_checkable',
    'Text',
    'TypeAlias',
    'TypeAliasType',
    'TypeForm',
    'TypeGuard',
    'TypeIs',
    'TYPE_CHECKING',
    'type_repr',
    'Never',
    'NoReturn',
    'ReadOnly',
    'Required',
    'NotRequired',
    'NoDefault',
    'NoExtraItems',
    'AbstractSet',
    'AnyStr',
    'BinaryIO',
    'Callable',
    'Collection',
    'Container',
    'Dict',
    'ForwardRef',
    'FrozenSet',
    'Generator',
    'Generic',
    'Hashable',
    'IO',
    'ItemsView',
    'Iterable',
    'Iterator',
    'KeysView',
    'List',
    'Mapping',
    'MappingView',
    'Match',
    'MutableMapping',
    'MutableSequence',
    'MutableSet',
    'Optional',
    'Pattern',
    'Reversible',
    'Sequence',
    'Set',
    'Sized',
    'TextIO',
    'Tuple',
    'Union',
    'ValuesView',
    'cast',
    'no_type_check',
    'no_type_check_decorator']
PEP_560 = True
GenericMeta = type
_PEP_696_IMPLEMENTED = sys.version_info >= (3, 13, 0, 'beta')
_FORWARD_REF_HAS_CLASS = '__forward_is_class__' in typing.ForwardRef.__slots__

class _Sentinel:
    
    def __repr__(self):
        return '<sentinel>'


_marker = _Sentinel()
NoReturn = typing.NoReturn
T = typing.TypeVar('T')
KT = typing.TypeVar('KT')
VT = typing.TypeVar('VT')
T_co = typing.TypeVar('T_co', covariant = True)
T_contra = typing.TypeVar('T_contra', contravariant = True)
ClassVar = typing.ClassVar

def _SpecialForm():
    '''_SpecialForm'''
    __slots__ = ('_name', '__doc__', '_getitem')
    
    def __init__(self, getitem):
        self._getitem = getitem
        self._name = getitem.__name__
        self.__doc__ = getitem.__doc__

    
    def __getattr__(self, item):
        if item in frozenset({'__name__', '__qualname__'}):
            return self._name
        raise None(item)

    
    def __mro_entries__(self, bases):
        raise TypeError(f'''Cannot subclass {self!r}''')

    
    def __repr__(self):
        return f'''typing_extensions.{self._name}'''

    
    def __reduce__(self):
        return self._name

    
    def __call__(self, *args, **kwds):
        raise TypeError(f'''Cannot instantiate {self!r}''')

    
    def __or__(self, other):
        return typing.Union[(self, other)]

    
    def __ror__(self, other):
        return typing.Union[(other, self)]

    
    def __instancecheck__(self, obj):
        raise TypeError(f'''{self} cannot be used with isinstance()''')

    
    def __subclasscheck__(self, cls):
        raise TypeError(f'''{self} cannot be used with issubclass()''')

    __getitem__ = (lambda self, parameters: self._getitem(self, parameters))()

_SpecialForm = <NODE:27>(_SpecialForm, '_SpecialForm', typing._Final, _root = True)

def _ExtensionsSpecialForm():
    '''_ExtensionsSpecialForm'''
    
    def __repr__(self):
        return 'typing_extensions.' + self._name


_ExtensionsSpecialForm = <NODE:27>(_ExtensionsSpecialForm, '_ExtensionsSpecialForm', typing._SpecialForm, _root = True)
Final = typing.Final

def IntVar(name):
    return typing.TypeVar(name)

_overload_dummy = typing._overload_dummy
Type = typing.Type
Awaitable = typing.Awaitable
Coroutine = typing.Coroutine
AsyncIterable = typing.AsyncIterable
AsyncIterator = typing.AsyncIterator
Deque = typing.Deque
DefaultDict = typing.DefaultDict
OrderedDict = typing.OrderedDict
Counter = typing.Counter
ChainMap = typing.ChainMap
Text = typing.Text
TYPE_CHECKING = typing.TYPE_CHECKING
_PROTO_ALLOWLIST = {
    'collections.abc': [
        'Callable',
        'Awaitable',
        'Iterable',
        'Iterator',
        'AsyncIterable',
        'Hashable',
        'Sized',
        'Container',
        'Collection',
        'Reversible',
        'Buffer'],
    'contextlib': [
        'AbstractContextManager',
        'AbstractAsyncContextManager'],
    'typing_extensions': [
        'Buffer'] }
_EXCLUDED_ATTRS = frozenset(typing.EXCLUDED_ATTRIBUTES) | {
    '__final__',
    '__match_args__',
    '__protocol_attrs__',
    '__non_callable_proto_members__'}

def _get_protocol_attrs(cls):
