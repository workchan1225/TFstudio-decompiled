# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cdp.pyc (Python 3.11)

import contextvars
import importlib
import itertools
import json
import logging
import pathlib
from collections import defaultdict
from collections.abc import AsyncGenerator, AsyncIterator, Generator
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass
from typing import Any, TypeVar
import trio
from trio_websocket import ConnectionClosed as WsConnectionClosed
from trio_websocket import connect_websocket_url
logger = logging.getLogger('trio_cdp')
T = TypeVar('T')
MAX_WS_MESSAGE_SIZE = 16777216
devtools = None
version = None

def import_devtools(ver):
    '''Attempt to load the current latest available devtools into the module cache for use later.'''
    global version, devtools, devtools
    version = ver
    base = 'selenium.webdriver.common.devtools.v'
    
    try:
        devtools = importlib.import_module(f'''{base}{ver}''')
        return devtools
    except ModuleNotFoundError:
        devtools_path = pathlib.Path(__file__).parents[1].joinpath('devtools')
        versions = (lambda .0: pass# WARNING: Decompyle incomplete
)(devtools_path.iterdir()())
        latest = (lambda .0: pass# WARNING: Decompyle incomplete
)(versions())
        selenium_logger = logging.getLogger(__name__)
        selenium_logger.debug('Falling back to loading `devtools`: v%s', latest)
        devtools = importlib.import_module(f'''{base}{latest}''')
        return 


_connection_context: contextvars.ContextVar = contextvars.ContextVar('connection_context')
_session_context: contextvars.ContextVar = contextvars.ContextVar('session_context')

def get_connection_context(fn_name):
    '''Look up the current connection.

    If there is no current connection, raise a ``RuntimeError`` with a
    helpful message.
    '''
    
    try:
        return _connection_context.get()
    except LookupError:
        raise RuntimeError(f'''{fn_name}() must be called in a connection context.''')



def get_session_context(fn_name):
    '''Look up the current session.

    If there is no current session, raise a ``RuntimeError`` with a
    helpful message.
    '''
    
    try:
        return _session_context.get()
    except LookupError:
        raise RuntimeError(f'''{fn_name}() must be called in a session context.''')


connection_context = (lambda connection: pass# WARNING: Decompyle incomplete
)()
session_context = (lambda session: pass# WARNING: Decompyle incomplete
)()

def set_global_connection(connection):
    '''Install ``connection`` in the root context so that it will become the default connection for all tasks.

    This is generally not recommended, except it may be necessary in
    certain use cases such as running inside Jupyter notebook.
    '''
    global _connection_context
    _connection_context = contextvars.ContextVar('_connection_context', default = connection)


def set_global_session(session):
    '''Install ``session`` in the root context so that it will become the default session for all tasks.

    This is generally not recommended, except it may be necessary in
    certain use cases such as running inside Jupyter notebook.
    '''
    global _session_context
    _session_context = contextvars.ContextVar('_session_context', default = session)


class BrowserError(Exception):
    """This exception is raised when the browser's response to a command indicates that an error occurred."""
    
    def __init__(self, obj):
        self.code = obj.get('code')
        self.message = obj.get('message')
        self.detail = obj.get('data')

    
    def __str__(self):
        return f'''BrowserError<code={self.code} message={self.message}> {self.detail}'''



class CdpConnectionClosed(WsConnectionClosed):
    '''Raised when a public method is called on a closed CDP connection.'''
    
    def __init__(self, reason):
        '''Constructor.

        Args:
            reason: wsproto.frame_protocol.CloseReason
        '''
        self.reason = reason

    
    def __repr__(self):
        '''Return representation.'''
        return f'''{self.__class__.__name__}<{self.reason}>'''



class InternalError(Exception):
    '''This exception is only raised when there is faulty logic in TrioCDP or the integration with PyCDP.'''
    pass

CmEventProxy = <NODE:12>()

class CdpBase:
    
    def __init__(self, ws, session_id, target_id):
        self.ws = ws
        self.session_id = session_id
        self.target_id = target_id
        self.channels = defaultdict(set)
        self.id_iter = itertools.count()
        self.inflight_cmd = { }
        self.inflight_result = { }

    
    async def execute(self = None, cmd = None):
        '''Execute a command on the server and wait for the result.

        Args:
            cmd: any CDP command

        Returns:
            a CDP result
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def listen(self = None, *, buffer_size, *event_types):
        '''Listen for events.

        Returns:
            An async iterator that iterates over events matching the indicated types.
        '''
        (sender, receiver) = trio.open_memory_channel(buffer_size)
        for event_type in event_types:
            self.channels[event_type].add(sender)
            return receiver

    wait_for = (lambda self = None, event_type = None, buffer_size = asynccontextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def _handle_data(self, data):
        '''Handle incoming WebSocket data.

        Args:
            data: a JSON dictionary
        '''
        if 'id' in data:
            self._handle_cmd_response(data)
            return None
        None._handle_event(data)

    
    def _handle_cmd_response(self = None, data = None):
        '''Handle a response to a command.

        This will set an event flag that will return control to the
        task that called the command.

        Args:
            data: response as a JSON dictionary
        '''
        cmd_id = data['id']
        
        try:
            (cmd, event) = self.inflight_cmd.pop(cmd_id)
        except KeyError:
            logger.warning('Got a message with a command ID that does not exist: %s', data)
            return None

        if 'error' in data:
            self.inflight_result[cmd_id] = BrowserError(data['error'])
        else:
            
            try:
                _ = cmd.send(data['result'])
                raise InternalError("The command's generator function did not exit when expected!")
            except StopIteration:
                exit = None
                return_ = exit.value
                exit = None
                del exit
            except:
                exit = None
                del exit

            self.inflight_result[cmd_id] = return_
        event.set()

    
    def _handle_event(self = None, data = None):
        '''Handle an event.

        Args:
            data: event as a JSON dictionary
        '''
        pass
    # WARNING: Decompyle incomplete



class CdpSession(CdpBase):
    pass
# WARNING: Decompyle incomplete


class CdpConnection(trio.abc.AsyncResource, CdpBase):
    pass
# WARNING: Decompyle incomplete

open_cdp = (lambda url = None: pass# WARNING: Decompyle incomplete
)()

async def connect_cdp(nursery = None, url = None):
    '''Connect to the browser specified by ``url`` and spawn a background task in the specified nursery.

    The ``open_cdp()`` context manager is preferred in most situations.
    You should only use this function if you need to specify a custom
    nursery. This connection is not automatically closed! You can either
    use the connection object as a context manager (``async with
    conn:``) or else call ``await conn.aclose()`` on it when you are
    done with it. If ``set_context`` is True, then the returned
    connection will be installed as the default connection for the
    current task. This argument is for unusual use cases, such as
    running inside of a notebook.
    '''
    pass
# WARNING: Decompyle incomplete
