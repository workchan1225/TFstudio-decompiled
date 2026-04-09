# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _manager.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence
import inspect
import types
from typing import Any
from typing import Callable
from typing import cast
from typing import Final
from typing import TYPE_CHECKING
import warnings
from  import _tracing
from _callers import _multicall
from _hooks import _HookImplFunction
from _hooks import _Namespace
from _hooks import _Plugin
from _hooks import _SubsetHookCaller
from _hooks import HookCaller
from _hooks import HookImpl
from _hooks import HookimplOpts
from _hooks import HookRelay
from _hooks import HookspecOpts
from _hooks import normalize_hookimpl_opts
from _result import Result
if TYPE_CHECKING:
    import importlib.metadata as importlib
_BeforeTrace = Callable[([
    str,
    Sequence[HookImpl],
    Mapping[(str, Any)]], None)]
_AfterTrace = Callable[([
    Result[Any],
    str,
    Sequence[HookImpl],
    Mapping[(str, Any)]], None)]

def _warn_for_function(warning = None, function = None):
    func = cast(types.FunctionType, function)
    warnings.warn_explicit(warning, type(warning), lineno = func.__code__.co_firstlineno, filename = func.__code__.co_filename)


class PluginValidationError(Exception):
    pass
# WARNING: Decompyle incomplete


class DistFacade:
    '''Emulate a pkg_resources Distribution'''
    
    def __init__(self = None, dist = None):
        self._dist = dist

    project_name = (lambda self = None: name = self.metadata['name']name)()
    
    def __getattr__(self = None, attr = None, default = None):
        return getattr(self._dist, attr, default)

    
    def __dir__(self = None):
        return sorted(dir(self._dist) + [
            '_dist',
            'project_name'])



