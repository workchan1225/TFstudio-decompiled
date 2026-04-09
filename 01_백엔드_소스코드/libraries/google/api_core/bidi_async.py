# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bidi_async.pyc (Python 3.11)

'''Asynchronous bi-directional streaming RPC helpers.'''
import asyncio
import logging
from typing import Callable, Optional, Union
from grpc import aio
from google.api_core import exceptions
from google.api_core.bidi_base import BidiRpcBase
from google.protobuf.message import Message as ProtobufMessage
_LOGGER = logging.getLogger(__name__)

class _AsyncRequestQueueGenerator:
    """_AsyncRequestQueueGenerator is a helper class for sending asynchronous
      requests to a gRPC stream from a Queue.

    This generator takes asynchronous requests off a given `asyncio.Queue` and
    yields them to gRPC.

    It's useful when you have an indeterminate, indefinite, or otherwise
    open-ended set of requests to send through a request-streaming (or
    bidirectional) RPC.

    Example::

        requests = _AsyncRequestQueueGenerator(q)
        call = await stub.StreamingRequest(requests)
        requests.call = call

        async for response in call:
            print(response)
            await q.put(...)

    Args:
        queue (asyncio.Queue): The request queue.
        initial_request (Union[ProtobufMessage,
                Callable[[], ProtobufMessage]]): The initial request to
            yield. This is done independently of the request queue to allow for
            easily restarting streams that require some initial configuration
            request.
    """
    
    def __init__(self = None, queue = None, initial_request = None):
        self._queue = queue
        self._initial_request = initial_request
        self.call = None

    
    def _is_active(self = None):
        '''Returns true if the call is not set or not completed.'''
        if not self.call is None:
            pass
        return not self.call.done()

    
    def __aiter__(self):
        pass
    # WARNING: Decompyle incomplete



class AsyncBidiRpc(BidiRpcBase):
    """A helper for consuming a async bi-directional streaming RPC.

    This maps gRPC's built-in interface which uses a request iterator and a
    response iterator into a socket-like :func:`send` and :func:`recv`. This
    is a more useful pattern for long-running or asymmetric streams (streams
    where there is not a direct correlation between the requests and
    responses).

    Example::

        initial_request = example_pb2.StreamingRpcRequest(
            setting='example')
        rpc = AsyncBidiRpc(
            stub.StreamingRpc,
            initial_request=initial_request,
            metadata=[('name', 'value')]
        )

        await rpc.open()

        while rpc.is_active:
            print(await rpc.recv())
            await rpc.send(example_pb2.StreamingRpcRequest(
                data='example'))

        await rpc.close()

    This does *not* retry the stream on errors.

    Args:
        start_rpc (grpc.aio.StreamStreamMultiCallable): The gRPC method used to
            start the RPC.
        initial_request (Union[ProtobufMessage,
                Callable[[], ProtobufMessage]]): The initial request to
            yield. This is useful if an initial request is needed to start the
            stream.
        metadata (Sequence[Tuple(str, str)]): RPC metadata to include in
            the request.
    """
    
    def _create_queue(self = None):
        '''Create a queue for requests.'''
        return asyncio.Queue()

    
    async def open(self = None):
        '''Opens the stream.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''Closes the stream.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, request = None):
        '''Queue a message to be sent on the stream.

        If the underlying RPC has been closed, this will raise.

        Args:
            request (ProtobufMessage): The request to send.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def recv(self = None):
        '''Wait for a message to be returned from the stream.

        If the underlying RPC has been closed, this will raise.

        Returns:
            ProtobufMessage: The received message.
        '''
        pass
    # WARNING: Decompyle incomplete

    is_active = (lambda self = None: if self.call is not None:
passnot self.call.done())()
