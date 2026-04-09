# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raises.pyc (Python 3.11)

from __future__ import annotations
from abc import ABC
from abc import abstractmethod
import re
from re import Pattern
import sys
from textwrap import indent
from typing import Any
from typing import cast
from typing import final
from typing import Generic
from typing import get_args
from typing import get_origin
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
import warnings
from _pytest._code import ExceptionInfo
from _pytest._code.code import stringify_exception
from _pytest.outcomes import fail
from _pytest.warning_types import PytestWarning
if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Sequence
    import types
    from typing import TypeGuard
    from typing_extensions import ParamSpec
    from typing_extensions import TypeVar
    P = ParamSpec('P')
    BaseExcT_co_default = TypeVar('BaseExcT_co_default', bound = BaseException, default = BaseException, covariant = True)
    E = TypeVar('E', bound = BaseException, default = BaseException)
else:
    from typing import TypeVar
    BaseExcT_co_default = TypeVar('BaseExcT_co_default', bound = BaseException, covariant = True)
BaseExcT_co = TypeVar('BaseExcT_co', bound = BaseException, covariant = True)
BaseExcT_1 = TypeVar('BaseExcT_1', bound = BaseException)
BaseExcT_2 = TypeVar('BaseExcT_2', bound = BaseException)
ExcT_1 = TypeVar('ExcT_1', bound = Exception)
ExcT_2 = TypeVar('ExcT_2', bound = Exception)
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
    from exceptiongroup import ExceptionGroup
_REGEX_NO_FLAGS = re.compile('').flags
raises = (lambda expected_exception = None, *, match: pass)()
raises = (lambda *: pass)()
raises = (lambda *: pass)()
raises = (lambda expected_exception = None, func = None: pass)()

