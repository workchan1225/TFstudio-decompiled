# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: live.pyc (Python 3.11)

'''[Preview] Live API client.'''
import asyncio
import base64
import contextlib
import json
import logging
import typing
from typing import Any, AsyncIterator, Optional, Sequence, Union, get_args
import warnings
import google.auth as google
import pydantic
from websockets import ConnectionClosed
from  import _api_module
from  import _common
from  import _live_converters as live_converters
from  import _mcp_utils
from  import _transformers as t
from  import errors
from  import types
from _api_client import BaseApiClient
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from live_music import AsyncLiveMusic
from models import _Content_to_mldev

try:
    from websockets.asyncio.client import ClientConnection
    from websockets.asyncio.client import connect as ws_connect
except ModuleNotFoundError:
    from websockets.client import ClientConnection
    from websockets.client import connect as ws_connect


try:
    from google.auth.transport import requests
except ImportError:
    requests = None

if typing.TYPE_CHECKING:
    from mcp import ClientSession as McpClientSession
    from mcp.types import Tool as McpTool
    from _adapters import McpToGenAiToolAdapter
    from _mcp_utils import mcp_to_gemini_tool
else:
    McpClientSession: typing.Type = Any
    McpTool: typing.Type = Any
    McpToGenAiToolAdapter: typing.Type = Any
    
    try:
        from mcp import ClientSession as McpClientSession
        from mcp.types import Tool as McpTool
        from _adapters import McpToGenAiToolAdapter
        from _mcp_utils import mcp_to_gemini_tool
    except ImportError:
        McpClientSession = None
        McpTool = None
        McpToGenAiToolAdapter = None
        mcp_to_gemini_tool = None

    logger = logging.getLogger('google_genai.live')
    _FUNCTION_RESPONSE_REQUIRES_ID = 'FunctionResponse request must have an `id` field from the response of a ToolCall.FunctionalCalls in Google AI.'
    
    class AsyncSession:
        '''[Preview] AsyncSession.'''
        
        def __init__(self = None, api_client = None, websocket = None, session_id = (None,)):
            self._api_client = api_client
            self._ws = websocket
            self.session_id = session_id

        
        async def send(self = None, *, input, end_of_turn):
            """[Deprecated] Send input to the model.

    > **Warning**: This method is deprecated and will be removed in a future
    version (not before Q3 2025). Please use one of the more specific methods:
    `send_client_content`, `send_realtime_input`, or `send_tool_response`
    instead.

    The method will send the input request to the server.

    Args:
      input: The input request to the model.
      end_of_turn: Whether the input is the last message in a turn.

    Example usage:

    .. code-block:: python

      client = genai.Client(api_key=API_KEY)

      async with client.aio.live.connect(model='...') as session:
        await session.send(input='Hello world!', end_of_turn=True)
        async for message in session.receive():
          print(message)
    """
            pass
        # WARNING: Decompyle incomplete

        
        async def send_client_content(self = None, *, turns, turn_complete):
            '''Send non-realtime, turn based content to the model.

    There are two ways to send messages to the live API:
    `send_client_content` and `send_realtime_input`.

    `send_client_content` messages are added to the model context **in order**.
    Having a conversation using `send_client_content` messages is roughly
    equivalent to using the `Chat.send_message_stream` method, except that the
    state of the `chat` history is stored on the API server.

    Because of `send_client_content`\'s order guarantee, the model cannot
    respond as quickly to `send_client_content` messages as to
    `send_realtime_input` messages. This makes the biggest difference when
    sending objects that have significant preprocessing time (typically images).

    The `send_client_content` message sends a list of `Content` objects,
    which has more options than the `media:Blob` sent by `send_realtime_input`.

    The main use-cases for `send_client_content` over `send_realtime_input` are:

    - Prefilling a conversation context (including sending anything that can\'t
      be represented as a realtime message), before starting a realtime
      conversation.
    - Conducting a non-realtime conversation, similar to `client.chat`, using
      the live api.

    Caution: Interleaving `send_client_content` and `send_realtime_input`
      in the same conversation is not recommended and can lead to unexpected
      results.

    Args:
      turns: A `Content` object or list of `Content` objects (or equivalent
        dicts).
      turn_complete: if true (the default) the model will reply immediately. If
        false, the model will wait for you to send additional client_content,
        and will not return until you send `turn_complete=True`.

    Example:

    .. code-block:: python

      import google.genai
      from google.genai import types
      import os

      if os.environ.get(\'GOOGLE_GENAI_USE_VERTEXAI\'):
        MODEL_NAME = \'gemini-2.0-flash-live-preview-04-09\'
      else:
        MODEL_NAME = \'gemini-live-2.5-flash-preview\';

      client = genai.Client()
      async with client.aio.live.connect(
          model=MODEL_NAME,
          config={"response_modalities": ["TEXT"]}
      ) as session:
        await session.send_client_content(
            turns=types.Content(
                role=\'user\',
                parts=[types.Part(text="Hello world!")]))
        async for msg in session.receive():
          if msg.text:
            print(msg.text)
    '''
            pass
        # WARNING: Decompyle incomplete

        
        async def send_realtime_input(self = None, *, media, audio, audio_stream_end, video, text, activity_start, activity_end):
            '''Send realtime input to the model, only send one argument per call.

    Use `send_realtime_input` for realtime audio chunks and video
    frames(images).

    With `send_realtime_input` the api will respond to audio automatically
    based on voice activity detection (VAD).

    `send_realtime_input` is optimized for responsivness at the expense of
    deterministic ordering. Audio and video tokens are added to the
    context when they become available.

    Args:
      media: A `Blob`-like object, the realtime media to send.

    Example:

    .. code-block:: python

      from pathlib import Path

      from google import genai
      from google.genai import types

      import PIL.Image

      import os

      if os.environ.get(\'GOOGLE_GENAI_USE_VERTEXAI\'):
        MODEL_NAME = \'gemini-2.0-flash-live-preview-04-09\'
      else:
        MODEL_NAME = \'gemini-live-2.5-flash-preview\';


      client = genai.Client()

      async with client.aio.live.connect(
          model=MODEL_NAME,
          config={"response_modalities": ["TEXT"]},
      ) as session:
        await session.send_realtime_input(
            media=PIL.Image.open(\'image.jpg\'))

        audio_bytes = Path(\'audio.pcm\').read_bytes()
        await session.send_realtime_input(
            media=types.Blob(data=audio_bytes, mime_type=\'audio/pcm;rate=16000\'))

        async for msg in session.receive():
          if msg.text is not None:
            print(f\'{msg.text}\')
    '''
            pass
        # WARNING: Decompyle incomplete

        
        async def send_tool_response(self = None, *, function_responses):
            '''Send a tool response to the session.

    Use `send_tool_response` to reply to `LiveServerToolCall` messages
    from the server.

    To set the available tools, use the `config.tools` argument
    when you connect to the session (`client.live.connect`).

    Args:
      function_responses: A `FunctionResponse`-like object or list of
        `FunctionResponse`-like objects.

    Example:

    .. code-block:: python

      from google import genai
      from google.genai import types

      import os

      if os.environ.get(\'GOOGLE_GENAI_USE_VERTEXAI\'):
        MODEL_NAME = \'gemini-2.0-flash-live-preview-04-09\'
      else:
        MODEL_NAME = \'gemini-live-2.5-flash-preview\';

      client = genai.Client()

      tools = [{\'function_declarations\': [{\'name\': \'turn_on_the_lights\'}]}]
      config = {
          "tools": tools,
          "response_modalities": [\'TEXT\']
      }

      async with client.aio.live.connect(
          model=\'models/gemini-live-2.5-flash-preview\',
          config=config
      ) as session:
        prompt = "Turn on the lights please"
        await session.send_client_content(
            turns={"parts": [{\'text\': prompt}]}
        )

        async for chunk in session.receive():
            if chunk.server_content:
              if chunk.text is not None:
                print(chunk.text)
            elif chunk.tool_call:
              print(chunk.tool_call)
              print(\'_\'*80)
              function_response=types.FunctionResponse(
                      name=\'turn_on_the_lights\',
                      response={\'result\': \'ok\'},
                      id=chunk.tool_call.function_calls[0].id,
                  )
              print(function_response)
              await session.send_tool_response(
                  function_responses=function_response
              )

              print(\'_\'*80)
    '''
            pass
        # WARNING: Decompyle incomplete

        
        def receive(self = None):
            """Receive model responses from the server.

    The method will yield the model responses from the server. The returned
    responses will represent a complete model turn. When the returned message
    is function call, user must call `send` with the function response to
    continue the turn.

    Yields:
      The model responses from the server.

    Example usage:

    .. code-block:: python

      client = genai.Client(api_key=API_KEY)

      async with client.aio.live.connect(model='...') as session:
        await session.send(input='Hello world!', end_of_turn=True)
        async for message in session.receive():
          print(message)
    """
            pass
        # WARNING: Decompyle incomplete

        
        def start_stream(self = None, *, stream, mime_type):
            """[Deprecated] Start a live session from a data stream.

    > **Warning**: This method is deprecated and will be removed in a future
    version (not before Q2 2025). Please use one of the more specific methods:
    `send_client_content`, `send_realtime_input`, or `send_tool_response`
    instead.

    The interaction terminates when the input stream is complete.
    This method will start two async tasks. One task will be used to send the
    input stream to the model and the other task will be used to receive the
    responses from the model.

    Args:
      stream: An iterator that yields the model response.
      mime_type: The MIME type of the data in the stream.

    Yields:
      The audio bytes received from the model and server response messages.

    Example usage:

    .. code-block:: python

      client = genai.Client(api_key=API_KEY)
      config = {'response_modalities': ['AUDIO']}
      async def audio_stream():
        stream = read_audio()
        for data in stream:
          yield data
      async with client.aio.live.connect(model='...', config=config) as session:
        for audio in session.start_stream(stream = audio_stream(),
        mime_type = 'audio/pcm'):
          play_audio_chunk(audio.data)
    """
            pass
        # WARNING: Decompyle incomplete

        
        async def _receive(self = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def _send_loop(self = None, data_stream = None, mime_type = None, stop_event = ('data_stream', AsyncIterator[bytes], 'mime_type', str, 'stop_event', asyncio.Event, 'return', None)):
            pass
        # WARNING: Decompyle incomplete

        
        def _parse_client_message(self = None, input = None, end_of_turn = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def close(self = None):
            pass
        # WARNING: Decompyle incomplete


    
    class AsyncLive(_api_module.BaseModule):
        pass
    # WARNING: Decompyle incomplete

    
    async def _t_live_connect_config(api_client = None, config = None):
        pass
    # WARNING: Decompyle incomplete

    return None
