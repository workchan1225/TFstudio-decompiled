# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operation_async.pyc (Python 3.11)

'''AsyncIO futures for long-running operations returned from Google Cloud APIs.

These futures can be used to await for the result of a long-running operation
using :meth:`AsyncOperation.result`:


.. code-block:: python

    operation = my_api_client.long_running_method()
    result = await operation.result()

Or asynchronously using callbacks and :meth:`Operation.add_done_callback`:

.. code-block:: python

    operation = my_api_client.long_running_method()

    def my_callback(future):
        result = await future.result()

    operation.add_done_callback(my_callback)

'''
import functools
import threading
from google.api_core import exceptions
from google.api_core import protobuf_helpers
from google.api_core.future import async_future
from google.longrunning import operations_pb2
from google.rpc import code_pb2

class AsyncOperation(async_future.AsyncFuture):
    pass
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
