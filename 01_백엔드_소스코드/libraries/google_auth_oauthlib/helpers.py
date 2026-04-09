# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

"""Integration helpers.

This module provides helpers for integrating with `requests-oauthlib`_.
Typically, you'll want to use the higher-level helpers in
:mod:`google_auth_oauthlib.flow`.

.. _requests-oauthlib: http://requests-oauthlib.readthedocs.io/en/latest/
"""
import datetime
import json
from google.auth import external_account_authorized_user
import google.oauth2.credentials as google
import requests_oauthlib
_REQUIRED_CONFIG_KEYS = frozenset(('auth_uri', 'token_uri', 'client_id'))

def session_from_client_config(client_config, scopes, **kwargs):
    '''Creates a :class:`requests_oauthlib.OAuth2Session` from client
    configuration loaded from a Google-format client secrets file.

    Args:
        client_config (Mapping[str, Any]): The client
            configuration in the Google `client secrets`_ format.
        scopes (Sequence[str]): The list of scopes to request during the
            flow.
        kwargs: Any additional parameters passed to
            :class:`requests_oauthlib.OAuth2Session`

    Raises:
        ValueError: If the client configuration is not in the correct
            format.

    Returns:
        Tuple[requests_oauthlib.OAuth2Session, Mapping[str, Any]]: The new
            oauthlib session and the validated client configuration.

    .. _client secrets:
        https://github.com/googleapis/google-api-python-client/blob/main/docs/client-secrets.md
    '''
    if 'web' in client_config:
        config = client_config['web']
    elif 'installed' in client_config:
        config = client_config['installed']
    else:
        raise ValueError('Client secrets must be for a web or installed app.')
    if not _REQUIRED_CONFIG_KEYS.issubset(config.keys()):
        raise ValueError('Client secrets is not in the correct format.')
# WARNING: Decompyle incomplete


def session_from_client_secrets_file(client_secrets_file, scopes, **kwargs):
    '''Creates a :class:`requests_oauthlib.OAuth2Session` instance from a
    Google-format client secrets file.

    Args:
        client_secrets_file (str): The path to the `client secrets`_ .json
            file.
        scopes (Sequence[str]): The list of scopes to request during the
            flow.
        kwargs: Any additional parameters passed to
            :class:`requests_oauthlib.OAuth2Session`

    Returns:
        Tuple[requests_oauthlib.OAuth2Session, Mapping[str, Any]]: The new
            oauthlib session and the validated client configuration.

    .. _client secrets:
        https://github.com/googleapis/google-api-python-client/blob/main/docs/client-secrets.md
    '''
    json_file = open(client_secrets_file, 'r')
    client_config = json.load(json_file)
    None(None, None)
# WARNING: Decompyle incomplete


def credentials_from_session(session, client_config = (None,)):
    """Creates :class:`google.oauth2.credentials.Credentials` from a
    :class:`requests_oauthlib.OAuth2Session`.

    :meth:`fetch_token` must be called on the session before before calling
    this. This uses the session's auth token and the provided client
    configuration to create :class:`google.oauth2.credentials.Credentials`.
    This allows you to use the credentials from the session with Google
    API client libraries.

    Args:
        session (requests_oauthlib.OAuth2Session): The OAuth 2.0 session.
        client_config (Mapping[str, Any]): The subset of the client
            configuration to use. For example, if you have a web client
            you would pass in `client_config['web']`.

    Returns:
        google.oauth2.credentials.Credentials: The constructed credentials.

    Raises:
        ValueError: If there is no access token in the session.
    """
    pass
# WARNING: Decompyle incomplete
