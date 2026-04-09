# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: selector_events.pyc (Python 3.11)

'''Event loop using a selector and related classes.

A selector is a "notify-when-ready" multiplexer.  For a subclass which
also includes support for signal handling, see the unix_events sub-module.
'''
__all__ = ('BaseSelectorEventLoop',)
import collections
import errno
import functools
import selectors
import socket
import warnings
import weakref

try:
    import ssl
except ImportError:
    ssl = None

from  import base_events
from  import constants
from  import events
from  import futures
from  import protocols
from  import sslproto
from  import transports
from  import trsock
from log import logger

def _test_selector_event(selector, fd, event):
    
    try:
        key = selector.get_key(fd)
        return bool(key.events & event)
    except KeyError:
        return False



class BaseSelectorEventLoop(base_events.BaseEventLoop):
    pass
# WARNING: Decompyle incomplete


class _SelectorTransport(transports.Transport, transports._FlowControlMixin):
    pass
# WARNING: Decompyle incomplete


class _SelectorSocketTransport(_SelectorTransport):
    pass
# WARNING: Decompyle incomplete


class _SelectorDatagramTransport(_SelectorTransport):
    pass
# WARNING: Decompyle incomplete
