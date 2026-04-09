# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _server_adaptations.pyc (Python 3.11)

"""Translates gRPC's server-side API into gRPC's server-side Beta API."""
import collections
import threading
import grpc
from grpc import _common
from grpc.beta import _metadata
from grpc.beta import interfaces
from grpc.framework.common import cardinality
from grpc.framework.common import style
from grpc.framework.foundation import abandonment
from grpc.framework.foundation import logging_pool
from grpc.framework.foundation import stream
from grpc.framework.interfaces.face import face
_DEFAULT_POOL_SIZE = 8

class _ServerProtocolContext(interfaces.GRPCServicerContext):
    
    def __init__(self, servicer_context):
        self._servicer_context = servicer_context

    
    def peer(self):
        return self._servicer_context.peer()

    
    def disable_next_response_compression(self):
        pass



class _FaceServicerContext(face.ServicerContext):
    
    def __init__(self, servicer_context):
        self._servicer_context = servicer_context

    
    def is_active(self):
        return self._servicer_context.is_active()

    
    def time_remaining(self):
        return self._servicer_context.time_remaining()

    
    def add_abortion_callback(self, abortion_callback):
        error_msg = 'add_abortion_callback no longer supported server-side!'
        raise NotImplementedError(error_msg)

    
    def cancel(self):
        self._servicer_context.cancel()

    
    def protocol_context(self):
        return _ServerProtocolContext(self._servicer_context)

    
    def invocation_metadata(self):
        return _metadata.beta(self._servicer_context.invocation_metadata())

    
    def initial_metadata(self, initial_metadata):
        self._servicer_context.send_initial_metadata(_metadata.unbeta(initial_metadata))

    
    def terminal_metadata(self, terminal_metadata):
        self._servicer_context.set_terminal_metadata(_metadata.unbeta(terminal_metadata))

    
    def code(self, code):
        self._servicer_context.set_code(code)

    
    def details(self, details):
        self._servicer_context.set_details(details)



def _adapt_unary_request_inline(unary_request_inline):
    pass
# WARNING: Decompyle incomplete


def _adapt_stream_request_inline(stream_request_inline):
    pass
# WARNING: Decompyle incomplete


class _Callback(stream.Consumer):
    
    def __init__(self):
        self._condition = threading.Condition()
        self._values = []
        self._terminated = False
        self._cancelled = False

    
    def consume(self, value):
        self._condition
        self._values.append(value)
        self._condition.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def terminate(self):
        self._condition
        self._terminated = True
        self._condition.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def consume_and_terminate(self, value):
        self._condition
        self._values.append(value)
        self._terminated = True
        self._condition.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def cancel(self):
        self._condition
        self._cancelled = True
        self._condition.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def draw_one_value(self):
        self._condition
        if self._cancelled:
            raise abandonment.Abandoned()
        if self._values:
            None(None, None)
            return 
        if None._terminated:
            None(None, None)
            return None
        None._condition.wait()
        continue
        with None:
            if not None:
                pass

    
    def draw_all_values(self):
        self._condition
        if self._cancelled:
            raise abandonment.Abandoned()
        if self._terminated:
            all_values = tuple(self._values)
            self._values = None
            None(None, None)
            return 
        None._condition.wait()
        continue
        with None:
            if not None:
                pass



def _run_request_pipe_thread(request_iterator, request_consumer, servicer_context):
    pass
# WARNING: Decompyle incomplete


def _adapt_unary_unary_event(unary_unary_event):
    pass
# WARNING: Decompyle incomplete


def _adapt_unary_stream_event(unary_stream_event):
    pass
# WARNING: Decompyle incomplete


def _adapt_stream_unary_event(stream_unary_event):
    pass
# WARNING: Decompyle incomplete


def _adapt_stream_stream_event(stream_stream_event):
    pass
# WARNING: Decompyle incomplete


def _SimpleMethodHandler():
    '''_SimpleMethodHandler'''
    pass

