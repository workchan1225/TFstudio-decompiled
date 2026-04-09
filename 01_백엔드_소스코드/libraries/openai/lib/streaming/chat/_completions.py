# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _completions.pyc (Python 3.11)

from __future__ import annotations
import inspect
from types import TracebackType
from typing import TYPE_CHECKING, Any, Generic, Callable, Iterable, Awaitable, AsyncIterator, cast
from typing_extensions import Self, Iterator, assert_never
from jiter import from_json
from _types import ParsedChoiceSnapshot, ParsedChatCompletionSnapshot, ParsedChatCompletionMessageSnapshot
from _events import ChunkEvent, ContentDoneEvent, RefusalDoneEvent, ContentDeltaEvent, RefusalDeltaEvent, LogprobsContentDoneEvent, LogprobsRefusalDoneEvent, ChatCompletionStreamEvent, LogprobsContentDeltaEvent, LogprobsRefusalDeltaEvent, FunctionToolCallArgumentsDoneEvent, FunctionToolCallArgumentsDeltaEvent
from _deltas import accumulate_delta
from _types import Omit, IncEx, omit
from _utils import is_given, consume_sync_iterator, consume_async_iterator
from _compat import model_dump
from _models import build, construct_type
from _parsing import ResponseFormatT, has_parseable_input, maybe_parse_content, parse_chat_completion, get_input_tool_by_name, solve_response_format_t, parse_function_tool_arguments
from _streaming import Stream, AsyncStream
from types.chat import ChatCompletionChunk, ParsedChatCompletion, ChatCompletionToolUnionParam
from _exceptions import LengthFinishReasonError, ContentFilterFinishReasonError
from types.chat.chat_completion import ChoiceLogprobs
from types.chat.chat_completion_chunk import Choice as ChoiceChunk
from types.chat.completion_create_params import ResponseFormat as ResponseFormatParam

