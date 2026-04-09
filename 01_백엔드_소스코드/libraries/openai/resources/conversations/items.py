# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: items.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, List, Iterable, cast
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncConversationCursorPage, AsyncConversationCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.conversations import item_list_params, item_create_params, item_retrieve_params
from types.conversations.conversation import Conversation
from types.responses.response_includable import ResponseIncludable
from types.conversations.conversation_item import ConversationItem
from types.responses.response_input_item_param import ResponseInputItemParam
from types.conversations.conversation_item_list import ConversationItemList
__all__ = [
    'Items',
    'AsyncItems']

class Items(SyncAPIResource):
    with_raw_response = (lambda self = None: ItemsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ItemsWithStreamingResponse(self))()
    
    def create(self = None, conversation_id = None, *, items, include, extra_headers, extra_query, extra_body, timeout):
        '''
        Create items in a conversation with the given ID.

        Args:
          items: The items to add to the conversation. You may add up to 20 items at a time.

          include: Additional fields to include in the response. See the `include` parameter for
              [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._post(f'''/conversations/{conversation_id}/items''', body = maybe_transform({
            'items': items }, item_create_params.ItemCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'include': include }, item_create_params.ItemCreateParams)), cast_to = ConversationItemList)

    
    def retrieve(self = None, item_id = None, *, conversation_id, include, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a single item from a conversation with the given IDs.

        Args:
          include: Additional fields to include in the response. See the `include` parameter for
              [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        if not item_id:
            raise ValueError(f'''Expected a non-empty value for `item_id` but received {item_id!r}''')
        return cast(ConversationItem, self._get(f'''/conversations/{conversation_id}/items/{item_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'include': include }, item_retrieve_params.ItemRetrieveParams)), cast_to = cast(Any, ConversationItem)))

    
    def list(self = None, conversation_id = None, *, after, include, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        List all items for a conversation with the given ID.

        Args:
          after: An item ID to list items after, used in pagination.

          include: Specify additional output data to include in the model response. Currently
              supported values are:

              - `web_search_call.action.sources`: Include the sources of the web search tool
                call.
              - `code_interpreter_call.outputs`: Includes the outputs of python code execution
                in code interpreter tool call items.
              - `computer_call_output.output.image_url`: Include image urls from the computer
                call output.
              - `file_search_call.results`: Include the search results of the file search tool
                call.
              - `message.input_image.image_url`: Include image urls from the input message.
              - `message.output_text.logprobs`: Include logprobs with assistant messages.
              - `reasoning.encrypted_content`: Includes an encrypted version of reasoning
                tokens in reasoning item outputs. This enables reasoning items to be used in
                multi-turn conversations when using the Responses API statelessly (like when
                the `store` parameter is set to `false`, or when an organization is enrolled
                in the zero data retention program).

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: The order to return the input items in. Default is `desc`.

              - `asc`: Return the input items in ascending order.
              - `desc`: Return the input items in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._get_api_list(f'''/conversations/{conversation_id}/items''', page = SyncConversationCursorPage[ConversationItem], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'include': include,
            'limit': limit,
            'order': order }, item_list_params.ItemListParams)), model = cast(Any, ConversationItem))

    
    def delete(self = None, item_id = None, *, conversation_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an item from a conversation with the given IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        if not item_id:
            raise ValueError(f'''Expected a non-empty value for `item_id` but received {item_id!r}''')
        return self._delete(f'''/conversations/{conversation_id}/items/{item_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Conversation)



class AsyncItems(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncItemsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncItemsWithStreamingResponse(self))()
    
    async def create(self = None, conversation_id = None, *, items, include, extra_headers, extra_query, extra_body, timeout):
        '''
        Create items in a conversation with the given ID.

        Args:
          items: The items to add to the conversation. You may add up to 20 items at a time.

          include: Additional fields to include in the response. See the `include` parameter for
              [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, item_id = None, *, conversation_id, include, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a single item from a conversation with the given IDs.

        Args:
          include: Additional fields to include in the response. See the `include` parameter for
              [listing Conversation items above](https://platform.openai.com/docs/api-reference/conversations/list-items#conversations_list_items-include)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, conversation_id = None, *, after, include, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        List all items for a conversation with the given ID.

        Args:
          after: An item ID to list items after, used in pagination.

          include: Specify additional output data to include in the model response. Currently
              supported values are:

              - `web_search_call.action.sources`: Include the sources of the web search tool
                call.
              - `code_interpreter_call.outputs`: Includes the outputs of python code execution
                in code interpreter tool call items.
              - `computer_call_output.output.image_url`: Include image urls from the computer
                call output.
              - `file_search_call.results`: Include the search results of the file search tool
                call.
              - `message.input_image.image_url`: Include image urls from the input message.
              - `message.output_text.logprobs`: Include logprobs with assistant messages.
              - `reasoning.encrypted_content`: Includes an encrypted version of reasoning
                tokens in reasoning item outputs. This enables reasoning items to be used in
                multi-turn conversations when using the Responses API statelessly (like when
                the `store` parameter is set to `false`, or when an organization is enrolled
                in the zero data retention program).

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: The order to return the input items in. Default is `desc`.

              - `asc`: Return the input items in ascending order.
              - `desc`: Return the input items in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not conversation_id:
            raise ValueError(f'''Expected a non-empty value for `conversation_id` but received {conversation_id!r}''')
        return self._get_api_list(f'''/conversations/{conversation_id}/items''', page = AsyncConversationCursorPage[ConversationItem], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'include': include,
            'limit': limit,
            'order': order }, item_list_params.ItemListParams)), model = cast(Any, ConversationItem))

    
    async def delete(self = None, item_id = None, *, conversation_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an item from a conversation with the given IDs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class ItemsWithRawResponse:
    
    def __init__(self = None, items = None):
        self._items = items
        self.create = _legacy_response.to_raw_response_wrapper(items.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(items.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(items.list)
        self.delete = _legacy_response.to_raw_response_wrapper(items.delete)



class AsyncItemsWithRawResponse:
    
    def __init__(self = None, items = None):
        self._items = items
        self.create = _legacy_response.async_to_raw_response_wrapper(items.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(items.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(items.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(items.delete)



class ItemsWithStreamingResponse:
    
    def __init__(self = None, items = None):
        self._items = items
        self.create = to_streamed_response_wrapper(items.create)
        self.retrieve = to_streamed_response_wrapper(items.retrieve)
        self.list = to_streamed_response_wrapper(items.list)
        self.delete = to_streamed_response_wrapper(items.delete)



class AsyncItemsWithStreamingResponse:
    
    def __init__(self = None, items = None):
        self._items = items
        self.create = async_to_streamed_response_wrapper(items.create)
        self.retrieve = async_to_streamed_response_wrapper(items.retrieve)
        self.list = async_to_streamed_response_wrapper(items.list)
        self.delete = async_to_streamed_response_wrapper(items.delete)
