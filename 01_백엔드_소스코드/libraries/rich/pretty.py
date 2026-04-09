# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pretty.pyc (Python 3.11)

import builtins
import collections
import dataclasses
import inspect
import os
import reprlib
import sys
from array import array
from collections import Counter, UserDict, UserList, defaultdict, deque
from dataclasses import dataclass, fields, is_dataclass
from inspect import isclass
from itertools import islice
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Callable, DefaultDict, Deque, Dict, Iterable, List, Optional, Sequence, Set, Tuple, Union
from rich.repr import RichReprResult

try:
    import attr as _attr_module
    _has_attrs = hasattr(_attr_module, 'ib')
except ImportError:
    _has_attrs = False

from  import get_console
from _loop import loop_last
from _pick import pick_bool
from abc import RichRenderable
from cells import cell_len
from highlighter import ReprHighlighter
from jupyter import JupyterMixin, JupyterRenderable
from measure import Measurement
from text import Text
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, HighlighterType, JustifyMethod, OverflowMethod, RenderResult

def _is_attr_object(obj = None):
    '''Check if an object was created with attrs module.'''
    if _has_attrs:
        pass
    return _attr_module.has(type(obj))


def _get_attr_fields(obj = None):
    '''Get fields for an attrs object.'''
    return _attr_module.fields(type(obj)) if _has_attrs else []


def _is_dataclass_repr(obj = None):
    '''Check if an instance of a dataclass contains the default repr.

    Args:
        obj (object): A dataclass instance.

    Returns:
        bool: True if the default repr is used, False if there is a custom repr.
    '''
    
    try:
        return obj.__repr__.__code__.co_filename in (dataclasses.__file__, reprlib.__file__)
    except Exception:
        return False


_dummy_namedtuple = collections.namedtuple('_dummy_namedtuple', [])

def _has_default_namedtuple_repr(obj = None):
    """Check if an instance of namedtuple contains the default repr

    Args:
        obj (object): A namedtuple

    Returns:
        bool: True if the default repr is used, False if there's a custom repr.
    """
    obj_file = None
    
    try:
        obj_file = inspect.getfile(obj.__repr__)
    except (OSError, TypeError):
        pass

    default_repr_file = inspect.getfile(_dummy_namedtuple.__repr__)
    return obj_file == default_repr_file


def _ipy_display_hook(value, console, overflow, crop, indent_guides = None, max_length = None, max_string = None, max_depth = (None, 'ignore', False, False, None, None, None, False), expand_all = ('value', Any, 'console', Optional['Console'], 'overflow', 'OverflowMethod', 'crop', bool, 'indent_guides', bool, 'max_length', Optional[int], 'max_string', Optional[int], 'max_depth', Optional[int], 'expand_all', bool, 'return', Union[(str, None)])):
    ConsoleRenderable = ConsoleRenderable
    import console
# WARNING: Decompyle incomplete


def _safe_isinstance(obj = None, class_or_tuple = None):
    '''isinstance can fail in rare cases, for example types with no __class__'''
    
    try:
        return isinstance(obj, class_or_tuple)
    except Exception:
        return False



def install(console, overflow, crop, indent_guides = None, max_length = None, max_string = None, max_depth = (None, 'ignore', False, False, None, None, None, False), expand_all = ('console', Optional['Console'], 'overflow', 'OverflowMethod', 'crop', bool, 'indent_guides', bool, 'max_length', Optional[int], 'max_string', Optional[int], 'max_depth', Optional[int], 'expand_all', bool, 'return', None)):
    '''Install automatic pretty printing in the Python REPL.

    Args:
        console (Console, optional): Console instance or ``None`` to use global console. Defaults to None.
        overflow (Optional[OverflowMethod], optional): Overflow method. Defaults to "ignore".
        crop (Optional[bool], optional): Enable cropping of long lines. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
    '''
    pass
# WARNING: Decompyle incomplete


class Pretty(JupyterMixin):
    '''A rich renderable that pretty prints an object.

    Args:
        _object (Any): An object to pretty print.
        highlighter (HighlighterType, optional): Highlighter object to apply to result, or None for ReprHighlighter. Defaults to None.
        indent_size (int, optional): Number of spaces in indent. Defaults to 4.
        justify (JustifyMethod, optional): Justify method, or None for default. Defaults to None.
        overflow (OverflowMethod, optional): Overflow method, or None for default. Defaults to None.
        no_wrap (Optional[bool], optional): Disable word wrapping. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        margin (int, optional): Subtrace a margin from width to force containers to expand earlier. Defaults to 0.
        insert_line (bool, optional): Insert a new line if the output has multiple new lines. Defaults to False.
    '''
    
    def __init__(self = None, _object = None, highlighter = None, *, indent_size, justify, overflow, no_wrap, indent_guides, max_length, max_string, max_depth, expand_all, margin, insert_line):
        self._object = _object
        if not highlighter:
            pass
        self.highlighter = ReprHighlighter()
        self.indent_size = indent_size
        self.justify = justify
        self.overflow = overflow
        self.no_wrap = no_wrap
        self.indent_guides = indent_guides
        self.max_length = max_length
        self.max_string = max_string
        self.max_depth = max_depth
        self.expand_all = expand_all
        self.margin = margin
        self.insert_line = insert_line

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        pretty_str = pretty_repr(self._object, max_width = options.max_width, indent_size = self.indent_size, max_length = self.max_length, max_string = self.max_string, max_depth = self.max_depth, expand_all = self.expand_all)
        text_width = (lambda .0: pass# WARNING: Decompyle incomplete
)(pretty_str.splitlines()()) if pretty_str else 0
        return Measurement(text_width, text_width)



def _get_braces_for_defaultdict(_object = None):
    return (f'''defaultdict({_object.default_factory!r}, {{''', '})', f'''defaultdict({_object.default_factory!r}, {{}})''')


def _get_braces_for_deque(_object = None):
    pass
# WARNING: Decompyle incomplete


def _get_braces_for_array(_object = None):
    return (f'''array({_object.typecode!r}, [''', '])', f'''array({_object.typecode!r})''')

_BRACES: Dict[(type, Callable[([
    Any], Tuple[(str, str, str)])])] = {
    MappingProxyType: (lambda _object: ('mappingproxy({', '})', 'mappingproxy({})')),
    tuple: (lambda _object: ('(', ')', '()')),
    set: (lambda _object: ('{', '}', 'set()')),
    UserList: (lambda _object: ('[', ']', '[]')),
    list: (lambda _object: ('[', ']', '[]')),
    frozenset: (lambda _object: ('frozenset({', '})', 'frozenset()')),
    UserDict: (lambda _object: ('{', '}', '{}')),
    dict: (lambda _object: ('{', '}', '{}')),
    deque: _get_braces_for_deque,
    Counter: (lambda _object: ('Counter({', '})', 'Counter()')),
    defaultdict: _get_braces_for_defaultdict,
    array: _get_braces_for_array,
    os._Environ: (lambda _object: ('environ({', '})', 'environ({})')) }
_CONTAINERS = tuple(_BRACES.keys())
_MAPPING_CONTAINERS = (dict, os._Environ, MappingProxyType, UserDict)

def is_expandable(obj = None):
