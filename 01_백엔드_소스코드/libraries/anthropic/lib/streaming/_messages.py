# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _messages.pyc (Python 3.11)

from __future__ import annotations
from types import TracebackType
from typing import TYPE_CHECKING, Any, Type, Callable, cast
from typing_extensions import Self, Iterator, Awaitable, AsyncIterator, assert_never
import httpx
from pydantic import BaseModel
from anthropic.types.tool_use_block import ToolUseBlock
from anthropic.types.server_tool_use_block import ServerToolUseBlock
from _types import TextEvent, CitationEvent, ThinkingEvent, InputJsonEvent, SignatureEvent, MessageStopEvent, MessageStreamEvent, ContentBlockStopEvent
from types import Message, ContentBlock, RawMessageStreamEvent
from _utils import consume_sync_iterator, consume_async_iterator
from _models import build, construct_type, construct_type_unchecked
from _streaming import Stream, AsyncStream

class MessageStream:
    text_stream: 'Iterator[str]' = 'MessageStream'
    
    def __init__(self = None, raw_stream = None):
        self._raw_stream = raw_stream
        self.text_stream = self.__stream_text__()
        self._iterator = self.__stream__()
        self._MessageStream__final_message_snapshot = None

    response = (lambda self = None: self._raw_stream.response)()
    request_id = (lambda self = None: self.response.headers.get('request-id'))()
    
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
        self._raw_stream.close()

    
    def get_final_message(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `Message` object.
        '''
        self.until_done()
    # WARNING: Decompyle incomplete

    
    def get_final_text(self = None):
        '''Returns all `text` content blocks concatenated together.

        > [!NOTE]
        > Currently the API will only respond with a single content block.

        Will raise an error if no `text` content blocks were returned.
        '''
        message = self.get_final_message()
        text_blocks = []
        for block in message.content:
            if block.type == 'text':
                text_blocks.append(block.text)
            if not text_blocks:
                raise '.get_final_text() can only be called when the API returns a `text` content block.\nThe API returned '(f'''{(lambda .0: [ b.type for b in .0 ])(message.content())} content block type(s) that you can access by calling get_final_message().content''')
            return ''.join(text_blocks)

    
    def until_done(self = None):
        '''Blocks until the stream has been consumed'''
        consume_sync_iterator(self)

    current_message_snapshot = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream_text__(self = None):
        pass
    # WARNING: Decompyle incomplete



class MessageStreamManager:
    '''Wrapper over MessageStream that is returned by `.stream()`.

    ```py
    with client.messages.stream(...) as stream:
        for chunk in stream:
            ...
    ```
    '''
    
    def __init__(self = None, api_request = None):
        self._MessageStreamManager__stream = None
        self._MessageStreamManager__api_request = api_request

    
    def __enter__(self = None):
        raw_stream = self._MessageStreamManager__api_request()
        self._MessageStreamManager__stream = MessageStream(raw_stream)
        return self._MessageStreamManager__stream

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class AsyncMessageStream:
    text_stream: 'AsyncIterator[str]' = 'AsyncMessageStream'
    
    def __init__(self = None, raw_stream = None):
        self._raw_stream = raw_stream
        self.text_stream = self.__stream_text__()
        self._iterator = self.__stream__()
        self._AsyncMessageStream__final_message_snapshot = None

    response = (lambda self = None: self._raw_stream.response)()
    request_id = (lambda self = None: self.response.headers.get('request-id'))()
    
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

    
    async def get_final_message(self = None):
        '''Waits until the stream has been read to completion and returns
        the accumulated `Message` object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_final_text(self = None):
        '''Returns all `text` content blocks concatenated together.

        > [!NOTE]
        > Currently the API will only respond with a single content block.

        Will raise an error if no `text` content blocks were returned.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def until_done(self = None):
        '''Waits until the stream has been consumed'''
        pass
    # WARNING: Decompyle incomplete

    current_message_snapshot = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream_text__(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncMessageStreamManager:
    '''Wrapper over AsyncMessageStream that is returned by `.stream()`
    so that an async context manager can be used without `await`ing the
    original client call.

    ```py
    async with client.messages.stream(...) as stream:
        async for chunk in stream:
            ...
    ```
    '''
    
    def __init__(self = None, api_request = None):
        self._AsyncMessageStreamManager__stream = None
        self._AsyncMessageStreamManager__api_request = api_request

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



def build_events(*, event, message_snapshot):
    events_to_fire = []
    if event.type == 'message_start':
        events_to_fire.append(event)
    elif event.type == 'message_delta':
        events_to_fire.append(event)
    elif event.type == 'message_stop':
        events_to_fire.append(build(MessageStopEvent, type = 'message_stop', message = message_snapshot))
    elif event.type == 'content_block_start':
        events_to_fire.append(event)
    elif event.type == 'content_block_delta':
        events_to_fire.append(event)
        content_block = message_snapshot.content[event.index]
        if event.delta.type == 'text_delta':
            if content_block.type == 'text':
                events_to_fire.append(build(TextEvent, type = 'text', text = event.delta.text, snapshot = content_block.text))
            elif event.delta.type == 'input_json_delta':
                if content_block.type == 'tool_use':
                    events_to_fire.append(build(InputJsonEvent, type = 'input_json', partial_json = event.delta.partial_json, snapshot = content_block.input))
                elif event.delta.type == 'citations_delta':
                    if content_block.type == 'text':
                        if not content_block.citations:
                            events_to_fire.append(build(CitationEvent, type = 'citation', citation = event.delta.citation, snapshot = []))
                        elif event.delta.type == 'thinking_delta':
                            if content_block.type == 'thinking':
                                events_to_fire.append(build(ThinkingEvent, type = 'thinking', thinking = event.delta.thinking, snapshot = content_block.thinking))
                            elif event.delta.type == 'signature_delta':
                                if content_block.type == 'thinking':
                                    events_to_fire.append(build(SignatureEvent, type = 'signature', signature = content_block.signature))
                                elif TYPE_CHECKING:
                                    assert_never(event.delta)
                                elif event.type == 'content_block_stop':
                                    content_block = message_snapshot.content[event.index]
                                    events_to_fire.append(build(ContentBlockStopEvent, type = 'content_block_stop', index = event.index, content_block = content_block))
                                elif TYPE_CHECKING:
                                    assert_never(event)
    return events_to_fire

JSON_BUF_PROPERTY = '__json_buf'
TRACKS_TOOL_INPUT = (ToolUseBlock, ServerToolUseBlock)

def accumulate_event(*, event, current_snapshot):
    if not isinstance(cast(Any, event), BaseModel):
        event = cast(RawMessageStreamEvent, construct_type_unchecked(type_ = cast(Type[RawMessageStreamEvent], RawMessageStreamEvent), value = event))
        if not isinstance(cast(Any, event), BaseModel):
            raise TypeError(f'''Unexpected event runtime type, after deserialising twice - {event} - {type(event)}''')
# WARNING: Decompyle incomplete
