# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: framing.pyc (Python 3.11)

from __future__ import annotations
import struct
from collections.abc import Awaitable, Sequence
from typing import Any, Callable, NamedTuple
from  import extensions, frames
from exceptions import PayloadTooBig, ProtocolError
from frames import BytesLike
from typing import Data

try:
    from speedups import apply_mask
except ImportError:
    from utils import apply_mask


class Frame(NamedTuple):
    data: 'bytes' = 'Frame'
    rsv1: 'bool' = False
    rsv2: 'bool' = False
    rsv3: 'bool' = False
    new_frame = (lambda self = None: frames.Frame(self.opcode, self.data, self.fin, self.rsv1, self.rsv2, self.rsv3))()
    
    def __str__(self = None):
        return str(self.new_frame)

    
    def check(self = None):
        return self.new_frame.check()

    read = (lambda cls = None, reader = None, *, mask, max_size: pass# WARNING: Decompyle incomplete
)()
    
    def write(self = None, write = None, *, mask, extensions):
        '''
        Write a WebSocket frame.

        Args:
            frame: Frame to write.
            write: Function that writes bytes.
            mask: Whether the frame should be masked i.e. whether the write
                happens on the client side.
            extensions: List of extensions, applied in order.

        Raises:
            ProtocolError: If the frame contains incorrect values.

        '''
        write(self.new_frame.serialize(mask = mask, extensions = extensions))



def prepare_data(data = None):
    """
    Convert a string or byte-like object to an opcode and a bytes-like object.

    This function is designed for data frames.

    If ``data`` is a :class:`str`, return ``OP_TEXT`` and a :class:`bytes`
    object encoding ``data`` in UTF-8.

    If ``data`` is a bytes-like object, return ``OP_BINARY`` and a bytes-like
    object.

    Raises:
        TypeError: If ``data`` doesn't have a supported type.

    """
    if isinstance(data, str):
        return (frames.Opcode.TEXT, data.encode())
    if None(data, BytesLike):
        return (frames.Opcode.BINARY, data)
    raise None('data must be str or bytes-like')


def prepare_ctrl(data = None):
    """
    Convert a string or byte-like object to bytes.

    This function is designed for ping and pong frames.

    If ``data`` is a :class:`str`, return a :class:`bytes` object encoding
    ``data`` in UTF-8.

    If ``data`` is a bytes-like object, return a :class:`bytes` object.

    Raises:
        TypeError: If ``data`` doesn't have a supported type.

    """
    if isinstance(data, str):
        return data.encode()
    if None(data, BytesLike):
        return bytes(data)
    raise None('data must be str or bytes-like')

encode_data = prepare_ctrl
from frames import Close

def parse_close(data = None):
    """
    Parse the payload from a close frame.

    Returns:
        Close code and reason.

    Raises:
        ProtocolError: If data is ill-formed.
        UnicodeDecodeError: If the reason isn't valid UTF-8.

    """
    close = Close.parse(data)
    return (close.code, close.reason)


def serialize_close(code = None, reason = None):
    '''
    Serialize the payload for a close frame.

    '''
    return Close(code, reason).serialize()
