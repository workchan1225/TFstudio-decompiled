# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _http.pyc (Python 3.11)

'''
_http.py
websocket - WebSocket client library for Python

Copyright 2025 engn33r

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import errno
import os
import socket
from base64 import encodebytes as base64encode
from _exceptions import WebSocketAddressException, WebSocketException, WebSocketProxyException
from _logging import debug, dump, trace
from _socket import DEFAULT_SOCKET_OPTION, recv_line, send
from _ssl_compat import HAVE_SSL, ssl
from _url import get_proxy_info, parse_url
__all__ = [
    'proxy_info',
    'connect',
    'read_headers']

try:
    from python_socks._errors import ProxyConnectionError, ProxyError, ProxyTimeoutError
    from python_socks._types import ProxyType
    from python_socks.sync import Proxy
    HAVE_PYTHON_SOCKS = True
except:
    HAVE_PYTHON_SOCKS = False
    
    class ProxyError(Exception):
        pass

    
    class ProxyTimeoutError(Exception):
        pass

    
    class ProxyConnectionError(Exception):
        pass



class proxy_info:
    
    def __init__(self, **options):
        self.proxy_host = options.get('http_proxy_host', None)
        if self.proxy_host:
            self.proxy_port = options.get('http_proxy_port', 0)
            self.auth = options.get('http_proxy_auth', None)
            self.no_proxy = options.get('http_no_proxy', None)
            self.proxy_protocol = options.get('proxy_type', 'http')
            self.proxy_timeout = options.get('http_proxy_timeout', None)
            if self.proxy_protocol not in ('http', 'socks4', 'socks4a', 'socks5', 'socks5h'):
                raise ProxyError('Only http, socks4, socks5 proxy protocols are supported')
            return None
        self.proxy_port = None
        self.auth = None
        self.no_proxy = None
        self.proxy_protocol = 'http'



def _start_proxied_socket(url = None, options = None, proxy = None):
    if not HAVE_PYTHON_SOCKS:
        raise WebSocketException('Python Socks is needed for SOCKS proxying but is not available')
    (hostname, port, resource, is_secure) = parse_url(url)
    if proxy.proxy_protocol == 'socks4':
        rdns = False
        proxy_type = ProxyType.SOCKS4
    elif proxy.proxy_protocol == 'socks4a':
        rdns = True
        proxy_type = ProxyType.SOCKS4
    elif proxy.proxy_protocol == 'socks5':
        rdns = False
        proxy_type = ProxyType.SOCKS5
    elif proxy.proxy_protocol == 'socks5h':
        rdns = True
        proxy_type = ProxyType.SOCKS5
    ws_proxy = Proxy.create(proxy_type = proxy_type, host = proxy.proxy_host, port = int(proxy.proxy_port), username = proxy.auth[0] if proxy.auth else None, password = proxy.auth[1] if proxy.auth else None, rdns = rdns)
    sock = ws_proxy.connect(hostname, port, timeout = proxy.proxy_timeout)
    if is_secure:
        if HAVE_SSL:
            sock = _ssl_socket(sock, options.sslopt, hostname)
        else:
            raise WebSocketException('SSL not available.')
    return (sock, (hostname, port, resource))


def connect(url = None, options = None, proxy = None, socket = ('url', str)):
    if proxy.proxy_host and socket and proxy.proxy_protocol != 'http':
        return _start_proxied_socket(url, options, proxy)
    (hostname, port_from_url, resource, is_secure) = None(url)
    if socket:
        return (socket, (hostname, port_from_url, resource))
    (addrinfo_list, need_tunnel, auth) = None(hostname, port_from_url, is_secure, proxy)
    if not addrinfo_list:
        raise WebSocketException(f'''Host not found.: {hostname}:{port_from_url}''')
    sock = None
    
    try:
        sock = _open_socket(addrinfo_list, options.sockopt, options.timeout)
        if need_tunnel:
            sock = _tunnel(sock, hostname, port_from_url, auth)
        if is_secure:
            if HAVE_SSL:
                sock = _ssl_socket(sock, options.sslopt, hostname)
            else:
                raise WebSocketException('SSL not available.')
        return (sock, (hostname, port_from_url, resource))
    except:
        if sock:
            sock.close()
        raise 



def _get_addrinfo_list(hostname = None, port = None, is_secure = None, proxy = ('port', int, 'is_secure', bool, 'return', tuple)):
    (phost, pport, pauth) = get_proxy_info(hostname, is_secure, proxy.proxy_host, proxy.proxy_port, proxy.auth, proxy.no_proxy)
    
    try:
        if not phost:
            addrinfo_list = socket.getaddrinfo(hostname, port, 0, socket.SOCK_STREAM, socket.SOL_TCP)
            return (addrinfo_list, False, None)
        if None:
            if not pport:
                pport = 80
                addrinfo_list = socket.getaddrinfo(phost, pport, 0, socket.SOCK_STREAM, socket.SOL_TCP)
                return (addrinfo_list, True, pauth)
            except socket.gaierror:
                e = None
                raise WebSocketAddressException(e)
                e = None
                del e



def _open_socket(addrinfo_list, sockopt, timeout):
    err = None
# WARNING: Decompyle incomplete


def _wrap_sni_socket(sock = None, sslopt = None, hostname = None, check_hostname = ('sock', socket.socket, 'sslopt', dict)):
    context = sslopt.get('context', None)
# WARNING: Decompyle incomplete


def _ssl_socket(sock = None, user_sslopt = None, hostname = None):
    sslopt = {
        'cert_reqs': ssl.CERT_REQUIRED }
    sslopt.update(user_sslopt)
    cert_path = os.environ.get('WEBSOCKET_CLIENT_CA_BUNDLE')
# WARNING: Decompyle incomplete


def _tunnel(sock = None, host = None, port = None, auth = ('sock', socket.socket, 'port', int, 'return', socket.socket)):
    debug('Connecting proxy...')
    connect_header = f'''CONNECT {host}:{port} HTTP/1.1\r\n'''
    connect_header += f'''Host: {host}:{port}\r\n'''
    if auth and auth[0]:
        auth_str = auth[0]
        if auth[1]:
            auth_str += f''':{auth[1]}'''
        encoded_str = base64encode(auth_str.encode()).strip().decode().replace('\n', '')
        connect_header += f'''Proxy-Authorization: Basic {encoded_str}\r\n'''
    connect_header += '\r\n'
    dump('request header', connect_header)
    send(sock, connect_header)
    
    try:
        (status, _, _) = read_headers(sock)
    except (socket.error, WebSocketException):
        e = None
        raise WebSocketProxyException(str(e))
        e = None
        del e

    if status != 200:
        raise WebSocketProxyException(f'''failed CONNECT via proxy status: {status}''')
    return sock


def read_headers(sock = None):
    status = None
    status_message = None
    headers = { }
    trace('--- response header ---')
    line = recv_line(sock)
    line = line.decode('utf-8').strip()
    if not line:
        pass
# WARNING: Decompyle incomplete
