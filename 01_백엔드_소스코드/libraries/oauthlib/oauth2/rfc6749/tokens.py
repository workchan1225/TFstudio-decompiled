# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tokens.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749.tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains methods for adding two types of access tokens to requests.

- Bearer https://tools.ietf.org/html/rfc6750
- MAC https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01
'''
import hashlib
import hmac
import warnings
from binascii import b2a_base64
from urllib.parse import urlparse
from oauthlib import common
from oauthlib.common import add_params_to_qs, add_params_to_uri
from  import utils

class OAuth2Token(dict):
    pass
# WARNING: Decompyle incomplete


def prepare_mac_header(token, uri, key, http_method, nonce, headers, body, ext, hash_algorithm, issue_time, draft = (None, None, None, '', 'hmac-sha-1', None, 0)):
    '''Add an `MAC Access Authentication`_ signature to headers.

    Unlike OAuth 1, this HMAC signature does not require inclusion of the
    request payload/body, neither does it use a combination of client_secret
    and token_secret but rather a mac_key provided together with the access
    token.

    Currently two algorithms are supported, "hmac-sha-1" and "hmac-sha-256",
    `extension algorithms`_ are not supported.

    Example MAC Authorization header, linebreaks added for clarity

    Authorization: MAC id="h480djs93hd8",
                       nonce="1336363200:dj83hs9s",
                       mac="bhCQXTVyfj5cmA9uKkPFx1zeOXM="

    .. _`MAC Access Authentication`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01
    .. _`extension algorithms`: https://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01#section-7.1

    :param token:
    :param uri: Request URI.
    :param key: MAC given provided by token endpoint.
    :param http_method: HTTP Request method.
    :param nonce:
    :param headers: Request headers as a dictionary.
    :param body:
    :param ext:
    :param hash_algorithm: HMAC algorithm provided by token endpoint.
    :param issue_time: Time when the MAC credentials were issued (datetime).
    :param draft: MAC authentication specification version.
    :return: headers dictionary with the authorization field added.
    '''
    http_method = http_method.upper()
    (host, port) = utils.host_from_uri(uri)
    if hash_algorithm.lower() == 'hmac-sha-1':
        h = hashlib.sha1
    elif hash_algorithm.lower() == 'hmac-sha-256':
        h = hashlib.sha256
    else:
        raise ValueError('unknown hash algorithm')
    if draft == 0:
        pass
    (sch, net, path, par, query, fra) = urlparse(uri)
    request_uri = path + '?' + query if query else path
# WARNING: Decompyle incomplete


def prepare_bearer_uri(token, uri):
    """Add a `Bearer Token`_ to the request URI.
    Not recommended, use only if client can't use authorization header or body.

    http://www.example.com/path?access_token=h480djs93hd8

    .. _`Bearer Token`: https://tools.ietf.org/html/rfc6750

    :param token:
    :param uri:
    """
    return add_params_to_uri(uri, [
        ('access_token', token)])


def prepare_bearer_headers(token, headers = (None,)):
