# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: azure.pyc (Python 3.11)

from __future__ import annotations
import os
import inspect
from typing import Any, Union, Mapping, TypeVar, Callable, Awaitable, cast, overload
from typing_extensions import Self, override
import httpx
from _types import NOT_GIVEN, Omit, Query, Timeout, NotGiven
from _utils import is_given, is_mapping
from _client import OpenAI, AsyncOpenAI
from _compat import model_copy
from _models import FinalRequestOptions
from _streaming import Stream, AsyncStream
from _exceptions import OpenAIError
from _base_client import DEFAULT_MAX_RETRIES, BaseClient
_deployments_endpoints = set([
    '/completions',
    '/chat/completions',
    '/embeddings',
    '/audio/transcriptions',
    '/audio/translations',
    '/audio/speech',
    '/images/generations',
    '/images/edits'])
AzureADTokenProvider = Callable[([], str)]
AsyncAzureADTokenProvider = Callable[([], 'str | Awaitable[str]')]
_HttpxClientT = TypeVar('_HttpxClientT', bound = Union[(httpx.Client, httpx.AsyncClient)])
_DefaultStreamT = TypeVar('_DefaultStreamT', bound = Union[(Stream[Any], AsyncStream[Any])])
API_KEY_SENTINEL = ''.join([
    '<',
    'missing API key',
    '>'])

class MutuallyExclusiveAuthError(OpenAIError):
    pass
# WARNING: Decompyle incomplete


def BaseAzureClient():
    '''BaseAzureClient'''
    pass
# WARNING: Decompyle incomplete

BaseAzureClient = <NODE:27>(BaseAzureClient, 'BaseAzureClient', BaseClient[(_HttpxClientT, _DefaultStreamT)])

def AzureOpenAI():
    '''AzureOpenAI'''
    pass
# WARNING: Decompyle incomplete

AzureOpenAI = <NODE:27>(AzureOpenAI, 'AzureOpenAI', BaseAzureClient[(httpx.Client, Stream[Any])], OpenAI)

def AsyncAzureOpenAI():
    '''AsyncAzureOpenAI'''
    pass
# WARNING: Decompyle incomplete

AsyncAzureOpenAI = <NODE:27>(AsyncAzureOpenAI, 'AsyncAzureOpenAI', BaseAzureClient[(httpx.AsyncClient, AsyncStream[Any])], AsyncOpenAI)
