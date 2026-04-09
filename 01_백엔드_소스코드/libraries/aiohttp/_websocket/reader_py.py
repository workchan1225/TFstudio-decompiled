# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reader_py.pyc (Python 3.11)

'''Reader for WebSocket protocol versions 13 and 8.'''
import asyncio
import builtins
from collections import deque
from typing import Deque, Final, Optional, Set, Tuple, Union
from base_protocol import BaseProtocol
from compression_utils import ZLibDecompressor
from helpers import _EXC_SENTINEL, set_exception
from streams import EofStream
from helpers import UNPACK_CLOSE_CODE, UNPACK_LEN3, websocket_mask
from models import WS_DEFLATE_TRAILING, WebSocketError, WSCloseCode, WSMessage, WSMsgType
ALLOWED_CLOSE_CODES: Final[Set[int]] = WSCloseCode()
READ_HEADER = 1
READ_PAYLOAD_LENGTH = 2
READ_PAYLOAD_MASK = 3
READ_PAYLOAD = 4
WS_MSG_TYPE_BINARY = WSMsgType.BINARY
WS_MSG_TYPE_TEXT = WSMsgType.TEXT
OP_CODE_NOT_SET = -1
OP_CODE_CONTINUATION = WSMsgType.CONTINUATION.value
OP_CODE_TEXT = WSMsgType.TEXT.value
OP_CODE_BINARY = WSMsgType.BINARY.value
OP_CODE_CLOSE = WSMsgType.CLOSE.value
OP_CODE_PING = WSMsgType.PING.value
OP_CODE_PONG = WSMsgType.PONG.value
EMPTY_FRAME_ERROR = (True, b'')
EMPTY_FRAME = (False, b'')
COMPRESSED_NOT_SET = -1
COMPRESSED_FALSE = 0
COMPRESSED_TRUE = 1
TUPLE_NEW = tuple.__new__
cython_int = int

