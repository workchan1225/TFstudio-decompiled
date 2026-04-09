# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: docscrape.pyc (Python 3.11)

'''Extract reference documentation from the NumPy source tree.'''
import copy
import inspect
import pydoc
import re
import sys
import textwrap
from collections import namedtuple
from collections.abc import Callable, Mapping
from functools import cached_property
from warnings import warn

def strip_blank_lines(l):
    '''Remove leading and trailing blank lines from a list of lines'''
    pass
# WARNING: Decompyle incomplete


class Reader:
    '''A line-based string reader.'''
    
    def __init__(self, data):
        """
        Parameters
        ----------
        data : str
           String with lines separated by '\\n'.

        """
        if isinstance(data, list):
            self._str = data
        else:
            self._str = data.split('\n')
        self.reset()

    
    def __getitem__(self, n):
        return self._str[n]

    
    def reset(self):
        self._l = 0

    
    def read(self):
        if not self.eof():
            out = self[self._l]
            return out

    
    def seek_next_non_empty_line(self):
        for l in self[self._l:]:
            if l.strip():
                return None
            return None

    
    def eof(self):
        return self._l >= len(self._str)

    
    def read_to_condition(self, condition_func):
        start = self._l
        for line in self[start:]:
            if condition_func(line):
                
                return None, self[start:self._l]
            if self.eof():
                
                return None, None._l += 1, ._l, self[start:self._l + 1]
            return []

    
    def read_to_next_empty_line(self):
        self.seek_next_non_empty_line()
        
        def is_empty(line):
            return not line.strip()

        return self.read_to_condition(is_empty)

    
    def read_to_next_unindented_line(self):
        
        def is_unindented(line):
            if line.strip():
                pass
            return len(line.lstrip()) == len(line)

        return self.read_to_condition(is_unindented)

    
    def peek(self, n = (0,)):
        if self._l + n < len(self._str):
            return self[self._l + n]

    
    def is_empty(self):
        return not ''.join(self._str).strip()



class ParseError(Exception):
    
    def __str__(self):
        message = self.args[0]
        if hasattr(self, 'docstring'):
            message = f'''{message} in {self.docstring!r}'''
        return message


Parameter = namedtuple('Parameter', [
    'name',
    'type',
    'desc'])

class NumpyDocString(Mapping):
    __module__ = __name__
    __qualname__ = 'NumpyDocString'
    __doc__ = 'Parses a numpydoc string to an abstract representation\n\n    Instances define a mapping from section title to structured data.\n\n    '
# WARNING: Decompyle incomplete


def dedent_lines(lines):
    '''Deindent a list of lines maximally'''
    return textwrap.dedent('\n'.join(lines)).split('\n')


class FunctionDoc(NumpyDocString):
    pass
# WARNING: Decompyle incomplete


class ObjDoc(NumpyDocString):
    
    def __init__(self, obj, doc, config = (None, None)):
        self._f = obj
    # WARNING: Decompyle incomplete



class ClassDoc(NumpyDocString):
    extra_public_methods = [
        '__call__']
    
    def __init__(self, cls, doc, modulename, func_doc, config = (None, '', FunctionDoc, None)):
        pass
    # WARNING: Decompyle incomplete

    methods = (lambda self: pass# WARNING: Decompyle incomplete
)()
    properties = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _should_skip_member = (lambda name, klass:
