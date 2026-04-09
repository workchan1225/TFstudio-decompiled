# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: voices.pyc (Python 3.11)

'''This module contains functions to list all available voices and a class to find the
correct voice based on their attributes.'''
import json
import ssl
from typing import Any, List, Optional
import aiohttp
import certifi
from typing_extensions import Unpack
from constants import SEC_MS_GEC_VERSION, VOICE_HEADERS, VOICE_LIST
from drm import DRM
from typing import Voice, VoicesManagerFind, VoicesManagerVoice

async def __list_voices(session = None, ssl_ctx = None, proxy = None):
    '''
    Private function that makes the request to the voice list URL and parses the
    JSON response. This function is used by list_voices() and makes it easier to
    handle client response errors related to clock skew.

    Args:
        session (aiohttp.ClientSession): The aiohttp session to use for the request.
        ssl_ctx (ssl.SSLContext): The SSL context to use for the request.
        proxy (Optional[str]): The proxy to use for the request.

    Returns:
        List[Voice]: A list of voices and their attributes.
    '''
    pass
# WARNING: Decompyle incomplete


async def list_voices(*, connector, proxy):
    '''
    List all available voices and their attributes.

    This pulls data from the URL used by Microsoft Edge to return a list of
    all available voices.

    Args:
        connector (Optional[aiohttp.BaseConnector]): The connector to use for the request.
        proxy (Optional[str]): The proxy to use for the request.

    Returns:
        List[Voice]: A list of voices and their attributes.
    '''
    pass
# WARNING: Decompyle incomplete


class VoicesManager:
    '''
    A class to find the correct voice based on their attributes.
    '''
    
    def __init__(self = None):
        self.voices = []
        self.called_create = False

    create = (lambda cls = None, custom_voices = None: pass# WARNING: Decompyle incomplete
)()
    
    def find(self = None, **kwargs):
        '''
        Finds all matching voices based on the provided attributes.
        '''
        pass
    # WARNING: Decompyle incomplete
