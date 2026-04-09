# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from connection import HTTPConnection
from connection_pool import ConnectionPool
from http11 import HTTP11Connection
from http_proxy import HTTPProxy
from interfaces import ConnectionInterface

try:
    from http2 import HTTP2Connection
except ImportError:
    
    class HTTP2Connection:
        
        def __init__(self = None, *args, **kwargs):
            raise RuntimeError("Attempted to use http2 support, but the `h2` package is not installed. Use 'pip install httpcore[http2]'.")




try:
    from socks_proxy import SOCKSProxy
except ImportError:
    
    class SOCKSProxy:
        
        def __init__(self = None, *args, **kwargs):
            raise RuntimeError("Attempted to use SOCKS support, but the `socksio` package is not installed. Use 'pip install httpcore[socks]'.")



__all__ = [
    'HTTPConnection',
    'ConnectionPool',
    'HTTPProxy',
    'HTTP11Connection',
    'HTTP2Connection',
    'ConnectionInterface',
    'SOCKSProxy']
