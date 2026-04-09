# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debug.pyc (Python 3.11)

'''Control of and utilities for debugging.'''
from __future__ import annotations
import _thread
import atexit
import contextlib
import datetime
import functools
import inspect
import itertools
import os
import pprint
import re
import reprlib
import sys
import traceback
import types
from collections.abc import Iterable, Iterator, Mapping
from typing import IO, Any, Callable, Final, overload
from coverage.misc import human_sorted_items, isolate_module
from coverage.types import AnyCallable, TWritable
os = isolate_module(os)
FORCED_DEBUG: 'list[str]' = []
FORCED_DEBUG_FILE = None

class DebugControl:
    '''Control and output for debugging.'''
    show_repr_attr = False
    
    def __init__(self = None, options = None, output = None, file_name = (None,)):
        '''Configure the options and output file for debugging.'''
        self.options = list(options) + FORCED_DEBUG
        self.suppress_callers = False
        filters = []
        if self.should('process'):
            filters.append(CwdTracker().filter)
            filters.append(ProcessTracker().filter)
        if self.should('pytest'):
            filters.append(PytestTracker().filter)
        if self.should('pid'):
            filters.append(add_pid_and_tid)
        self.output = DebugOutputFile.get_one(output, file_name = file_name, filters = filters)
        self.raw_output = self.output.outfile

    
    def __repr__(self = None):
        return f'''<DebugControl options={self.options!r} raw_output={self.raw_output!r}>'''

    
    def should(self = None, option = None):
        '''Decide whether to output debug information in category `option`.'''
        if option == 'callers' and self.suppress_callers:
            return False
        return None in self.options

    without_callers = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def write(self = None, msg = None, *, exc):
        '''Write a line of debug output.

        `msg` is the line to write. A newline will be appended.

        If `exc` is provided, a stack trace of the exception will be written
        after the message.

        '''
        self.output.write(msg + '\n')
    # WARNING: Decompyle incomplete



class NoDebugging(DebugControl):
    '''A replacement for DebugControl that will never try to do anything.'''
    
    def __init__(self = None):
        pass

    
    def should(self = None, option = None):
        '''Should we write debug messages?  Never.'''
        return False

    without_callers = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def write(self = None, msg = None, *, exc):
        '''This will never be called.'''
        raise AssertionError('NoDebugging.write should never be called.')



class DevNullDebug(NoDebugging):
    """A DebugControl that won't write anywhere."""
    
    def write(self = None, msg = None, *, exc):
        pass



def info_header(label = None):
    '''Make a nice header string.'''
    return '--{:-<60s}'.format(' ' + label + ' ')


def info_formatter(info = None):
    '''Produce a sequence of formatted lines from info.

    `info` is a sequence of pairs (label, data).  The produced lines are
    nicely formatted, ready to print.

    '''
    pass
# WARNING: Decompyle incomplete


def write_formatted_info(write = None, header = None, info = None):
    '''Write a sequence of (label,data) pairs nicely.

    `write` is a function write(str) that accepts each line of output.
    `header` is a string to start the section.  `info` is a sequence of
    (label, data) pairs, where label is a str, and data can be a single
    value, or a list/set/tuple.

    '''
    write(info_header(header))
    for line in info_formatter(info):
        write(f''' {line}''')
        return None


def exc_one_line(exc = None):
    '''Get a one-line summary of an exception, including class name and message.'''
    lines = traceback.format_exception_only(type(exc), exc)
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(lines())

_FILENAME_REGEXES: 'list[tuple[str, str]]' = [
    ('.*[/\\\\]pytest-of-.*[/\\\\]pytest-\\d+([/\\\\]popen-gw\\d+)?', 'tmp:')]
_FILENAME_SUBS: 'list[tuple[str, str]]' = []
short_filename = (lambda filename = None: pass)()
short_filename = (lambda filename = None: pass)()

def short_filename(filename = None):
    """Shorten a file name. Directories are replaced by prefixes like 'syspath:'"""
    pass
# WARNING: Decompyle incomplete


def file_summary(filename = None):
    '''A one-line summary of a file, for log messages.'''
    
    try:
        s = os.stat(filename)
        mod = datetime.datetime.fromtimestamp(s.st_mtime)
        summary = f'''{s.st_size} bytes, modified {mod}'''
    except FileNotFoundError:
        summary = 'does not exist'
    except Exception:
        e = None
        summary = f'''error: {e}'''
        e = None
        del e
    except:
        e = None
        del e

    return summary


