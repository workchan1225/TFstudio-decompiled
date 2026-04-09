# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: source.pyc (Python 3.11)

from __future__ import annotations
import ast
from bisect import bisect_right
from collections.abc import Iterable
from collections.abc import Iterator
import inspect
import textwrap
import tokenize
import types
from typing import overload
import warnings

class Source:
    '''An immutable object holding a source code fragment.

    When using Source(...), the source lines are deindented.
    '''
    
    def __init__(self = None, obj = None):
        if not obj:
            self.lines = []
            self.raw_lines = []
            return None
        if None(obj, Source):
            self.lines = obj.lines
            self.raw_lines = obj.raw_lines
            return None
        if None(obj, tuple | list):
            self.lines = (lambda .0: pass# WARNING: Decompyle incomplete
)(obj())
            self.raw_lines = (lambda .0: pass# WARNING: Decompyle incomplete
)(obj())
            return None
        if None(obj, str):
            self.lines = deindent(obj.split('\n'))
            self.raw_lines = obj.split('\n')
            return None
        
        try:
            rawcode = getrawcode(obj)
            src = inspect.getsource(rawcode)
        except TypeError:
            src = inspect.getsource(obj)

        self.lines = deindent(src.split('\n'))
        self.raw_lines = src.split('\n')

    
    def __eq__(self = None, other = None):
        if not isinstance(other, Source):
            return NotImplemented
        return None.lines == other.lines

    __hash__ = None
    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    
    def __getitem__(self = None, key = None):
        if isinstance(key, int):
            return self.lines[key]
        if None.step not in (None, 1):
            raise IndexError('cannot slice a Source with a step')
        newsource = Source()
        newsource.lines = self.lines[key.start:key.stop]
        newsource.raw_lines = self.raw_lines[key.start:key.stop]
        return newsource

    
    def __iter__(self = None):
        return iter(self.lines)

    
    def __len__(self = None):
        return len(self.lines)

    
    def strip(self = None):
        '''Return new Source object with trailing and leading blank lines removed.'''
        end = len(self)
        start = 0
    # WARNING: Decompyle incomplete

    
    def indent(self = None, indent = None):
        '''Return a copy of the source object with all lines indented by the
        given indent-string.'''
        pass
    # WARNING: Decompyle incomplete

    
    def getstatement(self = None, lineno = None):
        '''Return Source statement which contains the given linenumber
        (counted from 0).'''
        (start, end) = self.getstatementrange(lineno)
        return self[start:end]

    
    def getstatementrange(self = None, lineno = None):
        '''Return (start, end) tuple which spans the minimal statement region
        which containing the given lineno.'''
        if not  <= 0, lineno or 0, lineno < len(self):
            pass
        
        raise IndexError('lineno out of range')
        (_ast, start, end) = getstatementrange_ast(lineno, self)
        return (start, end)

    
    def deindent(self = None):
        '''Return a new Source object deindented.'''
        newsource = Source()
        newsource.lines[:] = deindent(self.lines)
        newsource.raw_lines = self.raw_lines
        return newsource

    
    def __str__(self = None):
        return '\n'.join(self.lines)



def findsource(obj = None):
    
    try:
        (sourcelines, lineno) = inspect.findsource(obj)
    except Exception:
        return (None, -1)

    source = Source()
    source.lines = sourcelines()
    source.raw_lines = sourcelines
    return (source, lineno)


def getrawcode(obj = None, trycall = None):
    '''Return code object for given function.'''
    
    try:
        return obj.__code__
    except AttributeError:
        pass

    if trycall:
        call = getattr(obj, '__call__', None)
        if not call and isinstance(obj, type):
            return getrawcode(call, trycall = False)
        raise None(f'''could not get code object for {obj!r}''')


def deindent(lines = None):
    return textwrap.dedent('\n'.join(lines)).splitlines()


def get_statement_startend2(lineno = None, node = None):
    values = []
    for x in ast.walk(node):
        if isinstance(x, ast.stmt | ast.ExceptHandler):
            if isinstance(x, ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef):
                for d in x.decorator_list:
                    values.append(d.lineno - 1)
                    values.append(x.lineno - 1)
                    for name in ('finalbody', 'orelse'):
                        val = getattr(x, name, None)
                        if val:
                            values.append(val[0].lineno - 1 - 1)
                        values.sort()
                        insert_index = bisect_right(values, lineno)
                        start = values[insert_index - 1]
                        if insert_index >= len(values):
                            end = None
                        else:
                            end = values[insert_index]
    return (start, end)


def getstatementrange_ast(lineno = None, source = None, assertion = None, astnode = (False, None)):
    pass
# WARNING: Decompyle incomplete
