# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interactive.pyc (Python 3.11)

'''Get user credentials from interactive code environments.

This module contains helpers for getting user credentials from interactive
code environments installed on a development machine, such as Jupyter
notebooks.
'''
from __future__ import absolute_import
import contextlib
import socket
import google_auth_oauthlib.flow as google_auth_oauthlib
LOCALHOST = 'localhost'
DEFAULT_PORTS_TO_TRY = 100

def is_port_open(port):
    '''Check if a port is open on localhost.
    Based on StackOverflow answer: https://stackoverflow.com/a/43238489/101923
    Parameters
    ----------
    port : int
        A port to check on localhost.
    Returns
    -------
    is_open : bool
        True if a socket can be opened at the requested port.
    '''
    sock = contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    sock.bind((LOCALHOST, port))
    sock.listen(1)
    is_open = True


def find_open_port(start, stop = (8080, None)):
    '''Find an open port between ``start`` and ``stop``.
    Parameters
    ----------
    start : Optional[int]
        Beginning of range of ports to try. Defaults to 8080.
    stop : Optional[int]
        End of range of ports to try (not including exactly equals ``stop``).
        This function tries 100 possible ports if no ``stop`` is specified.
    Returns
    -------
    Optional[int]
        ``None`` if no open port is found, otherwise an integer indicating an
        open port.
    '''
    if not stop:
        stop = start + DEFAULT_PORTS_TO_TRY
    for port in range(start, stop):
        if is_port_open(port):
            
            return None, port
        return None


def get_user_credentials(scopes, client_id, client_secret, minimum_port, maximum_port = (8080, None)):
    '''Gets credentials associated with your Google user account.

    This function authenticates using your user credentials by going through
    the OAuth 2.0 flow. You\'ll open a browser window to authenticate to your
    Google account. The permissions it requests correspond to the scopes
    you\'ve provided.

    To obtain the ``client_id`` and ``client_secret``, create an **OAuth
    client ID** with application type **Other** from the `Credentials page on
    the Google Developer\'s Console
    <https://console.developers.google.com/apis/credentials>`_. Learn more
    with the `Authenticating as an end user
    <https://cloud.google.com/docs/authentication/end-user>`_ guide.

    Args:
        scopes (Sequence[str]):
            A list of scopes to use when authenticating to Google APIs. See
            the `list of OAuth 2.0 scopes for Google APIs
            <https://developers.google.com/identity/protocols/googlescopes>`_.
        client_id (str):
            A string that identifies your application to Google APIs. Find
            this value in the `Credentials page on the Google Developer\'s
            Console
            <https://console.developers.google.com/apis/credentials>`_.
        client_secret (str):
            A string that verifies your application to Google APIs. Find this
            value in the `Credentials page on the Google Developer\'s Console
            <https://console.developers.google.com/apis/credentials>`_.
        minimum_port (int):
            Beginning of range of ports to try for redirect URI HTTP server.
            Defaults to 8080.
        maximum_port (Optional[int]):
            End of range of ports to try (not including exactly equals ``stop``).
            This function tries 100 possible ports if no ``stop`` is specified.

    Returns:
        google.oauth2.credentials.Credentials:
            The OAuth 2.0 credentials for the user.

    Examples:
        Get credentials for your user account and use them to run a query
        with BigQuery::

            import google_auth_oauthlib

            # TODO: Create a client ID for your project.
            client_id = "YOUR-CLIENT-ID.apps.googleusercontent.com"
            client_secret = "abc_ThIsIsAsEcReT"

            # TODO: Choose the needed scopes for your applications.
            scopes = ["https://www.googleapis.com/auth/cloud-platform"]

            credentials = google_auth_oauthlib.get_user_credentials(
                scopes, client_id, client_secret
            )

            # 1. Open the link.
            # 2. Authorize the application to have access to your account.
            # 3. Copy and paste the authorization code to the prompt.

            # Use the credentials to construct a client for Google APIs.
            from google.cloud import bigquery

            bigquery_client = bigquery.Client(
                credentials=credentials, project="your-project-id"
            )
            print(list(bigquery_client.query("SELECT 1").result()))
    '''
    client_config = {
        'installed': {
            'client_id': client_id,
            'client_secret': client_secret,
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://oauth2.googleapis.com/token' } }
    app_flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config(client_config, scopes = scopes)
    port = find_open_port(start = minimum_port, stop = maximum_port)
    if not port:
        raise ConnectionError('Could not find open port.')
    return app_flow.run_local_server(host = LOCALHOST, port = port)
