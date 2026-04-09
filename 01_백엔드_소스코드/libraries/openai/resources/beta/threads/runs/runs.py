# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runs.pyc (Python 3.11)

from __future__ import annotations
import typing_extensions
from typing import List, Union, Iterable, Optional
from functools import partial
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from steps import Steps, AsyncSteps, StepsWithRawResponse, AsyncStepsWithRawResponse, StepsWithStreamingResponse, AsyncStepsWithStreamingResponse
from _types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import is_given, required_args, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from pagination import SyncCursorPage, AsyncCursorPage
from _base_client import AsyncPaginator, make_request_options
from lib.streaming import AssistantEventHandler, AssistantEventHandlerT, AssistantStreamManager, AsyncAssistantEventHandler, AsyncAssistantEventHandlerT, AsyncAssistantStreamManager
from types.beta.threads import run_list_params, run_create_params, run_update_params, run_submit_tool_outputs_params
from types.beta.threads.run import Run
from types.shared.chat_model import ChatModel
from types.shared_params.metadata import Metadata
from types.shared.reasoning_effort import ReasoningEffort
from types.beta.assistant_tool_param import AssistantToolParam
from types.beta.assistant_stream_event import AssistantStreamEvent
from types.beta.threads.runs.run_step_include import RunStepInclude
from types.beta.assistant_tool_choice_option_param import AssistantToolChoiceOptionParam
from types.beta.assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'Runs',
    'AsyncRuns']

class Runs(SyncAPIResource):
    steps = (lambda self = None: Steps(self._client))()
    with_raw_response = (lambda self = None: RunsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: RunsWithStreamingResponse(self))()
    create = (lambda self = None, thread_id = None, *, assistant_id, include: pass)()()
    create = (lambda self = None, thread_id = None, *, assistant_id, stream: pass)()()
    create = (lambda self = None, thread_id = None, *, assistant_id, stream: pass)()()
    create = (lambda self = None, thread_id = None, *, assistant_id, include: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()()
    retrieve = (lambda self = None, run_id = None, *, thread_id, extra_headers: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, run_id = None, *, thread_id, metadata: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, thread_id = None, *, after, before: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    cancel = (lambda self = None, run_id = None, *, thread_id, extra_headers: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()
    create_and_poll = (lambda self = None, *, assistant_id: run = self.create(thread_id = thread_id, assistant_id = assistant_id, include = include, additional_instructions = additional_instructions, additional_messages = additional_messages, instructions = instructions, max_completion_tokens = max_completion_tokens, max_prompt_tokens = max_prompt_tokens, metadata = metadata, model = model, response_format = response_format, temperature = temperature, tool_choice = tool_choice, parallel_tool_calls = parallel_tool_calls, reasoning_effort = reasoning_effort, stream = False, tools = tools, truncation_strategy = truncation_strategy, top_p = top_p, extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout)self.poll(run.id, thread_id = thread_id, extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, poll_interval_ms = poll_interval_ms, timeout = timeout))()
    create_and_stream = (lambda self = None, *, assistant_id: pass)()()
    create_and_stream = (lambda self = None, *, assistant_id: pass)()()
    create_and_stream = (lambda self = None, *, assistant_id: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    poll = (lambda self, run_id, thread_id, extra_headers = None, extra_query = None, extra_body = typing_extensions.deprecated('The Assistants API is deprecated in favor of the Responses API'), timeout = (None, None, None, not_given, omit), poll_interval_ms = ('run_id', 'str', 'thread_id', 'str', 'extra_headers', 'Headers | None', 'extra_query', 'Query | None', 'extra_body', 'Body | None', 'timeout', 'float | httpx.Timeout | None | NotGiven', 'poll_interval_ms', 'int | Omit', 'return', 'Run'): pass# WARNING: Decompyle incomplete
)()
    stream = (lambda self = None, *, assistant_id: pass)()()
    stream = (lambda self = None, *, assistant_id: pass)()()
    stream = (lambda self = None, *, assistant_id: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, tool_outputs: pass)()()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, stream: pass)()()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, stream: pass)()()
    submit_tool_outputs = (lambda self = None, run_id = typing_extensions.deprecated('The Assistants API is deprecated in favor of the Responses API'), *, thread_id, tool_outputs: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')# WARNING: Decompyle incomplete
)()()()
    submit_tool_outputs_and_poll = (lambda self = None, *, tool_outputs: run = self.submit_tool_outputs(run_id = run_id, thread_id = thread_id, tool_outputs = tool_outputs, stream = False, extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout)self.poll(run_id = run.id, thread_id = thread_id, extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, poll_interval_ms = poll_interval_ms))()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: pass)()()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: pass)()()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()


