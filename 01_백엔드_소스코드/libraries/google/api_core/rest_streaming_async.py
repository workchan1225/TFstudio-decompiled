# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest_streaming_async.pyc (Python 3.11)

'''Helpers for asynchronous server-side streaming in REST.'''
from typing import Union
import proto

try:
    import google.auth.aio.transport as google
except ImportError:
    e = None
    raise ImportError('`google-api-core[async_rest]` is required to use asynchronous rest streaming. Install the `async_rest` extra of `google-api-core` using `pip install google-api-core[async_rest]`.'), e
    e = None
    del e

import google.protobuf.message as google
from google.api_core._rest_streaming_base import BaseResponseIterator

class AsyncResponseIterator(BaseResponseIterator):
    pass
# WARNING: Decompyle incomplete
