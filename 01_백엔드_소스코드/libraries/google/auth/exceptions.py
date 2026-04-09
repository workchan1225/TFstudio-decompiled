# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''Exceptions used in the google.auth package.'''

class GoogleAuthError(Exception):
    pass
# WARNING: Decompyle incomplete


class TransportError(GoogleAuthError):
    '''Used to indicate an error occurred during an HTTP request.'''
    pass


class RefreshError(GoogleAuthError):
    """Used to indicate that an refreshing the credentials' access token
    failed."""
    pass


class UserAccessTokenError(GoogleAuthError):
    '''Used to indicate ``gcloud auth print-access-token`` command failed.'''
    pass


class DefaultCredentialsError(GoogleAuthError):
    '''Used to indicate that acquiring default credentials failed.'''
    pass


class MutualTLSChannelError(GoogleAuthError):
    '''Used to indicate that mutual TLS channel creation is failed, or mutual
    TLS channel credentials is missing or invalid.'''
    pass


class ClientCertError(GoogleAuthError):
    '''Used to indicate that client certificate is missing or invalid.'''
    retryable = (lambda self: False)()


class OAuthError(GoogleAuthError):
    '''Used to indicate an error occurred during an OAuth related HTTP
    request.'''
    pass


class ReauthFailError(RefreshError):
    pass
# WARNING: Decompyle incomplete


class ReauthSamlChallengeFailError(ReauthFailError):
    '''An exception for SAML reauth challenge failures.'''
    pass


class MalformedError(ValueError, DefaultCredentialsError):
    '''An exception for malformed data.'''
    pass


class InvalidResource(ValueError, DefaultCredentialsError):
    '''An exception for URL error.'''
    pass


class InvalidOperation(ValueError, DefaultCredentialsError):
    '''An exception for invalid operation.'''
    pass


class InvalidValue(ValueError, DefaultCredentialsError):
    '''Used to wrap general ValueError of python.'''
    pass


class InvalidType(TypeError, DefaultCredentialsError):
    '''Used to wrap general TypeError of python.'''
    pass


class OSError(EnvironmentError, DefaultCredentialsError):
    '''Used to wrap EnvironmentError(OSError after python3.3).'''
    pass


class TimeoutError(GoogleAuthError):
    '''Used to indicate a timeout error occurred during an HTTP request.'''
    pass


class ResponseError(GoogleAuthError):
    '''Used to indicate an error occurred when reading an HTTP response.'''
    pass
