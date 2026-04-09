# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dtls.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import enum
import errno
import hmac
import os
import struct
import warnings
import weakref
from itertools import count
from typing import TYPE_CHECKING, Generic, TypeAlias, TypeVar
from weakref import ReferenceType, WeakValueDictionary
import attrs
import trio
from _util import NoPublicConstructor, final
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Iterable, Iterator
    from types import TracebackType
    SSL = SSL
    import OpenSSL
    from typing_extensions import Self, TypeVarTuple, Unpack
    from trio._socket import AddressFormat
    from trio.socket import SocketType
    PosArgsT = TypeVarTuple('PosArgsT')
MAX_UDP_PACKET_SIZE = 65527

def packet_header_overhead(sock = None):
    if sock.family == trio.socket.AF_INET:
        return 28


def worst_case_mtu(sock = None):
    if sock.family == trio.socket.AF_INET:
        return 576 - packet_header_overhead(sock)
    return None - packet_header_overhead(sock)


def best_guess_mtu(sock = None):
    return 1500 - packet_header_overhead(sock)


class ContentType(enum.IntEnum):
    change_cipher_spec = 20
    alert = 21
    handshake = 22
    application_data = 23
    heartbeat = 24


class HandshakeType(enum.IntEnum):
    hello_request = 0
    client_hello = 1
    server_hello = 2
    hello_verify_request = 3
    new_session_ticket = 4
    end_of_early_data = 4
    encrypted_extensions = 8
    certificate = 11
    server_key_exchange = 12
    certificate_request = 13
    server_hello_done = 14
    certificate_verify = 15
    client_key_exchange = 16
    finished = 20
    certificate_url = 21
    certificate_status = 22
    supplemental_data = 23
    key_update = 24
    compressed_certificate = 25
    ekt_key = 26
    message_hash = 254


class ProtocolVersion:
    DTLS10 = bytes([
        254,
        255])
    DTLS12 = bytes([
        254,
        253])

EPOCH_MASK = 0xFFFF000000000000

class BadPacket(Exception):
    pass


def part_of_handshake_untrusted(packet = None):
    return packet[3:5] == b'\x00\x00'


def is_client_hello_untrusted(packet = None):
    
    try:
        if packet[0] == ContentType.handshake:
            return packet[13] == HandshakeType.client_hello
        except IndexError:
            return False


RECORD_HEADER = struct.Struct('!B2sQH')

def to_hex(data = None):
    return data.hex()

Record = <NODE:12>()

def records_untrusted(packet = None):
    pass
# WARNING: Decompyle incomplete


def encode_record(record = None):
    header = RECORD_HEADER.pack(record.content_type, record.version, record.epoch_seqno, len(record.payload))
    return header + record.payload

HANDSHAKE_MESSAGE_HEADER = struct.Struct('!B3sH3s3s')
HandshakeFragment = <NODE:12>()

def decode_handshake_fragment_untrusted(payload = None):
    
    try:
        (msg_type, msg_len_bytes, msg_seq, frag_offset_bytes, frag_len_bytes) = HANDSHAKE_MESSAGE_HEADER.unpack_from(payload)
    except struct.error:
        exc = None
        raise BadPacket('bad handshake message header'), exc
        exc = None
        del exc

    msg_len = int.from_bytes(msg_len_bytes, 'big')
    frag_offset = int.from_bytes(frag_offset_bytes, 'big')
    frag_len = int.from_bytes(frag_len_bytes, 'big')
    frag = payload[HANDSHAKE_MESSAGE_HEADER.size:]
    if len(frag) != frag_len:
        raise BadPacket("handshake fragment length doesn't match record length")
    return HandshakeFragment(msg_type, msg_len, msg_seq, frag_offset, frag_len, frag)


def encode_handshake_fragment(hsf = None):
    hs_header = HANDSHAKE_MESSAGE_HEADER.pack(hsf.msg_type, hsf.msg_len.to_bytes(3, 'big'), hsf.msg_seq, hsf.frag_offset.to_bytes(3, 'big'), hsf.frag_len.to_bytes(3, 'big'))
    return hs_header + hsf.frag


