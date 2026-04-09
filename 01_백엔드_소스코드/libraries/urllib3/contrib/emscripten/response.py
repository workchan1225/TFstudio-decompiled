# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import annotations
import json as _json
import logging
import typing
from contextlib import contextmanager
from dataclasses import dataclass
from http.client import HTTPException
from io import BytesIO, IOBase
from exceptions import InvalidHeader, TimeoutError
from response import BaseHTTPResponse
from util.retry import Retry
from request import EmscriptenRequest
if typing.TYPE_CHECKING:
    from _base_connection import BaseHTTPConnection, BaseHTTPSConnection
log = logging.getLogger(__name__)
EmscriptenResponse = <NODE:12>()

class EmscriptenHttpResponseWrapper(BaseHTTPResponse):
    pass
# WARNING: Decompyle incomplete
