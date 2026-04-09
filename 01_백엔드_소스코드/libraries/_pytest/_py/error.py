# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)

'''create errno-specific classes for IO or os calls.'''
from __future__ import annotations
from collections.abc import Callable
import errno
import os
import sys
from typing import TYPE_CHECKING
from typing import TypeVar
if TYPE_CHECKING:
    from typing_extensions import ParamSpec
    P = ParamSpec('P')
R = TypeVar('R')

class Error(EnvironmentError):
    
    def __repr__(self = None):
        return '{}.{} {!r}: {} '.format(self.__class__.__module__, self.__class__.__name__, self.__class__.__doc__, ' '.join(map(str, self.args)))

    
    def __str__(self = None):
        s = '[{}]: {}'.format(self.__class__.__doc__, ' '.join(map(str, self.args)))
        return s


_winerrnomap = {
    2: errno.ENOENT,
    3: errno.ENOENT,
    17: errno.EEXIST,
    18: errno.EXDEV,
    13: errno.EBUSY,
    22: errno.ENOTDIR,
    20: errno.ENOTDIR,
    267: errno.ENOTDIR,
    5: errno.EACCES }

class ErrorMaker:
    """lazily provides Exception classes for each possible POSIX errno
    (as defined per the 'errno' module).  All such instances
    subclass EnvironmentError.
    """
    _errno2class: 'dict[int, type[Error]]' = { }
    
    def __getattr__(self = None, name = None):
        if name[0] == '_':
            raise AttributeError(name)
        eno = getattr(errno, name)
        cls = self._geterrnoclass(eno)
        setattr(self, name, cls)
        return cls

    
    def _geterrnoclass(self = None, eno = None):
        
        try:
            return self._errno2class[eno]
        except KeyError:
            clsname = errno.errorcode.get(eno, f'''UnknownErrno{eno}''')
            errorcls = type(clsname, (Error,), {
                '__module__': 'py.error',
                '__doc__': os.strerror(eno) })
            self._errno2class[eno] = errorcls
            return 


    
    def checked_call(self = None, func = None, *args, **kwargs):
        '''Call a function and raise an errno-exception if applicable.'''
        __tracebackhide__ = True
    # WARNING: Decompyle incomplete


_error_maker = ErrorMaker()
checked_call = _error_maker.checked_call

def __getattr__(attr = None):
    return getattr(_error_maker, attr)
