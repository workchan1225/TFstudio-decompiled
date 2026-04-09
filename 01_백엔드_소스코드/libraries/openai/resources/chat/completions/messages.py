# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.chat.completions import message_list_params
from types.chat.chat_completion_store_message import ChatCompletionStoreMessage
__all__ = [
    'Messages',
    'AsyncMessages']

class Messages(SyncAPIResource):
    with_raw_response = (lambda self = None: MessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: MessagesWithStreamingResponse(self))()
    
    def list(self = None, completion_id = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Get the messages in a stored chat completion.

        Only Chat Completions that have
        been created with the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last message from the previous pagination request.

          limit: Number of messages to retrieve.

          order: Sort order for messages by timestamp. Use `asc` for ascending order or `desc`
              for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not completion_id:
            raise ValueError(f'''Expected a non-empty value for `completion_id` but received {completion_id!r}''')
        return self._get_api_list(f'''/chat/completions/{completion_id}/messages''', page = SyncCursorPage[ChatCompletionStoreMessage], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, message_list_params.MessageListParams)), model = ChatCompletionStoreMessage)



class AsyncMessages(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncMessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncMessagesWithStreamingResponse(self))()
    
    def list(self = None, completion_id = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Get the messages in a stored chat completion.

        Only Chat Completions that have
        been created with the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last message from the previous pagination request.

          limit: Number of messages to retrieve.

          order: Sort order for messages by timestamp. Use `asc` for ascending order or `desc`
              for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not completion_id:
            raise ValueError(f'''Expected a non-empty value for `completion_id` but received {completion_id!r}''')
        return self._get_api_list(f'''/chat/completions/{completion_id}/messages''', page = AsyncCursorPage[ChatCompletionStoreMessage], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, message_list_params.MessageListParams)), model = ChatCompletionStoreMessage)



class MessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.list = _legacy_response.to_raw_response_wrapper(messages.list)



class AsyncMessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.list = _legacy_response.async_to_raw_response_wrapper(messages.list)



class MessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.list = to_streamed_response_wrapper(messages.list)



class AsyncMessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.list = async_to_streamed_response_wrapper(messages.list)
