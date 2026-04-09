# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Colored terminal output for Python\'s :mod:`logging` module.

.. contents::
   :local:

Getting started
===============

The easiest way to get started is by importing :mod:`coloredlogs` and calling
:mod:`coloredlogs.install()` (similar to :func:`logging.basicConfig()`):

 >>> import coloredlogs, logging
 >>> coloredlogs.install(level=\'DEBUG\')
 >>> logger = logging.getLogger(\'some.module.name\')
 >>> logger.info("this is an informational message")
 2015-10-22 19:13:52 peter-macbook some.module.name[28036] INFO this is an informational message

The :mod:`~coloredlogs.install()` function creates a :class:`ColoredFormatter`
that injects `ANSI escape sequences`_ into the log output.

.. _ANSI escape sequences: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

Environment variables
=====================

The following environment variables can be used to configure the
:mod:`coloredlogs` module without writing any code:

=============================  ============================  ==================================
Environment variable           Default value                 Type of value
=============================  ============================  ==================================
``$COLOREDLOGS_AUTO_INSTALL``  \'false\'                       a boolean that controls whether
                                                             :func:`auto_install()` is called
``$COLOREDLOGS_LOG_LEVEL``     \'INFO\'                        a log level name
``$COLOREDLOGS_LOG_FORMAT``    :data:`DEFAULT_LOG_FORMAT`    a log format string
``$COLOREDLOGS_DATE_FORMAT``   :data:`DEFAULT_DATE_FORMAT`   a date/time format string
``$COLOREDLOGS_LEVEL_STYLES``  :data:`DEFAULT_LEVEL_STYLES`  see :func:`parse_encoded_styles()`
``$COLOREDLOGS_FIELD_STYLES``  :data:`DEFAULT_FIELD_STYLES`  see :func:`parse_encoded_styles()`
=============================  ============================  ==================================

If the environment variable `$NO_COLOR`_ is set (the value doesn\'t matter, even
an empty string will do) then :func:`coloredlogs.install()` will take this as a
hint that colors should not be used (unless the ``isatty=True`` override was
passed by the caller).

.. _$NO_COLOR: https://no-color.org/

Examples of customization
=========================

Here we\'ll take a look at some examples of how you can customize
:mod:`coloredlogs` using environment variables.

.. contents::
   :local:

About the defaults
------------------

Here\'s a screen shot of the default configuration for easy comparison with the
screen shots of the following customizations (this is the same screen shot that
is shown in the introduction):

.. image:: images/defaults.png
   :alt: Screen shot of colored logging with defaults.

The screen shot above was taken from ``urxvt`` which doesn\'t support faint text
colors, otherwise the color of green used for `debug` messages would have
differed slightly from the color of green used for `spam` messages.

Apart from the `faint` style of the `spam` level, the default configuration of
`coloredlogs` sticks to the eight color palette defined by the original ANSI
standard, in order to provide a somewhat consistent experience across terminals
and terminal emulators.

Available text styles and colors
--------------------------------

Of course you are free to customize the default configuration, in this case you
can use any text style or color that you know is supported by your terminal.
You can use the ``humanfriendly --demo`` command to try out the supported text
styles and colors:

.. image:: http://humanfriendly.readthedocs.io/en/latest/_images/ansi-demo.png
   :alt: Screen shot of the \'humanfriendly --demo\' command.

Changing the log format
-----------------------

The simplest customization is to change the log format, for example:

.. literalinclude:: examples/custom-log-format.txt
   :language: console

Here\'s what that looks like in a terminal (I always work in terminals with a
black background and white text):

.. image:: images/custom-log-format.png
   :alt: Screen shot of colored logging with custom log format.

Changing the date/time format
-----------------------------

You can also change the date/time format, for example you can remove the date
part and leave only the time:

.. literalinclude:: examples/custom-datetime-format.txt
   :language: console

Here\'s what it looks like in a terminal:

.. image:: images/custom-datetime-format.png
   :alt: Screen shot of colored logging with custom date/time format.

Changing the colors/styles
--------------------------

Finally you can customize the colors and text styles that are used:

.. literalinclude:: examples/custom-colors.txt
   :language: console

Here\'s an explanation of the features used here:

- The numbers used in ``$COLOREDLOGS_LEVEL_STYLES`` demonstrate the use of 256
  color mode (the numbers refer to the 256 color mode palette which is fixed).

- The `success` level demonstrates the use of a text style (bold).

- The `critical` level demonstrates the use of a background color (red).

Of course none of this can be seen in the shell transcript quoted above, but
take a look at the following screen shot:

.. image:: images/custom-colors.png
   :alt: Screen shot of colored logging with custom colors.

.. _notes about log levels:

Some notes about log levels
===========================

With regards to the handling of log levels, the :mod:`coloredlogs` package
differs from Python\'s :mod:`logging` module in two aspects:

1. While the :mod:`logging` module uses the default logging level
   :data:`logging.WARNING`, the :mod:`coloredlogs` package has always used
   :data:`logging.INFO` as its default log level.

2. When logging to the terminal or system log is initialized by
   :func:`install()` or :func:`.enable_system_logging()` the effective
   level [#]_ of the selected logger [#]_ is compared against the requested
   level [#]_ and if the effective level is more restrictive than the requested
   level, the logger\'s level will be set to the requested level (this happens
   in :func:`adjust_level()`). The reason for this is to work around a
   combination of design choices in Python\'s :mod:`logging` module that can
   easily confuse people who aren\'t already intimately familiar with it:

   - All loggers are initialized with the level :data:`logging.NOTSET`.

   - When a logger\'s level is set to :data:`logging.NOTSET` the
     :func:`~logging.Logger.getEffectiveLevel()` method will
     fall back to the level of the parent logger.

   - The parent of all loggers is the root logger and the root logger has its
     level set to :data:`logging.WARNING` by default (after importing the
     :mod:`logging` module).

   Effectively all user defined loggers inherit the default log level
   :data:`logging.WARNING` from the root logger, which isn\'t very intuitive for
   those who aren\'t already familiar with the hierarchical nature of the
   :mod:`logging` module.

   By avoiding this potentially confusing behavior (see `#14`_, `#18`_, `#21`_,
   `#23`_ and `#24`_), while at the same time allowing the caller to specify a
   logger object, my goal and hope is to provide sane defaults that can easily
   be changed when the need arises.

   .. [#] Refer to :func:`logging.Logger.getEffectiveLevel()` for details.
   .. [#] The logger that is passed as an argument by the caller or the root
          logger which is selected as a default when no logger is provided.
   .. [#] The log level that is passed as an argument by the caller or the
          default log level :data:`logging.INFO` when no level is provided.

   .. _#14: https://github.com/xolox/python-coloredlogs/issues/14
   .. _#18: https://github.com/xolox/python-coloredlogs/issues/18
   .. _#21: https://github.com/xolox/python-coloredlogs/pull/21
   .. _#23: https://github.com/xolox/python-coloredlogs/pull/23
   .. _#24: https://github.com/xolox/python-coloredlogs/issues/24

Classes and functions
=====================
'''
import collections
import logging
import os
import re
import socket
import sys
from humanfriendly import coerce_boolean
from humanfriendly.compat import coerce_string, is_string, on_windows
from humanfriendly.terminal import ANSI_COLOR_CODES, ansi_wrap, enable_ansi_support, terminal_supports_colors
from humanfriendly.text import format, split
__version__ = '15.0.1'
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = '%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
CHROOT_FILES = [
    '/etc/debian_chroot']
DEFAULT_FIELD_STYLES = dict(asctime = dict(color = 'green'), hostname = dict(color = 'magenta'), levelname = dict(color = 'black', bold = True), name = dict(color = 'blue'), programname = dict(color = 'cyan'), username = dict(color = 'yellow'))
DEFAULT_LEVEL_STYLES = dict(spam = dict(color = 'green', faint = True), debug = dict(color = 'green'), verbose = dict(color = 'blue'), info = dict(), notice = dict(color = 'magenta'), warning = dict(color = 'yellow'), success = dict(color = 'green', bold = True), error = dict(color = 'red'), critical = dict(color = 'red', bold = True))
DEFAULT_FORMAT_STYLE = '%'
FORMAT_STYLE_PATTERNS = {
    '%': '%\\((\\w+)\\)[#0 +-]*\\d*(?:\\.\\d+)?[hlL]?[diouxXeEfFgGcrs%]',
    '{': '{(\\w+)[^}]*}',
    '$': '\\$(\\w+)|\\${(\\w+)}' }

def auto_install():
    '''
    Automatically call :func:`install()` when ``$COLOREDLOGS_AUTO_INSTALL`` is set.

    The `coloredlogs` package includes a `path configuration file`_ that
    automatically imports the :mod:`coloredlogs` module and calls
    :func:`auto_install()` when the environment variable
    ``$COLOREDLOGS_AUTO_INSTALL`` is set.

    This function uses :func:`~humanfriendly.coerce_boolean()` to check whether
    the value of ``$COLOREDLOGS_AUTO_INSTALL`` should be considered :data:`True`.

    .. _path configuration file: https://docs.python.org/2/library/site.html#module-site
    '''
    if coerce_boolean(os.environ.get('COLOREDLOGS_AUTO_INSTALL', 'false')):
        install()
        return None


def install(level = (None,), **kw):
    """
    Enable colored terminal output for Python's :mod:`logging` module.

    :param level: The default logging level (an integer or a string with a
                  level name, defaults to :data:`DEFAULT_LOG_LEVEL`).
    :param logger: The logger to which the stream handler should be attached (a
                   :class:`~logging.Logger` object, defaults to the root logger).
    :param fmt: Set the logging format (a string like those accepted by
                :class:`~logging.Formatter`, defaults to
                :data:`DEFAULT_LOG_FORMAT`).
    :param datefmt: Set the date/time format (a string, defaults to
                    :data:`DEFAULT_DATE_FORMAT`).
    :param style: One of the characters ``%``, ``{`` or ``$`` (defaults to
                  :data:`DEFAULT_FORMAT_STYLE`). See the documentation of the
                  :class:`python3:logging.Formatter` class in Python 3.2+. On
                  older Python versions only ``%`` is supported.
    :param milliseconds: :data:`True` to show milliseconds like :mod:`logging`
                         does by default, :data:`False` to hide milliseconds
                         (the default is :data:`False`, see `#16`_).
    :param level_styles: A dictionary with custom level styles (defaults to
                         :data:`DEFAULT_LEVEL_STYLES`).
    :param field_styles: A dictionary with custom field styles (defaults to
                         :data:`DEFAULT_FIELD_STYLES`).
    :param stream: The stream where log messages should be written to (a
                   file-like object). This defaults to :data:`None` which
                   means :class:`StandardErrorHandler` is used.
    :param isatty: :data:`True` to use a :class:`ColoredFormatter`,
                   :data:`False` to use a normal :class:`~logging.Formatter`
                   (defaults to auto-detection using
                   :func:`~humanfriendly.terminal.terminal_supports_colors()`).
    :param reconfigure: If :data:`True` (the default) multiple calls to
                        :func:`coloredlogs.install()` will each override
                        the previous configuration.
    :param use_chroot: Refer to :class:`HostNameFilter`.
    :param programname: Refer to :class:`ProgramNameFilter`.
    :param username: Refer to :class:`UserNameFilter`.
    :param syslog: If :data:`True` then :func:`.enable_system_logging()` will
                   be called without arguments (defaults to :data:`False`). The
                   `syslog` argument may also be a number or string, in this
                   case it is assumed to be a logging level which is passed on
                   to :func:`.enable_system_logging()`.

    The :func:`coloredlogs.install()` function is similar to
    :func:`logging.basicConfig()`, both functions take a lot of optional
    keyword arguments but try to do the right thing by default:

    1. If `reconfigure` is :data:`True` (it is by default) and an existing
       :class:`~logging.StreamHandler` is found that is connected to either
       :data:`~sys.stdout` or :data:`~sys.stderr` the handler will be removed.
       This means that first calling :func:`logging.basicConfig()` and then
       calling :func:`coloredlogs.install()` will replace the stream handler
       instead of adding a duplicate stream handler. If `reconfigure` is
       :data:`False` and an existing handler is found no further steps are
       taken (to avoid installing a duplicate stream handler).

    2. A :class:`~logging.StreamHandler` is created and connected to the stream
       given by the `stream` keyword argument (:data:`sys.stderr` by
       default). The stream handler's level is set to the value of the `level`
       keyword argument.

    3. A :class:`ColoredFormatter` is created if the `isatty` keyword argument
       allows it (or auto-detection allows it), otherwise a normal
       :class:`~logging.Formatter` is created. The formatter is initialized
       with the `fmt` and `datefmt` keyword arguments (or their computed
       defaults).

       The environment variable ``$NO_COLOR`` is taken as a hint by
       auto-detection that colors should not be used.

    4. :func:`HostNameFilter.install()`, :func:`ProgramNameFilter.install()`
       and :func:`UserNameFilter.install()` are called to enable the use of
       additional fields in the log format.

    5. If the logger's level is too restrictive it is relaxed (refer to `notes
       about log levels`_ for details).

    6. The formatter is added to the handler and the handler is added to the
       logger.

    .. _#16: https://github.com/xolox/python-coloredlogs/issues/16
    """
    pass
# WARNING: Decompyle incomplete


def check_style(value):
    """
    Validate a logging format style.

    :param value: The logging format style to validate (any value).
    :returns: The logging format character (a string of one character).
    :raises: :exc:`~exceptions.ValueError` when the given style isn't supported.

    On Python 3.2+ this function accepts the logging format styles ``%``, ``{``
    and ``$`` while on older versions only ``%`` is accepted (because older
    Python versions don't support alternative logging format styles).
    """
    if sys.version_info[:2] >= (3, 2):
        if value not in FORMAT_STYLE_PATTERNS:
            msg = 'Unsupported logging format style! (%r)'
            raise ValueError(format(msg, value))
    elif value != DEFAULT_FORMAT_STYLE:
        msg = 'Format string styles other than %r require Python 3.2+!'
        raise ValueError(msg, DEFAULT_FORMAT_STYLE)
    return value


def increase_verbosity():
    '''
    Increase the verbosity of the root handler by one defined level.

    Understands custom logging levels like defined by my ``verboselogs``
    module.
    '''
    defined_levels = sorted(set(find_defined_levels().values()))
    current_index = defined_levels.index(get_level())
    selected_index = max(0, current_index - 1)
    set_level(defined_levels[selected_index])


def decrease_verbosity():
    '''
    Decrease the verbosity of the root handler by one defined level.

    Understands custom logging levels like defined by my ``verboselogs``
    module.
    '''
    defined_levels = sorted(set(find_defined_levels().values()))
    current_index = defined_levels.index(get_level())
    selected_index = min(current_index + 1, len(defined_levels) - 1)
    set_level(defined_levels[selected_index])


def is_verbose():
    '''
    Check whether the log level of the root handler is set to a verbose level.

    :returns: ``True`` if the root handler is verbose, ``False`` if not.
    '''
    return get_level() < DEFAULT_LOG_LEVEL


def get_level():
    '''
    Get the logging level of the root handler.

    :returns: The logging level of the root handler (an integer) or
              :data:`DEFAULT_LOG_LEVEL` (if no root handler exists).
    '''
    (handler, logger) = find_handler(logging.getLogger(), match_stream_handler)
    return handler.level if handler else DEFAULT_LOG_LEVEL


def set_level(level):
    '''
    Set the logging level of the root handler.

    :param level: The logging level to filter on (an integer or string).

    If no root handler exists yet this automatically calls :func:`install()`.
    '''
    (handler, logger) = find_handler(logging.getLogger(), match_stream_handler)
    if handler and logger:
        handler.setLevel(level_to_number(level))
        adjust_level(logger, level)
        return None
    None(level = level)


def adjust_level(logger, level):
    '''
    Increase a logger\'s verbosity up to the requested level.

    :param logger: The logger to change (a :class:`~logging.Logger` object).
    :param level: The log level to enable (a string or number).

    This function is used by functions like :func:`install()`,
    :func:`increase_verbosity()` and :func:`.enable_system_logging()` to adjust
    a logger\'s level so that log messages up to the requested log level are
    propagated to the configured output handler(s).

    It uses :func:`logging.Logger.getEffectiveLevel()` to check whether
    `logger` propagates or swallows log messages of the requested `level` and
    sets the logger\'s level to the requested level if it would otherwise
    swallow log messages.

    Effectively this function will "widen the scope of logging" when asked to
    do so but it will never "narrow the scope of logging". This is because I am
    convinced that filtering of log messages should (primarily) be decided by
    handlers.
    '''
    level = level_to_number(level)
    if logger.getEffectiveLevel() > level:
        logger.setLevel(level)
        return None


def find_defined_levels():
    """
    Find the defined logging levels.

    :returns: A dictionary with level names as keys and integers as values.

    Here's what the result looks like by default (when
    no custom levels or level names have been defined):

    >>> find_defined_levels()
    {'NOTSET': 0,
     'DEBUG': 10,
     'INFO': 20,
     'WARN': 30,
     'WARNING': 30,
     'ERROR': 40,
     'FATAL': 50,
     'CRITICAL': 50}
    """
    defined_levels = { }
    for name in dir(logging):
        if name.isupper():
            value = getattr(logging, name)
            if isinstance(value, int):
                defined_levels[name] = value
        return defined_levels


def level_to_number(value):
    '''
    Coerce a logging level name to a number.

    :param value: A logging level (integer or string).
    :returns: The number of the log level (an integer).

    This function translates log level names into their numeric values..
    '''
    if is_string(value):
        
        try:
            defined_levels = find_defined_levels()
            value = defined_levels[value.upper()]
        except KeyError:
            value = DEFAULT_LOG_LEVEL

        return value


def find_level_aliases():
    """
    Find log level names which are aliases of each other.

    :returns: A dictionary that maps aliases to their canonical name.

    .. note:: Canonical names are chosen to be the alias with the longest
              string length so that e.g. ``WARN`` is an alias for ``WARNING``
              instead of the other way around.

    Here's what the result looks like by default (when
    no custom levels or level names have been defined):

    >>> from coloredlogs import find_level_aliases
    >>> find_level_aliases()
    {'WARN': 'WARNING', 'FATAL': 'CRITICAL'}
    """
    mapping = collections.defaultdict(list)
    for name, value in find_defined_levels().items():
        mapping[value].append(name)
        aliases = { }
        for value, names in mapping.items():
            if len(names) > 1:
                names = sorted(names, key = (lambda n: len(n)))
                canonical_name = names.pop()
                for alias in names:
                    aliases[alias] = canonical_name
                    return aliases


def parse_encoded_styles(text, normalize_key = (None,)):
    """
    Parse text styles encoded in a string into a nested data structure.

    :param text: The encoded styles (a string).
    :returns: A dictionary in the structure of the :data:`DEFAULT_FIELD_STYLES`
              and :data:`DEFAULT_LEVEL_STYLES` dictionaries.

    Here's an example of how this function works:

    >>> from coloredlogs import parse_encoded_styles
    >>> from pprint import pprint
    >>> encoded_styles = 'debug=green;warning=yellow;error=red;critical=red,bold'
    >>> pprint(parse_encoded_styles(encoded_styles))
    {'debug': {'color': 'green'},
     'warning': {'color': 'yellow'},
     'error': {'color': 'red'},
     'critical': {'bold': True, 'color': 'red'}}
    """
    parsed_styles = { }
    for assignment in split(text, ';'):
        (name, _, styles) = assignment.partition('=')
        target = parsed_styles.setdefault(name, { })
        for token in split(styles, ','):
            if token.isdigit():
                target['color'] = int(token)
                continue
            if token in ANSI_COLOR_CODES:
                target['color'] = token
                continue
            if '=' in token:
                (name, _, value) = token.partition('=')
                if name in ('color', 'background'):
                    if value.isdigit():
                        target[name] = int(value)
                        continue
                    if value in ANSI_COLOR_CODES:
                        target[name] = value
                continue
            target[token] = True
            return parsed_styles


def find_hostname(use_chroot = (True,)):
    '''
    Find the host name to include in log messages.

    :param use_chroot: Use the name of the chroot when inside a chroot?
                       (boolean, defaults to :data:`True`)
    :returns: A suitable host name (a string).

    Looks for :data:`CHROOT_FILES` that have a nonempty first line (taken to be
    the chroot name). If none are found then :func:`socket.gethostname()` is
    used as a fall back.
    '''
    for chroot_file in CHROOT_FILES:
        handle = open(chroot_file)
        first_line = next(handle)
        name = first_line.strip()
        if name:
            None(None, None)
            
            return None, name, 
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        continue
    return socket.gethostname()


def find_program_name():
    """
    Select a suitable program name to embed in log messages.

    :returns: One of the following strings (in decreasing order of preference):

              1. The base name of the currently running Python program or
                 script (based on the value at index zero of :data:`sys.argv`).
              2. The base name of the Python executable (based on
                 :data:`sys.executable`).
              3. The string 'python'.
    """
    if sys.argv and sys.argv[0] != '-c':
        pass
    elif '' or sys.executable:
        pass
    elif not '':
        return 'python'


def find_username():
    '''
    Find the username to include in log messages.

    :returns: A suitable username (a string).

    On UNIX systems this uses the :mod:`pwd` module which means ``root`` will
    be reported when :man:`sudo` is used (as it should). If this fails (for
    example on Windows) then :func:`getpass.getuser()` is used as a fall back.
    '''
    
    try:
        import pwd
        uid = os.getuid()
        entry = pwd.getpwuid(uid)
        return entry.pw_name
    except Exception:
        import getpass
        return 



def replace_handler(logger, match_handler, reconfigure):
    '''
    Prepare to replace a handler.

    :param logger: Refer to :func:`find_handler()`.
    :param match_handler: Refer to :func:`find_handler()`.
    :param reconfigure: :data:`True` if an existing handler should be replaced,
                        :data:`False` otherwise.
    :returns: A tuple of two values:

              1. The matched :class:`~logging.Handler` object or :data:`None`
                 if no handler was matched.
              2. The :class:`~logging.Logger` to which the matched handler was
                 attached or the logger given to :func:`replace_handler()`.
    '''
    (handler, other_logger) = find_handler(logger, match_handler)
    if handler and other_logger and reconfigure:
        other_logger.removeHandler(handler)
        logger = other_logger
    return (handler, logger)


def find_handler(logger, match_handler):
    """
    Find a (specific type of) handler in the propagation tree of a logger.

    :param logger: The logger to check (a :class:`~logging.Logger` object).
    :param match_handler: A callable that receives a :class:`~logging.Handler`
                          object and returns :data:`True` to match a handler or
                          :data:`False` to skip that handler and continue
                          searching for a match.
    :returns: A tuple of two values:

              1. The matched :class:`~logging.Handler` object or :data:`None`
                 if no handler was matched.
              2. The :class:`~logging.Logger` object to which the handler is
                 attached or :data:`None` if no handler was matched.

    This function finds a logging handler (of the given type) attached to a
    logger or one of its parents (see :func:`walk_propagation_tree()`). It uses
    the undocumented :class:`~logging.Logger.handlers` attribute to find
    handlers attached to a logger, however it won't raise an exception if the
    attribute isn't available. The advantages of this approach are:

    - This works regardless of whether :mod:`coloredlogs` attached the handler
      or other Python code attached the handler.

    - This will correctly recognize the situation where the given logger has no
      handlers but :attr:`~logging.Logger.propagate` is enabled and the logger
      has a parent logger that does have a handler attached.
    """
    for logger in walk_propagation_tree(logger):
        for handler in getattr(logger, 'handlers', []):
            if match_handler(handler):
                
                
                return None, None, (handler, logger)
            return (None, None)


def match_stream_handler(handler, streams = ([],)):
