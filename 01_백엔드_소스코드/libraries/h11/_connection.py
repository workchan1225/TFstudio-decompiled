# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _connection.pyc (Python 3.11)

from typing import Any, Callable, cast, Dict, List, Optional, overload, Tuple, Type, Union
from _events import ConnectionClosed, Data, EndOfMessage, Event, InformationalResponse, Request, Response
from _headers import get_comma_header, has_expect_100_continue, set_comma_header
from _readers import READERS, ReadersType
from _receivebuffer import ReceiveBuffer
from _state import _SWITCH_CONNECT, _SWITCH_UPGRADE, CLIENT, ConnectionState, DONE, ERROR, MIGHT_SWITCH_PROTOCOL, SEND_BODY, SERVER, SWITCHED_PROTOCOL
from _util import LocalProtocolError, RemoteProtocolError, Sentinel
from _writers import WRITERS, WritersType
__all__ = [
    'Connection',
    'NEED_DATA',
    'PAUSED']

def NEED_DATA():
    '''NEED_DATA'''
    pass

NEED_DATA = <NODE:27>(NEED_DATA, 'NEED_DATA', Sentinel, metaclass = Sentinel)

def PAUSED():
    '''PAUSED'''
    pass

PAUSED = <NODE:27>(PAUSED, 'PAUSED', Sentinel, metaclass = Sentinel)
DEFAULT_MAX_INCOMPLETE_EVENT_SIZE = 16384

def _keep_alive(event = None):
    connection = get_comma_header(event.headers, b'connection')
    if b'close' in connection:
        return False
    if None(event, 'http_version', b'1.1') < b'1.1':
        return False


def _body_framing(request_method = None, event = None):
    pass
# WARNING: Decompyle incomplete


class Connection:
    """An object encapsulating the state of an HTTP connection.

    Args:
        our_role: If you're implementing a client, pass :data:`h11.CLIENT`. If
            you're implementing a server, pass :data:`h11.SERVER`.

        max_incomplete_event_size (int):
            The maximum number of bytes we're willing to buffer of an
            incomplete event. In practice this mostly sets a limit on the
            maximum size of the request/response line + headers. If this is
            exceeded, then :meth:`next_event` will raise
            :exc:`RemoteProtocolError`.

    """
    
    def __init__(self = None, our_role = None, max_incomplete_event_size = None):
        self._max_incomplete_event_size = max_incomplete_event_size
        if our_role not in (CLIENT, SERVER):
            raise ValueError(f'''expected CLIENT or SERVER, not {our_role!r}''')
        self.our_role = our_role
        self
        if our_role is CLIENT:
            self.their_role = SERVER
        else:
            self.their_role = CLIENT
        self._cstate = ConnectionState()
        self._writer = self._get_io_object(self.our_role, None, WRITERS)
        self._reader = self._get_io_object(self.their_role, None, READERS)
        self._receive_buffer = ReceiveBuffer()
        self._receive_buffer_closed = False
        self.their_http_version = None
        self._request_method = None
        self.client_is_waiting_for_100_continue = False

    states = (lambda self = None: dict(self._cstate.states))()
    our_state = (lambda self = None: self._cstate.states[self.our_role])()
    their_state = (lambda self = None: self._cstate.states[self.their_role])()
    they_are_waiting_for_100_continue = (lambda self = None:
