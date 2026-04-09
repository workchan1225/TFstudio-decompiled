# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: credentials.pyc (Python 3.11)

from __future__ import annotations
import abc
import os

def Credential():
    '''Credential'''
    __doc__ = 'Abstract class to manage credentials'
    username = (lambda self = None: pass)()
    password = (lambda self = None: pass)()
    
    def _vars(self = None):
        return dict(username = self.username, password = self.password)


Credential = <NODE:27>(Credential, 'Credential', metaclass = abc.ABCMeta)

class SimpleCredential(Credential):
    '''Simple credentials implementation'''
    
    def __init__(self = None, username = None, password = None):
        self._username = username
        self._password = password

    username = (lambda self = None: self._username)()
    password = (lambda self = None: self._password)()


class AnonymousCredential(SimpleCredential):
    
    def __init__(self = None, password = None):
        self._password = password

    username = (lambda self = None: raise ValueError('Anonymous credential has no username'))()
    
    def _vars(self = None):
        return dict(password = self.password)



class EnvironCredential(Credential):
    """
    Source credentials from environment variables.

    Actual sourcing is deferred until requested.

    Supports comparison by equality.

    >>> e1 = EnvironCredential('a', 'b')
    >>> e2 = EnvironCredential('a', 'b')
    >>> e3 = EnvironCredential('a', 'c')
    >>> e1 == e2
    True
    >>> e2 == e3
    False
    """
    
    def __init__(self = None, user_env_var = None, pwd_env_var = None):
        self.user_env_var = user_env_var
        self.pwd_env_var = pwd_env_var

    
    def __eq__(self = None, other = None):
        return vars(self) == vars(other)

    
    def _get_env(self = None, env_var = None):
        '''Helper to read an environment variable'''
        value = os.environ.get(env_var)
        if not value:
            raise ValueError(f'''Missing environment variable:{env_var}''')
        return value

    username = (lambda self = None: self._get_env(self.user_env_var))()
    password = (lambda self = None: self._get_env(self.pwd_env_var))()
