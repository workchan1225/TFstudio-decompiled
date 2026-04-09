# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tls.pyc (Python 3.11)

from __future__ import annotations
__all__ = ('TLSAttribute', 'TLSConnectable', 'TLSListener', 'TLSStream')
import logging
import re
import ssl
import sys
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from functools import wraps
from ssl import SSLContext
from typing import Any, TypeVar
from  import BrokenResourceError, EndOfStream, aclose_forcefully, get_cancelled_exc_class, to_thread
from _core._typedattr import TypedAttributeSet, typed_attribute
from abc import AnyByteStream, AnyByteStreamConnectable, ByteStream, ByteStreamConnectable, Listener, TaskGroup
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from typing_extensions import TypeVarTuple, Unpack
if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override
T_Retval = TypeVar('T_Retval')
PosArgsT = TypeVarTuple('PosArgsT')
_PCTRTT: 'TypeAlias' = tuple[(tuple[(str, str)], ...)]
_PCTRTTT: 'TypeAlias' = tuple[(_PCTRTT, ...)]

class TLSAttribute(TypedAttributeSet):
    '''Contains Transport Layer Security related attributes.'''
    alpn_protocol: 'str | None' = typed_attribute()
    channel_binding_tls_unique: 'bytes' = typed_attribute()
    cipher: 'tuple[str, str, int]' = typed_attribute()
    peer_certificate: 'None | dict[str, str | _PCTRTTT | _PCTRTT]' = typed_attribute()
    peer_certificate_binary: 'bytes | None' = typed_attribute()
    server_side: 'bool' = typed_attribute()
    shared_ciphers: 'list[tuple[str, str, int]] | None' = typed_attribute()
    ssl_object: 'ssl.SSLObject' = typed_attribute()
    standard_compatible: 'bool' = typed_attribute()
    tls_version: 'str' = typed_attribute()

TLSStream = <NODE:12>()

def TLSListener():
    '''TLSListener'''
    ssl_context: 'ssl.SSLContext' = '\n    A convenience listener that wraps another listener and auto-negotiates a TLS session\n    on every accepted connection.\n\n    If the TLS handshake times out or raises an exception,\n    :meth:`handle_handshake_error` is called to do whatever post-mortem processing is\n    deemed necessary.\n\n    Supports only the :attr:`~TLSAttribute.standard_compatible` extra attribute.\n\n    :param Listener listener: the listener to wrap\n    :param ssl_context: the SSL context object\n    :param standard_compatible: a flag passed through to :meth:`TLSStream.wrap`\n    :param handshake_timeout: time limit for the TLS handshake\n        (passed to :func:`~anyio.fail_after`)\n    '
    standard_compatible: 'bool' = True
    handshake_timeout: 'float' = 30
    handle_handshake_error = (lambda exc = None, stream = None: pass# WARNING: Decompyle incomplete
)()
    
    async def serve(self = None, handler = None, task_group = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    extra_attributes = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

TLSListener = <NODE:27>(TLSListener, 'TLSListener', Listener[TLSStream])()

class TLSConnectable(ByteStreamConnectable):
    """
    Wraps another connectable and does TLS negotiation after a successful connection.

    :param connectable: the connectable to wrap
    :param hostname: host name of the server (if host name checking is desired)
    :param ssl_context: the SSLContext object to use (if not provided, a secure default
        will be created)
    :param standard_compatible: if ``False``, skip the closing handshake when closing
        the connection, and don't raise an exception if the server does the same
    """
    
    def __init__(self = None, connectable = None, *, hostname, ssl_context, standard_compatible):
        self.connectable = connectable
        if not ssl_context:
            pass
        self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        if not isinstance(self.ssl_context, ssl.SSLContext):
            raise TypeError(f'''ssl_context must be an instance of ssl.SSLContext, not {type(self.ssl_context).__name__}''')
        self.hostname = hostname
        self.standard_compatible = standard_compatible

    connect = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
