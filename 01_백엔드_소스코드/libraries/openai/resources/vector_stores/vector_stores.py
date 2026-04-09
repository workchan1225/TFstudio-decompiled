# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_stores.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal
import httpx
from  import _legacy_response
from files import Files, AsyncFiles, FilesWithRawResponse, AsyncFilesWithRawResponse, FilesWithStreamingResponse, AsyncFilesWithStreamingResponse
from types import FileChunkingStrategyParam, vector_store_list_params, vector_store_create_params, vector_store_search_params, vector_store_update_params
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage, SyncCursorPage, AsyncCursorPage
from file_batches import FileBatches, AsyncFileBatches, FileBatchesWithRawResponse, AsyncFileBatchesWithRawResponse, FileBatchesWithStreamingResponse, AsyncFileBatchesWithStreamingResponse
from _base_client import AsyncPaginator, make_request_options
from types.vector_store import VectorStore
from types.vector_store_deleted import VectorStoreDeleted
from types.shared_params.metadata import Metadata
from types.file_chunking_strategy_param import FileChunkingStrategyParam
from types.vector_store_search_response import VectorStoreSearchResponse
__all__ = [
    'VectorStores',
    'AsyncVectorStores']

class VectorStores(SyncAPIResource):
    files = (lambda self = None: Files(self._client))()
    file_batches = (lambda self = None: FileBatches(self._client))()
    with_raw_response = (lambda self = None: VectorStoresWithRawResponse(self))()
    with_streaming_response = (lambda self = None: VectorStoresWithStreamingResponse(self))()
    
    def create(self = None, *, chunking_strategy, description, expires_after, file_ids, metadata, name, extra_headers, extra_query, extra_body, timeout):
        """
        Create a vector store.

        Args:
          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          description: A description for the vector store. Can be used to describe the vector store's
              purpose.

          expires_after: The expiration policy for a vector store.

          file_ids: A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that
              the vector store should use. Useful for tools like `file_search` that can access
              files.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, vector_store_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete

    
    def update(self = None, vector_store_id = None, *, expires_after, metadata, name, extra_headers, extra_query, extra_body, timeout):
        '''
        Modifies a vector store.

        Args:
          expires_after: The expiration policy for a vector store.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of vector stores.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, vector_store_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete

    
    def search(self = None, vector_store_id = None, *, query, filters, max_num_results, ranking_options, rewrite_query, extra_headers, extra_query, extra_body, timeout):
        '''
        Search a vector store for relevant chunks based on a query and file attributes
        filter.

        Args:
          query: A query string for a search

          filters: A filter to apply based on file attributes.

          max_num_results: The maximum number of results to return. This number should be between 1 and 50
              inclusive.

          ranking_options: Ranking options for search.

          rewrite_query: Whether to rewrite the natural language query for vector search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncVectorStores(AsyncAPIResource):
    files = (lambda self = None: AsyncFiles(self._client))()
    file_batches = (lambda self = None: AsyncFileBatches(self._client))()
    with_raw_response = (lambda self = None: AsyncVectorStoresWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncVectorStoresWithStreamingResponse(self))()
    
    async def create(self = None, *, chunking_strategy, description, expires_after, file_ids, metadata, name, extra_headers, extra_query, extra_body, timeout):
        """
        Create a vector store.

        Args:
          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          description: A description for the vector store. Can be used to describe the vector store's
              purpose.

          expires_after: The expiration policy for a vector store.

          file_ids: A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that
              the vector store should use. Useful for tools like `file_search` that can access
              files.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, vector_store_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, vector_store_id = None, *, expires_after, metadata, name, extra_headers, extra_query, extra_body, timeout):
        '''
        Modifies a vector store.

        Args:
          expires_after: The expiration policy for a vector store.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the vector store.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of vector stores.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, vector_store_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a vector store.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def search(self = None, vector_store_id = None, *, query, filters, max_num_results, ranking_options, rewrite_query, extra_headers, extra_query, extra_body, timeout):
        '''
        Search a vector store for relevant chunks based on a query and file attributes
        filter.

        Args:
          query: A query string for a search

          filters: A filter to apply based on file attributes.

          max_num_results: The maximum number of results to return. This number should be between 1 and 50
              inclusive.

          ranking_options: Ranking options for search.

          rewrite_query: Whether to rewrite the natural language query for vector search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete



class VectorStoresWithRawResponse:
    
    def __init__(self = None, vector_stores = None):
        self._vector_stores = vector_stores
        self.create = _legacy_response.to_raw_response_wrapper(vector_stores.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(vector_stores.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(vector_stores.update)
        self.list = _legacy_response.to_raw_response_wrapper(vector_stores.list)
        self.delete = _legacy_response.to_raw_response_wrapper(vector_stores.delete)
        self.search = _legacy_response.to_raw_response_wrapper(vector_stores.search)

    files = (lambda self = None: FilesWithRawResponse(self._vector_stores.files))()
    file_batches = (lambda self = None: FileBatchesWithRawResponse(self._vector_stores.file_batches))()


class AsyncVectorStoresWithRawResponse:
    
    def __init__(self = None, vector_stores = None):
        self._vector_stores = vector_stores
        self.create = _legacy_response.async_to_raw_response_wrapper(vector_stores.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(vector_stores.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(vector_stores.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(vector_stores.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(vector_stores.delete)
        self.search = _legacy_response.async_to_raw_response_wrapper(vector_stores.search)

    files = (lambda self = None: AsyncFilesWithRawResponse(self._vector_stores.files))()
    file_batches = (lambda self = None: AsyncFileBatchesWithRawResponse(self._vector_stores.file_batches))()


class VectorStoresWithStreamingResponse:
    
    def __init__(self = None, vector_stores = None):
        self._vector_stores = vector_stores
        self.create = to_streamed_response_wrapper(vector_stores.create)
        self.retrieve = to_streamed_response_wrapper(vector_stores.retrieve)
        self.update = to_streamed_response_wrapper(vector_stores.update)
        self.list = to_streamed_response_wrapper(vector_stores.list)
        self.delete = to_streamed_response_wrapper(vector_stores.delete)
        self.search = to_streamed_response_wrapper(vector_stores.search)

    files = (lambda self = None: FilesWithStreamingResponse(self._vector_stores.files))()
    file_batches = (lambda self = None: FileBatchesWithStreamingResponse(self._vector_stores.file_batches))()


class AsyncVectorStoresWithStreamingResponse:
    
    def __init__(self = None, vector_stores = None):
        self._vector_stores = vector_stores
        self.create = async_to_streamed_response_wrapper(vector_stores.create)
        self.retrieve = async_to_streamed_response_wrapper(vector_stores.retrieve)
        self.update = async_to_streamed_response_wrapper(vector_stores.update)
        self.list = async_to_streamed_response_wrapper(vector_stores.list)
        self.delete = async_to_streamed_response_wrapper(vector_stores.delete)
        self.search = async_to_streamed_response_wrapper(vector_stores.search)

    files = (lambda self = None: AsyncFilesWithStreamingResponse(self._vector_stores.files))()
    file_batches = (lambda self = None: AsyncFileBatchesWithStreamingResponse(self._vector_stores.file_batches))()
