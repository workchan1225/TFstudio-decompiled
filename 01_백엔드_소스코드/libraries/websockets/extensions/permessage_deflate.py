# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permessage_deflate.pyc (Python 3.11)

from __future__ import annotations
import zlib
from collections.abc import Sequence
from typing import Any, Literal
from  import frames
from exceptions import DuplicateParameter, InvalidParameterName, InvalidParameterValue, NegotiationError, PayloadTooBig, ProtocolError
from typing import ExtensionName, ExtensionParameter
from base import ClientExtensionFactory, Extension, ServerExtensionFactory
__all__ = [
    'PerMessageDeflate',
    'ClientPerMessageDeflateFactory',
    'enable_client_permessage_deflate',
    'ServerPerMessageDeflateFactory',
    'enable_server_permessage_deflate']
_EMPTY_UNCOMPRESSED_BLOCK = b'\x00\x00\xff\xff'
_MAX_WINDOW_BITS_VALUES = range(8, 16)()

class PerMessageDeflate(Extension):
    '''
    Per-Message Deflate extension.

    '''
    name = ExtensionName('permessage-deflate')
    
    def __init__(self, remote_no_context_takeover = None, local_no_context_takeover = None, remote_max_window_bits = None, local_max_window_bits = (None,), compress_settings = ('remote_no_context_takeover', 'bool', 'local_no_context_takeover', 'bool', 'remote_max_window_bits', 'int', 'local_max_window_bits', 'int', 'compress_settings', 'dict[Any, Any] | None', 'return', 'None')):
        '''
        Configure the Per-Message Deflate extension.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''PerMessageDeflate(remote_no_context_takeover={self.remote_no_context_takeover}, local_no_context_takeover={self.local_no_context_takeover}, remote_max_window_bits={self.remote_max_window_bits}, local_max_window_bits={self.local_max_window_bits})'''

    
    def decode(self = None, frame = None, *, max_size):
        '''
        Decode an incoming frame.

        '''
        if frame.opcode in frames.CTRL_OPCODES:
            return frame
        if None.opcode is frames.OP_CONT:
            if not self.decode_cont_data:
                return frame
            if None.fin:
                self.decode_cont_data = False
            elif not frame.rsv1:
                return frame
        if not frame.fin:
            self.decode_cont_data = True
        if self.remote_no_context_takeover:
            self.decoder = zlib.decompressobj(wbits = -(self.remote_max_window_bits))
        if frame.fin and len(frame.data) < 2044:
            data = bytes(frame.data) + _EMPTY_UNCOMPRESSED_BLOCK
        else:
            data = frame.data
    # WARNING: Decompyle incomplete

    
    def encode(self = None, frame = None):
        '''
        Encode an outgoing frame.

        '''
        if frame.opcode in frames.CTRL_OPCODES:
            return frame
    # WARNING: Decompyle incomplete



def _build_parameters(server_no_context_takeover = None, client_no_context_takeover = (lambda .0: [ str(bits) for bits in .0 ]), server_max_window_bits = None, client_max_window_bits = ('server_no_context_takeover', 'bool', 'client_no_context_takeover', 'bool', 'server_max_window_bits', 'int | None', 'client_max_window_bits', 'int | Literal[True] | None', 'return', 'list[ExtensionParameter]')):
    '''
    Build a list of ``(name, value)`` pairs for some compression parameters.

    '''
    params = []
    if server_no_context_takeover:
        params.append(('server_no_context_takeover', None))
    if client_no_context_takeover:
        params.append(('client_no_context_takeover', None))
    if server_max_window_bits:
        params.append(('server_max_window_bits', str(server_max_window_bits)))
    if client_max_window_bits is True:
        params.append(('client_max_window_bits', None))
    elif client_max_window_bits:
        params.append(('client_max_window_bits', str(client_max_window_bits)))
    return params


def _extract_parameters(params = None, *, is_server):
    '''
    Extract compression parameters from a list of ``(name, value)`` pairs.

    If ``is_server`` is :obj:`True`, ``client_max_window_bits`` may be
    provided without a value. This is only allowed in handshake requests.

    '''
    server_no_context_takeover = False
    client_no_context_takeover = False
    server_max_window_bits = None
    client_max_window_bits = None
# WARNING: Decompyle incomplete