def short_stack(skip = None, full = None, frame_ids = None, short_filenames = (0, False, False, False)):
    '''Return a string summarizing the call stack.

    The string is multi-line, with one line per stack frame. Each line shows
    the function name, the file name, and the line number:

        ...
        start_import_stop : /Users/ned/coverage/trunk/tests/coveragetest.py:95
        import_local_file : /Users/ned/coverage/trunk/tests/coveragetest.py:81
        import_local_file : /Users/ned/coverage/trunk/coverage/backward.py:159
        ...

    `skip` is the number of closest immediate frames to skip, so that debugging
    functions can call this and not be included in the result.

    If `full` is true, then include all frames.  Otherwise, initial "boring"
    frames (ones in site-packages and earlier) are omitted.

    `short_filenames` will shorten filenames using `short_filename`, to reduce
    the amount of repetitive noise in stack traces.

    '''
    BORING_PRELUDE = [
        '<string>',
        '\\bigor.py$',
        '\\bsite-packages\\b']
    stack = inspect.stack()[:skip:-1]
    if not full:
        for pat in BORING_PRELUDE:
            stack = itertools.dropwhile((lambda fi, pat = (pat,): re.search(pat, fi.filename)), stack)
            lines = []
            for frame_info in stack:
                line = f'''{frame_info.function:>30s} : '''
                if frame_ids:
                    line += f'''{id(frame_info.frame):#x} '''
                filename = frame_info.filename
                if short_filenames:
                    filename = short_filename(filename)
                line += f'''{filename}:{frame_info.lineno}'''
                lines.append(line)
                return '\n'.join(lines)


def dump_stack_frames(out = None, skip = None):
    '''Print a summary of the stack to `out`.'''
    out.write(short_stack(skip = skip + 1) + '\n')


def clipped_repr(text = None, numchars = None):
    '''`repr(text)`, but limited to `numchars`.'''
    r = reprlib.Repr()
    r.maxstring = numchars
    return r.repr(text)


def short_id(id64 = None):
    '''Given a 64-bit id, make a shorter 16-bit one.'''
    id16 = 0
    for offset in range(0, 64, 16):
        id16 ^= id64 >> offset
        return id16 & 65535


def add_pid_and_tid(text = None):
    '''A filter to add pid and tid to debug messages.'''
    tid = f'''{short_id(_thread.get_ident()):04x}'''
    text = f'''{os.getpid():5d}.{tid}: {text}'''
    return text

AUTO_REPR_IGNORE = {
    '$coverage.object_id'}

def auto_repr(self = None):
    '''A function implementing an automatic __repr__ for debugging.'''
    show_attrs = self.__dict__.items()()
    return self.__class__.__name__(klass = id(self), id = ''.join, attrs = (lambda .0: pass# WARNING: Decompyle incomplete
)(show_attrs()))


def simplify(v = None):
    '''Turn things which are nearly dict/list/etc into dict/list/etc.'''
    if isinstance(v, dict):
        return v.items()()
    if None(v, (list, tuple)):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(v())
    if None(v, '__dict__'):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(v.__dict__.items()())


def ppformat(v = None):
    '''Debug helper to pretty-print data, including SimpleNamespace objects.'''
    return pprint.pformat(simplify(v), indent = 4, compact = True, sort_dicts = True, width = 140)


def pp(v = None):
    '''Debug helper to pretty-print data, including SimpleNamespace objects.'''
    print(ppformat(v))


def filter_text(text = None, filters = None):
    '''Run `text` through a series of filters.

    `filters` is a list of functions. Each takes a string and returns a
    string.  Each is run in turn. After each filter, the text is split into
    lines, and each line is passed through the next filter.

    Returns: the final string that results after all of the filters have
    run.

    '''
    clean_text = text.rstrip()
    ending = text[len(clean_text):]
    text = clean_text
    for filter_fn in filters:
        lines = []
        for line in text.splitlines():
            lines.extend(filter_fn(line).splitlines())
            text = '\n'.join(lines)
            return text + ending


