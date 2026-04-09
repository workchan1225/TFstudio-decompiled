# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime.pyc (Python 3.11)

from __future__ import annotations
import json
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Iterator, cast
from typing_extensions import AsyncIterator
import httpx
from pydantic import BaseModel
from sessions import Sessions, AsyncSessions, SessionsWithRawResponse, AsyncSessionsWithRawResponse, SessionsWithStreamingResponse, AsyncSessionsWithStreamingResponse
from _types import NOT_GIVEN, Query, Headers, NotGiven
from _utils import is_azure_client, maybe_transform, strip_not_given, async_maybe_transform, is_async_azure_client
from _compat import cached_property
from _models import construct_type_unchecked
from _resource import SyncAPIResource, AsyncAPIResource
from _exceptions import OpenAIError
from _base_client import _merge_mappings
from types.beta.realtime import session_update_event_param, response_create_event_param, transcription_session_update_param
from transcription_sessions import TranscriptionSessions, AsyncTranscriptionSessions, TranscriptionSessionsWithRawResponse, AsyncTranscriptionSessionsWithRawResponse, TranscriptionSessionsWithStreamingResponse, AsyncTranscriptionSessionsWithStreamingResponse
from types.websocket_connection_options import WebsocketConnectionOptions
from types.beta.realtime.realtime_client_event import RealtimeClientEvent
from types.beta.realtime.realtime_server_event import RealtimeServerEvent
from types.beta.realtime.conversation_item_param import ConversationItemParam
from types.beta.realtime.realtime_client_event_param import RealtimeClientEventParam
if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebsocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebsocketConnection
    from _client import OpenAI, AsyncOpenAI
__all__ = [
    'Realtime',
    'AsyncRealtime']
log: 'logging.Logger' = logging.getLogger(__name__)

class Realtime(SyncAPIResource):
    sessions = (lambda self = None: Sessions(self._client))()
    transcription_sessions = (lambda self = None: TranscriptionSessions(self._client))()
    with_raw_response = (lambda self = None: RealtimeWithRawResponse(self))()
    with_streaming_response = (lambda self = None: RealtimeWithStreamingResponse(self))()
    
    def connect(self = None, *, model, extra_query, extra_headers, websocket_connection_options):
        '''
        The Realtime API enables you to build low-latency, multi-modal conversational experiences. It currently supports text and audio as both input and output, as well as function calling.

        Some notable benefits of the API include:

        - Native speech-to-speech: Skipping an intermediate text format means low latency and nuanced output.
        - Natural, steerable voices: The models have natural inflection and can laugh, whisper, and adhere to tone direction.
        - Simultaneous multimodal output: Text is useful for moderation; faster-than-realtime audio ensures stable playback.

        The Realtime API is a stateful, event-based API that communicates over a WebSocket.
        '''
        return RealtimeConnectionManager(client = self._client, extra_query = extra_query, extra_headers = extra_headers, websocket_connection_options = websocket_connection_options, model = model)



class AsyncRealtime(AsyncAPIResource):
    sessions = (lambda self = None: AsyncSessions(self._client))()
    transcription_sessions = (lambda self = None: AsyncTranscriptionSessions(self._client))()
    with_raw_response = (lambda self = None: AsyncRealtimeWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncRealtimeWithStreamingResponse(self))()
    
    def connect(self = None, *, model, extra_query, extra_headers, websocket_connection_options):
        '''
        The Realtime API enables you to build low-latency, multi-modal conversational experiences. It currently supports text and audio as both input and output, as well as function calling.

        Some notable benefits of the API include:

        - Native speech-to-speech: Skipping an intermediate text format means low latency and nuanced output.
        - Natural, steerable voices: The models have natural inflection and can laugh, whisper, and adhere to tone direction.
        - Simultaneous multimodal output: Text is useful for moderation; faster-than-realtime audio ensures stable playback.

        The Realtime API is a stateful, event-based API that communicates over a WebSocket.
        '''
        return AsyncRealtimeConnectionManager(client = self._client, extra_query = extra_query, extra_headers = extra_headers, websocket_connection_options = websocket_connection_options, model = model)



class RealtimeWithRawResponse:
    
    def __init__(self = None, realtime = None):
        self._realtime = realtime

    sessions = (lambda self = None: SessionsWithRawResponse(self._realtime.sessions))()
    transcription_sessions = (lambda self = None: TranscriptionSessionsWithRawResponse(self._realtime.transcription_sessions))()


