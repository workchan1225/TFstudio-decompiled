# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

'''Helpers for WebSocket protocol versions 13 and 8.'''
import functools
import re
from struct import Struct
from typing import TYPE_CHECKING, Final, List, Optional, Pattern, Tuple
from helpers import NO_EXTENSIONS
from models import WSHandshakeError
UNPACK_LEN3 = Struct('!Q').unpack_from
UNPACK_CLOSE_CODE = Struct('!H').unpack
PACK_LEN1 = Struct('!BB').pack
PACK_LEN2 = Struct('!BBH').pack
PACK_LEN3 = Struct('!BBQ').pack
PACK_CLOSE_CODE = Struct('!H').pack
PACK_RANDBITS = Struct('!L').pack
MSG_SIZE: Final[int] = 16384
MASK_LEN: Final[int] = 4
WS_KEY: Final[bytes] = b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
_xor_table = (lambda : range(256)())()

def _websocket_mask_python(mask = None, data = None):
    '''Websocket masking function.

    `mask` is a `bytes` object of length 4; `data` is a `bytearray`
    object of any length. The contents of `data` are masked with `mask`,
    as specified in section 5.3 of RFC 6455.

    Note that this function mutates the `data` argument.

    This pure-python implementation may be replaced by an optimized
    version when available.

    '''
    pass
# WARNING: Decompyle incomplete

if TYPE_CHECKING or NO_EXTENSIONS:
    websocket_mask = _websocket_mask_python
else:
    
    try:
        from mask import _websocket_mask_cython
        websocket_mask = _websocket_mask_cython
    except ImportError:
        websocket_mask = _websocket_mask_python

    _WS_EXT_RE: Final[Pattern[str]] = re.compile('^(?:;\\s*(?:(server_no_context_takeover)|(client_no_context_takeover)|(server_max_window_bits(?:=(\\d+))?)|(client_max_window_bits(?:=(\\d+))?)))*$')
    _WS_EXT_RE_SPLIT: Final[Pattern[str]] = re.compile('permessage-deflate([^,]+)?')
    
    def ws_ext_parse(extstr = None, isserver = None):
        if not extstr:
            return (0, False)
        compress = None
        notakeover = False
        for ext in _WS_EXT_RE_SPLIT.finditer(extstr):
            defext = ext.group(1)
            if not defext:
                compress = 15
            else:
                match = _WS_EXT_RE.match(defext)
                if match:
                    compress = 15
                    if isserver:
                        if match.group(4):
                            compress = int(match.group(4))
                            if compress > 15 or compress < 9:
                                compress = 0
                                continue
                        if match.group(1):
                            notakeover = True
                    elif match.group(6):
                        compress = int(match.group(6))
                        if compress > 15 or compress < 9:
                            raise WSHandshakeError('Invalid window size')
                    if match.group(2):
                        notakeover = True
                elif not isserver:
                    raise WSHandshakeError('Extension for deflate not supported' + ext.group(1))
            return (compress, notakeover)

    
    def ws_ext_gen(compress = None, isserver = None, server_notakeover = None):
        if compress < 9 or compress > 15:
            raise ValueError('Compress wbits must between 9 and 15, zlib does not support wbits=8')
        enabledext = [
            'permessage-deflate']
        if not isserver:
            enabledext.append('client_max_window_bits')
        if compress < 15:
            enabledext.append('server_max_window_bits=' + str(compress))
        if server_notakeover:
            enabledext.append('server_no_context_takeover')
        return '; '.join(enabledext)

    return None
