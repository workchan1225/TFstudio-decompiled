# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _generics.pyc (Python 3.11)

from __future__ import annotations
import operator
import sys
import types
import typing
from collections import ChainMap
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from contextvars import ContextVar
from functools import reduce
from itertools import zip_longest
from types import prepare_class
from typing import TYPE_CHECKING, Annotated, Any, TypedDict, TypeVar, cast
from weakref import WeakValueDictionary
import typing_extensions
from typing_inspection import typing_objects
from typing_inspection.introspection import is_union_origin
from  import _typing_extra
from _core_utils import get_type_ref
from _forward_ref import PydanticRecursiveRef
from _utils import all_identical, is_model_class
if TYPE_CHECKING:
    from main import BaseModel
GenericTypesCacheKey = tuple[(Any, Any, tuple[(Any, ...)])]
KT = TypeVar('KT')
VT = TypeVar('VT')
_LIMITED_DICT_SIZE = 100

def LimitedDict():
    '''LimitedDict'''
    pass
# WARNING: Decompyle incomplete

LimitedDict = <NODE:27>(LimitedDict, 'LimitedDict', dict[(KT, VT)])
GenericTypesCache = WeakValueDictionary[(GenericTypesCacheKey, 'type[BaseModel]')]
_GENERIC_TYPES_CACHE: 'ContextVar[GenericTypesCache | None]' = ContextVar('_GENERIC_TYPES_CACHE', default = None)

class PydanticGenericMetadata(TypedDict):
    parameters: 'tuple[TypeVar, ...]' = 'PydanticGenericMetadata'


def create_generic_submodel(model_name = None, origin = None if TYPE_CHECKING else None, args = None, params = ('model_name', 'str', 'origin', 'type[BaseModel]', 'args', 'tuple[Any, ...]', 'params', 'tuple[Any, ...]', 'return', 'type[BaseModel]')):
    '''Dynamically create a submodel of a provided (generic) BaseModel.

    This is used when producing concrete parametrizations of generic models. This function
    only *creates* the new subclass; the schema/validators/serialization must be updated to
    reflect a concrete parametrization elsewhere.

    Args:
        model_name: The name of the newly created model.
        origin: The base class for the new model to inherit from.
        args: A tuple of generic metadata arguments.
        params: A tuple of generic metadata parameters.

    Returns:
        The created submodel.
    '''
    namespace = {
        '__module__': origin.__module__ }
    bases = (origin,)
    (meta, ns, kwds) = prepare_class(model_name, bases)
    namespace.update(ns)
# WARNING: Decompyle incomplete


def _get_caller_frame_info(depth = None):
    '''Used inside a function to check whether it was called globally.

    Args:
        depth: The depth to get the frame.

    Returns:
        A tuple contains `module_name` and `called_globally`.

    Raises:
        RuntimeError: If the function is not called inside a function.
    '''
    
    try:
        previous_caller_frame = sys._getframe(depth)
    except ValueError:
        e = None
        raise RuntimeError('This function must be used inside another function'), e
        e = None
        del e
        except AttributeError:
            return (None, False)

    frame_globals = previous_caller_frame.f_globals
    return (frame_globals.get('__name__'), previous_caller_frame.f_locals is frame_globals)

DictValues: 'type[Any]' = { }.values().__class__

def iter_contained_typevars(v = None):
    """Recursively iterate through all subtypes and type args of `v` and yield any typevars that are found.

    This is inspired as an alternative to directly accessing the `__parameters__` attribute of a GenericAlias,
    since __parameters__ of (nested) generic BaseModel subclasses won't show up in that list.
    """
    pass
# WARNING: Decompyle incomplete


def get_args(v = None):
    pydantic_generic_metadata = getattr(v, '__pydantic_generic_metadata__', None)
    if pydantic_generic_metadata:
        return pydantic_generic_metadata.get('args')
    return None.get_args(v)


