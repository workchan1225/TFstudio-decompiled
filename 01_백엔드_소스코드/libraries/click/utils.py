# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
import re
import sys
import typing as t
from functools import update_wrapper
from types import ModuleType
from types import TracebackType
from _compat import _default_text_stderr
from _compat import _default_text_stdout
from _compat import _find_binary_writer
from _compat import auto_wrap_for_ansi
from _compat import binary_streams
from _compat import open_stream
from _compat import should_strip_ansi
from _compat import strip_ansi
from _compat import text_streams
from _compat import WIN
from globals import resolve_color_default
if t.TYPE_CHECKING:
    import typing_extensions as te
    P = te.ParamSpec('P')
R = t.TypeVar('R')

def _posixify(name = None):
    return '-'.join(name.split()).lower()


def safecall(func = None):
    '''Wraps a function so that it swallows exceptions.'''
    pass
# WARNING: Decompyle incomplete


def make_str(value = None):
    '''Converts a value into a valid string.'''
    if isinstance(value, bytes):
        
        try:
            return value.decode(sys.getfilesystemencoding())
        except UnicodeError:
            return 
            return str(value)



def make_default_short_help(help = None, max_length = None):
    '''Returns a condensed version of help string.'''
    paragraph_end = help.find('\n\n')
    if paragraph_end != -1:
        help = help[:paragraph_end]
    words = help.split()
    if not words:
        return ''
    if None[0] == '\x08':
        words = words[1:]
    total_length = 0
    last_index = len(words) - 1
# WARNING: Decompyle incomplete


