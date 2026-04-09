# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _app.pyc (Python 3.11)

import inspect
import socket
import threading
import time
from typing import Any, Callable, Optional, Union
from  import _logging
from _abnf import ABNF
from _core import WebSocket, getdefaulttimeout
from _exceptions import WebSocketConnectionClosedException, WebSocketException, WebSocketTimeoutException
from _ssl_compat import SSLEOFError
from _url import parse_url
from _dispatcher import Dispatcher, DispatcherBase, SSLDispatcher, WrappedDispatcher
__all__ = [
    'WebSocketApp']
RECONNECT = 0

def set_reconnect(reconnectInterval = None):
    global RECONNECT
    RECONNECT = reconnectInterval


class WebSocketApp:
    '''
    Higher level of APIs are provided. The interface is like JavaScript WebSocket object.
    '''
    
    def __init__(self, url, header, on_open, on_reconnect, on_message, on_error, on_close, on_ping, on_pong, on_cont_message, keep_running, get_mask_key = None, cookie = None, subprotocols = None, on_data = (None, None, None, None, None, None, None, None, None, True, None, None, None, None, None), socket = ('url', str, 'header', Optional[Union[(list[str], dict[(str, str)], Callable[([], Union[(list[str], dict[(str, str)])])])]], 'on_open', Optional[Callable[([
        'WebSocketApp'], None)]], 'on_reconnect', Optional[Callable[([
        'WebSocketApp'], None)]], 'on_message', Optional[Callable[([
        'WebSocketApp',
        Any], None)]], 'on_error', Optional[Callable[([
        'WebSocketApp',
        Any], None)]], 'on_close', Optional[Callable[([
        'WebSocketApp',
        Any,
        Any], None)]], 'on_ping', Optional[Callable], 'on_pong', Optional[Callable], 'on_cont_message', Optional[Callable], 'keep_running', bool, 'get_mask_key', Optional[Callable], 'cookie', Optional[str], 'subprotocols', Optional[list[str]], 'on_data', Optional[Callable], 'socket', Optional[socket.socket], 'return', None)):
        """
        WebSocketApp initialization

        Parameters
        ----------
        url: str
            Websocket url.
        header: list or dict or Callable
            Custom header for websocket handshake.
            If the parameter is a callable object, it is called just before the connection attempt.
            The returned dict or list is used as custom header value.
            This could be useful in order to properly setup timestamp dependent headers.
        on_open: function
            Callback object which is called at opening websocket.
            on_open has one argument.
            The 1st argument is this class object.
        on_reconnect: function
            Callback object which is called at reconnecting websocket.
            on_reconnect has one argument.
            The 1st argument is this class object.
        on_message: function
            Callback object which is called when received data.
            on_message has 2 arguments.
            The 1st argument is this class object.
            The 2nd argument is utf-8 data received from the server.
        on_error: function
            Callback object which is called when we get error.
            on_error has 2 arguments.
            The 1st argument is this class object.
            The 2nd argument is exception object.
        on_close: function
            Callback object which is called when connection is closed.
            on_close has 3 arguments.
            The 1st argument is this class object.
            The 2nd argument is close_status_code.
            The 3rd argument is close_msg.
        on_cont_message: function
            Callback object which is called when a continuation
            frame is received.
            on_cont_message has 3 arguments.
            The 1st argument is this class object.
            The 2nd argument is utf-8 string which we get from the server.
            The 3rd argument is continue flag. if 0, the data continue
            to next frame data
        on_data: function
            Callback object which is called when a message received.
            This is called before on_message or on_cont_message,
            and then on_message or on_cont_message is called.
            on_data has 4 argument.
            The 1st argument is this class object.
            The 2nd argument is utf-8 string which we get from the server.
            The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
            The 4th argument is continue flag. If 0, the data continue
        keep_running: bool
            This parameter is obsolete and ignored.
        get_mask_key: function
            A callable function to get new mask keys, see the
            WebSocket.set_mask_key's docstring for more information.
        cookie: str
            Cookie value.
        subprotocols: list
            List of available sub protocols. Default is None.
        socket: socket
            Pre-initialized stream socket.
        """
        self.url = url
    # WARNING: Decompyle incomplete

    
    def send(self = None, data = None, opcode = None):
        '''
        send message

        Parameters
        ----------
        data: str
            Message to send. If you set opcode to OPCODE_TEXT,
            data must be utf-8 string or unicode.
        opcode: int
            Operation code of data. Default is OPCODE_TEXT.
        '''
        if self.sock or self.sock.send(data, opcode) == 0:
            raise WebSocketConnectionClosedException('Connection is already closed.')

    
    def send_text(self = None, text_data = None):
        '''
        Sends UTF-8 encoded text.
        '''
        if self.sock or self.sock.send(text_data, ABNF.OPCODE_TEXT) == 0:
            raise WebSocketConnectionClosedException('Connection is already closed.')

    
    def send_bytes(self = None, data = None):
        '''
        Sends a sequence of bytes.
        '''
        if self.sock or self.sock.send(data, ABNF.OPCODE_BINARY) == 0:
            raise WebSocketConnectionClosedException('Connection is already closed.')

    
    def close(self = None, **kwargs):
        '''
        Close websocket connection.
        '''
        self.keep_running = False
    # WARNING: Decompyle incomplete

    
    def _start_ping_thread(self = None):
        self.last_ping_tm = float(0)
        self.last_pong_tm = float(0)
        self.stop_ping = threading.Event()
        self.ping_thread = threading.Thread(target = self._send_ping)
        self.ping_thread.daemon = True
        self.ping_thread.start()

    
    def _stop_ping_thread(self = None):
        if self.stop_ping:
            self.stop_ping.set()
        if self.ping_thread and self.ping_thread.is_alive():
            self.ping_thread.join(3)
            if self.ping_thread.is_alive():
                _logging.warning('Ping thread failed to terminate within 3 seconds, forcing cleanup. Thread may be blocked.')
        self.ping_thread = None
        self.stop_ping = None
        self.last_ping_tm = float(0)
        self.last_pong_tm = float(0)

    
    def _send_ping(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def ready(self):
        if self.sock:
            pass
        return self.sock.connected

    
    def run_forever(self, sockopt, sslopt, ping_interval, ping_timeout, ping_payload, http_proxy_host, http_proxy_port, http_no_proxy, http_proxy_auth, http_proxy_timeout, skip_utf8_validation, host, origin = None, dispatcher = None, suppress_origin = None, proxy_type = (None, None, 0, None, '', None, None, None, None, None, False, None, None, None, False, None, None), reconnect = ('sockopt', tuple, 'sslopt', dict, 'ping_interval', Union[(float, int)], 'ping_timeout', Optional[Union[(float, int)]], 'ping_payload', str, 'http_proxy_host', str, 'http_proxy_port', Union[(int, str)], 'http_no_proxy', list, 'http_proxy_auth', tuple, 'http_proxy_timeout', Optional[float], 'skip_utf8_validation', bool, 'host', str, 'origin', str, 'suppress_origin', bool, 'proxy_type', str, 'reconnect', int, 'return', bool)):
        '''
        Run event loop for WebSocket framework.

        This loop is an infinite loop and is alive while websocket is available.

        Parameters
        ----------
        sockopt: tuple
            Values for socket.setsockopt.
            sockopt must be tuple
            and each element is argument of sock.setsockopt.
        sslopt: dict
            Optional dict object for ssl socket option.
        ping_interval: int or float
            Automatically send "ping" command
            every specified period (in seconds).
            If set to 0, no ping is sent periodically.
        ping_timeout: int or float
            Timeout (in seconds) if the pong message is not received.
        ping_payload: str
            Payload message to send with each ping.
        http_proxy_host: str
            HTTP proxy host name.
        http_proxy_port: int or str
            HTTP proxy port. If not set, set to 80.
        http_no_proxy: list
            Whitelisted host names that don\'t use the proxy.
        http_proxy_timeout: int or float
            HTTP proxy timeout, default is 60 sec as per python-socks.
        http_proxy_auth: tuple
            HTTP proxy auth information. tuple of username and password. Default is None.
        skip_utf8_validation: bool
            skip utf8 validation.
        host: str
            update host header.
        origin: str
            update origin header.
        dispatcher: Dispatcher object
            customize reading data from socket.
        suppress_origin: bool
            suppress outputting origin header.
        proxy_type: str
            type of proxy from: http, socks4, socks4a, socks5, socks5h
        reconnect: int
            delay interval when reconnecting

        Returns
        -------
        teardown: bool
            False if the `WebSocketApp` is closed or caught KeyboardInterrupt,
            True if any other exception was raised during a loop.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def create_dispatcher(self = None, ping_timeout = None, dispatcher = None, is_ssl = (None, False, None), handleDisconnect = ('ping_timeout', Optional[Union[(float, int)]], 'dispatcher', Optional[DispatcherBase], 'is_ssl', bool, 'handleDisconnect', Callable, 'return', Union[(Dispatcher, SSLDispatcher, WrappedDispatcher)])):
