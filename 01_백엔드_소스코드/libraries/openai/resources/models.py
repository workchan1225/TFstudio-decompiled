# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from __future__ import annotations
import httpx
from  import _legacy_response
from _types import Body, Query, Headers, NotGiven, not_given
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPage, AsyncPage
from types.model import Model
from _base_client import AsyncPaginator, make_request_options
from types.model_deleted import ModelDeleted
__all__ = [
    'Models',
    'AsyncModels']

class Models(SyncAPIResource):
    with_raw_response = (lambda self = None: ModelsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ModelsWithStreamingResponse(self))()
    
    def retrieve(self = None, model = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a model instance, providing basic information about the model such as
        the owner and permissioning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not model:
            raise ValueError(f'''Expected a non-empty value for `model` but received {model!r}''')
        return self._get(f'''/models/{model}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = Model)

    
    def list(self = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Lists the currently available models, and provides basic information about each
        one such as the owner and availability.
        '''
        return self._get_api_list('/models', page = SyncPage[Model], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), model = Model)

    
    def delete(self = None, model = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a fine-tuned model.

        You must have the Owner role in your organization to
        delete a model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not model:
            raise ValueError(f'''Expected a non-empty value for `model` but received {model!r}''')
        return self._delete(f'''/models/{model}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ModelDeleted)



class AsyncModels(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncModelsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncModelsWithStreamingResponse(self))()
    
    async def retrieve(self = None, model = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves a model instance, providing basic information about the model such as
        the owner and permissioning.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Lists the currently available models, and provides basic information about each
        one such as the owner and availability.
        '''
        return self._get_api_list('/models', page = AsyncPage[Model], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), model = Model)

    
    async def delete(self = None, model = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a fine-tuned model.

        You must have the Owner role in your organization to
        delete a model.

        Args:
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
        self.delete = _legacy_response.to_raw_response_wrapper(models.delete)



class AsyncModelsWithRawResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(models.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(models.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(models.delete)



class ModelsWithStreamingResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = to_streamed_response_wrapper(models.retrieve)
        self.list = to_streamed_response_wrapper(models.list)
        self.delete = to_streamed_response_wrapper(models.delete)



class AsyncModelsWithStreamingResponse:
    
    def __init__(self = None, models = None):
        self._models = models
        self.retrieve = async_to_streamed_response_wrapper(models.retrieve)
        self.list = async_to_streamed_response_wrapper(models.list)
        self.delete = async_to_streamed_response_wrapper(models.delete)
