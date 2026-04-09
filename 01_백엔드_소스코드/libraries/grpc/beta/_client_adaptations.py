# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client_adaptations.pyc (Python 3.11)

"""Translates gRPC's client-side API into gRPC's client-side Beta API."""
import grpc
from grpc import _common
from grpc.beta import _metadata
from grpc.beta import interfaces
from grpc.framework.common import cardinality
from grpc.framework.foundation import future
from grpc.framework.interfaces.face import face
_STATUS_CODE_TO_ABORTION_KIND_AND_ABORTION_ERROR_CLASS = {
    grpc.StatusCode.UNIMPLEMENTED: (face.Abortion.Kind.LOCAL_FAILURE, face.LocalError),
    grpc.StatusCode.DEADLINE_EXCEEDED: (face.Abortion.Kind.EXPIRED, face.ExpirationError),
    grpc.StatusCode.UNKNOWN: (face.Abortion.Kind.REMOTE_FAILURE, face.RemoteError),
    grpc.StatusCode.CANCELLED: (face.Abortion.Kind.CANCELLED, face.CancellationError) }

def _effective_metadata(metadata, metadata_transformer):
    pass
# WARNING: Decompyle incomplete


def _credentials(grpc_call_options):
    pass
# WARNING: Decompyle incomplete


def _abortion(rpc_error_call):
    code = rpc_error_call.code()
    pair = _STATUS_CODE_TO_ABORTION_KIND_AND_ABORTION_ERROR_CLASS.get(code)
# WARNING: Decompyle incomplete


def _abortion_error(rpc_error_call):
    code = rpc_error_call.code()
    pair = _STATUS_CODE_TO_ABORTION_KIND_AND_ABORTION_ERROR_CLASS.get(code)
# WARNING: Decompyle incomplete


class _InvocationProtocolContext(interfaces.GRPCInvocationContext):
    
    def disable_next_request_compression(self):
        pass



