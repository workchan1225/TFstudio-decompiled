# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _credentials_base.pyc (Python 3.11)

'''Interface for base credentials.'''
import abc
from google.auth import _helpers

def _BaseCredentials():
    '''_BaseCredentials'''
    __doc__ = 'Base class for all credentials.\n\n    All credentials have a :attr:`token` that is used for authentication and\n    may also optionally set an :attr:`expiry` to indicate when the token will\n    no longer be valid.\n\n    Most credentials will be :attr:`invalid` until :meth:`refresh` is called.\n    Credentials can do this automatically before the first HTTP request in\n    :meth:`before_request`.\n\n    Although the token and expiration will change as the credentials are\n    :meth:`refreshed <refresh>` and used, credentials should be considered\n    immutable. Various credentials will accept configuration such as private\n    keys, scopes, and other options. These options are not changeable after\n    construction. Some classes will provide mechanisms to copy the credentials\n    with modifications such as :meth:`ScopedCredentials.with_scopes`.\n\n    Attributes:\n        token (Optional[str]): The bearer token that can be used in HTTP headers to make\n            authenticated requests.\n    '
    
    def __init__(self):
        self.token = None

    refresh = (lambda self, request: raise NotImplementedError('Refresh must be implemented'))()
    
    def _apply(self, headers, token = (None,)):
