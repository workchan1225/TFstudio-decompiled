# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: warning_types.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import inspect
from types import FunctionType
from typing import Any
from typing import final
from typing import Generic
from typing import TypeVar
import warnings

class PytestWarning(UserWarning):
    '''Base class for all warnings emitted by pytest.'''
    __module__ = 'pytest'

PytestAssertRewriteWarning = <NODE:12>()
PytestCacheWarning = <NODE:12>()
PytestConfigWarning = <NODE:12>()
PytestCollectionWarning = <NODE:12>()

class PytestDeprecationWarning(DeprecationWarning, PytestWarning):
    '''Warning class for features that will be removed in a future version.'''
    __module__ = 'pytest'


class PytestRemovedIn9Warning(PytestDeprecationWarning):
    '''Warning class for features that will be removed in pytest 9.'''
    __module__ = 'pytest'


class PytestRemovedIn10Warning(PytestDeprecationWarning):
    '''Warning class for features that will be removed in pytest 10.'''
    __module__ = 'pytest'

PytestExperimentalApiWarning = <NODE:12>()
PytestReturnNotNoneWarning = <NODE:12>()
PytestUnknownMarkWarning = <NODE:12>()
PytestUnraisableExceptionWarning = <NODE:12>()
PytestUnhandledThreadExceptionWarning = <NODE:12>()
_W = TypeVar('_W', bound = PytestWarning)

def UnformattedWarning():
    '''UnformattedWarning'''
    template: 'str' = 'A warning meant to be formatted during runtime.\n\n    This is used to hold warnings that need to format their message at runtime,\n    as opposed to a direct message.\n    '
    
    def format(self = None, **kwargs):
        '''Return an instance of the warning category, formatted with given kwargs.'''
        pass
    # WARNING: Decompyle incomplete


UnformattedWarning = <NODE:27>(UnformattedWarning, 'UnformattedWarning', Generic[_W])()()
PytestFDWarning = <NODE:12>()

def warn_explicit_for(method = final, message = dataclasses.dataclass):
    '''
    Issue the warning :param:`message` for the definition of the given :param:`method`

    this helps to log warnings for functions defined prior to finding an issue with them
    (like hook wrappers being marked in a legacy mechanism)
    '''
    lineno = method.__code__.co_firstlineno
    filename = inspect.getfile(method)
    module = method.__module__
    mod_globals = method.__globals__
    
    try:
        warnings.warn_explicit(message, type(message), filename = filename, module = module, registry = mod_globals.setdefault('__warningregistry__', { }), lineno = lineno)
        return None
    except Warning:
        w = None
        raise type(w)(f'''{w}\n at {filename}:{lineno}'''), None
        w = None
        del w
