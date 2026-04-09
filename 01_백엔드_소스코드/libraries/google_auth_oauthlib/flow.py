# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: flow.pyc (Python 3.11)

"""OAuth 2.0 Authorization Flow

This module provides integration with `requests-oauthlib`_ for running the
`OAuth 2.0 Authorization Flow`_ and acquiring user credentials.  See
`Using OAuth 2.0 to Access Google APIs`_ for an overview of OAuth 2.0
authorization scenarios Google APIs support.

Here's an example of using :class:`InstalledAppFlow`::

    from google_auth_oauthlib.flow import InstalledAppFlow

    # Create the flow using the client secrets file from the Google API
    # Console.
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=['profile', 'email'])

    flow.run_local_server()

    # You can use flow.credentials, or you can just get a requests session
    # using flow.authorized_session.
    session = flow.authorized_session()

    profile_info = session.get(
        'https://www.googleapis.com/userinfo/v2/me').json()

    print(profile_info)
    # {'name': '...',  'email': '...', ...}

.. _requests-oauthlib: http://requests-oauthlib.readthedocs.io/en/latest/
.. _OAuth 2.0 Authorization Flow:
    https://tools.ietf.org/html/rfc6749#section-1.2
.. _Using OAuth 2.0 to Access Google APIs:
    https://developers.google.com/identity/protocols/oauth2

"""
from base64 import urlsafe_b64encode
import hashlib
import json
import logging

try:
    from secrets import SystemRandom
except ImportError:
    from random import SystemRandom

from string import ascii_letters, digits
import webbrowser
import wsgiref.simple_server as wsgiref
import wsgiref.util as wsgiref
import google.auth.transport.requests as google
import google.oauth2.credentials as google
import google_auth_oauthlib.helpers as google_auth_oauthlib
_LOGGER = logging.getLogger(__name__)

