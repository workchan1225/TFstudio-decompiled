# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backend.pyc (Python 3.11)

'''
Keyring implementation support
'''
from __future__ import annotations
import abc
import copy
import functools
import logging
import operator
import os
import typing
import warnings
from jaraco.context import ExceptionTrap
from jaraco.functools import once
from  import credentials, errors, util
from compat import properties
from compat.py312 import metadata
log = logging.getLogger(__name__)
by_priority = operator.attrgetter('priority')
_limit: 'typing.Callable[[KeyringBackend], bool] | None' = None

class KeyringBackendMeta(abc.ABCMeta):
    pass
# WARNING: Decompyle incomplete


def KeyringBackend():
    '''KeyringBackend'''
    __doc__ = 'The abstract base class of the keyring, every backend must implement\n    this interface.\n    '
    
    def __init__(self):
        self.set_properties_from_env()

    priority = (lambda self = None: raise NotImplementedError)()
    passes = ExceptionTrap().passes
    viable = (lambda cls: cls.priority)()()
    get_viable_backends = (lambda cls = properties.classproperty: filter(operator.attrgetter('viable'), cls._classes))()
    name = (lambda cls = None: (parent, sep, mod_name) = cls.__module__.rpartition('.')mod_name = mod_name.replace('_', ' ')' '.join([
mod_name,
cls.__name__]))()
    
    def __str__(self = None):
        keyring_class = type(self)
        return f'''{keyring_class.__module__}.{keyring_class.__name__} (priority: {keyring_class.priority:g})'''

    get_password = (lambda self = None, service = None, username = abc.abstractmethod: pass)()
    
    def _validate_username(self = None, username = None):
        '''
        Ensure the username is not empty.
        '''
        if not username:
            warnings.warn('Empty usernames are deprecated. See #668', DeprecationWarning, stacklevel = 3)
            return None

    set_password = (lambda self = None, service = None, username = abc.abstractmethod, password = ('service', 'str', 'username', 'str', 'password', 'str', 'return', 'None'): raise errors.PasswordSetError('reason'))()
    
    def delete_password(self = None, service = None, username = None):
        '''Delete the password for the username of the service.

        If the backend cannot delete passwords, raise
        PasswordDeleteError.
        '''
        raise errors.PasswordDeleteError('reason')

    
    def get_credential(self = None, service = None, username = None):
        '''Gets the username and password for the service.
        Returns a Credential instance.

        The *username* argument is optional and may be omitted by
        the caller or ignored by the backend. Callers must use the
        returned username.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_properties_from_env(self = None):
        '''For all KEYRING_PROPERTY_* env var, set that property.'''
        
        def parse(item = None):
