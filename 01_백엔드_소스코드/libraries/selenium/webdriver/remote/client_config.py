# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_config.pyc (Python 3.11)

import base64
import os
import socket
from enum import Enum
from urllib import parse
import certifi
from selenium.webdriver.common.proxy import Proxy, ProxyType

class AuthType(Enum):
    BASIC = 'Basic'
    BEARER = 'Bearer'
    X_API_KEY = 'X-API-Key'


class _ClientConfigDescriptor:
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self, obj, cls):
        return obj.__dict__[self.name]

    
    def __set__(self = None, obj = None, value = None):
        obj.__dict__[self.name] = value



class ClientConfig:
    remote_server_addr = _ClientConfigDescriptor('_remote_server_addr')
    keep_alive = _ClientConfigDescriptor('_keep_alive')
    proxy = _ClientConfigDescriptor('_proxy')
    ignore_certificates = _ClientConfigDescriptor('_ignore_certificates')
    init_args_for_pool_manager = _ClientConfigDescriptor('_init_args_for_pool_manager')
    timeout = _ClientConfigDescriptor('_timeout')
    ca_certs = _ClientConfigDescriptor('_ca_certs')
    username = _ClientConfigDescriptor('_username')
    password = _ClientConfigDescriptor('_password')
    auth_type = _ClientConfigDescriptor('_auth_type')
    token = _ClientConfigDescriptor('_token')
    user_agent = _ClientConfigDescriptor('_user_agent')
    extra_headers = _ClientConfigDescriptor('_extra_headers')
    websocket_timeout = _ClientConfigDescriptor('_websocket_timeout')
    websocket_interval = _ClientConfigDescriptor('_websocket_interval')
    
    def __init__(self, remote_server_addr, keep_alive, proxy, ignore_certificates, init_args_for_pool_manager, timeout, ca_certs, username, password, auth_type, token = None, user_agent = None, extra_headers = None, websocket_timeout = (True, Proxy(raw = {
        'proxyType': ProxyType.SYSTEM }), False, None, None, None, None, None, AuthType.BASIC, None, None, None, 30, 0.1), websocket_interval = ('remote_server_addr', str, 'keep_alive', bool | None, 'proxy', Proxy | None, 'ignore_certificates', bool | None, 'init_args_for_pool_manager', dict | None, 'timeout', int | None, 'ca_certs', str | None, 'username', str | None, 'password', str | None, 'auth_type', AuthType | None, 'token', str | None, 'user_agent', str | None, 'extra_headers', dict | None, 'websocket_timeout', float | None, 'websocket_interval', float | None, 'return', None)):
        self.remote_server_addr = remote_server_addr
        self.keep_alive = keep_alive
        self.proxy = proxy
        self.ignore_certificates = ignore_certificates
    # WARNING: Decompyle incomplete

    
    def reset_timeout(self = None):
        '''Resets the timeout to the default value of socket.'''
        self._timeout = socket.getdefaulttimeout()

    
    def get_proxy_url(self = None):
        '''Returns the proxy URL to use for the connection.'''
        proxy_type = self.proxy.proxy_type
        remote_add = parse.urlparse(self.remote_server_addr)
        if proxy_type is ProxyType.DIRECT:
            return None
        if None is ProxyType.SYSTEM:
            _no_proxy = os.environ.get('no_proxy', os.environ.get('NO_PROXY'))
            if _no_proxy:
                for entry in map(str.strip, _no_proxy.split(',')):
                    if entry == '*':
                        return None
                    n_url = None.urlparse(entry)
                    if n_url.netloc and remote_add.netloc == n_url.netloc:
                        return None
                    if None.path in remote_add.netloc:
                        return None
            return os.environ.get('https_proxy' if self.remote_server_addr.startswith('https://') else 'http_proxy', os.environ.get('HTTPS_PROXY' if self.remote_server_addr.startswith('https://') else 'HTTP_PROXY'))
        if proxy_type is ProxyType.MANUAL:
            return self.proxy.sslProxy if self.remote_server_addr.startswith('https://') else self.proxy.http_proxy

    
    def get_auth_header(self = None):
        '''Returns the authorization to add to the request headers.'''
        if self.auth_type is AuthType.BASIC and self.username and self.password:
            credentials = f'''{self.username}:{self.password}'''
            encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
            return {
                'Authorization': f'''{AuthType.BASIC.value} {encoded_credentials}''' }
        if None.auth_type is AuthType.BEARER and self.token:
            return {
                'Authorization': f'''{AuthType.BEARER.value} {self.token}''' }
        if None.auth_type is AuthType.X_API_KEY and self.token:
            return {
                f'''{AuthType.X_API_KEY.value}''': f'''{self.token}''' }