class AsyncRealtimeWithRawResponse:
    
    def __init__(self = None, realtime = None):
        self._realtime = realtime

    sessions = (lambda self = None: AsyncSessionsWithRawResponse(self._realtime.sessions))()
    transcription_sessions = (lambda self = None: AsyncTranscriptionSessionsWithRawResponse(self._realtime.transcription_sessions))()


class RealtimeWithStreamingResponse:
    
    def __init__(self = None, realtime = None):
        self._realtime = realtime

    sessions = (lambda self = None: SessionsWithStreamingResponse(self._realtime.sessions))()
    transcription_sessions = (lambda self = None: TranscriptionSessionsWithStreamingResponse(self._realtime.transcription_sessions))()


class AsyncRealtimeWithStreamingResponse:
    
    def __init__(self = None, realtime = None):
        self._realtime = realtime

    sessions = (lambda self = None: AsyncSessionsWithStreamingResponse(self._realtime.sessions))()
    transcription_sessions = (lambda self = None: AsyncTranscriptionSessionsWithStreamingResponse(self._realtime.transcription_sessions))()


class AsyncRealtimeConnection:
    _connection: 'AsyncWebsocketConnection' = 'Represents a live websocket connection to the Realtime API'
    
    def __init__(self = None, connection = None):
        self._connection = connection
        self.session = AsyncRealtimeSessionResource(self)
        self.response = AsyncRealtimeResponseResource(self)
        self.input_audio_buffer = AsyncRealtimeInputAudioBufferResource(self)
        self.conversation = AsyncRealtimeConversationResource(self)
        self.output_audio_buffer = AsyncRealtimeOutputAudioBufferResource(self)
        self.transcription_session = AsyncRealtimeTranscriptionSessionResource(self)

    
    def __aiter__(self = None):
        '''
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def recv(self = None):
        """
        Receive the next message from the connection and parses it into a `RealtimeServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def recv_bytes(self = None):
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `RealtimeServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, event = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None, *, code, reason):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_event(self = None, data = None):
        """
        Converts a raw `str` or `bytes` message into a `RealtimeServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(RealtimeServerEvent, construct_type_unchecked(value = json.loads(data), type_ = cast(Any, RealtimeServerEvent)))



class AsyncRealtimeConnectionManager:
    """
    Context manager over a `AsyncRealtimeConnection` that is returned by `beta.realtime.connect()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = await client.beta.realtime.connect(...).enter()
    # ...
    await connection.close()
    ```
    """
    
    def __init__(self = None, *, client, model, extra_query, extra_headers, websocket_connection_options):
        self._AsyncRealtimeConnectionManager__client = client
        self._AsyncRealtimeConnectionManager__model = model
        self._AsyncRealtimeConnectionManager__connection = None
        self._AsyncRealtimeConnectionManager__extra_query = extra_query
        self._AsyncRealtimeConnectionManager__extra_headers = extra_headers
        self._AsyncRealtimeConnectionManager__websocket_connection_options = websocket_connection_options

    
    async def __aenter__(self = None):
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.beta.realtime.connect(...).enter()
        # ...
        await connection.close()
        ```
        """
        pass
    # WARNING: Decompyle incomplete

    enter = __aenter__
    
    def _prepare_url(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class RealtimeConnection:
    _connection: 'WebsocketConnection' = 'Represents a live websocket connection to the Realtime API'
    
    def __init__(self = None, connection = None):
        self._connection = connection
        self.session = RealtimeSessionResource(self)
        self.response = RealtimeResponseResource(self)
        self.input_audio_buffer = RealtimeInputAudioBufferResource(self)
        self.conversation = RealtimeConversationResource(self)
        self.output_audio_buffer = RealtimeOutputAudioBufferResource(self)
        self.transcription_session = RealtimeTranscriptionSessionResource(self)

    
    def __iter__(self = None):
        '''
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def recv(self = None):
        """
        Receive the next message from the connection and parses it into a `RealtimeServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(self.recv_bytes())

    
    def recv_bytes(self = None):
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `RealtimeServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = self._connection.recv(decode = False)
        log.debug('Received websocket message: %s', message)
        return message

    
    def send(self = None, event = None):
        data = event.to_json(use_api_names = True, exclude_defaults = True, exclude_unset = True) if isinstance(event, BaseModel) else json.dumps(maybe_transform(event, RealtimeClientEventParam))
        self._connection.send(data)

    
    def close(self = None, *, code, reason):
        self._connection.close(code = code, reason = reason)

    
    def parse_event(self = None, data = None):
        """
        Converts a raw `str` or `bytes` message into a `RealtimeServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(RealtimeServerEvent, construct_type_unchecked(value = json.loads(data), type_ = cast(Any, RealtimeServerEvent)))



class RealtimeConnectionManager:
    """
    Context manager over a `RealtimeConnection` that is returned by `beta.realtime.connect()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = client.beta.realtime.connect(...).enter()
    # ...
    connection.close()
    ```
    """
    
    def __init__(self = None, *, client, model, extra_query, extra_headers, websocket_connection_options):
        self._RealtimeConnectionManager__client = client
        self._RealtimeConnectionManager__model = model
        self._RealtimeConnectionManager__connection = None
        self._RealtimeConnectionManager__extra_query = extra_query
        self._RealtimeConnectionManager__extra_headers = extra_headers
        self._RealtimeConnectionManager__websocket_connection_options = websocket_connection_options

    
    def __enter__(self = None):
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.beta.realtime.connect(...).enter()
        # ...
        connection.close()
        ```
        """
        
        try:
            connect = connect
            import websockets.sync.client
        except ImportError:
            exc = None
            raise OpenAIError('You need to install `openai[realtime]` to use this method'), exc
            exc = None
            del exc

        extra_query = self._RealtimeConnectionManager__extra_query
        self._RealtimeConnectionManager__client._refresh_api_key()
        auth_headers = self._RealtimeConnectionManager__client.auth_headers
        if is_azure_client(self._RealtimeConnectionManager__client):
            (url, auth_headers) = self._RealtimeConnectionManager__client._configure_realtime(self._RealtimeConnectionManager__model, extra_query)
    # WARNING: Decompyle incomplete

    enter = __enter__
    
    def _prepare_url(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class BaseRealtimeConnectionResource:
    
    def __init__(self = None, connection = None):
        self._connection = connection



class RealtimeSessionResource(BaseRealtimeConnectionResource):
    
    def update(self = None, *, session, event_id):
        '''
        Send this event to update the session’s default configuration.
        The client may send this event at any time to update any field,
        except for `voice`. However, note that once a session has been
        initialized with a particular `model`, it can’t be changed to
        another model using `session.update`.

        When the server receives a `session.update`, it will respond
        with a `session.updated` event showing the full, effective configuration.
        Only the fields that are present are updated. To clear a field like
        `instructions`, pass an empty string.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'session.update',
            'session': session,
            'event_id': event_id })))



class RealtimeResponseResource(BaseRealtimeConnectionResource):
    
    def create(self = None, *, event_id, response):
        """
        This event instructs the server to create a Response, which means triggering
        model inference. When in Server VAD mode, the server will create Responses
        automatically.

        A Response will include at least one Item, and may have two, in which case
        the second will be a function call. These Items will be appended to the
        conversation history.

        The server will respond with a `response.created` event, events for Items
        and content created, and finally a `response.done` event to indicate the
        Response is complete.

        The `response.create` event includes inference configuration like
        `instructions`, and `temperature`. These fields will override the Session's
        configuration for this Response only.
        """
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'response.create',
            'event_id': event_id,
            'response': response })))

    
    def cancel(self = None, *, event_id, response_id):
        '''Send this event to cancel an in-progress response.

        The server will respond
        with a `response.done` event with a status of `response.status=cancelled`. If
        there is no response to cancel, the server will respond with an error.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'response.cancel',
            'event_id': event_id,
            'response_id': response_id })))



class RealtimeInputAudioBufferResource(BaseRealtimeConnectionResource):
    
    def clear(self = None, *, event_id):
        '''Send this event to clear the audio bytes in the buffer.

        The server will
        respond with an `input_audio_buffer.cleared` event.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'input_audio_buffer.clear',
            'event_id': event_id })))

    
    def commit(self = None, *, event_id):
        '''
        Send this event to commit the user input audio buffer, which will create a
        new user message item in the conversation. This event will produce an error
        if the input audio buffer is empty. When in Server VAD mode, the client does
        not need to send this event, the server will commit the audio buffer
        automatically.

        Committing the input audio buffer will trigger input audio transcription
        (if enabled in session configuration), but it will not create a response
        from the model. The server will respond with an `input_audio_buffer.committed`
        event.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'input_audio_buffer.commit',
            'event_id': event_id })))

    
    def append(self = None, *, audio, event_id):
        '''Send this event to append audio bytes to the input audio buffer.

        The audio
        buffer is temporary storage you can write to and later commit. In Server VAD
        mode, the audio buffer is used to detect speech and the server will decide
        when to commit. When Server VAD is disabled, you must commit the audio buffer
        manually.

        The client may choose how much audio to place in each event up to a maximum
        of 15 MiB, for example streaming smaller chunks from the client may allow the
        VAD to be more responsive. Unlike made other client events, the server will
        not send a confirmation response to this event.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'input_audio_buffer.append',
            'audio': audio,
            'event_id': event_id })))



class RealtimeConversationResource(BaseRealtimeConnectionResource):
    item = (lambda self = None: RealtimeConversationItemResource(self._connection))()


class RealtimeConversationItemResource(BaseRealtimeConnectionResource):
    
    def delete(self = None, *, item_id, event_id):
        '''Send this event when you want to remove any item from the conversation
        history.

        The server will respond with a `conversation.item.deleted` event,
        unless the item does not exist in the conversation history, in which case the
        server will respond with an error.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'conversation.item.delete',
            'item_id': item_id,
            'event_id': event_id })))

    
    def create(self = None, *, item, event_id, previous_item_id):
        '''
        Add a new Item to the Conversation\'s context, including messages, function
        calls, and function call responses. This event can be used both to populate a
        "history" of the conversation and to add new items mid-stream, but has the
        current limitation that it cannot populate assistant audio messages.

        If successful, the server will respond with a `conversation.item.created`
        event, otherwise an `error` event will be sent.
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'conversation.item.create',
            'item': item,
            'event_id': event_id,
            'previous_item_id': previous_item_id })))

    
    def truncate(self = None, *, audio_end_ms, content_index, item_id, event_id):
        """Send this event to truncate a previous assistant message’s audio.

        The server
        will produce audio faster than realtime, so this event is useful when the user
        interrupts to truncate audio that has already been sent to the client but not
        yet played. This will synchronize the server's understanding of the audio with
        the client's playback.

        Truncating audio will delete the server-side text transcript to ensure there
        is not text in the context that hasn't been heard by the user.

        If successful, the server will respond with a `conversation.item.truncated`
        event.
        """
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'conversation.item.truncate',
            'audio_end_ms': audio_end_ms,
            'content_index': content_index,
            'item_id': item_id,
            'event_id': event_id })))

    
    def retrieve(self = None, *, item_id, event_id):
        """
        Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.
        The server will respond with a `conversation.item.retrieved` event,
        unless the item does not exist in the conversation history, in which case the
        server will respond with an error.
        """
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'conversation.item.retrieve',
            'item_id': item_id,
            'event_id': event_id })))



class RealtimeOutputAudioBufferResource(BaseRealtimeConnectionResource):
    
    def clear(self = None, *, event_id):
        '''**WebRTC Only:** Emit to cut off the current audio response.

        This will trigger the server to
        stop generating audio and emit a `output_audio_buffer.cleared` event. This
        event should be preceded by a `response.cancel` client event to stop the
        generation of the current response.
        [Learn more](https://platform.openai.com/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).
        '''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'output_audio_buffer.clear',
            'event_id': event_id })))



class RealtimeTranscriptionSessionResource(BaseRealtimeConnectionResource):
    
    def update(self = None, *, session, event_id):
        '''Send this event to update a transcription session.'''
        self._connection.send(cast(RealtimeClientEventParam, strip_not_given({
            'type': 'transcription_session.update',
            'session': session,
            'event_id': event_id })))



class BaseAsyncRealtimeConnectionResource:
    
    def __init__(self = None, connection = None):
        self._connection = connection



class AsyncRealtimeSessionResource(BaseAsyncRealtimeConnectionResource):
    
    async def update(self = None, *, session, event_id):
        '''
        Send this event to update the session’s default configuration.
        The client may send this event at any time to update any field,
        except for `voice`. However, note that once a session has been
        initialized with a particular `model`, it can’t be changed to
        another model using `session.update`.

        When the server receives a `session.update`, it will respond
        with a `session.updated` event showing the full, effective configuration.
        Only the fields that are present are updated. To clear a field like
        `instructions`, pass an empty string.
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncRealtimeResponseResource(BaseAsyncRealtimeConnectionResource):
    
    async def create(self = None, *, event_id, response):
        """
        This event instructs the server to create a Response, which means triggering
        model inference. When in Server VAD mode, the server will create Responses
        automatically.

        A Response will include at least one Item, and may have two, in which case
        the second will be a function call. These Items will be appended to the
        conversation history.

        The server will respond with a `response.created` event, events for Items
        and content created, and finally a `response.done` event to indicate the
        Response is complete.

        The `response.create` event includes inference configuration like
        `instructions`, and `temperature`. These fields will override the Session's
        configuration for this Response only.
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, *, event_id, response_id):
        '''Send this event to cancel an in-progress response.

        The server will respond
        with a `response.done` event with a status of `response.status=cancelled`. If
        there is no response to cancel, the server will respond with an error.
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncRealtimeInputAudioBufferResource(BaseAsyncRealtimeConnectionResource):
    
    async def clear(self = None, *, event_id):
        '''Send this event to clear the audio bytes in the buffer.

        The server will
        respond with an `input_audio_buffer.cleared` event.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def commit(self = None, *, event_id):
        '''
        Send this event to commit the user input audio buffer, which will create a
        new user message item in the conversation. This event will produce an error
        if the input audio buffer is empty. When in Server VAD mode, the client does
        not need to send this event, the server will commit the audio buffer
        automatically.

        Committing the input audio buffer will trigger input audio transcription
        (if enabled in session configuration), but it will not create a response
        from the model. The server will respond with an `input_audio_buffer.committed`
        event.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def append(self = None, *, audio, event_id):
        '''Send this event to append audio bytes to the input audio buffer.

        The audio
        buffer is temporary storage you can write to and later commit. In Server VAD
        mode, the audio buffer is used to detect speech and the server will decide
        when to commit. When Server VAD is disabled, you must commit the audio buffer
        manually.

        The client may choose how much audio to place in each event up to a maximum
        of 15 MiB, for example streaming smaller chunks from the client may allow the
        VAD to be more responsive. Unlike made other client events, the server will
        not send a confirmation response to this event.
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncRealtimeConversationResource(BaseAsyncRealtimeConnectionResource):
    item = (lambda self = None: AsyncRealtimeConversationItemResource(self._connection))()


