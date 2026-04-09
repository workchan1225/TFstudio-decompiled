# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permissions.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage
from _base_client import AsyncPaginator, make_request_options
from types.fine_tuning.checkpoints import permission_create_params, permission_retrieve_params
from types.fine_tuning.checkpoints.permission_create_response import PermissionCreateResponse
from types.fine_tuning.checkpoints.permission_delete_response import PermissionDeleteResponse
from types.fine_tuning.checkpoints.permission_retrieve_response import PermissionRetrieveResponse
__all__ = [
    'Permissions',
    'AsyncPermissions']

class Permissions(SyncAPIResource):
    with_raw_response = (lambda self = None: PermissionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: PermissionsWithStreamingResponse(self))()
    
    def create(self = None, fine_tuned_model_checkpoint = None, *, project_ids, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

        This enables organization owners to share fine-tuned models with other projects
        in their organization.

        Args:
          project_ids: The project identifiers to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuned_model_checkpoint:
            raise ValueError(f'''Expected a non-empty value for `fine_tuned_model_checkpoint` but received {fine_tuned_model_checkpoint!r}''')
        return self._get_api_list(f'''/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions''', page = SyncPage[PermissionCreateResponse], body = maybe_transform({
            'project_ids': project_ids }, permission_create_params.PermissionCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), model = PermissionCreateResponse, method = 'post')

    
    def retrieve(self = None, fine_tuned_model_checkpoint = None, *, after, limit, order, project_id, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to view all permissions for a
        fine-tuned model checkpoint.

        Args:
          after: Identifier for the last permission ID from the previous pagination request.

          limit: Number of permissions to retrieve.

          order: The order in which to retrieve permissions.

          project_id: The ID of the project to get permissions for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuned_model_checkpoint:
            raise ValueError(f'''Expected a non-empty value for `fine_tuned_model_checkpoint` but received {fine_tuned_model_checkpoint!r}''')
        return self._get(f'''/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'order': order,
            'project_id': project_id }, permission_retrieve_params.PermissionRetrieveParams)), cast_to = PermissionRetrieveResponse)

    
    def delete(self = None, permission_id = None, *, fine_tuned_model_checkpoint, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to delete a permission for a
        fine-tuned model checkpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuned_model_checkpoint:
            raise ValueError(f'''Expected a non-empty value for `fine_tuned_model_checkpoint` but received {fine_tuned_model_checkpoint!r}''')
        if not permission_id:
            raise ValueError(f'''Expected a non-empty value for `permission_id` but received {permission_id!r}''')
        return self._delete(f'''/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = PermissionDeleteResponse)



class AsyncPermissions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncPermissionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncPermissionsWithStreamingResponse(self))()
    
    def create(self = None, fine_tuned_model_checkpoint = None, *, project_ids, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

        This enables organization owners to share fine-tuned models with other projects
        in their organization.

        Args:
          project_ids: The project identifiers to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuned_model_checkpoint:
            raise ValueError(f'''Expected a non-empty value for `fine_tuned_model_checkpoint` but received {fine_tuned_model_checkpoint!r}''')
        return self._get_api_list(f'''/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions''', page = AsyncPage[PermissionCreateResponse], body = maybe_transform({
            'project_ids': project_ids }, permission_create_params.PermissionCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), model = PermissionCreateResponse, method = 'post')

    
    async def retrieve(self = None, fine_tuned_model_checkpoint = None, *, after, limit, order, project_id, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to view all permissions for a
        fine-tuned model checkpoint.

        Args:
          after: Identifier for the last permission ID from the previous pagination request.

          limit: Number of permissions to retrieve.

          order: The order in which to retrieve permissions.

          project_id: The ID of the project to get permissions for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, permission_id = None, *, fine_tuned_model_checkpoint, extra_headers, extra_query, extra_body, timeout):
        '''
        **NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

        Organization owners can use this endpoint to delete a permission for a
        fine-tuned model checkpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class PermissionsWithRawResponse:
    
    def __init__(self = None, permissions = None):
        self._permissions = permissions
        self.create = _legacy_response.to_raw_response_wrapper(permissions.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(permissions.retrieve)
        self.delete = _legacy_response.to_raw_response_wrapper(permissions.delete)



class AsyncPermissionsWithRawResponse:
    
    def __init__(self = None, permissions = None):
        self._permissions = permissions
        self.create = _legacy_response.async_to_raw_response_wrapper(permissions.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(permissions.retrieve)
        self.delete = _legacy_response.async_to_raw_response_wrapper(permissions.delete)



class PermissionsWithStreamingResponse:
    
    def __init__(self = None, permissions = None):
        self._permissions = permissions
        self.create = to_streamed_response_wrapper(permissions.create)
        self.retrieve = to_streamed_response_wrapper(permissions.retrieve)
        self.delete = to_streamed_response_wrapper(permissions.delete)



class AsyncPermissionsWithStreamingResponse:
    
    def __init__(self = None, permissions = None):
        self._permissions = permissions
        self.create = async_to_streamed_response_wrapper(permissions.create)
        self.retrieve = async_to_streamed_response_wrapper(permissions.retrieve)
        self.delete = async_to_streamed_response_wrapper(permissions.delete)
