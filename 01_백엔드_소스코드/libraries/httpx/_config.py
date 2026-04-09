# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _config.pyc (Python 3.11)

from __future__ import annotations
import os
import typing
from _models import Headers
from _types import CertTypes, HeaderTypes, TimeoutTypes
from _urls import URL
if typing.TYPE_CHECKING:
    import ssl
__all__ = [
    'Limits',
    'Proxy',
    'Timeout',
    'create_ssl_context']

class UnsetType:
    pass

UNSET = UnsetType()

def create_ssl_context(verify = None, cert = None, trust_env = None):
    import ssl
    import warnings
    import certifi
    if verify is True:
        if trust_env and os.environ.get('SSL_CERT_FILE'):
            ctx = ssl.create_default_context(cafile = os.environ['SSL_CERT_FILE'])
        elif trust_env and os.environ.get('SSL_CERT_DIR'):
            ctx = ssl.create_default_context(capath = os.environ['SSL_CERT_DIR'])
        else:
            ctx = ssl.create_default_context(cafile = certifi.where())
    elif verify is False:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    elif isinstance(verify, str):
        message = '`verify=<str>` is deprecated. Use `verify=ssl.create_default_context(cafile=...)` or `verify=ssl.create_default_context(capath=...)` instead.'
        warnings.warn(message, DeprecationWarning)
        if os.path.isdir(verify):
            return ssl.create_default_context(capath = verify)
        return ssl.create_default_context(cafile = verify)
    ctx = verify
# WARNING: Decompyle incomplete


class Timeout:
    '''
    Timeout configuration.

    **Usage**:

    Timeout(None)               # No timeouts.
    Timeout(5.0)                # 5s timeout on all operations.
    Timeout(None, connect=5.0)  # 5s timeout on connect, no other timeouts.
    Timeout(5.0, connect=10.0)  # 10s timeout on connect. 5s timeout elsewhere.
    Timeout(5.0, pool=None)     # No timeout on acquiring connection from pool.
                                # 5s timeout elsewhere.
    '''
    
    def __init__(self = None, timeout = None, *, connect, read, write, pool):
        pass
    # WARNING: Decompyle incomplete

    
    def as_dict(self = None):
        return {
            'connect': self.connect,
            'read': self.read,
            'write': self.write,
            'pool': self.pool }

    
    def __eq__(self = None, other = None):
