# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: foundry.pyc (Python 3.11)

from __future__ import annotations
import os
import inspect
from typing import Any, Union, Mapping, TypeVar, Callable, Awaitable, cast, overload
from functools import cached_property
from typing_extensions import Self, override
import httpx
from _types import NOT_GIVEN, Omit, Timeout, NotGiven
from _utils import is_given
from _client import Anthropic, AsyncAnthropic
from _compat import model_copy
from _models import FinalRequestOptions
from _streaming import Stream, AsyncStream
from _exceptions import AnthropicError
from _base_client import DEFAULT_MAX_RETRIES, BaseClient
from resources.beta import Beta, AsyncBeta
from resources.messages import Messages, AsyncMessages
from resources.beta.messages import Messages as BetaMessages, AsyncMessages as AsyncBetaMessages
AzureADTokenProvider = Callable[([], str)]
AsyncAzureADTokenProvider = Callable[([], 'str | Awaitable[str]')]
_HttpxClientT = TypeVar('_HttpxClientT', bound = Union[(httpx.Client, httpx.AsyncClient)])
_DefaultStreamT = TypeVar('_DefaultStreamT', bound = Union[(Stream[Any], AsyncStream[Any])])

class MutuallyExclusiveAuthError(AnthropicError):
    pass
# WARNING: Decompyle incomplete


def BaseFoundryClient():
    '''BaseFoundryClient'''
    pass

BaseFoundryClient = <NODE:27>(BaseFoundryClient, 'BaseFoundryClient', BaseClient[(_HttpxClientT, _DefaultStreamT)])

class MessagesFoundry(Messages):
    batches = (lambda self = None: pass)()()


class BetaFoundryMessages(BetaMessages):
    batches = (lambda self = None: pass)()()


class BetaFoundry(Beta):
    messages = (lambda self = None: BetaFoundryMessages(self._client))()()


class AsyncMessagesFoundry(AsyncMessages):
    batches = (lambda self = None: pass)()()


class AsyncBetaFoundryMessages(AsyncBetaMessages):
    batches = (lambda self = None: pass)()()


class AsyncBetaFoundry(AsyncBeta):
    messages = (lambda self = None: AsyncBetaFoundryMessages(self._client))()()


def AnthropicFoundry():
    '''AnthropicFoundry'''
    pass
# WARNING: Decompyle incomplete

AnthropicFoundry = <NODE:27>(AnthropicFoundry, 'AnthropicFoundry', BaseFoundryClient[(httpx.Client, Stream[Any])], Anthropic)

def AsyncAnthropicFoundry():
    '''AsyncAnthropicFoundry'''
    pass
# WARNING: Decompyle incomplete

AsyncAnthropicFoundry = <NODE:27>(AsyncAnthropicFoundry, 'AsyncAnthropicFoundry', BaseFoundryClient[(httpx.AsyncClient, AsyncStream[Any])], AsyncAnthropic)
