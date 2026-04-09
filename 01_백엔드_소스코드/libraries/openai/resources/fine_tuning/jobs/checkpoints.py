# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: checkpoints.pyc (Python 3.11)

from __future__ import annotations
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.fine_tuning.jobs import checkpoint_list_params
from types.fine_tuning.jobs.fine_tuning_job_checkpoint import FineTuningJobCheckpoint
__all__ = [
    'Checkpoints',
    'AsyncCheckpoints']

class Checkpoints(SyncAPIResource):
    with_raw_response = (lambda self = None: CheckpointsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: CheckpointsWithStreamingResponse(self))()
    
    def list(self = None, fine_tuning_job_id = None, *, after, limit, extra_headers, extra_query, extra_body, timeout):
        '''
        List checkpoints for a fine-tuning job.

        Args:
          after: Identifier for the last checkpoint ID from the previous pagination request.

          limit: Number of checkpoints to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuning_job_id:
            raise ValueError(f'''Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}''')
        return self._get_api_list(f'''/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints''', page = SyncCursorPage[FineTuningJobCheckpoint], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit }, checkpoint_list_params.CheckpointListParams)), model = FineTuningJobCheckpoint)



class AsyncCheckpoints(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncCheckpointsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncCheckpointsWithStreamingResponse(self))()
    
    def list(self = None, fine_tuning_job_id = None, *, after, limit, extra_headers, extra_query, extra_body, timeout):
        '''
        List checkpoints for a fine-tuning job.

        Args:
          after: Identifier for the last checkpoint ID from the previous pagination request.

          limit: Number of checkpoints to retrieve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not fine_tuning_job_id:
            raise ValueError(f'''Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}''')
        return self._get_api_list(f'''/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints''', page = AsyncCursorPage[FineTuningJobCheckpoint], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit }, checkpoint_list_params.CheckpointListParams)), model = FineTuningJobCheckpoint)



class CheckpointsWithRawResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints
        self.list = _legacy_response.to_raw_response_wrapper(checkpoints.list)



class AsyncCheckpointsWithRawResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints
        self.list = _legacy_response.async_to_raw_response_wrapper(checkpoints.list)



class CheckpointsWithStreamingResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints
        self.list = to_streamed_response_wrapper(checkpoints.list)



class AsyncCheckpointsWithStreamingResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints
        self.list = async_to_streamed_response_wrapper(checkpoints.list)