class LazyFile:
    '''A lazy file works like a regular file but it does not fully open
    the file but it does perform some basic checks early to see if the
    filename parameter does make sense.  This is useful for safely opening
    files for writing.
    '''
    
    def __init__(self, filename = None, mode = None, encoding = None, errors = ('r', None, 'strict', False), atomic = ('filename', t.Union[(str, 'os.PathLike[str]')], 'mode', str, 'encoding', t.Optional[str], 'errors', t.Optional[str], 'atomic', bool)):
        self.name = os.fspath(filename)
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.atomic = atomic
        self
        self
        if self.name == '-':
            (self._f, self.should_close) = open_stream(filename, mode, encoding, errors)
            return None
        if None in mode:
            open(filename, mode).close()
        self._f = None
        self.should_close = True

    
    def __getattr__(self = None, name = None):
        return getattr(self.open(), name)

    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def open(self = None):
        """Opens the file if it's not yet open.  This call might fail with
        a :exc:`FileError`.  Not handling this error will produce an error
        that Click shows.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        '''Closes the underlying file, no matter what.'''
        pass
    # WARNING: Decompyle incomplete

    
    def close_intelligently(self = None):
        '''This function only closes the file if it was opened by the lazy
        file wrapper.  For instance this will never close stdin.
        '''
        if self.should_close:
            self.close()
            return None

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', t.Optional[t.Type[BaseException]], 'exc_value', t.Optional[BaseException], 'tb', t.Optional[TracebackType], 'return', None)):
        self.close_intelligently()

    
    def __iter__(self = None):
        self.open()
        return iter(self._f)



class KeepOpenFile:
    
    def __init__(self = None, file = None):
        self._file = file

    
    def __getattr__(self = None, name = None):
        return getattr(self._file, name)

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', t.Optional[t.Type[BaseException]], 'exc_value', t.Optional[BaseException], 'tb', t.Optional[TracebackType], 'return', None)):
        pass

    
    def __repr__(self = None):
        return repr(self._file)

    
    def __iter__(self = None):
        return iter(self._file)



def echo(message = None, file = None, nl = None, err = (None, None, True, False, None), color = ('message', t.Optional[t.Any], 'file', t.Optional[t.IO[t.Any]], 'nl', bool, 'err', bool, 'color', t.Optional[bool], 'return', None)):
    '''Print a message and newline to stdout or a file. This should be
    used instead of :func:`print` because it provides better support
    for different data, files, and environments.

    Compared to :func:`print`, this does the following:

    -   Ensures that the output encoding is not misconfigured on Linux.
    -   Supports Unicode in the Windows console.
    -   Supports writing to binary outputs, and supports writing bytes
        to text outputs.
    -   Supports colors and styles on Windows.
    -   Removes ANSI color and style codes if the output does not look
        like an interactive terminal.
    -   Always flushes the output.

    :param message: The string or bytes to output. Other objects are
        converted to strings.
    :param file: The file to write to. Defaults to ``stdout``.
    :param err: Write to ``stderr`` instead of ``stdout``.
    :param nl: Print a newline after the message. Enabled by default.
    :param color: Force showing or hiding colors and other styles. By
        default Click will remove color if the output does not look like
        an interactive terminal.

    .. versionchanged:: 6.0
        Support Unicode output on the Windows console. Click does not
        modify ``sys.stdout``, so ``sys.stdout.write()`` and ``print()``
        will still not support Unicode.

    .. versionchanged:: 4.0
        Added the ``color`` parameter.

    .. versionadded:: 3.0
        Added the ``err`` parameter.

    .. versionchanged:: 2.0
        Support colors on Windows if colorama is installed.
    '''
    pass
# WARNING: Decompyle incomplete


def get_binary_stream(name = None):
    """Returns a system stream for byte processing.

    :param name: the name of the stream to open.  Valid names are ``'stdin'``,
                 ``'stdout'`` and ``'stderr'``
    """
    opener = binary_streams.get(name)
# WARNING: Decompyle incomplete


def get_text_stream(name = None, encoding = None, errors = None):
    """Returns a system stream for text processing.  This usually returns
    a wrapped stream around a binary stream returned from
    :func:`get_binary_stream` but it also can take shortcuts for already
    correctly configured streams.

    :param name: the name of the stream to open.  Valid names are ``'stdin'``,
                 ``'stdout'`` and ``'stderr'``
    :param encoding: overrides the detected default encoding.
    :param errors: overrides the default error mode.
    """
    opener = text_streams.get(name)
# WARNING: Decompyle incomplete


def open_file(filename, mode = None, encoding = None, errors = None, lazy = ('r', None, 'strict', False, False), atomic = ('filename', t.Union[(str, 'os.PathLike[str]')], 'mode', str, 'encoding', t.Optional[str], 'errors', t.Optional[str], 'lazy', bool, 'atomic', bool, 'return', t.IO[t.Any])):
    """Open a file, with extra behavior to handle ``'-'`` to indicate
    a standard stream, lazy open on write, and atomic write. Similar to
    the behavior of the :class:`~click.File` param type.

    If ``'-'`` is given to open ``stdout`` or ``stdin``, the stream is
    wrapped so that using it in a context manager will not close it.
    This makes it possible to use the function without accidentally
    closing a standard stream:

    .. code-block:: python

        with open_file(filename) as f:
            ...

    :param filename: The name or Path of the file to open, or ``'-'`` for
        ``stdin``/``stdout``.
    :param mode: The mode in which to open the file.
    :param encoding: The encoding to decode or encode a file opened in
        text mode.
    :param errors: The error handling mode.
    :param lazy: Wait to open the file until it is accessed. For read
        mode, the file is temporarily opened to raise access errors
        early, then closed until it is read again.
    :param atomic: Write to a temporary file and replace the given file
        on close.

    .. versionadded:: 3.0
    """
    if lazy:
        return t.cast(t.IO[t.Any], LazyFile(filename, mode, encoding, errors, atomic = atomic))
    (f, should_close) = None(filename, mode, encoding, errors, atomic = atomic)
    if not should_close:
        f = t.cast(t.IO[t.Any], KeepOpenFile(f))
    return f


def format_filename(filename = None, shorten = None):
    '''Format a filename as a string for display. Ensures the filename can be
    displayed by replacing any invalid bytes or surrogate escapes in the name
    with the replacement character ``�``.

    Invalid bytes or surrogate escapes will raise an error when written to a
    stream with ``errors="strict"``. This will typically happen with ``stdout``
    when the locale is something like ``en_GB.UTF-8``.

    Many scenarios *are* safe to write surrogates though, due to PEP 538 and
    PEP 540, including:

    -   Writing to ``stderr``, which uses ``errors="backslashreplace"``.
    -   The system has ``LANG=C.UTF-8``, ``C``, or ``POSIX``. Python opens
        stdout and stderr with ``errors="surrogateescape"``.
    -   None of ``LANG/LC_*`` are set. Python assumes ``LANG=C.UTF-8``.
    -   Python is started in UTF-8 mode  with  ``PYTHONUTF8=1`` or ``-X utf8``.
        Python opens stdout and stderr with ``errors="surrogateescape"``.

    :param filename: formats a filename for UI display.  This will also convert
                     the filename into unicode without failing.
    :param shorten: this optionally shortens the filename to strip of the
                    path that leads up to it.
    '''
    if shorten:
        filename = os.path.basename(filename)
    else:
        filename = os.fspath(filename)
    if isinstance(filename, bytes):
        filename = filename.decode(sys.getfilesystemencoding(), 'replace')
    else:
        filename = filename.encode('utf-8', 'surrogateescape').decode('utf-8', 'replace')
    return filename


def get_app_dir(app_name = None, roaming = None, force_posix = None):
    '''Returns the config folder for the application.  The default behavior
    is to return whatever is most appropriate for the operating system.

    To give you an idea, for an app called ``"Foo Bar"``, something like
    the following folders could be returned:

    Mac OS X:
      ``~/Library/Application Support/Foo Bar``
    Mac OS X (POSIX):
      ``~/.foo-bar``
    Unix:
      ``~/.config/foo-bar``
    Unix (POSIX):
      ``~/.foo-bar``
    Windows (roaming):
      ``C:\\Users\\<user>\\AppData\\Roaming\\Foo Bar``
    Windows (not roaming):
      ``C:\\Users\\<user>\\AppData\\Local\\Foo Bar``

    .. versionadded:: 2.0

    :param app_name: the application name.  This should be properly capitalized
                     and can contain whitespace.
    :param roaming: controls if the folder should be roaming or not on Windows.
                    Has no effect otherwise.
    :param force_posix: if this is set to `True` then on any POSIX system the
                        folder will be stored in the home folder with a leading
                        dot instead of the XDG config home or darwin\'s
                        application support folder.
    '''
    pass
# WARNING: Decompyle incomplete


class PacifyFlushWrapper:
    '''This wrapper is used to catch and suppress BrokenPipeErrors resulting
    from ``.flush()`` being called on broken pipe during the shutdown/final-GC
    of the Python interpreter. Notably ``.flush()`` is always called on
    ``sys.stdout`` and ``sys.stderr``. So as to have minimal impact on any
    other cleanup code, and the case where the underlying file is not a broken
    pipe, all calls and attributes are proxied.
    '''
    
    def __init__(self = None, wrapped = None):
        self.wrapped = wrapped

    
    def flush(self = None):
        
        try:
            self.wrapped.flush()
            return None
        except OSError:
            e = None
            import errno
            if e.errno != errno.EPIPE:
                raise 
            e = None
            del e
            return None
            e = None
            del e


    
    def __getattr__(self = None, attr = None):
        return getattr(self.wrapped, attr)



def _detect_program_name(path = None, _main = None):
    """Determine the command used to run the program, for use in help
    text. If a file or entry point was executed, the file name is
    returned. If ``python -m`` was used to execute a module or package,
    ``python -m name`` is returned.

    This doesn't try to be too precise, the goal is to give a concise
    name for help text. Files are only shown as their name without the
    path. ``python`` is only shown for modules, and the full path to
    ``sys.executable`` is not shown.

    :param path: The Python file being executed. Python puts this in
        ``sys.argv[0]``, which is used by default.
    :param _main: The ``__main__`` module. This should only be passed
        during internal testing.

    .. versionadded:: 8.0
        Based on command args detection in the Werkzeug reloader.

    :meta private:
    """
    pass
# WARNING: Decompyle incomplete


def _expand_args(args = None, *, user, env, glob_recursive):
    '''Simulate Unix shell expansion with Python functions.

    See :func:`glob.glob`, :func:`os.path.expanduser`, and
    :func:`os.path.expandvars`.

    This is intended for use on Windows, where the shell does not do any
    expansion. It may not exactly match what a Unix shell would do.

    :param args: List of command line arguments to expand.
    :param user: Expand user home directory.
    :param env: Expand environment variables.
    :param glob_recursive: ``**`` matches directories recursively.

    .. versionchanged:: 8.1
        Invalid glob patterns are treated as empty expansions rather
        than raising an error.

    .. versionadded:: 8.0

    :meta private:
    '''
    glob = glob
    import glob
    out = []
    for arg in args:
        if user:
            arg = os.path.expanduser(arg)
        if env:
            arg = os.path.expandvars(arg)
        matches = glob(arg, recursive = glob_recursive)
    except re.error:
        matches = []
    if not matches:
        out.append(arg)
        continue
    out.extend(matches)
    continue
    return out
