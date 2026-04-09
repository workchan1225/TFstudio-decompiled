# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: containers.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal
import httpx
from  import _legacy_response
from types import container_list_params, container_create_params
from _types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from files.files import Files, AsyncFiles, FilesWithRawResponse, AsyncFilesWithRawResponse, FilesWithStreamingResponse, AsyncFilesWithStreamingResponse
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.container_list_response import ContainerListResponse
from types.container_create_response import ContainerCreateResponse
from types.container_retrieve_response import ContainerRetrieveResponse
__all__ = [
    'Containers',
    'AsyncContainers']

class Containers(SyncAPIResource):
    files = (lambda self = None: Files(self._client))()
    with_raw_response = (lambda self = None: ContainersWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ContainersWithStreamingResponse(self))()
    
    def create(self = None, *, name, expires_after, file_ids, memory_limit, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Container

        Args:
          name: Name of the container to create.

          expires_after: Container expiration time in seconds relative to the \'anchor\' time.

          file_ids: IDs of files to copy to the container.

          memory_limit: Optional memory limit for the container. Defaults to "1g".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/containers', body = maybe_transform({
            'name': name,
            'expires_after': expires_after,
            'file_ids': file_ids,
            'memory_limit': memory_limit }, container_create_params.ContainerCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ContainerCreateResponse)

    
    def retrieve(self = None, container_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
        return self._get(f'''/containers/{container_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ContainerRetrieveResponse)

    
    def list(self = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''List Containers

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
        return self._get_api_list('/containers', page = SyncCursorPage[ContainerListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, container_list_params.ContainerListParams)), model = ContainerListResponse)

    
    def delete(self = None, container_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Container

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not container_id:
            raise ValueError(f'''Expected a non-empty value for `container_id` but received {container_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncContainers(AsyncAPIResource):
    files = (lambda self = None: AsyncFiles(self._client))()
    with_raw_response = (lambda self = None: AsyncContainersWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncContainersWithStreamingResponse(self))()
    
    async def create(self = None, *, name, expires_after, file_ids, memory_limit, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Container

        Args:
          name: Name of the container to create.

          expires_after: Container expiration time in seconds relative to the \'anchor\' time.

          file_ids: IDs of files to copy to the container.

          memory_limit: Optional memory limit for the container. Defaults to "1g".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, container_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieve Container

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''List Containers

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
        return self._get_api_list('/containers', page = AsyncCursorPage[ContainerListResponse], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order }, container_list_params.ContainerListParams)), model = ContainerListResponse)

    
    async def delete(self = None, container_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Container

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class ContainersWithRawResponse:
    
    def __init__(self = None, containers = None):
        self._containers = containers
        self.create = _legacy_response.to_raw_response_wrapper(containers.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(containers.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(containers.list)
        self.delete = _legacy_response.to_raw_response_wrapper(containers.delete)

    files = (lambda self = None: FilesWithRawResponse(self._containers.files))()


class AsyncContainersWithRawResponse:
    
    def __init__(self = None, containers = None):
        self._containers = containers
        self.create = _legacy_response.async_to_raw_response_wrapper(containers.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(containers.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(containers.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(containers.delete)

    files = (lambda self = None: AsyncFilesWithRawResponse(self._containers.files))()


class ContainersWithStreamingResponse:
    
    def __init__(self = None, containers = None):
        self._containers = containers
        self.create = to_streamed_response_wrapper(containers.create)
        self.retrieve = to_streamed_response_wrapper(containers.retrieve)
        self.list = to_streamed_response_wrapper(containers.list)
        self.delete = to_streamed_response_wrapper(containers.delete)

    files = (lambda self = None: FilesWithStreamingResponse(self._containers.files))()


class AsyncContainersWithStreamingResponse:
    
    def __init__(self = None, containers = None):
        self._containers = containers
        self.create = async_to_streamed_response_wrapper(containers.create)
        self.retrieve = async_to_streamed_response_wrapper(containers.retrieve)
        self.list = async_to_streamed_response_wrapper(containers.list)
        self.delete = async_to_streamed_response_wrapper(containers.delete)

    files = (lambda self = None: AsyncFilesWithStreamingResponse(self._containers.files))()
