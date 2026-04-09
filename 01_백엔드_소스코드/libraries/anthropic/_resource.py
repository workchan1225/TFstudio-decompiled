# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _resource.pyc (Python 3.11)

from __future__ import annotations
import time
import anyio
from _base_client import SyncAPIClient, AsyncAPIClient

class SyncAPIResource:
    _client: 'SyncAPIClient' = 'SyncAPIResource'
    
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
    _client: 'AsyncAPIClient' = 'AsyncAPIResource'
    
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
