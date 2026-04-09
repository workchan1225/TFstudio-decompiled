# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _resource.pyc (Python 3.11)

from __future__ import annotations
import time
from typing import TYPE_CHECKING
import anyio
if TYPE_CHECKING:
    from _client import OpenAI, AsyncOpenAI

class SyncAPIResource:
    _client: 'OpenAI' = 'SyncAPIResource'
    
    def __init__(self = None, client = None):
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    
    def _sleep(self = None, seconds = None):
        time.sleep(seconds)



class AsyncAPIResource:
    _client: 'AsyncOpenAI' = 'AsyncAPIResource'
    
    def __init__(self = None, client = None):
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    
    async def _sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
