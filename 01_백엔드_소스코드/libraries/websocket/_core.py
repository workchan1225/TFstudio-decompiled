# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _core.pyc (Python 3.11)

import socket
import struct
import threading
import time
from typing import Optional, Union
from _abnf import ABNF, STATUS_NORMAL, continuous_frame, frame_buffer
from _exceptions import WebSocketProtocolException, WebSocketConnectionClosedException, WebSocketTimeoutException
from _handshake import SUPPORTED_REDIRECT_STATUSES, handshake
from _http import connect, proxy_info
from _logging import debug, error, trace, isEnabledForError, isEnabledForTrace
from _socket import getdefaulttimeout, recv, send, sock_opt
from _ssl_compat import ssl
from _utils import NoLock
from _dispatcher import DispatcherBase, WrappedDispatcher
__all__ = [
    'WebSocket',
    'create_connection']

class WebSocket:
    '''
    Low level WebSocket interface.

    This class is based on the WebSocket protocol `draft-hixie-thewebsocketprotocol-76 <http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-76>`_

    We can connect to the websocket server and send/receive data.
    The following example is an echo client.

    >>> import websocket
    >>> ws = websocket.WebSocket()
    >>> ws.connect("ws://echo.websocket.events")
    >>> ws.recv()
    \'echo.websocket.events sponsored by Lob.com\'
    >>> ws.send("Hello, Server")
    19
    >>> ws.recv()
    \'Hello, Server\'
    >>> ws.close()

    Parameters
    ----------
    get_mask_key: func
        A callable function to get new mask keys, see the
        WebSocket.set_mask_key\'s docstring for more information.
    sockopt: tuple
        Values for socket.setsockopt.
        sockopt must be tuple and each element is argument of sock.setsockopt.
    sslopt: dict
        Optional dict object for ssl socket options. See FAQ for details.
    fire_cont_frame: bool
        Fire recv event for each cont frame. Default is False.
    enable_multithread: bool
        If set to True, lock send method.
    skip_utf8_validation: bool
        Skip utf8 validation.
    '''
    
    def __init__(self, get_mask_key, sockopt, sslopt = None, fire_cont_frame = None, enable_multithread = None, skip_utf8_validation = (None, None, None, False, True, False, None), dispatcher = ('fire_cont_frame', bool, 'enable_multithread', bool, 'skip_utf8_validation', bool, 'dispatcher', Union[(DispatcherBase, WrappedDispatcher)]), **_):
        '''
        Initialize WebSocket object.

        Parameters
        ----------
        sslopt: dict
            Optional dict object for ssl socket options. See FAQ for details.
        '''
        self.sock_opt = sock_opt(sockopt, sslopt)
        self.handshake_response = None
        self.sock = None
        self.connected = False
        self.get_mask_key = get_mask_key
        self.frame_buffer = frame_buffer(self._recv, skip_utf8_validation)
        self.cont_frame = continuous_frame(fire_cont_frame, skip_utf8_validation)
        self.dispatcher = dispatcher
        if enable_multithread:
            self.lock = threading.Lock()
            self.readlock = threading.Lock()
            return None
        self.lock = None()
        self.readlock = NoLock()

    
    def __iter__(self):
        '''
        Allow iteration over websocket, implying sequential `recv` executions.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __next__(self):
        return self.recv()

    
    def next(self):
        return self.__next__()

    
    def fileno(self):
        return self.sock.fileno()

    
    def set_mask_key(self, func):
        '''
        Set function to create mask key. You can customize mask key generator.
        Mainly, this is for testing purpose.

        Parameters
        ----------
        func: func
            callable object. the func takes 1 argument as integer.
            The argument means length of mask key.
            This func must return string(byte array),
            which length is argument specified.
        '''
        self.get_mask_key = func

    
    def gettimeout(self = None):
        '''
        Get the websocket timeout (in seconds) as an int or float

        Returns
        ----------
        timeout: int or float
             returns timeout value (in seconds). This value could be either float/integer.
        '''
        return self.sock_opt.timeout

    
    def settimeout(self = None, timeout = None):
        '''
        Set the timeout to the websocket.

        Parameters
        ----------
        timeout: int or float
            timeout time (in seconds). This value could be either float/integer.
        '''
        self.sock_opt.timeout = timeout
        if self.sock:
            self.sock.settimeout(timeout)
            return None

    timeout = property(gettimeout, settimeout)
    
    def getsubprotocol(self):
        '''
        Get subprotocol
        '''
        if self.handshake_response:
            return self.handshake_response.subprotocol

    subprotocol = property(getsubprotocol)
    
    def getstatus(self):
        '''
        Get handshake status
        '''
        if self.handshake_response:
            return self.handshake_response.status

    status = property(getstatus)
    
    def getheaders(self):
        '''
        Get handshake response header
        '''
        if self.handshake_response:
            return self.handshake_response.headers

    
    def is_ssl(self):
        
        try:
            return isinstance(self.sock, ssl.SSLSocket)
        except (AttributeError, NameError):
            return False


    headers = property(getheaders)
    
    def connect(self, url, **options):
        '''
        Connect to url. url is websocket url scheme.
        ie. ws://host:port/resource
        You can customize using \'options\'.
        If you set "header" list object, you can set your own custom header.

        >>> ws = WebSocket()
        >>> ws.connect("ws://echo.websocket.events",
                ...     header=["User-Agent: MyProgram",
                ...             "x-custom: header"])

        Parameters
        ----------
        header: list or dict
            Custom http header list or dict.
        cookie: str
            Cookie value.
        origin: str
            Custom origin url.
        connection: str
            Custom connection header value.
            Default value "Upgrade" set in _handshake.py
        suppress_origin: bool
            Suppress outputting origin header.
        host: str
            Custom host header string.
        timeout: int or float
            Socket timeout time. This value is an integer or float.
            If you set None for this value, it means "use default_timeout value"
        http_proxy_host: str
            HTTP proxy host name.
        http_proxy_port: str or int
            HTTP proxy port. Default is 80.
        http_no_proxy: list
            Whitelisted host names that don\'t use the proxy.
        http_proxy_auth: tuple
            HTTP proxy auth information. Tuple of username and password. Default is None.
        http_proxy_timeout: int or float
            HTTP proxy timeout, default is 60 sec as per python-socks.
        redirect_limit: int
            Number of redirects to follow.
        subprotocols: list
            List of available subprotocols. Default is None.
        socket: socket
            Pre-initialized stream socket.
        '''
        self.sock_opt.timeout = options.get('timeout', self.sock_opt.timeout)
    # WARNING: Decompyle incomplete

    
    def send(self = None, payload = None, opcode = None):
        '''
        Send the data as string.

        Parameters
        ----------
        payload: str
            Payload must be utf-8 string or unicode,
            If the opcode is OPCODE_TEXT.
            Otherwise, it must be string(byte array).
        opcode: int
            Operation code (opcode) to send.
        '''
        frame = ABNF.create_frame(payload, opcode)
        return self.send_frame(frame)

    
    def send_text(self = None, text_data = None):
        '''
        Sends UTF-8 encoded text.
        '''
        return self.send(text_data, ABNF.OPCODE_TEXT)

    
    def send_bytes(self = None, data = None):
        '''
        Sends a sequence of bytes.
        '''
        return self.send(data, ABNF.OPCODE_BINARY)

    
    def send_frame(self = None, frame = None):
        '''
        Send the data frame.

        >>> ws = create_connection("ws://echo.websocket.events")
        >>> frame = ABNF.create_frame("Hello", ABNF.OPCODE_TEXT)
        >>> ws.send_frame(frame)
        >>> cont_frame = ABNF.create_frame("My name is ", ABNF.OPCODE_CONT, 0)
        >>> ws.send_frame(frame)
        >>> cont_frame = ABNF.create_frame("Foo Bar", ABNF.OPCODE_CONT, 1)
        >>> ws.send_frame(frame)

        Parameters
        ----------
        frame: ABNF frame
            frame data created by ABNF.create_frame
        '''
        if self.get_mask_key:
            frame.get_mask_key = self.get_mask_key
        data = frame.format()
        length = len(data)
        if isEnabledForTrace():
            trace(f'''++Sent raw: {repr(data)}''')
            trace(f'''++Sent decoded: {frame.__str__()}''')
        self.lock
    # WARNING: Decompyle incomplete

    
    def send_binary(self = None, payload = None):
        '''
        Send a binary message (OPCODE_BINARY).

        Parameters
        ----------
        payload: bytes
            payload of message to send.
        '''
        return self.send(payload, ABNF.OPCODE_BINARY)

    
    def ping(self = None, payload = None):
        '''
        Send ping data.

        Parameters
        ----------
        payload: str
            data payload to send server.
        '''
        if isinstance(payload, str):
            payload = payload.encode('utf-8')
        self.send(payload, ABNF.OPCODE_PING)

    
    def pong(self = None, payload = None):
        '''
        Send pong data.

        Parameters
        ----------
        payload: str
            data payload to send server.
        '''
        if isinstance(payload, str):
            payload = payload.encode('utf-8')
        self.send(payload, ABNF.OPCODE_PONG)

    
    def recv(self = None):
