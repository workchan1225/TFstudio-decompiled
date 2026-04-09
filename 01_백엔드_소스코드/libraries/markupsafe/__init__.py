# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import string
import typing as t

try:
    from _speedups import _escape_inner
except ImportError:
    from _native import _escape_inner

if t.TYPE_CHECKING:
    import typing_extensions as te

class _HasHTML(t.Protocol):
    
    def __html__(self = None):
        pass



class _TPEscape(t.Protocol):
    
    def __call__(self = None, s = None):
        pass



def escape(s = None):
    '''Replace the characters ``&``, ``<``, ``>``, ``\'``, and ``"`` in
    the string with HTML-safe sequences. Use this if you need to display
    text that might contain such characters in HTML.

    If the object has an ``__html__`` method, it is called and the
    return value is assumed to already be safe for HTML.

    :param s: An object to be converted to a string and escaped.
    :return: A :class:`Markup` string with the escaped text.
    '''
    if type(s) is str:
        return Markup(_escape_inner(s))
    if None(s, '__html__'):
        return Markup(s.__html__())
    return None(_escape_inner(str(s)))


def escape_silent(s = None):
    """Like :func:`escape` but treats ``None`` as the empty string.
    Useful with optional values, as otherwise you get the string
    ``'None'`` when the value is ``None``.

    >>> escape(None)
    Markup('None')
    >>> escape_silent(None)
    Markup('')
    """
    pass
# WARNING: Decompyle incomplete


def soft_str(s = None):
    '''Convert an object to a string if it isn\'t already. This preserves
    a :class:`Markup` string rather than converting it back to a basic
    string, so it will still be marked as safe and won\'t be escaped
    again.

    >>> value = escape("<User 1>")
    >>> value
    Markup(\'&lt;User 1&gt;\')
    >>> escape(str(value))
    Markup(\'&amp;lt;User 1&amp;gt;\')
    >>> escape(soft_str(value))
    Markup(\'&lt;User 1&gt;\')
    '''
    if not isinstance(s, str):
        return str(s)


class Markup(str):
    pass
# WARNING: Decompyle incomplete


class EscapeFormatter(string.Formatter):
    pass
# WARNING: Decompyle incomplete


class _MarkupEscapeHelper:
    '''Helper for :meth:`Markup.__mod__`.'''
    __slots__ = ('obj', 'escape')
    
    def __init__(self = None, obj = None, escape = None):
        self.obj = obj
        self.escape = escape

    
    def __getitem__(self = None, key = None):
        return self.__class__(self.obj[key], self.escape)

    
    def __str__(self = None):
        return str(self.escape(self.obj))

    
    def __repr__(self = None):
        return str(self.escape(repr(self.obj)))

    
    def __int__(self = None):
        return int(self.obj)

    
    def __float__(self = None):
        return float(self.obj)



def __getattr__(name = None):
    if name == '__version__':
        import importlib.metadata as importlib
        import warnings
        warnings.warn('The \'__version__\' attribute is deprecated and will be removed in MarkupSafe 3.1. Use feature detection, or `importlib.metadata.version("markupsafe")`, instead.', DeprecationWarning, stacklevel = 2)
        return importlib.metadata.version('markupsafe')
    raise None(name)
