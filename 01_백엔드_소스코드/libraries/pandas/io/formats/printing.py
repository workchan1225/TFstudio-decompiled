# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: printing.pyc (Python 3.11)

'''
Printing tools.
'''
from __future__ import annotations
from collections.abc import Callable, Iterable, Mapping, Sequence
import sys
from typing import TYPE_CHECKING, Any, TypeAlias, TypeVar
from unicodedata import east_asian_width
from pandas._config import get_option
from pandas.core.dtypes.inference import is_sequence
from pandas.io.formats.console import get_console_size
if TYPE_CHECKING:
    from pandas._typing import ListLike
EscapeChars: 'TypeAlias' = Mapping[(str, str)] | Iterable[str]
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

def adjoin(space = None, *lists, **kwargs):
    '''
    Glues together two sets of strings using the amount of space requested.
    The idea is to prettify.

    ----------
    space : int
        number of spaces for padding
    lists : str
        list of str which being joined
    strlen : callable
        function used to calculate the length of each str. Needed for unicode
        handling.
    justfunc : callable
        function used to justify str. Needed for unicode handling.
    '''
    pass
# WARNING: Decompyle incomplete


def _adj_justify(texts = None, max_len = None, mode = None):
    '''
    Perform ljust, center, rjust against string or list-like
    '''
    pass
# WARNING: Decompyle incomplete


def _pprint_seq(seq = None, _nest_lvl = None, max_seq_items = None, **kwds):
    '''
    internal. pprinter for iterables. you should probably use pprint_thing()
    rather than calling this directly.

    bounds length of printed sequence, depending on options
    '''
    if isinstance(seq, set):
        fmt = '{{{body}}}'
    elif isinstance(seq, frozenset):
        fmt = 'frozenset({{{body}}})'
    elif hasattr(seq, '__setitem__'):
        pass
    
    fmt = '({body})'
    if max_seq_items is False:
        max_items = None
# WARNING: Decompyle incomplete


def _pprint_dict(seq = None, _nest_lvl = None, max_seq_items = None, **kwds):
    '''
    internal. pprinter for iterables. you should probably use pprint_thing()
    rather than calling this directly.
    '''
    fmt = '{{{things}}}'
    pairs = []
    pfmt = '{key}: {val}'
    if max_seq_items is False:
        nitems = len(seq)
    elif not max_seq_items:
        pass
# WARNING: Decompyle incomplete


def pprint_thing(thing, _nest_lvl = None, escape_chars = None, default_escapes = None, quote_strings = (0, None, False, False, None), max_seq_items = ('thing', 'object', '_nest_lvl', 'int', 'escape_chars', 'EscapeChars | None', 'default_escapes', 'bool', 'quote_strings', 'bool', 'max_seq_items', 'int | None', 'return', 'str')):
    '''
    This function is the sanctioned way of converting objects
    to a string representation and properly handles nested sequences.

    Parameters
    ----------
    thing : anything to be formatted
    _nest_lvl : internal use only. pprint_thing() is mutually-recursive
        with pprint_sequence, this argument is used to keep track of the
        current nesting level, and limit it.
    escape_chars : list[str] or Mapping[str, str], optional
        Characters to escape. If a Mapping is passed the values are the
        replacements
    default_escapes : bool, default False
        Whether the input escape characters replaces or adds to the defaults
    max_seq_items : int or None, default None
        Pass through to other pretty printers to limit sequence printing

    Returns
    -------
    str
    '''
    pass
# WARNING: Decompyle incomplete


def pprint_thing_encoded(object = None, encoding = None, errors = None):
    value = pprint_thing(object)
    return value.encode(encoding, errors)


def enable_data_resource_formatter(enable = None):
    pass
# WARNING: Decompyle incomplete


def default_pprint(thing = None, max_seq_items = None):
    return pprint_thing(thing, escape_chars = ('\t', '\r', '\n'), quote_strings = True, max_seq_items = max_seq_items)


def format_object_summary(obj, formatter = None, is_justify = None, name = None, indent_for_name = (True, None, True, False), line_break_each_value = ('obj', 'ListLike', 'formatter', 'Callable', 'is_justify', 'bool', 'name', 'str | None', 'indent_for_name', 'bool', 'line_break_each_value', 'bool', 'return', 'str')):
    '''
    Return the formatted obj as a unicode string

    Parameters
    ----------
    obj : object
        must be iterable and support __getitem__
    formatter : callable
        string formatter for an element
    is_justify : bool
        should justify the display
    name : name, optional
        defaults to the class name of the obj
    indent_for_name : bool, default True
        Whether subsequent lines should be indented to
        align with the name.
    line_break_each_value : bool, default False
        If True, inserts a line break for each value of ``obj``.
        If False, only break lines when the a line of values gets wider
        than the display width.

    Returns
    -------
    summary string
    '''
    pass
# WARNING: Decompyle incomplete


def _justify(head = None, tail = None):
    '''
    Justify items in head and tail, so they are right-aligned when stacked.

    Parameters
    ----------
    head : list-like of list-likes of strings
    tail : list-like of list-likes of strings

    Returns
    -------
    tuple of list of tuples of strings
        Same as head and tail, but items are right aligned when stacked
        vertically.

    Examples
    --------
    >>> _justify([["a", "b"]], [["abc", "abcd"]])
    ([(\'  a\', \'   b\')], [(\'abc\', \'abcd\')])
    '''
    pass
# WARNING: Decompyle incomplete


def PrettyDict():
    '''PrettyDict'''
    __doc__ = 'Dict extension to support abbreviated __repr__'
    
    def __repr__(self = None):
        return pprint_thing(self)


PrettyDict = <NODE:27>(PrettyDict, 'PrettyDict', dict[(_KT, _VT)])

class _TextAdjustment:
    
    def __init__(self = None):
        self.encoding = get_option('display.encoding')

    
    def len(self = None, text = None):
        return len(text)

    
    def justify(self = None, texts = None, max_len = None, mode = ('right',)):
        '''
        Perform ljust, center, rjust against string or list-like
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def adjoin(self = None, space = None, *lists, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class _EastAsianTextAdjustment(_TextAdjustment):
    pass
# WARNING: Decompyle incomplete


def get_adjustment():
    use_east_asian_width = get_option('display.unicode.east_asian_width')
    if use_east_asian_width:
        return _EastAsianTextAdjustment()
    return None()