def decode_client_hello_untrusted(packet = None):
    
    try:
        record = next(records_untrusted(packet))
        if record.content_type != ContentType.handshake:
            raise BadPacket('not a handshake record')
        fragment = decode_handshake_fragment_untrusted(record.payload)
        if fragment.msg_type != HandshakeType.client_hello:
            raise BadPacket('not a ClientHello')
        if fragment.frag_offset != 0:
            raise BadPacket('fragmented ClientHello')
        if fragment.frag_len != fragment.msg_len:
            raise BadPacket('fragmented ClientHello')
        body = fragment.frag
        session_id_len = body[34]
        cookie_len_offset = 35 + session_id_len
        cookie_len = body[cookie_len_offset]
        cookie_start = cookie_len_offset + 1
        cookie_end = cookie_start + cookie_len
        before_cookie = body[:cookie_len_offset]
        cookie = body[cookie_start:cookie_end]
        after_cookie = body[cookie_end:]
        if len(cookie) != cookie_len:
            raise BadPacket('short cookie')
        return (record.epoch_seqno, cookie, before_cookie + after_cookie)
    except (struct.error, IndexError):
        exc = None
        raise BadPacket('bad ClientHello'), exc
        exc = None
        del exc


HandshakeMessage = <NODE:12>()
PseudoHandshakeMessage = <NODE:12>()
OpaqueHandshakeMessage = <NODE:12>()
_AnyHandshakeMessage: 'TypeAlias' = HandshakeMessage | PseudoHandshakeMessage | OpaqueHandshakeMessage

def decode_volley_trusted(volley = attrs.frozen):
    messages = []
    messages_by_seq = { }
# WARNING: Decompyle incomplete


class RecordEncoder:
    
    def __init__(self = None):
        self._record_seq = count()

    
    def set_first_record_number(self = None, n = None):
        self._record_seq = count(n)

    
    def encode_volley(self = None, messages = None, mtu = None):
        packets = []
        packet = bytearray()
    # WARNING: Decompyle incomplete


COOKIE_REFRESH_INTERVAL = 30
KEY_BYTES = 32
COOKIE_HASH = 'sha256'
SALT_BYTES = 8
COOKIE_LENGTH = 32

def _current_cookie_tick():
    return int(trio.current_time() / COOKIE_REFRESH_INTERVAL)


def _signable(*fields):
    out = []
    for field in fields:
        out.extend((struct.pack('!Q', len(field)), field))
        return b''.join(out)


def _make_cookie(key, salt = None, tick = None, address = None, client_hello_bits = ('key', 'bytes', 'salt', 'bytes', 'tick', 'int', 'address', 'AddressFormat', 'client_hello_bits', 'bytes', 'return', 'bytes')):
    pass
# WARNING: Decompyle incomplete


def valid_cookie(key = None, cookie = None, address = None, client_hello_bits = ('key', 'bytes', 'cookie', 'bytes', 'address', 'AddressFormat', 'client_hello_bits', 'bytes', 'return', 'bool')):
    if len(cookie) > SALT_BYTES:
        salt = cookie[:SALT_BYTES]
        tick = _current_cookie_tick()
        cur_cookie = _make_cookie(key, salt, tick, address, client_hello_bits)
        old_cookie = _make_cookie(key, salt, max(tick - 1, 0), address, client_hello_bits)
        return hmac.compare_digest(cookie, cur_cookie) | hmac.compare_digest(cookie, old_cookie)


