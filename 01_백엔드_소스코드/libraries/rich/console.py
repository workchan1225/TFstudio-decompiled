# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: console.pyc (Python 3.11)

import inspect
import os
import sys
import threading
import zlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from functools import wraps
from getpass import getpass
from html import escape
from inspect import isclass
from itertools import islice
from math import ceil
from time import monotonic
from types import FrameType, ModuleType, TracebackType
from typing import IO, TYPE_CHECKING, Any, Callable, Dict, Iterable, List, Literal, Mapping, NamedTuple, Optional, Protocol, TextIO, Tuple, Type, Union, cast, runtime_checkable
from rich._null_file import NULL_FILE
from  import errors, themes
from _emoji_replace import _emoji_replace
from _export_format import CONSOLE_HTML_FORMAT, CONSOLE_SVG_FORMAT
from _fileno import get_fileno
from _log_render import FormatTimeCallable, LogRender
from align import Align, AlignMethod
from color import ColorSystem, blend_rgb
from control import Control
from emoji import EmojiVariant
from highlighter import NullHighlighter, ReprHighlighter
from markup import render as render_markup
from measure import Measurement, measure_renderables
from pager import Pager, SystemPager
from pretty import Pretty, is_expandable
from protocol import rich_cast
from region import Region
from scope import render_scope
from screen import Screen
from segment import Segment
from style import Style, StyleType
from styled import Styled
from terminal_theme import DEFAULT_TERMINAL_THEME, SVG_EXPORT_THEME, TerminalTheme
from text import Text, TextType
from theme import Theme, ThemeStack
if TYPE_CHECKING:
    from _windows import WindowsConsoleFeatures
    from live import Live
    from status import Status
JUPYTER_DEFAULT_COLUMNS = 115
JUPYTER_DEFAULT_LINES = 100
WINDOWS = sys.platform == 'win32'
HighlighterType = Callable[([
    Union[(str, 'Text')]], 'Text')]
JustifyMethod = Literal[('default', 'left', 'center', 'right', 'full')]
OverflowMethod = Literal[('fold', 'crop', 'ellipsis', 'ignore')]

class NoChange:
    pass

NO_CHANGE = NoChange()

try:
    _STDIN_FILENO = sys.__stdin__.fileno()
except Exception:
    _STDIN_FILENO = 0


try:
    _STDOUT_FILENO = sys.__stdout__.fileno()
except Exception:
    _STDOUT_FILENO = 1


try:
    _STDERR_FILENO = sys.__stderr__.fileno()
except Exception:
    _STDERR_FILENO = 2

_STD_STREAMS = (_STDIN_FILENO, _STDOUT_FILENO, _STDERR_FILENO)
_STD_STREAMS_OUTPUT = (_STDOUT_FILENO, _STDERR_FILENO)
_TERM_COLORS = {
    'kitty': ColorSystem.EIGHT_BIT,
    '256color': ColorSystem.EIGHT_BIT,
    '16color': ColorSystem.STANDARD }

class ConsoleDimensions(NamedTuple):
    height: int = 'Size of the terminal.'

ConsoleOptions = <NODE:12>()
RichCast = <NODE:12>()
ConsoleRenderable = <NODE:12>()
RenderableType = Union[(ConsoleRenderable, RichCast, str)]
RenderResult = Iterable[Union[(RenderableType, Segment)]]
_null_highlighter = NullHighlighter()

class CaptureError(Exception):
    '''An error in the Capture context manager.'''
    pass


class NewLine:
    '''A renderable to generate new line(s)'''
    
    def __init__(self = None, count = None):
        self.count = count

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete



class ScreenUpdate:
    '''Render a list of lines at a given offset.'''
    
    def __init__(self = None, lines = None, x = None, y = ('lines', List[List[Segment]], 'x', int, 'y', int, 'return', None)):
        self._lines = lines
        self.x = x
        self.y = y

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete



