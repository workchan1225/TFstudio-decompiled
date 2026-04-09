# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Mapping, cast
from itertools import chain
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from _utils import is_given, extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import BinaryAPIResponse, AsyncBinaryAPIResponse, StreamedBinaryAPIResponse, AsyncStreamedBinaryAPIResponse, to_streamed_response_wrapper, to_custom_raw_response_wrapper, async_to_streamed_response_wrapper, to_custom_streamed_response_wrapper, async_to_custom_raw_response_wrapper, async_to_custom_streamed_response_wrapper
from pagination import SyncPage, AsyncPage
from types.beta import file_list_params, file_upload_params
from _base_client import AsyncPaginator, make_request_options
from types.beta.deleted_file import DeletedFile
from types.beta.file_metadata import FileMetadata
from types.anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'Files',
    'AsyncFiles']

class Files(SyncAPIResource):
    with_raw_response = (lambda self = None: FilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FilesWithStreamingResponse(self))()
    
    def list(self = None, *, after_id, before_id, limit, betas, extra_headers, extra_query, extra_body, timeout):
        '''List Files

        Args:
          after_id: ID of the object to use as a cursor for pagination.

        When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete File

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def download(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Download File

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def retrieve_metadata(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get File Metadata

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not file_id:
            raise ValueError(f'''Expected a non-empty value for `file_id` but received {file_id!r}''')
    # WARNING: Decompyle incomplete

    
    def upload(self = None, *, file, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Upload File

        Args:
          file: The file to upload

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncFiles(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncFilesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFilesWithStreamingResponse(self))()
    
    def list(self = None, *, after_id, before_id, limit, betas, extra_headers, extra_query, extra_body, timeout):
        '''List Files

        Args:
          after_id: ID of the object to use as a cursor for pagination.

        When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete File

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def download(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Download File

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve_metadata(self = None, file_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get File Metadata

        Args:
          file_id: ID of the File.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def upload(self = None, *, file, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Upload File

        Args:
          file: The file to upload

          betas: Optional header to specify the beta version(s) you want to use.

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
        self.list = _legacy_response.to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.to_raw_response_wrapper(files.delete)
        self.download = to_custom_raw_response_wrapper(files.download, BinaryAPIResponse)
        self.retrieve_metadata = _legacy_response.to_raw_response_wrapper(files.retrieve_metadata)
        self.upload = _legacy_response.to_raw_response_wrapper(files.upload)



class AsyncFilesWithRawResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.list = _legacy_response.async_to_raw_response_wrapper(files.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(files.delete)
        self.download = async_to_custom_raw_response_wrapper(files.download, AsyncBinaryAPIResponse)
        self.retrieve_metadata = _legacy_response.async_to_raw_response_wrapper(files.retrieve_metadata)
        self.upload = _legacy_response.async_to_raw_response_wrapper(files.upload)



class FilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.list = to_streamed_response_wrapper(files.list)
        self.delete = to_streamed_response_wrapper(files.delete)
        self.download = to_custom_streamed_response_wrapper(files.download, StreamedBinaryAPIResponse)
        self.retrieve_metadata = to_streamed_response_wrapper(files.retrieve_metadata)
        self.upload = to_streamed_response_wrapper(files.upload)



class AsyncFilesWithStreamingResponse:
    
    def __init__(self = None, files = None):
        self._files = files
        self.list = async_to_streamed_response_wrapper(files.list)
        self.delete = async_to_streamed_response_wrapper(files.delete)
        self.download = async_to_custom_streamed_response_wrapper(files.download, AsyncStreamedBinaryAPIResponse)
        self.retrieve_metadata = async_to_streamed_response_wrapper(files.retrieve_metadata)
        self.upload = async_to_streamed_response_wrapper(files.upload)
