# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _api_module.pyc (Python 3.11)

'''Utilities for the API Modules of the Google Gen AI SDK.'''
from typing import Optional
from  import _api_client

class BaseModule:
    
    def __init__(self = None, api_client_ = None):
        self._api_client = api_client_

    vertexai = (lambda self = None: self._api_client.vertexai)()
