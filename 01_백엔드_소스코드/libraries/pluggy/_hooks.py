# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _hooks.pyc (Python 3.11)

'''
Internal hook annotation, representation and calling machinery.
'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Mapping
from collections.abc import Sequence
from collections.abc import Set
import inspect
import sys
from types import ModuleType
from typing import Any
from typing import Callable
from typing import Final
from typing import final
from typing import Optional
from typing import overload
from typing import TYPE_CHECKING
from typing import TypedDict
from typing import TypeVar
from typing import Union
import warnings
from _result import Result
_T = TypeVar('_T')
_F = TypeVar('_F', bound = Callable[(..., object)])
_Namespace = Union[(ModuleType, type)]
_Plugin = object
_HookExec = Callable[([
    str,
    Sequence['HookImpl'],
    Mapping[(str, object)],
    bool], Union[(object, list[object])])]
_HookImplFunction = Callable[(..., Union[(_T, Generator[(None, Result[_T], None)])])]

class HookspecOpts(TypedDict):
    warn_on_impl_args: 'Mapping[str, Warning] | None' = 'Options for a hook specification.'


class HookimplOpts(TypedDict):
    specname: 'str | None' = 'Options for a hook implementation.'

HookspecMarker = <NODE:12>()
HookimplMarker = <NODE:12>()

def normalize_hookimpl_opts(opts = None):
    opts.setdefault('tryfirst', False)
    opts.setdefault('trylast', False)
    opts.setdefault('wrapper', False)
    opts.setdefault('hookwrapper', False)
    opts.setdefault('optionalhook', False)
    opts.setdefault('specname', None)

_PYPY = hasattr(sys, 'pypy_version_info')

def varnames(func = None):
    '''Return tuple of positional and keywrord argument names for a function,
    method, class or callable.

    In case of a class, its ``__init__`` method is considered.
    For methods the ``self`` parameter is not included.
    '''
    pass
# WARNING: Decompyle incomplete

HookRelay = <NODE:12>()
_HookRelay = HookRelay
_CallHistory = list[tuple[(Mapping[(str, object)], Optional[Callable[([
    Any], None)]])]]

class HookCaller:
    '''A caller of all registered implementations of a hook specification.'''
    __slots__ = ('name', 'spec', '_hookexec', '_hookimpls', '_call_history')
    
    def __init__(self = None, name = None, hook_execute = None, specmodule_or_class = (None, None), spec_opts = ('name', 'str', 'hook_execute', '_HookExec', 'specmodule_or_class', '_Namespace | None', 'spec_opts', 'HookspecOpts | None', 'return', 'None')):
        ''':meta private:'''
        self.name = name
        self._hookexec = hook_execute
        self._hookimpls = []
        self._call_history = None
        self.spec = None
    # WARNING: Decompyle incomplete

    
    def has_spec(self = None):
        return self.spec is not None

    
    def set_specification(self = None, specmodule_or_class = None, spec_opts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_historic(self = None):
        '''Whether this caller is :ref:`historic <historic>`.'''
        return self._call_history is not None

    
    def _remove_plugin(self = None, plugin = None):
        for i, method in enumerate(self._hookimpls):
            if method.plugin == plugin:
                del self._hookimpls[i]
                return None
            raise ValueError(f'''plugin {plugin!r} not found''')

    
    def get_hookimpls(self = None):
        '''Get all registered hook implementations for this hook.'''
        return self._hookimpls.copy()

    
    def _add_hookimpl(self = None, hookimpl = None):
        '''Add an implementation to the callback chain.'''
        for i, method in enumerate(self._hookimpls):
            if method.hookwrapper or method.wrapper:
                splitpoint = i
            
            splitpoint = len(self._hookimpls)
            if hookimpl.hookwrapper or hookimpl.wrapper:
                end = len(self._hookimpls)
                start = splitpoint
            else:
                end = splitpoint
                start = 0
        if hookimpl.trylast:
            self._hookimpls.insert(start, hookimpl)
            return None
        if None.tryfirst:
            self._hookimpls.insert(end, hookimpl)
            return None
        i = None - 1
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<HookCaller {self.name!r}>'''

    
    def _verify_all_args_are_provided(self = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, **kwargs):
        '''Call the hook.

        Only accepts keyword arguments, which should match the hook
        specification.

        Returns the result(s) of calling all registered plugins, see
        :ref:`calling`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def call_historic(self = None, result_callback = None, kwargs = None):
        '''Call the hook with given ``kwargs`` for all registered plugins and
        for all plugins which will be registered afterwards, see
        :ref:`historic`.

        :param result_callback:
            If provided, will be called for each non-``None`` result obtained
            from a hook implementation.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def call_extra(self = None, methods = None, kwargs = None):
        '''Call the hook with some additional temporarily participating
        methods using the specified ``kwargs`` as call parameters, see
        :ref:`call_extra`.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _maybe_apply_history(self = None, method = None):
        '''Apply call history to a new hookimpl if it is marked as historic.'''
        pass
    # WARNING: Decompyle incomplete


_HookCaller = HookCaller

class _SubsetHookCaller(HookCaller):
    '''A proxy to another HookCaller which manages calls to all registered
    plugins except the ones from remove_plugins.'''
    __slots__ = ('_orig', '_remove_plugins')
    
    def __init__(self = None, orig = None, remove_plugins = None):
        self._orig = orig
        self._remove_plugins = remove_plugins
        self.name = orig.name
        self._hookexec = orig._hookexec

    _hookimpls = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    spec = (lambda self = None: self._orig.spec)()
    _call_history = (lambda self = None: self._orig._call_history)()
    
    def __repr__(self = None):
        return f'''<_SubsetHookCaller {self.name!r}>'''


HookImpl = <NODE:12>()
HookSpec = <NODE:12>()