def get_origin(v = None):
    pydantic_generic_metadata = getattr(v, '__pydantic_generic_metadata__', None)
    if pydantic_generic_metadata:
        return pydantic_generic_metadata.get('origin')
    return None.get_origin(v)


def get_standard_typevars_map(cls = None):
    """Package a generic type's typevars and parametrization (if present) into a dictionary compatible with the
    `replace_types` function. Specifically, this works with standard typing generics and typing._GenericAlias.
    """
    origin = get_origin(cls)
# WARNING: Decompyle incomplete


def get_model_typevars_map(cls = None):
    """Package a generic BaseModel's typevars and concrete parametrization (if present) into a dictionary compatible
    with the `replace_types` function.

    Since BaseModel.__class_getitem__ does not produce a typing._GenericAlias, and the BaseModel generic info is
    stored in the __pydantic_generic_metadata__ attribute, we need special handling here.
    """
    generic_metadata = cls.__pydantic_generic_metadata__
    origin = generic_metadata['origin']
    args = generic_metadata['args']
    if not args:
        return { }
    return None(zip(iter_contained_typevars(origin), args))


def replace_types(type_ = None, type_map = None):
    '''Return type with all occurrences of `type_map` keys recursively replaced with their values.

    Args:
        type_: The class or generic alias.
        type_map: Mapping from `TypeVar` instance to concrete types.

    Returns:
        A new type representing the basic structure of `type_` with all
        `typevar_map` keys recursively replaced.

    Example:
        ```python
        from typing import Union

        from pydantic._internal._generics import replace_types

        replace_types(tuple[str, Union[list[str], float]], {str: int})
        #> tuple[int, Union[list[int], float]]
        ```
    '''
    pass
# WARNING: Decompyle incomplete


def map_generic_model_arguments(cls = None, args = None):
    '''Return a mapping between the parameters of a generic model and the provided arguments during parameterization.

    Raises:
        TypeError: If the number of arguments does not match the parameters (i.e. if providing too few or too many arguments).

    Example:
        ```python {test="skip" lint="skip"}
        class Model[T, U, V = int](BaseModel): ...

        map_generic_model_arguments(Model, (str, bytes))
        #> {T: str, U: bytes, V: int}

        map_generic_model_arguments(Model, (str,))
        #> TypeError: Too few arguments for <class \'__main__.Model\'>; actual 1, expected at least 2

        map_generic_model_arguments(Model, (str, bytes, int, complex))
        #> TypeError: Too many arguments for <class \'__main__.Model\'>; actual 4, expected 3
        ```

    Note:
        This function is analogous to the private `typing._check_generic_specialization` function.
    '''
    parameters = cls.__pydantic_generic_metadata__['parameters']
    expected_len = len(parameters)
    typevars_map = { }
    _missing = object()
    for parameter, argument in zip_longest(parameters, args, fillvalue = _missing):
        if parameter is _missing:
            raise TypeError(f'''Too many arguments for {cls}; actual {len(args)}, expected {expected_len}''')
        if argument is _missing:
            param = cast(TypeVar, parameter)
            has_default = param.has_default()
        else:
            except AttributeError:
                has_default = False
            if has_default:
                typevars_map[param] = replace_types(param.__default__, typevars_map)
                continue
        sum -= (lambda .0: pass# WARNING: Decompyle incomplete
)(parameters())
        raise TypeError(f'''Too few arguments for {cls}; actual {len(args)}, expected at least {expected_len}''')
        param = cast(TypeVar, parameter)
        typevars_map[param] = argument
        return typevars_map

_generic_recursion_cache: 'ContextVar[set[str] | None]' = ContextVar('_generic_recursion_cache', default = None)
generic_recursion_self_type = (lambda origin = None, args = None: pass# WARNING: Decompyle incomplete
)()

def recursively_defined_type_refs():
    visited = _generic_recursion_cache.get()
    if not visited:
        return set()
    return None.copy()


