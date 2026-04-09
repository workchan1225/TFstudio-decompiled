# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utilities.pyc (Python 3.11)

'''Utilities for the gRPC Python Beta API.'''
import threading
import time
from grpc.beta import implementations
from grpc.beta import interfaces
from grpc.framework.foundation import callable_util
from grpc.framework.foundation import future
_DONE_CALLBACK_EXCEPTION_LOG_MESSAGE = 'Exception calling connectivity future "done" callback!'

class _ChannelReadyFuture(future.Future):
    
    def __init__(self, channel):
        self._condition = threading.Condition()
        self._channel = channel
        self._matured = False
        self._cancelled = False
        self._done_callbacks = []

    
    def _block(self, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def _update(self, connectivity):
        self._condition
        if self._cancelled and connectivity is interfaces.ChannelConnectivity.READY:
            self._matured = True
            self._channel.unsubscribe(self._update)
            self._condition.notify_all()
            done_callbacks = tuple(self._done_callbacks)
            self._done_callbacks = None
        else:
            None(None, None)
            return None
        None(None, None)

    
    def cancel(self):
        self._condition
        if not self._matured:
            self._cancelled = True
            self._channel.unsubscribe(self._update)
            self._condition.notify_all()
            done_callbacks = tuple(self._done_callbacks)
            self._done_callbacks = None
        else:
            None(None, None)
            return False
        None(None, None)

    
    def cancelled(self):
        self._condition
        None(None, None)
        return 
        with None:
            if not None, self._cancelled:
                pass

    
    def running(self):
        self._condition
        if not (self._cancelled):
            None(None, None)
            return 
        with None:
            if not not (self._cancelled):
                pass

    
    def done(self):
        self._condition
        if not self._cancelled:
            None(None, None)
            return 
        with None:
            if not self._cancelled:
                pass

    
    def result(self, timeout = (None,)):
        self._block(timeout)

    
    def exception(self, timeout = (None,)):
        self._block(timeout)

    
    def traceback(self, timeout = (None,)):
        self._block(timeout)

    
    def add_done_callback(self, fn):
        self._condition
        if not self._cancelled and self._matured:
            self._done_callbacks.append(fn)
            None(None, None)
            return None
        None(None, None)

    
    def start(self):
        self._condition
        self._channel.subscribe(self._update, try_to_connect = True)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def __del__(self):
        self._condition
        if not self._cancelled and self._matured:
            self._channel.unsubscribe(self._update)
        None(None, None)
        return None
        with None:
            if not None:
                pass



def channel_ready_future(channel):
    """Creates a future.Future tracking when an implementations.Channel is ready.

    Cancelling the returned future.Future does not tell the given
    implementations.Channel to abandon attempts it may have been making to
    connect; cancelling merely deactivates the return future.Future's
    subscription to the given implementations.Channel's connectivity.

    Args:
      channel: An implementations.Channel.

    Returns:
      A future.Future that matures when the given Channel has connectivity
        interfaces.ChannelConnectivity.READY.
    """
    ready_future = _ChannelReadyFuture(channel)
    ready_future.start()
    return ready_future
