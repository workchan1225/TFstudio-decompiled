# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""
Interaction with interactive text terminals.

The :mod:`~humanfriendly.terminal` module makes it easy to interact with
interactive text terminals and format text for rendering on such terminals. If
the terms used in the documentation of this module don't make sense to you then
please refer to the `Wikipedia article on ANSI escape sequences`_ for details
about how ANSI escape sequences work.

This module was originally developed for use on UNIX systems, but since then
Windows 10 gained native support for ANSI escape sequences and this module was
enhanced to recognize and support this. For details please refer to the
:func:`enable_ansi_support()` function.

.. _Wikipedia article on ANSI escape sequences: http://en.wikipedia.org/wiki/ANSI_escape_code#Sequence_elements
"""
import codecs
import numbers
import os
import platform
import re
import subprocess
import sys

try:
    import fcntl
    import termios
    import struct
    HAVE_IOCTL = True
except ImportError:
    HAVE_IOCTL = False

from humanfriendly.compat import coerce_string, is_unicode, on_windows, which
from humanfriendly.decorators import cached
from humanfriendly.deprecation import define_aliases
from humanfriendly.text import concatenate, format
from humanfriendly.usage import format_usage
__all__ = ('ANSI_COLOR_CODES', 'ANSI_CSI', 'ANSI_ERASE_LINE', 'ANSI_HIDE_CURSOR', 'ANSI_RESET', 'ANSI_SGR', 'ANSI_SHOW_CURSOR', 'ANSI_TEXT_STYLES', 'CLEAN_OUTPUT_PATTERN', 'DEFAULT_COLUMNS', 'DEFAULT_ENCODING', 'DEFAULT_LINES', 'HIGHLIGHT_COLOR', 'ansi_strip', 'ansi_style', 'ansi_width', 'ansi_wrap', 'auto_encode', 'clean_terminal_output', 'connected_to_terminal', 'enable_ansi_support', 'find_terminal_size', 'find_terminal_size_using_ioctl', 'find_terminal_size_using_stty', 'get_pager_command', 'have_windows_native_ansi_support', 'message', 'output', 'readline_strip', 'readline_wrap', 'show_pager', 'terminal_supports_colors', 'usage', 'warning')
ANSI_CSI = '\x1b['
ANSI_SGR = 'm'
ANSI_ERASE_LINE = '%sK' % ANSI_CSI
ANSI_RESET = f'''{ANSI_CSI!s}0{ANSI_SGR!s}'''
ANSI_HIDE_CURSOR = '%s?25l' % ANSI_CSI
ANSI_SHOW_CURSOR = '%s?25h' % ANSI_CSI
ANSI_COLOR_CODES = dict(black = 0, red = 1, green = 2, yellow = 3, blue = 4, magenta = 5, cyan = 6, white = 7)
ANSI_TEXT_STYLES = dict(bold = 1, faint = 2, italic = 3, underline = 4, inverse = 7, strike_through = 9)
CLEAN_OUTPUT_PATTERN = re.compile('(\r|\n|\x08|%s)' % re.escape(ANSI_ERASE_LINE))
DEFAULT_LINES = 25
DEFAULT_COLUMNS = 80
DEFAULT_ENCODING = 'UTF-8'
HIGHLIGHT_COLOR = os.environ.get('HUMANFRIENDLY_HIGHLIGHT_COLOR', 'green')

def ansi_strip(text, readline_hints = (True,)):
    '''
    Strip ANSI escape sequences from the given string.

    :param text: The text from which ANSI escape sequences should be removed (a
                 string).
    :param readline_hints: If :data:`True` then :func:`readline_strip()` is
                           used to remove `readline hints`_ from the string.
    :returns: The text without ANSI escape sequences (a string).
    '''
    pattern = f'''{re.escape(ANSI_CSI)!s}.*?{re.escape(ANSI_SGR)!s}'''
    text = re.sub(pattern, '', text)
    if readline_hints:
        text = readline_strip(text)
    return text


def ansi_style(**kw):
    """
    Generate ANSI escape sequences for the given color and/or style(s).

    :param color: The foreground color. Three types of values are supported:

                  - The name of a color (one of the strings 'black', 'red',
                    'green', 'yellow', 'blue', 'magenta', 'cyan' or 'white').
                  - An integer that refers to the 256 color mode palette.
                  - A tuple or list with three integers representing an RGB
                    (red, green, blue) value.

                  The value :data:`None` (the default) means no escape
                  sequence to switch color will be emitted.
    :param background: The background color (see the description
                       of the `color` argument).
    :param bright: Use high intensity colors instead of default colors
                   (a boolean, defaults to :data:`False`).
    :param readline_hints: If :data:`True` then :func:`readline_wrap()` is
                           applied to the generated ANSI escape sequences (the
                           default is :data:`False`).
    :param kw: Any additional keyword arguments are expected to match a key
               in the :data:`ANSI_TEXT_STYLES` dictionary. If the argument's
               value evaluates to :data:`True` the respective style will be
               enabled.
    :returns: The ANSI escape sequences to enable the requested text styles or
              an empty string if no styles were requested.
    :raises: :exc:`~exceptions.ValueError` when an invalid color name is given.

    Even though only eight named colors are supported, the use of `bright=True`
    and `faint=True` increases the number of available colors to around 24 (it
    may be slightly lower, for example because faint black is just black).

    **Support for 8-bit colors**

    In `release 4.7`_ support for 256 color mode was added. While this
    significantly increases the available colors it's not very human friendly
    in usage because you need to look up color codes in the `256 color mode
    palette <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`_.

    You can use the ``humanfriendly --demo`` command to get a demonstration of
    the available colors, see also the screen shot below. Note that the small
    font size in the screen shot was so that the demonstration of 256 color
    mode support would fit into a single screen shot without scrolling :-)
    (I wasn't feeling very creative).

      .. image:: images/ansi-demo.png

    **Support for 24-bit colors**

    In `release 4.14`_ support for 24-bit colors was added by accepting a tuple
    or list with three integers representing the RGB (red, green, blue) value
    of a color. This is not included in the demo because rendering millions of
    colors was deemed unpractical ;-).

    .. _release 4.7: http://humanfriendly.readthedocs.io/en/latest/changelog.html#release-4-7-2018-01-14
    .. _release 4.14: http://humanfriendly.readthedocs.io/en/latest/changelog.html#release-4-14-2018-07-13
    """
    sequences = kw.items()()
    for color_type in ('color', 'background'):
        color_value = kw.get(color_type)
        if isinstance(color_value, (tuple, list)):
            if len(color_value) != 3:
                msg = 'Invalid color value %r! (expected tuple or list with three numbers)'
                raise ValueError(msg % color_value)
            sequences.append(48 if color_type == 'background' else 38)
            sequences.append(2)
            sequences.extend(map(int, color_value))
            continue
        if isinstance(color_value, numbers.Number):
            sequences.extend((39 if color_type == 'background' else 38, 5, int(color_value)))
            continue
        if color_value:
            if color_value not in ANSI_COLOR_CODES:
                msg = 'Invalid color value %r! (expected an integer or one of the strings %s)'
                raise ValueError(msg % (color_value, concatenate(map(repr, sorted(ANSI_COLOR_CODES)))))
            if color_type == 'background':
                if kw.get('bright'):
                    pass
                
            elif kw.get('bright'):
                pass
            
            offset = 30
            sequences.append(offset + ANSI_COLOR_CODES[color_value])
        if sequences:
            encoded = ANSI_CSI + ';'.join(map(str, sequences)) + ANSI_SGR
            return readline_wrap(encoded) if kw.get('readline_hints') else encoded
        return 90


def ansi_width(text):
    '''
    Calculate the effective width of the given text (ignoring ANSI escape sequences).

    :param text: The text whose width should be calculated (a string).
    :returns: The width of the text without ANSI escape sequences (an
              integer).

    This function uses :func:`ansi_strip()` to strip ANSI escape sequences from
    the given string and returns the length of the resulting string.
    '''
    return len(ansi_strip(text))


def ansi_wrap(text, **kw):
    '''
    Wrap text in ANSI escape sequences for the given color and/or style(s).

    :param text: The text to wrap (a string).
    :param kw: Any keyword arguments are passed to :func:`ansi_style()`.
    :returns: The result of this function depends on the keyword arguments:

              - If :func:`ansi_style()` generates an ANSI escape sequence based
                on the keyword arguments, the given text is prefixed with the
                generated ANSI escape sequence and suffixed with
                :data:`ANSI_RESET`.

              - If :func:`ansi_style()` returns an empty string then the text
                given by the caller is returned unchanged.
    '''
    pass
# WARNING: Decompyle incomplete


def auto_encode(stream, text, *args, **kw):
    """
    Reliably write Unicode strings to the terminal.

    :param stream: The file-like object to write to (a value like
                   :data:`sys.stdout` or :data:`sys.stderr`).
    :param text: The text to write to the stream (a string).
    :param args: Refer to :func:`~humanfriendly.text.format()`.
    :param kw: Refer to :func:`~humanfriendly.text.format()`.

    Renders the text using :func:`~humanfriendly.text.format()` and writes it
    to the given stream. If an :exc:`~exceptions.UnicodeEncodeError` is
    encountered in doing so, the text is encoded using :data:`DEFAULT_ENCODING`
    and the write is retried. The reasoning behind this rather blunt approach
    is that it's preferable to get output on the command line in the wrong
    encoding then to have the Python program blow up with a
    :exc:`~exceptions.UnicodeEncodeError` exception.
    """
    pass
# WARNING: Decompyle incomplete


def clean_terminal_output(text):
    """
    Clean up the terminal output of a command.

    :param text: The raw text with special characters (a Unicode string).
    :returns: A list of Unicode strings (one for each line).

    This function emulates the effect of backspace (0x08), carriage return
    (0x0D) and line feed (0x0A) characters and the ANSI 'erase line' escape
    sequence on interactive terminals. It's intended to clean up command output
    that was originally meant to be rendered on an interactive terminal and
    that has been captured using e.g. the :man:`script` program [#]_ or the
    :mod:`pty` module [#]_.

    .. [#] My coloredlogs_ package supports the ``coloredlogs --to-html``
           command which uses :man:`script` to fool a subprocess into thinking
           that it's connected to an interactive terminal (in order to get it
           to emit ANSI escape sequences).

    .. [#] My capturer_ package uses the :mod:`pty` module to fool the current
           process and subprocesses into thinking they are connected to an
           interactive terminal (in order to get them to emit ANSI escape
           sequences).

    **Some caveats about the use of this function:**

    - Strictly speaking the effect of carriage returns cannot be emulated
      outside of an actual terminal due to the interaction between overlapping
      output, terminal widths and line wrapping. The goal of this function is
      to sanitize noise in terminal output while preserving useful output.
      Think of it as a useful and pragmatic but possibly lossy conversion.

    - The algorithm isn't smart enough to properly handle a pair of ANSI escape
      sequences that open before a carriage return and close after the last
      carriage return in a linefeed delimited string; the resulting string will
      contain only the closing end of the ANSI escape sequence pair. Tracking
      this kind of complexity requires a state machine and proper parsing.

    .. _capturer: https://pypi.org/project/capturer
    .. _coloredlogs: https://pypi.org/project/coloredlogs
    """
    cleaned_lines = []
    current_line = ''
    current_position = 0
# WARNING: Decompyle incomplete


def connected_to_terminal(stream = (None,)):
    '''
    Check if a stream is connected to a terminal.

    :param stream: The stream to check (a file-like object,
                   defaults to :data:`sys.stdout`).
    :returns: :data:`True` if the stream is connected to a terminal,
              :data:`False` otherwise.

    See also :func:`terminal_supports_colors()`.
    '''
    pass
# WARNING: Decompyle incomplete

enable_ansi_support = (lambda : if have_windows_native_ansi_support():
import ctypesctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-12), 7)Trueif None():
if 'ANSICON' in os.environ:
Truetry:
import coloramacolorama.init()Trueexcept ImportError:
Falseconnected_to_terminal())()

def find_terminal_size():
    """
    Determine the number of lines and columns visible in the terminal.

    :returns: A tuple of two integers with the line and column count.

    The result of this function is based on the first of the following three
    methods that works:

    1. First :func:`find_terminal_size_using_ioctl()` is tried,
    2. then :func:`find_terminal_size_using_stty()` is tried,
    3. finally :data:`DEFAULT_LINES` and :data:`DEFAULT_COLUMNS` are returned.

    .. note:: The :func:`find_terminal_size()` function performs the steps
              above every time it is called, the result is not cached. This is
              because the size of a virtual terminal can change at any time and
              the result of :func:`find_terminal_size()` should be correct.

              `Pre-emptive snarky comment`_: It's possible to cache the result
              of this function and use :mod:`signal.SIGWINCH <signal>` to
              refresh the cached values!

              Response: As a library I don't consider it the role of the
              :mod:`humanfriendly.terminal` module to install a process wide
              signal handler ...

    .. _Pre-emptive snarky comment: http://blogs.msdn.com/b/oldnewthing/archive/2008/01/30/7315957.aspx
    """
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        result = find_terminal_size_using_ioctl(stream)
        if min(result) >= 1:
            
            return None, result
        except Exception:
            continue
        
        try:
            if min(result) >= 1:
                return result
        except Exception:
            pass

        return (DEFAULT_LINES, DEFAULT_COLUMNS)


def find_terminal_size_using_ioctl(stream):
    """
    Find the terminal size using :func:`fcntl.ioctl()`.

    :param stream: A stream connected to the terminal (a file object with a
                   ``fileno`` attribute).
    :returns: A tuple of two integers with the line and column count.
    :raises: This function can raise exceptions but I'm not going to document
             them here, you should be using :func:`find_terminal_size()`.

    Based on an `implementation found on StackOverflow <http://stackoverflow.com/a/3010495/788200>`_.
    """
    if not HAVE_IOCTL:
        raise NotImplementedError("It looks like the `fcntl' module is not available!")
    (h, w, hp, wp) = struct.unpack('HHHH', fcntl.ioctl(stream, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return (h, w)


def find_terminal_size_using_stty():
    """
    Find the terminal size using the external command ``stty size``.

    :param stream: A stream connected to the terminal (a file object).
    :returns: A tuple of two integers with the line and column count.
    :raises: This function can raise exceptions but I'm not going to document
             them here, you should be using :func:`find_terminal_size()`.
    """
    stty = subprocess.Popen([
        'stty',
        'size'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    (stdout, stderr) = stty.communicate()
    tokens = stdout.split()
    if len(tokens) != 2:
        raise Exception("Invalid output from `stty size'!")
    return tuple(map(int, tokens))


def get_pager_command(text = (None,)):
    """
    Get the command to show a text on the terminal using a pager.

    :param text: The text to print to the terminal (a string).
    :returns: A list of strings with the pager command and arguments.

    The use of a pager helps to avoid the wall of text effect where the user
    has to scroll up to see where the output began (not very user friendly).

    If the given text contains ANSI escape sequences the command ``less
    --RAW-CONTROL-CHARS`` is used, otherwise the environment variable
    ``$PAGER`` is used (if ``$PAGER`` isn't set :man:`less` is used).

    When the selected pager is :man:`less`, the following options are used to
    make the experience more user friendly:

    - ``--quit-if-one-screen`` causes :man:`less` to automatically exit if the
      entire text can be displayed on the first screen. This makes the use of a
      pager transparent for smaller texts (because the operator doesn't have to
      quit the pager).

    - ``--no-init`` prevents :man:`less` from clearing the screen when it
      exits. This ensures that the operator gets a chance to review the text
      (for example a usage message) after quitting the pager, while composing
      the next command.
    """
    if text and ANSI_CSI in text:
        command_line = [
            'less',
            '--RAW-CONTROL-CHARS']
    else:
        command_line = [
            os.environ.get('PAGER', 'less')]
    if os.path.basename(command_line[0]) == 'less':
        command_line.append('--no-init')
        command_line.append('--quit-if-one-screen')
    return command_line

have_windows_native_ansi_support = (lambda :