class AsyncRuns(AsyncAPIResource):
    steps = (lambda self = None: AsyncSteps(self._client))()
    with_raw_response = (lambda self = None: AsyncRunsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncRunsWithStreamingResponse(self))()
    create = (lambda self = None, thread_id = None, *, assistant_id, include: pass# WARNING: Decompyle incomplete
)()()
    create = (lambda self = None, thread_id = None, *, assistant_id, stream: pass# WARNING: Decompyle incomplete
)()()
    create = (lambda self = None, thread_id = None, *, assistant_id, stream: pass# WARNING: Decompyle incomplete
)()()
    create = (lambda self = None, thread_id = typing_extensions.deprecated('The Assistants API is deprecated in favor of the Responses API'), *, assistant_id, include: pass# WARNING: Decompyle incomplete
)()()()
    retrieve = (lambda self = None, run_id = None, *, thread_id, extra_headers: pass# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, run_id = None, *, thread_id, metadata: pass# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, thread_id = None, *, after, before: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    cancel = (lambda self = None, run_id = None, *, thread_id, extra_headers: pass# WARNING: Decompyle incomplete
)()
    create_and_poll = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()
    create_and_stream = (lambda self = None, *, assistant_id: pass)()()
    create_and_stream = (lambda self = None, *, assistant_id: pass)()()
    create_and_stream = (lambda self = None, *, assistant_id: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    poll = (lambda self, run_id, thread_id, extra_headers = None, extra_query = None, extra_body = typing_extensions.deprecated('The Assistants API is deprecated in favor of the Responses API'), timeout = (None, None, None, not_given, omit), poll_interval_ms = ('run_id', 'str', 'thread_id', 'str', 'extra_headers', 'Headers | None', 'extra_query', 'Query | None', 'extra_body', 'Body | None', 'timeout', 'float | httpx.Timeout | None | NotGiven', 'poll_interval_ms', 'int | Omit', 'return', 'Run'): pass# WARNING: Decompyle incomplete
)()
    stream = (lambda self = None, *, assistant_id: pass)()()
    stream = (lambda self = None, *, assistant_id: pass)()()
    stream = (lambda self = None, *, assistant_id: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, tool_outputs: pass# WARNING: Decompyle incomplete
)()()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, stream: pass# WARNING: Decompyle incomplete
)()()
    submit_tool_outputs = (lambda self = None, run_id = None, *, thread_id, stream: pass# WARNING: Decompyle incomplete
)()()
    submit_tool_outputs = (lambda self = None, run_id = typing_extensions.deprecated('The Assistants API is deprecated in favor of the Responses API'), *, thread_id, tool_outputs: pass# WARNING: Decompyle incomplete
)()()()
    submit_tool_outputs_and_poll = (lambda self = None, *, tool_outputs: pass# WARNING: Decompyle incomplete
)()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: pass)()()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: pass)()()
    submit_tool_outputs_stream = (lambda self = None, *, tool_outputs: if not run_id:
raise ValueError(f'''Expected a non-empty value for `run_id` but received {run_id!r}''')if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()


class RunsWithRawResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = _legacy_response.to_raw_response_wrapper(runs.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(runs.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(runs.update)
        self.list = _legacy_response.to_raw_response_wrapper(runs.list)
        self.cancel = _legacy_response.to_raw_response_wrapper(runs.cancel)
        self.submit_tool_outputs = _legacy_response.to_raw_response_wrapper(runs.submit_tool_outputs)

    steps = (lambda self = None: StepsWithRawResponse(self._runs.steps))()


class AsyncRunsWithRawResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = _legacy_response.async_to_raw_response_wrapper(runs.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(runs.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(runs.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(runs.list)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(runs.cancel)
        self.submit_tool_outputs = _legacy_response.async_to_raw_response_wrapper(runs.submit_tool_outputs)

    steps = (lambda self = None: AsyncStepsWithRawResponse(self._runs.steps))()


class RunsWithStreamingResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = to_streamed_response_wrapper(runs.create)
        self.retrieve = to_streamed_response_wrapper(runs.retrieve)
        self.update = to_streamed_response_wrapper(runs.update)
        self.list = to_streamed_response_wrapper(runs.list)
        self.cancel = to_streamed_response_wrapper(runs.cancel)
        self.submit_tool_outputs = to_streamed_response_wrapper(runs.submit_tool_outputs)

    steps = (lambda self = None: StepsWithStreamingResponse(self._runs.steps))()


class AsyncRunsWithStreamingResponse:
    
    def __init__(self = None, runs = None):
        self._runs = runs
        self.create = async_to_streamed_response_wrapper(runs.create)
        self.retrieve = async_to_streamed_response_wrapper(runs.retrieve)
        self.update = async_to_streamed_response_wrapper(runs.update)
        self.list = async_to_streamed_response_wrapper(runs.list)
        self.cancel = async_to_streamed_response_wrapper(runs.cancel)
        self.submit_tool_outputs = async_to_streamed_response_wrapper(runs.submit_tool_outputs)

    steps = (lambda self = None: AsyncStepsWithStreamingResponse(self._runs.steps))()
