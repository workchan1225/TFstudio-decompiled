# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

import typing as t
from gettext import gettext as _
from gettext import ngettext
from _compat import get_text_stderr
from globals import resolve_color_default
from utils import echo
from utils import format_filename
if t.TYPE_CHECKING:
    from core import Command
    from core import Context
    from core import Parameter

def _join_param_hints(param_hint = None):
    pass
# WARNING: Decompyle incomplete


class ClickException(Exception):
    pass
# WARNING: Decompyle incomplete


class UsageError(ClickException):
    pass
# WARNING: Decompyle incomplete


class BadParameter(UsageError):
    pass
# WARNING: Decompyle incomplete


class MissingParameter(BadParameter):
    pass
# WARNING: Decompyle incomplete


class NoSuchOption(UsageError):
    pass
# WARNING: Decompyle incomplete


class BadOptionUsage(UsageError):
    pass
# WARNING: Decompyle incomplete


class BadArgumentUsage(UsageError):
    '''Raised if an argument is generally supplied but the use of the argument
    was incorrect.  This is for instance raised if the number of values
    for an argument is not correct.

    .. versionadded:: 6.0
    '''
    pass


class FileError(ClickException):
    pass
# WARNING: Decompyle incomplete


class Abort(RuntimeError):
    '''An internal signalling exception that signals Click to abort.'''
    pass


class Exit(RuntimeError):
    '''An exception that indicates that the application should exit with some
    status code.

    :param code: the status code to exit with.
    '''
    __slots__ = ('exit_code',)
    
    def __init__(self = None, code = None):
        self.exit_code = code
