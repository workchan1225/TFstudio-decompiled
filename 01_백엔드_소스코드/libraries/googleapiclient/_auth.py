# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _auth.pyc (Python 3.11)

'''Helpers for authentication using oauth2client or google-auth.'''
import httplib2

try:
    import google.auth as google
    import google.auth.credentials as google
    HAS_GOOGLE_AUTH = True
except ImportError:
    HAS_GOOGLE_AUTH = False


try:
    import google_auth_httplib2
except ImportError:
    google_auth_httplib2 = None


try:
    import oauth2client
    import oauth2client.client as oauth2client
    HAS_OAUTH2CLIENT = True
except ImportError:
    HAS_OAUTH2CLIENT = False


def credentials_from_file(filename, scopes, quota_project_id = (None, None)):
    '''Returns credentials loaded from a file.'''
    if HAS_GOOGLE_AUTH:
        (credentials, _) = google.auth.load_credentials_from_file(filename, scopes = scopes, quota_project_id = quota_project_id)
        return credentials
    raise None('client_options.credentials_file is only supported in google-auth.')


def default_credentials(scopes, quota_project_id = (None, None)):
    '''Returns Application Default Credentials.'''
    if HAS_GOOGLE_AUTH:
        (credentials, _) = google.auth.default(scopes = scopes, quota_project_id = quota_project_id)
        return credentials
# WARNING: Decompyle incomplete


def with_scopes(credentials, scopes):
    '''Scopes the credentials if necessary.

    Args:
        credentials (Union[
            google.auth.credentials.Credentials,
            oauth2client.client.Credentials]): The credentials to scope.
        scopes (Sequence[str]): The list of scopes.

    Returns:
        Union[google.auth.credentials.Credentials,
            oauth2client.client.Credentials]: The scoped credentials.
    '''
    if HAS_GOOGLE_AUTH and isinstance(credentials, google.auth.credentials.Credentials):
        return google.auth.credentials.with_scopes_if_required(credentials, scopes)
    
    try:
        if credentials.create_scoped_required():
            return credentials.create_scoped(scopes)
        return None
    except AttributeError:
        return 



def authorized_http(credentials):
    '''Returns an http client that is authorized with the given credentials.

    Args:
        credentials (Union[
            google.auth.credentials.Credentials,
            oauth2client.client.Credentials]): The credentials to use.

    Returns:
        Union[httplib2.Http, google_auth_httplib2.AuthorizedHttp]: An
            authorized http client.
    '''
    build_http = build_http
    import googleapiclient.http
# WARNING: Decompyle incomplete


def refresh_credentials(credentials):
    refresh_http = httplib2.Http()
    if HAS_GOOGLE_AUTH and isinstance(credentials, google.auth.credentials.Credentials):
        request = google_auth_httplib2.Request(refresh_http)
        return credentials.refresh(request)
    return None.refresh(refresh_http)


def apply_credentials(credentials, headers):
    if not is_valid(credentials):
        refresh_credentials(credentials)
    return credentials.apply(headers)


def is_valid(credentials):
