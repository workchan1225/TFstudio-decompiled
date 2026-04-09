# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _auth.pyc (Python 3.11)

from __future__ import annotations
import hashlib
import os
import re
import time
import typing
from base64 import b64encode
from urllib.request import parse_http_list
from _exceptions import ProtocolError
from _models import Cookies, Request, Response
from _utils import to_bytes, to_str, unquote
if typing.TYPE_CHECKING:
    from hashlib import _Hash
__all__ = [
    'Auth',
    'BasicAuth',
    'DigestAuth',
    'NetRCAuth']

class Auth:
    '''
    Base class for all authentication schemes.

    To implement a custom authentication scheme, subclass `Auth` and override
    the `.auth_flow()` method.

    If the authentication scheme does I/O such as disk access or network calls, or uses
    synchronization primitives such as locks, you should override `.sync_auth_flow()`
    and/or `.async_auth_flow()` instead of `.auth_flow()` to provide specialized
    implementations that will be used by `Client` and `AsyncClient` respectively.
    '''
    requires_request_body = False
    requires_response_body = False
    
    def auth_flow(self = None, request = None):
        '''
        Execute the authentication flow.

        To dispatch a request, `yield` it:

        ```
        yield request
        ```

        The client will `.send()` the response back into the flow generator. You can
        access it like so:

        ```
        response = yield request
        ```

        A `return` (or reaching the end of the generator) will result in the
        client returning the last response obtained from the server.

        You can dispatch as many requests as is necessary.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def sync_auth_flow(self = None, request = None):
        '''
        Execute the authentication flow synchronously.

        By default, this defers to `.auth_flow()`. You should override this method
        when the authentication scheme does I/O and/or uses concurrency primitives.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def async_auth_flow(self = None, request = None):
        '''
        Execute the authentication flow asynchronously.

        By default, this defers to `.auth_flow()`. You should override this method
        when the authentication scheme does I/O and/or uses concurrency primitives.
        '''
        pass
    # WARNING: Decompyle incomplete



class FunctionAuth(Auth):
    """
    Allows the 'auth' argument to be passed as a simple callable function,
    that takes the request, and returns a new, modified request.
    """
    
    def __init__(self = None, func = None):
        self._func = func

    
    def auth_flow(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete



class BasicAuth(Auth):
    """
    Allows the 'auth' argument to be passed as a (username, password) pair,
    and uses HTTP Basic authentication.
    """
    
    def __init__(self = None, username = None, password = None):
        self._auth_header = self._build_auth_header(username, password)

    
    def auth_flow(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _build_auth_header(self = None, username = None, password = None):
        userpass = b':'.join((to_bytes(username), to_bytes(password)))
        token = b64encode(userpass).decode()
        return f'''Basic {token}'''



class NetRCAuth(Auth):
    """
    Use a 'netrc' file to lookup basic auth credentials based on the url host.
    """
    
    def __init__(self = None, file = None):
        import netrc
        self._netrc_info = netrc.netrc(file)

    
    def auth_flow(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _build_auth_header(self = None, username = None, password = None):
        userpass = b':'.join((to_bytes(username), to_bytes(password)))
        token = b64encode(userpass).decode()
        return f'''Basic {token}'''



class DigestAuth(Auth):
    _ALGORITHM_TO_HASH_FUNCTION: 'dict[str, typing.Callable[[bytes], _Hash]]' = {
        'MD5': hashlib.md5,
        'MD5-SESS': hashlib.md5,
        'SHA': hashlib.sha1,
        'SHA-SESS': hashlib.sha1,
        'SHA-256': hashlib.sha256,
        'SHA-256-SESS': hashlib.sha256,
        'SHA-512': hashlib.sha512,
        'SHA-512-SESS': hashlib.sha512 }
    
    def __init__(self = None, username = None, password = None):
        self._username = to_bytes(username)
        self._password = to_bytes(password)
        self._last_challenge = None
        self._nonce_count = 1

    
    def auth_flow(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_challenge(self = None, request = None, response = None, auth_header = ('request', 'Request', 'response', 'Response', 'auth_header', 'str', 'return', '_DigestAuthChallenge')):
        '''
        Returns a challenge from a Digest WWW-Authenticate header.
        These take the form of:
        `Digest realm="realm@host.com",qop="auth,auth-int",nonce="abc",opaque="xyz"`
        '''
        (scheme, _, fields) = auth_header.partition(' ')
    # WARNING: Decompyle incomplete

    
    def _build_auth_header(self = None, request = None, challenge = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_client_nonce(self = None, nonce_count = None, nonce = None):
        s = str(nonce_count).encode()
        s += nonce
        s += time.ctime().encode()
        s += os.urandom(8)
        return hashlib.sha1(s).hexdigest()[:16].encode()

    
    def _get_header_value(self = None, header_fields = None):
        NON_QUOTED_FIELDS = ('algorithm', 'qop', 'nc')
        QUOTED_TEMPLATE = '{}="{}"'
        NON_QUOTED_TEMPLATE = '{}={}'
        header_value = ''
        for field, value in enumerate(header_fields.items()):
            if i > 0:
                header_value += ', '
            template = QUOTED_TEMPLATE if field not in NON_QUOTED_FIELDS else NON_QUOTED_TEMPLATE
            header_value += template.format(field, to_str(value))
            return header_value

    
    def _resolve_qop(self = None, qop = None, request = None):
        pass
    # WARNING: Decompyle incomplete



class _DigestAuthChallenge(typing.NamedTuple):
    qop: 'bytes | None' = '_DigestAuthChallenge'
