# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: frames.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import enum
import io
import os
import secrets
import struct
from collections.abc import Generator, Sequence
from typing import Callable, Union
from exceptions import PayloadTooBig, ProtocolError

try:
    from speedups import apply_mask
except ImportError:
    from utils import apply_mask

__all__ = [
    'Opcode',
    'OP_CONT',
    'OP_TEXT',
    'OP_BINARY',
    'OP_CLOSE',
    'OP_PING',
    'OP_PONG',
    'DATA_OPCODES',
    'CTRL_OPCODES',
    'CloseCode',
    'Frame',
    'Close']

class Opcode(enum.IntEnum):
    '''Opcode values for WebSocket frames.'''
    (CONT, TEXT, BINARY) = (0, 1, 2)
    (CLOSE, PING, PONG) = (8, 9, 10)

OP_CONT = Opcode.CONT
OP_TEXT = Opcode.TEXT
OP_BINARY = Opcode.BINARY
OP_CLOSE = Opcode.CLOSE
OP_PING = Opcode.PING
OP_PONG = Opcode.PONG
DATA_OPCODES = (OP_CONT, OP_TEXT, OP_BINARY)
CTRL_OPCODES = (OP_CLOSE, OP_PING, OP_PONG)

class CloseCode(enum.IntEnum):
    '''Close code values for WebSocket close frames.'''
    NORMAL_CLOSURE = 1000
    GOING_AWAY = 1001
    PROTOCOL_ERROR = 1002
    UNSUPPORTED_DATA = 1003
    NO_STATUS_RCVD = 1005
    ABNORMAL_CLOSURE = 1006
    INVALID_DATA = 1007
    POLICY_VIOLATION = 1008
    MESSAGE_TOO_BIG = 1009
    MANDATORY_EXTENSION = 1010
    INTERNAL_ERROR = 1011
    SERVICE_RESTART = 1012
    TRY_AGAIN_LATER = 1013
    BAD_GATEWAY = 1014
    TLS_HANDSHAKE = 1015

CLOSE_CODE_EXPLANATIONS: 'dict[int, str]' = {
    CloseCode.TLS_HANDSHAKE: 'TLS handshake failure [internal]',
    CloseCode.BAD_GATEWAY: 'bad gateway',
    CloseCode.TRY_AGAIN_LATER: 'try again later',
    CloseCode.SERVICE_RESTART: 'service restart',
    CloseCode.INTERNAL_ERROR: 'internal error',
    CloseCode.MANDATORY_EXTENSION: 'mandatory extension',
    CloseCode.MESSAGE_TOO_BIG: 'message too big',
    CloseCode.POLICY_VIOLATION: 'policy violation',
    CloseCode.INVALID_DATA: 'invalid frame payload data',
    CloseCode.ABNORMAL_CLOSURE: 'abnormal closure [internal]',
    CloseCode.NO_STATUS_RCVD: 'no status received [internal]',
    CloseCode.UNSUPPORTED_DATA: 'unsupported data',
    CloseCode.PROTOCOL_ERROR: 'protocol error',
    CloseCode.GOING_AWAY: 'going away',
    CloseCode.NORMAL_CLOSURE: 'OK' }
EXTERNAL_CLOSE_CODES = {
    CloseCode.NORMAL_CLOSURE,
    CloseCode.GOING_AWAY,
    CloseCode.PROTOCOL_ERROR,
    CloseCode.UNSUPPORTED_DATA,
    CloseCode.INVALID_DATA,
    CloseCode.POLICY_VIOLATION,
    CloseCode.MESSAGE_TOO_BIG,
    CloseCode.MANDATORY_EXTENSION,
    CloseCode.INTERNAL_ERROR,
    CloseCode.SERVICE_RESTART,
    CloseCode.TRY_AGAIN_LATER,
    CloseCode.BAD_GATEWAY}
OK_CLOSE_CODES = {
    CloseCode.NORMAL_CLOSURE,
    CloseCode.GOING_AWAY,
    CloseCode.NO_STATUS_RCVD}
BytesLike = (bytes, bytearray, memoryview)
Frame = <NODE:12>()
Close = <NODE:12>()
from  import extensions
