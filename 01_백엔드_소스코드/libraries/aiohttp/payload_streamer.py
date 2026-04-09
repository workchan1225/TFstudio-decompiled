# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: payload_streamer.pyc (Python 3.11)

"""
Payload implementation for coroutines as data provider.

As a simple case, you can upload data from file::

   @aiohttp.streamer
   async def file_sender(writer, file_name=None):
      with open(file_name, 'rb') as f:
          chunk = f.read(2**16)
          while chunk:
              await writer.write(chunk)

              chunk = f.read(2**16)

Then you can use `file_sender` like this:

    async with session.post('http://httpbin.org/post',
                            data=file_sender(file_name='huge_file')) as resp:
        print(await resp.text())

..note:: Coroutine must accept `writer` as first argument

"""
import types
import warnings
from typing import Any, Awaitable, Callable, Dict, Tuple
from abc import AbstractStreamWriter
from payload import Payload, payload_type
__all__ = ('streamer',)

class _stream_wrapper:
    
    def __init__(self = None, coro = None, args = None, kwargs = ('coro', Callable[(..., Awaitable[None])], 'args', Tuple[(Any, ...)], 'kwargs', Dict[(str, Any)], 'return', None)):
        self.coro = types.coroutine(coro)
        self.args = args
        self.kwargs = kwargs

    
    async def __call__(self = None, writer = None):
        pass
    # WARNING: Decompyle incomplete



class streamer:
    
    def __init__(self = None, coro = None):
        warnings.warn('@streamer is deprecated, use async generators instead', DeprecationWarning, stacklevel = 2)
        self.coro = coro

    
    def __call__(self = None, *args, **kwargs):
        return _stream_wrapper(self.coro, args, kwargs)


StreamWrapperPayload = <NODE:12>()
StreamPayload = <NODE:12>()
