# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_open_tcp_stream.pyc (Python 3.11)

from __future__ import annotations
import sys
from contextlib import contextmanager, suppress
from typing import TYPE_CHECKING, Any
import trio
from trio.socket import SOCK_STREAM, SocketType, getaddrinfo, socket
if TYPE_CHECKING:
    from collections.abc import Generator, MutableSequence
    from socket import AddressFamily, SocketKind
    from trio._socket import AddressFormat
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup, ExceptionGroup
DEFAULT_DELAY = 0.25
close_all = (lambda : pass# WARNING: Decompyle incomplete
)()

def reorder_for_rfc_6555_section_5_4(targets = None):
    for i in range(1, len(targets)):
        if targets[i][0] != targets[0][0]:
            if i != 1:
                targets.insert(1, targets.pop(i))
            return None
        return None


def format_host_port(host = None, port = None):
    host = host.decode('ascii') if isinstance(host, bytes) else host
    if ':' in host:
        return f'''[{host}]:{port}'''
    return f'''{None}:{port}'''


async def open_tcp_stream(host = None, port = None, *, happy_eyeballs_delay, local_address):
    '''Connect to the given host and port over TCP.

    If the given ``host`` has multiple IP addresses associated with it, then
    we have a problem: which one do we use?

    One approach would be to attempt to connect to the first one, and then if
    that fails, attempt to connect to the second one ... until we\'ve tried all
    of them. But the problem with this is that if the first IP address is
    unreachable (for example, because it\'s an IPv6 address and our network
    discards IPv6 packets), then we might end up waiting tens of seconds for
    the first connection attempt to timeout before we try the second address.

    Another approach would be to attempt to connect to all of the addresses at
    the same time, in parallel, and then use whichever connection succeeds
    first, abandoning the others. This would be fast, but create a lot of
    unnecessary load on the network and the remote server.

    This function strikes a balance between these two extremes: it works its
    way through the available addresses one at a time, like the first
    approach; but, if ``happy_eyeballs_delay`` seconds have passed and it\'s
    still waiting for an attempt to succeed or fail, then it gets impatient
    and starts the next connection attempt in parallel. As soon as any one
    connection attempt succeeds, all the other attempts are cancelled. This
    avoids unnecessary load because most connections will succeed after just
    one or two attempts, but if one of the addresses is unreachable then it
    doesn\'t slow us down too much.

    This is known as a "happy eyeballs" algorithm, and our particular variant
    is modelled after how Chrome connects to webservers; see `RFC 6555
    <https://tools.ietf.org/html/rfc6555>`__ for more details.

    Args:
      host (str or bytes): The host to connect to. Can be an IPv4 address,
          IPv6 address, or a hostname.

      port (int): The port to connect to.

      happy_eyeballs_delay (float or None): How many seconds to wait for each
          connection attempt to succeed or fail before getting impatient and
          starting another one in parallel. Set to `None` if you want
          to limit to only one connection attempt at a time (like
          :func:`socket.create_connection`). Default: 0.25 (250 ms).

      local_address (None or str): The local IP address or hostname to use as
          the source for outgoing connections. If ``None``, we let the OS pick
          the source IP.

          This is useful in some exotic networking configurations where your
          host has multiple IP addresses, and you want to force the use of a
          specific one.

          Note that if you pass an IPv4 ``local_address``, then you won\'t be
          able to connect to IPv6 hosts, and vice-versa. If you want to take
          advantage of this to force the use of IPv4 or IPv6 without
          specifying an exact source address, you can use the IPv4 wildcard
          address ``local_address="0.0.0.0"``, or the IPv6 wildcard address
          ``local_address="::"``.

    Returns:
      SocketStream: a :class:`~trio.abc.Stream` connected to the given server.

    Raises:
      OSError: if the connection fails.

    See also:
      open_ssl_over_tcp_stream

    '''
    pass
# WARNING: Decompyle incomplete
