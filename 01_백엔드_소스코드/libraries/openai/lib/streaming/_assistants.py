# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _assistants.pyc (Python 3.11)

from __future__ import annotations
import asyncio
from types import TracebackType
from typing import TYPE_CHECKING, Any, Generic, TypeVar, Callable, Iterable, Iterator, cast
from typing_extensions import Awaitable, AsyncIterable, AsyncIterator, assert_never
import httpx
from _utils import is_dict, is_list, consume_sync_iterator, consume_async_iterator
from _compat import model_dump
from _models import construct_type
from _streaming import Stream, AsyncStream
from types.beta import AssistantStreamEvent
from types.beta.threads import Run, Text, Message, ImageFile, TextDelta, MessageDelta, MessageContent, MessageContentDelta
from types.beta.threads.runs import RunStep, ToolCall, RunStepDelta, ToolCallDelta

class AssistantEventHandler:
    text_deltas: 'Iterable[str]' = 'AssistantEventHandler'
    
    def __init__(self = None):
        self._current_event = None
        self._current_message_content_index = None
        self._current_message_content = None
        self._current_tool_call_index = None
        self._current_tool_call = None
        self._AssistantEventHandler__current_run_step_id = None
        self._AssistantEventHandler__current_run = None
        self._AssistantEventHandler__run_step_snapshots = { }
        self._AssistantEventHandler__message_snapshots = { }
        self._AssistantEventHandler__current_message_snapshot = None
        self.text_deltas = self.__text_deltas__()
        self._iterator = self.__stream__()
        self._AssistantEventHandler__stream = None

    
    def _init(self = None, stream = None):
        if self._AssistantEventHandler__stream:
            raise RuntimeError('A single event handler cannot be shared between multiple streams; You will need to construct a new event handler instance')
        self._AssistantEventHandler__stream = stream

    
    def __next__(self = None):
        return self._iterator.__next__()

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    current_event = (lambda self = None: self._current_event)()
    current_run = (lambda self = None: self._AssistantEventHandler__current_run)()
    current_run_step_snapshot = (lambda self = None: if not self._AssistantEventHandler__current_run_step_id:
NoneNone._AssistantEventHandler__run_step_snapshots[self._AssistantEventHandler__current_run_step_id])()
    current_message_snapshot = (lambda self = None: self._AssistantEventHandler__current_message_snapshot)()
    
    def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called when the context manager exits.
        '''
        if self._AssistantEventHandler__stream:
            self._AssistantEventHandler__stream.close()
            return None

    
    def until_done(self = None):
        '''Waits until the stream has been consumed'''
        consume_sync_iterator(self)

    
    def get_final_run(self = None):
        '''Wait for the stream to finish and returns the completed Run object'''
        self.until_done()
        if not self._AssistantEventHandler__current_run:
            raise RuntimeError('No final run object found')
        return self._AssistantEventHandler__current_run

    
    def get_final_run_steps(self = None):
        '''Wait for the stream to finish and returns the steps taken in this run'''
        self.until_done()
        if not self._AssistantEventHandler__run_step_snapshots:
            raise RuntimeError('No run steps found')
        return self._AssistantEventHandler__run_step_snapshots.values()()

    
    def get_final_messages(self = None):
        '''Wait for the stream to finish and returns the messages emitted in this run'''
        self.until_done()
        if not self._AssistantEventHandler__message_snapshots:
            raise RuntimeError('No messages found')
        return self._AssistantEventHandler__message_snapshots.values()()

    
    def __text_deltas__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_end(self = None):
        '''Fires when the stream has finished.

        This happens if the stream is read to completion
        or if an exception occurs during iteration.
        '''
        pass

    
    def on_event(self = None, event = None):
        '''Callback that is fired for every Server-Sent-Event'''
        pass

    
    def on_run_step_created(self = None, run_step = None):
        '''Callback that is fired when a run step is created'''
        pass

    
    def on_run_step_delta(self = None, delta = None, snapshot = None):
        """Callback that is fired whenever a run step delta is returned from the API

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the run step. For example, a tool calls event may
        look like this:

        # delta
        tool_calls=[
            RunStepDeltaToolCallsCodeInterpreter(
                index=0,
                type='code_interpreter',
                id=None,
                code_interpreter=CodeInterpreter(input=' sympy', outputs=None)
            )
        ]
        # snapshot
        tool_calls=[
            CodeToolCall(
                id='call_wKayJlcYV12NiadiZuJXxcfx',
                code_interpreter=CodeInterpreter(input='from sympy', outputs=[]),
                type='code_interpreter',
                index=0
            )
        ],
        """
        pass

    
    def on_run_step_done(self = None, run_step = None):
        '''Callback that is fired when a run step is completed'''
        pass

    
    def on_tool_call_created(self = None, tool_call = None):
        '''Callback that is fired when a tool call is created'''
        pass

    
    def on_tool_call_delta(self = None, delta = None, snapshot = None):
        '''Callback that is fired when a tool call delta is encountered'''
        pass

    
    def on_tool_call_done(self = None, tool_call = None):
        '''Callback that is fired when a tool call delta is encountered'''
        pass

    
    def on_exception(self = None, exception = None):
        '''Fired whenever an exception happens during streaming'''
        pass

    
    def on_timeout(self = None):
        '''Fires if the request times out'''
        pass

    
    def on_message_created(self = None, message = None):
        '''Callback that is fired when a message is created'''
        pass

    
    def on_message_delta(self = None, delta = None, snapshot = None):
        """Callback that is fired whenever a message delta is returned from the API

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the message. For example, a text content event may
        look like this:

        # delta
        MessageDeltaText(
            index=0,
            type='text',
            text=Text(
                value=' Jane'
            ),
        )
        # snapshot
        MessageContentText(
            index=0,
            type='text',
            text=Text(
                value='Certainly, Jane'
            ),
        )
        """
        pass

    
    def on_message_done(self = None, message = None):
        '''Callback that is fired when a message is completed'''
        pass

    
    def on_text_created(self = None, text = None):
        '''Callback that is fired when a text content block is created'''
        pass

    
    def on_text_delta(self = None, delta = None, snapshot = None):
        '''Callback that is fired whenever a text content delta is returned
        by the API.

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the text. For example:

        on_text_delta(TextDelta(value="The"), Text(value="The")),
        on_text_delta(TextDelta(value=" solution"), Text(value="The solution")),
        on_text_delta(TextDelta(value=" to"), Text(value="The solution to")),
        on_text_delta(TextDelta(value=" the"), Text(value="The solution to the")),
        on_text_delta(TextDelta(value=" equation"), Text(value="The solution to the equation")),
        '''
        pass

    
    def on_text_done(self = None, text = None):
        '''Callback that is fired when a text content block is finished'''
        pass

    
    def on_image_file_done(self = None, image_file = None):
        '''Callback that is fired when an image file block is finished'''
        pass

    
    def _emit_sse_event(self = None, event = None):
        self._current_event = event
        self.on_event(event)
        (self._AssistantEventHandler__current_message_snapshot, new_content) = accumulate_event(event = event, current_message_snapshot = self._AssistantEventHandler__current_message_snapshot)
    # WARNING: Decompyle incomplete

    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete


AssistantEventHandlerT = TypeVar('AssistantEventHandlerT', bound = AssistantEventHandler)

def AssistantStreamManager():
    '''AssistantStreamManager'''
    __doc__ = 'Wrapper over AssistantStreamEventHandler that is returned by `.stream()`\n    so that a context manager can be used.\n\n    ```py\n    with client.threads.create_and_run_stream(...) as stream:\n        for event in stream:\n            ...\n    ```\n    '
    
    def __init__(self = None, api_request = None, *, event_handler):
        self._AssistantStreamManager__stream = None
        self._AssistantStreamManager__event_handler = event_handler
        self._AssistantStreamManager__api_request = api_request

    
    def __enter__(self = None):
        self._AssistantStreamManager__stream = self._AssistantStreamManager__api_request()
        self._AssistantStreamManager__event_handler._init(self._AssistantStreamManager__stream)
        return self._AssistantStreamManager__event_handler

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AssistantStreamManager = <NODE:27>(AssistantStreamManager, 'AssistantStreamManager', Generic[AssistantEventHandlerT])

class AsyncAssistantEventHandler:
    text_deltas: 'AsyncIterable[str]' = 'AsyncAssistantEventHandler'
    
    def __init__(self = None):
        self._current_event = None
        self._current_message_content_index = None
        self._current_message_content = None
        self._current_tool_call_index = None
        self._current_tool_call = None
        self._AsyncAssistantEventHandler__current_run_step_id = None
        self._AsyncAssistantEventHandler__current_run = None
        self._AsyncAssistantEventHandler__run_step_snapshots = { }
        self._AsyncAssistantEventHandler__message_snapshots = { }
        self._AsyncAssistantEventHandler__current_message_snapshot = None
        self.text_deltas = self.__text_deltas__()
        self._iterator = self.__stream__()
        self._AsyncAssistantEventHandler__stream = None

    
    def _init(self = None, stream = None):
        if self._AsyncAssistantEventHandler__stream:
            raise RuntimeError('A single event handler cannot be shared between multiple streams; You will need to construct a new event handler instance')
        self._AsyncAssistantEventHandler__stream = stream

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called when the context manager exits.
        '''
        pass
    # WARNING: Decompyle incomplete

    current_event = (lambda self = None: self._current_event)()
    current_run = (lambda self = None: self._AsyncAssistantEventHandler__current_run)()
    current_run_step_snapshot = (lambda self = None: if not self._AsyncAssistantEventHandler__current_run_step_id:
NoneNone._AsyncAssistantEventHandler__run_step_snapshots[self._AsyncAssistantEventHandler__current_run_step_id])()
    current_message_snapshot = (lambda self = None: self._AsyncAssistantEventHandler__current_message_snapshot)()
    
    async def until_done(self = None):
        '''Waits until the stream has been consumed'''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_final_run(self = None):
        '''Wait for the stream to finish and returns the completed Run object'''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_final_run_steps(self = None):
        '''Wait for the stream to finish and returns the steps taken in this run'''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_final_messages(self = None):
        '''Wait for the stream to finish and returns the messages emitted in this run'''
        pass
    # WARNING: Decompyle incomplete

    
    def __text_deltas__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def on_end(self = None):
        '''Fires when the stream has finished.

        This happens if the stream is read to completion
        or if an exception occurs during iteration.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_event(self = None, event = None):
        '''Callback that is fired for every Server-Sent-Event'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_run_step_created(self = None, run_step = None):
        '''Callback that is fired when a run step is created'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_run_step_delta(self = None, delta = None, snapshot = None):
        """Callback that is fired whenever a run step delta is returned from the API

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the run step. For example, a tool calls event may
        look like this:

        # delta
        tool_calls=[
            RunStepDeltaToolCallsCodeInterpreter(
                index=0,
                type='code_interpreter',
                id=None,
                code_interpreter=CodeInterpreter(input=' sympy', outputs=None)
            )
        ]
        # snapshot
        tool_calls=[
            CodeToolCall(
                id='call_wKayJlcYV12NiadiZuJXxcfx',
                code_interpreter=CodeInterpreter(input='from sympy', outputs=[]),
                type='code_interpreter',
                index=0
            )
        ],
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def on_run_step_done(self = None, run_step = None):
        '''Callback that is fired when a run step is completed'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_tool_call_created(self = None, tool_call = None):
        '''Callback that is fired when a tool call is created'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_tool_call_delta(self = None, delta = None, snapshot = None):
        '''Callback that is fired when a tool call delta is encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_tool_call_done(self = None, tool_call = None):
        '''Callback that is fired when a tool call delta is encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_exception(self = None, exception = None):
        '''Fired whenever an exception happens during streaming'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_timeout(self = None):
        '''Fires if the request times out'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_message_created(self = None, message = None):
        '''Callback that is fired when a message is created'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_message_delta(self = None, delta = None, snapshot = None):
        """Callback that is fired whenever a message delta is returned from the API

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the message. For example, a text content event may
        look like this:

        # delta
        MessageDeltaText(
            index=0,
            type='text',
            text=Text(
                value=' Jane'
            ),
        )
        # snapshot
        MessageContentText(
            index=0,
            type='text',
            text=Text(
                value='Certainly, Jane'
            ),
        )
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def on_message_done(self = None, message = None):
        '''Callback that is fired when a message is completed'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_text_created(self = None, text = None):
        '''Callback that is fired when a text content block is created'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_text_delta(self = None, delta = None, snapshot = None):
        '''Callback that is fired whenever a text content delta is returned
        by the API.

        The first argument is just the delta as sent by the API and the second argument
        is the accumulated snapshot of the text. For example:

        on_text_delta(TextDelta(value="The"), Text(value="The")),
        on_text_delta(TextDelta(value=" solution"), Text(value="The solution")),
        on_text_delta(TextDelta(value=" to"), Text(value="The solution to")),
        on_text_delta(TextDelta(value=" the"), Text(value="The solution to the")),
        on_text_delta(TextDelta(value=" equation"), Text(value="The solution to the equivalent")),
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_text_done(self = None, text = None):
        '''Callback that is fired when a text content block is finished'''
        pass
    # WARNING: Decompyle incomplete

    
    async def on_image_file_done(self = None, image_file = None):
        '''Callback that is fired when an image file block is finished'''
        pass
    # WARNING: Decompyle incomplete

    
    async def _emit_sse_event(self = None, event = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete


AsyncAssistantEventHandlerT = TypeVar('AsyncAssistantEventHandlerT', bound = AsyncAssistantEventHandler)

def AsyncAssistantStreamManager():
    '''AsyncAssistantStreamManager'''
    __doc__ = 'Wrapper over AsyncAssistantStreamEventHandler that is returned by `.stream()`\n    so that an async context manager can be used without `await`ing the\n    original client call.\n\n    ```py\n    async with client.threads.create_and_run_stream(...) as stream:\n        async for event in stream:\n            ...\n    ```\n    '
    
    def __init__(self = None, api_request = None, *, event_handler):
        self._AsyncAssistantStreamManager__stream = None
        self._AsyncAssistantStreamManager__event_handler = event_handler
        self._AsyncAssistantStreamManager__api_request = api_request

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AsyncAssistantStreamManager = <NODE:27>(AsyncAssistantStreamManager, 'AsyncAssistantStreamManager', Generic[AsyncAssistantEventHandlerT])

def accumulate_run_step(*, event, run_step_snapshots):
    if event.event == 'thread.run.step.created':
        run_step_snapshots[event.data.id] = event.data
        return None
    if None.event == 'thread.run.step.delta':
        data = event.data
        snapshot = run_step_snapshots[data.id]
        if data.delta:
            merged = accumulate_delta(cast('dict[object, object]', model_dump(snapshot, exclude_unset = True, warnings = False)), cast('dict[object, object]', model_dump(data.delta, exclude_unset = True, warnings = False)))
            run_step_snapshots[snapshot.id] = cast(RunStep, construct_type(type_ = RunStep, value = merged))


def accumulate_event(*, event, current_message_snapshot):
    '''Returns a tuple of message snapshot and newly created text message deltas'''
    if event.event == 'thread.message.created':
        return (event.data, [])
    new_content = None
    if event.event != 'thread.message.delta':
        return (current_message_snapshot, [])
    if not None:
        raise RuntimeError('Encountered a message delta with no previous snapshot')
    data = event.data
    if data.delta.content:
        for content_delta in data.delta.content:
            block = current_message_snapshot.content[content_delta.index]
            merged = accumulate_delta(cast('dict[object, object]', model_dump(block, exclude_unset = True, warnings = False)), cast('dict[object, object]', model_dump(content_delta, exclude_unset = True, warnings = False)))
            current_message_snapshot.content[content_delta.index] = cast(MessageContent, construct_type(type_ = cast(Any, MessageContent), value = merged))
            except IndexError:
                current_message_snapshot.content.insert(content_delta.index, cast(MessageContent, construct_type(type_ = cast(Any, MessageContent), value = model_dump(content_delta, exclude_unset = True, warnings = False))))
                new_content.append(content_delta)
                continue
            return (current_message_snapshot, new_content)


def accumulate_delta(acc = None, delta = None):
    pass
# WARNING: Decompyle incomplete
