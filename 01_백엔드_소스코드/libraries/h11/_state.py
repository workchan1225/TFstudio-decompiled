# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _state.pyc (Python 3.11)

from typing import cast, Dict, Optional, Set, Tuple, Type, Union
from _events import *
from _util import LocalProtocolError, Sentinel
__all__ = [
    'CLIENT',
    'SERVER',
    'IDLE',
    'SEND_RESPONSE',
    'SEND_BODY',
    'DONE',
    'MUST_CLOSE',
    'CLOSED',
    'MIGHT_SWITCH_PROTOCOL',
    'SWITCHED_PROTOCOL',
    'ERROR']

def CLIENT():
    '''CLIENT'''
    pass

CLIENT = <NODE:27>(CLIENT, 'CLIENT', Sentinel, metaclass = Sentinel)

def SERVER():
    '''SERVER'''
    pass

SERVER = <NODE:27>(SERVER, 'SERVER', Sentinel, metaclass = Sentinel)

def IDLE():
    '''IDLE'''
    pass

IDLE = <NODE:27>(IDLE, 'IDLE', Sentinel, metaclass = Sentinel)

def SEND_RESPONSE():
    '''SEND_RESPONSE'''
    pass

SEND_RESPONSE = <NODE:27>(SEND_RESPONSE, 'SEND_RESPONSE', Sentinel, metaclass = Sentinel)

def SEND_BODY():
    '''SEND_BODY'''
    pass

SEND_BODY = <NODE:27>(SEND_BODY, 'SEND_BODY', Sentinel, metaclass = Sentinel)

def DONE():
    '''DONE'''
    pass

DONE = <NODE:27>(DONE, 'DONE', Sentinel, metaclass = Sentinel)

def MUST_CLOSE():
    '''MUST_CLOSE'''
    pass

MUST_CLOSE = <NODE:27>(MUST_CLOSE, 'MUST_CLOSE', Sentinel, metaclass = Sentinel)

def CLOSED():
    '''CLOSED'''
    pass

CLOSED = <NODE:27>(CLOSED, 'CLOSED', Sentinel, metaclass = Sentinel)

def ERROR():
    '''ERROR'''
    pass

ERROR = <NODE:27>(ERROR, 'ERROR', Sentinel, metaclass = Sentinel)

def MIGHT_SWITCH_PROTOCOL():
    '''MIGHT_SWITCH_PROTOCOL'''
    pass

MIGHT_SWITCH_PROTOCOL = <NODE:27>(MIGHT_SWITCH_PROTOCOL, 'MIGHT_SWITCH_PROTOCOL', Sentinel, metaclass = Sentinel)

def SWITCHED_PROTOCOL():
    '''SWITCHED_PROTOCOL'''
    pass

SWITCHED_PROTOCOL = <NODE:27>(SWITCHED_PROTOCOL, 'SWITCHED_PROTOCOL', Sentinel, metaclass = Sentinel)

def _SWITCH_UPGRADE():
    '''_SWITCH_UPGRADE'''
    pass

_SWITCH_UPGRADE = <NODE:27>(_SWITCH_UPGRADE, '_SWITCH_UPGRADE', Sentinel, metaclass = Sentinel)

def _SWITCH_CONNECT():
    '''_SWITCH_CONNECT'''
    pass