class _Rendezvous(face.Call, future.Future):
    
    def __init__(self, response_future, response_iterator, call):
        self._future = response_future
        self._iterator = response_iterator
        self._call = call

    
    def cancel(self):
        return self._call.cancel()

    
    def cancelled(self):
        return self._future.cancelled()

    
    def running(self):
        return self._future.running()

    
    def done(self):
        return self._future.done()

    
    def result(self, timeout = (None,)):
        
        try:
            return self._future.result(timeout = timeout)
        except grpc.RpcError:
            rpc_error_call = None
            raise _abortion_error(rpc_error_call)
            rpc_error_call = None
            del rpc_error_call
            except grpc.FutureTimeoutError:
                raise future.TimeoutError()
            except grpc.FutureCancelledError:
                raise future.CancelledError()


    
    def exception(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def traceback(self, timeout = (None,)):
        
        try:
            return self._future.traceback(timeout = timeout)
        except grpc.FutureTimeoutError:
            raise future.TimeoutError()
            except grpc.FutureCancelledError:
                raise future.CancelledError()


    
    def add_done_callback(self, fn):
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        return self

    
    def _next(self):
        
        try:
            return next(self._iterator)
        except grpc.RpcError:
            rpc_error_call = None
            raise _abortion_error(rpc_error_call)
            rpc_error_call = None
            del rpc_error_call


    
    def __next__(self):
        return self._next()

    
    def next(self):
        return self._next()

    
    def is_active(self):
        return self._call.is_active()

    
    def time_remaining(self):
        return self._call.time_remaining()

    
    def add_abortion_callback(self, abortion_callback):
        pass
    # WARNING: Decompyle incomplete

    
    def protocol_context(self):
        return _InvocationProtocolContext()

    
    def initial_metadata(self):
        return _metadata.beta(self._call.initial_metadata())

    
    def terminal_metadata(self):
        return _metadata.beta(self._call.terminal_metadata())

    
    def code(self):
        return self._call.code()

    
    def details(self):
        return self._call.details()



def _blocking_unary_unary(channel, group, method, timeout, with_call, protocol_options, metadata, metadata_transformer, request, request_serializer, response_deserializer):
    
    try:
        multi_callable = channel.unary_unary(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
        effective_metadata = _effective_metadata(metadata, metadata_transformer)
        if with_call:
            (response, call) = multi_callable.with_call(request, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
            return (response, _Rendezvous(None, None, call))
        return multi_callable(request, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    except grpc.RpcError:
        rpc_error_call = None
        raise _abortion_error(rpc_error_call)
        rpc_error_call = None
        del rpc_error_call



def _future_unary_unary(channel, group, method, timeout, protocol_options, metadata, metadata_transformer, request, request_serializer, response_deserializer):
    multi_callable = channel.unary_unary(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
    effective_metadata = _effective_metadata(metadata, metadata_transformer)
    response_future = multi_callable.future(request, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    return _Rendezvous(response_future, None, response_future)


def _unary_stream(channel, group, method, timeout, protocol_options, metadata, metadata_transformer, request, request_serializer, response_deserializer):
    multi_callable = channel.unary_stream(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
    effective_metadata = _effective_metadata(metadata, metadata_transformer)
    response_iterator = multi_callable(request, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    return _Rendezvous(None, response_iterator, response_iterator)


def _blocking_stream_unary(channel, group, method, timeout, with_call, protocol_options, metadata, metadata_transformer, request_iterator, request_serializer, response_deserializer):
    
    try:
        multi_callable = channel.stream_unary(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
        effective_metadata = _effective_metadata(metadata, metadata_transformer)
        if with_call:
            (response, call) = multi_callable.with_call(request_iterator, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
            return (response, _Rendezvous(None, None, call))
        return multi_callable(request_iterator, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    except grpc.RpcError:
        rpc_error_call = None
        raise _abortion_error(rpc_error_call)
        rpc_error_call = None
        del rpc_error_call



def _future_stream_unary(channel, group, method, timeout, protocol_options, metadata, metadata_transformer, request_iterator, request_serializer, response_deserializer):
    multi_callable = channel.stream_unary(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
    effective_metadata = _effective_metadata(metadata, metadata_transformer)
    response_future = multi_callable.future(request_iterator, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    return _Rendezvous(response_future, None, response_future)


def _stream_stream(channel, group, method, timeout, protocol_options, metadata, metadata_transformer, request_iterator, request_serializer, response_deserializer):
    multi_callable = channel.stream_stream(_common.fully_qualified_method(group, method), request_serializer = request_serializer, response_deserializer = response_deserializer)
    effective_metadata = _effective_metadata(metadata, metadata_transformer)
    response_iterator = multi_callable(request_iterator, timeout = timeout, metadata = _metadata.unbeta(effective_metadata), credentials = _credentials(protocol_options))
    return _Rendezvous(None, response_iterator, response_iterator)


class _UnaryUnaryMultiCallable(face.UnaryUnaryMultiCallable):
    
    def __init__(self, channel, group, method, metadata_transformer, request_serializer, response_deserializer):
        self._channel = channel
        self._group = group
        self._method = method
        self._metadata_transformer = metadata_transformer
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer

    
    def __call__(self, request, timeout, metadata, with_call, protocol_options = (None, False, None)):
        return _blocking_unary_unary(self._channel, self._group, self._method, timeout, with_call, protocol_options, metadata, self._metadata_transformer, request, self._request_serializer, self._response_deserializer)

    
    def future(self, request, timeout, metadata, protocol_options = (None, None)):
        return _future_unary_unary(self._channel, self._group, self._method, timeout, protocol_options, metadata, self._metadata_transformer, request, self._request_serializer, self._response_deserializer)

    
    def event(self, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None)):
        raise NotImplementedError()



class _UnaryStreamMultiCallable(face.UnaryStreamMultiCallable):
    
    def __init__(self, channel, group, method, metadata_transformer, request_serializer, response_deserializer):
        self._channel = channel
        self._group = group
        self._method = method
        self._metadata_transformer = metadata_transformer
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer

    
    def __call__(self, request, timeout, metadata, protocol_options = (None, None)):
        return _unary_stream(self._channel, self._group, self._method, timeout, protocol_options, metadata, self._metadata_transformer, request, self._request_serializer, self._response_deserializer)

    
    def event(self, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None)):
        raise NotImplementedError()



class _StreamUnaryMultiCallable(face.StreamUnaryMultiCallable):
    
    def __init__(self, channel, group, method, metadata_transformer, request_serializer, response_deserializer):
        self._channel = channel
        self._group = group
        self._method = method
        self._metadata_transformer = metadata_transformer
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer

    
    def __call__(self, request_iterator, timeout, metadata, with_call, protocol_options = (None, False, None)):
        return _blocking_stream_unary(self._channel, self._group, self._method, timeout, with_call, protocol_options, metadata, self._metadata_transformer, request_iterator, self._request_serializer, self._response_deserializer)

    
    def future(self, request_iterator, timeout, metadata, protocol_options = (None, None)):
        return _future_stream_unary(self._channel, self._group, self._method, timeout, protocol_options, metadata, self._metadata_transformer, request_iterator, self._request_serializer, self._response_deserializer)

    
    def event(self, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None)):
        raise NotImplementedError()



class _StreamStreamMultiCallable(face.StreamStreamMultiCallable):
    
    def __init__(self, channel, group, method, metadata_transformer, request_serializer, response_deserializer):
        self._channel = channel
        self._group = group
        self._method = method
        self._metadata_transformer = metadata_transformer
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer

    
    def __call__(self, request_iterator, timeout, metadata, protocol_options = (None, None)):
        return _stream_stream(self._channel, self._group, self._method, timeout, protocol_options, metadata, self._metadata_transformer, request_iterator, self._request_serializer, self._response_deserializer)

    
    def event(self, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None)):
        raise NotImplementedError()



class _GenericStub(face.GenericStub):
    
    def __init__(self, channel, metadata_transformer, request_serializers, response_deserializers):
