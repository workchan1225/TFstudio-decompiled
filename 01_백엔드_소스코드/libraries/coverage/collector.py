# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: collector.pyc (Python 3.11)

'''Raw data collector for coverage.py.'''
from __future__ import annotations
import contextlib
import functools
import os
import sys
from collections.abc import Mapping
from types import FrameType
from typing import Any, Callable, TypeVar, cast
from coverage import env
from coverage.core import Core
from coverage.data import CoverageData
from coverage.debug import short_stack
from coverage.exceptions import ConfigError
from coverage.misc import human_sorted_items, isolate_module
from coverage.plugin import CoveragePlugin
from coverage.types import TArc, TCheckIncludeFn, TFileDisposition, Tracer, TShouldStartContextFn, TShouldTraceFn, TTraceData, TTraceFn, TWarnFn
os = isolate_module(os)
T = TypeVar('T')

class Collector:
    '''Collects trace data.

    Creates a Tracer object for each thread, since they track stack
    information.  Each Tracer points to the same shared data, contributing
    traced data points.

    When the Collector is started, it creates a Tracer for the current thread,
    and installs a function to create Tracers for each new thread started.
    When the Collector is stopped, all active Tracers are stopped.

    Threads started while the Collector is stopped will never have Tracers
    associated with them.

    '''
    _collectors: 'list[Collector]' = []
    
    def __init__(self, core, should_trace, check_include, should_start_context, file_mapper = None, branch = None, warn = None, concurrency = ('core', 'Core', 'should_trace', 'TShouldTraceFn', 'check_include', 'TCheckIncludeFn', 'should_start_context', 'TShouldStartContextFn | None', 'file_mapper', 'Callable[[str], str]', 'branch', 'bool', 'warn', 'TWarnFn', 'concurrency', 'list[str]', 'return', 'None')):
        '''Create a collector.

        `should_trace` is a function, taking a file name and a frame, and
        returning a `coverage.FileDisposition object`.

        `check_include` is a function taking a file name and a frame. It returns
        a boolean: True if the file should be traced, False if not.

        `should_start_context` is a function taking a frame, and returning a
        string. If the frame should be the start of a new context, the string
        is the new context. If the frame should not be the start of a new
        context, return None.

        `file_mapper` is a function taking a filename, and returning a Unicode
        filename.  The result is the name that will be recorded in the data
        file.

        If `branch` is true, then branches will be measured.  This involves
        collecting data on which statements followed each other (arcs).  Use
        `get_arc_data` to get the arc data.

        `warn` is a warning function, taking a single string message argument
        and an optional slug argument which will be a string or None, to be
        used if a warning needs to be issued.

        `concurrency` is a list of strings indicating the concurrency libraries
        in use.  Valid values are "greenlet", "eventlet", "gevent", or "thread"
        (the default).  "thread" can be combined with one of the other three.
        Other values are ignored.

        '''
        self.core = core
        self.should_trace = should_trace
        self.check_include = check_include
        self.should_start_context = should_start_context
        self.file_mapper = file_mapper
        self.branch = branch
        self.warn = warn
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<Collector at {id(self):#x}: {self.tracer_name()}>'''

    
    def use_data(self = None, covdata = None, context = None):
        '''Use `covdata` for recording data.'''
        self.covdata = covdata
        self.static_context = context
        self.covdata.set_context(self.static_context)

    
    def tracer_name(self = None):
        """Return the class name of the tracer we're using."""
        return self.core.tracer_class.__name__

    
    def _clear_data(self = None):
        '''Clear out existing data, but stay ready for more collection.'''
        if not self.data_lock:
            pass
        contextlib.nullcontext()
        for d in self.data.values():
            d.clear()
            None(None, None)
        with None:
            if not None:
                pass
        for tracer in self.tracers:
            tracer.reset_activity()
            return None

    
    def reset(self = None):
        '''Clear collected data, and prepare to collect more.'''
        self.data_lock = self.threading.Lock() if self.threading else None
        self.data = { }
        self.file_tracers = { }
        self.disabled_plugins = set()
        if env.PYPY:
            import __pypy__
            self.should_trace_cache = __pypy__.newdict('module')
        else:
            self.should_trace_cache = { }
        self.tracers = []
        self._clear_data()

    
    def lock_data(self = None):
        '''Lock self.data_lock, for use by the C tracer.'''
        pass
    # WARNING: Decompyle incomplete

    
    def unlock_data(self = None):
        '''Unlock self.data_lock, for use by the C tracer.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _start_tracer(self = None):
        '''Start a new Tracer object, and store it in self.tracers.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _installation_trace(self = None, frame = None, event = None, arg = ('frame', 'FrameType', 'event', 'str', 'arg', 'Any', 'return', 'TTraceFn | None')):
        '''Called on new threads, installs the real tracer.'''
        sys.settrace(None)
        fn = self._start_tracer()
        if fn:
            fn = fn(frame, event, arg)
        return fn

    
    def start(self = None):
        '''Start collecting trace information.'''
        keep_collectors = []
        for c in self._collectors:
            if c.pid == self.pid:
                keep_collectors.append(c)
                continue
            c.post_fork()
            self._collectors[:] = keep_collectors
            if self._collectors:
                self._collectors[-1].pause()
        self.tracers = []
        
        try:
            self._start_tracer()
        except:
            if self._collectors:
                self._collectors[-1].resume()
            raise 

        self._collectors.append(self)
        if self.core.systrace or self.threading:
            self.threading.settrace(self._installation_trace)
            return None
        return None

    
    def stop(self = None):
        '''Stop collecting trace information.'''
        pass
    # WARNING: Decompyle incomplete

    
    def pause(self = None):
        '''Pause tracing, but be prepared to `resume`.'''
        for tracer in self.tracers:
            tracer.stop()
            stats = tracer.get_stats()
            if stats:
                print(f'''\nCoverage.py {tracer.__class__.__name__} stats:''')
                for k, v in human_sorted_items(stats.items()):
                    print(f'''{k:>20}: {v}''')
                    if self.threading:
                        self.threading.settrace(None)
                        return None
                    return None

    
    def resume(self = None):
        '''Resume tracing after a `pause`.'''
        for tracer in self.tracers:
            tracer.start()
            if self.core.systrace:
                if self.threading:
                    self.threading.settrace(self._installation_trace)
                    return None
                None._start_tracer()
                return None
            return None

    
    def post_fork(self = None):
        '''After a fork, tracers might need to adjust.'''
        for tracer in self.tracers:
            if hasattr(tracer, 'post_fork'):
                tracer.post_fork()
            return None

    
    def _activity(self = None):
        '''Has any activity been traced?

        Returns a boolean, True if any trace function was invoked.

        '''
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.tracers())

    
    def switch_context(self = None, new_context = None):
        '''Switch to a new dynamic context.'''
        self.flush_data()
        if self.static_context:
            context = self.static_context
            if new_context:
                context += '|' + new_context
            else:
                context = new_context
        self.covdata.set_context(context)

    
    def disable_plugin(self = None, disposition = None):
        '''Disable the plugin mentioned in `disposition`.'''
        file_tracer = disposition.file_tracer
    # WARNING: Decompyle incomplete

    cached_mapped_file = (lambda self = None, filename = None: self.file_mapper(filename))()
    
    def mapped_file_dict(self = None, d = None):
        '''Return a dict like d, but with keys modified by file_mapper.'''
        pass
    # WARNING: Decompyle incomplete

    
    def plugin_was_disabled(self = None, plugin = None):
        '''Record that `plugin` was disabled during the run.'''
        self.disabled_plugins.add(plugin._coverage_plugin_name)

    
    def flush_data(self = None):
        '''Save the collected data to our associated `CoverageData`.

        Data may have also been saved along the way. This forces the
        last of the data to be saved.

        Returns True if there was data to save, False if not.
        '''
        pass
    # WARNING: Decompyle incomplete
