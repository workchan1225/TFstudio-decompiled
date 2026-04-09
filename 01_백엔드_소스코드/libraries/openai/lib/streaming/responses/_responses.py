# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _responses.pyc (Python 3.11)

from __future__ import annotations
import inspect
from types import TracebackType
from typing import Any, List, Generic, Iterable, Awaitable, cast
from typing_extensions import Self, Callable, Iterator, AsyncIterator
from _types import ParsedResponseSnapshot
from _events import ResponseStreamEvent, ResponseTextDoneEvent, ResponseCompletedEvent, ResponseTextDeltaEvent, ResponseFunctionCallArgumentsDeltaEvent
from _types import Omit, omit
from _utils import is_given, consume_sync_iterator, consume_async_iterator
from _models import build, construct_type_unchecked
from _streaming import Stream, AsyncStream
from types.responses import ParsedResponse, ResponseStreamEvent as RawResponseStreamEvent
from _parsing._responses import TextFormatT, parse_text, parse_response
from types.responses.tool_param import ToolParam
from types.responses.parsed_response import ParsedContent, ParsedResponseOutputMessage, ParsedResponseFunctionToolCall

def ResponseStream():
    '''ResponseStream'''
    
    def __init__(self = None, *, raw_stream, text_format, input_tools, starting_after):
        self._raw_stream = raw_stream
        self._response = raw_stream.response
        self._iterator = self.__stream__()
        self._state = ResponseStreamState(text_format = text_format, input_tools = input_tools)
        self._starting_after = starting_after

    
    def __next__(self = None):
        return self._iterator.__next__()

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        self._response.close()

    
    def get_final_response(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `ParsedResponse` object.
        '''
        self.until_done()
        response = self._state._completed_response
        if not response:
            raise RuntimeError("Didn't receive a `response.completed` event.")
        return response

    
    def until_done(self = None):
        '''Blocks until the stream has been consumed.'''
        consume_sync_iterator(self)
        return self


ResponseStream = <NODE:27>(ResponseStream, 'ResponseStream', Generic[TextFormatT])

def ResponseStreamManager():
    '''ResponseStreamManager'''
    
    def __init__(self = None, api_request = None, *, text_format, input_tools, starting_after):
        self._ResponseStreamManager__stream = None
        self._ResponseStreamManager__api_request = api_request
        self._ResponseStreamManager__text_format = text_format
        self._ResponseStreamManager__input_tools = input_tools
        self._ResponseStreamManager__starting_after = starting_after

    
    def __enter__(self = None):
        raw_stream = self._ResponseStreamManager__api_request()
        self._ResponseStreamManager__stream = ResponseStream(raw_stream = raw_stream, text_format = self._ResponseStreamManager__text_format, input_tools = self._ResponseStreamManager__input_tools, starting_after = self._ResponseStreamManager__starting_after)
        return self._ResponseStreamManager__stream

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


ResponseStreamManager = <NODE:27>(ResponseStreamManager, 'ResponseStreamManager', Generic[TextFormatT])

def AsyncResponseStream():
    '''AsyncResponseStream'''
    
    def __init__(self = None, *, raw_stream, text_format, input_tools, starting_after):
        self._raw_stream = raw_stream
        self._response = raw_stream.response
        self._iterator = self.__stream__()
        self._state = ResponseStreamState(text_format = text_format, input_tools = input_tools)
        self._starting_after = starting_after

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream__(self = None):
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

    
    async def get_final_response(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `ParsedResponse` object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def until_done(self = None):
        '''Blocks until the stream has been consumed.'''
        pass
    # WARNING: Decompyle incomplete


AsyncResponseStream = <NODE:27>(AsyncResponseStream, 'AsyncResponseStream', Generic[TextFormatT])

def AsyncResponseStreamManager():
    '''AsyncResponseStreamManager'''
    
    def __init__(self = None, api_request = None, *, text_format, input_tools, starting_after):
        self._AsyncResponseStreamManager__stream = None
        self._AsyncResponseStreamManager__api_request = api_request
        self._AsyncResponseStreamManager__text_format = text_format
        self._AsyncResponseStreamManager__input_tools = input_tools
        self._AsyncResponseStreamManager__starting_after = starting_after

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AsyncResponseStreamManager = <NODE:27>(AsyncResponseStreamManager, 'AsyncResponseStreamManager', Generic[TextFormatT])

def ResponseStreamState():
    '''ResponseStreamState'''
    
    def __init__(self = None, *, input_tools, text_format):
        self._ResponseStreamState__current_snapshot = None
        self._completed_response = None
        self._input_tools = input_tools() if is_given(input_tools) else []
        self._text_format = text_format
        self._rich_text_format = text_format if inspect.isclass(text_format) else omit

    
    def handle_event(self = None, event = None):
        self._ResponseStreamState__current_snapshot = self.accumulate_event(event)
        snapshot = self.accumulate_event(event)
        events = []
    # WARNING: Decompyle incomplete

    
    def accumulate_event(self = None, event = None):
        snapshot = self._ResponseStreamState__current_snapshot
    # WARNING: Decompyle incomplete

    
    def _create_initial_response(self = None, event = None):
        if event.type != 'response.created':
            raise RuntimeError(f'''Expected to have received `response.created` before `{event.type}`''')
        return construct_type_unchecked(type_ = ParsedResponseSnapshot, value = event.response.to_dict())


ResponseStreamState = <NODE:27>(ResponseStreamState, 'ResponseStreamState', Generic[TextFormatT])
