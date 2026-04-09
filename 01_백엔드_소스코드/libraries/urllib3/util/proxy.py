# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: proxy.pyc (Python 3.11)

from __future__ import annotations
import typing
from url import Url
if typing.TYPE_CHECKING:
    from connection import ProxyConfig

def connection_requires_http_tunnel(proxy_url = None, proxy_config = None, destination_scheme = None):
    '''
    Returns True if the connection requires an HTTP CONNECT through the proxy.

    :param URL proxy_url:
        URL of the proxy.
    :param ProxyConfig proxy_config:
        Proxy configuration from poolmanager.py
    :param str destination_scheme:
        The scheme of the destination. (i.e https, http, etc)
    '''
    pass
# WARNING: Decompyle incomplete
