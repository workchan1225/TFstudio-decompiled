# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

import sys
import warnings

class KeyringError(Exception):
    '''Base class for exceptions in keyring'''
    pass


class PasswordSetError(KeyringError):
    """Raised when the password can't be set."""
    pass


class PasswordDeleteError(KeyringError):
    """Raised when the password can't be deleted."""
    pass


class InitError(KeyringError):
    '''Raised when the keyring could not be initialised'''
    pass


class KeyringLocked(KeyringError):
    '''Raised when the keyring failed unlocking'''
    pass


class NoKeyringError(RuntimeError, KeyringError):
    '''Raised when there is no keyring backend'''
    pass


class ExceptionRaisedContext:
    '''
    An exception-trapping context that indicates whether an exception was
    raised.
    '''
    
    def __init__(self, ExpectedException = (Exception,)):
        warnings.warn('ExceptionRaisedContext is deprecated; use `jaraco.context.ExceptionTrap`', DeprecationWarning, stacklevel = 2)
        self.ExpectedException = ExpectedException
        self.exc_info = None

    
    def __enter__(self):
        self.exc_info = object.__new__(ExceptionInfo)
        return self.exc_info

    
    def __exit__(self, *exc_info):
        pass
    # WARNING: Decompyle incomplete



class ExceptionInfo:
    
    def __init__(self, *info):
        if not info:
            info = sys.exc_info()
        (self.type, self.value, _) = info

    
    def __bool__(self):
        '''
        Return True if an exception occurred
        '''
        return bool(self.type)

    __nonzero__ = __bool__
