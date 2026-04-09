# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import annotations
import base64
import binascii
import email.utils as email
import http
import re
import warnings
from collections.abc import Generator, Sequence
from typing import Any, Callable, cast
from datastructures import Headers, MultipleValuesError
from exceptions import InvalidHandshake, InvalidHeader, InvalidHeaderValue, InvalidMessage, InvalidOrigin, InvalidUpgrade, NegotiationError
from extensions import Extension, ServerExtensionFactory
from headers import build_extension, parse_connection, parse_extension, parse_subprotocol, parse_upgrade
from http11 import Request, Response
from imports import lazy_import
from protocol import CONNECTING, OPEN, SERVER, Protocol, State
from typing import ConnectionOption, ExtensionHeader, LoggerLike, Origin, StatusLike, Subprotocol, UpgradeProtocol
from utils import accept_key
__all__ = [
    'ServerProtocol']

class ServerProtocol(Protocol):
    pass
# WARNING: Decompyle incomplete


class ServerConnection(ServerProtocol):
    pass
# WARNING: Decompyle incomplete

lazy_import(globals(), deprecated_aliases = {
    'WebSocketServer': '.legacy.server',
    'WebSocketServerProtocol': '.legacy.server',
    'broadcast': '.legacy.server',
    'serve': '.legacy.server',
    'unix_serve': '.legacy.server' })
