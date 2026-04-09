# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_items.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, List, cast
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
from types.responses import input_item_list_params
from types.responses.response_item import ResponseItem
from types.responses.response_includable import ResponseIncludable
__all__ = [
    'InputItems',
    'AsyncInputItems']

class InputItems(SyncAPIResource):
    with_raw_response = (lambda self = None: InputItemsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: InputItemsWithStreamingResponse(self))()
    
    def list(self = None, response_id = None, *, after, include, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of input items for a given response.

        Args:
          after: An item ID to list items after, used in pagination.

          include: Additional fields to include in the response. See the `include` parameter for
              Response creation above for more information.

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
        if not response_id:
            raise ValueError(f'''Expected a non-empty value for `response_id` but received {response_id!r}''')
        return self._get_api_list(f'''/responses/{response_id}/input_items''', page = SyncCursorPage[ResponseItem], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'include': include,
            'limit': limit,
            'order': order }, input_item_list_params.InputItemListParams)), model = cast(Any, ResponseItem))



class AsyncInputItems(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncInputItemsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncInputItemsWithStreamingResponse(self))()
    
    def list(self = None, response_id = None, *, after, include, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of input items for a given response.

        Args:
          after: An item ID to list items after, used in pagination.

          include: Additional fields to include in the response. See the `include` parameter for
              Response creation above for more information.

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
        if not response_id:
            raise ValueError(f'''Expected a non-empty value for `response_id` but received {response_id!r}''')
        return self._get_api_list(f'''/responses/{response_id}/input_items''', page = AsyncCursorPage[ResponseItem], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'include': include,
            'limit': limit,
            'order': order }, input_item_list_params.InputItemListParams)), model = cast(Any, ResponseItem))



class InputItemsWithRawResponse:
    
    def __init__(self = None, input_items = None):
        self._input_items = input_items
        self.list = _legacy_response.to_raw_response_wrapper(input_items.list)



class AsyncInputItemsWithRawResponse:
    
    def __init__(self = None, input_items = None):
        self._input_items = input_items
        self.list = _legacy_response.async_to_raw_response_wrapper(input_items.list)



class InputItemsWithStreamingResponse:
    
    def __init__(self = None, input_items = None):
        self._input_items = input_items
        self.list = to_streamed_response_wrapper(input_items.list)



class AsyncInputItemsWithStreamingResponse:
    
    def __init__(self = None, input_items = None):
        self._input_items = input_items
        self.list = async_to_streamed_response_wrapper(input_items.list)