class WebSocketDataQueue:
    '''WebSocketDataQueue resumes and pauses an underlying stream.

    It is a destination for WebSocket data.
    '''
    
    def __init__(self = None, protocol = None, limit = None, *, loop):
        self._size = 0
        self._protocol = protocol
        self._limit = limit * 2
        self._loop = loop
        self._eof = False
        self._waiter = None
        self._exception = None
        self._buffer = deque()
        self._get_buffer = self._buffer.popleft
        self._put_buffer = self._buffer.append

    
    def is_eof(self = None):
        return self._eof

    
    def exception(self = None):
        return self._exception

    
    def set_exception(self = None, exc = None, exc_cause = None):
        self._eof = True
        self._exception = exc
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def _release_waiter(self = None):
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def feed_eof(self = None):
        self._eof = True
        self._release_waiter()
        self._exception = None

    
    def feed_data(self = None, data = None, size = None):
        self._put_buffer((data, size))
        self._release_waiter()
        if not self._size > self._limit or self._protocol._reading_paused:
            self._protocol.pause_reading()
            return None
        return self, self._size += size, ._size

    
    async def read(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _read_from_buffer(self = None):
        if self._buffer:
            (data, size) = self._get_buffer()
            if self._size < self._limit and self._protocol._reading_paused:
                self._protocol.resume_reading()
            return data
    # WARNING: Decompyle incomplete



class WebSocketReader:
    
    def __init__(self = None, queue = None, max_msg_size = None, compress = (True,)):
        self.queue = queue
        self._max_msg_size = max_msg_size
        self._exc = None
        self._partial = bytearray()
        self._state = READ_HEADER
        self._opcode = OP_CODE_NOT_SET
        self._frame_fin = False
        self._frame_opcode = OP_CODE_NOT_SET
        self._payload_fragments = []
        self._frame_payload_len = 0
        self._tail = b''
        self._has_mask = False
        self._frame_mask = None
        self._payload_bytes_to_read = 0
        self._payload_len_flag = 0
        self._compressed = COMPRESSED_NOT_SET
        self._decompressobj = None
        self._compress = compress

    
    def feed_eof(self = None):
        self.queue.feed_eof()

    
    def feed_data(self = None, data = None):
        if type(data) is not bytes:
            data = bytes(data)
    # WARNING: Decompyle incomplete

    
    def _handle_frame(self, fin = None, opcode = None, payload = None, compressed = ('fin', bool, 'opcode', Union[(int, cython_int)], 'payload', Union[(bytes, bytearray)], 'compressed', Union[(int, cython_int)], 'return', None)):
        if opcode in {
            OP_CODE_TEXT,
            OP_CODE_BINARY,
            OP_CODE_CONTINUATION}:
            if not fin:
                if opcode != OP_CODE_CONTINUATION:
                    self._opcode = opcode
                if self._max_msg_size and len(self._partial) >= self._max_msg_size:
                    raise WebSocketError(WSCloseCode.MESSAGE_TOO_BIG, f'''Message size {len(self._partial)} exceeds limit {self._max_msg_size}''')
                return None
            None(self._partial) = None
            if opcode == OP_CODE_CONTINUATION:
                if self._opcode == OP_CODE_NOT_SET:
                    raise WebSocketError(WSCloseCode.PROTOCOL_ERROR, 'Continuation frame for non started message')
                opcode = self._opcode
                self._opcode = OP_CODE_NOT_SET
            elif has_partial:
                raise WebSocketError(WSCloseCode.PROTOCOL_ERROR, f'''The opcode in non-fin frame is expected to be zero, got {opcode!r}''')
            if has_partial:
                assembled_payload = self._partial + payload
                self._partial.clear()
            else:
                assembled_payload = payload
            if self._max_msg_size and len(assembled_payload) >= self._max_msg_size:
                raise WebSocketError(WSCloseCode.MESSAGE_TOO_BIG, f'''Message size {len(assembled_payload)} exceeds limit {self._max_msg_size}''')
            if compressed:
                if not self._decompressobj:
                    self._decompressobj = ZLibDecompressor(suppress_deflate_header = True)
                payload_merged = self._decompressobj.decompress_sync(assembled_payload + WS_DEFLATE_TRAILING, self._max_msg_size + 1 if self._max_msg_size else self._max_msg_size)
                if self._max_msg_size and len(payload_merged) > self._max_msg_size:
                    raise WebSocketError(WSCloseCode.MESSAGE_TOO_BIG, f'''Decompressed message exceeds size limit {self._max_msg_size}''')
            elif type(assembled_payload) is bytes:
                payload_merged = assembled_payload
            else:
                payload_merged = bytes(assembled_payload)
            if opcode == OP_CODE_TEXT:
                
                try:
                    text = payload_merged.decode('utf-8')
                except UnicodeDecodeError:
                    exc = None
                    raise WebSocketError(WSCloseCode.INVALID_TEXT, 'Invalid UTF-8 text message'), exc
                    exc = None
                    del exc

                self.queue.feed_data(TUPLE_NEW(WSMessage, (WS_MSG_TYPE_TEXT, text, '')), len(payload_merged))
                return None
            None.queue.feed_data(TUPLE_NEW(WSMessage, (WS_MSG_TYPE_BINARY, payload_merged, '')), len(payload_merged))
            return None
        if opcode == OP_CODE_CLOSE:
            if len(payload) >= 2:
                close_code = UNPACK_CLOSE_CODE(payload[:2])[0]
                if close_code < 3000 and close_code not in ALLOWED_CLOSE_CODES:
                    raise WebSocketError(WSCloseCode.PROTOCOL_ERROR, f'''Invalid close code: {close_code}''')
                
                try:
                    close_message = payload[2:].decode('utf-8')
                except UnicodeDecodeError:
                    exc = None
                    raise WebSocketError(WSCloseCode.INVALID_TEXT, 'Invalid UTF-8 text message'), exc
                    exc = None
                    del exc

                msg = TUPLE_NEW(WSMessage, (WSMsgType.CLOSE, close_code, close_message))
            elif payload:
                raise WebSocketError(WSCloseCode.PROTOCOL_ERROR, f'''Invalid close frame: {fin} {opcode} {payload!r}''')
            msg = TUPLE_NEW(WSMessage, (WSMsgType.CLOSE, 0, ''))
            self.queue.feed_data(msg, 0)
            return None
        if opcode == OP_CODE_PING:
            msg = TUPLE_NEW(WSMessage, (WSMsgType.PING, payload, ''))
            self.queue.feed_data(msg, len(payload))
            return None
        if None == OP_CODE_PONG:
            msg = TUPLE_NEW(WSMessage, (WSMsgType.PONG, payload, ''))
            self.queue.feed_data(msg, len(payload))
            return None
        raise None(WSCloseCode.PROTOCOL_ERROR, f'''Unexpected opcode={opcode!r}''')

    
    def _feed_data(self = None, data = None):
        '''Return the next frame from the socket.'''
        if self._tail:
            data, self._tail = self._tail + data, b''
        start_pos = 0
        data_len = len(data)
        data_cstr = data
    # WARNING: Decompyle incomplete