class Capture:
    '''Context manager to capture the result of printing to the console.
    See :meth:`~rich.console.Console.capture` for how to use.

    Args:
        console (Console): A console instance to capture output.
    '''
    
    def __init__(self = None, console = None):
        self._console = console
        self._result = None

    
    def __enter__(self = None):
        self._console.begin_capture()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', Optional[Type[BaseException]], 'exc_val', Optional[BaseException], 'exc_tb', Optional[TracebackType], 'return', None)):
        self._result = self._console.end_capture()

    
    def get(self = None):
        '''Get the result of the capture.'''
        pass
    # WARNING: Decompyle incomplete



class ThemeContext:
    '''A context manager to use a temporary theme. See :meth:`~rich.console.Console.use_theme` for usage.'''
    
    def __init__(self = None, console = None, theme = None, inherit = (True,)):
        self.console = console
        self.theme = theme
        self.inherit = inherit

    
    def __enter__(self = None):
        self.console.push_theme(self.theme)
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', Optional[Type[BaseException]], 'exc_val', Optional[BaseException], 'exc_tb', Optional[TracebackType], 'return', None)):
        self.console.pop_theme()



class PagerContext:
    """A context manager that 'pages' content. See :meth:`~rich.console.Console.pager` for usage."""
    
    def __init__(self = None, console = None, pager = None, styles = (None, False, False), links = ('console', 'Console', 'pager', Optional[Pager], 'styles', bool, 'links', bool, 'return', None)):
        self._console = console
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self._console._enter_buffer()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', Optional[Type[BaseException]], 'exc_val', Optional[BaseException], 'exc_tb', Optional[TracebackType], 'return', None)):
        pass
    # WARNING: Decompyle incomplete



class ScreenContext:
    '''A context manager that enables an alternative screen. See :meth:`~rich.console.Console.screen` for usage.'''
    
    def __init__(self = None, console = None, hide_cursor = None, style = ('',)):
        self.console = console
        self.hide_cursor = hide_cursor
        self.screen = Screen(style = style)
        self._changed = False

    
    def update(self = None, *, style, *renderables):
        '''Update the screen.

        Args:
            renderable (RenderableType, optional): Optional renderable to replace current renderable,
                or None for no change. Defaults to None.
            style: (Style, optional): Replacement style, or None for no change. Defaults to None.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self._changed = self.console.set_alt_screen(True)
        if self._changed and self.hide_cursor:
            self.console.show_cursor(False)
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', Optional[Type[BaseException]], 'exc_val', Optional[BaseException], 'exc_tb', Optional[TracebackType], 'return', None)):
        if self._changed:
            self.console.set_alt_screen(False)
            if self.hide_cursor:
                self.console.show_cursor(True)
                return None
            return None



class Group:
    '''Takes a group of renderables and returns a renderable object that renders the group.

    Args:
        renderables (Iterable[RenderableType]): An iterable of renderable objects.
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    '''
    
    def __init__(self = None, *, fit, *renderables):
        self._renderables = renderables
        self.fit = fit
        self._render = None

    renderables = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __rich_measure__(self = None, console = None, options = None):
        if self.fit:
            return measure_renderables(console, options, self.renderables)
        return None(options.max_width, options.max_width)

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete



def group(fit = None):
    '''A decorator that turns an iterable of renderables in to a group.

    Args:
        fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_jupyter():
    """Check if we're running in a Jupyter notebook."""
    
    try:
        get_ipython
    except NameError:
        return False

    ipython = get_ipython()
    shell = ipython.__class__.__name__
    if 'google.colab' in str(ipython.__class__) and os.getenv('DATABRICKS_RUNTIME_VERSION') or shell == 'ZMQInteractiveShell':
        return True
    if None == 'TerminalInteractiveShell':
        return False

COLOR_SYSTEMS = {
    'standard': ColorSystem.STANDARD,
    '256': ColorSystem.EIGHT_BIT,
    'truecolor': ColorSystem.TRUECOLOR,
    'windows': ColorSystem.WINDOWS }
_COLOR_SYSTEMS_NAMES = COLOR_SYSTEMS.items()()
ConsoleThreadLocals = <NODE:12>()

