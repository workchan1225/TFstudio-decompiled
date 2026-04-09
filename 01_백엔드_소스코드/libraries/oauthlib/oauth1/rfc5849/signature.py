# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: signature.pyc (Python 3.11)

'''
This module is an implementation of `section 3.4`_ of RFC 5849.

**Usage**

Steps for signing a request:

1. Collect parameters from the request using ``collect_parameters``.
2. Normalize those parameters using ``normalize_parameters``.
3. Create the *base string URI* using ``base_string_uri``.
4. Create the *signature base string* from the above three components
   using ``signature_base_string``.
5. Pass the *signature base string* and the client credentials to one of the
   sign-with-client functions. The HMAC-based signing functions needs
   client credentials with secrets. The RSA-based signing functions needs
   client credentials with an RSA private key.

To verify a request, pass the request and credentials to one of the verify
functions. The HMAC-based signing functions needs the shared secrets. The
RSA-based verify functions needs the RSA public key.

**Scope**

All of the functions in this module should be considered internal to OAuthLib,
since they are not imported into the "oauthlib.oauth1" module. Programs using
OAuthLib should not use directly invoke any of the functions in this module.

**Deprecated functions**

The "sign_" methods that are not "_with_client" have been deprecated. They may
be removed in a future release. Since they are all internal functions, this
should have no impact on properly behaving programs.

.. _`section 3.4`: https://tools.ietf.org/html/rfc5849#section-3.4
'''
import binascii
import hashlib
import hmac
import ipaddress
import logging
from urllib.parse import parse as urlparse
import warnings
from oauthlib.common import extract_params, safe_string_equals, urldecode
from  import utils
import contextlib
log = logging.getLogger(__name__)

def signature_base_string(http_method = None, base_str_uri = None, normalized_encoded_request_parameters = None):
    """
    Construct the signature base string.

    The *signature base string* is the value that is calculated and signed by
    the client. It is also independently calculated by the server to verify
    the signature, and therefore must produce the exact same value at both
    ends or the signature won't verify.

    The rules for calculating the *signature base string* are defined in
    section 3.4.1.1`_ of RFC 5849.

    .. _`section 3.4.1.1`: https://tools.ietf.org/html/rfc5849#section-3.4.1.1
    """
    base_string = utils.escape(http_method.upper())
    base_string += '&'
    base_string += utils.escape(base_str_uri)
    base_string += '&'
    base_string += utils.escape(normalized_encoded_request_parameters)
    return base_string


def base_string_uri(uri = None, host = None):
    '''
    Calculates the _base string URI_.

    The *base string URI* is one of the components that make up the
     *signature base string*.

    The ``host`` is optional. If provided, it is used to override any host and
    port values in the ``uri``. The value for ``host`` is usually extracted from
    the "Host" request header from the HTTP request. Its value may be just the
    hostname, or the hostname followed by a colon and a TCP/IP port number
    (hostname:port). If a value for the``host`` is provided but it does not
    contain a port number, the default port number is used (i.e. if the ``uri``
    contained a port number, it will be discarded).

    The rules for calculating the *base string URI* are defined in
    section 3.4.1.2`_ of RFC 5849.

    .. _`section 3.4.1.2`: https://tools.ietf.org/html/rfc5849#section-3.4.1.2

    :param uri: URI
    :param host: hostname with optional port number, separated by a colon
    :return: base string URI
    '''
    if not isinstance(uri, str):
        raise ValueError('uri must be a string.')
    output = urlparse.urlparse(uri)
    scheme = output.scheme
    hostname = output.hostname
    port = output.port
    path = output.path
    params = output.params
    if not scheme:
        raise ValueError('missing scheme')
    if not path:
        path = '/'
    scheme = scheme.lower()
# WARNING: Decompyle incomplete


def collect_parameters(uri_query, body, headers, exclude_oauth_signature, with_realm = ('', None, None, True, False)):
    '''
    Gather the request parameters from all the parameter sources.

    This function is used to extract all the parameters, which are then passed
    to ``normalize_parameters`` to produce one of the components that make up
    the *signature base string*.

    Parameters starting with `oauth_` will be unescaped.

    Body parameters must be supplied as a dict, a list of 2-tuples, or a
    form encoded query string.

    Headers must be supplied as a dict.

    The rules where the parameters must be sourced from are defined in
    `section 3.4.1.3.1`_ of RFC 5849.

    .. _`Sec 3.4.1.3.1`: https://tools.ietf.org/html/rfc5849#section-3.4.1.3.1
    '''
    pass
# WARNING: Decompyle incomplete


def normalize_parameters(params = None):
    '''
    Calculate the normalized request parameters.

    The *normalized request parameters* is one of the components that make up
    the *signature base string*.

    The rules for parameter normalization are defined in `section 3.4.1.3.2`_ of
    RFC 5849.

    .. _`Sec 3.4.1.3.2`: https://tools.ietf.org/html/rfc5849#section-3.4.1.3.2
    '''
    key_values = params()
    key_values.sort()
    parameter_parts = key_values()
    return '&'.join(parameter_parts)


def _sign_hmac(hash_algorithm_name = None, sig_base_str = None, client_secret = None, resource_owner_secret = ('hash_algorithm_name', str, 'sig_base_str', str, 'client_secret', str, 'resource_owner_secret', str)):
