# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _result.pyc (Python 3.11)

'''
Hook wrapper "result" utilities.
'''
from __future__ import annotations
from types import TracebackType
from typing import Callable
from typing import cast
from typing import final
from typing import Generic
from typing import Optional
from typing import TypeVar
_ExcInfo = tuple[(type[BaseException], BaseException, Optional[TracebackType])]
ResultType = TypeVar('ResultType')

class HookCallError(Exception):
    '''Hook was called incorrectly.'''
    pass


def Result():
    '''Result'''
    __doc__ = 'An object used to inspect and set the result in a :ref:`hook wrapper\n    <hookwrappers>`.'
    __slots__ = ('_result', '_exception', '_traceback')
    
    def __init__(self = None, result = None, exception = None):
        ''':meta private:'''
        self._result = result
        self._exception = exception
    # WARNING: Decompyle incomplete

    excinfo = (lambda self = None: exc = self._exception# WARNING: Decompyle incomplete
)()
    exception = (lambda self = None: self._exception)()
    from_call = (lambda cls = None, func = None: __tracebackhide__ = Trueresult = Noneexception = Nonetry:
result = func()except BaseException:
exc = Noneexception = excexc = Nonedel excexcept:
exc = Nonedel exccls(result, exception))()
    
    def force_result(self = None, result = None):
        '''Force the result(s) to ``result``.

        If the hook was marked as a ``firstresult`` a single value should
        be set, otherwise set a (modified) list of results. Any exceptions
        found during invocation will be deleted.

        This overrides any previous result or exception.
        '''
        self._result = result
        self._exception = None
        self._traceback = None

    
    def force_exception(self = None, exception = None):
        '''Force the result to fail with ``exception``.

        This overrides any previous result or exception.

        .. versionadded:: 1.1.0
        '''
        self._result = None
        self._exception = exception
    # WARNING: Decompyle incomplete

    
    def get_result(self = None):
        '''Get the result(s) for this hook call.

        If the hook was marked as a ``firstresult`` only a single value
        will be returned, otherwise a list of results.
        '''
        __tracebackhide__ = True
        exc = self._exception
        tb = self._traceback
    # WARNING: Decompyle incomplete


Result = <NODE:27>(Result, 'Result', Generic[ResultType])()
_Result = Result