def raises(expected_exception = None, *args, **kwargs):
    '''Assert that a code block/function call raises an exception type, or one of its subclasses.

    :param expected_exception:
        The expected exception type, or a tuple if one of multiple possible
        exception types are expected. Note that subclasses of the passed exceptions
        will also match.

        This is not a required parameter, you may opt to only use ``match`` and/or
        ``check`` for verifying the raised exception.

    :kwparam str | re.Pattern[str] | None match:
        If specified, a string containing a regular expression,
        or a regular expression object, that is tested against the string
        representation of the exception and its :pep:`678` `__notes__`
        using :func:`re.search`.

        To match a literal string that may contain :ref:`special characters
        <re-syntax>`, the pattern can first be escaped with :func:`re.escape`.

        (This is only used when ``pytest.raises`` is used as a context manager,
        and passed through to the function otherwise.
        When using ``pytest.raises`` as a function, you can use:
        ``pytest.raises(Exc, func, match="passed on").match("my pattern")``.)

    :kwparam Callable[[BaseException], bool] check:

        .. versionadded:: 8.4

        If specified, a callable that will be called with the exception as a parameter
        after checking the type and the match regex if specified.
        If it returns ``True`` it will be considered a match, if not it will
        be considered a failed match.


    Use ``pytest.raises`` as a context manager, which will capture the exception of the given
    type, or any of its subclasses::

        >>> import pytest
        >>> with pytest.raises(ZeroDivisionError):
        ...    1/0

    If the code block does not raise the expected exception (:class:`ZeroDivisionError` in the example
    above), or no exception at all, the check will fail instead.

    You can also use the keyword argument ``match`` to assert that the
    exception matches a text or regex::

        >>> with pytest.raises(ValueError, match=\'must be 0 or None\'):
        ...     raise ValueError("value must be 0 or None")

        >>> with pytest.raises(ValueError, match=r\'must be \\d+$\'):
        ...     raise ValueError("value must be 42")

    The ``match`` argument searches the formatted exception string, which includes any
    `PEP-678 <https://peps.python.org/pep-0678/>`__ ``__notes__``:

        >>> with pytest.raises(ValueError, match=r"had a note added"):  # doctest: +SKIP
        ...     e = ValueError("value must be 42")
        ...     e.add_note("had a note added")
        ...     raise e

    The ``check`` argument, if provided, must return True when passed the raised exception
    for the match to be successful, otherwise an :exc:`AssertionError` is raised.

        >>> import errno
        >>> with pytest.raises(OSError, check=lambda e: e.errno == errno.EACCES):
        ...     raise OSError(errno.EACCES, "no permission to view")

    The context manager produces an :class:`ExceptionInfo` object which can be used to inspect the
    details of the captured exception::

        >>> with pytest.raises(ValueError) as exc_info:
        ...     raise ValueError("value must be 42")
        >>> assert exc_info.type is ValueError
        >>> assert exc_info.value.args[0] == "value must be 42"

    .. warning::

       Given that ``pytest.raises`` matches subclasses, be wary of using it to match :class:`Exception` like this::

           # Careful, this will catch ANY exception raised.
           with pytest.raises(Exception):
               some_function()

       Because :class:`Exception` is the base class of almost all exceptions, it is easy for this to hide
       real bugs, where the user wrote this expecting a specific exception, but some other exception is being
       raised due to a bug introduced during a refactoring.

       Avoid using ``pytest.raises`` to catch :class:`Exception` unless certain that you really want to catch
       **any** exception raised.

    .. note::

       When using ``pytest.raises`` as a context manager, it\'s worthwhile to
       note that normal context manager rules apply and that the exception
       raised *must* be the final line in the scope of the context manager.
       Lines of code after that, within the scope of the context manager will
       not be executed. For example::

           >>> value = 15
           >>> with pytest.raises(ValueError) as exc_info:
           ...     if value > 10:
           ...         raise ValueError("value must be <= 10")
           ...     assert exc_info.type is ValueError  # This will not execute.

       Instead, the following approach must be taken (note the difference in
       scope)::

           >>> with pytest.raises(ValueError) as exc_info:
           ...     if value > 10:
           ...         raise ValueError("value must be <= 10")
           ...
           >>> assert exc_info.type is ValueError

    **Expecting exception groups**

    When expecting exceptions wrapped in :exc:`BaseExceptionGroup` or
    :exc:`ExceptionGroup`, you should instead use :class:`pytest.RaisesGroup`.

    **Using with** ``pytest.mark.parametrize``

    When using :ref:`pytest.mark.parametrize ref`
    it is possible to parametrize tests such that
    some runs raise an exception and others do not.

    See :ref:`parametrizing_conditional_raising` for an example.

    .. seealso::

        :ref:`assertraises` for more examples and detailed discussion.

    **Legacy form**

    It is possible to specify a callable by passing a to-be-called lambda::

        >>> raises(ZeroDivisionError, lambda: 1/0)
        <ExceptionInfo ...>

    or you can specify an arbitrary callable with arguments::

        >>> def f(x): return 1/x
        ...
        >>> raises(ZeroDivisionError, f, 0)
        <ExceptionInfo ...>
        >>> raises(ZeroDivisionError, f, x=0)
        <ExceptionInfo ...>

    The form above is fully supported but discouraged for new code because the
    context manager form is regarded as more readable and less error-prone.

    .. note::
        Similar to caught exception objects in Python, explicitly clearing
        local references to returned ``ExceptionInfo`` objects can
        help the Python interpreter speed up its garbage collection.

        Clearing those references breaks a reference cycle
        (``ExceptionInfo`` --> caught exception --> frame stack raising
        the exception --> current frame stack --> local variables -->
        ``ExceptionInfo``) which makes Python keep all objects referenced
        from that cycle (including all local variables in the current
        frame) alive until the next cyclic garbage collection run.
        More detailed information can be found in the official Python
        documentation for :ref:`the try statement <python:try>`.
    '''
    __tracebackhide__ = True
# WARNING: Decompyle incomplete

raises.Exception = fail.Exception

def _match_pattern(match = None):
    '''Helper function to remove redundant `re.compile` calls when printing regex'''
    return match.pattern if match.flags == _REGEX_NO_FLAGS else match


