# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: frame_protocol.pyc (Python 3.11)

'''
wsproto/frame_protocol
~~~~~~~~~~~~~~~~~~~~~~

WebSocket frame protocol implementation.
'''
from __future__ import annotations
import contextlib
import os
import struct
from codecs import IncrementalDecoder, getincrementaldecoder
from enum import IntEnum
from typing import TYPE_CHECKING, NamedTuple
if TYPE_CHECKING:
    from collections.abc import Generator
    from extensions import Extension
_XOR_TABLE = range(256)()

class XorMaskerSimple:
    
    def __init__(self = None, masking_key = None):
        self._masking_key = masking_key

    
    def process(self = None, data = None):
        data = bytearray(data)
        if data:
            data_array = data
            (a, b, c, d) = self._masking_key()
            data_array[::4] = data_array[::4].translate(a)
            data_array[1::4] = data_array[1::4].translate(b)
            data_array[2::4] = data_array[2::4].translate(c)
            data_array[3::4] = data_array[3::4].translate(d)
            key_rotation = len(data) % 4
            self._masking_key = self._masking_key[key_rotation:] + self._masking_key[:key_rotation]
            return data_array



class XorMaskerNull:
    
    def process(self = None, data = None):
        return data


PAYLOAD_LENGTH_TWO_BYTE = 126
PAYLOAD_LENGTH_EIGHT_BYTE = 127
MAX_PAYLOAD_NORMAL = 125
MAX_PAYLOAD_TWO_BYTE = 65535
MAX_PAYLOAD_EIGHT_BYTE = 0xFFFFFFFFFFFFFFFF
MAX_FRAME_PAYLOAD = MAX_PAYLOAD_EIGHT_BYTE
MASK_MASK = 128
PAYLOAD_LEN_MASK = 127
FIN_MASK = 128
RSV1_MASK = 64
RSV2_MASK = 32
RSV3_MASK = 16
OPCODE_MASK = 15

class Opcode(IntEnum):
    '''
    RFC 6455, Section 5.2 - Base Framing Protocol
    '''
    CONTINUATION = 0
    TEXT = 1
    BINARY = 2
    CLOSE = 8
    PING = 9
    PONG = 10
    
    def iscontrol(self = None):
        return bool(self & 8)



class CloseReason(IntEnum):
    '''
    RFC 6455, Section 7.4.1 - Defined Status Codes
    '''
    NORMAL_CLOSURE = 1000
    GOING_AWAY = 1001
    PROTOCOL_ERROR = 1002
    UNSUPPORTED_DATA = 1003
    NO_STATUS_RCVD = 1005
    ABNORMAL_CLOSURE = 1006
    INVALID_FRAME_PAYLOAD_DATA = 1007
    POLICY_VIOLATION = 1008
    MESSAGE_TOO_BIG = 1009
    MANDATORY_EXT = 1010
    INTERNAL_ERROR = 1011
    SERVICE_RESTART = 1012
    TRY_AGAIN_LATER = 1013
    TLS_HANDSHAKE_FAILED = 1015

LOCAL_ONLY_CLOSE_REASONS = (CloseReason.NO_STATUS_RCVD, CloseReason.ABNORMAL_CLOSURE, CloseReason.TLS_HANDSHAKE_FAILED)
MIN_CLOSE_REASON = 1000
MIN_PROTOCOL_CLOSE_REASON = 1000
MAX_PROTOCOL_CLOSE_REASON = 2999
MIN_LIBRARY_CLOSE_REASON = 3000
MAX_LIBRARY_CLOSE_REASON = 3999
MIN_PRIVATE_CLOSE_REASON = 4000
MAX_PRIVATE_CLOSE_REASON = 4999
MAX_CLOSE_REASON = 4999
NULL_MASK = struct.pack('!I', 0)

class ParseFailed(Exception):
    pass
# WARNING: Decompyle incomplete


class RsvBits(NamedTuple):
    rsv3: 'bool' = 'RsvBits'


class Header(NamedTuple):
    masking_key: 'bytes | None' = 'Header'


class Frame(NamedTuple):
    message_finished: 'bool' = 'Frame'


def _truncate_utf8(data = None, nbytes = None):
    if len(data) <= nbytes:
        return data
    data = None[:nbytes]
    return data.decode('utf-8', errors = 'ignore').encode('utf-8')


class Buffer:
    
    def __init__(self = None, initial_bytes = None):
        self.buffer = bytearray()
        self.bytes_used = 0
        if initial_bytes:
            self.feed(initial_bytes)
            return None

    
    def feed(self = None, new_bytes = None):
        pass

    
    def consume_at_most(self = None, nbytes = None):
        if not nbytes:
            return bytearray()
        data = None.buffer[self.bytes_used:self.bytes_used + nbytes]
        return data

    
    def consume_exactly(self = None, nbytes = None):
        if len(self.buffer) - self.bytes_used < nbytes:
            return None
        return None.consume_at_most(nbytes)

    
    def commit(self = None):
        del self.buffer[:self.bytes_used]
        self.bytes_used = 0

    
    def rollback(self = None):
        self.bytes_used = 0

    
    def __len__(self = None):
        return len(self.buffer)



class MessageDecoder:
    
    def __init__(self = None):
        self.opcode = None
        self.decoder = None

    
    def process_frame(self = None, frame = None):
        pass
    # WARNING: Decompyle incomplete



class FrameDecoder:
    
    def __init__(self = None, client = None, extensions = None):
