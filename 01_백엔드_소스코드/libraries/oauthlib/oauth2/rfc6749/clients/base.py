# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming OAuth 2.0 RFC6749.
'''
import base64
import hashlib
import time
import warnings
from oauthlib.common import UNICODE_ASCII_CHARACTER_SET, generate_token
from oauthlib.oauth2.rfc6749 import tokens
from oauthlib.oauth2.rfc6749.errors import InsecureTransportError, TokenExpiredError
from oauthlib.oauth2.rfc6749.parameters import parse_expires, parse_token_response, prepare_token_request, prepare_token_revocation_request
from oauthlib.oauth2.rfc6749.utils import is_secure_transport
AUTH_HEADER = 'auth_header'
URI_QUERY = 'query'
BODY = 'body'
FORM_ENC_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded' }

class Client:
    '''Base OAuth2 client responsible for access token management.

    This class also acts as a generic interface providing methods common to all
    client types such as ``prepare_authorization_request`` and
    ``prepare_token_revocation_request``. The ``prepare_x_request`` methods are
    the recommended way of interacting with clients (as opposed to the abstract
    prepare uri/body/etc methods). They are recommended over the older set
    because they are easier to use (more consistent) and add a few additional
    security checks, such as HTTPS and state checking.

    Some of these methods require further implementation only provided by the
    specific purpose clients such as
    :py:class:`oauthlib.oauth2.MobileApplicationClient` and thus you should always
    seek to use the client class matching the OAuth workflow you need. For
    Python, this is usually :py:class:`oauthlib.oauth2.WebApplicationClient`.

    '''
    refresh_token_key = 'refresh_token'
    
    def __init__(self, client_id, default_token_placement, token_type, access_token, refresh_token, mac_key, mac_algorithm, token, scope, state, redirect_url, state_generator, code_verifier, code_challenge, code_challenge_method = (AUTH_HEADER, 'Bearer', None, None, None, None, None, None, None, None, generate_token, None, None, None), **kwargs):
