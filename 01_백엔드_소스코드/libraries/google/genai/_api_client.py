# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _api_client.pyc (Python 3.11)

'''Base client for calling HTTP APIs sending and receiving JSON.

The BaseApiClient is intended to be a private module and is subject to change.
'''
import asyncio
from collections.abc import Generator
import copy
from dataclasses import dataclass
import inspect
import io
import json
import logging
import math
import os
import random
import ssl
import sys
import threading
import time
from typing import Any, AsyncIterator, Iterator, Optional, Tuple, TYPE_CHECKING, Union
from urllib.parse import urlparse
from urllib.parse import urlunparse
import warnings
import anyio
import certifi
import google.auth as google
import google.auth.credentials as google
from google.auth.credentials import Credentials
import httpx
from pydantic import BaseModel
from pydantic import ValidationError
import tenacity
from  import _common
from  import errors
from  import version
from types import HttpOptions
from types import HttpOptionsOrDict
from types import HttpResponse as SdkHttpResponse
from types import HttpRetryOptions
from types import ResourceScope

try:
    from websockets.asyncio.client import connect as ws_connect
except ModuleNotFoundError:
    from websockets.client import connect as ws_connect

has_aiohttp = False

try:
    import aiohttp
    has_aiohttp = True
except ImportError:
    pass

if TYPE_CHECKING:
    from multidict import CIMultiDictProxy
logger = logging.getLogger('google_genai._api_client')
CHUNK_SIZE = 8388608
READ_BUFFER_SIZE = 4194304
MAX_RETRY_COUNT = 3
INITIAL_RETRY_DELAY = 1
DELAY_MULTIPLIER = 2

class EphemeralTokenAPIKeyError(ValueError):
    '''Error raised when the API key is invalid.'''
    pass


def get_env_api_key():