class RenderHook(ABC):
    '''Provides hooks in to the render process.'''
    process_renderables = (lambda self = None, renderables = None: pass)()

_windows_console_features: Optional['WindowsConsoleFeatures'] = None

def get_windows_console_features():
    pass
# WARNING: Decompyle incomplete


def detect_legacy_windows():
    '''Detect legacy Windows.'''
    if WINDOWS:
        pass
    return not (get_windows_console_features().vt)


class Console:
    '''A high level console interface.

    Args:
        color_system (str, optional): The color system supported by your terminal,
            either ``"standard"``, ``"256"`` or ``"truecolor"``. Leave as ``"auto"`` to autodetect.
        force_terminal (Optional[bool], optional): Enable/disable terminal control codes, or None to auto-detect terminal. Defaults to None.
        force_jupyter (Optional[bool], optional): Enable/disable Jupyter rendering, or None to auto-detect Jupyter. Defaults to None.
        force_interactive (Optional[bool], optional): Enable/disable interactive mode, or None to auto detect. Defaults to None.
        soft_wrap (Optional[bool], optional): Set soft wrap default on print method. Defaults to False.
        theme (Theme, optional): An optional style theme object, or ``None`` for default theme.
        stderr (bool, optional): Use stderr rather than stdout if ``file`` is not specified. Defaults to False.
        file (IO, optional): A file object where the console should write to. Defaults to stdout.
        quiet (bool, Optional): Boolean to suppress all output. Defaults to False.
        width (int, optional): The width of the terminal. Leave as default to auto-detect width.
        height (int, optional): The height of the terminal. Leave as default to auto-detect height.
        style (StyleType, optional): Style to apply to all output, or None for no style. Defaults to None.
        no_color (Optional[bool], optional): Enabled no color mode, or None to auto detect. Defaults to None.
        tab_size (int, optional): Number of spaces used to replace a tab character. Defaults to 8.
        record (bool, optional): Boolean to enable recording of terminal output,
            required to call :meth:`export_html`, :meth:`export_svg`, and :meth:`export_text`. Defaults to False.
        markup (bool, optional): Boolean to enable :ref:`console_markup`. Defaults to True.
        emoji (bool, optional): Enable emoji code. Defaults to True.
        emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.
        highlight (bool, optional): Enable automatic highlighting. Defaults to True.
        log_time (bool, optional): Boolean to enable logging of time by :meth:`log` methods. Defaults to True.
        log_path (bool, optional): Boolean to enable the logging of the caller by :meth:`log`. Defaults to True.
        log_time_format (Union[str, TimeFormatterCallable], optional): If ``log_time`` is enabled, either string for strftime or callable that formats the time. Defaults to "[%X] ".
        highlighter (HighlighterType, optional): Default highlighter.
        legacy_windows (bool, optional): Enable legacy Windows mode, or ``None`` to auto detect. Defaults to ``None``.
        safe_box (bool, optional): Restrict box options that don\'t render on legacy Windows.
        get_datetime (Callable[[], datetime], optional): Callable that gets the current time as a datetime.datetime object (used by Console.log),
            or None for datetime.now.
        get_time (Callable[[], time], optional): Callable that gets the current time in seconds, default uses time.monotonic.
    '''
    _environ: Mapping[(str, str)] = os.environ
    
    def __init__(self = None, *, color_system, force_terminal, force_jupyter, force_interactive, soft_wrap, theme, stderr, file, quiet, width, height, style, no_color, tab_size, record, markup, emoji, emoji_variant, highlight, log_time, log_path, log_time_format, highlighter, legacy_windows, safe_box, get_datetime, get_time, _environ):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<console width={self.width} {self._color_system!s}>'''

    file = (lambda self = None: if not self._file:
passfile = sys.stderr if self.stderr else sys.stdoutfile = getattr(file, 'rich_proxied_file', file)# WARNING: Decompyle incomplete
)()
    file = (lambda self = None, new_file = None: self._file = new_file)()
    _buffer = (lambda self = None: self._thread_locals.buffer)()
    _buffer_index = (lambda self = None: self._thread_locals.buffer_index)()
    _buffer_index = (lambda self = None, value = None: self._thread_locals.buffer_index = value)()
    _theme_stack = (lambda self = None: self._thread_locals.theme_stack)()
    
    def _detect_color_system(self = None):
        '''Detect color system from env vars.'''
        if self.is_jupyter:
            return ColorSystem.TRUECOLOR
        if None.is_terminal or self.is_dumb_terminal:
            return None
        if None:
            if self.legacy_windows:
                return ColorSystem.WINDOWS
            windows_console_features = None()
            return ColorSystem.TRUECOLOR if windows_console_features.truecolor else ColorSystem.EIGHT_BIT
        color_term = None._environ.get('COLORTERM', '').strip().lower()
        if color_term in ('truecolor', '24bit'):
            return ColorSystem.TRUECOLOR
        term = None._environ.get('TERM', '').strip().lower()
        (_term_name, _hyphen, colors) = term.rpartition('-')
        color_system = _TERM_COLORS.get(colors, ColorSystem.STANDARD)
        return color_system

    
    def _enter_buffer(self = None):
        '''Enter in to a buffer context, and buffer all output.'''
        pass

    
    def _exit_buffer(self = None):
        '''Leave buffer context, and render content if required.'''
        self._check_buffer()

    
    def set_live(self = None, live = None):
        '''Set Live instance. Used by Live context manager (no need to call directly).

        Args:
            live (Live): Live instance using this Console.

        Returns:
            Boolean that indicates if the live is the topmost of the stack.

        Raises:
            errors.LiveError: If this Console has a Live context currently active.
        '''
        self._lock
        self._live_stack.append(live)
        None(None, None)
        return 
        with None:
            if not None, len(self._live_stack) == 1:
                pass

    
    def clear_live(self = None):
        '''Clear the Live instance. Used by the Live context manager (no need to call directly).'''
        self._lock
        self._live_stack.pop()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def push_render_hook(self = None, hook = None):
        '''Add a new render hook to the stack.

        Args:
            hook (RenderHook): Render hook instance.
        '''
        self._lock
        self._render_hooks.append(hook)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def pop_render_hook(self = None):
        '''Pop the last renderhook from the stack.'''
        self._lock
        self._render_hooks.pop()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def __enter__(self = None):
        '''Own context manager to enter buffer context.'''
        self._enter_buffer()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', Any, 'exc_value', Any, 'traceback', Any, 'return', None)):
        '''Exit buffer context.'''
        self._exit_buffer()

    
    def begin_capture(self = None):
        '''Begin capturing console output. Call :meth:`end_capture` to exit capture mode and return output.'''
        self._enter_buffer()

    
    def end_capture(self = None):
        '''End capture mode and return captured string.

        Returns:
            str: Console output.
        '''
        render_result = self._render_buffer(self._buffer)
        del self._buffer[:]
        self._exit_buffer()
        return render_result

    
    def push_theme(self = None, theme = None, *, inherit):
        '''Push a new theme on to the top of the stack, replacing the styles from the previous theme.
        Generally speaking, you should call :meth:`~rich.console.Console.use_theme` to get a context manager, rather
        than calling this method directly.

        Args:
            theme (Theme): A theme instance.
            inherit (bool, optional): Inherit existing styles. Defaults to True.
        '''
        self._theme_stack.push_theme(theme, inherit = inherit)

    
    def pop_theme(self = None):
        '''Remove theme from top of stack, restoring previous theme.'''
        self._theme_stack.pop_theme()

    
    def use_theme(self = None, theme = None, *, inherit):
        '''Use a different theme for the duration of the context manager.

        Args:
            theme (Theme): Theme instance to user.
            inherit (bool, optional): Inherit existing console styles. Defaults to True.

        Returns:
            ThemeContext: [description]
        '''
        return ThemeContext(self, theme, inherit)

    color_system = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    encoding = (lambda self = None:
