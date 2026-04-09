# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Types for use throughout coverage.py.
'''
from __future__ import annotations
import os
import pathlib
from collections.abc import Iterable, Mapping
from types import FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Callable, Optional, Protocol
if TYPE_CHECKING:
    from coverage.plugin import FileTracer
AnyCallable = Callable[(..., Any)]
FilePath = str | os.PathLike[str]
FilePathClasses = [
    str,
    pathlib.Path]
FilePathType = type[str] | type[pathlib.Path]

class TTraceFn(Protocol):
    '''A Python trace function.'''
    
    def __call__(self = None, frame = None, event = None, arg = (None,), lineno = ('frame', 'FrameType', 'event', 'str', 'arg', 'Any', 'lineno', 'TLineNo | None', 'return', 'TTraceFn | None')):
        pass


TLineNo = int
TOffset = int
TArc = tuple[(TLineNo, TLineNo)]

class TFileDisposition(Protocol):
    has_dynamic_filename: 'bool' = 'A simple value type for recording what to do with a file.'

TTraceFileData = set[TLineNo] | set[TArc] | set[int]
TTraceData = dict[(str, TTraceFileData)]
TShouldTraceFn = Callable[([
    str,
    FrameType], TFileDisposition)]
TCheckIncludeFn = Callable[([
    str,
    FrameType], bool)]
TShouldStartContextFn = Callable[([
    FrameType], str | None)]

class Tracer(Protocol):
    warn: 'TWarnFn' = 'Anything that can report on Python execution.'
    
    def __init__(self = None):
        pass

    
    def start(self = None):
        '''Start this tracer, return a trace function if based on sys.settrace.'''
        pass

    
    def stop(self = None):
        '''Stop this tracer.'''
        pass

    
    def activity(self = None):
        '''Has there been any activity?'''
        pass

    
    def reset_activity(self = None):
        '''Reset the activity() flag.'''
        pass

    
    def get_stats(self = None):
        '''Return a dictionary of statistics, or None.'''
        pass


TCovKwargs = Any
TConfigValueIn = Optional[bool | int | float | str | Iterable[str] | Mapping[(str, Iterable[str])]]
TConfigValueOut = Optional[bool | int | float | str | list[str] | dict[(str, list[str])]]
TConfigSectionIn = Mapping[(str, TConfigValueIn)]
TConfigSectionOut = Mapping[(str, TConfigValueOut)]

class TConfigurable(Protocol):
    '''Something that can proxy to the coverage configuration settings.'''
    
    def get_option(self = None, option_name = None):
        '''Get an option from the configuration.

        `option_name` is a colon-separated string indicating the section and
        option name.  For example, the ``branch`` option in the ``[run]``
        section of the config file would be indicated with `"run:branch"`.

        Returns the value of the option.

        '''
        pass

    
    def set_option(self = None, option_name = None, value = None):
        '''Set an option in the configuration.

        `option_name` is a colon-separated string indicating the section and
        option name.  For example, the ``branch`` option in the ``[run]``
        section of the config file would be indicated with `"run:branch"`.

        `value` is the new value for the option.

        '''
        pass



class TPluginConfig(Protocol):
    '''Something that can provide options to a plugin.'''
    
    def get_plugin_options(self = None, plugin = None):
        '''Get the options for a plugin.'''
        pass


TMorf = ModuleType | str
TSourceTokenLines = Iterable[list[tuple[(str, str)]]]

class TPlugin(Protocol):
    _coverage_enabled: 'bool' = 'What all plugins have in common.'


class TWarnFn(Protocol):
    '''A callable warn() function.'''
    
    def __call__(self = None, msg = None, slug = None, once = (None, False)):
        pass



class TDebugCtl(Protocol):
    '''A DebugControl object, or something like it.'''
    
    def should(self = None, option = None):
        '''Decide whether to output debug information in category `option`.'''
        pass

    
    def write(self = None, msg = None):
        '''Write a line of debug output.'''
        pass



class TWritable(Protocol):
    '''Anything that can be written to.'''
    
    def write(self = None, msg = None):
        '''Write a message.'''
        pass