_SWITCH_CONNECT = <NODE:27>(_SWITCH_CONNECT, '_SWITCH_CONNECT', Sentinel, metaclass = Sentinel)
EventTransitionType = Dict[(Type[Sentinel], Dict[(Type[Sentinel], Dict[(Union[(Type[Event], Tuple[(Type[Event], Type[Sentinel])])], Type[Sentinel])])])]
EVENT_TRIGGERED_TRANSITIONS: EventTransitionType = {
    SERVER: {
        ERROR: { },
        SWITCHED_PROTOCOL: { },
        CLOSED: {
            ConnectionClosed: CLOSED },
        MUST_CLOSE: {
            ConnectionClosed: CLOSED },
        DONE: {
            ConnectionClosed: CLOSED },
        SEND_BODY: {
            EndOfMessage: DONE,
            Data: SEND_BODY },
        SEND_RESPONSE: {
            (Response, _SWITCH_CONNECT): SWITCHED_PROTOCOL,
            (InformationalResponse, _SWITCH_UPGRADE): SWITCHED_PROTOCOL,
            Response: SEND_BODY,
            InformationalResponse: SEND_RESPONSE },
        IDLE: {
            (Request, CLIENT): SEND_RESPONSE,
            Response: SEND_BODY,
            ConnectionClosed: CLOSED } },
    CLIENT: {
        ERROR: { },
        SWITCHED_PROTOCOL: { },
        MIGHT_SWITCH_PROTOCOL: { },
        CLOSED: {
            ConnectionClosed: CLOSED },
        MUST_CLOSE: {
            ConnectionClosed: CLOSED },
        DONE: {
            ConnectionClosed: CLOSED },
        SEND_BODY: {
            EndOfMessage: DONE,
            Data: SEND_BODY },
        IDLE: {
            ConnectionClosed: CLOSED,
            Request: SEND_BODY } } }
StateTransitionType = Dict[(Tuple[(Type[Sentinel], Type[Sentinel])], Dict[(Type[Sentinel], Type[Sentinel])])]
STATE_TRIGGERED_TRANSITIONS: StateTransitionType = {
    (DONE, ERROR): {
        CLIENT: MUST_CLOSE },
    (IDLE, CLOSED): {
        CLIENT: MUST_CLOSE },
    (DONE, CLOSED): {
        CLIENT: MUST_CLOSE },
    (ERROR, DONE): {
        SERVER: MUST_CLOSE },
    (CLOSED, IDLE): {
        SERVER: MUST_CLOSE },
    (CLOSED, DONE): {
        SERVER: MUST_CLOSE },
    (MIGHT_SWITCH_PROTOCOL, SWITCHED_PROTOCOL): {
        CLIENT: SWITCHED_PROTOCOL } }

class ConnectionState:
    
    def __init__(self = None):
        self.keep_alive = True
        self.pending_switch_proposals = set()
        self.states = {
            SERVER: IDLE,
            CLIENT: IDLE }

    
    def process_error(self = None, role = None):
        self.states[role] = ERROR
        self._fire_state_triggered_transitions()

    
    def process_keep_alive_disabled(self = None):
        self.keep_alive = False
        self._fire_state_triggered_transitions()

    
    def process_client_switch_proposal(self = None, switch_event = None):
        self.pending_switch_proposals.add(switch_event)
        self._fire_state_triggered_transitions()

    
    def process_event(self = None, role = None, event_type = None, server_switch_event = (None,)):
        _event_type = event_type
    # WARNING: Decompyle incomplete

    
    def _fire_event_triggered_transitions(self = None, role = None, event_type = None):
        state = self.states[role]
        
        try:
            new_state = EVENT_TRIGGERED_TRANSITIONS[role][state][event_type]
        except KeyError:
            event_type = cast(Type[Event], event_type)
            raise LocalProtocolError("can't handle event type {} when role={} and state={}".format(event_type.__name__, role, self.states[role])), None

        self.states[role] = new_state

    
    def _fire_state_triggered_transitions(self = None):
        start_states = dict(self.states)
        if self.pending_switch_proposals and self.states[CLIENT] is DONE:
            self.states[CLIENT] = MIGHT_SWITCH_PROTOCOL
        if self.pending_switch_proposals and self.states[CLIENT] is MIGHT_SWITCH_PROTOCOL:
            self.states[CLIENT] = DONE
        if not self.keep_alive:
            for role in (CLIENT, SERVER):
                if self.states[role] is DONE:
                    self.states[role] = MUST_CLOSE
                joint_state = (self.states[CLIENT], self.states[SERVER])
                changes = STATE_TRIGGERED_TRANSITIONS.get(joint_state, { })
                self.states.update(changes)
                if self.states == start_states:
                    return None

    
    def start_next_cycle(self = None):
        if self.states != {
            SERVER: DONE,
            CLIENT: DONE }:
            raise LocalProtocolError(f'''not in a reusable state. self.states={self.states}''')
    # WARNING: Decompyle incomplete
