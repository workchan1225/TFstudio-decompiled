# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: uri.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import urllib.parse as urllib
import urllib.request as urllib
from exceptions import InvalidProxy, InvalidURI
__all__ = [
    'parse_uri',
    'WebSocketURI']
DELIMS = ":/?#[]@!$&'()*+,;="
WebSocketURI = <NODE:12>()

def parse_uri(uri = None):
    """
    Parse and validate a WebSocket URI.

    Args:
        uri: WebSocket URI.

    Returns:
        Parsed WebSocket URI.

    Raises:
        InvalidURI: If ``uri`` isn't a valid WebSocket URI.

    """
    parsed = urllib.parse.urlparse(uri)
    if parsed.scheme not in ('ws', 'wss'):
        raise InvalidURI(uri, "scheme isn't ws or wss")
# WARNING: Decompyle incomplete

Proxy = <NODE:12>()

def parse_proxy(proxy = None):
    """
    Parse and validate a proxy.

    Args:
        proxy: proxy.

    Returns:
        Parsed proxy.

    Raises:
        InvalidProxy: If ``proxy`` isn't a valid proxy.

    """
    parsed = urllib.parse.urlparse(proxy)
    if parsed.scheme not in ('socks5h', 'socks5', 'socks4a', 'socks4', 'https', 'http'):
        raise InvalidProxy(proxy, f'''scheme {parsed.scheme} isn\'t supported''')
# WARNING: Decompyle incomplete


def get_proxy(uri = None):
    '''
    Return the proxy to use for connecting to the given WebSocket URI, if any.

    '''
    if urllib.request.proxy_bypass(f'''{uri.host}:{uri.port}'''):
        return None
    proxies = None.request.getproxies()
    if uri.secure:
        schemes = [
            'wss',
            'socks',
            'https']
    else:
        schemes = [
            'ws',
            'socks',
            'https',
            'http']
# WARNING: Decompyle incomplete
