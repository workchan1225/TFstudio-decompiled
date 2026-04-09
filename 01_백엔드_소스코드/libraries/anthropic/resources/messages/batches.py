# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batches.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage
from _exceptions import AnthropicError
from _base_client import AsyncPaginator, make_request_options
from types.messages import batch_list_params, batch_create_params
from _decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from types.messages.message_batch import MessageBatch
from types.messages.deleted_message_batch import DeletedMessageBatch
from types.messages.message_batch_individual_response import MessageBatchIndividualResponse
__all__ = [
    'Batches',
    'AsyncBatches']

class Batches(SyncAPIResource):
    with_raw_response = (lambda self = None: BatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: BatchesWithStreamingResponse(self))()
    
    def create(self = None, *, requests, extra_headers, extra_query, extra_body, timeout):
        '''
        Send a batch of Message creation requests.

        The Message Batches API can be used to process multiple Messages API requests at
        once. Once a Message Batch is created, it begins processing immediately. Batches
        can take up to 24 hours to complete.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          requests: List of requests for prompt completion. Each is an individual request to create
              a Message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/v1/messages/batches', body = maybe_transform({
            'requests': requests }, batch_create_params.BatchCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = MessageBatch)

    
    def retrieve(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''This endpoint is idempotent and can be used to poll for Message Batch
        completion.

        To access the results of a Message Batch, make a request to the
        `results_url` field in the response.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not message_batch_id:
            raise ValueError(f'''Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}''')
        return self._get(f'''/v1/messages/batches/{message_batch_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = MessageBatch)

    
    def list(self = None, *, after_id, before_id, limit, extra_headers, extra_query, extra_body, timeout):
        '''List all Message Batches within a Workspace.

        Most recently created batches are
        returned first.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/v1/messages/batches', page = SyncPage[MessageBatch], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after_id': after_id,
            'before_id': before_id,
            'limit': limit }, batch_list_params.BatchListParams)), model = MessageBatch)

    
    def delete(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        """
        Delete a Message Batch.

        Message Batches can only be deleted once they've finished processing. If you'd
        like to delete an in-progress batch, you must first cancel it.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_batch_id:
            raise ValueError(f'''Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}''')
        return self._delete(f'''/v1/messages/batches/{message_batch_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = DeletedMessageBatch)

    
    def cancel(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not message_batch_id:
            raise ValueError(f'''Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}''')
        return self._post(f'''/v1/messages/batches/{message_batch_id}/cancel''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = MessageBatch)

    
    def results(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not message_batch_id:
            raise ValueError(f'''Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}''')
        batch = self.retrieve(message_batch_id = message_batch_id)
        if not batch.results_url:
            raise AnthropicError(f'''No `results_url` for the given batch; Has it finished processing? {batch.processing_status}''')
    # WARNING: Decompyle incomplete



class AsyncBatches(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncBatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncBatchesWithStreamingResponse(self))()
    
    async def create(self = None, *, requests, extra_headers, extra_query, extra_body, timeout):
        '''
        Send a batch of Message creation requests.

        The Message Batches API can be used to process multiple Messages API requests at
        once. Once a Message Batch is created, it begins processing immediately. Batches
        can take up to 24 hours to complete.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          requests: List of requests for prompt completion. Each is an individual request to create
              a Message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''This endpoint is idempotent and can be used to poll for Message Batch
        completion.

        To access the results of a Message Batch, make a request to the
        `results_url` field in the response.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after_id, before_id, limit, extra_headers, extra_query, extra_body, timeout):
        '''List all Message Batches within a Workspace.

        Most recently created batches are
        returned first.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/v1/messages/batches', page = AsyncPage[MessageBatch], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after_id': after_id,
            'before_id': before_id,
            'limit': limit }, batch_list_params.BatchListParams)), model = MessageBatch)

    
    async def delete(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        """
        Delete a Message Batch.

        Message Batches can only be deleted once they've finished processing. If you'd
        like to delete an in-progress batch, you must first cancel it.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def results(self = None, message_batch_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        self.delete = _legacy_response.to_raw_response_wrapper(batches.delete)
        self.cancel = _legacy_response.to_raw_response_wrapper(batches.cancel)



class AsyncBatchesWithRawResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = _legacy_response.async_to_raw_response_wrapper(batches.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(batches.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(batches.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(batches.delete)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(batches.cancel)



class BatchesWithStreamingResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = to_streamed_response_wrapper(batches.create)
        self.retrieve = to_streamed_response_wrapper(batches.retrieve)
        self.list = to_streamed_response_wrapper(batches.list)
        self.delete = to_streamed_response_wrapper(batches.delete)
        self.cancel = to_streamed_response_wrapper(batches.cancel)



class AsyncBatchesWithStreamingResponse:
    
    def __init__(self = None, batches = None):
        self._batches = batches
        self.create = async_to_streamed_response_wrapper(batches.create)
        self.retrieve = async_to_streamed_response_wrapper(batches.retrieve)
        self.list = async_to_streamed_response_wrapper(batches.list)
        self.delete = async_to_streamed_response_wrapper(batches.delete)
        self.cancel = async_to_streamed_response_wrapper(batches.cancel)