class CwdTracker:
    '''A class to add cwd info to debug messages.'''
    
    def __init__(self = None):
        self.cwd = None

    
    def filter(self = None, text = None):
        '''Add a cwd message for each new cwd.'''
        cwd = os.getcwd()
        if cwd != self.cwd:
            text = f'''cwd is now {cwd!r}\n{text}'''
            self.cwd = cwd
        return text



class ProcessTracker:
    '''Track process creation for debug logging.'''
    
    def __init__(self = None):
        self.pid = os.getpid()
        self.did_welcome = False

    
    def filter(self = None, text = None):
        '''Add a message about how new processes came to be.'''
        welcome = ''
        pid = os.getpid()
        if self.pid != pid:
            welcome = f'''New process: forked {self.pid} -> {pid}\n'''
            self.pid = pid
        elif not self.did_welcome:
            argv = getattr(sys, 'argv', None)
            welcome = f'''New process: pid={pid!r}, executable: {sys.executable!r}\n''' + f'''New process: cmd: {argv!r}\n''' + f'''New process parent pid: {os.getppid()!r}\n'''
        if welcome:
            self.did_welcome = True
            return welcome + text



class PytestTracker:
    '''Track the current pytest test name to add to debug messages.'''
    
    def __init__(self = None):
        self.test_name = None

    
    def filter(self = None, text = None):
        '''Add a message when the pytest test changes.'''
        test_name = os.getenv('PYTEST_CURRENT_TEST')
        if test_name != self.test_name:
            text = f'''Pytest context: {test_name}\n{text}'''
            self.test_name = test_name
        return text



class DebugOutputFile:
    '''A file-like object that includes pid and cwd information.'''
    
    def __init__(self = None, outfile = None, filters = None):
        self.outfile = outfile
        self.filters = list(filters)
        self.pid = os.getpid()

    get_one = (lambda cls = None, fileobj = None, file_name = classmethod, filters = (None, None, (), False), interim = ('fileobj', 'IO[str] | None', 'file_name', 'str | None', 'filters', 'Iterable[Callable[[str], str]]', 'interim', 'bool', 'return', 'DebugOutputFile'): pass# WARNING: Decompyle incomplete
)()
    SYS_MOD_NAME: 'Final[str]' = '$coverage.debug.DebugOutputFile.the_one'
    SINGLETON_ATTR: 'Final[str]' = 'the_one_and_is_interim'
    _set_singleton_data = (lambda cls = None, the_one = None, interim = classmethod: singleton_module = types.ModuleType(cls.SYS_MOD_NAME)setattr(singleton_module, cls.SINGLETON_ATTR, (the_one, interim))sys.modules[cls.SYS_MOD_NAME] = singleton_module)()
    _get_singleton_data = (lambda cls = None: singleton_module = sys.modules.get(cls.SYS_MOD_NAME)getattr(singleton_module, cls.SINGLETON_ATTR, (None, True)))()
    _del_singleton_data = (lambda cls = None: if cls.SYS_MOD_NAME in sys.modules:
del sys.modules[cls.SYS_MOD_NAME]None)()
    
    def write(self = None, text = None):
        '''Just like file.write, but filter through all our filters.'''
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self = None):
        '''Flush our file.'''
        pass
    # WARNING: Decompyle incomplete



def log(msg = None, stack = None):
    '''Write a log message as forcefully as possible.'''
    out = DebugOutputFile.get_one(interim = True)
    out.write(msg + '\n')
    if stack:
        dump_stack_frames(out = out, skip = 1)
        return None


def decorate_methods(decorator = None, butnot = None, private = None):
    '''A class decorator to apply a decorator to methods.'''
    pass
# WARNING: Decompyle incomplete


def break_in_pudb(func = None):
    '''A function decorator to stop in the debugger for each call.'''
    pass
# WARNING: Decompyle incomplete

OBJ_IDS = itertools.count()
CALLS = itertools.count()
OBJ_ID_ATTR = '$coverage.object_id'

def show_calls(show_args = None, show_stack = None, show_return = None):
    '''A method decorator to debug-log each call to the function.'''
    pass
# WARNING: Decompyle incomplete


def relevant_environment_display(env = None):
    '''Filter environment variables for a debug display.

    Select variables to display (with COV or PY in the name, or HOME, TEMP, or
    TMP), and also cloak sensitive values with asterisks.

    Arguments:
        env: a dict of environment variable names and values.

    Returns:
        A list of pairs (name, value) to show.

    '''
    pass
# WARNING: Decompyle incomplete
