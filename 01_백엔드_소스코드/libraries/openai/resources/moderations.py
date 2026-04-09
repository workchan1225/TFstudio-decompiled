# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderations.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
import httpx
from  import _legacy_response
from types import moderation_create_params
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.moderation_model import ModerationModel
from types.moderation_create_response import ModerationCreateResponse
from types.moderation_multi_modal_input_param import ModerationMultiModalInputParam
__all__ = [
    'Moderations',
    'AsyncModerations']

class Moderations(SyncAPIResource):
    with_raw_response = (lambda self = None: ModerationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ModerationsWithStreamingResponse(self))()
    
    def create(self = None, *, input, model, extra_headers, extra_query, extra_body, timeout):
        '''Classifies if text and/or image inputs are potentially harmful.

        Learn more in
        the [moderation guide](https://platform.openai.com/docs/guides/moderation).

        Args:
          input: Input (or inputs) to classify. Can be a single string, an array of strings, or
              an array of multi-modal input objects similar to other models.

          model: The content moderation model you would like to use. Learn more in
              [the moderation guide](https://platform.openai.com/docs/guides/moderation), and
              learn about available models
              [here](https://platform.openai.com/docs/models#moderation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/moderations', body = maybe_transform({
            'input': input,
            'model': model }, moderation_create_params.ModerationCreateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ModerationCreateResponse)



class AsyncModerations(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncModerationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncModerationsWithStreamingResponse(self))()
    
    async def create(self = None, *, input, model, extra_headers, extra_query, extra_body, timeout):
        '''Classifies if text and/or image inputs are potentially harmful.

        Learn more in
        the [moderation guide](https://platform.openai.com/docs/guides/moderation).

        Args:
          input: Input (or inputs) to classify. Can be a single string, an array of strings, or
              an array of multi-modal input objects similar to other models.

          model: The content moderation model you would like to use. Learn more in
              [the moderation guide](https://platform.openai.com/docs/guides/moderation), and
              learn about available models
              [here](https://platform.openai.com/docs/models#moderation).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class ModerationsWithRawResponse:
    
    def __init__(self = None, moderations = None):
        self._moderations = moderations
        self.create = _legacy_response.to_raw_response_wrapper(moderations.create)



class AsyncModerationsWithRawResponse:
    
    def __init__(self = None, moderations = None):
        self._moderations = moderations
        self.create = _legacy_response.async_to_raw_response_wrapper(moderations.create)



class ModerationsWithStreamingResponse:
    
    def __init__(self = None, moderations = None):
        self._moderations = moderations
        self.create = to_streamed_response_wrapper(moderations.create)



class AsyncModerationsWithStreamingResponse:
    
    def __init__(self = None, moderations = None):
        self._moderations = moderations
        self.create = async_to_streamed_response_wrapper(moderations.create)