class AsyncRealtimeConversationItemResource(BaseAsyncRealtimeConnectionResource):
    
    async def delete(self = None, *, item_id, event_id):
        '''Send this event when you want to remove any item from the conversation
        history.

        The server will respond with a `conversation.item.deleted` event,
        unless the item does not exist in the conversation history, in which case the
        server will respond with an error.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create(self = None, *, item, event_id, previous_item_id):
        '''
        Add a new Item to the Conversation\'s context, including messages, function
        calls, and function call responses. This event can be used both to populate a
        "history" of the conversation and to add new items mid-stream, but has the
        current limitation that it cannot populate assistant audio messages.

        If successful, the server will respond with a `conversation.item.created`
        event, otherwise an `error` event will be sent.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def truncate(self = None, *, audio_end_ms, content_index, item_id, event_id):
        """Send this event to truncate a previous assistant message’s audio.

        The server
        will produce audio faster than realtime, so this event is useful when the user
        interrupts to truncate audio that has already been sent to the client but not
        yet played. This will synchronize the server's understanding of the audio with
        the client's playback.

        Truncating audio will delete the server-side text transcript to ensure there
        is not text in the context that hasn't been heard by the user.

        If successful, the server will respond with a `conversation.item.truncated`
        event.
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, *, item_id, event_id):
        """
        Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.
        The server will respond with a `conversation.item.retrieved` event,
        unless the item does not exist in the conversation history, in which case the
        server will respond with an error.
        """
        pass
    # WARNING: Decompyle incomplete



class AsyncRealtimeOutputAudioBufferResource(BaseAsyncRealtimeConnectionResource):
    
    async def clear(self = None, *, event_id):
        '''**WebRTC Only:** Emit to cut off the current audio response.

        This will trigger the server to
        stop generating audio and emit a `output_audio_buffer.cleared` event. This
        event should be preceded by a `response.cancel` client event to stop the
        generation of the current response.
        [Learn more](https://platform.openai.com/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncRealtimeTranscriptionSessionResource(BaseAsyncRealtimeConnectionResource):
    
    async def update(self = None, *, session, event_id):
        '''Send this event to update a transcription session.'''
        pass
    # WARNING: Decompyle incomplete
