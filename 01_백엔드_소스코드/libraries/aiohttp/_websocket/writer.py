# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: writer.pyc (Python 3.11)

'''WebSocket protocol versions 13 and 8.'''
import asyncio
import random
import sys
from functools import partial
from typing import Final, Optional, Set, Union
from base_protocol import BaseProtocol
from client_exceptions import ClientConnectionResetError
from compression_utils import ZLibBackend, ZLibCompressor
from helpers import MASK_LEN, MSG_SIZE, PACK_CLOSE_CODE, PACK_LEN1, PACK_LEN2, PACK_LEN3, PACK_RANDBITS, websocket_mask
from models import WS_DEFLATE_TRAILING, WSMsgType
DEFAULT_LIMIT: Final[int] = 65536
WS_CONTROL_FRAME_OPCODE: Final[int] = 8
WEBSOCKET_MAX_SYNC_CHUNK_SIZE = 16384

class WebSocketWriter:
    '''WebSocket writer.

    The writer is responsible for sending messages to the client. It is
    created by the protocol when a connection is established. The writer
    should avoid implementing any application logic and should only be
    concerned with the low-level details of the WebSocket protocol.
    '''
    
    def __init__(self = None, protocol = None, transport = None, *, use_mask, limit, random, compress, notakeover):
        '''Initialize a WebSocket writer.'''
        self.protocol = protocol
        self.transport = transport
        self.use_mask = use_mask
        self.get_random_bits = partial(random.getrandbits, 32)
        self.compress = compress
        self.notakeover = notakeover
        self._closing = False
        self._limit = limit
        self._output_size = 0
        self._compressobj = None
        self._send_lock = asyncio.Lock()
        self._background_tasks = set()

    
    async def send_frame(self = None, message = None, opcode = None, compress = (None,)):
        '''Send a frame over the websocket with message as its payload.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _write_websocket_frame(self = None, message = None, opcode = None, rsv = ('message', bytes, 'opcode', int, 'rsv', int, 'return', None)):
        '''
        Write a websocket frame to the transport.

        This method handles frame header construction, masking, and writing to transport.
        It does not handle compression or flow control - those are the responsibility
        of the caller.
        '''
        msg_length = len(message)
        use_mask = self.use_mask
        mask_bit = 128 if use_mask else 0
        first_byte = 128 | rsv | opcode
        if msg_length < 126:
            header = PACK_LEN1(first_byte, msg_length | mask_bit)
            header_len = 2
        elif msg_length < 65536:
            header = PACK_LEN2(first_byte, 126 | mask_bit, msg_length)
            header_len = 4
        else:
            header = PACK_LEN3(first_byte, 127 | mask_bit, msg_length)
            header_len = 10
        if self.transport.is_closing():
            raise ClientConnectionResetError('Cannot write to closing transport')
        if use_mask:
            mask = PACK_RANDBITS(self.get_random_bits())
            message = bytearray(message)
            websocket_mask(mask, message)
            self.transport.write(header + mask + message)
        elif msg_length > MSG_SIZE:
            self.transport.write(header)
            self.transport.write(message)
        else:
            self.transport.write(header + message)

    
    def _get_compressor(self = None, compress = None):
        '''Get or create a compressor object for the given compression level.'''
        if compress:
            return ZLibCompressor(level = ZLibBackend.Z_BEST_SPEED, wbits = -compress, max_sync_chunk_size = WEBSOCKET_MAX_SYNC_CHUNK_SIZE)
        if not None._compressobj:
            self._compressobj = ZLibCompressor(level = ZLibBackend.Z_BEST_SPEED, wbits = -(self.compress), max_sync_chunk_size = WEBSOCKET_MAX_SYNC_CHUNK_SIZE)
        return self._compressobj

    
    def _send_compressed_frame_sync(self = None, message = None, opcode = None, compress = ('message', bytes, 'opcode', int, 'compress', Optional[int], 'return', None)):
        '''
        Synchronous send for small compressed frames.

        This is used for small compressed payloads that compress synchronously in the event loop.
        Since there are no await points, this is inherently cancellation-safe.
        '''
        compressobj = self._get_compressor(compress)
        self._write_websocket_frame((compressobj.compress_sync(message) + compressobj.flush(ZLibBackend.Z_FULL_FLUSH if self.notakeover else ZLibBackend.Z_SYNC_FLUSH)).removesuffix(WS_DEFLATE_TRAILING), opcode, 64)

    
    async def _send_compressed_frame_async_locked(self = None, message = None, opcode = None, compress = ('message', bytes, 'opcode', int, 'compress', Optional[int], 'return', None)):
        '''
        Async send for large compressed frames with lock.

        Acquires the lock and compresses large payloads asynchronously in
        the executor. The lock is held for the entire operation to ensure
        the compressor state is not corrupted by concurrent sends.

        MUST be run shielded from cancellation. If cancelled after
        compression but before sending, the compressor state would be
        advanced but data not sent, corrupting subsequent frames.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None, code = None, message = None):
        '''Close the websocket, sending the specified code and message.'''
        pass
    # WARNING: Decompyle incomplete