def challenge_for(key = None, address = None, epoch_seqno = None, client_hello_bits = ('key', 'bytes', 'address', 'AddressFormat', 'epoch_seqno', 'int', 'client_hello_bits', 'bytes', 'return', 'bytes')):
    salt = os.urandom(SALT_BYTES)
    tick = _current_cookie_tick()
    cookie = _make_cookie(key, salt, tick, address, client_hello_bits)
    body = ProtocolVersion.DTLS10 + bytes([
        len(cookie)]) + cookie
    hs = HandshakeFragment(msg_type = HandshakeType.hello_verify_request, msg_len = len(body), msg_seq = 0, frag_offset = 0, frag_len = len(body), frag = body)
    payload = encode_handshake_fragment(hs)
    packet = encode_record(Record(ContentType.handshake, ProtocolVersion.DTLS10, epoch_seqno, payload))
    return packet

_T = TypeVar('_T')

def _Queue():
    '''_Queue'''
    
    def __init__(self = None, incoming_packets_buffer = None):
        (self.s, self.r) = trio.open_memory_channel[_T](incoming_packets_buffer)


_Queue = <NODE:27>(_Queue, '_Queue', Generic[_T])

def _read_loop(read_fn = None):
    chunks = []
    
    try:
        chunk = read_fn(16384)
    except SSL.WantReadError:
        pass
    except:
        chunks.append(chunk)
        continue

    return b''.join(chunks)


async def handle_client_hello_untrusted(endpoint = None, address = None, packet = None):
    pass
# WARNING: Decompyle incomplete


async def dtls_receive_loop(endpoint_ref = None, sock = None):
    pass
# WARNING: Decompyle incomplete

DTLSChannelStatistics = <NODE:12>()

