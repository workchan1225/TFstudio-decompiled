# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: graders.pyc (Python 3.11)

from __future__ import annotations
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.fine_tuning.alpha import grader_run_params, grader_validate_params
from types.fine_tuning.alpha.grader_run_response import GraderRunResponse
from types.fine_tuning.alpha.grader_validate_response import GraderValidateResponse
__all__ = [
    'Graders',
    'AsyncGraders']

class Graders(SyncAPIResource):
    with_raw_response = (lambda self = None: GradersWithRawResponse(self))()
    with_streaming_response = (lambda self = None: GradersWithStreamingResponse(self))()
    
    def run(self = None, *, grader, model_sample, item, extra_headers, extra_query, extra_body, timeout):
        '''
        Run a grader.

        Args:
          grader: The grader used for the fine-tuning job.

          model_sample: The model sample to be evaluated. This value will be used to populate the
              `sample` namespace. See
              [the guide](https://platform.openai.com/docs/guides/graders) for more details.
              The `output_json` variable will be populated if the model sample is a valid JSON
              string.

          item: The dataset item provided to the grader. This will be used to populate the
              `item` namespace. See
              [the guide](https://platform.openai.com/docs/guides/graders) for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/fine_tuning/alpha/graders/run', body = maybe_transform({
            'grader': grader,
            'model_sample': model_sample,
            'item': item }, grader_run_params.GraderRunParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = GraderRunResponse)

    
    def validate(self = None, *, grader, extra_headers, extra_query, extra_body, timeout):
        '''
        Validate a grader.

        Args:
          grader: The grader used for the fine-tuning job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._post('/fine_tuning/alpha/graders/validate', body = maybe_transform({
            'grader': grader }, grader_validate_params.GraderValidateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = GraderValidateResponse)



class AsyncGraders(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncGradersWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncGradersWithStreamingResponse(self))()
    
    async def run(self = None, *, grader, model_sample, item, extra_headers, extra_query, extra_body, timeout):
        '''
        Run a grader.

        Args:
          grader: The grader used for the fine-tuning job.

          model_sample: The model sample to be evaluated. This value will be used to populate the
              `sample` namespace. See
              [the guide](https://platform.openai.com/docs/guides/graders) for more details.
              The `output_json` variable will be populated if the model sample is a valid JSON
              string.

          item: The dataset item provided to the grader. This will be used to populate the
              `item` namespace. See
              [the guide](https://platform.openai.com/docs/guides/graders) for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def validate(self = None, *, grader, extra_headers, extra_query, extra_body, timeout):
        '''
        Validate a grader.

        Args:
          grader: The grader used for the fine-tuning job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class GradersWithRawResponse:
    
    def __init__(self = None, graders = None):
        self._graders = graders
        self.run = _legacy_response.to_raw_response_wrapper(graders.run)
        self.validate = _legacy_response.to_raw_response_wrapper(graders.validate)



class AsyncGradersWithRawResponse:
    
    def __init__(self = None, graders = None):
        self._graders = graders
        self.run = _legacy_response.async_to_raw_response_wrapper(graders.run)
        self.validate = _legacy_response.async_to_raw_response_wrapper(graders.validate)



class GradersWithStreamingResponse:
    
    def __init__(self = None, graders = None):
        self._graders = graders
        self.run = to_streamed_response_wrapper(graders.run)
        self.validate = to_streamed_response_wrapper(graders.validate)



class AsyncGradersWithStreamingResponse:
    
    def __init__(self = None, graders = None):
        self._graders = graders
        self.run = async_to_streamed_response_wrapper(graders.run)
        self.validate = async_to_streamed_response_wrapper(graders.validate)
