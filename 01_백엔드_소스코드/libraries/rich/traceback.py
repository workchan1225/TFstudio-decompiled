# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: traceback.pyc (Python 3.11)

import inspect
import linecache
import os
import sys
from dataclasses import dataclass, field
from itertools import islice
from traceback import walk_tb
from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple, Type, Union
from pygments.lexers import guess_lexer_for_filename
from pygments.token import Comment, Keyword, Name, Number, Operator, String
from pygments.token import Text as TextToken
from pygments.token import Token
from pygments.util import ClassNotFound
from  import pretty
from _loop import loop_first_last, loop_last
from columns import Columns
from console import Console, ConsoleOptions, ConsoleRenderable, OverflowMethod, Group, RenderResult, group
from constrain import Constrain
from highlighter import RegexHighlighter, ReprHighlighter
from panel import Panel
from scope import render_scope
from style import Style
from syntax import Syntax, SyntaxPosition
from text import Text
from theme import Theme
WINDOWS = sys.platform == 'win32'
LOCALS_MAX_LENGTH = 10
LOCALS_MAX_STRING = 80

def _iter_syntax_lines(start = None, end = None):
    '''Yield start and end positions per line.

    Args:
        start: Start position.
        end: End position.

    Returns:
        Iterable of (LINE, COLUMN1, COLUMN2).
    '''
    pass
# WARNING: Decompyle incomplete


def install(*, console, width, code_width, extra_lines, theme, word_wrap, show_locals, locals_max_length, locals_max_string, locals_max_depth, locals_hide_dunder, locals_hide_sunder, locals_overflow, indent_guides, suppress, max_frames):
    '''Install a rich traceback handler.

    Once installed, any tracebacks will be printed with syntax highlighting and rich formatting.


    Args:
        console (Optional[Console], optional): Console to write exception to. Default uses internal Console instance.
        width (Optional[int], optional): Width (in characters) of traceback. Defaults to 100.
        code_width (Optional[int], optional): Code width (in characters) of traceback. Defaults to 88.
        extra_lines (int, optional): Extra lines of code. Defaults to 3.
        theme (Optional[str], optional): Pygments theme to use in traceback. Defaults to ``None`` which will pick
            a theme appropriate for the platform.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_max_depth (int, optional): Maximum depths of locals before truncating, or None to disable. Defaults to None.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        locals_overflow (OverflowMethod, optional): How to handle overflowing locals, or None to disable. Defaults to None.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.

    Returns:
        Callable: The previous exception handler that was replaced.

    '''
    pass
# WARNING: Decompyle incomplete

Frame = <NODE:12>()
_SyntaxError = <NODE:12>()
Stack = <NODE:12>()
Trace = <NODE:12>()

class PathHighlighter(RegexHighlighter):
    highlights = [
        '(?P<dim>.*/)(?P<bold>.+)']


class Traceback:
    '''A Console renderable that renders a traceback.

    Args:
        trace (Trace, optional): A `Trace` object produced from `extract`. Defaults to None, which uses
            the last exception.
        width (Optional[int], optional): Number of characters used to traceback. Defaults to 100.
        code_width (Optional[int], optional): Number of code characters used to traceback. Defaults to 88.
        extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
        theme (str, optional): Override pygments theme used in traceback.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_max_depth (int, optional): Maximum depths of locals before truncating, or None to disable. Defaults to None.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        locals_overflow (OverflowMethod, optional): How to handle overflowing locals, or None to disable. Defaults to None.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

    '''
    LEXERS = {
        '': 'text',
        '.py': 'python',
        '.pxd': 'cython',
        '.pyx': 'cython',
        '.pxi': 'pyrex' }
    
    def __init__(self = None, trace = None, *, width, code_width, extra_lines, theme, word_wrap, show_locals, locals_max_length, locals_max_string, locals_max_depth, locals_hide_dunder, locals_hide_sunder, locals_overlow, indent_guides, suppress, max_frames):
        pass
    # WARNING: Decompyle incomplete

    from_exception = (lambda cls = None, exc_type = None, exc_value = None, traceback = classmethod, *, width, code_width, extra_lines, theme: rich_traceback = cls.extract(exc_type, exc_value, traceback, show_locals = show_locals, locals_max_length = locals_max_length, locals_max_string = locals_max_string, locals_max_depth = locals_max_depth, locals_hide_dunder = locals_hide_dunder, locals_hide_sunder = locals_hide_sunder)# WARNING: Decompyle incomplete
)()
    extract = (lambda cls = None, exc_type = None, exc_value = None, traceback = classmethod, *, show_locals, locals_max_length, locals_max_string, locals_max_depth: pass# WARNING: Decompyle incomplete
)()
    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    _render_syntax_error = (lambda self = None, syntax_error = None: pass# WARNING: Decompyle incomplete
)()
    _guess_lexer = (lambda cls = None, filename = None, code = classmethod: ext = os.path.splitext(filename)[-1]if not ext:
new_line_index = code.index('\n')first_line = code[:new_line_index] if new_line_index != -1 else codeif first_line.startswith('#!') and 'python' in first_line.lower():
'python'try:
if not cls.LEXERS.get(ext):
guess_lexer_for_filename(filename, code).nameexcept ClassNotFound:
'text')()
    _render_stack = (lambda self = None, stack = None: pass# WARNING: Decompyle incomplete
)()

if __name__ == '__main__':
    install(show_locals = True)
    import sys
    
    def bar(a = dataclass):
        one = 1
        print(one / a)

    
    def foo(a = dataclass):
        _rich_traceback_guard = True
        zed = {
            'characters': {
                'Duncan Idaho',
                'Thufir Hawat',
                'Paul Atreides',
                'Vladimir Harkonnen'},
            'atomic_types': (None, False, True) }
        bar(a)

    
    def error():
        foo(0)

    error()
    return None
