# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _make.pyc (Python 3.11)

from __future__ import annotations
import abc
import contextlib
import copy
import enum
import inspect
import itertools
import linecache
import sys
import types
import unicodedata
import weakref
from collections.abc import Callable, Mapping
from functools import cached_property
from typing import Any, NamedTuple, TypeVar
from  import _compat, _config, setters
from _compat import PY_3_10_PLUS, PY_3_11_PLUS, PY_3_13_PLUS, _AnnotationExtractor, _get_annotations, get_generic_base
from exceptions import DefaultAlreadySetError, FrozenInstanceError, NotAnAttrsClassError, UnannotatedAttributeError
_OBJ_SETATTR = object.__setattr__
_INIT_FACTORY_PAT = '__attr_factory_%s'
_CLASSVAR_PREFIXES = ('typing.ClassVar', 't.ClassVar', 'ClassVar', 'typing_extensions.ClassVar')
_HASH_CACHE_FIELD = '_attrs_cached_hash'
_EMPTY_METADATA_SINGLETON = types.MappingProxyType({ })
_SENTINEL = object()
_DEFAULT_ON_SETATTR = setters.pipe(setters.convert, setters.validate)

class _Nothing(enum.Enum):
    '''
    Sentinel to indicate the lack of a value when `None` is ambiguous.

    If extending attrs, you can use ``typing.Literal[NOTHING]`` to show
    that a value may be ``NOTHING``.

    .. versionchanged:: 21.1.0 ``bool(NOTHING)`` is now False.
    .. versionchanged:: 22.2.0 ``NOTHING`` is now an ``enum.Enum`` variant.
    '''
    NOTHING = enum.auto()
    
    def __repr__(self):
        return 'NOTHING'

    
    def __bool__(self):
        return False


NOTHING = _Nothing.NOTHING

class _CacheHashWrapper(int):
    """
    An integer subclass that pickles / copies as None

    This is used for non-slots classes with ``cache_hash=True``, to avoid
    serializing a potentially (even likely) invalid hash value. Since `None`
    is the default value for uncalculated hashes, whenever this is copied,
    the copy's value for the hash should automatically reset.

    See GH #613 for more details.
    """
    
    def __reduce__(self, _none_constructor, _args = (type(None), ())):
        return (_none_constructor, _args)



def attrib(default, validator, repr, cmp, hash, init, metadata, type, converter, factory, kw_only, eq, order, on_setattr, alias = (NOTHING, None, True, None, None, True, None, None, None, None, None, None, None, None, None)):
    """
    Create a new field / attribute on a class.

    Identical to `attrs.field`, except it's not keyword-only.

    Consider using `attrs.field` in new code (``attr.ib`` will *never* go away,
    though).

    ..  warning::

        Does **nothing** unless the class is also decorated with
        `attr.s` (or similar)!


    .. versionadded:: 15.2.0 *convert*
    .. versionadded:: 16.3.0 *metadata*
    .. versionchanged:: 17.1.0 *validator* can be a ``list`` now.
    .. versionchanged:: 17.1.0
       *hash* is `None` and therefore mirrors *eq* by default.
    .. versionadded:: 17.3.0 *type*
    .. deprecated:: 17.4.0 *convert*
    .. versionadded:: 17.4.0
       *converter* as a replacement for the deprecated *convert* to achieve
       consistency with other noun-based arguments.
    .. versionadded:: 18.1.0
       ``factory=f`` is syntactic sugar for ``default=attr.Factory(f)``.
    .. versionadded:: 18.2.0 *kw_only*
    .. versionchanged:: 19.2.0 *convert* keyword argument removed.
    .. versionchanged:: 19.2.0 *repr* also accepts a custom callable.
    .. deprecated:: 19.2.0 *cmp* Removal on or after 2021-06-01.
    .. versionadded:: 19.2.0 *eq* and *order*
    .. versionadded:: 20.1.0 *on_setattr*
    .. versionchanged:: 20.3.0 *kw_only* backported to Python 2
    .. versionchanged:: 21.1.0
       *eq*, *order*, and *cmp* also accept a custom callable
    .. versionchanged:: 21.1.0 *cmp* undeprecated
    .. versionadded:: 22.2.0 *alias*
    .. versionchanged:: 25.4.0
       *kw_only* can now be None, and its default is also changed from False to
       None.
    """
    (eq, eq_key, order, order_key) = _determine_attrib_eq_order(cmp, eq, order, True)
