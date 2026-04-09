# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client.pyc (Python 3.11)

from __future__ import annotations
import datetime
import enum
import logging
import time
import typing
import warnings
from contextlib import asynccontextmanager, contextmanager
from types import TracebackType
from __version__ import __version__
from _auth import Auth, BasicAuth, FunctionAuth
from _config import DEFAULT_LIMITS, DEFAULT_MAX_REDIRECTS, DEFAULT_TIMEOUT_CONFIG, Limits, Proxy, Timeout
from _decoders import SUPPORTED_DECODERS
from _exceptions import InvalidURL, RemoteProtocolError, TooManyRedirects, request_context
from _models import Cookies, Headers, Request, Response
from _status_codes import codes
from _transports.base import AsyncBaseTransport, BaseTransport
from _transports.default import AsyncHTTPTransport, HTTPTransport
from _types import AsyncByteStream, AuthTypes, CertTypes, CookieTypes, HeaderTypes, ProxyTypes, QueryParamTypes, RequestContent, RequestData, RequestExtensions, RequestFiles, SyncByteStream, TimeoutTypes
from _urls import URL, QueryParams
from _utils import URLPattern, get_environment_proxies
if typing.TYPE_CHECKING:
    import ssl
__all__ = [
    'USE_CLIENT_DEFAULT',
    'AsyncClient',
    'Client']
T = typing.TypeVar('T', bound = 'Client')
U = typing.TypeVar('U', bound = 'AsyncClient')

def _is_https_redirect(url = None, location = None):
