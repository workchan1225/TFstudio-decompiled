# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stream_util.pyc (Python 3.11)

'''Helpful utilities related to the stream module.'''
import logging
import threading
from grpc.framework.foundation import stream
_NO_VALUE = object()
_LOGGER = logging.getLogger(__name__)

class TransformingConsumer(stream.Consumer):
    '''A stream.Consumer that passes a transformation of its input to another.'''
    
    def __init__(self, transformation, downstream):
        self._transformation = transformation
        self._downstream = downstream

    
    def consume(self, value):
        self._downstream.consume(self._transformation(value))

    
    def terminate(self):
        self._downstream.terminate()

    
    def consume_and_terminate(self, value):
        self._downstream.consume_and_terminate(self._transformation(value))



class IterableConsumer(stream.Consumer):
    '''A Consumer that when iterated over emits the values it has consumed.'''
    
    def __init__(self):
        self._condition = threading.Condition()
        self._values = []
        self._active = True

    
    def consume(self, value):
        self._condition
        if self._active:
            self._values.append(value)
            self._condition.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def terminate(self):
        self._condition
        self._active = False
        self._condition.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def consume_and_terminate(self, value):
        self._condition
        if self._active:
            self._values.append(value)
            self._active = False
            self._condition.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def __iter__(self):
        return self

    
    def __next__(self):
        return self.next()

    
    def next(self):
        self._condition
    # WARNING: Decompyle incomplete



class ThreadSwitchingConsumer(stream.Consumer):
    '''A Consumer decorator that affords serialization and asynchrony.'''
    
    def __init__(self, sink, pool):
        self._lock = threading.Lock()
        self._sink = sink
        self._pool = pool
        self._spinning = False
        self._values = []
        self._active = True

    
    def _spin(self, sink, value, terminate):
        
        try:
            if value is _NO_VALUE:
                sink.terminate()
            elif terminate:
                sink.consume_and_terminate(value)
            else:
                sink.consume(value)
        except Exception:
            e = None
            _LOGGER.exception(e)
            e = None
            del e
        except:
            e = None
            del e

        self._lock
        if terminate:
            self._spinning = False
            None(None, None)
            return None
        if None._values:
            value = self._values.pop(0)
            if not (self._values):
                terminate = not (self._active)
            elif not self._active:
                value = _NO_VALUE
                terminate = True
            else:
                self._spinning = False
                None(None, None)
                return None
            not (self._values)(None, None)
        else:
            with None:
                if not None:
                    pass
        continue

    
    def consume(self, value):
        self._lock
        if self._active:
            if self._spinning:
                self._values.append(value)
            else:
                self._pool.submit(self._spin, self._sink, value, False)
                self._spinning = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def terminate(self):
        self._lock
        if self._active:
            self._active = False
            if not self._spinning:
                self._pool.submit(self._spin, self._sink, _NO_VALUE, True)
                self._spinning = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def consume_and_terminate(self, value):
        self._lock
        if self._active:
            self._active = False
            if self._spinning:
                self._values.append(value)
            else:
                self._pool.submit(self._spin, self._sink, value, True)
                self._spinning = True
        None(None, None)
        return None
        with None:
            if not None:
                pass