class Flow(object):
    """OAuth 2.0 Authorization Flow

    This class uses a :class:`requests_oauthlib.OAuth2Session` instance at
    :attr:`oauth2session` to perform all of the OAuth 2.0 logic. This class
    just provides convenience methods and sane defaults for doing Google's
    particular flavors of OAuth 2.0.

    Typically you'll construct an instance of this flow using
    :meth:`from_client_secrets_file` and a `client secrets file`_ obtained
    from the `Google API Console`_.

    .. _client secrets file:
        https://developers.google.com/identity/protocols/oauth2/web-server
        #creatingcred
    .. _Google API Console:
        https://console.developers.google.com/apis/credentials
    """
    
    def __init__(self, oauth2session, client_type, client_config, redirect_uri, code_verifier, autogenerate_code_verifier = (None, None, True)):
        '''
        Args:
            oauth2session (requests_oauthlib.OAuth2Session):
                The OAuth 2.0 session from ``requests-oauthlib``.
            client_type (str): The client type, either ``web`` or
                ``installed``.
            client_config (Mapping[str, Any]): The client
                configuration in the Google `client secrets`_ format.
            redirect_uri (str): The OAuth 2.0 redirect URI if known at flow
                creation time. Otherwise, it will need to be set using
                :attr:`redirect_uri`.
            code_verifier (str): random string of 43-128 chars used to verify
                the key exchange.using PKCE.
            autogenerate_code_verifier (bool): If true, auto-generate a
                code_verifier.
        .. _client secrets:
            https://github.com/googleapis/google-api-python-client/blob
            /main/docs/client-secrets.md
        '''
        self.client_type = client_type
        self.client_config = client_config[client_type]
        self.oauth2session = oauth2session
        self.redirect_uri = redirect_uri
        self.code_verifier = code_verifier
        self.autogenerate_code_verifier = autogenerate_code_verifier

    from_client_config = (lambda cls, client_config, scopes: if 'web' in client_config:
client_type = 'web'elif 'installed' in client_config:
client_type = 'installed'else:
raise ValueError('Client secrets must be for a web or installed app.')code_verifier = kwargs.pop('code_verifier', None)autogenerate_code_verifier = kwargs.pop('autogenerate_code_verifier', None)# WARNING: Decompyle incomplete
)()
    from_client_secrets_file = (lambda cls, client_secrets_file, scopes: json_file = open(client_secrets_file, 'r')client_config = json.load(json_file)None(None, None)# WARNING: Decompyle incomplete
)()
    redirect_uri = (lambda self: self.oauth2session.redirect_uri)()
    redirect_uri = (lambda self, value: self.oauth2session.redirect_uri = value)()
    
    def authorization_url(self, **kwargs):
        '''Generates an authorization URL.

        This is the first step in the OAuth 2.0 Authorization Flow. The user\'s
        browser should be redirected to the returned URL.

        This method calls
        :meth:`requests_oauthlib.OAuth2Session.authorization_url`
        and specifies the client configuration\'s authorization URI (usually
        Google\'s authorization server) and specifies that "offline" access is
        desired. This is required in order to obtain a refresh token.

        Args:
            kwargs: Additional arguments passed through to
                :meth:`requests_oauthlib.OAuth2Session.authorization_url`

        Returns:
            Tuple[str, str]: The generated authorization URL and state. The
                user must visit the URL to complete the flow. The state is used
                when completing the flow to verify that the request originated
                from your application. If your application is using a different
                :class:`Flow` instance to obtain the token, you will need to
                specify the ``state`` when constructing the :class:`Flow`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fetch_token(self, **kwargs):
        """Completes the Authorization Flow and obtains an access token.

        This is the final step in the OAuth 2.0 Authorization Flow. This is
        called after the user consents.

        This method calls
        :meth:`requests_oauthlib.OAuth2Session.fetch_token`
        and specifies the client configuration's token URI (usually Google's
        token server).

        Args:
            kwargs: Arguments passed through to
                :meth:`requests_oauthlib.OAuth2Session.fetch_token`. At least
                one of ``code`` or ``authorization_response`` must be
                specified.

        Returns:
            Mapping[str, str]: The obtained tokens. Typically, you will not use
                return value of this function and instead use
                :meth:`credentials` to obtain a
                :class:`~google.auth.credentials.Credentials` instance.
        """
        kwargs.setdefault('client_secret', self.client_config['client_secret'])
        kwargs.setdefault('code_verifier', self.code_verifier)
    # WARNING: Decompyle incomplete

    credentials = (lambda self: google_auth_oauthlib.helpers.credentials_from_session(self.oauth2session, self.client_config))()
    
    def authorized_session(self):
        """Returns a :class:`requests.Session` authorized with credentials.

        :meth:`fetch_token` must be called before this method. This method
        constructs a :class:`google.auth.transport.requests.AuthorizedSession`
        class using this flow's :attr:`credentials`.

        Returns:
            google.auth.transport.requests.AuthorizedSession: The constructed
                session.
        """
        return google.auth.transport.requests.AuthorizedSession(self.credentials)



class InstalledAppFlow(Flow):
    """Authorization flow helper for installed applications.

    This :class:`Flow` subclass makes it easier to perform the
    `Installed Application Authorization Flow`_. This flow is useful for
    local development or applications that are installed on a desktop operating
    system.

    This flow uses a local server strategy provided by :meth:`run_local_server`.

    Example::

        from google_auth_oauthlib.flow import InstalledAppFlow

        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=['profile', 'email'])

        flow.run_local_server()

        session = flow.authorized_session()

        profile_info = session.get(
            'https://www.googleapis.com/userinfo/v2/me').json()

        print(profile_info)
        # {'name': '...',  'email': '...', ...}


    Note that this isn't the only way to accomplish the installed
    application flow, just one of the most common. You can use the
    :class:`Flow` class to perform the same flow with different methods of
    presenting the authorization URL to the user or obtaining the authorization
    response, such as using an embedded web view.

    .. _Installed Application Authorization Flow:
        https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth-installed.md
    """
    _DEFAULT_AUTH_PROMPT_MESSAGE = 'Please visit this URL to authorize this application: {url}'
    _DEFAULT_AUTH_CODE_MESSAGE = 'Enter the authorization code: '
    _DEFAULT_WEB_SUCCESS_MESSAGE = 'The authentication flow has completed. You may close this window.'
    
    def run_local_server(self, host, bind_addr, port, authorization_prompt_message, success_message, open_browser, redirect_uri_trailing_slash, timeout_seconds, token_audience, browser = ('localhost', None, 8080, _DEFAULT_AUTH_PROMPT_MESSAGE, _DEFAULT_WEB_SUCCESS_MESSAGE, True, True, None, None, None), **kwargs):
        """Run the flow using the server strategy.

        The server strategy instructs the user to open the authorization URL in
        their browser and will attempt to automatically open the URL for them.
        It will start a local web server to listen for the authorization
        response. Once authorization is complete the authorization server will
        redirect the user's browser to the local web server. The web server
        will get the authorization code from the response and shutdown. The
        code is then exchanged for a token.

        Args:
            host (str): The hostname for the local redirect server. This will
                be served over http, not https.
            bind_addr (str): Optionally provide an ip address for the redirect
                server to listen on when it is not the same as host
                (e.g. in a container). Default value is None,
                which means that the redirect server will listen
                on the ip address specified in the host parameter.
            port (int): The port for the local redirect server.
            authorization_prompt_message (str | None): The message to display to tell
                the user to navigate to the authorization URL. If None or empty,
                don't display anything.
            success_message (str): The message to display in the web browser
                the authorization flow is complete.
            open_browser (bool): Whether or not to open the authorization URL
                in the user's browser.
            redirect_uri_trailing_slash (bool): whether or not to add trailing
                slash when constructing the redirect_uri. Default value is True.
            timeout_seconds (int): It will raise an error after the timeout timing
                if there are no credentials response. The value is in seconds.
                When set to None there is no timeout.
                Default value is None.
            token_audience (str): Passed along with the request for an access
                token. Determines the endpoints with which the token can be
                used. Optional.
            browser (str): specify which browser to open for authentication. If not
                specified this defaults to default browser.
            kwargs: Additional keyword arguments passed through to
                :meth:`authorization_url`.

        Returns:
            google.oauth2.credentials.Credentials: The OAuth 2.0 credentials
                for the user.
        """
        wsgi_app = _RedirectWSGIApp(success_message)
        wsgiref.simple_server.WSGIServer.allow_reuse_address = False
    # WARNING: Decompyle incomplete



class _WSGIRequestHandler(wsgiref.simple_server.WSGIRequestHandler):
    '''Custom WSGIRequestHandler.

    Uses a named logger instead of printing to stderr.
    '''
    
    def log_message(self, format, *args):
        pass
    # WARNING: Decompyle incomplete



class _RedirectWSGIApp(object):
    '''WSGI app to handle the authorization redirect.

    Stores the request URI and displays the given success message.
    '''
    
    def __init__(self, success_message):
        '''
        Args:
            success_message (str): The message to display in the web browser
                the authorization flow is complete.
        '''
        self.last_request_uri = None
        self._success_message = success_message

    
    def __call__(self, environ, start_response):
        '''WSGI Callable.

        Args:
            environ (Mapping[str, Any]): The WSGI environment.
            start_response (Callable[str, list]): The WSGI start_response
                callable.

        Returns:
            Iterable[bytes]: The response body.
        '''
        start_response('200 OK', [
            ('Content-type', 'text/plain; charset=utf-8')])
        self.last_request_uri = wsgiref.util.request_uri(environ)
        return [
            self._success_message.encode('utf-8')]
