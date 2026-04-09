# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dataclasses.pyc (Python 3.11)

import re
import sys
import copy
import types
import inspect
import keyword
import builtins
import functools
import itertools
import abc
import _thread
from types import FunctionType, GenericAlias
__all__ = [
    'dataclass',
    'field',
    'Field',
    'FrozenInstanceError',
    'InitVar',
    'KW_ONLY',
    'MISSING',
    'fields',
    'asdict',
    'astuple',
    'make_dataclass',
    'replace',
    'is_dataclass']

class FrozenInstanceError(AttributeError):
    pass


class _HAS_DEFAULT_FACTORY_CLASS:
    
    def __repr__(self):
        return '<factory>'


_HAS_DEFAULT_FACTORY = _HAS_DEFAULT_FACTORY_CLASS()

class _MISSING_TYPE:
    pass

MISSING = _MISSING_TYPE()

class _KW_ONLY_TYPE:
    pass

KW_ONLY = _KW_ONLY_TYPE()
_EMPTY_METADATA = types.MappingProxyType({ })

class _FIELD_BASE:
    
    def __init__(self, name):
        self.name = name

    
    def __repr__(self):
        return self.name


_FIELD = _FIELD_BASE('_FIELD')
_FIELD_CLASSVAR = _FIELD_BASE('_FIELD_CLASSVAR')
_FIELD_INITVAR = _FIELD_BASE('_FIELD_INITVAR')
_FIELDS = '__dataclass_fields__'
_PARAMS = '__dataclass_params__'
_POST_INIT_NAME = '__post_init__'
_MODULE_IDENTIFIER_RE = re.compile('^(?:\\s*(\\w+)\\s*\\.)?\\s*(\\w+)')

def _recursive_repr(user_function):
    pass
# WARNING: Decompyle incomplete


class InitVar:
    __slots__ = ('type',)
    
    def __init__(self, type):
        self.type = type

    
    def __repr__(self):
        if isinstance(self.type, type):
            type_name = self.type.__name__
        else:
            type_name = repr(self.type)
        return f'''dataclasses.InitVar[{type_name}]'''

    
    def __class_getitem__(cls, type):
        return InitVar(type)



class Field:
    __slots__ = ('name', 'type', 'default', 'default_factory', 'repr', 'hash', 'init', 'compare', 'metadata', 'kw_only', '_field_type')
    
    def __init__(self, default, default_factory, init, repr, hash, compare, metadata, kw_only):
        self.name = None
        self.type = None
        self.default = default
        self.default_factory = default_factory
        self.init = init
        self.repr = repr
        self.hash = hash
        self.compare = compare
    # WARNING: Decompyle incomplete

    __repr__ = (lambda self: f'''Field(name={self.name!r},type={self.type!r},default={self.default!r},default_factory={self.default_factory!r},init={self.init!r},repr={self.repr!r},hash={self.hash!r},compare={self.compare!r},metadata={self.metadata!r},kw_only={self.kw_only!r},_field_type={self._field_type})''')()
    
    def __set_name__(self, owner, name):
        func = getattr(type(self.default), '__set_name__', None)
        if func:
            func(self.default, owner, name)
            return None

    __class_getitem__ = classmethod(GenericAlias)


class _DataclassParams:
    __slots__ = ('init', 'repr', 'eq', 'order', 'unsafe_hash', 'frozen')
    
    def __init__(self, init, repr, eq, order, unsafe_hash, frozen):
        self.init = init
        self.repr = repr
        self.eq = eq
        self.order = order
        self.unsafe_hash = unsafe_hash
        self.frozen = frozen

    
    def __repr__(self):
        return f'''_DataclassParams(init={self.init!r},repr={self.repr!r},eq={self.eq!r},order={self.order!r},unsafe_hash={self.unsafe_hash!r},frozen={self.frozen!r})'''



def field(*, default, default_factory, init, repr, hash, compare, metadata, kw_only):
    """Return an object to identify dataclass fields.

    default is the default value of the field.  default_factory is a
    0-argument function called to initialize a field's value.  If init
    is true, the field will be a parameter to the class's __init__()
    function.  If repr is true, the field will be included in the
    object's repr().  If hash is true, the field will be included in the
    object's hash().  If compare is true, the field will be used in
    comparison functions.  metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass.  If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
    """
    if default is not MISSING and default_factory is not MISSING:
        raise ValueError('cannot specify both default and default_factory')
    return Field(default, default_factory, init, repr, hash, compare, metadata, kw_only)


def _fields_in_init_order(fields):
    return (tuple, (lambda .0: pass# WARNING: Decompyle incomplete
)(fields()))


def _tuple_str(obj_name, fields):
    pass
# WARNING: Decompyle incomplete


def _create_fn(name, args = None, body = {
    'globals': None,
    'locals': None,
    'return_type': MISSING }, *, globals, locals, return_type):
    pass
# WARNING: Decompyle incomplete


def _field_assign(frozen, name, value, self_name):
    if frozen:
        return f'''__dataclass_builtins_object__.__setattr__({self_name},{name!r},{value})'''
    return f'''{None}.{name}={value}'''


def _field_init(f, frozen, globals, self_name, slots):
    default_name = f'''_dflt_{f.name}'''
    if f.default_factory is not MISSING:
        if f.init:
            globals[default_name] = f.default_factory
            value = f'''{default_name}() if {f.name} is _HAS_DEFAULT_FACTORY else {f.name}'''
        else:
            globals[default_name] = f.default_factory
            value = f'''{default_name}()'''
    elif f.init:
        if f.default is MISSING:
            value = f.name
        elif f.default is not MISSING:
            globals[default_name] = f.default
            value = f.name
        elif slots and f.default is not MISSING:
            globals[default_name] = f.default
            value = default_name
        else:
            return None
        if None._field_type is _FIELD_INITVAR:
            return None
        return None(frozen, f.name, value, self_name)


def _init_param(f):
    if f.default is MISSING and f.default_factory is MISSING:
        default = ''
    elif f.default is not MISSING:
        default = f'''=_dflt_{f.name}'''
    elif f.default_factory is not MISSING:
        default = '=_HAS_DEFAULT_FACTORY'
    return f'''{f.name}:_type_{f.name}{default}'''


def _init_fn(fields, std_fields, kw_only_fields, frozen, has_post_init, self_name, globals, slots):
    seen_default = False
    for f in std_fields:
        if f.init:
            if not f.default is MISSING or f.default_factory is MISSING:
                seen_default = True
                continue
            if seen_default:
                raise TypeError(f'''non-default argument {f.name!r} follows default argument''')
        locals = fields()
        locals.update({
            'MISSING': MISSING,
            '_HAS_DEFAULT_FACTORY': _HAS_DEFAULT_FACTORY,
            '__dataclass_builtins_object__': object })
        body_lines = []
        for f in fields:
            line = _field_init(f, frozen, locals, self_name, slots)
            if line:
                body_lines.append(line)
            if has_post_init:
                params_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(fields())
                body_lines.append(f'''{self_name}.{_POST_INIT_NAME}({params_str})''')
    if not body_lines:
        body_lines = [
            'pass']
    _init_params = std_fields()
    if kw_only_fields:
        _init_params += [
            '*']
        (lambda .0: [ _init_param(f) for f in .0 ]) += kw_only_fields()
    return _create_fn('__init__', [
        self_name] + _init_params, body_lines, locals = locals, globals = globals, return_type = None)


def _repr_fn(fields, globals):
    fn = '__repr__'(('self',), 'return self.__class__.__qualname__ + f"(', [
        ', '.join + (lambda .0: [ f'''{f.name}={{self.{f.name}!r}}''' for f in .0 ])(fields()) + ')"'], globals = globals)
    return _recursive_repr(fn)


def _frozen_get_del_attr(cls, fields, globals):
    locals = {
        'cls': cls,
        'FrozenInstanceError': FrozenInstanceError }
    return (_create_fn('__setattr__', ('self', 'name', 'value'), (f'''if type(self) is cls or name in {fields_str}:''', ' raise FrozenInstanceError(f"cannot assign to field {name!r}")', 'super(cls, self).__setattr__(name, value)'), locals = locals, globals = globals), _create_fn('__delattr__', ('self', 'name'), (f'''if type(self) is cls or name in {fields_str}:''', ' raise FrozenInstanceError(f"cannot delete field {name!r}")', 'super(cls, self).__delattr__(name)'), locals = locals, globals = globals))


def _cmp_fn(name, op, self_tuple, other_tuple, globals):
    return _create_fn(name, ('self', 'other'), [
        'if other.__class__ is self.__class__:',
        f''' return {self_tuple}{op}{other_tuple}''',
        'return NotImplemented'], globals = globals)


def _hash_fn(fields, globals):
    self_tuple = _tuple_str('self', fields)
    return _create_fn('__hash__', ('self',), [
        f'''return hash({self_tuple})'''], globals = globals)


def _is_classvar(a_type, typing):
