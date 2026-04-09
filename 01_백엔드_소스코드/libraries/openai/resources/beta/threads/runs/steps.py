# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: steps.pyc (Python 3.11)

from __future__ import annotations
import typing_extensions
from typing import List
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from types.beta.threads.runs import step_list_params, step_retrieve_params
from types.beta.threads.runs.run_step import RunStep
from types.beta.threads.runs.run_step_include import RunStepInclude
__all__ = [
    'Steps',
    'AsyncSteps']

class Steps(SyncAPIResource):
    with_raw_response = (lambda self = None: StepsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: StepsWithStreamingResponse(self))()
    retrieve = (lambda self = None, step_id = None, *, thread_id, run_id: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')if not step_id:
raise ValueError(f'''Expected a non-empty value for `step_id` but received {step_id!r}''')# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, run_id = None, *, thread_id, after: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()


class AsyncSteps(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncStepsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncStepsWithStreamingResponse(self))()
    retrieve = (lambda self = None, step_id = None, *, thread_id, run_id: pass# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, run_id = None, *, thread_id, after: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()


class StepsWithRawResponse:
    
    def __init__(self = None, steps = None):
        self._steps = steps
        self.retrieve = _legacy_response.to_raw_response_wrapper(steps.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(steps.list)



class AsyncStepsWithRawResponse:
    
    def __init__(self = None, steps = None):
        self._steps = steps
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(steps.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(steps.list)



class StepsWithStreamingResponse:
    
    def __init__(self = None, steps = None):
        self._steps = steps
        self.retrieve = to_streamed_response_wrapper(steps.retrieve)
        self.list = to_streamed_response_wrapper(steps.list)



class AsyncStepsWithStreamingResponse:
    
    def __init__(self = None, steps = None):
        self._steps = steps
        self.retrieve = async_to_streamed_response_wrapper(steps.retrieve)
        self.list = async_to_streamed_response_wrapper(steps.list)
