# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: impl.pyc (Python 3.11)

'''Base implementation.'''
import asyncio
import collections
import contextlib
import functools
import itertools
import socket
from typing import List, Optional, Sequence, Set, Union
from  import _staggered
from types import AddrInfoType, SocketFactoryType

async def start_connection(addr_infos = None, *, local_addr_infos, happy_eyeballs_delay, interleave, loop, socket_factory):
    '''
    Connect to a TCP server.

    Create a socket connection to a specified destination.  The
    destination is specified as a list of AddrInfoType tuples as
    returned from getaddrinfo().

    The arguments are, in order:

    * ``family``: the address family, e.g. ``socket.AF_INET`` or
        ``socket.AF_INET6``.
    * ``type``: the socket type, e.g. ``socket.SOCK_STREAM`` or
        ``socket.SOCK_DGRAM``.
    * ``proto``: the protocol, e.g. ``socket.IPPROTO_TCP`` or
        ``socket.IPPROTO_UDP``.
    * ``canonname``: the canonical name of the address, e.g.
        ``"www.python.org"``.
    * ``sockaddr``: the socket address

    This method is a coroutine which will try to establish the connection
    in the background. When successful, the coroutine returns a
    socket.

    The expected use case is to use this method in conjunction with
    loop.create_connection() to establish a connection to a server::

            socket = await start_connection(addr_infos)
            transport, protocol = await loop.create_connection(
                MyProtocol, sock=socket, ...)
    '''
    pass
# WARNING: Decompyle incomplete


async def _connect_sock(loop, exceptions = None, addr_info = None, local_addr_infos = None, open_sockets = (None, None, None), socket_factory = ('loop', asyncio.AbstractEventLoop, 'exceptions', List[List[Union[(OSError, RuntimeError)]]], 'addr_info', AddrInfoType, 'local_addr_infos', Optional[Sequence[AddrInfoType]], 'open_sockets', Optional[Set[socket.socket]], 'socket_factory', Optional[SocketFactoryType], 'return', socket.socket)):
    '''
    Create, bind and connect one socket.

    If open_sockets is passed, add the socket to the set of open sockets.
    Any failure caught here will remove the socket from the set and close it.

    Callers can use this set to close any sockets that are not the winner
    of all staggered tasks in the result there are runner up sockets aka
    multiple winners.
    '''
    pass
# WARNING: Decompyle incomplete


def _interleave_addrinfos(addrinfos = None, first_address_family_count = None):
    '''Interleave list of addrinfo tuples by family.'''
    addrinfos_by_family = collections.OrderedDict()
    for addr in addrinfos:
        family = addr[0]
        if family not in addrinfos_by_family:
            addrinfos_by_family[family] = []
        addrinfos_by_family[family].append(addr)
        addrinfos_lists = list(addrinfos_by_family.values())
        reordered = []
        if first_address_family_count > 1:
            reordered.extend(addrinfos_lists[0][:first_address_family_count - 1])
            del addrinfos_lists[0][:first_address_family_count - 1]
# WARNING: Decompyle incomplete
