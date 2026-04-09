# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operation.pyc (Python 3.11)

'''Futures for long-running operations returned from Google Cloud APIs.

These futures can be used to synchronously wait for the result of a
long-running operation using :meth:`Operation.result`:


.. code-block:: python

    operation = my_api_client.long_running_method()
    result = operation.result()

Or asynchronously using callbacks and :meth:`Operation.add_done_callback`:

.. code-block:: python

    operation = my_api_client.long_running_method()

    def my_callback(future):
        result = future.result()

    operation.add_done_callback(my_callback)

'''
import functools
import threading
from google.api_core import exceptions
from google.api_core import protobuf_helpers
from google.api_core.future import polling
from google.longrunning import operations_pb2
from google.protobuf import json_format
from google.rpc import code_pb2

class Operation(polling.PollingFuture):
    pass
# WARNING: Decompyle incomplete


def _refresh_http(api_request, operation_name, retry = (None,)):
    '''Refresh an operation using a JSON/HTTP client.

    Args:
        api_request (Callable): A callable used to make an API request. This
            should generally be
            :meth:`google.cloud._http.Connection.api_request`.
        operation_name (str): The name of the operation.
        retry (google.api_core.retry.Retry): (Optional) retry policy

    Returns:
        google.longrunning.operations_pb2.Operation: The operation.
    '''
    path = 'operations/{}'.format(operation_name)
# WARNING: Decompyle incomplete


def _cancel_http(api_request, operation_name):
    '''Cancel an operation using a JSON/HTTP client.

    Args:
        api_request (Callable): A callable used to make an API request. This
            should generally be
            :meth:`google.cloud._http.Connection.api_request`.
        operation_name (str): The name of the operation.
    '''
    path = 'operations/{}:cancel'.format(operation_name)
    api_request(method = 'POST', path = path)


def from_http_json(operation, api_request, result_type, **kwargs):
    '''Create an operation future using a HTTP/JSON client.

    This interacts with the long-running operations `service`_ (specific
    to a given API) via `HTTP/JSON`_.

    .. _HTTP/JSON: https://cloud.google.com/speech/reference/rest/            v1beta1/operations#Operation

    Args:
        operation (dict): Operation as a dictionary.
        api_request (Callable): A callable used to make an API request. This
            should generally be
            :meth:`google.cloud._http.Connection.api_request`.
        result_type (:func:`type`): The protobuf result type.
        kwargs: Keyword args passed into the :class:`Operation` constructor.

    Returns:
        ~.api_core.operation.Operation: The operation future to track the given
            operation.
    '''
    operation_proto = json_format.ParseDict(operation, operations_pb2.Operation())
    refresh = functools.partial(_refresh_http, api_request, operation_proto.name)
    cancel = functools.partial(_cancel_http, api_request, operation_proto.name)
# WARNING: Decompyle incomplete


def _refresh_grpc(operations_stub, operation_name, retry = (None,)):
    '''Refresh an operation using a gRPC client.

    Args:
        operations_stub (google.longrunning.operations_pb2.OperationsStub):
            The gRPC operations stub.
        operation_name (str): The name of the operation.
        retry (google.api_core.retry.Retry): (Optional) retry policy

    Returns:
        google.longrunning.operations_pb2.Operation: The operation.
    '''
    request_pb = operations_pb2.GetOperationRequest(name = operation_name)
    rpc = operations_stub.GetOperation
# WARNING: Decompyle incomplete


def _cancel_grpc(operations_stub, operation_name):
    '''Cancel an operation using a gRPC client.

    Args:
        operations_stub (google.longrunning.operations_pb2.OperationsStub):
            The gRPC operations stub.
        operation_name (str): The name of the operation.
    '''
    request_pb = operations_pb2.CancelOperationRequest(name = operation_name)
    operations_stub.CancelOperation(request_pb)


def from_grpc(operation, operations_stub, result_type, grpc_metadata = (None,), **kwargs):
    '''Create an operation future using a gRPC client.

    This interacts with the long-running operations `service`_ (specific
    to a given API) via gRPC.

    .. _service: https://github.com/googleapis/googleapis/blob/                 050400df0fdb16f63b63e9dee53819044bffc857/                 google/longrunning/operations.proto#L38

    Args:
        operation (google.longrunning.operations_pb2.Operation): The operation.
        operations_stub (google.longrunning.operations_pb2.OperationsStub):
            The operations stub.
        result_type (:func:`type`): The protobuf result type.
        grpc_metadata (Optional[List[Tuple[str, str]]]): Additional metadata to pass
            to the rpc.
        kwargs: Keyword args passed into the :class:`Operation` constructor.

    Returns:
        ~.api_core.operation.Operation: The operation future to track the given
            operation.
    '''
    refresh = functools.partial(_refresh_grpc, operations_stub, operation.name, metadata = grpc_metadata)
    cancel = functools.partial(_cancel_grpc, operations_stub, operation.name, metadata = grpc_metadata)
# WARNING: Decompyle incomplete


def from_gapic(operation, operations_client, result_type, grpc_metadata = (None,), **kwargs):
    '''Create an operation future from a gapic client.

    This interacts with the long-running operations `service`_ (specific
    to a given API) via a gapic client.

    .. _service: https://github.com/googleapis/googleapis/blob/                 050400df0fdb16f63b63e9dee53819044bffc857/                 google/longrunning/operations.proto#L38

    Args:
        operation (google.longrunning.operations_pb2.Operation): The operation.
        operations_client (google.api_core.operations_v1.OperationsClient):
            The operations client.
        result_type (:func:`type`): The protobuf result type.
        grpc_metadata (Optional[List[Tuple[str, str]]]): Additional metadata to pass
            to the rpc.
        kwargs: Keyword args passed into the :class:`Operation` constructor.

    Returns:
        ~.api_core.operation.Operation: The operation future to track the given
            operation.
    '''
    refresh = functools.partial(operations_client.get_operation, operation.name, metadata = grpc_metadata)
    cancel = functools.partial(operations_client.cancel_operation, operation.name, metadata = grpc_metadata)
# WARNING: Decompyle incomplete
