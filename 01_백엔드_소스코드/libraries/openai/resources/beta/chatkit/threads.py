# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: threads.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, cast
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncConversationCursorPage, AsyncConversationCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.beta.chatkit import thread_list_params, thread_list_items_params
from types.beta.chatkit.chatkit_thread import ChatKitThread
from types.beta.chatkit.thread_delete_response import ThreadDeleteResponse
from types.beta.chatkit.chatkit_thread_item_list import Data
__all__ = [
    'Threads',
    'AsyncThreads']

class Threads(SyncAPIResource):
    with_raw_response = (lambda self = None: ThreadsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ThreadsWithStreamingResponse(self))()
    
    def retrieve(self = None, thread_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve a ChatKit thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not thread_id:
            raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, user, extra_headers, extra_query, extra_body, timeout):
        '''
        List ChatKit threads

        Args:
          after: List items created after this thread item ID. Defaults to null for the first
              page.

          before: List items created before this thread item ID. Defaults to null for the newest
              results.

          limit: Maximum number of thread items to return. Defaults to 20.

          order: Sort order for results by creation time. Defaults to `desc`.

          user: Filter threads that belong to this user identifier. Defaults to null to return
              all users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, thread_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a ChatKit thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not thread_id:
            raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list_items(self = None, thread_id = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        List ChatKit thread items

        Args:
          after: List items created after this thread item ID. Defaults to null for the first
              page.

          before: List items created before this thread item ID. Defaults to null for the newest
              results.

          limit: Maximum number of thread items to return. Defaults to 20.

          order: Sort order for results by creation time. Defaults to `desc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not thread_id:
            raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncThreads(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncThreadsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncThreadsWithStreamingResponse(self))()
    
    async def retrieve(self = None, thread_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve a ChatKit thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, user, extra_headers, extra_query, extra_body, timeout):
        '''
        List ChatKit threads

        Args:
          after: List items created after this thread item ID. Defaults to null for the first
              page.

          before: List items created before this thread item ID. Defaults to null for the newest
              results.

          limit: Maximum number of thread items to return. Defaults to 20.

          order: Sort order for results by creation time. Defaults to `desc`.

          user: Filter threads that belong to this user identifier. Defaults to null to return
              all users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, thread_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a ChatKit thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list_items(self = None, thread_id = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        List ChatKit thread items

        Args:
          after: List items created after this thread item ID. Defaults to null for the first
              page.

          before: List items created before this thread item ID. Defaults to null for the newest
              results.

          limit: Maximum number of thread items to return. Defaults to 20.

          order: Sort order for results by creation time. Defaults to `desc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not thread_id:
            raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')
    # WARNING: Decompyle incomplete



class ThreadsWithRawResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.retrieve = _legacy_response.to_raw_response_wrapper(threads.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(threads.list)
        self.delete = _legacy_response.to_raw_response_wrapper(threads.delete)
        self.list_items = _legacy_response.to_raw_response_wrapper(threads.list_items)



class AsyncThreadsWithRawResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(threads.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(threads.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(threads.delete)
        self.list_items = _legacy_response.async_to_raw_response_wrapper(threads.list_items)



class ThreadsWithStreamingResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.retrieve = to_streamed_response_wrapper(threads.retrieve)
        self.list = to_streamed_response_wrapper(threads.list)
        self.delete = to_streamed_response_wrapper(threads.delete)
        self.list_items = to_streamed_response_wrapper(threads.list_items)



class AsyncThreadsWithStreamingResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.retrieve = async_to_streamed_response_wrapper(threads.retrieve)
        self.list = async_to_streamed_response_wrapper(threads.list)
        self.delete = async_to_streamed_response_wrapper(threads.delete)
        self.list_items = async_to_streamed_response_wrapper(threads.list_items)