def repr_callable(fun = None):
    '''Get the repr of a ``check`` parameter.

    Split out so it can be monkeypatched (e.g. by hypothesis)
    '''
    return repr(fun)


def backquote(s = None):
    return '`' + s + '`'


def _exception_type_name(e = None):
    if isinstance(e, type):
        return e.__name__
    if None(e) == 1:
        return e[0].__name__
    return ', '.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(e()) + ')'


def _check_raw_type(expected_type = None, exception = None):
    pass
# WARNING: Decompyle incomplete


def is_fully_escaped(s = None):
    pass
# WARNING: Decompyle incomplete


def unescape(s = None):
    return re.sub('\\\\([{}()+-.*?^$\\[\\]\\s\\\\])', '\\1', s)


def AbstractRaises():
    '''AbstractRaises'''
    __doc__ = 'ABC with common functionality shared between RaisesExc and RaisesGroup'
    
    def __init__(self = None, *, match, check):
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_exc(self = None, exc = None, expected = None):
        if isinstance(exc, type) and issubclass(exc, BaseException):
            if not issubclass(exc, Exception):
                self.is_baseexception = True
            return exc
        origin_exc = None(exc)
        if origin_exc and issubclass(origin_exc, BaseExceptionGroup):
            exc_type = get_args(exc)[0]
            if (issubclass(origin_exc, ExceptionGroup) or exc_type in (Exception, Any) or issubclass(origin_exc, BaseExceptionGroup)) and exc_type in (BaseException, Any):
                if not issubclass(origin_exc, ExceptionGroup):
                    self.is_baseexception = True
                return cast(type[BaseExcT_1], origin_exc)
            raise None(f'''Only `ExceptionGroup[Exception]` or `BaseExceptionGroup[BaseException]` are accepted as generic types but got `{exc}`. As `raises` will catch all instances of the specified group regardless of the generic argument specific nested exceptions has to be checked with `RaisesGroup`.''')
        msg = f'''Expected {expected}, but got '''
        if isinstance(exc, type):
            raise ValueError(msg + f'''{exc.__name__!r}''')
        if isinstance(exc, BaseException):
            raise TypeError(msg + f'''an exception instance: {type(exc).__name__}''')
        raise TypeError(msg + repr(type(exc).__name__))

    fail_reason = (lambda self = None: self._fail_reason)()
    
    def _check_check(self = None, exception = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_match(self = None, e = None):
        pass
    # WARNING: Decompyle incomplete

    matches = (lambda self = None, exception = None: pass)()

AbstractRaises = <NODE:27>(AbstractRaises, 'AbstractRaises', ABC, Generic[BaseExcT_co])

def RaisesExc():
    '''RaisesExc'''
    pass
# WARNING: Decompyle incomplete

RaisesExc = <NODE:27>(RaisesExc, 'RaisesExc', AbstractRaises[BaseExcT_co_default])()

def RaisesGroup():
    '''RaisesGroup'''
    pass
# WARNING: Decompyle incomplete

RaisesGroup = <NODE:27>(RaisesGroup, 'RaisesGroup', AbstractRaises[BaseExceptionGroup[BaseExcT_co]])()
NotChecked = <NODE:12>()

class ResultHolder:
    '''Container for results of checking exceptions.
    Used in RaisesGroup._check_exceptions and possible_match.
    '''
    
    def __init__(self = None, expected_exceptions = None, actual_exceptions = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_result(self = None, expected = None, actual = None, result = ('expected', 'int', 'actual', 'int', 'result', 'str | None', 'return', 'None')):
        self.results[actual][expected] = result

    
    def get_result(self = None, expected = None, actual = None):
        res = self.results[actual][expected]
    # WARNING: Decompyle incomplete

    
    def has_result(self = None, expected = None, actual = None):
        return self.results[actual][expected] is not NotChecked

    
    def no_match_for_expected(self = None, expected = None):
        pass
    # WARNING: Decompyle incomplete

    
    def no_match_for_actual(self = None, actual = None):
        pass
    # WARNING: Decompyle incomplete



def possible_match(results = final, used = final):
    pass
# WARNING: Decompyle incomplete
