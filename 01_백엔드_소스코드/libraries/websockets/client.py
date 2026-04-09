# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from __future__ import annotations
import os
import random
import warnings
from collections.abc import Generator, Sequence
from typing import Any
from datastructures import Headers, MultipleValuesError
from exceptions import InvalidHandshake, InvalidHeader, InvalidHeaderValue, InvalidMessage, InvalidStatus, InvalidUpgrade, NegotiationError
from extensions import ClientExtensionFactory, Extension
from headers import build_authorization_basic, build_extension, build_host, build_subprotocol, parse_connection, parse_extension, parse_subprotocol, parse_upgrade
from http11 import Request, Response
from imports import lazy_import
from protocol import CLIENT, CONNECTING, OPEN, Protocol, State
from typing import ConnectionOption, ExtensionHeader, LoggerLike, Origin, Subprotocol, UpgradeProtocol
from uri import WebSocketURI
from utils import accept_key, generate_key
__all__ = [
    'ClientProtocol']

class ClientProtocol(Protocol):
    pass
# WARNING: Decompyle incomplete


class ClientConnection(ClientProtocol):
    pass
# WARNING: Decompyle incomplete

BACKOFF_INITIAL_DELAY = float(os.environ.get('WEBSOCKETS_BACKOFF_INITIAL_DELAY', '5'))
BACKOFF_MIN_DELAY = float(os.environ.get('WEBSOCKETS_BACKOFF_MIN_DELAY', '3.1'))
BACKOFF_MAX_DELAY = float(os.environ.get('WEBSOCKETS_BACKOFF_MAX_DELAY', '90.0'))
BACKOFF_FACTOR = float(os.environ.get('WEBSOCKETS_BACKOFF_FACTOR', '1.618'))

def backoff(initial_delay = None, min_delay = None, max_delay = None, factor = (BACKOFF_INITIAL_DELAY, BACKOFF_MIN_DELAY, BACKOFF_MAX_DELAY, BACKOFF_FACTOR)):
    '''
    Generate a series of backoff delays between reconnection attempts.

    Yields:
        How many seconds to wait before retrying to connect.

    '''
    pass
# WARNING: Decompyle incomplete

lazy_import(globals(), deprecated_aliases = {
    'WebSocketClientProtocol': '.legacy.client',
    'connect': '.legacy.client',
    'unix_connect': '.legacy.client' })
