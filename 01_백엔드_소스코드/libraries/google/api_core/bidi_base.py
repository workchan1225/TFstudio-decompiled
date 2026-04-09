# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bidi_base.pyc (Python 3.11)

'''Base class for bi-directional streaming RPC helpers.'''

class BidiRpcBase:
    """A base class for consuming a bi-directional streaming RPC.

    This maps gRPC's built-in interface which uses a request iterator and a
    response iterator into a socket-like :func:`send` and :func:`recv`. This
    is a more useful pattern for long-running or asymmetric streams (streams
    where there is not a direct correlation between the requests and
    responses).

    This does *not* retry the stream on errors.

    Args:
        start_rpc (Union[grpc.StreamStreamMultiCallable,
                    grpc.aio.StreamStreamMultiCallable]): The gRPC method used
                    to start the RPC.
        initial_request (Union[protobuf.Message,
                Callable[[], protobuf.Message]]): The initial request to
            yield. This is useful if an initial request is needed to start the
            stream.
        metadata (Sequence[Tuple(str, str)]): RPC metadata to include in
            the request.
    """
    
    def __init__(self, start_rpc, initial_request, metadata = (None, None)):
        self._start_rpc = start_rpc
        self._initial_request = initial_request
        self._rpc_metadata = metadata
        self._request_queue = self._create_queue()
        self._request_generator = None
        self._callbacks = []
        self.call = None

    
    def _create_queue(self):
        '''Create a queue for requests.'''
        raise NotImplementedError('`_create_queue` is not implemented.')

    
    def add_done_callback(self, callback):
        '''Adds a callback that will be called when the RPC terminates.

        This occurs when the RPC errors or is successfully terminated.

        Args:
            callback (Union[Callable[[grpc.Future], None], Callable[[Any], None]]):
                The callback to execute after gRPC call completed (success or
                failure).

                For sync streaming gRPC: Callable[[grpc.Future], None]

                For async streaming gRPC: Callable[[Any], None]
        '''
        self._callbacks.append(callback)

    
    def _on_call_done(self, future):
        for callback in self._callbacks:
            callback(future)
            return None

    is_active = (lambda self: raise NotImplementedError('`is_active` is not implemented.'))()
    pending_requests = (lambda self: self._request_queue.qsize())()