# WARNING: Decompyle incomplete


def _compile_and_eval(script = None, globs = None, locs = None, filename = (None, '')):
    '''
    Evaluate the script with the given global (globs) and local (locs)
    variables.
    '''
    bytecode = compile(script, filename, 'exec')
    eval(bytecode, globs, locs)


def _linecache_and_compile(script = None, filename = None, globs = None, locals = (None,)):
    '''
    Cache the script with _linecache_, compile it and return the _locals_.
    '''
    pass
# WARNING: Decompyle incomplete


def _make_attr_tuple_class(cls_name = None, attr_names = None):
    '''
    Create a tuple subclass to hold `Attribute`s for an `attrs` class.

    The subclass is a bare tuple with properties for names.

    class MyClassAttributes(tuple):
        __slots__ = ()
        x = property(itemgetter(0))
    '''
    attr_class_name = f'''{cls_name}Attributes'''
    body = { }
    for i, attr_name in enumerate(attr_names):
        
        def getter(self, i = (i,)):
            return self[i]

        body[attr_name] = property(getter)
        return type(attr_class_name, (tuple,), body)


class _Attributes(NamedTuple):
    base_attrs_map: 'dict[str, type]' = '_Attributes'


def _is_class_var(annot):
    '''
    Check whether *annot* is a typing.ClassVar.

    The string comparison hack is used to avoid evaluating all string
    annotations which would put attrs-based classes at a performance
    disadvantage compared to plain old classes.
    '''
    annot = str(annot)
    if annot.startswith(("'", '"')) and annot.endswith(("'", '"')):
        annot = annot[1:-1]
    return annot.startswith(_CLASSVAR_PREFIXES)


def _has_own_attribute(cls, attrib_name):
    """
    Check whether *cls* defines *attrib_name* (and doesn't just inherit it).
    """
    return attrib_name in cls.__dict__


def _collect_base_attrs(cls = None, taken_attr_names = None):
    '''
    Collect attr.ibs from base classes of *cls*, except *taken_attr_names*.
    '''
    base_attrs = []
    base_attr_map = { }
    for base_cls in reversed(cls.__mro__[1:-1]):
        for a in getattr(base_cls, '__attrs_attrs__', []):
            if a.inherited or a.name in taken_attr_names:
                continue
            a = a.evolve(inherited = True)
            base_attrs.append(a)
            base_attr_map[a.name] = base_cls
            filtered = []
            seen = set()
            for a in reversed(base_attrs):
                if a.name in seen:
                    continue
                filtered.insert(0, a)
                seen.add(a.name)
                return (filtered, base_attr_map)


def _collect_base_attrs_broken(cls, taken_attr_names):
    '''
    Collect attr.ibs from base classes of *cls*, except *taken_attr_names*.

    N.B. *taken_attr_names* will be mutated.

    Adhere to the old incorrect behavior.

    Notably it collects from the front and considers inherited attributes which
    leads to the buggy behavior reported in #428.
    '''
    base_attrs = []
    base_attr_map = { }
    for base_cls in cls.__mro__[1:-1]:
        for a in getattr(base_cls, '__attrs_attrs__', []):
            if a.name in taken_attr_names:
                continue
            a = a.evolve(inherited = True)
            taken_attr_names.add(a.name)
            base_attrs.append(a)
            base_attr_map[a.name] = base_cls
            return (base_attrs, base_attr_map)


def _transform_attrs(cls, these, auto_attribs = None, kw_only = None, collect_by_mro = None, field_transformer = ('return', '_Attributes')):
    """
    Transform all `_CountingAttr`s on a class into `Attribute`s.

    If *these* is passed, use that and don't look for them on the class.

    If *collect_by_mro* is True, collect them in the correct MRO order,
    otherwise use the old -- incorrect -- order.  See #428.

    Return an `_Attributes`.
    """
    pass
