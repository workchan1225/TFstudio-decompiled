# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: live_music.pyc (Python 3.11)

'''[Experimental] Live Music API client.'''
import contextlib
import json
import logging
from typing import AsyncIterator
from  import _api_module
from  import _common
from  import _live_converters as live_converters
from  import _transformers as t
from  import types
from _api_client import BaseApiClient
from _common import set_value_by_path as setv

try:
    from websockets.asyncio.client import ClientConnection
    from websockets.asyncio.client import connect
except ModuleNotFoundError:
    from websockets.client import ClientConnection
    from websockets.client import connect

logger = logging.getLogger('google_genai.live_music')

class AsyncMusicSession:
    '''[Experimental] AsyncMusicSession.'''
    
    def __init__(self = None, api_client = None, websocket = None):
        self._api_client = api_client
        self._ws = websocket

    
    async def set_weighted_prompts(self = None, prompts = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def set_music_generation_config(self = None, config = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_control_signal(self = None, playback_control = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def play(self = None):
        '''Sends playback signal to start the music stream.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def pause(self = None):
        '''Sends a playback signal to pause the music stream.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def stop(self = None):
        '''Sends a playback signal to stop the music stream.

    Resets the music generation context while retaining the current config.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def reset_context(self = None):
        '''Reset the context (prompts retained) without stopping the music generation.'''
        pass
    # WARNING: Decompyle incomplete

    
    def receive(self = None):
        '''Receive model responses from the server.

    Yields:
      The audio chunks from the server.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''Closes the bi-directional stream and terminates the session.'''
        pass
    # WARNING: Decompyle incomplete



class AsyncLiveMusic(_api_module.BaseModule):
    '''[Experimental] Live music module.

  Live music can be accessed via `client.aio.live.music`.
  '''
    connect = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()()