def ChatCompletionStream():
    '''ChatCompletionStream'''
    __doc__ = 'Wrapper over the Chat Completions streaming API that adds helpful\n    events such as `content.done`, supports automatically parsing\n    responses & tool calls and accumulates a `ChatCompletion` object\n    from each individual chunk.\n\n    https://platform.openai.com/docs/api-reference/streaming\n    '
    
    def __init__(self = None, *, raw_stream, response_format, input_tools):
        self._raw_stream = raw_stream
        self._response = raw_stream.response
        self._iterator = self.__stream__()
        self._state = ChatCompletionStreamState(response_format = response_format, input_tools = input_tools)

    
    def __next__(self = None):
        return self._iterator.__next__()

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        self._response.close()

    
    def get_final_completion(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `ParsedChatCompletion` object.

        If you passed a class type to `.stream()`, the `completion.choices[0].message.parsed`
        property will be the content deserialised into that class, if there was any content returned
        by the API.
        '''
        self.until_done()
        return self._state.get_final_completion()

    
    def until_done(self = None):
        '''Blocks until the stream has been consumed.'''
        consume_sync_iterator(self)
        return self

    current_completion_snapshot = (lambda self = None: self._state.current_completion_snapshot)()
    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete


ChatCompletionStream = <NODE:27>(ChatCompletionStream, 'ChatCompletionStream', Generic[ResponseFormatT])

def ChatCompletionStreamManager():
    '''ChatCompletionStreamManager'''
    __doc__ = "Context manager over a `ChatCompletionStream` that is returned by `.stream()`.\n\n    This context manager ensures the response cannot be leaked if you don't read\n    the stream to completion.\n\n    Usage:\n    ```py\n    with client.chat.completions.stream(...) as stream:\n        for event in stream:\n            ...\n    ```\n    "
    
    def __init__(self = None, api_request = None, *, response_format, input_tools):
        self._ChatCompletionStreamManager__stream = None
        self._ChatCompletionStreamManager__api_request = api_request
        self._ChatCompletionStreamManager__response_format = response_format
        self._ChatCompletionStreamManager__input_tools = input_tools

    
    def __enter__(self = None):
        raw_stream = self._ChatCompletionStreamManager__api_request()
        self._ChatCompletionStreamManager__stream = ChatCompletionStream(raw_stream = raw_stream, response_format = self._ChatCompletionStreamManager__response_format, input_tools = self._ChatCompletionStreamManager__input_tools)
        return self._ChatCompletionStreamManager__stream

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


ChatCompletionStreamManager = <NODE:27>(ChatCompletionStreamManager, 'ChatCompletionStreamManager', Generic[ResponseFormatT])

def AsyncChatCompletionStream():
    '''AsyncChatCompletionStream'''
    __doc__ = 'Wrapper over the Chat Completions streaming API that adds helpful\n    events such as `content.done`, supports automatically parsing\n    responses & tool calls and accumulates a `ChatCompletion` object\n    from each individual chunk.\n\n    https://platform.openai.com/docs/api-reference/streaming\n    '
    
    def __init__(self = None, *, raw_stream, response_format, input_tools):
        self._raw_stream = raw_stream
        self._response = raw_stream.response
        self._iterator = self.__stream__()
        self._state = ChatCompletionStreamState(response_format = response_format, input_tools = input_tools)

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_final_completion(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `ParsedChatCompletion` object.

        If you passed a class type to `.stream()`, the `completion.choices[0].message.parsed`
        property will be the content deserialised into that class, if there was any content returned
        by the API.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def until_done(self = None):
        '''Blocks until the stream has been consumed.'''
        pass
    # WARNING: Decompyle incomplete

    current_completion_snapshot = (lambda self = None: self._state.current_completion_snapshot)()
    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete


AsyncChatCompletionStream = <NODE:27>(AsyncChatCompletionStream, 'AsyncChatCompletionStream', Generic[ResponseFormatT])

def AsyncChatCompletionStreamManager():
    '''AsyncChatCompletionStreamManager'''
    __doc__ = "Context manager over a `AsyncChatCompletionStream` that is returned by `.stream()`.\n\n    This context manager ensures the response cannot be leaked if you don't read\n    the stream to completion.\n\n    Usage:\n    ```py\n    async with client.chat.completions.stream(...) as stream:\n        for event in stream:\n            ...\n    ```\n    "
    
    def __init__(self = None, api_request = None, *, response_format, input_tools):
        self._AsyncChatCompletionStreamManager__stream = None
        self._AsyncChatCompletionStreamManager__api_request = api_request
        self._AsyncChatCompletionStreamManager__response_format = response_format
        self._AsyncChatCompletionStreamManager__input_tools = input_tools

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AsyncChatCompletionStreamManager = <NODE:27>(AsyncChatCompletionStreamManager, 'AsyncChatCompletionStreamManager', Generic[ResponseFormatT])

def ChatCompletionStreamState():
    '''ChatCompletionStreamState'''
    __doc__ = "Helper class for manually accumulating `ChatCompletionChunk`s into a final `ChatCompletion` object.\n\n    This is useful in cases where you can't always use the `.stream()` method, e.g.\n\n    ```py\n    from openai.lib.streaming.chat import ChatCompletionStreamState\n\n    state = ChatCompletionStreamState()\n\n    stream = client.chat.completions.create(..., stream=True)\n    for chunk in response:\n        state.handle_chunk(chunk)\n\n        # can also access the accumulated `ChatCompletion` mid-stream\n        state.current_completion_snapshot\n\n    print(state.get_final_completion())\n    ```\n    "
    
    def __init__(self = None, *, input_tools, response_format):
        self._ChatCompletionStreamState__current_completion_snapshot = None
        self._ChatCompletionStreamState__choice_event_states = []
        self._input_tools = input_tools() if is_given(input_tools) else []
        self._response_format = response_format
        self._rich_response_format = response_format if inspect.isclass(response_format) else omit

    
    def get_final_completion(self = None):
        '''Parse the final completion object.

        Note this does not provide any guarantees that the stream has actually finished, you must
        only call this method when the stream is finished.
        '''
        return parse_chat_completion(chat_completion = self.current_completion_snapshot, response_format = self._rich_response_format, input_tools = self._input_tools)

    current_completion_snapshot = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def handle_chunk(self = None, chunk = None):
        '''Accumulate a new chunk into the snapshot and returns an iterable of events to yield.'''
        self._ChatCompletionStreamState__current_completion_snapshot = self._accumulate_chunk(chunk)
        return self._build_events(chunk = chunk, completion_snapshot = self._ChatCompletionStreamState__current_completion_snapshot)

    
    def _get_choice_state(self = None, choice = None):
        
        try:
            return self._ChatCompletionStreamState__choice_event_states[choice.index]
        except IndexError:
            choice_state = ChoiceEventState(input_tools = self._input_tools)
            self._ChatCompletionStreamState__choice_event_states.append(choice_state)
            return 


    
    def _accumulate_chunk(self = None, chunk = None):
        completion_snapshot = self._ChatCompletionStreamState__current_completion_snapshot
    # WARNING: Decompyle incomplete

    
    def _build_events(self = None, *, chunk, completion_snapshot):
        events_to_fire = []
        events_to_fire.append(build(ChunkEvent, type = 'chunk', chunk = chunk, snapshot = completion_snapshot))
    # WARNING: Decompyle incomplete


ChatCompletionStreamState = <NODE:27>(ChatCompletionStreamState, 'ChatCompletionStreamState', Generic[ResponseFormatT])

class ChoiceEventState:
    
    def __init__(self = None, *, input_tools):
        self._input_tools = input_tools
        self._content_done = False
        self._refusal_done = False
        self._logprobs_content_done = False
        self._logprobs_refusal_done = False
        self._done_tool_calls = set()
        self._ChoiceEventState__current_tool_call_index = None

    
    def get_done_events(self = None, *, choice_chunk, choice_snapshot, response_format):
        events_to_fire = []
    # WARNING: Decompyle incomplete

    
    def _content_done_events(self = None, *, choice_snapshot, response_format):
        events_to_fire = []
        if not choice_snapshot.message.content and self._content_done:
            self._content_done = True
            parsed = maybe_parse_content(response_format = response_format, message = choice_snapshot.message)
            choice_snapshot.message.parsed = parsed
            events_to_fire.append(build(cast('type[ContentDoneEvent[ResponseFormatT]]', cast(Any, ContentDoneEvent)[solve_response_format_t(response_format)]), type = 'content.done', content = choice_snapshot.message.content, parsed = parsed))
    # WARNING: Decompyle incomplete

    
    def _add_tool_done_event(self = None, *, events_to_fire, choice_snapshot, tool_index):
        if tool_index in self._done_tool_calls:
            return None
        None._done_tool_calls.add(tool_index)
    # WARNING: Decompyle incomplete



def _convert_initial_chunk_into_snapshot(chunk = None):
    data = chunk.to_dict()
    choices = cast('list[object]', data['choices'])
# WARNING: Decompyle incomplete


def _is_valid_chat_completion_chunk_weak(sse_event = None):
    return sse_event.object == 'chat.completion.chunk'
