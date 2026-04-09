# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: outcomes.pyc (Python 3.11)

'''Exception classes and constants handling test outcomes as well as
functions creating them.'''
from __future__ import annotations
import sys
from typing import Any
from typing import ClassVar
from typing import NoReturn
from warning_types import PytestDeprecationWarning

class OutcomeException(BaseException):
    pass
# WARNING: Decompyle incomplete

TEST_OUTCOME = (OutcomeException, Exception)

class Skipped(OutcomeException):
    pass
# WARNING: Decompyle incomplete


class Failed(OutcomeException):
    '''Raised from an explicit call to pytest.fail().'''
    __module__ = 'builtins'


class Exit(Exception):
    pass
# WARNING: Decompyle incomplete


class XFailed(Failed):
    '''Raised from an explicit call to pytest.xfail().'''
    pass


class _Exit:
    '''Exit testing process.

    :param reason:
        The message to show as the reason for exiting pytest.  reason has a default value
        only because `msg` is deprecated.

    :param returncode:
        Return code to be used when exiting pytest. None means the same as ``0`` (no error),
        same as :func:`sys.exit`.

    :raises pytest.exit.Exception:
        The exception that is raised.
    '''
    Exception: 'ClassVar[type[Exit]]' = Exit
    
    def __call__(self = None, reason = None, returncode = None):
        __tracebackhide__ = True
        raise Exit(msg = reason, returncode = returncode)


exit: '_Exit' = _Exit()

class _Skip:
    '''Skip an executing test with the given message.

    This function should be called only during testing (setup, call or teardown) or
    during collection by using the ``allow_module_level`` flag.  This function can
    be called in doctests as well.

    :param reason:
        The message to show the user as reason for the skip.

    :param allow_module_level:
        Allows this function to be called at module level.
        Raising the skip exception at module level will stop
        the execution of the module and prevent the collection of all tests in the module,
        even those defined before the `skip` call.

        Defaults to False.

    :raises pytest.skip.Exception:
        The exception that is raised.

    .. note::
        It is better to use the :ref:`pytest.mark.skipif ref` marker when
        possible to declare a test to be skipped under certain conditions
        like mismatching platforms or dependencies.
        Similarly, use the ``# doctest: +SKIP`` directive (see :py:data:`doctest.SKIP`)
        to skip a doctest statically.
    '''
    Exception: 'ClassVar[type[Skipped]]' = Skipped
    
    def __call__(self = None, reason = None, allow_module_level = None):
        __tracebackhide__ = True
        raise Skipped(msg = reason, allow_module_level = allow_module_level)


skip: '_Skip' = _Skip()

class _Fail:
    '''Explicitly fail an executing test with the given message.

    :param reason:
        The message to show the user as reason for the failure.

    :param pytrace:
        If False, msg represents the full failure information and no
        python traceback will be reported.

    :raises pytest.fail.Exception:
        The exception that is raised.
    '''
    Exception: 'ClassVar[type[Failed]]' = Failed
    
    def __call__(self = None, reason = None, pytrace = None):
        __tracebackhide__ = True
        raise Failed(msg = reason, pytrace = pytrace)


fail: '_Fail' = _Fail()

class _XFail:
    '''Imperatively xfail an executing test or setup function with the given reason.

    This function should be called only during testing (setup, call or teardown).

    No other code is executed after using ``xfail()`` (it is implemented
    internally by raising an exception).

    :param reason:
        The message to show the user as reason for the xfail.

    .. note::
        It is better to use the :ref:`pytest.mark.xfail ref` marker when
        possible to declare a test to be xfailed under certain conditions
        like known bugs or missing features.

    :raises pytest.xfail.Exception:
        The exception that is raised.
    '''
    Exception: 'ClassVar[type[XFailed]]' = XFailed
    
    def __call__(self = None, reason = None):
        __tracebackhide__ = True
        raise XFailed(msg = reason)


xfail: '_XFail' = _XFail()

def importorskip(modname = None, minversion = None, reason = None, *, exc_type):
    '''Import and return the requested module ``modname``, or skip the
    current test if the module cannot be imported.

    :param modname:
        The name of the module to import.
    :param minversion:
        If given, the imported module\'s ``__version__`` attribute must be at
        least this minimal version, otherwise the test is still skipped.
    :param reason:
        If given, this reason is shown as the message when the module cannot
        be imported.
    :param exc_type:
        The exception that should be captured in order to skip modules.
        Must be :py:class:`ImportError` or a subclass.

        If the module can be imported but raises :class:`ImportError`, pytest will
        issue a warning to the user, as often users expect the module not to be
        found (which would raise :class:`ModuleNotFoundError` instead).

        This warning can be suppressed by passing ``exc_type=ImportError`` explicitly.

        See :ref:`import-or-skip-import-error` for details.


    :returns:
        The imported module. This should be assigned to its canonical name.

    :raises pytest.skip.Exception:
        If the module cannot be imported.

    Example::

        docutils = pytest.importorskip("docutils")

    .. versionadded:: 8.2

        The ``exc_type`` parameter.
    '''
    import warnings
    __tracebackhide__ = True
    compile(modname, '', 'eval')
# WARNING: Decompyle incomplete
