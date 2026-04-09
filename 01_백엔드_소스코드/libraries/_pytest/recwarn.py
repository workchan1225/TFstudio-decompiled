# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: recwarn.pyc (Python 3.11)

'''Record warnings during test function execution.'''
from __future__ import annotations
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterator
from pprint import pformat
import re
from types import TracebackType
from typing import Any
from typing import final
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
if TYPE_CHECKING:
    from typing_extensions import Self
import warnings
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.outcomes import Exit
from _pytest.outcomes import fail
T = TypeVar('T')
recwarn = (lambda : pass# WARNING: Decompyle incomplete
)()
deprecated_call = (lambda *: pass)()
deprecated_call = (lambda func = None: pass)()

def deprecated_call(func = None, *args, **kwargs):
    """Assert that code produces a ``DeprecationWarning`` or ``PendingDeprecationWarning`` or ``FutureWarning``.

    This function can be used as a context manager::

        >>> import warnings
        >>> def api_call_v2():
        ...     warnings.warn('use v3 of this api', DeprecationWarning)
        ...     return 200

        >>> import pytest
        >>> with pytest.deprecated_call():
        ...    assert api_call_v2() == 200

    It can also be used by passing a function and ``*args`` and ``**kwargs``,
    in which case it will ensure calling ``func(*args, **kwargs)`` produces one of
    the warnings types above. The return value is the return value of the function.

    In the context manager form you may use the keyword argument ``match`` to assert
    that the warning matches a text or regex.

    The context manager produces a list of :class:`warnings.WarningMessage` objects,
    one for each warning raised.
    """
    __tracebackhide__ = True
# WARNING: Decompyle incomplete

warns = (lambda expected_warning = None, *, match: pass)()
warns = (lambda expected_warning = None, func = None: pass)()

def warns(expected_warning = None, *, match, *args, **kwargs):
    '''Assert that code raises a particular class of warning.

    Specifically, the parameter ``expected_warning`` can be a warning class or tuple
    of warning classes, and the code inside the ``with`` block must issue at least one
    warning of that class or classes.

    This helper produces a list of :class:`warnings.WarningMessage` objects, one for
    each warning emitted (regardless of whether it is an ``expected_warning`` or not).
    Since pytest 8.0, unmatched warnings are also re-emitted when the context closes.

    This function can be used as a context manager::

        >>> import pytest
        >>> with pytest.warns(RuntimeWarning):
        ...    warnings.warn("my warning", RuntimeWarning)

    In the context manager form you may use the keyword argument ``match`` to assert
    that the warning matches a text or regex::

        >>> with pytest.warns(UserWarning, match=\'must be 0 or None\'):
        ...     warnings.warn("value must be 0 or None", UserWarning)

        >>> with pytest.warns(UserWarning, match=r\'must be \\d+$\'):
        ...     warnings.warn("value must be 42", UserWarning)

        >>> with pytest.warns(UserWarning):  # catch re-emitted warning
        ...     with pytest.warns(UserWarning, match=r\'must be \\d+$\'):
        ...         warnings.warn("this is not here", UserWarning)
        Traceback (most recent call last):
          ...
        Failed: DID NOT WARN. No warnings of type ...UserWarning... were emitted...

    **Using with** ``pytest.mark.parametrize``

    When using :ref:`pytest.mark.parametrize ref` it is possible to parametrize tests
    such that some runs raise a warning and others do not.

    This could be achieved in the same way as with exceptions, see
    :ref:`parametrizing_conditional_raising` for an example.

    '''
    __tracebackhide__ = True
    if not args:
        if kwargs:
            argnames = ', '.join(sorted(kwargs))
            raise TypeError(f'''Unexpected keyword arguments passed to pytest.warns: {argnames}\nUse context-manager form instead?''')
        return WarningsChecker(expected_warning, match_expr = match, _ispytest = True)
    func = None[0]
    if not callable(func):
        raise TypeError(f'''{func!r} object (type: {type(func)}) must be callable''')
    WarningsChecker(expected_warning, _ispytest = True)
# WARNING: Decompyle incomplete


class WarningsRecorder(warnings.catch_warnings):
    pass
# WARNING: Decompyle incomplete

WarningsChecker = <NODE:12>()
