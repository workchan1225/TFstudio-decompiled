# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content.pyc (Python 3.11)

from __future__ import annotations
import httpx
from  import _legacy_response
from _types import Body, Query, Headers, NotGiven, not_given
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import StreamedBinaryAPIResponse, AsyncStreamedBinaryAPIResponse, to_custom_streamed_response_wrapper, async_to_custom_streamed_response_wrapper
from _base_client import make_request_options
__all__ = [
    'Content',
    'AsyncContent']

class Content(SyncAPIResource):
    with_raw_response = (lambda self = None: ContentWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ContentWithStreamingResponse(self))()
    
    def retrieve(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container File Content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncContent(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncContentWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncContentWithStreamingResponse(self))()
    
    async def retrieve(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container File Content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class ContentWithRawResponse:
    
    def __init__(self = None, content = None):
        self._content = content
        self.retrieve = _legacy_response.to_raw_response_wrapper(content.retrieve)



class AsyncContentWithRawResponse:
    
    def __init__(self = None, content = None):
        self._content = content
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(content.retrieve)



class ContentWithStreamingResponse:
    
    def __init__(self = None, content = None):
        self._content = content
        self.retrieve = to_custom_streamed_response_wrapper(content.retrieve, StreamedBinaryAPIResponse)



class AsyncContentWithStreamingResponse:
    
    def __init__(self = None, content = None):
        self._content = content
        self.retrieve = async_to_custom_streamed_response_wrapper(content.retrieve, AsyncStreamedBinaryAPIResponse)
