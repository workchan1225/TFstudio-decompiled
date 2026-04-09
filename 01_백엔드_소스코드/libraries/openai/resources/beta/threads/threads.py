# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: threads.pyc (Python 3.11)

from __future__ import annotations
import typing_extensions
from typing import Union, Iterable, Optional
from functools import partial
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from messages import Messages, AsyncMessages, MessagesWithRawResponse, AsyncMessagesWithRawResponse, MessagesWithStreamingResponse, AsyncMessagesWithStreamingResponse
from _types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import required_args, maybe_transform, async_maybe_transform
from runs.runs import Runs, AsyncRuns, RunsWithRawResponse, AsyncRunsWithRawResponse, RunsWithStreamingResponse, AsyncRunsWithStreamingResponse
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from types.beta import thread_create_params, thread_update_params, thread_create_and_run_params
from _base_client import make_request_options
from lib.streaming import AssistantEventHandler, AssistantEventHandlerT, AssistantStreamManager, AsyncAssistantEventHandler, AsyncAssistantEventHandlerT, AsyncAssistantStreamManager
from types.beta.thread import Thread
from types.beta.threads.run import Run
from types.shared.chat_model import ChatModel
from types.beta.thread_deleted import ThreadDeleted
from types.shared_params.metadata import Metadata
from types.beta.assistant_tool_param import AssistantToolParam
from types.beta.assistant_stream_event import AssistantStreamEvent
from types.beta.assistant_tool_choice_option_param import AssistantToolChoiceOptionParam
from types.beta.assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'Threads',
    'AsyncThreads']

