# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dispatcher.pyc (Python 3.11)

import time
import socket
import inspect
import selectors
from typing import TYPE_CHECKING, Callable, Optional, Union
if TYPE_CHECKING:
    from _app import WebSocketApp
from  import _logging
from _socket import send

class DispatcherBase:
    '''
    DispatcherBase
    '''
    
    def __init__(self = None, app = None, ping_timeout = None):
        self.app = app
        self.ping_timeout = ping_timeout

    
    def timeout(self = None, seconds = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def reconnect(self = None, seconds = None, reconnector = None):
        
        try:
            _logging.info(f'''reconnect() - retrying in {seconds} seconds [{len(inspect.stack())} frames in stack]''')
            time.sleep(seconds)
            reconnector(reconnecting = True)
            return None
        except KeyboardInterrupt:
            e = None
            _logging.info(f'''User exited {e}''')
            raise e
            e = None
            del e


    
    def send(self = None, sock = None, data = None):
        return send(sock, data)



class Dispatcher(DispatcherBase):
    '''
    Dispatcher
    '''
    
    def read(self = None, sock = None, read_callback = None, check_callback = ('sock', socket.socket, 'read_callback', Callable, 'check_callback', Callable, 'return', None)):
        pass
    # WARNING: Decompyle incomplete



class SSLDispatcher(DispatcherBase):
    '''
    SSLDispatcher
    '''
    
    def read(self = None, sock = None, read_callback = None, check_callback = ('sock', socket.socket, 'read_callback', Callable, 'check_callback', Callable, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    def select(self = None, sock = None, sel = None):
        pass
    # WARNING: Decompyle incomplete



class WrappedDispatcher:
    '''
    WrappedDispatcher
    '''
    
    def __init__(self, app = None, ping_timeout = None, dispatcher = None, handleDisconnect = ('app', 'WebSocketApp', 'ping_timeout', Optional[Union[(float, int)]], 'return', None)):
        self.app = app
        self.ping_timeout = ping_timeout
        self.dispatcher = dispatcher
        self.handleDisconnect = handleDisconnect
        dispatcher.signal(2, dispatcher.abort)

    
    def read(self = None, sock = None, read_callback = None, check_callback = ('sock', socket.socket, 'read_callback', Callable, 'check_callback', Callable, 'return', None)):
        self.dispatcher.read(sock, read_callback)
        if self.ping_timeout:
            self.timeout(self.ping_timeout, check_callback)
            return None

    
    def send(self = None, sock = None, data = None):
        self.dispatcher.buffwrite(sock, data, send, self.handleDisconnect)
        return len(data)

    
    def timeout(self = None, seconds = None, callback = None, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def reconnect(self = None, seconds = None, reconnector = None):
        self.timeout(seconds, reconnector, True)
