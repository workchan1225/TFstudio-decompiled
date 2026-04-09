# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta.pyc (Python 3.11)

from __future__ import annotations
from _compat import cached_property
from assistants import Assistants, AsyncAssistants, AssistantsWithRawResponse, AsyncAssistantsWithRawResponse, AssistantsWithStreamingResponse, AsyncAssistantsWithStreamingResponse
from _resource import SyncAPIResource, AsyncAPIResource
from chatkit.chatkit import ChatKit, AsyncChatKit, ChatKitWithRawResponse, AsyncChatKitWithRawResponse, ChatKitWithStreamingResponse, AsyncChatKitWithStreamingResponse
from threads.threads import Threads, AsyncThreads, ThreadsWithRawResponse, AsyncThreadsWithRawResponse, ThreadsWithStreamingResponse, AsyncThreadsWithStreamingResponse
from resources.chat import Chat, AsyncChat
from realtime.realtime import Realtime, AsyncRealtime
__all__ = [
    'Beta',
    'AsyncBeta']

class Beta(SyncAPIResource):
    chat = (lambda self = None: Chat(self._client))()
    realtime = (lambda self = None: Realtime(self._client))()
    chatkit = (lambda self = None: ChatKit(self._client))()
    assistants = (lambda self = None: Assistants(self._client))()
    threads = (lambda self = None: Threads(self._client))()
    with_raw_response = (lambda self = None: BetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: BetaWithStreamingResponse(self))()


class AsyncBeta(AsyncAPIResource):
    chat = (lambda self = None: AsyncChat(self._client))()
    realtime = (lambda self = None: AsyncRealtime(self._client))()
    chatkit = (lambda self = None: AsyncChatKit(self._client))()
    assistants = (lambda self = None: AsyncAssistants(self._client))()
    threads = (lambda self = None: AsyncThreads(self._client))()
    with_raw_response = (lambda self = None: AsyncBetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncBetaWithStreamingResponse(self))()


class BetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    chatkit = (lambda self = None: ChatKitWithRawResponse(self._beta.chatkit))()
    assistants = (lambda self = None: AssistantsWithRawResponse(self._beta.assistants))()
    threads = (lambda self = None: ThreadsWithRawResponse(self._beta.threads))()


class AsyncBetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    chatkit = (lambda self = None: AsyncChatKitWithRawResponse(self._beta.chatkit))()
    assistants = (lambda self = None: AsyncAssistantsWithRawResponse(self._beta.assistants))()
    threads = (lambda self = None: AsyncThreadsWithRawResponse(self._beta.threads))()


class BetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    chatkit = (lambda self = None: ChatKitWithStreamingResponse(self._beta.chatkit))()
    assistants = (lambda self = None: AssistantsWithStreamingResponse(self._beta.assistants))()
    threads = (lambda self = None: ThreadsWithStreamingResponse(self._beta.threads))()


class AsyncBetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    chatkit = (lambda self = None: AsyncChatKitWithStreamingResponse(self._beta.chatkit))()
    assistants = (lambda self = None: AsyncAssistantsWithStreamingResponse(self._beta.assistants))()
    threads = (lambda self = None: AsyncThreadsWithStreamingResponse(self._beta.threads))()
