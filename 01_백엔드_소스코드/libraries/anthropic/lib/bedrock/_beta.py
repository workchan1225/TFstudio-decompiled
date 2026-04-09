# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta.pyc (Python 3.11)

from __future__ import annotations
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _beta_messages import Messages, AsyncMessages, MessagesWithRawResponse, AsyncMessagesWithRawResponse, MessagesWithStreamingResponse, AsyncMessagesWithStreamingResponse
__all__ = [
    'Beta',
    'AsyncBeta']

class Beta(SyncAPIResource):
    messages = (lambda self = None: Messages(self._client))()
    with_raw_response = (lambda self = None: BetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: BetaWithStreamingResponse(self))()


class AsyncBeta(AsyncAPIResource):
    messages = (lambda self = None: AsyncMessages(self._client))()
    with_raw_response = (lambda self = None: AsyncBetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncBetaWithStreamingResponse(self))()


class BetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    messages = (lambda self = None: MessagesWithRawResponse(self._beta.messages))()


class AsyncBetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    messages = (lambda self = None: AsyncMessagesWithRawResponse(self._beta.messages))()


class BetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    messages = (lambda self = None: MessagesWithStreamingResponse(self._beta.messages))()


class AsyncBetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    messages = (lambda self = None: AsyncMessagesWithStreamingResponse(self._beta.messages))()
