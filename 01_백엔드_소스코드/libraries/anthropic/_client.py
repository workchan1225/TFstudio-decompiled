# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override
import httpx
from  import _constants, _exceptions
from _qs import Querystring
from _types import Omit, Headers, Timeout, NotGiven, Transport, ProxiesTypes, RequestOptions, not_given
from _utils import is_given, get_async_library
from _compat import cached_property
from _version import __version__
from _streaming import Stream, AsyncStream
from _exceptions import APIStatusError
from _base_client import DEFAULT_MAX_RETRIES, SyncAPIClient, AsyncAPIClient
if TYPE_CHECKING:
    from resources import beta, models, messages, completions
    from resources.models import Models, AsyncModels
    from resources.beta.beta import Beta, AsyncBeta
    from resources.completions import Completions, AsyncCompletions
    from resources.messages.messages import Messages, AsyncMessages
__all__ = [
    'Timeout',
    'Transport',
    'ProxiesTypes',
    'RequestOptions',
    'Anthropic',
    'AsyncAnthropic',
    'Client',
    'AsyncClient']

class Anthropic(SyncAPIClient):
    pass
# WARNING: Decompyle incomplete


class AsyncAnthropic(AsyncAPIClient):
    pass
# WARNING: Decompyle incomplete


class AnthropicWithRawResponse:
    _client: 'Anthropic' = 'AnthropicWithRawResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: CompletionsWithRawResponse = CompletionsWithRawResponseimport resources.completionsCompletionsWithRawResponse(self._client.completions))()
    messages = (lambda self = None: MessagesWithRawResponse = MessagesWithRawResponseimport resources.messagesMessagesWithRawResponse(self._client.messages))()
    models = (lambda self = None: ModelsWithRawResponse = ModelsWithRawResponseimport resources.modelsModelsWithRawResponse(self._client.models))()
    beta = (lambda self = None: BetaWithRawResponse = BetaWithRawResponseimport resources.betaBetaWithRawResponse(self._client.beta))()


class AsyncAnthropicWithRawResponse:
    _client: 'AsyncAnthropic' = 'AsyncAnthropicWithRawResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: AsyncCompletionsWithRawResponse = AsyncCompletionsWithRawResponseimport resources.completionsAsyncCompletionsWithRawResponse(self._client.completions))()
    messages = (lambda self = None: AsyncMessagesWithRawResponse = AsyncMessagesWithRawResponseimport resources.messagesAsyncMessagesWithRawResponse(self._client.messages))()
    models = (lambda self = None: AsyncModelsWithRawResponse = AsyncModelsWithRawResponseimport resources.modelsAsyncModelsWithRawResponse(self._client.models))()
    beta = (lambda self = None: AsyncBetaWithRawResponse = AsyncBetaWithRawResponseimport resources.betaAsyncBetaWithRawResponse(self._client.beta))()


class AnthropicWithStreamedResponse:
    _client: 'Anthropic' = 'AnthropicWithStreamedResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: CompletionsWithStreamingResponse = CompletionsWithStreamingResponseimport resources.completionsCompletionsWithStreamingResponse(self._client.completions))()
    messages = (lambda self = None: MessagesWithStreamingResponse = MessagesWithStreamingResponseimport resources.messagesMessagesWithStreamingResponse(self._client.messages))()
    models = (lambda self = None: ModelsWithStreamingResponse = ModelsWithStreamingResponseimport resources.modelsModelsWithStreamingResponse(self._client.models))()
    beta = (lambda self = None: BetaWithStreamingResponse = BetaWithStreamingResponseimport resources.betaBetaWithStreamingResponse(self._client.beta))()


class AsyncAnthropicWithStreamedResponse:
    _client: 'AsyncAnthropic' = 'AsyncAnthropicWithStreamedResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: AsyncCompletionsWithStreamingResponse = AsyncCompletionsWithStreamingResponseimport resources.completionsAsyncCompletionsWithStreamingResponse(self._client.completions))()
    messages = (lambda self = None: AsyncMessagesWithStreamingResponse = AsyncMessagesWithStreamingResponseimport resources.messagesAsyncMessagesWithStreamingResponse(self._client.messages))()
    models = (lambda self = None: AsyncModelsWithStreamingResponse = AsyncModelsWithStreamingResponseimport resources.modelsAsyncModelsWithStreamingResponse(self._client.models))()
    beta = (lambda self = None: AsyncBetaWithStreamingResponse = AsyncBetaWithStreamingResponseimport resources.betaAsyncBetaWithStreamingResponse(self._client.beta))()

Client = Anthropic
AsyncClient = AsyncAnthropic