_SimpleMethodHandler = <NODE:27>(_SimpleMethodHandler, '_SimpleMethodHandler', collections.namedtuple('_MethodHandler', ('request_streaming', 'response_streaming', 'request_deserializer', 'response_serializer', 'unary_unary', 'unary_stream', 'stream_unary', 'stream_stream')), grpc.RpcMethodHandler)

def _simple_method_handler(implementation, request_deserializer, response_serializer):
    if implementation.style is style.Service.INLINE:
        if implementation.cardinality is cardinality.Cardinality.UNARY_UNARY:
            return _SimpleMethodHandler(False, False, request_deserializer, response_serializer, _adapt_unary_request_inline(implementation.unary_unary_inline), None, None, None)
        if None.cardinality is cardinality.Cardinality.UNARY_STREAM:
            return _SimpleMethodHandler(False, True, request_deserializer, response_serializer, None, _adapt_unary_request_inline(implementation.unary_stream_inline), None, None)
        if None.cardinality is cardinality.Cardinality.STREAM_UNARY:
            return _SimpleMethodHandler(True, False, request_deserializer, response_serializer, None, None, _adapt_stream_request_inline(implementation.stream_unary_inline), None)
        if None.cardinality is cardinality.Cardinality.STREAM_STREAM:
            return _SimpleMethodHandler(True, True, request_deserializer, response_serializer, None, None, None, _adapt_stream_request_inline(implementation.stream_stream_inline))
    if implementation.style is style.Service.EVENT:
        if implementation.cardinality is cardinality.Cardinality.UNARY_UNARY:
            return _SimpleMethodHandler(False, False, request_deserializer, response_serializer, _adapt_unary_unary_event(implementation.unary_unary_event), None, None, None)
        if None.cardinality is cardinality.Cardinality.UNARY_STREAM:
            return _SimpleMethodHandler(False, True, request_deserializer, response_serializer, None, _adapt_unary_stream_event(implementation.unary_stream_event), None, None)
        if None.cardinality is cardinality.Cardinality.STREAM_UNARY:
            return _SimpleMethodHandler(True, False, request_deserializer, response_serializer, None, None, _adapt_stream_unary_event(implementation.stream_unary_event), None)
        if None.cardinality is cardinality.Cardinality.STREAM_STREAM:
            return _SimpleMethodHandler(True, True, request_deserializer, response_serializer, None, None, None, _adapt_stream_stream_event(implementation.stream_stream_event))
        raise None()


def _flatten_method_pair_map(method_pair_map):
    if not method_pair_map:
        method_pair_map = { }
        flat_map = { }
        for method_pair in method_pair_map:
            method = _common.fully_qualified_method(method_pair[0], method_pair[1])
            flat_map[method] = method_pair_map[method_pair]
            return flat_map


class _GenericRpcHandler(grpc.GenericRpcHandler):
    
    def __init__(self, method_implementations, multi_method_implementation, request_deserializers, response_serializers):
        self._method_implementations = _flatten_method_pair_map(method_implementations)
        self._request_deserializers = _flatten_method_pair_map(request_deserializers)
        self._response_serializers = _flatten_method_pair_map(response_serializers)
        self._multi_method_implementation = multi_method_implementation

    
    def service(self, handler_call_details):
        method_implementation = self._method_implementations.get(handler_call_details.method)
    # WARNING: Decompyle incomplete



class _Server(interfaces.Server):
    
    def __init__(self, grpc_server):
        self._grpc_server = grpc_server

    
    def add_insecure_port(self, address):
        return self._grpc_server.add_insecure_port(address)

    
    def add_secure_port(self, address, server_credentials):
        return self._grpc_server.add_secure_port(address, server_credentials)

    
    def start(self):
        self._grpc_server.start()

    
    def stop(self, grace):
        return self._grpc_server.stop(grace)

    
    def __enter__(self):
        self._grpc_server.start()
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._grpc_server.stop(None)
        return False



def server(service_implementations, multi_method_implementation, request_deserializers, response_serializers, thread_pool, thread_pool_size):
    generic_rpc_handler = _GenericRpcHandler(service_implementations, multi_method_implementation, request_deserializers, response_serializers)
# WARNING: Decompyle incomplete
