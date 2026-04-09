# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batches.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal
import httpx
from  import _legacy_response
from types import batch_list_params, batch_create_params
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from types.batch import Batch
from _base_client import AsyncPaginator, make_request_options
from types.shared_params.metadata import Metadata
__all__ = [
    'Batches',
    'AsyncBatches']

class Batches(SyncAPIResource):
    with_raw_response = (lambda self = None: BatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: BatchesWithStreamingResponse(self))()
    
    def create(self = None, *, completion_window, endpoint, input_file_id, metadata, output_expires_after, extra_headers, extra_query, extra_body, timeout):
        '''
        Creates and executes a batch from an uploaded file of requests

        Args:
          completion_window: The time frame within which the batch should be processed. Currently only `24h`
              is supported.

          endpoint: The endpoint to be used for all requests in the batch. Currently
              `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`,
              and `/v1/moderations` are supported. Note that `/v1/embeddings` batches are also
              restricted to a maximum of 50,000 embedding inputs across all requests in the
              batch.

          input_file_id: The ID of an uploaded file that contains requests for the new batch.

              See [upload file](https://platform.openai.com/docs/api-reference/files/create)
              for how to upload a file.

              Your input file must be formatted as a
              [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input),
              and must be uploaded with the purpose `batch`. The file can contain up to 50,000
              requests, and can be up to 200 MB in size.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          output_expires_after: The expiration policy for the output and/or error file that are generated for a
              batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/batches', body = maybe_transform({
            'completion_window': completion_window,
            'endpoint': endpoint,
            'input_file_id': input_file_id,
            'metadata': metadata,
            'output_expires_after': output_expires_after }, batch_create_params.BatchCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Batch)

    
    def retrieve(self = None, batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
        return self._get(f'''/batches/{batch_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Batch)

    
    def list(self = None, *, after, limit, extra_headers, extra_query, extra_body, timeout):
        """List your organization's batches.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list('/batches', page = SyncCursorPage[Batch], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit }, batch_list_params.BatchListParams)), model = Batch)

    
    def cancel(self = None, batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Cancels an in-progress batch.

        The batch will be in status `cancelling` for up to
        10 minutes, before changing to `cancelled`, where it will have partial results
        (if any) available in the output file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
        return self._post(f'''/batches/{batch_id}/cancel''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Batch)



class AsyncBatches(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncBatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncBatchesWithStreamingResponse(self))()
    
    async def create(self = None, *, completion_window, endpoint, input_file_id, metadata, output_expires_after, extra_headers, extra_query, extra_body, timeout):
        '''
        Creates and executes a batch from an uploaded file of requests

        Args:
          completion_window: The time frame within which the batch should be processed. Currently only `24h`
              is supported.

          endpoint: The endpoint to be used for all requests in the batch. Currently
              `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`,
              and `/v1/moderations` are supported. Note that `/v1/embeddings` batches are also
              restricted to a maximum of 50,000 embedding inputs across all requests in the
              batch.

          input_file_id: The ID of an uploaded file that contains requests for the new batch.

              See [upload file](https://platform.openai.com/docs/api-reference/files/create)
              for how to upload a file.

              Your input file must be formatted as a
              [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input),
              and must be uploaded with the purpose `batch`. The file can contain up to 50,000
              requests, and can be up to 200 MB in size.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          output_expires_after: The expiration policy for the output and/or error file that are generated for a
              batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, limit, extra_headers, extra_query, extra_body, timeout):
        """List your organization's batches.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list('/batches', page = AsyncCursorPage[Batch], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit }, batch_list_params.BatchListParams)), model = Batch)

    
    async def cancel(self = None, batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Cancels an in-progress batch.

        The batch will be in status `cancelling` for up to
        10 minutes, before changing to `cancelled`, where it will have partial results
        (if any) available in the output file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class BatchesWithRawResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = _legacy_response.to_raw_response_wrapper(batches.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(batches.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(batches.list)
        self.cancel = _legacy_response.to_raw_response_wrapper(batches.cancel)



class AsyncBatchesWithRawResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = _legacy_response.async_to_raw_response_wrapper(batches.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(batches.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(batches.list)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(batches.cancel)



class BatchesWithStreamingResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = to_streamed_response_wrapper(batches.create)
        self.retrieve = to_streamed_response_wrapper(batches.retrieve)
        self.list = to_streamed_response_wrapper(batches.list)
        self.cancel = to_streamed_response_wrapper(batches.cancel)



class AsyncBatchesWithStreamingResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = async_to_streamed_response_wrapper(batches.create)
        self.retrieve = async_to_streamed_response_wrapper(batches.retrieve)
        self.list = async_to_streamed_response_wrapper(batches.list)
        self.cancel = async_to_streamed_response_wrapper(batches.cancel)
