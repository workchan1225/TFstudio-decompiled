# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pprint.pyc (Python 3.11)

"""Support to pretty-print lists, tuples, & dictionaries recursively.

Very simple, but useful, especially in debugging data structures.

Classes
-------

PrettyPrinter()
    Handle pretty-printing operations onto a stream using a configured
    set of formatting parameters.

Functions
---------

pformat()
    Format a Python object into a pretty-printed representation.

pprint()
    Pretty-print a Python object to a stream [default is sys.stdout].

saferepr()
    Generate a 'standard' repr()-like value, but protect against recursive
    data structures.

"""
import collections as _collections
import dataclasses as _dataclasses
import re
import sys as _sys
import types as _types
from io import StringIO as _StringIO
__all__ = [
    'pprint',
    'pformat',
    'isreadable',
    'isrecursive',
    'saferepr',
    'PrettyPrinter',
    'pp']

def pprint(object, stream, indent = None, width = (None, 1, 80, None), depth = {
    'compact': False,
    'sort_dicts': True,
    'underscore_numbers': False }, *, compact, sort_dicts, underscore_numbers):
    '''Pretty-print a Python object to a stream [default is sys.stdout].'''
    printer = PrettyPrinter(stream = stream, indent = indent, width = width, depth = depth, compact = compact, sort_dicts = sort_dicts, underscore_numbers = underscore_numbers)
    printer.pprint(object)


def pformat(object, indent = None, width = (1, 80, None), depth = {
    'compact': False,
    'sort_dicts': True,
    'underscore_numbers': False }, *, compact, sort_dicts, underscore_numbers):
    '''Format a Python object into a pretty-printed representation.'''
    return PrettyPrinter(indent = indent, width = width, depth = depth, compact = compact, sort_dicts = sort_dicts, underscore_numbers = underscore_numbers).pformat(object)


def pp(object = None, *, sort_dicts, *args, **kwargs):
    '''Pretty-print a Python object'''
    pass
# WARNING: Decompyle incomplete


def saferepr(object):
    '''Version of repr() which can handle recursive data structures.'''
    return PrettyPrinter()._safe_repr(object, { }, None, 0)[0]


def isreadable(object):
    '''Determine if saferepr(object) is readable by eval().'''
    return PrettyPrinter()._safe_repr(object, { }, None, 0)[1]


def isrecursive(object):
    '''Determine if object requires a recursive representation.'''
    return PrettyPrinter()._safe_repr(object, { }, None, 0)[2]


class _safe_key:
    '''Helper function for key functions when sorting unorderable objects.

    The wrapped-object will fallback to a Py2.x style comparison for
    unorderable types (sorting first comparing the type name and then by
    the obj ids).  Does not work recursively, so dict.items() must have
    _safe_key applied to both the key and the value.

    '''
    __slots__ = [
        'obj']
    
    def __init__(self, obj):
        self.obj = obj

    
    def __lt__(self, other):
        
        try:
            return self.obj < other.obj
        except TypeError:
            return 




def _safe_tuple(t):
    '''Helper function for comparing 2-tuples'''
    return (_safe_key(t[0]), _safe_key(t[1]))


class PrettyPrinter:
    
    def __init__(self, indent, width = None, depth = (1, 80, None, None), stream = {
        'compact': False,
        'sort_dicts': True,
        'underscore_numbers': False }, *, compact, sort_dicts, underscore_numbers):
        '''Handle pretty printing operations onto a stream using a set of
        configured parameters.

        indent
            Number of spaces to indent for each level of nesting.

        width
            Attempted maximum number of columns in the output.

        depth
            The maximum depth to print out nested structures.

        stream
            The desired output stream.  If omitted (or false), the standard
            output stream available at construction will be used.

        compact
            If true, several items will be combined in one line.

        sort_dicts
            If true, dict keys are sorted.

        underscore_numbers
            If true, digit groups are separated with underscores.

        '''
        indent = int(indent)
        width = int(width)
        if indent < 0:
            raise ValueError('indent must be >= 0')
    # WARNING: Decompyle incomplete

    
    def pprint(self, object):
        pass
    # WARNING: Decompyle incomplete

    
    def pformat(self, object):
        sio = _StringIO()
        self._format(object, sio, 0, 0, { }, 0)
        return sio.getvalue()

    
    def isrecursive(self, object):
        return self.format(object, { }, 0, 0)[2]

    
    def isreadable(self, object):
