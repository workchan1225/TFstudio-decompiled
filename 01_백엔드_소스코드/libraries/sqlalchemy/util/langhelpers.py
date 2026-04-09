# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: langhelpers.pyc (Python 3.11)

'''Routines to help with the creation, loading and introspection of
modules, classes, hierarchies, attributes, functions, and methods.

'''
from __future__ import annotations
import collections
import enum
from functools import update_wrapper
import inspect
import itertools
import operator
import re
import sys
import textwrap
import threading
import types
from types import CodeType
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import warnings
from  import _collections
from  import compat
from _has_cy import HAS_CYEXTENSION
from typing import Literal
from  import exc
_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant = True)
_F = TypeVar('_F', bound = Callable[(..., Any)])
_MP = TypeVar('_MP', bound = 'memoized_property[Any]')
_MA = TypeVar('_MA', bound = 'HasMemoized.memoized_attribute[Any]')
_HP = TypeVar('_HP', bound = 'hybridproperty[Any]')
_HM = TypeVar('_HM', bound = 'hybridmethod[Any]')
if compat.py314:
    from annotationlib import call_annotate_function
    from annotationlib import Format
    
    def _get_and_call_annotate(obj, format):
        annotate = getattr(obj, '__annotate__', None)
    # WARNING: Decompyle incomplete

    _BASE_GET_ANNOTATIONS = type.__dict__['__annotations__'].__get__
    
    def _get_dunder_annotations(obj):
        pass
    # WARNING: Decompyle incomplete

    
    def _vendored_get_annotations(obj = None, *, format):
        '''A sparse implementation of annotationlib.get_annotations()'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_annotations(obj = None):
        return _vendored_get_annotations(obj, format = Format.FORWARDREF)

elif compat.py310:
    
    def get_annotations(obj = None):
        return inspect.get_annotations(obj)

else:
    
    def get_annotations(obj = None):
        if isinstance(obj, type):
            ann = obj.__dict__.get('__annotations__', None)
        else:
            ann = getattr(obj, '__annotations__', None)
    # WARNING: Decompyle incomplete


def md5_hex(x = None):
    x = x.encode('utf-8')
    m = compat.md5_not_for_security()
    m.update(x)
    return cast(str, m.hexdigest())


class safe_reraise:
    '''Reraise an exception after invoking some
    handler code.

    Stores the existing exception info before
    invoking so that it is maintained across a potential
    coroutine context switch.

    e.g.::

        try:
            sess.commit()
        except:
            with safe_reraise():
                sess.rollback()

    TODO: we should at some point evaluate current behaviors in this regard
    based on current greenlet, gevent/eventlet implementations in Python 3, and
    also see the degree to which our own asyncio (based on greenlet also) is
    impacted by this. .rollback() will cause IO / context switch to occur in
    all these scenarios; what happens to the exception context from an
    "except:" block if we don\'t explicitly store it? Original issue was #2703.

    '''
    _exc_info: 'Union[None, Tuple[Type[BaseException], BaseException, types.TracebackType], Tuple[None, None, None]]' = ('_exc_info',)
    
    def __enter__(self = None):
        self._exc_info = sys.exc_info()

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Optional[Type[BaseException]]', 'value', 'Optional[BaseException]', 'traceback', 'Optional[types.TracebackType]', 'return', 'NoReturn')):
        pass
    # WARNING: Decompyle incomplete



def walk_subclasses(cls = None):
    pass
# WARNING: Decompyle incomplete


def string_or_unprintable(element = None):
    if isinstance(element, str):
        return element
    
    try:
        return str(element)
    except Exception:
        return 



def clsname_as_plain_name(cls = None, use_name = None):
    if not use_name:
        pass
    name = cls.__name__
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(re.findall('([A-Z][a-z]+|SQL)', name)())


def method_is_overridden(instance_or_cls = None, against_method = None):
    """Return True if the two class methods don't match."""
    if not isinstance(instance_or_cls, type):
        current_cls = instance_or_cls.__class__
    else:
        current_cls = instance_or_cls
    method_name = against_method.__name__
    current_method = getattr(current_cls, method_name)
    return current_method != against_method


def decode_slice(slc = None):
    '''decode a slice object as sent to __getitem__.

    takes into account the 2.5 __index__() method, basically.

    '''
    ret = []
    for x in (slc.start, slc.stop, slc.step):
        if hasattr(x, '__index__'):
            x = x.__index__()
        ret.append(x)
        return tuple(ret)


def _unique_symbols(used = None, *bases):
    pass
# WARNING: Decompyle incomplete


def map_bits(fn = None, n = None):
    '''Call the given function given each nonzero bit from n.'''
    pass
# WARNING: Decompyle incomplete

_Fn = TypeVar('_Fn', bound = 'Callable[..., Any]')

def decorator(target = None):
    '''A signature-matching decorator factory.'''
    pass
# WARNING: Decompyle incomplete


def _exec_code_in_env(code = None, env = None, fn_name = None):
    exec(code, env)
    return env[fn_name]

_PF = TypeVar('_PF')
_TE = TypeVar('_TE')

class PluginLoader:
    
    def __init__(self = None, group = None, auto_fn = None):
        self.group = group
        self.impls = { }
        self.auto_fn = auto_fn

    
    def clear(self):
        self.impls.clear()

    
    def load(self = None, name = None):
        if name in self.impls:
            return self.impls[name]()
        if None.auto_fn:
            loader = self.auto_fn(name)
            if loader:
                self.impls[name] = loader
                return loader()
            for impl in None.importlib_metadata_get(self.group):
                if impl.name == name:
                    self.impls[name] = impl.load
                    
                    return None, impl.load()
                raise exc.NoSuchModuleError(f'''Can\'t load plugin: {self.group!s}:{name!s}''')

    
    def register(self = None, name = None, modulepath = None, objname = ('name', 'str', 'modulepath', 'str', 'objname', 'str', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def deregister(self = None, name = None):
        del self.impls[name]



def _inspect_func_args(fn):
    
    try:
        co_varkeywords = inspect.CO_VARKEYWORDS
        co = fn.__code__
        nargs = co.co_argcount
        return (list(co.co_varnames[:nargs]), bool(co.co_flags & co_varkeywords))
    except AttributeError:
        spec = compat.inspect_getfullargspec(fn)
        return 


get_cls_kwargs = (lambda cls = None, *, _set: pass)()
get_cls_kwargs = (lambda cls = None, *, _set: pass)()

def get_cls_kwargs(cls = None, *, _set, raiseerr):
    """Return the full set of inherited kwargs for the given `cls`.

    Probes a class's __init__ method, collecting all named arguments.  If the
    __init__ defines a \\**kwargs catch-all, then the constructor is presumed
    to pass along unrecognized keywords to its base classes, and the
    collection process is repeated recursively on each of the bases.

    Uses a subset of inspect.getfullargspec() to cut down on method overhead,
    as this is used within the Core typing system to create copies of type
    objects which is a performance-sensitive operation.

    No anonymous tuple arguments please !

    """
    toplevel = _set is None
    if toplevel:
        _set = set()
# WARNING: Decompyle incomplete


def get_func_kwargs(func = None):
    '''Return the set of legal kwargs for the given `func`.

    Uses getargspec so is safe to call for methods, functions,
    etc.

    '''
    return compat.inspect_getfullargspec(func)[0]


def get_callable_argspec(fn = None, no_self = None, _is_init = None):
    '''Return the argument signature for any callable.

    All pure-Python callables are accepted, including
    functions, methods, classes, objects with __call__;
    builtins and other edge cases like functools.partial() objects
    raise a TypeError.

    '''
    if inspect.isbuiltin(fn):
        raise TypeError("Can't inspect builtin: %s" % fn)
    if inspect.isfunction(fn):
        if _is_init and no_self:
            spec = compat.inspect_getfullargspec(fn)
            return compat.FullArgSpec(spec.args[1:], spec.varargs, spec.varkw, spec.defaults, spec.kwonlyargs, spec.kwonlydefaults, spec.annotations)
        return None.inspect_getfullargspec(fn)
    if None.ismethod(fn):
        if no_self:
            if _is_init or fn.__self__:
                spec = compat.inspect_getfullargspec(fn.__func__)
                return compat.FullArgSpec(spec.args[1:], spec.varargs, spec.varkw, spec.defaults, spec.kwonlyargs, spec.kwonlydefaults, spec.annotations)
            return None.inspect_getfullargspec(fn.__func__)
        if None.isclass(fn):
            return get_callable_argspec(fn.__init__, no_self = no_self, _is_init = True)
        if None(fn, '__func__'):
            return compat.inspect_getfullargspec(fn.__func__)
        if None(fn, '__call__'):
            if inspect.ismethod(fn.__call__):
                return get_callable_argspec(fn.__call__, no_self = no_self)
            raise None("Can't inspect callable: %s" % fn)
        raise TypeError("Can't inspect callable: %s" % fn)


def format_argspec_plus(fn = None, grouped = None):
    """Returns a dictionary of formatted, introspected function arguments.

    A enhanced variant of inspect.formatargspec to support code generation.

    fn
       An inspectable callable or tuple of inspect getargspec() results.
    grouped
      Defaults to True; include (parens, around, argument) lists

    Returns:

    args
      Full inspect.formatargspec for fn
    self_arg
      The name of the first positional argument, varargs[0], or None
      if the function defines no positional arguments.
    apply_pos
      args, re-written in calling rather than receiving syntax.  Arguments are
      passed positionally.
    apply_kw
      Like apply_pos, except keyword-ish args are passed as keywords.
    apply_pos_proxied
      Like apply_pos but omits the self/cls argument

    Example::

      >>> format_argspec_plus(lambda self, a, b, c=3, **d: 123)
      {'grouped_args': '(self, a, b, c=3, **d)',
       'self_arg': 'self',
       'apply_kw': '(self, a, b, c=c, **d)',
       'apply_pos': '(self, a, b, c, **d)'}

    """
    if callable(fn):
        spec = compat.inspect_getfullargspec(fn)
    else:
        spec = fn
# WARNING: Decompyle incomplete


def format_argspec_init(method, grouped = (True,)):