# WARNING: Decompyle incomplete


def _make_cached_property_getattr(cached_properties, original_getattr, cls):
    lines = [
        'def wrapper(_cls):',
        '    __class__ = _cls',
        '    def __getattr__(self, item, cached_properties=cached_properties, original_getattr=original_getattr, _cached_setattr_get=_cached_setattr_get):',
        '         func = cached_properties.get(item)',
        '         if func is not None:',
        '              result = func(self)',
        '              _setter = _cached_setattr_get(self)',
        '              _setter(item, result)',
        '              return result']
# WARNING: Decompyle incomplete


def _frozen_setattrs(self, name, value):
    '''
    Attached to frozen classes as __setattr__.
    '''
    if isinstance(self, BaseException) and name in ('__cause__', '__context__', '__traceback__', '__suppress_context__', '__notes__'):
        BaseException.__setattr__(self, name, value)
        return None
    raise None


def _frozen_delattrs(self, name):
    '''
    Attached to frozen classes as __delattr__.
    '''
    if isinstance(self, BaseException) and name in ('__notes__',):
        BaseException.__delattr__(self, name)
        return None
    raise None


def evolve(*args, **changes):
    """
    Create a new instance, based on the first positional argument with
    *changes* applied.

    .. tip::

       On Python 3.13 and later, you can also use `copy.replace` instead.

    Args:

        inst:
            Instance of a class with *attrs* attributes. *inst* must be passed
            as a positional argument.

        changes:
            Keyword changes in the new copy.

    Returns:
        A copy of inst with *changes* incorporated.

    Raises:
        TypeError:
            If *attr_name* couldn't be found in the class ``__init__``.

        attrs.exceptions.NotAnAttrsClassError:
            If *cls* is not an *attrs* class.

    .. versionadded:: 17.1.0
    .. deprecated:: 23.1.0
       It is now deprecated to pass the instance using the keyword argument
       *inst*. It will raise a warning until at least April 2024, after which
       it will become an error. Always pass the instance as a positional
       argument.
    .. versionchanged:: 24.1.0
       *inst* can't be passed as a keyword argument anymore.
    """
    
    try:
        (inst,) = args
    except ValueError:
        msg = f'''evolve() takes 1 positional argument, but {len(args)} were given'''
        raise TypeError(msg), None

    cls = inst.__class__
    attrs = fields(cls)
# WARNING: Decompyle incomplete


