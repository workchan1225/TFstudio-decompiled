# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: credentials.pyc (Python 3.11)

'''Interfaces for credentials.'''
import abc
from enum import Enum
import os
from typing import List
from google.auth import _helpers, environment_vars
from google.auth import exceptions
from google.auth import metrics
from google.auth._credentials_base import _BaseCredentials
from google.auth._default import _LOGGER
from google.auth._refresh_worker import RefreshThreadManager
DEFAULT_UNIVERSE_DOMAIN = 'googleapis.com'
NO_OP_TRUST_BOUNDARY_LOCATIONS: List[str] = []
NO_OP_TRUST_BOUNDARY_ENCODED_LOCATIONS = '0x0'

class Credentials(_BaseCredentials):
    pass
# WARNING: Decompyle incomplete


class CredentialsWithQuotaProject(Credentials):
    '''Abstract base for credentials supporting ``with_quota_project`` factory'''
    
    def with_quota_project(self, quota_project_id):
        '''Returns a copy of these credentials with a modified quota project.

        Args:
            quota_project_id (str): The project to use for quota and
                billing purposes

        Returns:
            google.auth.credentials.Credentials: A new credentials instance.
        '''
        raise NotImplementedError('This credential does not support quota project.')

    
    def with_quota_project_from_environment(self):
        quota_from_env = os.environ.get(environment_vars.GOOGLE_CLOUD_QUOTA_PROJECT)
        if quota_from_env:
            return self.with_quota_project(quota_from_env)



class CredentialsWithTokenUri(Credentials):
    '''Abstract base for credentials supporting ``with_token_uri`` factory'''
    
    def with_token_uri(self, token_uri):
        '''Returns a copy of these credentials with a modified token uri.

        Args:
            token_uri (str): The uri to use for fetching/exchanging tokens

        Returns:
            google.auth.credentials.Credentials: A new credentials instance.
        '''
        raise NotImplementedError('This credential does not use token uri.')



class CredentialsWithUniverseDomain(Credentials):
    '''Abstract base for credentials supporting ``with_universe_domain`` factory'''
    
    def with_universe_domain(self, universe_domain):
        '''Returns a copy of these credentials with a modified universe domain.

        Args:
            universe_domain (str): The universe domain to use

        Returns:
            google.auth.credentials.Credentials: A new credentials instance.
        '''
        raise NotImplementedError('This credential does not support with_universe_domain.')



class CredentialsWithTrustBoundary(Credentials):
    pass
# WARNING: Decompyle incomplete


class AnonymousCredentials(Credentials):
    '''Credentials that do not provide any authentication information.

    These are useful in the case of services that support anonymous access or
    local service emulators that do not use credentials.
    '''
    expired = (lambda self: False)()
    valid = (lambda self: True)()
    
    def refresh(self, request):
        '''Raises :class:``InvalidOperation``, anonymous credentials cannot be
        refreshed.'''
        raise exceptions.InvalidOperation('Anonymous credentials cannot be refreshed.')

    
    def apply(self, headers, token = (None,)):
        '''Anonymous credentials do nothing to the request.

        The optional ``token`` argument is not supported.

        Raises:
            google.auth.exceptions.InvalidValue: If a token was specified.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def before_request(self, request, method, url, headers):
        '''Anonymous credentials do nothing to the request.'''
        pass



def ReadOnlyScoped():
    '''ReadOnlyScoped'''
    pass
# WARNING: Decompyle incomplete

ReadOnlyScoped = <NODE:27>(ReadOnlyScoped, 'ReadOnlyScoped', metaclass = abc.ABCMeta)

class Scoped(ReadOnlyScoped):
    """Interface for credentials whose scopes can be replaced while copying.

    OAuth 2.0-based credentials allow limiting access using scopes as described
    in `RFC6749 Section 3.3`_.
    If a credential class implements this interface then the credentials either
    use scopes in their implementation.

    Some credentials require scopes in order to obtain a token. You can check
    if scoping is necessary with :attr:`requires_scopes`::

        if credentials.requires_scopes:
            # Scoping is required.
            credentials = credentials.create_scoped(['one', 'two'])

    Credentials that require scopes must either be constructed with scopes::

        credentials = SomeScopedCredentials(scopes=['one', 'two'])

    Or must copy an existing instance using :meth:`with_scopes`::

        scoped_credentials = credentials.with_scopes(scopes=['one', 'two'])

    Some credentials have scopes but do not allow or require scopes to be set,
    these credentials can be used as-is.

    .. _RFC6749 Section 3.3: https://tools.ietf.org/html/rfc6749#section-3.3
    """
    with_scopes = (lambda self, scopes, default_scopes = (None,): raise NotImplementedError('This class does not require scoping.'))()


def with_scopes_if_required(credentials, scopes, default_scopes = (None,)):
    """Creates a copy of the credentials with scopes if scoping is required.

    This helper function is useful when you do not know (or care to know) the
    specific type of credentials you are using (such as when you use
    :func:`google.auth.default`). This function will call
    :meth:`Scoped.with_scopes` if the credentials are scoped credentials and if
    the credentials require scoping. Otherwise, it will return the credentials
    as-is.

    Args:
        credentials (google.auth.credentials.Credentials): The credentials to
            scope if necessary.
        scopes (Sequence[str]): The list of scopes to use.
        default_scopes (Sequence[str]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.

    Returns:
        google.auth.credentials.Credentials: Either a new set of scoped
            credentials, or the passed in credentials instance if no scoping
            was required.
    """
    if isinstance(credentials, Scoped) and credentials.requires_scopes:
        return credentials.with_scopes(scopes, default_scopes = default_scopes)


def Signing():
    '''Signing'''
    __doc__ = 'Interface for credentials that can cryptographically sign messages.'
    sign_bytes = (lambda self, message: raise NotImplementedError('Sign bytes must be implemented.'))()
    signer_email = (lambda self: raise NotImplementedError('Signer email must be implemented.'))()
    signer = (lambda self: raise NotImplementedError('Signer must be implemented.'))()

Signing = <NODE:27>(Signing, 'Signing', metaclass = abc.ABCMeta)

class TokenState(Enum):
    '''
    Tracks the state of a token.
    FRESH: The token is valid. It is not expired or close to expired, or the token has no expiry.
    STALE: The token is close to expired, and should be refreshed. The token can be used normally.
    INVALID: The token is expired or invalid. The token cannot be used for a normal operation.
    '''
    FRESH = 1
    STALE = 2
    INVALID = 3
