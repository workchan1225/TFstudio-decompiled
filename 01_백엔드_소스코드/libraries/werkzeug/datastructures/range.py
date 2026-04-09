# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: range.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import typing as t
from datetime import datetime
if t.TYPE_CHECKING:
    import typing_extensions as te
T = t.TypeVar('T')

class IfRange:
    '''Very simple object that represents the `If-Range` header in parsed
    form.  It will either have neither a etag or date or one of either but
    never both.

    .. versionadded:: 0.7
    '''
    
    def __init__(self = None, etag = None, date = None):
        self.etag = etag
        self.date = date

    
    def to_header(self = None):
        '''Converts the object back into an HTTP header.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return self.to_header()

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {str(self)!r}>'''



class Range:
    '''Represents a ``Range`` header. All methods only support only
    bytes as the unit. Stores a list of ranges if given, but the methods
    only work if only one range is provided.

    :raise ValueError: If the ranges provided are invalid.

    .. versionchanged:: 0.15
        The ranges passed in are validated.

    .. versionadded:: 0.7
    '''
    
    def __init__(self = None, units = None, ranges = None):
        self.units = units
        self.ranges = ranges
    # WARNING: Decompyle incomplete

    
    def range_for_length(self = None, length = None):
        '''If the range is for bytes, the length is not None and there is
        exactly one range and it is satisfiable it returns a ``(start, stop)``
        tuple, otherwise `None`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def make_content_range(self = None, length = None):
        '''Creates a :class:`~werkzeug.datastructures.ContentRange` object
        from the current range and given content length.
        '''
        rng = self.range_for_length(length)
    # WARNING: Decompyle incomplete

    
    def to_header(self = None):
        '''Converts the object back into an HTTP header.'''
        ranges = []
    # WARNING: Decompyle incomplete

    
    def to_content_range_header(self = None, length = None):
        '''Converts the object into `Content-Range` HTTP header,
        based on given length
        '''
        range = self.range_for_length(length)
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return self.to_header()

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {str(self)!r}>'''



def _CallbackProperty():
    '''_CallbackProperty'''
    
    def __set_name__(self = None, owner = None, name = None):
        self.attr = f'''_{name}'''

    __get__ = (lambda self = None, instance = None, owner = t.overload: pass)()
    __get__ = (lambda self = None, instance = None, owner = t.overload: pass)()
    
    def __get__(self = None, instance = None, owner = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, instance = None, value = None):
        instance.__dict__[self.attr] = value
    # WARNING: Decompyle incomplete


_CallbackProperty = <NODE:27>(_CallbackProperty, '_CallbackProperty', t.Generic[T])

class ContentRange:
    '''Represents the content range header.

    .. versionadded:: 0.7
    '''
    
    def __init__(self, units = None, start = None, stop = None, length = (None, None), on_update = ('units', 'str | None', 'start', 'int | None', 'stop', 'int | None', 'length', 'int | None', 'on_update', 'cabc.Callable[[ContentRange], None] | None', 'return', 'None')):
        self.on_update = on_update
        self.set(start, stop, length, units)

    units: 'str | None' = _CallbackProperty()
    start: 'int | None' = _CallbackProperty()
    stop: 'int | None' = _CallbackProperty()
    length: 'int | None' = _CallbackProperty()
    
    def set(self = None, start = None, stop = None, length = (None, 'bytes'), units = ('start', 'int | None', 'stop', 'int | None', 'length', 'int | None', 'units', 'str | None', 'return', 'None')):
        '''Simple method to update the ranges.'''
        pass
    # WARNING: Decompyle incomplete

    
    def unset(self = None):
        '''Sets the units to `None` which indicates that the header should
        no longer be used.
        '''
        self.set(None, None, units = None)

    
    def to_header(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return self._units is not None

    
    def __str__(self = None):
        return self.to_header()

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {str(self)!r}>'''


from  import http