class ClientPerMessageDeflateFactory(ClientExtensionFactory):
    """
    Client-side extension factory for the Per-Message Deflate extension.

    Parameters behave as described in `section 7.1 of RFC 7692`_.

    .. _section 7.1 of RFC 7692: https://datatracker.ietf.org/doc/html/rfc7692#section-7.1

    Set them to :obj:`True` to include them in the negotiation offer without a
    value or to an integer value to include them with this value.

    Args:
        server_no_context_takeover: Prevent server from using context takeover.
        client_no_context_takeover: Prevent client from using context takeover.
        server_max_window_bits: Maximum size of the server's LZ77 sliding window
            in bits, between 8 and 15.
        client_max_window_bits: Maximum size of the client's LZ77 sliding window
            in bits, between 8 and 15, or :obj:`True` to indicate support without
            setting a limit.
        compress_settings: Additional keyword arguments for :func:`zlib.compressobj`,
            excluding ``wbits``.

    """
    name = ExtensionName('permessage-deflate')
    
    def __init__(self, server_no_context_takeover = None, client_no_context_takeover = None, server_max_window_bits = None, client_max_window_bits = (False, False, None, True, None), compress_settings = ('server_no_context_takeover', 'bool', 'client_no_context_takeover', 'bool', 'server_max_window_bits', 'int | None', 'client_max_window_bits', 'int | Literal[True] | None', 'compress_settings', 'dict[str, Any] | None', 'return', 'None')):
        '''
        Configure the Per-Message Deflate extension factory.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_request_params(self = None):
        '''
        Build request parameters.

        '''
        return _build_parameters(self.server_no_context_takeover, self.client_no_context_takeover, self.server_max_window_bits, self.client_max_window_bits)

    
    def process_response_params(self = None, params = None, accepted_extensions = None):
        '''
        Process response parameters.

        Return an extension instance.

        '''
        pass
    # WARNING: Decompyle incomplete



def enable_client_permessage_deflate(extensions = None):
    """
    Enable Per-Message Deflate with default settings in client extensions.

    If the extension is already present, perhaps with non-default settings,
    the configuration isn't changed.

    """
    pass
# WARNING: Decompyle incomplete


class ServerPerMessageDeflateFactory(ServerExtensionFactory):
    """
    Server-side extension factory for the Per-Message Deflate extension.

    Parameters behave as described in `section 7.1 of RFC 7692`_.

    .. _section 7.1 of RFC 7692: https://datatracker.ietf.org/doc/html/rfc7692#section-7.1

    Set them to :obj:`True` to include them in the negotiation offer without a
    value or to an integer value to include them with this value.

    Args:
        server_no_context_takeover: Prevent server from using context takeover.
        client_no_context_takeover: Prevent client from using context takeover.
        server_max_window_bits: Maximum size of the server's LZ77 sliding window
            in bits, between 8 and 15.
        client_max_window_bits: Maximum size of the client's LZ77 sliding window
            in bits, between 8 and 15.
        compress_settings: Additional keyword arguments for :func:`zlib.compressobj`,
            excluding ``wbits``.
        require_client_max_window_bits: Do not enable compression at all if
            client doesn't advertise support for ``client_max_window_bits``;
            the default behavior is to enable compression without enforcing
            ``client_max_window_bits``.

    """
    name = ExtensionName('permessage-deflate')
    
    def __init__(self, server_no_context_takeover, client_no_context_takeover = None, server_max_window_bits = None, client_max_window_bits = None, compress_settings = (False, False, None, None, None, False), require_client_max_window_bits = ('server_no_context_takeover', 'bool', 'client_no_context_takeover', 'bool', 'server_max_window_bits', 'int | None', 'client_max_window_bits', 'int | None', 'compress_settings', 'dict[str, Any] | None', 'require_client_max_window_bits', 'bool', 'return', 'None')):
        '''
        Configure the Per-Message Deflate extension factory.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def process_request_params(self = None, params = None, accepted_extensions = None):
        '''
        Process request parameters.

        Return response params and an extension instance.

        '''
        pass
    # WARNING: Decompyle incomplete



def enable_server_permessage_deflate(extensions = None):
    """
    Enable Per-Message Deflate with default settings in server extensions.

    If the extension is already present, perhaps with non-default settings,
    the configuration isn't changed.

    """
    pass
# WARNING: Decompyle incomplete
