# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_batches.pyc (Python 3.11)

from __future__ import annotations
import asyncio
from typing import Dict, Iterable, Optional
from typing_extensions import Union, Literal
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
import httpx
import sniffio
from  import _legacy_response
from types import FileChunkingStrategyParam
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from _utils import is_given, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.file_object import FileObject
from types.vector_stores import file_batch_create_params, file_batch_list_files_params
from types.file_chunking_strategy_param import FileChunkingStrategyParam
from types.vector_stores.vector_store_file import VectorStoreFile
from types.vector_stores.vector_store_file_batch import VectorStoreFileBatch
__all__ = [
    'FileBatches',
    'AsyncFileBatches']

class FileBatches(SyncAPIResource):
    with_raw_response = (lambda self = None: FileBatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FileBatchesWithStreamingResponse(self))()
    
    def create(self = None, vector_store_id = None, *, attributes, chunking_strategy, file_ids, files, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a vector store file batch.

        Args:
          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          file_ids: A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that
              the vector store should use. Useful for tools like `file_search` that can access
              files. If `attributes` or `chunking_strategy` are provided, they will be applied
              to all files in the batch. Mutually exclusive with `files`.

          files: A list of objects that each include a `file_id` plus optional `attributes` or
              `chunking_strategy`. Use this when you need to override metadata for specific
              files. The global `attributes` or `chunking_strategy` will be ignored and must
              be specified for each file. Mutually exclusive with `file_ids`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, batch_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
    # WARNING: Decompyle incomplete

    
    def cancel(self = None, batch_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''Cancel a vector store file batch.

        This attempts to cancel the processing of
        files in this batch as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
    # WARNING: Decompyle incomplete

    
    def create_and_poll(self = None, vector_store_id = None, *, file_ids, poll_interval_ms, chunking_strategy):
        '''Create a vector store batch and poll until all files have been processed.'''
        batch = self.create(vector_store_id = vector_store_id, file_ids = file_ids, chunking_strategy = chunking_strategy)
        return self.poll(batch.id, vector_store_id = vector_store_id, poll_interval_ms = poll_interval_ms)

    
    def list_files(self = None, batch_id = None, *, vector_store_id, after, before, filter, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of vector store files in a batch.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          filter: Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
    # WARNING: Decompyle incomplete

    
    def poll(self = None, batch_id = None, *, vector_store_id, poll_interval_ms):
        '''Wait for the given file batch to be processed.

        Note: this will return even if one of the files failed to process, you need to
        check batch.file_counts.failed_count to handle this case.
        '''
        headers = {
            'X-Stainless-Poll-Helper': 'true' }
        if is_given(poll_interval_ms):
            headers['X-Stainless-Custom-Poll-Interval'] = str(poll_interval_ms)
        response = self.with_raw_response.retrieve(batch_id, vector_store_id = vector_store_id, extra_headers = headers)
        batch = response.parse()
    # WARNING: Decompyle incomplete

    
    def upload_and_poll(self = None, vector_store_id = None, *, files, max_concurrency, file_ids, poll_interval_ms, chunking_strategy):
        """Uploads the given files concurrently and then creates a vector store file batch.

        If you've already uploaded certain files that you want to include in this batch
        then you can pass their IDs through the `file_ids` argument.

        By default, if any file upload fails then an exception will be eagerly raised.

        The number of concurrency uploads is configurable using the `max_concurrency`
        parameter.

        Note: this method only supports `asyncio` or `trio` as the backing async
        runtime.
        """
        pass
    # WARNING: Decompyle incomplete



class AsyncFileBatches(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncFileBatchesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFileBatchesWithStreamingResponse(self))()
    
    async def create(self = None, vector_store_id = None, *, attributes, chunking_strategy, file_ids, files, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a vector store file batch.

        Args:
          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          file_ids: A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that
              the vector store should use. Useful for tools like `file_search` that can access
              files. If `attributes` or `chunking_strategy` are provided, they will be applied
              to all files in the batch. Mutually exclusive with `files`.

          files: A list of objects that each include a `file_id` plus optional `attributes` or
              `chunking_strategy`. Use this when you need to override metadata for specific
              files. The global `attributes` or `chunking_strategy` will be ignored and must
              be specified for each file. Mutually exclusive with `file_ids`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, batch_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store file batch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, batch_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''Cancel a vector store file batch.

        This attempts to cancel the processing of
        files in this batch as soon as possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create_and_poll(self = None, vector_store_id = None, *, file_ids, poll_interval_ms, chunking_strategy):
        '''Create a vector store batch and poll until all files have been processed.'''
        pass
    # WARNING: Decompyle incomplete

    
    def list_files(self = None, batch_id = None, *, vector_store_id, after, before, filter, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of vector store files in a batch.

        Args:
          after: A cursor for use in pagination. `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          filter: Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not batch_id:
            raise ValueError(f'''Expected a non-empty value for `batch_id` but received {batch_id!r}''')
    # WARNING: Decompyle incomplete

    
    async def poll(self = None, batch_id = None, *, vector_store_id, poll_interval_ms):
        '''Wait for the given file batch to be processed.

        Note: this will return even if one of the files failed to process, you need to
        check batch.file_counts.failed_count to handle this case.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def upload_and_poll(self = None, vector_store_id = None, *, files, max_concurrency, file_ids, poll_interval_ms, chunking_strategy):
        """Uploads the given files concurrently and then creates a vector store file batch.

        If you've already uploaded certain files that you want to include in this batch
        then you can pass their IDs through the `file_ids` argument.

        By default, if any file upload fails then an exception will be eagerly raised.

        The number of concurrency uploads is configurable using the `max_concurrency`
        parameter.

        Note: this method only supports `asyncio` or `trio` as the backing async
        runtime.
        """
        pass
    # WARNING: Decompyle incomplete



class FileBatchesWithRawResponse:
    
    def __init__(self = None, file_batches = None):
        self._file_batches = file_batches
        self.create = _legacy_response.to_raw_response_wrapper(file_batches.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(file_batches.retrieve)
        self.cancel = _legacy_response.to_raw_response_wrapper(file_batches.cancel)
        self.list_files = _legacy_response.to_raw_response_wrapper(file_batches.list_files)



class AsyncFileBatchesWithRawResponse:
    
    def __init__(self = None, file_batches = None):
        self._file_batches = file_batches
        self.create = _legacy_response.async_to_raw_response_wrapper(file_batches.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(file_batches.retrieve)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(file_batches.cancel)
        self.list_files = _legacy_response.async_to_raw_response_wrapper(file_batches.list_files)



class FileBatchesWithStreamingResponse:
    
    def __init__(self = None, file_batches = None):
        self._file_batches = file_batches
        self.create = to_streamed_response_wrapper(file_batches.create)
        self.retrieve = to_streamed_response_wrapper(file_batches.retrieve)
        self.cancel = to_streamed_response_wrapper(file_batches.cancel)
        self.list_files = to_streamed_response_wrapper(file_batches.list_files)



class AsyncFileBatchesWithStreamingResponse:
    
    def __init__(self = None, file_batches = None):
        self._file_batches = file_batches
        self.create = async_to_streamed_response_wrapper(file_batches.create)
        self.retrieve = async_to_streamed_response_wrapper(file_batches.retrieve)
        self.cancel = async_to_streamed_response_wrapper(file_batches.cancel)
        self.list_files = async_to_streamed_response_wrapper(file_batches.list_files)
