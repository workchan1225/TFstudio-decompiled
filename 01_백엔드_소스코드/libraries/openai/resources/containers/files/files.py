# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import annotations
from typing import Mapping, cast
from typing_extensions import Literal
import httpx
from  import _legacy_response
from content import Content, AsyncContent, ContentWithRawResponse, AsyncContentWithRawResponse, ContentWithStreamingResponse, AsyncContentWithStreamingResponse
from _types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from _utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.containers import file_list_params, file_create_params
from types.containers.file_list_response import FileListResponse
from types.containers.file_create_response import FileCreateResponse
from types.containers.file_retrieve_response import FileRetrieveResponse
__all__ = [
    'Files',
    'AsyncFiles']

class Files(SyncAPIResource):
    content = (lambda self = None: Content(self._client))()
    with_raw_response = (lambda self = None: FilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FilesWithStreamingResponse(self))()
    
    def create(self = None, container_id = None, *, file, file_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a Container File

        You can send either a multipart/form-data request with the raw file content, or
        a JSON request with a file ID.

        Args:
          file: The File object (not file name) to be uploaded.

          file_id: Name of the file to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
        body = deepcopy_minimal({
            'file': file,
            'file_id': file_id })
        files = extract_files(cast(Mapping[(str, object)], body), paths = [
            [
                'file']])
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container File

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
        return self._get(f'''/containers/{container_id}/files/{file_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = FileRetrieveResponse)

    
    def list(self = None, container_id = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''List Container files

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
        return self._get_api_list(f'''/containers/{container_id}/files''', page = SyncCursorPage[FileListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, file_list_params.FileListParams)), model = FileListResponse)

    
    def delete(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Container File

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



class AsyncFiles(AsyncAPIResource):
    content = (lambda self = None: AsyncContent(self._client))()
    with_raw_response = (lambda self = None: AsyncFilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFilesWithStreamingResponse(self))()
    
    async def create(self = None, container_id = None, *, file, file_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a Container File

        You can send either a multipart/form-data request with the raw file content, or
        a JSON request with a file ID.

        Args:
          file: The File object (not file name) to be uploaded.

          file_id: Name of the file to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, container_id = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''List Container files

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
        return self._get_api_list(f'''/containers/{container_id}/files''', page = AsyncCursorPage[FileListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, file_list_params.FileListParams)), model = FileListResponse)

    
    async def delete(self = None, file_id = None, *, container_id, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Container File

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class FilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(files.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.to_raw_response_wrapper(files.delete)

    content = (lambda self = None: ContentWithRawResponse(self._files.content))()


class AsyncFilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = _legacy_response.async_to_raw_response_wrapper(files.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(files.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(files.delete)

    content = (lambda self = None: AsyncContentWithRawResponse(self._files.content))()


class FilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = to_streamed_response_wrapper(files.create)
        self.retrieve = to_streamed_response_wrapper(files.retrieve)
        self.list = to_streamed_response_wrapper(files.list)
        self.delete = to_streamed_response_wrapper(files.delete)

    content = (lambda self = None: ContentWithStreamingResponse(self._files.content))()


class AsyncFilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.create = async_to_streamed_response_wrapper(files.create)
        self.retrieve = async_to_streamed_response_wrapper(files.retrieve)
        self.list = async_to_streamed_response_wrapper(files.list)
        self.delete = async_to_streamed_response_wrapper(files.delete)

    content = (lambda self = None: AsyncContentWithStreamingResponse(self._files.content))()
