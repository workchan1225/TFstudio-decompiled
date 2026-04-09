# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: console.pyc (Python 3.11)

from __future__ import annotations
import code
import sys
import typing as t
from contextvars import ContextVar
from types import CodeType
from markupsafe import escape
from repr import debug_repr
from repr import dump
from repr import helper
_stream: 'ContextVar[HTMLStringO]' = ContextVar('werkzeug.debug.console.stream')
_ipy: 'ContextVar[_InteractiveConsole]' = ContextVar('werkzeug.debug.console.ipy')

class HTMLStringO:
    '''A StringO version that HTML escapes on write.'''
    
    def __init__(self = None):
        self._buffer = []

    
    def isatty(self = None):
        return False

    
    def close(self = None):
        pass

    
    def flush(self = None):
        pass

    
    def seek(self = None, n = None, mode = None):
        pass

    
    def readline(self = None):
        if len(self._buffer) == 0:
            return ''
        ret = None._buffer[0]
        del self._buffer[0]
        return ret

    
    def reset(self = None):
        val = ''.join(self._buffer)
        del self._buffer[:]
        return val

    
    def _write(self = None, x = None):
        self._buffer.append(x)

    
    def write(self = None, x = None):
        self._write(escape(x))

    
    def writelines(self = None, x = None):
        self._write(escape(''.join(x)))



class ThreadedStream:
    '''Thread-local wrapper for sys.stdout for the interactive console.'''
    push = (lambda : if not isinstance(sys.stdout, ThreadedStream):
sys.stdout = t.cast(t.TextIO, ThreadedStream())_stream.set(HTMLStringO()))()
    fetch = (lambda : try:
stream = _stream.get()except LookupError:
''stream.reset())()
    displayhook = (lambda obj = None: try:
stream = _stream.get()except LookupError:
# WARNING: Decompyle incomplete
)()
    
    def __setattr__(self = None, name = None, value = None):
        raise AttributeError(f'''read only attribute {name}''')

    
    def __dir__(self = None):
        return dir(sys.__stdout__)

    
    def __getattribute__(self = None, name = None):
        
        try:
            stream = _stream.get()
        except LookupError:
            stream = sys.__stdout__

        return getattr(stream, name)

    
    def __repr__(self = None):
        return repr(sys.__stdout__)


_displayhook = sys.displayhook
sys.displayhook = ThreadedStream.displayhook

class _ConsoleLoader:
    
    def __init__(self = None):
        self._storage = { }

    
    def register(self = None, code = None, source = None):
        self._storage[id(code)] = source
        for var in code.co_consts:
            if isinstance(var, CodeType):
                self._storage[id(var)] = source
            return None

    
    def get_source_by_code(self = None, code = None):
        
        try:
            return self._storage[id(code)]
        except KeyError:
            return None




class _InteractiveConsole(code.InteractiveInterpreter):
    pass
# WARNING: Decompyle incomplete


class Console:
    '''An interactive console.'''
    
    def __init__(self = None, globals = None, locals = None):
        pass
    # WARNING: Decompyle incomplete

    
    def eval(self = None, code = None):
        _ipy.set(self._ipy)
        old_sys_stdout = sys.stdout
        
        try:
            sys.stdout = old_sys_stdout
            return self._ipy.runsource(code)
        except:
            sys.stdout = old_sys_stdout
