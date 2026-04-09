# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _handshake.pyc (Python 3.11)

'''
_handshake.py
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
import hashlib
import hmac
import os
from base64 import encodebytes as base64encode
from http import HTTPStatus
from _cookiejar import SimpleCookieJar
from _exceptions import WebSocketException, WebSocketBadStatusException
from _http import read_headers
from _logging import dump, error
from _socket import send
__all__ = [
    'handshake_response',
    'handshake',
    'SUPPORTED_REDIRECT_STATUSES']
VERSION = 13
SUPPORTED_REDIRECT_STATUSES = (HTTPStatus.MOVED_PERMANENTLY, HTTPStatus.FOUND, HTTPStatus.SEE_OTHER, HTTPStatus.TEMPORARY_REDIRECT, HTTPStatus.PERMANENT_REDIRECT)
SUCCESS_STATUSES = SUPPORTED_REDIRECT_STATUSES + (HTTPStatus.SWITCHING_PROTOCOLS,)
CookieJar = SimpleCookieJar()

class handshake_response:
    
    def __init__(self = None, status = None, headers = None, subprotocol = ('status', int, 'headers', dict)):
        self.status = status
        self.headers = headers
        self.subprotocol = subprotocol
        CookieJar.add(headers.get('set-cookie'))



def handshake(sock, url = None, hostname = None, port = None, resource = ('url', str, 'hostname', str, 'port', int, 'resource', str, 'return', handshake_response), **options):
    (headers, key) = _get_handshake_headers(resource, url, hostname, port, options)
    header_str = '\r\n'.join(headers)
    send(sock, header_str)
    dump('request header', header_str)
    (status, resp) = _get_resp_headers(sock)
    if status in SUPPORTED_REDIRECT_STATUSES:
        return handshake_response(status, resp, None)
    (success, subproto) = None(resp, key, options.get('subprotocols'))
    if not success:
        raise WebSocketException('Invalid WebSocket Header')
    return handshake_response(status, resp, subproto)


def _pack_hostname(hostname = None):
    if ':' in hostname:
        return f'''[{hostname}]'''


def _get_handshake_headers(resource, url = None, host = None, port = None, options = ('resource', str, 'url', str, 'host', str, 'port', int, 'options', dict, 'return', tuple)):
    headers = [
        f'''GET {resource} HTTP/1.1''',
        'Upgrade: websocket']
    if port in (80, 443):
        hostport = _pack_hostname(host)
    else:
        hostport = f'''{_pack_hostname(host)}:{port}'''
    if options.get('host'):
        headers.append(f'''Host: {options['host']}''')
    else:
        headers.append(f'''Host: {hostport}''')
    (scheme, url) = url.split(':', 1)
# WARNING: Decompyle incomplete


def _get_resp_headers(sock = None, success_statuses = None):
    (status, resp_headers, status_message) = read_headers(sock)
# WARNING: Decompyle incomplete

_HEADERS_TO_CHECK = {
    'upgrade': 'websocket',
    'connection': 'upgrade' }

def _validate(headers = None, key = None, subprotocols = None):
