# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_messages.pyc (Python 3.11)

from __future__ import annotations
from  import _legacy_response
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from resources.beta import Messages as FirstPartyMessagesAPI, AsyncMessages as FirstPartyAsyncMessagesAPI
__all__ = [
    'Messages',
    'AsyncMessages']

class Messages(SyncAPIResource):
    create = FirstPartyMessagesAPI.create
    stream = FirstPartyMessagesAPI.stream
    count_tokens = FirstPartyMessagesAPI.count_tokens
    with_raw_response = (lambda self = None: MessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: MessagesWithStreamingResponse(self))()


class AsyncMessages(AsyncAPIResource):
    create = FirstPartyAsyncMessagesAPI.create
    stream = FirstPartyAsyncMessagesAPI.stream
    count_tokens = FirstPartyAsyncMessagesAPI.count_tokens
    with_raw_response = (lambda self = None: AsyncMessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncMessagesWithStreamingResponse(self))()


class MessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.to_raw_response_wrapper(messages.create)



class AsyncMessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.async_to_raw_response_wrapper(messages.create)



class MessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = to_streamed_response_wrapper(messages.create)



class AsyncMessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = async_to_streamed_response_wrapper(messages.create)
