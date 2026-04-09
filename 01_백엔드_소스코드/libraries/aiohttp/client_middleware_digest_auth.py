# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_middleware_digest_auth.pyc (Python 3.11)

"""
Digest authentication middleware for aiohttp client.

This middleware implements HTTP Digest Authentication according to RFC 7616,
providing a more secure alternative to Basic Authentication. It supports all
standard hash algorithms including MD5, SHA, SHA-256, SHA-512 and their session
variants, as well as both 'auth' and 'auth-int' quality of protection (qop) options.
"""
import hashlib
import os
import re
import time
from typing import Callable, Dict, Final, FrozenSet, List, Literal, Tuple, TypedDict, Union
from yarl import URL
from  import hdrs
from client_exceptions import ClientError
from client_middlewares import ClientHandlerType
from client_reqrep import ClientRequest, ClientResponse
from payload import Payload

def DigestAuthChallenge():
    '''DigestAuthChallenge'''
    stale: str = 'DigestAuthChallenge'

DigestAuthChallenge = <NODE:27>(DigestAuthChallenge, 'DigestAuthChallenge', TypedDict, total = False)
DigestFunctions: Dict[(str, Callable[([
    bytes], 'hashlib._Hash')])] = {
    'MD5': hashlib.md5,
    'MD5-SESS': hashlib.md5,
    'SHA': hashlib.sha1,
    'SHA-SESS': hashlib.sha1,
    'SHA256': hashlib.sha256,
    'SHA256-SESS': hashlib.sha256,
    'SHA-256': hashlib.sha256,
    'SHA-256-SESS': hashlib.sha256,
    'SHA512': hashlib.sha512,
    'SHA512-SESS': hashlib.sha512,
    'SHA-512': hashlib.sha512,
    'SHA-512-SESS': hashlib.sha512 }
_HEADER_PAIRS_PATTERN = re.compile('(\\w+)\\s*=\\s*(?:"((?:[^"\\\\]|\\\\.)*)"|([^\\s,]+))')
CHALLENGE_FIELDS: Final[Tuple[(Literal[('realm', 'nonce', 'qop', 'algorithm', 'opaque', 'domain', 'stale')], ...)]] = ('realm', 'nonce', 'qop', 'algorithm', 'opaque', 'domain', 'stale')
SUPPORTED_ALGORITHMS: Final[Tuple[(str, ...)]] = tuple(sorted(DigestFunctions.keys()))
QUOTED_AUTH_FIELDS: Final[FrozenSet[str]] = frozenset({
    'uri',
    'nonce',
    'realm',
    'cnonce',
    'opaque',
    'response',
    'username'})

def escape_quotes(value = None):
    '''Escape double quotes for HTTP header values.'''
    return value.replace('"', '\\"')


def unescape_quotes(value = None):
    '''Unescape double quotes in HTTP header values.'''
    return value.replace('\\"', '"')


def parse_header_pairs(header = None):
    '''
    Parse key-value pairs from WWW-Authenticate or similar HTTP headers.

    This function handles the complex format of WWW-Authenticate header values,
    supporting both quoted and unquoted values, proper handling of commas in
    quoted values, and whitespace variations per RFC 7616.

    Examples of supported formats:
      - key1="value1", key2=value2
      - key1 = "value1" , key2="value, with, commas"
      - key1=value1,key2="value2"
      - realm="example.com", nonce="12345", qop="auth"

    Args:
        header: The header value string to parse

    Returns:
        Dictionary mapping parameter names to their values
    '''
    pass
# WARNING: Decompyle incomplete


class DigestAuthMiddleware:
    """
    HTTP digest authentication middleware for aiohttp client.

    This middleware intercepts 401 Unauthorized responses containing a Digest
    authentication challenge, calculates the appropriate digest credentials,
    and automatically retries the request with the proper Authorization header.

    Features:
    - Handles all aspects of Digest authentication handshake automatically
    - Supports all standard hash algorithms:
      - MD5, MD5-SESS
      - SHA, SHA-SESS
      - SHA256, SHA256-SESS, SHA-256, SHA-256-SESS
      - SHA512, SHA512-SESS, SHA-512, SHA-512-SESS
    - Supports 'auth' and 'auth-int' quality of protection modes
    - Properly handles quoted strings and parameter parsing
    - Includes replay attack protection with client nonce count tracking
    - Supports preemptive authentication per RFC 7616 Section 3.6

    Standards compliance:
    - RFC 7616: HTTP Digest Access Authentication (primary reference)
    - RFC 2617: HTTP Authentication (deprecated by RFC 7616)
    - RFC 1945: Section 11.1 (username restrictions)

    Implementation notes:
    The core digest calculation is inspired by the implementation in
    https://github.com/requests/requests/blob/v2.18.4/requests/auth.py
    with added support for modern digest auth features and error handling.
    """
    
    def __init__(self = None, login = None, password = None, preemptive = (True,)):
        pass
    # WARNING: Decompyle incomplete

    
    async def _encode(self = None, method = None, url = None, body = ('method', str, 'url', URL, 'body', Union[(Payload, Literal[b''])], 'return', str)):
        '''
        Build digest authorization header for the current challenge.

        Args:
            method: The HTTP method (GET, POST, etc.)
            url: The request URL
            body: The request body (used for qop=auth-int)

        Returns:
            A fully formatted Digest authorization header string

        Raises:
            ClientError: If the challenge is missing required parameters or
                         contains unsupported values

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _in_protection_space(self = None, url = None):
        '''
        Check if the given URL is within the current protection space.

        According to RFC 7616, a URI is in the protection space if any URI
        in the protection space is a prefix of it (after both have been made absolute).
        '''
        request_str = str(url)
        for space_str in self._protection_space:
            if not request_str.startswith(space_str):
                continue
            if len(request_str) == len(space_str) or space_str[-1] == '/':
                return True
            if None[len(space_str)] == '/':
                return True
            return False

    
    def _authenticate(self = None, response = None):
        '''
        Takes the given response and tries digest-auth, if needed.

        Returns true if the original request must be resent.
        '''
        if response.status != 401:
            return False
        auth_header = None.headers.get('www-authenticate', '')
        if not auth_header:
            return False
        (method, sep, headers) = None.partition(' ')
        if not sep:
            return False
        if None.lower() != 'digest':
            return False
        if not None:
            return False
        header_pairs = None(headers)
        if not None(headers):
            return False
        self._challenge = None
        for field in CHALLENGE_FIELDS:
            value = header_pairs.get(field)
            if header_pairs.get(field):
                self._challenge[field] = value
            origin = response.url.origin()
            domain = self._challenge.get('domain')
            if self._challenge.get('domain'):
                self._protection_space = []
                for uri in domain.split():
                    uri = uri.strip('"')
                    if uri.startswith('/'):
                        self._protection_space.append(str(origin.join(URL(uri))))
                        continue
                    self._protection_space.append(str(URL(uri)))
        self._protection_space = [
            str(origin)]
        return bool(self._challenge)

    
    async def __call__(self = None, request = None, handler = None):
        '''Run the digest auth middleware.'''
        pass
    # WARNING: Decompyle incomplete
