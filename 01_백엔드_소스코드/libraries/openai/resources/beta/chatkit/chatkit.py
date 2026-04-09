# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit.pyc (Python 3.11)

from __future__ import annotations
from threads import Threads, AsyncThreads, ThreadsWithRawResponse, AsyncThreadsWithRawResponse, ThreadsWithStreamingResponse, AsyncThreadsWithStreamingResponse
from sessions import Sessions, AsyncSessions, SessionsWithRawResponse, AsyncSessionsWithRawResponse, SessionsWithStreamingResponse, AsyncSessionsWithStreamingResponse
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
__all__ = [
    'ChatKit',
    'AsyncChatKit']

class ChatKit(SyncAPIResource):
    sessions = (lambda self = None: Sessions(self._client))()
    threads = (lambda self = None: Threads(self._client))()
    with_raw_response = (lambda self = None: ChatKitWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ChatKitWithStreamingResponse(self))()


class AsyncChatKit(AsyncAPIResource):
    sessions = (lambda self = None: AsyncSessions(self._client))()
    threads = (lambda self = None: AsyncThreads(self._client))()
    with_raw_response = (lambda self = None: AsyncChatKitWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncChatKitWithStreamingResponse(self))()


class ChatKitWithRawResponse:
    
    def __init__(self = None, chatkit = None):
        self._chatkit = chatkit

    sessions = (lambda self = None: SessionsWithRawResponse(self._chatkit.sessions))()
    threads = (lambda self = None: ThreadsWithRawResponse(self._chatkit.threads))()


class AsyncChatKitWithRawResponse:
    
    def __init__(self = None, chatkit = None):
        self._chatkit = chatkit

    sessions = (lambda self = None: AsyncSessionsWithRawResponse(self._chatkit.sessions))()
    threads = (lambda self = None: AsyncThreadsWithRawResponse(self._chatkit.threads))()


class ChatKitWithStreamingResponse:
    
    def __init__(self = None, chatkit = None):
        self._chatkit = chatkit

    sessions = (lambda self = None: SessionsWithStreamingResponse(self._chatkit.sessions))()
    threads = (lambda self = None: ThreadsWithStreamingResponse(self._chatkit.threads))()


class AsyncChatKitWithStreamingResponse:
    
    def __init__(self = None, chatkit = None):
        self._chatkit = chatkit

    sessions = (lambda self = None: AsyncSessionsWithStreamingResponse(self._chatkit.sessions))()
    threads = (lambda self = None: AsyncThreadsWithStreamingResponse(self._chatkit.threads))()
