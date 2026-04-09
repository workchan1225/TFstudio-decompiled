# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
from importlib.metadata import version
__all__ = [
    'inject_into_urllib3',
    'extract_from_urllib3']
import typing
orig_HTTPSConnection: 'typing.Any' = None

def inject_into_urllib3():
    global orig_HTTPSConnection
    h2_version = version('h2')
    if not h2_version.startswith('4.'):
        raise ImportError(f'''urllib3 v2 supports h2 version 4.x.x, currently the \'h2\' module is compiled with {h2_version!r}. See: https://github.com/urllib3/urllib3/issues/3290''')
    urllib3_connection = connection
    import 
    urllib3_util = util
    import 
    HTTPSConnectionPool = HTTPSConnectionPool
    import connectionpool
    urllib3_util_ssl = ssl_
    import util
    HTTP2Connection = HTTP2Connection
    import connection
    orig_HTTPSConnection = urllib3_connection.HTTPSConnection
    HTTPSConnectionPool.ConnectionCls = HTTP2Connection
    urllib3_connection.HTTPSConnection = HTTP2Connection
    urllib3_util.ALPN_PROTOCOLS = [
        'h2']
    urllib3_util_ssl.ALPN_PROTOCOLS = [
        'h2']


def extract_from_urllib3():
    urllib3_connection = connection
    import 
    urllib3_util = util
    import 
    HTTPSConnectionPool = HTTPSConnectionPool
    import connectionpool
    urllib3_util_ssl = ssl_
    import util
    HTTPSConnectionPool.ConnectionCls = orig_HTTPSConnection
    urllib3_connection.HTTPSConnection = orig_HTTPSConnection
    urllib3_util.ALPN_PROTOCOLS = [
        'http/1.1']
    urllib3_util_ssl.ALPN_PROTOCOLS = [
        'http/1.1']
