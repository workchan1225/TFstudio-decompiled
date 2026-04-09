# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversations.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable, Optional
import httpx
from  import _legacy_response
from items import Items, AsyncItems, ItemsWithRawResponse, AsyncItemsWithRawResponse, ItemsWithStreamingResponse, AsyncItemsWithStreamingResponse
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.conversations import conversation_create_params, conversation_update_params
from types.shared_params.metadata import Metadata
from types.conversations.conversation import Conversation
from types.responses.response_input_item_param import ResponseInputItemParam
from types.conversations.conversation_deleted_resource import ConversationDeletedResource
__all__ = [
    'Conversations',
    'AsyncConversations']

class Conversations(SyncAPIResource):
    items = (lambda self = None: Items(self._client))()
    with_raw_response = (lambda self = None: ConversationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ConversationsWithStreamingResponse(self))()
    
    def create(self = None, *, items, metadata, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a conversation.

        Args:
          items: Initial items to include in the conversation context. You may add up to 20 items
              at a time.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/conversations', body = maybe_transform({
            'items': items,
            'metadata': metadata }, conversation_create_params.ConversationCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Conversation)

    
    def retrieve(self = None, conversation_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._get(f'''/conversations/{conversation_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Conversation)

    
    def update(self = None, conversation_id = None, *, metadata, extra_headers, extra_query, extra_body, timeout):
        '''
        Update a conversation

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._post(f'''/conversations/{conversation_id}''', body = maybe_transform({
            'metadata': metadata }, conversation_update_params.ConversationUpdateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Conversation)

    
    def delete(self = None, conversation_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a conversation.

        Items in the conversation will not be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._delete(f'''/conversations/{conversation_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ConversationDeletedResource)



class AsyncConversations(AsyncAPIResource):
    items = (lambda self = None: AsyncItems(self._client))()
    with_raw_response = (lambda self = None: AsyncConversationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncConversationsWithStreamingResponse(self))()
    
    async def create(self = None, *, items, metadata, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a conversation.

        Args:
          items: Initial items to include in the conversation context. You may add up to 20 items
              at a time.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, conversation_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, conversation_id = None, *, metadata, extra_headers, extra_query, extra_body, timeout):
        '''
        Update a conversation

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, conversation_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a conversation.

        Items in the conversation will not be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class ConversationsWithRawResponse:
    
    def __init__(self = None, conversations = None):
        self._conversations = conversations
        self.create = _legacy_response.to_raw_response_wrapper(conversations.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(conversations.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(conversations.update)
        self.delete = _legacy_response.to_raw_response_wrapper(conversations.delete)

    items = (lambda self = None: ItemsWithRawResponse(self._conversations.items))()


class AsyncConversationsWithRawResponse:
    
    def __init__(self = None, conversations = None):
        self._conversations = conversations
        self.create = _legacy_response.async_to_raw_response_wrapper(conversations.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(conversations.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(conversations.update)
        self.delete = _legacy_response.async_to_raw_response_wrapper(conversations.delete)

    items = (lambda self = None: AsyncItemsWithRawResponse(self._conversations.items))()


class ConversationsWithStreamingResponse:
    
    def __init__(self = None, conversations = None):
        self._conversations = conversations
        self.create = to_streamed_response_wrapper(conversations.create)
        self.retrieve = to_streamed_response_wrapper(conversations.retrieve)
        self.update = to_streamed_response_wrapper(conversations.update)
        self.delete = to_streamed_response_wrapper(conversations.delete)

    items = (lambda self = None: ItemsWithStreamingResponse(self._conversations.items))()


class AsyncConversationsWithStreamingResponse:
    
    def __init__(self = None, conversations = None):
        self._conversations = conversations
        self.create = async_to_streamed_response_wrapper(conversations.create)
        self.retrieve = async_to_streamed_response_wrapper(conversations.retrieve)
        self.update = async_to_streamed_response_wrapper(conversations.update)
        self.delete = async_to_streamed_response_wrapper(conversations.delete)

    items = (lambda self = None: AsyncItemsWithStreamingResponse(self._conversations.items))()
