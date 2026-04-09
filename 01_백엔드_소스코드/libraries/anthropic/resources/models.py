# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from __future__ import annotations
from typing import List
import httpx
from  import _legacy_response
from types import model_list_params
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import is_given, maybe_transform, strip_not_given
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage
from _base_client import AsyncPaginator, make_request_options
from types.model_info import ModelInfo
from types.anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'Models',
    'AsyncModels']

class Models(SyncAPIResource):
    with_raw_response = (lambda self = None: ModelsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ModelsWithStreamingResponse(self))()
    
    def retrieve(self = None, model_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a specific model.

        The Models API response can be used to determine information about a specific
        model or resolve a model alias to a model ID.

        Args:
          model_id: Model identifier or alias.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not model_id:
            raise ValueError(f'''Expected a non-empty value for `model_id` but received {model_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after_id, before_id, limit, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List available models.

        The Models API response can be used to determine which models are available for
        use in the API. More recently released models are listed first.

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
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



class AsyncModels(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncModelsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncModelsWithStreamingResponse(self))()
    
    async def retrieve(self = None, model_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get a specific model.

        The Models API response can be used to determine information about a specific
        model or resolve a model alias to a model ID.

        Args:
          model_id: Model identifier or alias.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after_id, before_id, limit, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List available models.

        The Models API response can be used to determine which models are available for
        use in the API. More recently released models are listed first.

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
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



class ModelsWithRawResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = _legacy_response.to_raw_response_wrapper(models.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(models.list)



class AsyncModelsWithRawResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(models.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(models.list)



class ModelsWithStreamingResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = to_streamed_response_wrapper(models.retrieve)
        self.list = to_streamed_response_wrapper(models.list)



class AsyncModelsWithStreamingResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = async_to_streamed_response_wrapper(models.retrieve)
        self.list = async_to_streamed_response_wrapper(models.list)
