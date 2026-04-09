# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_client.pyc (Python 3.11)

from __future__ import annotations
import sys
import json
import time
import uuid
import email
import asyncio
import inspect
import logging
import platform
import email.utils as email
from types import TracebackType
from random import random
from typing import TYPE_CHECKING, Any, Dict, Type, Union, Generic, Mapping, TypeVar, Iterable, Iterator, Optional, Generator, AsyncIterator, cast, overload
from typing_extensions import Literal, override, get_origin
import anyio
import httpx
import distro
import pydantic
from httpx import URL
from pydantic import PrivateAttr
from  import _exceptions
from _qs import Querystring
from _files import to_httpx_files, async_to_httpx_files
from _types import Body, Omit, Query, Headers, Timeout, NotGiven, ResponseT, AnyMapping, PostParser, RequestFiles, HttpxSendArgs, RequestOptions, HttpxRequestFiles, ModelBuilderProtocol, not_given
from _utils import SensitiveHeadersFilter, is_dict, is_list, asyncify, is_given, lru_cache, is_mapping
from _compat import PYDANTIC_V1, model_copy, model_dump
from _models import GenericModel, FinalRequestOptions, validate_type, construct_type
from _response import APIResponse, BaseAPIResponse, AsyncAPIResponse, extract_response_type
from _constants import DEFAULT_TIMEOUT, MAX_RETRY_DELAY, DEFAULT_MAX_RETRIES, INITIAL_RETRY_DELAY, RAW_RESPONSE_HEADER, OVERRIDE_CAST_TO_HEADER, DEFAULT_CONNECTION_LIMITS
from _streaming import Stream, SSEDecoder, AsyncStream, SSEBytesDecoder
from _exceptions import APIStatusError, APITimeoutError, APIConnectionError, APIResponseValidationError
from _legacy_response import LegacyAPIResponse
log: 'logging.Logger' = logging.getLogger(__name__)
log.addFilter(SensitiveHeadersFilter())
SyncPageT = TypeVar('SyncPageT', bound = 'BaseSyncPage[Any]')
AsyncPageT = TypeVar('AsyncPageT', bound = 'BaseAsyncPage[Any]')
_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant = True)
_StreamT = TypeVar('_StreamT', bound = Stream[Any])
_AsyncStreamT = TypeVar('_AsyncStreamT', bound = AsyncStream[Any])

class SyncHttpxClientWrapper(DefaultHttpxClient):
    
    def __del__(self = None):
        if self.is_closed:
            return None
        
        try:
            self.close()
            return None
        except Exception:
            return None




def SyncAPIClient():
    '''SyncAPIClient'''
    pass
# WARNING: Decompyle incomplete

SyncAPIClient = <NODE:27>(SyncAPIClient, 'SyncAPIClient', BaseClient[(httpx.Client, Stream[Any])])

class _DefaultAsyncHttpxClient(httpx.AsyncClient):
    pass
# WARNING: Decompyle incomplete


try:
    import httpx_aiohttp
    
    class _DefaultAioHttpClient(httpx_aiohttp.HttpxAiohttpClient):
        pass
    # WARNING: Decompyle incomplete

except ImportError:
    
    class _DefaultAioHttpClient(httpx.AsyncClient):
        
        def __init__(self = None, **_kwargs):
            raise RuntimeError('To use the aiohttp client you must have installed the package with the `aiohttp` extra')




class AsyncHttpxClientWrapper(DefaultAsyncHttpxClient):
    
    def __del__(self = None):
        if self.is_closed:
            return None
        
        try:
            asyncio.get_running_loop().create_task(self.aclose())
            return None
        except Exception:
            return None




def AsyncAPIClient():
    '''AsyncAPIClient'''
    pass
# WARNING: Decompyle incomplete

AsyncAPIClient = <NODE:27>(AsyncAPIClient, 'AsyncAPIClient', BaseClient[(httpx.AsyncClient, AsyncStream[Any])])

def make_request_options(*, query, extra_headers, extra_query, extra_body, idempotency_key, timeout, post_parser):
    '''Create a dict of type RequestOptions without keys of NotGiven values.'''
    options = { }
# WARNING: Decompyle incomplete


def ForceMultipartDict():
    '''ForceMultipartDict'''
    
    def __bool__(self = None):
        return True


ForceMultipartDict = <NODE:27>(ForceMultipartDict, 'ForceMultipartDict', Dict[(str, None)])

class OtherPlatform:
    
    def __init__(self = None, name = None):
        self.name = name

    __str__ = (lambda self = None: f'''Other:{self.name}''')()

Platform = Union[(OtherPlatform, Literal[('MacOS', 'Linux', 'Windows', 'FreeBSD', 'OpenBSD', 'iOS', 'Android', 'Unknown')])]

def get_platform():
    
    try:
        system = platform.system().lower()
        platform_name = platform.platform().lower()
    except Exception:
        return 'Unknown'

    if 'iphone' in platform_name or 'ipad' in platform_name:
        return 'iOS'
    if None == 'darwin':
        return 'MacOS'
    if None == 'windows':
        return 'Windows'
    if None in platform_name:
        return 'Android'
    if None == 'linux':
        distro_id = distro.id()
        if distro_id == 'freebsd':
            return 'FreeBSD'
        if None == 'openbsd':
            return 'OpenBSD'
        return None
    if None:
        return OtherPlatform(platform_name)

platform_headers = (lambda version = None, *, platform: if not platform:
pass{
'X-Stainless-Lang': 'python',
'X-Stainless-Package-Version': version,
'X-Stainless-OS': str(get_platform()),
'X-Stainless-Arch': str(get_architecture()),
'X-Stainless-Runtime': get_python_runtime(),
'X-Stainless-Runtime-Version': get_python_version() })()

class OtherArch:
    
    def __init__(self = None, name = None):
        self.name = name

    __str__ = (lambda self = None: f'''other:{self.name}''')()

Arch = Union[(OtherArch, Literal[('x32', 'x64', 'arm', 'arm64', 'unknown')])]

def get_python_runtime():
    
    try:
        return platform.python_implementation()
    except Exception:
        return 'unknown'



def get_python_version():
    
    try:
        return platform.python_version()
    except Exception:
        return 'unknown'



def get_architecture():
    
    try:
        machine = platform.machine().lower()
    except Exception:
        return 'unknown'

    if machine in ('arm64', 'aarch64'):
        return 'arm64'
    if None == 'arm':
        return 'arm'
    if None == 'x86_64':
        return 'x64'
    if None.maxsize <= 0x100000000:
        return 'x32'
    if None:
        return OtherArch(machine)


def _merge_mappings(obj1 = None, obj2 = None):
    '''Merge two mappings of the same type, removing any values that are instances of `Omit`.

    In cases with duplicate keys the second mapping takes precedence.
    '''
    pass
# WARNING: Decompyle incomplete
