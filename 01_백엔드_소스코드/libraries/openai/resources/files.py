# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import annotations
import time
import typing_extensions
from typing import Mapping, cast
from typing_extensions import Literal
import httpx
from  import _legacy_response
from types import FilePurpose, file_list_params, file_create_params
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from _utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import StreamedBinaryAPIResponse, AsyncStreamedBinaryAPIResponse, to_streamed_response_wrapper, async_to_streamed_response_wrapper, to_custom_streamed_response_wrapper, async_to_custom_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.file_object import FileObject
from types.file_deleted import FileDeleted
from types.file_purpose import FilePurpose
__all__ = [
    'Files',
    'AsyncFiles']

class Files(SyncAPIResource):
    with_raw_response = (lambda self = None: FilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FilesWithStreamingResponse(self))()
    
    def create(self = None, *, file, purpose, expires_after, extra_headers, extra_query, extra_body, timeout):
        '''Upload a file that can be used across various endpoints.

        Individual files can be
        up to 512 MB, and the size of all files uploaded by one organization can be up
        to 1 TB.

        - The Assistants API supports files up to 2 million tokens and of specific file
          types. See the
          [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools)
          for details.
        - The Fine-tuning API only supports `.jsonl` files. The input also has certain
          required formats for fine-tuning
          [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input)
          or
          [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input)
          models.
        - The Batch API only supports `.jsonl` files up to 200 MB in size. The input
          also has a specific required
          [format](https://platform.openai.com/docs/api-reference/batch/request-input).

        Please [contact us](https://help.openai.com/) if you need to increase these
        storage limits.

        Args:
          file: The File object (not file name) to be uploaded.

          purpose: The intended purpose of the uploaded file. One of: - `assistants`: Used in the
              Assistants API - `batch`: Used in the Batch API - `fine-tune`: Used for
              fine-tuning - `vision`: Images used for vision fine-tuning - `user_data`:
              Flexible file type for any purpose - `evals`: Used for eval data sets

          expires_after: The expiration policy for a file. By default, files with `purpose=batch` expire
              after 30 days and all other files are persisted until they are manually deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        body = deepcopy_minimal({
            'file': file,
            'purpose': purpose,
            'expires_after': expires_after })
        files = extract_files(cast(Mapping[(str, object)], body), paths = [
            [
                'file']])
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns information about a specific file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
        return self._get(f'''/files/{file_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = FileObject)

    
    def list(self = None, *, after, limit, order, purpose, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of files.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              10,000, and the default is 10,000.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          purpose: Only return files with the given purpose.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/files', page = SyncCursorPage[FileObject], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order,
            'purpose': purpose }, file_list_params.FileListParams)), model = FileObject)

    
    def delete(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a file and remove it from all vector stores.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
        return self._delete(f'''/files/{file_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = FileDeleted)

    
    def content(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns the contents of the specified file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    retrieve_content = (lambda self = None, file_id = None, *, extra_headers, extra_query: if not file_id:
raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')self._get(f'''/files/{file_id}/content''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = str))()
    
    def wait_for_processing(self = None, id = None, *, poll_interval, max_wait_seconds):
        '''Waits for the given file to be processed, default timeout is 30 mins.'''
        TERMINAL_STATES = {
            'error',
            'deleted',
            'processed'}
        start = time.time()
        file = self.retrieve(id)
    # WARNING: Decompyle incomplete



class AsyncFiles(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncFilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFilesWithStreamingResponse(self))()
    
    async def create(self = None, *, file, purpose, expires_after, extra_headers, extra_query, extra_body, timeout):
        '''Upload a file that can be used across various endpoints.

        Individual files can be
        up to 512 MB, and the size of all files uploaded by one organization can be up
        to 1 TB.

        - The Assistants API supports files up to 2 million tokens and of specific file
          types. See the
          [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools)
          for details.
        - The Fine-tuning API only supports `.jsonl` files. The input also has certain
          required formats for fine-tuning
          [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input)
          or
          [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input)
          models.
        - The Batch API only supports `.jsonl` files up to 200 MB in size. The input
          also has a specific required
          [format](https://platform.openai.com/docs/api-reference/batch/request-input).

        Please [contact us](https://help.openai.com/) if you need to increase these
        storage limits.

        Args:
          file: The File object (not file name) to be uploaded.

          purpose: The intended purpose of the uploaded file. One of: - `assistants`: Used in the
              Assistants API - `batch`: Used in the Batch API - `fine-tune`: Used for
              fine-tuning - `vision`: Images used for vision fine-tuning - `user_data`:
              Flexible file type for any purpose - `evals`: Used for eval data sets

          expires_after: The expiration policy for a file. By default, files with `purpose=batch` expire
              after 30 days and all other files are persisted until they are manually deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns information about a specific file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, limit, order, purpose, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of files.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              10,000, and the default is 10,000.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          purpose: Only return files with the given purpose.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/files', page = AsyncCursorPage[FileObject], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order,
            'purpose': purpose }, file_list_params.FileListParams)), model = FileObject)

    
    async def delete(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete a file and remove it from all vector stores.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def content(self = None, file_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Returns the contents of the specified file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    retrieve_content = (lambda self = None, file_id = None, *, extra_headers, extra_query: pass# WARNING: Decompyle incomplete
)()
    
    async def wait_for_processing(self = None, id = None, *, poll_interval, max_wait_seconds):
        '''Waits for the given file to be processed, default timeout is 30 mins.'''
        pass
    # WARNING: Decompyle incomplete



class FilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(files.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.to_raw_response_wrapper(files.delete)
        self.content = _legacy_response.to_raw_response_wrapper(files.content)
        self.retrieve_content = _legacy_response.to_raw_response_wrapper(files.retrieve_content)



class AsyncFilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.async_to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(files.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(files.delete)
        self.content = _legacy_response.async_to_raw_response_wrapper(files.content)
        self.retrieve_content = _legacy_response.async_to_raw_response_wrapper(files.retrieve_content)



class FilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = to_streamed_response_wrapper(files.create)
        self.retrieve = to_streamed_response_wrapper(files.retrieve)
        self.list = to_streamed_response_wrapper(files.list)
        self.delete = to_streamed_response_wrapper(files.delete)
        self.content = to_custom_streamed_response_wrapper(files.content, StreamedBinaryAPIResponse)
        self.retrieve_content = to_streamed_response_wrapper(files.retrieve_content)



class AsyncFilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = async_to_streamed_response_wrapper(files.create)
        self.retrieve = async_to_streamed_response_wrapper(files.retrieve)
        self.list = async_to_streamed_response_wrapper(files.list)
        self.delete = async_to_streamed_response_wrapper(files.delete)
        self.content = async_to_custom_streamed_response_wrapper(files.content, AsyncStreamedBinaryAPIResponse)
        self.retrieve_content = async_to_streamed_response_wrapper(files.retrieve_content)
