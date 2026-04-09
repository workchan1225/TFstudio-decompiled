# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runs.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from output_items import OutputItems, AsyncOutputItems, OutputItemsWithRawResponse, AsyncOutputItemsWithRawResponse, OutputItemsWithStreamingResponse, AsyncOutputItemsWithStreamingResponse
from pagination import SyncCursorPage, AsyncCursorPage
from types.evals import run_list_params, run_create_params
from _base_client import AsyncPaginator, make_request_options
from types.shared_params.metadata import Metadata
from types.evals.run_list_response import RunListResponse
from types.evals.run_cancel_response import RunCancelResponse
from types.evals.run_create_response import RunCreateResponse
from types.evals.run_delete_response import RunDeleteResponse
from types.evals.run_retrieve_response import RunRetrieveResponse
__all__ = [
    'Runs',
    'AsyncRuns']

class Runs(SyncAPIResource):
    output_items = (lambda self = None: OutputItems(self._client))()
    with_raw_response = (lambda self = None: RunsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: RunsWithStreamingResponse(self))()
    
    def create(self = None, eval_id = None, *, data_source, metadata, name, extra_headers, extra_query, extra_body, timeout):
        """
        Kicks off a new run for a given evaluation, specifying the data source, and what
        model configuration to use to test. The datasource will be validated against the
        schema specified in the config of the evaluation.

        Args:
          data_source: Details about the run's data source.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        return self._post(f'''/evals/{eval_id}/runs''', body = maybe_transform({
            'data_source': data_source,
            'metadata': metadata,
            'name': name }, run_create_params.RunCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = RunCreateResponse)

    
    def retrieve(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Get an evaluation run by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        if not run_id:
            raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')
        return self._get(f'''/evals/{eval_id}/runs/{run_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = RunRetrieveResponse)

    
    def list(self = None, eval_id = None, *, after, limit, order, status, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a list of runs for an evaluation.

        Args:
          after: Identifier for the last run from the previous pagination request.

          limit: Number of runs to retrieve.

          order: Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for
              descending order. Defaults to `asc`.

          status: Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed`
              | `canceled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        return self._get_api_list(f'''/evals/{eval_id}/runs''', page = SyncCursorPage[RunListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order,
            'status': status }, run_list_params.RunListParams)), model = RunListResponse)

    
    def delete(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an eval run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        if not run_id:
            raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')
        return self._delete(f'''/evals/{eval_id}/runs/{run_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = RunDeleteResponse)

    
    def cancel(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Cancel an ongoing evaluation run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        if not run_id:
            raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')
        return self._post(f'''/evals/{eval_id}/runs/{run_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = RunCancelResponse)



class AsyncRuns(AsyncAPIResource):
    output_items = (lambda self = None: AsyncOutputItems(self._client))()
    with_raw_response = (lambda self = None: AsyncRunsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncRunsWithStreamingResponse(self))()
    
    async def create(self = None, eval_id = None, *, data_source, metadata, name, extra_headers, extra_query, extra_body, timeout):
        """
        Kicks off a new run for a given evaluation, specifying the data source, and what
        model configuration to use to test. The datasource will be validated against the
        schema specified in the config of the evaluation.

        Args:
          data_source: Details about the run's data source.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Get an evaluation run by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, eval_id = None, *, after, limit, order, status, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a list of runs for an evaluation.

        Args:
          after: Identifier for the last run from the previous pagination request.

          limit: Number of runs to retrieve.

          order: Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for
              descending order. Defaults to `asc`.

          status: Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed`
              | `canceled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not eval_id:
            raise ValueError(f'''Expected a non-empty value for `eval_id` but received {eval_id!r}''')
        return self._get_api_list(f'''/evals/{eval_id}/runs''', page = AsyncCursorPage[RunListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order,
            'status': status }, run_list_params.RunListParams)), model = RunListResponse)

    
    async def delete(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an eval run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, run_id = None, *, eval_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Cancel an ongoing evaluation run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class RunsWithRawResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = _legacy_response.to_raw_response_wrapper(runs.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(runs.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(runs.list)
        self.delete = _legacy_response.to_raw_response_wrapper(runs.delete)
        self.cancel = _legacy_response.to_raw_response_wrapper(runs.cancel)

    output_items = (lambda self = None: OutputItemsWithRawResponse(self._runs.output_items))()


class AsyncRunsWithRawResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = _legacy_response.async_to_raw_response_wrapper(runs.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(runs.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(runs.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(runs.delete)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(runs.cancel)

    output_items = (lambda self = None: AsyncOutputItemsWithRawResponse(self._runs.output_items))()


class RunsWithStreamingResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = to_streamed_response_wrapper(runs.create)
        self.retrieve = to_streamed_response_wrapper(runs.retrieve)
        self.list = to_streamed_response_wrapper(runs.list)
        self.delete = to_streamed_response_wrapper(runs.delete)
        self.cancel = to_streamed_response_wrapper(runs.cancel)

    output_items = (lambda self = None: OutputItemsWithStreamingResponse(self._runs.output_items))()


class AsyncRunsWithStreamingResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = async_to_streamed_response_wrapper(runs.create)
        self.retrieve = async_to_streamed_response_wrapper(runs.retrieve)
        self.list = async_to_streamed_response_wrapper(runs.list)
        self.delete = async_to_streamed_response_wrapper(runs.delete)
        self.cancel = async_to_streamed_response_wrapper(runs.cancel)

    output_items = (lambda self = None: AsyncOutputItemsWithStreamingResponse(self._runs.output_items))()
