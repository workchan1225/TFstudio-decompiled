# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: credentials.pyc (Python 3.11)

'''Interfaces for asynchronous credentials.'''
from google.auth import _helpers
from google.auth import exceptions
from google.auth._credentials_base import _BaseCredentials

class Credentials(_BaseCredentials):
    pass
# WARNING: Decompyle incomplete


class StaticCredentials(Credentials):
    pass
# WARNING: Decompyle incomplete


class AnonymousCredentials(Credentials):
    '''Asynchronous Credentials that do not provide any authentication information.

    These are useful in the case of services that support anonymous access or
    local service emulators that do not use credentials.
    '''
    
    async def refresh(self, request):
        '''Raises :class:``InvalidOperation``, anonymous credentials cannot be
        refreshed.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def apply(self, headers, token = (None,)):
        '''Anonymous credentials do nothing to the request.

        The optional ``token`` argument is not supported.

        Raises:
            google.auth.exceptions.InvalidValue: If a token was specified.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def before_request(self, request, method, url, headers):
        '''Anonymous credentials do nothing to the request.'''
        pass
    # WARNING: Decompyle incomplete
