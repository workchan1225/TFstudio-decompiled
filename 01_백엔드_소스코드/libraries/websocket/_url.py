# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _url.pyc (Python 3.11)

import ipaddress
import os
from typing import Optional
from urllib.parse import unquote, urlparse
from _exceptions import WebSocketProxyException
__all__ = [
    'parse_url',
    'get_proxy_info']

def parse_url(url = None):
    '''
    parse url and the result is tuple of
    (hostname, port, resource path and the flag of secure mode)

    Parameters
    ----------
    url: str
        url string.
    '''
    if ':' not in url:
        raise ValueError('url is invalid')
    (scheme, url) = url.split(':', 1)
    parsed = urlparse(url, scheme = 'http')
    if parsed.hostname:
        hostname = parsed.hostname
    else:
        raise ValueError('hostname is invalid')
    port = 0
    if parsed.port:
        port = parsed.port
    is_secure = False
    if scheme == 'ws':
        if not port:
            port = 80
        elif scheme == 'wss':
            is_secure = True
            if not port:
                port = 443
            else:
                raise ValueError('scheme %s is invalid' % scheme)
            if parsed.path:
                resource = parsed.path
            else:
                resource = '/'
    if parsed.query:
        resource += f'''?{parsed.query}'''
    return (hostname, port, resource, is_secure)


def _is_ip_address(addr = None):
    if not isinstance(addr, str):
        raise TypeError('_is_ip_address() argument 1 must be str')
    
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False



def _is_subnet_address(hostname = None):
    
    try:
        ipaddress.ip_network(hostname)
        return True
    except ValueError:
        return False



def _is_address_in_network(ip = None, net = None):
    
    try:
        return ipaddress.ip_network(ip).subnet_of(ipaddress.ip_network(net))
    except TypeError:
        return False



def _is_no_proxy_host(hostname = None, no_proxy = None):
    pass
# WARNING: Decompyle incomplete


def get_proxy_info(hostname, is_secure, proxy_host = None, proxy_port = None, proxy_auth = None, no_proxy = (None, 0, None, None, 'http'), proxy_type = ('hostname', str, 'is_secure', bool, 'proxy_host', Optional[str], 'proxy_port', int, 'proxy_auth', Optional[tuple], 'no_proxy', Optional[list[str]], 'proxy_type', str, 'return', tuple)):
    '''
    Try to retrieve proxy host and port from environment
    if not provided in options.
    Result is (proxy_host, proxy_port, proxy_auth).
    proxy_auth is tuple of username and password
    of proxy authentication information.

    Parameters
    ----------
    hostname: str
        Websocket server name.
    is_secure: bool
        Is the connection secure? (wss) looks for "https_proxy" in env
        instead of "http_proxy"
    proxy_host: str
        http proxy host name.
    proxy_port: str or int
        http proxy port.
    no_proxy: list
        Whitelisted host names that don\'t use the proxy.
    proxy_auth: tuple
        HTTP proxy auth information. Tuple of username and password. Default is None.
    proxy_type: str
        Specify the proxy protocol (http, socks4, socks4a, socks5, socks5h). Default is "http".
        Use socks4a or socks5h if you want to send DNS requests through the proxy.
    '''
    if _is_no_proxy_host(hostname, no_proxy):
        return (None, 0, None)
    if None:
        if not proxy_port:
            raise WebSocketProxyException('Cannot use port 0 when proxy_host specified')
        port = proxy_port
        auth = proxy_auth
        return (proxy_host, port, auth)
    env_key = 'https_proxy' if None else 'http_proxy'
    value = os.environ.get(env_key, os.environ.get(env_key.upper(), '')).replace(' ', '')
    if value:
        proxy = urlparse(value)
        if proxy.username:
            pass
        auth = (unquote(''), unquote('')) if not proxy.username and proxy.password else None
        return (proxy.hostname, proxy.port, auth)
