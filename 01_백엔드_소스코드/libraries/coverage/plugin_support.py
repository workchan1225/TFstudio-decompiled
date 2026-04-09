# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plugin_support.pyc (Python 3.11)

'''Support for plugins.'''
from __future__ import annotations
import os
import os.path as os
import sys
from collections.abc import Iterable, Iterator
from types import FrameType
from typing import Any, Callable
from coverage.exceptions import PluginError
from coverage.misc import isolate_module
from coverage.plugin import CoveragePlugin, FileReporter, FileTracer
from coverage.types import TArc, TConfigurable, TDebugCtl, TLineNo, TPluginConfig, TSourceTokenLines
os = isolate_module(os)

class Plugins:
    '''The currently loaded collection of coverage.py plugins.'''
    
    def __init__(self = None, debug = None):
        self.order = []
        self.names = { }
        self.file_tracers = []
        self.configurers = []
        self.context_switchers = []
        self.current_module = None
        self.debug = debug

    
    def load_from_config(self = None, modules = None, config = None):
        '''Load plugin modules, and read their settings from configuration.'''
        for module in modules:
            self.current_module = module
            __import__(module)
            mod = sys.modules[module]
            coverage_init = getattr(mod, 'coverage_init', None)
            if not coverage_init:
                raise PluginError(f'''Plugin module {module!r} didn\'t define a coverage_init function''')
            options = config.get_plugin_options(module)
            coverage_init(self, options)
            self.current_module = None
            return None

    
    def load_from_callables(self = None, plugin_inits = None):
        '''Load plugins from callables provided.'''
        for fn in plugin_inits:
            fn(self)
            return None

    
    def add_file_tracer(self = None, plugin = None):
        '''Add a file tracer plugin.

        `plugin` is an instance of a third-party plugin class.  It must
        implement the :meth:`CoveragePlugin.file_tracer` method.

        '''
        self._add_plugin(plugin, self.file_tracers)

    
    def add_configurer(self = None, plugin = None):
        '''Add a configuring plugin.

        `plugin` is an instance of a third-party plugin class. It must
        implement the :meth:`CoveragePlugin.configure` method.

        '''
        self._add_plugin(plugin, self.configurers)

    
    def add_dynamic_context(self = None, plugin = None):
        '''Add a dynamic context plugin.

        `plugin` is an instance of a third-party plugin class.  It must
        implement the :meth:`CoveragePlugin.dynamic_context` method.

        '''
        self._add_plugin(plugin, self.context_switchers)

    
    def add_noop(self = None, plugin = None):
        '''Add a plugin that does nothing.

        This is only useful for testing the plugin support.

        '''
        self._add_plugin(plugin, None)

    
    def _add_plugin(self = None, plugin = None, specialized = None):
        '''Add a plugin object.

        `plugin` is a :class:`CoveragePlugin` instance to add.  `specialized`
        is a list to append the plugin to.

        '''
        plugin_name = f'''{self.current_module}.{plugin.__class__.__name__}'''
        if self.debug and self.debug.should('plugin'):
            self.debug.write(f'''Loaded plugin {self.current_module!r}: {plugin!r}''')
            labelled = LabelledDebug(f'''plugin {self.current_module!r}''', self.debug)
            plugin = DebugPluginWrapper(plugin, labelled)
        plugin._coverage_plugin_name = plugin_name
        plugin._coverage_enabled = True
        self.order.append(plugin)
        self.names[plugin_name] = plugin
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return bool(self.order)

    
    def __iter__(self = None):
        return iter(self.order)

    
    def get(self = None, plugin_name = None):
        '''Return a plugin by name.'''
        return self.names[plugin_name]


TCoverageInit = Callable[([
    Plugins], None)]

class LabelledDebug:
    '''A Debug writer, but with labels for prepending to the messages.'''
    
    def __init__(self = None, label = None, debug = None, prev_labels = ((),)):
        self.labels = list(prev_labels) + [
            label]
        self.debug = debug

    
    def add_label(self = None, label = None):
        '''Add a label to the writer, and return a new `LabelledDebug`.'''
        return LabelledDebug(label, self.debug, self.labels)

    
    def message_prefix(self = None):
        '''The prefix to use on messages, combining the labels.'''
        prefixes = self.labels + [
            '']
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(prefixes)())

    
    def write(self = None, message = None):
        '''Write `message`, but with the labels prepended.'''
        self.debug.write(f'''{self.message_prefix()}{message}''')



class DebugPluginWrapper(CoveragePlugin):
    pass
# WARNING: Decompyle incomplete


class DebugFileTracerWrapper(FileTracer):
    '''A debugging `FileTracer`.'''
    
    def __init__(self = None, tracer = None, debug = None):
        self.tracer = tracer
        self.debug = debug

    
    def _show_frame(self = None, frame = None):
        '''A short string identifying a frame, for debug messages.'''
        filename = os.path.basename(frame.f_code.co_filename)
        return f'''{filename}@{frame.f_lineno}'''

    
    def source_filename(self = None):
        sfilename = self.tracer.source_filename()
        self.debug.write(f'''source_filename() --> {sfilename!r}''')
        return sfilename

    
    def has_dynamic_source_filename(self = None):
        has = self.tracer.has_dynamic_source_filename()
        self.debug.write(f'''has_dynamic_source_filename() --> {has!r}''')
        return has

    
    def dynamic_source_filename(self = None, filename = None, frame = None):
        dyn = self.tracer.dynamic_source_filename(filename, frame)
        self.debug.write('dynamic_source_filename({!r}, {}) --> {!r}'.format(filename, self._show_frame(frame), dyn))
        return dyn

    
    def line_number_range(self = None, frame = None):
        pair = self.tracer.line_number_range(frame)
        self.debug.write(f'''line_number_range({self._show_frame(frame)}) --> {pair!r}''')
        return pair



class DebugFileReporterWrapper(FileReporter):
    pass
# WARNING: Decompyle incomplete
