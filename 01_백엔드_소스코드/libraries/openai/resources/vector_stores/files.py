# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, assert_never
import httpx
from  import _legacy_response
from types import FileChunkingStrategyParam
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from _utils import is_given, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage, SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.vector_stores import file_list_params, file_create_params, file_update_params
from types.file_chunking_strategy_param import FileChunkingStrategyParam
from types.vector_stores.vector_store_file import VectorStoreFile
from types.vector_stores.file_content_response import FileContentResponse
from types.vector_stores.vector_store_file_deleted import VectorStoreFileDeleted
__all__ = [
    'Files',
    'AsyncFiles']

class Files(SyncAPIResource):
    with_raw_response = (lambda self = None: FilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FilesWithStreamingResponse(self))()
    
    def create(self = None, vector_store_id = None, *, file_id, attributes, chunking_strategy, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a vector store file by attaching a
        [File](https://platform.openai.com/docs/api-reference/files) to a
        [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

        Args:
          file_id: A [File](https://platform.openai.com/docs/api-reference/files) ID that the
              vector store should use. Useful for tools like `file_search` that can access
              files.

          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def update(self = None, file_id = None, *, vector_store_id, attributes, extra_headers, extra_query, extra_body, timeout):
        '''
        Update attributes on a vector store file.

        Args:
          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, vector_store_id = None, *, after, before, filter, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of vector store files.

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
    # WARNING: Decompyle incomplete

    
    def delete(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''Delete a vector store file.

        This will remove the file from the vector store but
        the file itself will not be deleted. To delete the file, use the
        [delete file](https://platform.openai.com/docs/api-reference/files/delete)
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def create_and_poll(self = None, file_id = None, *, vector_store_id, attributes, poll_interval_ms, chunking_strategy):
        '''Attach a file to the given vector store and wait for it to be processed.'''
        self.create(vector_store_id = vector_store_id, file_id = file_id, chunking_strategy = chunking_strategy, attributes = attributes)
        return self.poll(file_id, vector_store_id = vector_store_id, poll_interval_ms = poll_interval_ms)

    
    def poll(self = None, file_id = None, *, vector_store_id, poll_interval_ms):
        '''Wait for the vector store file to finish processing.

        Note: this will return even if the file failed to process, you need to check
        file.last_error and file.status to handle these cases
        '''
        headers = {
            'X-Stainless-Poll-Helper': 'true' }
        if is_given(poll_interval_ms):
            headers['X-Stainless-Custom-Poll-Interval'] = str(poll_interval_ms)
        response = self.with_raw_response.retrieve(file_id, vector_store_id = vector_store_id, extra_headers = headers)
        file = response.parse()
    # WARNING: Decompyle incomplete

    
    def upload(self = None, *, vector_store_id, file, chunking_strategy):
        '''Upload a file to the `files` API and then attach it to the given vector store.

        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        '''
        file_obj = self._client.files.create(file = file, purpose = 'assistants')
        return self.create(vector_store_id = vector_store_id, file_id = file_obj.id, chunking_strategy = chunking_strategy)

    
    def upload_and_poll(self = None, *, vector_store_id, file, attributes, poll_interval_ms, chunking_strategy):
        '''Add a file to a vector store and poll until processing is complete.'''
        file_obj = self._client.files.create(file = file, purpose = 'assistants')
        return self.create_and_poll(vector_store_id = vector_store_id, file_id = file_obj.id, chunking_strategy = chunking_strategy, poll_interval_ms = poll_interval_ms, attributes = attributes)

    
    def content(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve the parsed contents of a vector store file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncFiles(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncFilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFilesWithStreamingResponse(self))()
    
    async def create(self = None, vector_store_id = None, *, file_id, attributes, chunking_strategy, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a vector store file by attaching a
        [File](https://platform.openai.com/docs/api-reference/files) to a
        [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

        Args:
          file_id: A [File](https://platform.openai.com/docs/api-reference/files) ID that the
              vector store should use. Useful for tools like `file_search` that can access
              files.

          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          chunking_strategy: The chunking strategy used to chunk the file(s). If not set, will use the `auto`
              strategy. Only applicable if `file_ids` is non-empty.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a vector store file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, file_id = None, *, vector_store_id, attributes, extra_headers, extra_query, extra_body, timeout):
        '''
        Update attributes on a vector store file.

        Args:
          attributes: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard. Keys are strings with a maximum
              length of 64 characters. Values are strings with a maximum length of 512
              characters, booleans, or numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, vector_store_id = None, *, after, before, filter, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns a list of vector store files.

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
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''Delete a vector store file.

        This will remove the file from the vector store but
        the file itself will not be deleted. To delete the file, use the
        [delete file](https://platform.openai.com/docs/api-reference/files/delete)
        endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create_and_poll(self = None, file_id = None, *, vector_store_id, attributes, poll_interval_ms, chunking_strategy):
        '''Attach a file to the given vector store and wait for it to be processed.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def poll(self = None, file_id = None, *, vector_store_id, poll_interval_ms):
        '''Wait for the vector store file to finish processing.

        Note: this will return even if the file failed to process, you need to check
        file.last_error and file.status to handle these cases
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def upload(self = None, *, vector_store_id, file, chunking_strategy):
        '''Upload a file to the `files` API and then attach it to the given vector store.

        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def upload_and_poll(self = None, *, vector_store_id, file, attributes, poll_interval_ms, chunking_strategy):
        '''Add a file to a vector store and poll until processing is complete.'''
        pass
    # WARNING: Decompyle incomplete

    
    def content(self = None, file_id = None, *, vector_store_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve the parsed contents of a vector store file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not vector_store_id:
            raise ValueError(f'''Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}''')
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete



class FilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(files.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(files.update)
        self.list = _legacy_response.to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.to_raw_response_wrapper(files.delete)
        self.content = _legacy_response.to_raw_response_wrapper(files.content)



class AsyncFilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.async_to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(files.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(files.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(files.delete)
        self.content = _legacy_response.async_to_raw_response_wrapper(files.content)



class FilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = to_streamed_response_wrapper(files.create)
        self.retrieve = to_streamed_response_wrapper(files.retrieve)
        self.update = to_streamed_response_wrapper(files.update)
        self.list = to_streamed_response_wrapper(files.list)
        self.delete = to_streamed_response_wrapper(files.delete)
        self.content = to_streamed_response_wrapper(files.content)



class AsyncFilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = async_to_streamed_response_wrapper(files.create)
        self.retrieve = async_to_streamed_response_wrapper(files.retrieve)
        self.update = async_to_streamed_response_wrapper(files.update)
        self.list = async_to_streamed_response_wrapper(files.list)
        self.delete = async_to_streamed_response_wrapper(files.delete)
        self.content = async_to_streamed_response_wrapper(files.content)
