# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _raises_group.pyc (Python 3.11)

from __future__ import annotations
import re
import sys
from abc import ABC, abstractmethod
from re import Pattern
from textwrap import indent
from typing import TYPE_CHECKING, Generic, Literal, TypeGuard, cast, overload
from trio._util import final
if TYPE_CHECKING:
    import builtins
    import types
    from collections.abc import Callable, Sequence
    from _pytest._code.code import ExceptionChainRepr, ReprExceptionInfo, Traceback
    from typing_extensions import TypeVar
    MatchE = TypeVar('MatchE', bound = BaseException, default = BaseException, covariant = True)
else:
    from typing import TypeVar
    MatchE = TypeVar('MatchE', bound = BaseException, covariant = True)
BaseExcT_co = TypeVar('BaseExcT_co', bound = BaseException, covariant = True)
BaseExcT_1 = TypeVar('BaseExcT_1', bound = BaseException)
BaseExcT_2 = TypeVar('BaseExcT_2', bound = BaseException)
ExcT_1 = TypeVar('ExcT_1', bound = Exception)
ExcT_2 = TypeVar('ExcT_2', bound = Exception)
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup, ExceptionGroup

def _ExceptionInfo():
    '''_ExceptionInfo'''
    _excinfo: 'tuple[type[MatchE], MatchE, types.TracebackType] | None' = 'Minimal re-implementation of pytest.ExceptionInfo, only used if pytest is not available. Supports a subset of its features necessary for functionality of :class:`trio.testing.RaisesGroup` and :class:`trio.testing.Matcher`.'
    
    def __init__(self = None, excinfo = None):
        self._excinfo = excinfo

    
    def fill_unfilled(self = None, exc_info = None):
        '''Fill an unfilled ExceptionInfo created with ``for_later()``.'''
        pass
    # WARNING: Decompyle incomplete

    for_later = (lambda cls = None: cls(None))()
    type = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    value = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    tb = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def exconly(self = None, tryshort = None):
        raise NotImplementedError('This is a helper method only available if you use RaisesGroup with the pytest package installed')

    
    def errisinstance(self = None, exc = None):
        raise NotImplementedError('This is a helper method only available if you use RaisesGroup with the pytest package installed')

    
    def getrepr(self, showlocals, style, abspath = None, tbfilter = None, funcargs = None, truncate_locals = (False, 'long', False, True, False, True, True), chain = ('showlocals', 'bool', 'style', 'str', 'abspath', 'bool', 'tbfilter', 'bool | Callable[[_ExceptionInfo], Traceback]', 'funcargs', 'bool', 'truncate_locals', 'bool', 'chain', 'bool', 'return', 'ReprExceptionInfo | ExceptionChainRepr')):
        raise NotImplementedError('This is a helper method only available if you use RaisesGroup with the pytest package installed')


_ExceptionInfo = <NODE:27>(_ExceptionInfo, '_ExceptionInfo', Generic[MatchE])()
if TYPE_CHECKING:
    ExceptionInfo = _ExceptionInfo
else:
    
    try:
        from pytest import ExceptionInfo
    except ImportError:
        ExceptionInfo = _ExceptionInfo

    
    def _stringify_exception(exc = None):
        return None('\n'.join)

    _REGEX_NO_FLAGS = re.compile('').flags
    
    def _match_pattern(match = None):
        '''helper function to remove redundant `re.compile` calls when printing regex'''
        return match.pattern if match.flags == _REGEX_NO_FLAGS else match

    
    def repr_callable(fun = None):
        '''Get the repr of a ``check`` parameter.

    Split out so it can be monkeypatched (e.g. by our hypothesis plugin)
    '''
        return repr(fun)

    
    def _exception_type_name(e = None):
        return repr(e.__name__)

    
    def _check_raw_type(expected_type = None, exception = None):
        pass
    # WARNING: Decompyle incomplete

    
    def AbstractMatcher():
        '''AbstractMatcher'''
        __doc__ = 'ABC with common functionality shared between Matcher and RaisesGroup'
        
        def __init__(self = None, match = None, check = None):
            if isinstance(match, str):
                self.match = re.compile(match)
            else:
                self.match = match
            self.check = check
            self._fail_reason = None
            self._nested = False

        fail_reason = (lambda self = None: self._fail_reason)()
        
        def _check_check(self = None, exception = None):
            pass
        # WARNING: Decompyle incomplete

        
        def _check_match(self = None, e = None):
            pass
        # WARNING: Decompyle incomplete

        matches = (lambda self = None, exc_val = None: pass)()

    AbstractMatcher = <NODE:27>(AbstractMatcher, 'AbstractMatcher', ABC, Generic[BaseExcT_co])
    
    def Matcher():
        '''Matcher'''
        pass
    # WARNING: Decompyle incomplete

    Matcher = <NODE:27>(Matcher, 'Matcher', AbstractMatcher[MatchE])()
    
    def RaisesGroup():
        '''RaisesGroup'''
        pass
    # WARNING: Decompyle incomplete

    RaisesGroup = <NODE:27>(RaisesGroup, 'RaisesGroup', AbstractMatcher[BaseExceptionGroup[BaseExcT_co]])()
    NotChecked = <NODE:12>()
    
    class ResultHolder:
        
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

    return None
