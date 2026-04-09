# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _abnf.pyc (Python 3.11)

import array
import os
import struct
import sys
from threading import Lock
from typing import Callable, Optional, Union, Any
from _exceptions import WebSocketPayloadException, WebSocketProtocolException
from _utils import validate_utf8

try:
    from wsaccel.xormask import XorMaskerSimple
    
    def _mask(mask_value = None, data_value = None):
        mask_result = XorMaskerSimple(mask_value).process(data_value)
        return mask_result

except ImportError:
    native_byteorder = sys.byteorder
    
    def _mask(mask_value = None, data_value = None):
        datalen = len(data_value)
        int_data_value = int.from_bytes(data_value, native_byteorder)
        int_mask_value = int.from_bytes(mask_value * (datalen // 4) + mask_value[:datalen % 4], native_byteorder)
        return (int_data_value ^ int_mask_value).to_bytes(datalen, native_byteorder)


__all__ = [
    'ABNF',
    'continuous_frame',
    'frame_buffer',
    'STATUS_NORMAL',
    'STATUS_GOING_AWAY',
    'STATUS_PROTOCOL_ERROR',
    'STATUS_UNSUPPORTED_DATA_TYPE',
    'STATUS_STATUS_NOT_AVAILABLE',
    'STATUS_ABNORMAL_CLOSED',
    'STATUS_INVALID_PAYLOAD',
    'STATUS_POLICY_VIOLATION',
    'STATUS_MESSAGE_TOO_BIG',
    'STATUS_INVALID_EXTENSION',
    'STATUS_UNEXPECTED_CONDITION',
    'STATUS_BAD_GATEWAY',
    'STATUS_TLS_HANDSHAKE_ERROR']
STATUS_NORMAL = 1000
STATUS_GOING_AWAY = 1001
STATUS_PROTOCOL_ERROR = 1002
STATUS_UNSUPPORTED_DATA_TYPE = 1003
STATUS_STATUS_NOT_AVAILABLE = 1005
STATUS_ABNORMAL_CLOSED = 1006
STATUS_INVALID_PAYLOAD = 1007
STATUS_POLICY_VIOLATION = 1008
STATUS_MESSAGE_TOO_BIG = 1009
STATUS_INVALID_EXTENSION = 1010
STATUS_UNEXPECTED_CONDITION = 1011
STATUS_SERVICE_RESTART = 1012
STATUS_TRY_AGAIN_LATER = 1013
STATUS_BAD_GATEWAY = 1014
STATUS_TLS_HANDSHAKE_ERROR = 1015
VALID_CLOSE_STATUS = (STATUS_NORMAL, STATUS_GOING_AWAY, STATUS_PROTOCOL_ERROR, STATUS_UNSUPPORTED_DATA_TYPE, STATUS_INVALID_PAYLOAD, STATUS_POLICY_VIOLATION, STATUS_MESSAGE_TOO_BIG, STATUS_INVALID_EXTENSION, STATUS_UNEXPECTED_CONDITION, STATUS_SERVICE_RESTART, STATUS_TRY_AGAIN_LATER, STATUS_BAD_GATEWAY)

class ABNF:
    '''
    ABNF frame class.
    See http://tools.ietf.org/html/rfc5234
    and http://tools.ietf.org/html/rfc6455#section-5.2
    '''
    OPCODE_CONT = 0
    OPCODE_TEXT = 1
    OPCODE_BINARY = 2
    OPCODE_CLOSE = 8
    OPCODE_PING = 9
    OPCODE_PONG = 10
    OPCODES = (OPCODE_CONT, OPCODE_TEXT, OPCODE_BINARY, OPCODE_CLOSE, OPCODE_PING, OPCODE_PONG)
    OPCODE_MAP = {
        OPCODE_PONG: 'pong',
        OPCODE_PING: 'ping',
        OPCODE_CLOSE: 'close',
        OPCODE_BINARY: 'binary',
        OPCODE_TEXT: 'text',
        OPCODE_CONT: 'cont' }
    LENGTH_7 = 126
    LENGTH_16 = 65536
    LENGTH_63 = 0x8000000000000000
    
    def __init__(self, fin, rsv1, rsv2 = None, rsv3 = None, opcode = None, mask_value = (0, 0, 0, 0, OPCODE_TEXT, 1, ''), data = ('fin', int, 'rsv1', int, 'rsv2', int, 'rsv3', int, 'opcode', int, 'mask_value', int, 'data', Optional[Union[(str, bytes)]], 'return', None)):
        '''
        Constructor for ABNF. Please check RFC for arguments.
        '''
        self.fin = fin
        self.rsv1 = rsv1
        self.rsv2 = rsv2
        self.rsv3 = rsv3
        self.opcode = opcode
        self.mask_value = mask_value
    # WARNING: Decompyle incomplete

    
    def validate(self = None, skip_utf8_validation = None):
        '''
        Validate the ABNF frame.

        Parameters
        ----------
        skip_utf8_validation: skip utf8 validation.
        '''
        if self.rsv1 and self.rsv2 or self.rsv3:
            raise WebSocketProtocolException('rsv is not implemented, yet')
        if self.opcode not in ABNF.OPCODES:
            raise WebSocketProtocolException('Invalid opcode %r', self.opcode)
        if not self.opcode == ABNF.OPCODE_PING and self.fin:
            raise WebSocketProtocolException('Invalid ping frame.')
        if self.opcode == ABNF.OPCODE_CLOSE:
            data_length = len(self.data)
            if not data_length:
                return None
            if None == 1 or data_length >= 126:
                raise WebSocketProtocolException('Invalid close frame.')
            if not data_length > 2 and skip_utf8_validation and validate_utf8(self.data[2:]):
                raise WebSocketProtocolException('Invalid close frame.')
            data_bytes = self.data[:2] if isinstance(self.data, bytes) else self.data[:2].encode('utf-8')
            code = struct.unpack('!H', data_bytes)[0]
            if not self._is_valid_close_status(code):
                raise WebSocketProtocolException('Invalid close opcode %r', code)
        return None

    _is_valid_close_status = (lambda code = None: if not code in VALID_CLOSE_STATUS:
passNone if  <= 3000, code else None, 3000, code < 5000)()
    
    def __str__(self = None):
        data_repr = self.data if isinstance(self.data, str) else repr(self.data)
        return f'''fin={self.fin} opcode={self.opcode} data={data_repr}'''

    create_frame = (lambda data = None, opcode = None, fin = staticmethod: if opcode == ABNF.OPCODE_TEXT and isinstance(data, str):
data = data.encode('utf-8')ABNF(fin, 0, 0, 0, opcode, 1, data))()
    
    def format(self = None):
        '''
        Format this object to string(byte array) to send data to server.
        '''
        if (lambda .0: pass# WARNING: Decompyle incomplete
)((self.fin, self.rsv1, self.rsv2, self.rsv3)()):
            raise ValueError('not 0 or 1')
        if self.opcode not in ABNF.OPCODES:
            raise ValueError('Invalid OPCODE')
        length = len(self.data)
        if length >= ABNF.LENGTH_63:
            raise ValueError('data is too long')
        frame_header = chr(self.fin << 7 | self.rsv1 << 6 | self.rsv2 << 5 | self.rsv3 << 4 | self.opcode).encode('latin-1')
        if length < ABNF.LENGTH_7:
            frame_header += chr(self.mask_value << 7 | length).encode('latin-1')
        elif length < ABNF.LENGTH_16:
            frame_header += chr(self.mask_value << 7 | 126).encode('latin-1')
            frame_header += struct.pack('!H', length)
        else:
            frame_header += chr(self.mask_value << 7 | 127).encode('latin-1')
            frame_header += struct.pack('!Q', length)
        if not self.mask_value:
            if isinstance(self.data, str):
                self.data = self.data.encode('utf-8')
            return frame_header + self.data
        mask_key = any.get_mask_key(4)
        return frame_header + self._get_masked(mask_key)

    
    def _get_masked(self = None, mask_key = None):
        s = ABNF.mask(mask_key, self.data)
        if isinstance(mask_key, str):
            mask_key = mask_key.encode('utf-8')
        return mask_key + s

    mask = (lambda mask_key = None, data = None: pass# WARNING: Decompyle incomplete
)()


class frame_buffer:
    _HEADER_MASK_INDEX = 5
    _HEADER_LENGTH_INDEX = 6
    
    def __init__(self = None, recv_fn = None, skip_utf8_validation = None):
        self.recv = recv_fn
        self.skip_utf8_validation = skip_utf8_validation
        self.recv_buffer = []
        self.clear()
        self.lock = Lock()

    
    def clear(self = None):
        self.header = None
        self.length = None
        self.mask_value = None

    
    def needs_header(self = None):
        return self.header is None

    
    def recv_header(self = None):
        header = self.recv_strict(2)
        b1 = header[0]
        fin = b1 >> 7 & 1
        rsv1 = b1 >> 6 & 1
        rsv2 = b1 >> 5 & 1
        rsv3 = b1 >> 4 & 1
        opcode = b1 & 15
        b2 = header[1]
        has_mask = b2 >> 7 & 1
        length_bits = b2 & 127
        self.header = (fin, rsv1, rsv2, rsv3, opcode, has_mask, length_bits)

    
    def has_mask(self = None):
        if not self.header:
            return False
        header_val = None.header[frame_buffer._HEADER_MASK_INDEX]
        return header_val

    
    def needs_length(self = None):
        return self.length is None

    
    def recv_length(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def needs_mask(self = None):
        return self.mask_value is None

    
    def recv_mask(self = None):
        self.mask_value = self.recv_strict(4) if self.has_mask() else ''

    
    def recv_frame(self = None):
        self.lock
        if self.needs_header():
            self.recv_header()
    # WARNING: Decompyle incomplete

    
    def recv_strict(self = None, bufsize = None):
        if not isinstance(bufsize, int):
            raise ValueError('bufsize must be an integer')
        shortage = sum - (lambda .0: pass# WARNING: Decompyle incomplete
)(self.recv_buffer())
        if shortage > 0:
            bytes_ = self.recv(min(16384, shortage))
            if isinstance(bytes_, bytes):
                self.recv_buffer.append(bytes_)
                shortage -= len(bytes_)
            
    # WARNING: Decompyle incomplete



class continuous_frame:
    
    def __init__(self = None, fire_cont_frame = None, skip_utf8_validation = None):
        self.fire_cont_frame = fire_cont_frame
        self.skip_utf8_validation = skip_utf8_validation
        self.cont_data = None
        self.recving_frames = None

    
    def validate(self = None, frame = None):
        if self.recving_frames and frame.opcode == ABNF.OPCODE_CONT:
            raise WebSocketProtocolException('Illegal frame')
        if self.recving_frames or frame.opcode in (ABNF.OPCODE_TEXT, ABNF.OPCODE_BINARY):
            raise WebSocketProtocolException('Illegal frame')
        return None

    
    def add(self = None, frame = None):
        if self.cont_data:
            pass
        elif frame.opcode in (ABNF.OPCODE_TEXT, ABNF.OPCODE_BINARY):
            frame.opcode = None
        self.cont_data = [
            frame.opcode,
            frame.data]
        if frame.fin:
            self.recving_frames = None
            return None

    
    def is_fire(self = None, frame = None):
