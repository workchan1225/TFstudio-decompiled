# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

'''
wsproto/extensions
~~~~~~~~~~~~~~~~~~

WebSocket extensions.
'''
from __future__ import annotations
import zlib
from abc import ABC, abstractmethod
from typing import Optional
from frame_protocol import CloseReason, FrameDecoder, FrameProtocol, Opcode, RsvBits

class Extension(ABC):
    name: 'str' = 'Extension'
    
    def enabled(self = None):
        return False

    offer = (lambda self = None: pass)()
    
    def accept(self = None, offer = None):
        pass

    
    def finalize(self = None, offer = None):
        pass

    
    def frame_inbound_header(self, proto = None, opcode = None, rsv = None, payload_length = ('proto', 'FrameDecoder | FrameProtocol', 'opcode', 'Opcode', 'rsv', 'RsvBits', 'payload_length', 'int', 'return', 'CloseReason | RsvBits')):
        return RsvBits(False, False, False)

    
    def frame_inbound_payload_data(self = None, proto = None, data = None):
        return data

    
    def frame_inbound_complete(self = None, proto = None, fin = None):
        pass

    
    def frame_outbound(self, proto, opcode = None, rsv = None, data = None, fin = ('proto', 'FrameDecoder | FrameProtocol', 'opcode', 'Opcode', 'rsv', 'RsvBits', 'data', 'bytes', 'fin', 'bool', 'return', 'tuple[RsvBits, bytes]')):
        return (rsv, data)



class PerMessageDeflate(Extension):
    name = 'permessage-deflate'
    DEFAULT_CLIENT_MAX_WINDOW_BITS = 15
    DEFAULT_SERVER_MAX_WINDOW_BITS = 15
    
    def __init__(self = None, client_no_context_takeover = None, client_max_window_bits = None, server_no_context_takeover = (False, None, False, None), server_max_window_bits = ('client_no_context_takeover', 'bool', 'client_max_window_bits', 'int | None', 'server_no_context_takeover', 'bool', 'server_max_window_bits', 'int | None', 'return', 'None')):
        self.client_no_context_takeover = client_no_context_takeover
        self.server_no_context_takeover = server_no_context_takeover
        self._client_max_window_bits = self.DEFAULT_CLIENT_MAX_WINDOW_BITS
        self._server_max_window_bits = self.DEFAULT_SERVER_MAX_WINDOW_BITS
    # WARNING: Decompyle incomplete

    client_max_window_bits = (lambda self = None: self._client_max_window_bits)()
    client_max_window_bits = (lambda self = None, value = None: if value < 9 or value > 15:
msg = 'Window size must be between 9 and 15 inclusive'raise ValueError(msg)self._client_max_window_bits = value)()
    server_max_window_bits = (lambda self = None: self._server_max_window_bits)()
    server_max_window_bits = (lambda self = None, value = None: if value < 9 or value > 15:
msg = 'Window size must be between 9 and 15 inclusive'raise ValueError(msg)self._server_max_window_bits = value)()
    
    def _compressible_opcode(self = None, opcode = None):
        return opcode in (Opcode.TEXT, Opcode.BINARY, Opcode.CONTINUATION)

    
    def enabled(self = None):
        return self._enabled

    
    def offer(self = None):
        parameters = [
            f'''client_max_window_bits={self.client_max_window_bits}''',
            f'''server_max_window_bits={self.server_max_window_bits}''']
        if self.client_no_context_takeover:
            parameters.append('client_no_context_takeover')
        if self.server_no_context_takeover:
            parameters.append('server_no_context_takeover')
        return '; '.join(parameters)

    
    def finalize(self = None, offer = None):
        bits = offer.split(';')()
        for bit in bits[1:]:
            if bit.startswith('client_no_context_takeover'):
                self.client_no_context_takeover = True
                continue
            if bit.startswith('server_no_context_takeover'):
                self.server_no_context_takeover = True
                continue
            if bit.startswith('client_max_window_bits'):
                self.client_max_window_bits = int(bit.split('=', 1)[1].strip())
                continue
            if bit.startswith('server_max_window_bits'):
                self.server_max_window_bits = int(bit.split('=', 1)[1].strip())
            self._enabled = True
            return None

    
    def _parse_params(self = None, params = None):
        client_max_window_bits = None
        server_max_window_bits = None
        bits = params.split(';')()
        for bit in bits[1:]:
            if bit.startswith('client_no_context_takeover'):
                self.client_no_context_takeover = True
                continue
            if bit.startswith('server_no_context_takeover'):
                self.server_no_context_takeover = True
                continue
            if bit.startswith('client_max_window_bits'):
                if '=' in bit:
                    client_max_window_bits = int(bit.split('=', 1)[1].strip())
                    continue
                client_max_window_bits = self.client_max_window_bits
                continue
            if bit.startswith('server_max_window_bits'):
                if '=' in bit:
                    server_max_window_bits = int(bit.split('=', 1)[1].strip())
                    continue
                server_max_window_bits = self.server_max_window_bits
            return (client_max_window_bits, server_max_window_bits)

    
    def accept(self = None, offer = None):
        (client_max_window_bits, server_max_window_bits) = self._parse_params(offer)
        parameters = []
        if self.client_no_context_takeover:
            parameters.append('client_no_context_takeover')
        if self.server_no_context_takeover:
            parameters.append('server_no_context_takeover')
    # WARNING: Decompyle incomplete

    
    def frame_inbound_header(self, proto = None, opcode = None, rsv = None, payload_length = ('proto', 'FrameDecoder | FrameProtocol', 'opcode', 'Opcode', 'rsv', 'RsvBits', 'payload_length', 'int', 'return', 'CloseReason | RsvBits')):
        if rsv.rsv1 and opcode.iscontrol():
            return CloseReason.PROTOCOL_ERROR
        if None.rsv1 and opcode is Opcode.CONTINUATION:
            return CloseReason.PROTOCOL_ERROR
        self._inbound_is_compressible = None._compressible_opcode(opcode)
    # WARNING: Decompyle incomplete

    
    def frame_inbound_payload_data(self = None, proto = None, data = None):
        if not self._inbound_compressed or self._inbound_is_compressible:
            return data
    # WARNING: Decompyle incomplete

    
    def frame_inbound_complete(self = None, proto = None, fin = None):
        if not fin:
            return None
        if not None._inbound_is_compressible:
            self._inbound_compressed = None
            return None
        if not None._inbound_compressed:
            self._inbound_compressed = None
            return None
    # WARNING: Decompyle incomplete

    
    def frame_outbound(self, proto, opcode = None, rsv = None, data = None, fin = ('proto', 'FrameDecoder | FrameProtocol', 'opcode', 'Opcode', 'rsv', 'RsvBits', 'data', 'bytes', 'fin', 'bool', 'return', 'tuple[RsvBits, bytes]')):
        if not self._compressible_opcode(opcode):
            return (rsv, data)
        if None is not Opcode.CONTINUATION:
            rsv = RsvBits(True, rsv[1], rsv[2])
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        descr = [
            f'''client_max_window_bits={self.client_max_window_bits}''']
        if self.client_no_context_takeover:
            descr.append('client_no_context_takeover')
        descr.append(f'''server_max_window_bits={self.server_max_window_bits}''')
        if self.server_no_context_takeover:
            descr.append('server_no_context_takeover')
        return '<{} {}>'.format(self.__class__.__name__, '; '.join(descr))


SUPPORTED_EXTENSIONS = {
    PerMessageDeflate.name: PerMessageDeflate }
