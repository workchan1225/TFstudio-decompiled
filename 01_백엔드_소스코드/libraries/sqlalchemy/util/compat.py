# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

'''Handle Python version/platform incompatibilities.'''
from __future__ import annotations
import base64
import dataclasses
import hashlib
import inspect
import operator
import platform
import sys
import sysconfig
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
py314b1 = sys.version_info >= (3, 14, 0, 'beta', 1)
py314 = sys.version_info >= (3, 14)
py313 = sys.version_info >= (3, 13)
py312 = sys.version_info >= (3, 12)
py311 = sys.version_info >= (3, 11)
py310 = sys.version_info >= (3, 10)
py39 = sys.version_info >= (3, 9)
py38 = sys.version_info >= (3, 8)
pypy = platform.python_implementation() == 'PyPy'
cpython = platform.python_implementation() == 'CPython'
freethreading = bool(sysconfig.get_config_var('Py_GIL_DISABLED'))
win32 = sys.platform.startswith('win')
osx = sys.platform.startswith('darwin')
arm = 'aarch' in platform.machine().lower()
is64bit = sys.maxsize > 0x100000000
has_refcount_gc = bool(cpython)
dottedgetter = operator.attrgetter
_T_co = TypeVar('_T_co', covariant = True)

class FullArgSpec(typing.NamedTuple):
    annotations: 'Dict[str, Any]' = 'FullArgSpec'


def inspect_getfullargspec(func = None):
    '''Fully vendored version of getfullargspec from Python 3.3.'''
    if inspect.ismethod(func):
        func = func.__func__
    if not inspect.isfunction(func):
        raise TypeError(f'''{func!r} is not a Python function''')
    co = func.__code__
    if not inspect.iscode(co):
        raise TypeError(f'''{co!r} is not a code object''')
    nargs = co.co_argcount
    names = co.co_varnames
    nkwargs = co.co_kwonlyargcount
    args = list(names[:nargs])
    kwonlyargs = list(names[nargs:nargs + nkwargs])
    nargs += nkwargs
    varargs = None
    if co.co_flags & inspect.CO_VARARGS:
        varargs = co.co_varnames[nargs]
        nargs = nargs + 1
    varkw = None
    if co.co_flags & inspect.CO_VARKEYWORDS:
        varkw = co.co_varnames[nargs]
    return FullArgSpec(args, varargs, varkw, func.__defaults__, kwonlyargs, func.__kwdefaults__, func.__annotations__)

if py39:
    
    def md5_not_for_security():
        return hashlib.md5(usedforsecurity = False)

else:
    
    def md5_not_for_security():
        return hashlib.md5()

if typing.TYPE_CHECKING or py38:
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata
if typing.TYPE_CHECKING or py39:
    dict_union = operator.or_
else:
    
    def dict_union(a = None, b = None):
        a = a.copy()
        a.update(b)
        return a

if py310:
    anext_ = anext
else:
    _NOT_PROVIDED = object()
    from collections.abc import AsyncIterator
    
    async def anext_(async_iterator, default = (_NOT_PROVIDED,)):
        '''vendored from https://github.com/python/cpython/pull/8895'''
        pass
    # WARNING: Decompyle incomplete


def importlib_metadata_get(group):
    ep = importlib_metadata.entry_points()
    if typing.TYPE_CHECKING or hasattr(ep, 'select'):
        return ep.select(group = group)
    return None.get(group, ())


def b(s):
    return s.encode('latin-1')


def b64decode(x = None):
    return base64.b64decode(x.encode('ascii'))


def b64encode(x = None):
    return base64.b64encode(x).decode('ascii')


def decode_backslashreplace(text = None, encoding = None):
    return text.decode(encoding, errors = 'backslashreplace')


def cmp(a, b):
    return (a > b) - (a < b)


def _formatannotation(annotation, base_module = (None,)):
    '''vendored from python 3.7'''
    if isinstance(annotation, str):
        return annotation
    if None(annotation, '__module__', None) == 'typing':
        return repr(annotation).replace('typing.', '').replace('~', '')
    if None(annotation, type):
        if annotation.__module__ in ('builtins', base_module):
            return repr(annotation.__qualname__)
        return None.__module__ + '.' + annotation.__qualname__
    if None(annotation, typing.TypeVar):
        return repr(annotation).replace('~', '')
    return None(annotation).replace('~', '')


def inspect_formatargspec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations, formatarg, formatvarargs = None, formatvarkw = None, formatvalue = None, formatreturns = (None, None, None, (), { }, { }, str, (lambda name: '*' + name), (lambda name: '**' + name), (lambda value: '=' + repr(value)), (lambda text: ' -> ' + str(text)), _formatannotation), formatannotation = ('args', 'List[str]', 'varargs', 'Optional[str]', 'varkw', 'Optional[str]', 'defaults', 'Optional[Sequence[Any]]', 'kwonlyargs', 'Optional[Sequence[str]]', 'kwonlydefaults', 'Optional[Mapping[str, Any]]', 'annotations', 'Mapping[str, Any]', 'formatarg', 'Callable[[str], str]', 'formatvarargs', 'Callable[[str], str]', 'formatvarkw', 'Callable[[str], str]', 'formatvalue', 'Callable[[Any], str]', 'formatreturns', 'Callable[[Any], str]', 'formatannotation', 'Callable[[Any], str]', 'return', 'str')):
    '''Copy formatargspec from python 3.7 standard library.

    Python 3 has deprecated formatargspec and requested that Signature
    be used instead, however this requires a full reimplementation
    of formatargspec() in terms of creating Parameter objects and such.
    Instead of introducing all the object-creation overhead and having
    to reinvent from scratch, just copy their compatibility routine.

    Ultimately we would need to rewrite our "decorator" routine completely
    which is not really worth it right now, until all Python 2.x support
    is dropped.

    '''
    pass
# WARNING: Decompyle incomplete


def dataclass_fields(cls = None):
    '''Return a sequence of all dataclasses.Field objects associated
    with a class as an already processed dataclass.

    The class must **already be a dataclass** for Field objects to be returned.

    '''
    if dataclasses.is_dataclass(cls):
        return dataclasses.fields(cls)


def local_dataclass_fields(cls = None):
    '''Return a sequence of all dataclasses.Field objects associated with
    an already processed dataclass, excluding those that originate from a
    superclass.

    The class must **already be a dataclass** for Field objects to be returned.

    '''
    pass
# WARNING: Decompyle incomplete

if freethreading:
    import threading
    mini_gil = threading.RLock()
    return None
import contextlib
mini_gil = contextlib.nullcontext()
