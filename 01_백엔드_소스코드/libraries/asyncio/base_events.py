# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_events.pyc (Python 3.11)

'''Base implementation of event loop.

The event loop can be broken up into a multiplexer (the part
responsible for notifying us of I/O events) and the event loop proper,
which wraps a multiplexer with functionality for scheduling callbacks,
immediately or at a given time in the future.

Whenever a public API takes a callback, subsequent positional
arguments will be passed to the callback if/when it is called.  This
avoids the proliferation of trivial lambdas implementing closures.
Keyword arguments for the callback are not supported; this is a
conscious design decision, leaving the door open for keyword arguments
to modify the meaning of the API call itself.
'''
import collections
import collections.abc as collections
import concurrent.futures as concurrent
import errno
import functools
import heapq
import itertools
import os
import socket
import stat
import subprocess
import threading
import time
import traceback
import sys
import warnings
import weakref

try:
    import ssl
except ImportError:
    ssl = None

from  import constants
from  import coroutines
from  import events
from  import exceptions
from  import futures
from  import protocols
from  import sslproto
from  import staggered
from  import tasks
from  import transports
from  import trsock
from log import logger
__all__ = ('BaseEventLoop', 'Server')
_MIN_SCHEDULED_TIMER_HANDLES = 100
_MIN_CANCELLED_TIMER_HANDLES_FRACTION = 0.5
_HAS_IPv6 = hasattr(socket, 'AF_INET6')
MAXIMUM_SELECT_TIMEOUT = 86400

def _format_handle(handle):
    cb = handle._callback
    if isinstance(getattr(cb, '__self__', None), tasks.Task):
        return repr(cb.__self__)
    return None(handle)


def _format_pipe(fd):
    if fd == subprocess.PIPE:
        return '<pipe>'
    if None == subprocess.STDOUT:
        return '<stdout>'
    return None(fd)


def _set_reuseport(sock):
    if not hasattr(socket, 'SO_REUSEPORT'):
        raise ValueError('reuse_port not supported by socket module')
    
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        return None
    except OSError:
        raise ValueError('reuse_port not supported by socket module, SO_REUSEPORT defined but not implemented.')



def _ipaddr_info(host, port, family, type, proto, flowinfo, scopeid = (0, 0)):
    if not hasattr(socket, 'inet_pton'):
        return None
# WARNING: Decompyle incomplete


def _interleave_addrinfos(addrinfos, first_address_family_count = (1,)):
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


def _run_until_complete_cb(fut):