class PluginManager:
    """Core class which manages registration of plugin objects and 1:N hook
    calling.

    You can register new hooks by calling :meth:`add_hookspecs(module_or_class)
    <PluginManager.add_hookspecs>`.

    You can register plugin objects (which contain hook implementations) by
    calling :meth:`register(plugin) <PluginManager.register>`.

    For debugging purposes you can call :meth:`PluginManager.enable_tracing`
    which will subsequently send debug information to the trace helper.

    :param project_name:
        The short project name. Prefer snake case. Make sure it's unique!
    """
    
    def __init__(self = None, project_name = None):
        self.project_name = project_name
        self._name2plugin = { }
        self._plugin_distinfo = []
        self.hook = HookRelay()
        self.trace = _tracing.TagTracer().get('pluginmanage')
        self._inner_hookexec = _multicall

    
    def _hookexec(self, hook_name = None, methods = None, kwargs = None, firstresult = ('hook_name', 'str', 'methods', 'Sequence[HookImpl]', 'kwargs', 'Mapping[str, object]', 'firstresult', 'bool', 'return', 'object | list[object]')):
        return self._inner_hookexec(hook_name, methods, kwargs, firstresult)

    
    def register(self = None, plugin = None, name = None):
        '''Register a plugin and return its name.

        :param name:
            The name under which to register the plugin. If not specified, a
            name is generated using :func:`get_canonical_name`.

        :returns:
            The plugin name. If the name is blocked from registering, returns
            ``None``.

        If the plugin is already registered, raises a :exc:`ValueError`.
        '''
        if not name:
            pass
        plugin_name = self.get_canonical_name(plugin)
    # WARNING: Decompyle incomplete

    
    def parse_hookimpl_opts(self = None, plugin = None, name = None):
        '''Try to obtain a hook implementation from an item with the given name
        in the given plugin which is being searched for hook impls.

        :returns:
            The parsed hookimpl options, or None to skip the given item.

        This method can be overridden by ``PluginManager`` subclasses to
        customize how hook implementation are picked up. By default, returns the
        options for items decorated with :class:`HookimplMarker`.
        '''
        method = getattr(plugin, name)
        if not inspect.isroutine(method):
            return None
        
        try:
            res = getattr(method, self.project_name + '_impl', None)
        except Exception:
            res = { }

    # WARNING: Decompyle incomplete

    
    def unregister(self = None, plugin = None, name = None):
        '''Unregister a plugin and all of its hook implementations.

        The plugin can be specified either by the plugin object or the plugin
        name. If both are specified, they must agree.

        Returns the unregistered plugin, or ``None`` if not found.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_blocked(self = None, name = None):
        '''Block registrations of the given name, unregister if already registered.'''
        self.unregister(name = name)
        self._name2plugin[name] = None

    
    def is_blocked(self = None, name = None):
        '''Return whether the given plugin name is blocked.'''
        if name in self._name2plugin:
            pass
        return self._name2plugin[name] is None

    
    def unblock(self = None, name = None):
        '''Unblocks a name.

        Returns whether the name was actually blocked.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_hookspecs(self = None, module_or_class = None):
        '''Add new hook specifications defined in the given ``module_or_class``.

        Functions are recognized as hook specifications if they have been
        decorated with a matching :class:`HookspecMarker`.
        '''
        names = []
    # WARNING: Decompyle incomplete

    
    def parse_hookspec_opts(self = None, module_or_class = None, name = None):
        '''Try to obtain a hook specification from an item with the given name
        in the given module or class which is being searched for hook specs.

        :returns:
            The parsed hookspec options for defining a hook, or None to skip the
            given item.

        This method can be overridden by ``PluginManager`` subclasses to
        customize how hook specifications are picked up. By default, returns the
        options for items decorated with :class:`HookspecMarker`.
        '''
        method = getattr(module_or_class, name)
        opts = getattr(method, self.project_name + '_spec', None)
        return opts

    
    def get_plugins(self = None):
        '''Return a set of all registered plugin objects.'''
        return self._name2plugin.values()()

    
    def is_registered(self = None, plugin = None):
        '''Return whether the plugin is already registered.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_canonical_name(self = None, plugin = None):
        '''Return a canonical name for a plugin object.

        Note that a plugin may be registered under a different name
        specified by the caller of :meth:`register(plugin, name) <register>`.
        To obtain the name of a registered plugin use :meth:`get_name(plugin)
        <get_name>` instead.
        '''
        name = getattr(plugin, '__name__', None)
        if not name:
            pass
        return str(id(plugin))

    
    def get_plugin(self = None, name = None):
        '''Return the plugin registered under the given name, if any.'''
        return self._name2plugin.get(name)

    
    def has_plugin(self = None, name = None):
        '''Return whether a plugin with the given name is registered.'''
        return self.get_plugin(name) is not None

    
    def get_name(self = None, plugin = None):
        """Return the name the plugin is registered under, or ``None`` if
        is isn't."""
        for name, val in self._name2plugin.items():
            if plugin == val:
                
                return None, name
            return None

    
    def _verify_hook(self = None, hook = None, hookimpl = None):
        if hook.is_historic():
            if hookimpl.hookwrapper or hookimpl.wrapper:
                raise PluginValidationError(hookimpl.plugin, f'''Plugin {hookimpl.plugin_name!r}\nhook {hook.name!r}\nhistoric incompatible with yield/wrapper/hookwrapper''')
    # WARNING: Decompyle incomplete

    
    def check_pending(self = None):
        '''Verify that all hooks which have not been verified against a
        hook specification are optional, otherwise raise
        :exc:`PluginValidationError`.'''
        for name in self.hook.__dict__:
            if name[0] == '_':
                continue
            hook = getattr(self.hook, name)
            if not hook.has_spec():
                for hookimpl in hook.get_hookimpls():
                    if not hookimpl.optionalhook:
                        raise PluginValidationError(hookimpl.plugin, f'''unknown hook {name!r} in plugin {hookimpl.plugin!r}''')
                    return None

    
    def load_setuptools_entrypoints(self = None, group = None, name = None):
        '''Load modules from querying the specified setuptools ``group``.

        :param group:
            Entry point group to load plugins.
        :param name:
            If given, loads only plugins with the given ``name``.

        :return:
            The number of plugins loaded by this call.
        '''
        import importlib.metadata as importlib
        count = 0
    # WARNING: Decompyle incomplete

    
    def list_plugin_distinfo(self = None):
        '''Return a list of (plugin, distinfo) pairs for all
        setuptools-registered plugins.'''
        return list(self._plugin_distinfo)

    
    def list_name_plugin(self = None):
        '''Return a list of (name, plugin) pairs for all registered plugins.'''
        return list(self._name2plugin.items())

    
    def get_hookcallers(self = None, plugin = None):
        '''Get all hook callers for the specified plugin.

        :returns:
            The hook callers, or ``None`` if ``plugin`` is not registered in
            this plugin manager.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_hookcall_monitoring(self = None, before = None, after = None):
        '''Add before/after tracing functions for all hooks.

        Returns an undo function which, when called, removes the added tracers.

        ``before(hook_name, hook_impls, kwargs)`` will be called ahead
        of all hook calls and receive a hookcaller instance, a list
        of HookImpl instances and the keyword arguments for the hook call.

        ``after(outcome, hook_name, hook_impls, kwargs)`` receives the
        same arguments as ``before`` but also a :class:`~pluggy.Result` object
        which represents the result of the overall hook call.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def enable_tracing(self = None):
        '''Enable tracing of hook calls.

        Returns an undo function which, when called, removes the added tracing.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def subset_hook_caller(self = None, name = None, remove_plugins = None):
        '''Return a proxy :class:`~pluggy.HookCaller` instance for the named
        method which manages calls to all registered plugins except the ones
        from remove_plugins.'''
        pass
    # WARNING: Decompyle incomplete



def _formatdef(func = None):
    return f'''{func.__name__}{inspect.signature(func)}'''