def DTLSChannel():
    '''DTLSChannel'''
    __doc__ = 'A DTLS connection.\n\n    This class has no public constructor – you get instances by calling\n    `DTLSEndpoint.serve` or `~DTLSEndpoint.connect`.\n\n    .. attribute:: endpoint\n\n       The `DTLSEndpoint` that this connection is using.\n\n    .. attribute:: peer_address\n\n       The IP/port of the remote peer that this connection is associated with.\n\n    '
    
    def __init__(self = None, endpoint = None, peer_address = None, ctx = ('endpoint', 'DTLSEndpoint', 'peer_address', 'AddressFormat', 'ctx', 'SSL.Context', 'return', 'None')):
        self.endpoint = endpoint
        self.peer_address = peer_address
        self._packets_dropped_in_trio = 0
        self._client_hello = None
        self._did_handshake = False
        self._ssl = SSL.Connection(ctx)
        self._handshake_mtu = 0
        self.set_ciphertext_mtu(best_guess_mtu(self.endpoint.socket))
        self._replaced = False
        self._closed = False
        self._q = _Queue[bytes](endpoint.incoming_packets_buffer)
        self._handshake_lock = trio.Lock()
        self._record_encoder = RecordEncoder()
        self._final_volley = []

    
    def _set_replaced(self = None):
        self._replaced = True
        self._q.s.close()

    
    def _check_replaced(self = None):
        if self._replaced:
            raise trio.BrokenResourceError('peer tore down this connection to start a new one')

    
    def close(self = None):
        """Close this connection.

        `DTLSChannel`\\s don't actually own any OS-level resources – the
        socket is owned by the `DTLSEndpoint`, not the individual connections. So
        you don't really *have* to call this. But it will interrupt any other tasks
        calling `receive` with a `ClosedResourceError`, and cause future attempts to use
        this connection to fail.

        You can also use this object as a synchronous or asynchronous context manager.

        """
        if self._closed:
            return None
        self._closed = None
        if self.endpoint._streams.get(self.peer_address) is self:
            del self.endpoint._streams[self.peer_address]
        self._q.r.close()

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        return self.close()

    
    async def aclose(self = None):
        """Close this connection, but asynchronously.

        This is included to satisfy the `trio.abc.Channel` contract. It's
        identical to `close`, but async.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_volley(self = None, volley_messages = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _resend_final_volley(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def do_handshake(self = None, *, initial_retransmit_timeout):
        """Perform the handshake.

        Calling this is optional – if you don't, then it will be automatically called
        the first time you call `send` or `receive`. But calling it explicitly can be
        useful in case you want to control the retransmit timeout, use a cancel scope to
        place an overall timeout on the handshake, or catch errors from the handshake
        specifically.

        It's safe to call this multiple times, or call it simultaneously from multiple
        tasks – the first call will perform the handshake, and the rest will be no-ops.

        Args:

          initial_retransmit_timeout (float): Since UDP is an unreliable protocol, it's
            possible that some of the packets we send during the handshake will get
            lost. To handle this, DTLS uses a timer to automatically retransmit
            handshake packets that don't receive a response. This lets you set the
            timeout we use to detect packet loss. Ideally, it should be set to ~1.5
            times the round-trip time to your peer, but 1 second is a reasonable
            default. There's `some useful guidance here
            <https://tlswg.org/dtls13-spec/draft-ietf-tls-dtls13.html#name-timer-values>`__.

            This is the *initial* timeout, because if packets keep being lost then Trio
            will automatically back off to longer values, to avoid overloading the
            network.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, data = None):
        '''Send a packet of data, securely.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def receive(self = None):
        """Fetch the next packet of data from this connection's peer, waiting if
        necessary.

        This is safe to call from multiple tasks simultaneously, in case you have some
        reason to do that. And more importantly, it's cancellation-safe, meaning that
        cancelling a call to `receive` will never cause a packet to be lost or corrupt
        the underlying connection.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def set_ciphertext_mtu(self = None, new_mtu = None):
        """Tells Trio the `largest amount of data that can be sent in a single packet to
        this peer <https://en.wikipedia.org/wiki/Maximum_transmission_unit>`__.

        Trio doesn't actually enforce this limit – if you pass a huge packet to `send`,
        then we'll dutifully encrypt it and attempt to send it. But calling this method
        does have two useful effects:

        - If called before the handshake is performed, then Trio will automatically
          fragment handshake messages to fit within the given MTU. It also might
          fragment them even smaller, if it detects signs of packet loss, so setting
          this should never be necessary to make a successful connection. But, the
          packet loss detection only happens after multiple timeouts have expired, so if
          you have reason to believe that a smaller MTU is required, then you can set
          this to skip those timeouts and establish the connection more quickly.

        - It changes the value returned from `get_cleartext_mtu`. So if you have some
          kind of estimate of the network-level MTU, then you can use this to figure out
          how much overhead DTLS will need for hashes/padding/etc., and how much space
          you have left for your application data.

        The MTU here is measuring the largest UDP *payload* you think can be sent, the
        amount of encrypted data that can be handed to the operating system in a single
        call to `send`. It should *not* include IP/UDP headers. Note that OS estimates
        of the MTU often are link-layer MTUs, so you have to subtract off 28 bytes on
        IPv4 and 48 bytes on IPv6 to get the ciphertext MTU.

        By default, Trio assumes an MTU of 1472 bytes on IPv4, and 1452 bytes on IPv6,
        which correspond to the common Ethernet MTU of 1500 bytes after accounting for
        IP/UDP overhead.

        """
        self._handshake_mtu = new_mtu
        self._ssl.set_ciphertext_mtu(new_mtu)

    
    def get_cleartext_mtu(self = None):
        '''Returns the largest number of bytes that you can pass in a single call to
        `send` while still fitting within the network-level MTU.

        See `set_ciphertext_mtu` for more details.

        '''
        if not self._did_handshake:
            raise trio.NeedHandshakeError
        return self._ssl.get_cleartext_mtu()

    
    def statistics(self = None):
        '''Returns a `DTLSChannelStatistics` object with statistics about this connection.'''
        return DTLSChannelStatistics(self._packets_dropped_in_trio)


DTLSChannel = <NODE:27>(DTLSChannel, 'DTLSChannel', trio.abc.Channel[bytes], metaclass = NoPublicConstructor)()
DTLSEndpoint = <NODE:12>()

def set_ssl_context_options(ctx = attrs.frozen):
    ctx.set_options(SSL.OP_NO_QUERY_MTU | SSL.OP_NO_RENEGOTIATION)