class _ClassBuilder:
    '''
    Iteratively build *one* class.
    '''
    __slots__ = ('_add_method_dunders', '_attr_names', '_attrs', '_base_attr_map', '_base_names', '_cache_hash', '_cls', '_cls_dict', '_delete_attribs', '_frozen', '_has_custom_setattr', '_has_post_init', '_has_pre_init', '_is_exc', '_on_setattr', '_pre_init_has_args', '_repr_added', '_script_snippets', '_slots', '_weakref_slot', '_wrote_own_setattr')
    
    def __init__(self, cls, these = None, auto_attribs = None, props = None, has_custom_setattr = ('cls', 'type', 'auto_attribs', 'bool', 'props', 'ClassProps', 'has_custom_setattr', 'bool')):
        (attrs, base_attrs, base_map) = _transform_attrs(cls, these, auto_attribs, props.kw_only, props.collected_fields_by_mro, props.field_transformer)
        self._cls = cls
        self._cls_dict = dict(cls.__dict__) if props.is_slotted else { }
        self._attrs = attrs
        self._base_names = base_attrs()
        self._base_attr_map = base_map
        self._attr_names = (lambda .0: pass# WARNING: Decompyle incomplete
)(attrs())
        self._slots = props.is_slotted
        self._frozen = props.is_frozen
        self._weakref_slot = props.has_weakref_slot
        self._cache_hash = props.hashability is ClassProps.Hashability.HASHABLE_CACHED
        self._has_pre_init = bool(getattr(cls, '__attrs_pre_init__', False))
        self._pre_init_has_args = False
        if self._has_pre_init:
            pre_init_func = cls.__attrs_pre_init__
            pre_init_signature = inspect.signature(pre_init_func)
            self._pre_init_has_args = len(pre_init_signature.parameters) > 1
        self._has_post_init = bool(getattr(cls, '__attrs_post_init__', False))
        self._delete_attribs = not bool(these)
        self._is_exc = props.is_exception
        self._on_setattr = props.on_setattr_hook
        self._has_custom_setattr = has_custom_setattr
        self._wrote_own_setattr = False
        self._cls_dict['__attrs_attrs__'] = self._attrs
        self._cls_dict['__attrs_props__'] = props
        if props.is_frozen:
            self._cls_dict['__setattr__'] = _frozen_setattrs
            self._cls_dict['__delattr__'] = _frozen_delattrs
            self._wrote_own_setattr = True
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''<_ClassBuilder(cls={self._cls.__name__})>'''

    
    def _eval_snippets(self = None):
        '''
        Evaluate any registered snippets in one go.
        '''
        script = (lambda .0: [ snippet[0] for snippet in .0 ])(self._script_snippets())
        globs = { }
        for _, snippet_globs, _ in self._script_snippets:
            globs.update(snippet_globs)
            locs = _linecache_and_compile(script, _generate_unique_filename(self._cls, 'methods'), globs)
            for _, _, hook in self._script_snippets:
                hook(self._cls_dict, locs)
                return None

    
    def build_class(self):
        '''
        Finalize class based on the accumulated configuration.

        Builder cannot be used after calling this method.
        '''
        self._eval_snippets()
        if self._slots is True:
            cls = self._create_slots_class()
            self._cls.__attrs_base_of_slotted__ = weakref.ref(cls)
        else:
            cls = self._patch_original_class()
            if PY_3_10_PLUS:
                cls = abc.update_abstractmethods(cls)
        if getattr(cls, '__attrs_init_subclass__', None) and '__attrs_init_subclass__' not in cls.__dict__:
            cls.__attrs_init_subclass__()
        return cls

    
    def _patch_original_class(self):
        '''
        Apply accumulated methods and return the class.
        '''
        cls = self._cls
        base_names = self._base_names
        if self._delete_attribs:
            for name in self._attr_names:
                if name not in base_names and getattr(cls, name, _SENTINEL) is not _SENTINEL:
                    contextlib.suppress(AttributeError)
                    delattr(cls, name)
                    None(None, None)
                else:
                    with None:
                        if not None:
                            pass
                for name, value in self._cls_dict.items():
                    setattr(cls, name, value)
                    if self._wrote_own_setattr and getattr(cls, '__attrs_own_setattr__', False):
                        cls.__attrs_own_setattr__ = False
                        if not self._has_custom_setattr:
                            cls.__setattr__ = _OBJ_SETATTR
        return cls

    
    def _create_slots_class(self):
        '''
        Build and return a new class with a `__slots__` attribute.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_repr(self, ns):
        pass
    # WARNING: Decompyle incomplete

    
    def add_str(self):
        if not self._repr_added:
            msg = '__str__ can only be generated if a __repr__ exists.'
            raise ValueError(msg)
        
        def __str__(self):
            return self.__repr__()

        self._cls_dict['__str__'] = self._add_method_dunders(__str__)
        return self

    
    def _make_getstate_setstate(self):
        '''
        Create custom __setstate__ and __getstate__ methods.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def make_unhashable(self):
        self._cls_dict['__hash__'] = None
        return self

    
    def add_hash(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_init(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_replace(self):
        self._cls_dict['__replace__'] = self._add_method_dunders((lambda self: pass# WARNING: Decompyle incomplete
))
        return self

    
    def add_match_args(self):
        self._cls_dict['__match_args__'] = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._attrs())

    
    def add_attrs_init(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_eq(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_order(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_setattr(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _add_method_dunders_unsafe(self = None, method = None):
        '''
        Add __module__ and __qualname__ to a *method*.
        '''
        method.__module__ = self._cls.__module__
        method.__qualname__ = f'''{self._cls.__qualname__}.{method.__name__}'''
        method.__doc__ = f'''Method generated by attrs for class {self._cls.__qualname__}.'''
        return method

    
    def _add_method_dunders_safe(self = None, method = None):