class Threads(SyncAPIResource):
    runs = (lambda self = None: Runs(self._client))()
    messages = (lambda self = None: Messages(self._client))()
    with_raw_response = (lambda self = None: ThreadsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ThreadsWithStreamingResponse(self))()
    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    retrieve = (lambda self = None, thread_id = None, *, extra_headers, extra_query: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, thread_id = None, *, metadata, tool_resources: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    delete = (lambda self = None, thread_id = None, *, extra_headers, extra_query: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    create_and_run = (lambda self = None, *, assistant_id: pass)()()
    create_and_run = (lambda self = None, *, assistant_id: pass)()()
    create_and_run = (lambda self = None, *, assistant_id: pass)()()
    create_and_run = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()()()
    
    def create_and_run_poll(self = None, *, assistant_id, instructions, max_completion_tokens, max_prompt_tokens, metadata, model, parallel_tool_calls, response_format, temperature, thread, tool_choice, tool_resources, tools, top_p, truncation_strategy, poll_interval_ms, extra_headers, extra_query, extra_body, timeout):
        '''
        A helper to create a thread, start a run and then poll for a terminal state.
        More information on Run lifecycles can be found here:
        https://platform.openai.com/docs/assistants/how-it-works/runs-and-run-steps
        '''
        run = self.create_and_run(assistant_id = assistant_id, instructions = instructions, max_completion_tokens = max_completion_tokens, max_prompt_tokens = max_prompt_tokens, metadata = metadata, model = model, parallel_tool_calls = parallel_tool_calls, response_format = response_format, temperature = temperature, stream = False, thread = thread, tool_resources = tool_resources, tool_choice = tool_choice, truncation_strategy = truncation_strategy, top_p = top_p, tools = tools, extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout)
        return self.runs.poll(run.id, run.thread_id, extra_headers, extra_query, extra_body, timeout, poll_interval_ms)

    create_and_run_stream = (lambda self = None, *, assistant_id: pass)()
    create_and_run_stream = (lambda self = None, *, assistant_id: pass)()
    
    def create_and_run_stream(self = None, *, assistant_id, instructions, max_completion_tokens, max_prompt_tokens, metadata, model, parallel_tool_calls, response_format, temperature, thread, tool_choice, tool_resources, tools, top_p, truncation_strategy, event_handler, extra_headers, extra_query, extra_body, timeout):
        '''Create a thread and stream the run back'''
        pass
    # WARNING: Decompyle incomplete



class AsyncThreads(AsyncAPIResource):
    runs = (lambda self = None: AsyncRuns(self._client))()
    messages = (lambda self = None: AsyncMessages(self._client))()
    with_raw_response = (lambda self = None: AsyncThreadsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncThreadsWithStreamingResponse(self))()
    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    retrieve = (lambda self = None, thread_id = None, *, extra_headers, extra_query: pass# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, thread_id = None, *, metadata, tool_resources: pass# WARNING: Decompyle incomplete
)()
    delete = (lambda self = None, thread_id = None, *, extra_headers, extra_query: pass# WARNING: Decompyle incomplete
)()
    create_and_run = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()()
    create_and_run = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()()
    create_and_run = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()()
    create_and_run = (lambda self = None, *, assistant_id: pass# WARNING: Decompyle incomplete
)()()()
    
    async def create_and_run_poll(self = None, *, assistant_id, instructions, max_completion_tokens, max_prompt_tokens, metadata, model, parallel_tool_calls, response_format, temperature, thread, tool_choice, tool_resources, tools, top_p, truncation_strategy, poll_interval_ms, extra_headers, extra_query, extra_body, timeout):
        '''
        A helper to create a thread, start a run and then poll for a terminal state.
        More information on Run lifecycles can be found here:
        https://platform.openai.com/docs/assistants/how-it-works/runs-and-run-steps
        '''
        pass
    # WARNING: Decompyle incomplete

    create_and_run_stream = (lambda self = None, *, assistant_id: pass)()
    create_and_run_stream = (lambda self = None, *, assistant_id: pass)()
    
    def create_and_run_stream(self = None, *, assistant_id, instructions, max_completion_tokens, max_prompt_tokens, metadata, model, parallel_tool_calls, response_format, temperature, thread, tool_choice, tool_resources, tools, top_p, truncation_strategy, event_handler, extra_headers, extra_query, extra_body, timeout):
        '''Create a thread and stream the run back'''
        pass
    # WARNING: Decompyle incomplete



class ThreadsWithRawResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.create = _legacy_response.to_raw_response_wrapper(threads.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(threads.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(threads.update)
        self.delete = _legacy_response.to_raw_response_wrapper(threads.delete)
        self.create_and_run = _legacy_response.to_raw_response_wrapper(threads.create_and_run)

    runs = (lambda self = None: RunsWithRawResponse(self._threads.runs))()
    messages = (lambda self = None: MessagesWithRawResponse(self._threads.messages))()


class AsyncThreadsWithRawResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.create = _legacy_response.async_to_raw_response_wrapper(threads.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(threads.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(threads.update)
        self.delete = _legacy_response.async_to_raw_response_wrapper(threads.delete)
        self.create_and_run = _legacy_response.async_to_raw_response_wrapper(threads.create_and_run)

    runs = (lambda self = None: AsyncRunsWithRawResponse(self._threads.runs))()
    messages = (lambda self = None: AsyncMessagesWithRawResponse(self._threads.messages))()


class ThreadsWithStreamingResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.create = to_streamed_response_wrapper(threads.create)
        self.retrieve = to_streamed_response_wrapper(threads.retrieve)
        self.update = to_streamed_response_wrapper(threads.update)
        self.delete = to_streamed_response_wrapper(threads.delete)
        self.create_and_run = to_streamed_response_wrapper(threads.create_and_run)

    runs = (lambda self = None: RunsWithStreamingResponse(self._threads.runs))()
    messages = (lambda self = None: MessagesWithStreamingResponse(self._threads.messages))()


class AsyncThreadsWithStreamingResponse:
    
    def __init__(self = None, threads = None):
        self._threads = threads
        self.create = async_to_streamed_response_wrapper(threads.create)
        self.retrieve = async_to_streamed_response_wrapper(threads.retrieve)
        self.update = async_to_streamed_response_wrapper(threads.update)
        self.delete = async_to_streamed_response_wrapper(threads.delete)
        self.create_and_run = async_to_streamed_response_wrapper(threads.create_and_run)

    runs = (lambda self = None: AsyncRunsWithStreamingResponse(self._threads.runs))()
    messages = (lambda self = None: AsyncMessagesWithStreamingResponse(self._threads.messages))()
