# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat.pyc (Python 3.11)

from __future__ import annotations
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from completions.completions import Completions, AsyncCompletions, CompletionsWithRawResponse, AsyncCompletionsWithRawResponse, CompletionsWithStreamingResponse, AsyncCompletionsWithStreamingResponse
__all__ = [
    'Chat',
    'AsyncChat']

class Chat(SyncAPIResource):
    completions = (lambda self = None: Completions(self._client))()
    with_raw_response = (lambda self = None: ChatWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ChatWithStreamingResponse(self))()


class AsyncChat(AsyncAPIResource):
    completions = (lambda self = None: AsyncCompletions(self._client))()
    with_raw_response = (lambda self = None: AsyncChatWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncChatWithStreamingResponse(self))()


class ChatWithRawResponse:
    
    def __init__(self = None, chat = None):
        self._chat = chat

    completions = (lambda self = None: CompletionsWithRawResponse(self._chat.completions))()


class AsyncChatWithRawResponse:
    
    def __init__(self = None, chat = None):
        self._chat = chat

    completions = (lambda self = None: AsyncCompletionsWithRawResponse(self._chat.completions))()


class ChatWithStreamingResponse:
    
    def __init__(self = None, chat = None):
        self._chat = chat

    completions = (lambda self = None: CompletionsWithStreamingResponse(self._chat.completions))()


class AsyncChatWithStreamingResponse:
    
    def __init__(self = None, chat = None):
        self._chat = chat

    completions = (lambda self = None: AsyncCompletionsWithStreamingResponse(self._chat.completions))()