def get_cached_generic_type_early(parent = None, typevar_values = None):
    '''The use of a two-stage cache lookup approach was necessary to have the highest performance possible for
    repeated calls to `__class_getitem__` on generic types (which may happen in tighter loops during runtime),
    while still ensuring that certain alternative parametrizations ultimately resolve to the same type.

    As a concrete example, this approach was necessary to make Model[List[T]][int] equal to Model[List[int]].
    The approach could be modified to not use two different cache keys at different points, but the
    _early_cache_key is optimized to be as quick to compute as possible (for repeated-access speed), and the
    _late_cache_key is optimized to be as "correct" as possible, so that two types that will ultimately be the
    same after resolving the type arguments will always produce cache hits.

    If we wanted to move to only using a single cache key per type, we would either need to always use the
    slower/more computationally intensive logic associated with _late_cache_key, or would need to accept
    that Model[List[T]][int] is a different type than Model[List[T]][int]. Because we rely on subclass relationships
    during validation, I think it is worthwhile to ensure that types that are functionally equivalent are actually
    equal.
    '''
    generic_types_cache = _GENERIC_TYPES_CACHE.get()
# WARNING: Decompyle incomplete


def get_cached_generic_type_late(parent = None, typevar_values = None, origin = None, args = ('parent', 'type[BaseModel]', 'typevar_values', 'Any', 'origin', 'type[BaseModel]', 'args', 'tuple[Any, ...]', 'return', 'type[BaseModel] | None')):
    '''See the docstring of `get_cached_generic_type_early` for more information about the two-stage cache lookup.'''
    generic_types_cache = _GENERIC_TYPES_CACHE.get()
# WARNING: Decompyle incomplete


def set_cached_generic_type(parent = None, typevar_values = None, type_ = None, origin = (None, None), args = ('parent', 'type[BaseModel]', 'typevar_values', 'tuple[Any, ...]', 'type_', 'type[BaseModel]', 'origin', 'type[BaseModel] | None', 'args', 'tuple[Any, ...] | None', 'return', 'None')):
    '''See the docstring of `get_cached_generic_type_early` for more information about why items are cached with
    two different keys.
    '''
    generic_types_cache = _GENERIC_TYPES_CACHE.get()
# WARNING: Decompyle incomplete


def _union_orderings_key(typevar_values = None):
    '''This is intended to help differentiate between Union types with the same arguments in different order.

    Thanks to caching internal to the `typing` module, it is not possible to distinguish between
    List[Union[int, float]] and List[Union[float, int]] (and similarly for other "parent" origins besides List)
    because `typing` considers Union[int, float] to be equal to Union[float, int].

    However, you _can_ distinguish between (top-level) Union[int, float] vs. Union[float, int].
    Because we parse items as the first Union type that is successful, we get slightly more consistent behavior
    if we make an effort to distinguish the ordering of items in a union. It would be best if we could _always_
    get the exact-correct order of items in the union, but that would require a change to the `typing` module itself.
    (See https://github.com/python/cpython/issues/86483 for reference.)
    '''
    if isinstance(typevar_values, tuple):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(typevar_values())
    if None.is_union(typing_extensions.get_origin(typevar_values)):
        return get_args(typevar_values)


def _early_cache_key(cls = None, typevar_values = None):
    """This is intended for minimal computational overhead during lookups of cached types.

    Note that this is overly simplistic, and it's possible that two different cls/typevar_values
    inputs would ultimately result in the same type being created in BaseModel.__class_getitem__.
    To handle this, we have a fallback _late_cache_key that is checked later if the _early_cache_key
    lookup fails, and should result in a cache hit _precisely_ when the inputs to __class_getitem__
    would result in the same type.
    """
    return (cls, typevar_values, _union_orderings_key(typevar_values))


def _late_cache_key(origin = None, args = None, typevar_values = None):
    '''This is intended for use later in the process of creating a new type, when we have more information
    about the exact args that will be passed. If it turns out that a different set of inputs to
    __class_getitem__ resulted in the same inputs to the generic type creation process, we can still
    return the cached type, and update the cache with the _early_cache_key as well.
    '''
    return (_union_orderings_key(typevar_values), origin, args)
