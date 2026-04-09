# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operations_client.pyc (Python 3.11)

'''A client for the google.longrunning.operations meta-API.

This is a client that deals with long-running operations that follow the
pattern outlined by the `Google API Style Guide`_.

When an API method normally takes long time to complete, it can be designed to
return ``Operation`` to the client, and the client can use this interface to
receive the real response asynchronously by polling the operation resource to
receive the response.

It is not a separate service, but rather an interface implemented by a larger
service. The protocol-level definition is available at
`google/longrunning/operations.proto`_. Typically, this will be constructed
automatically by another client class to deal with operations.

.. _Google API Style Guide:
    https://cloud.google.com/apis/design/design_pattern
    s#long_running_operations
.. _google/longrunning/operations.proto:
    https://github.com/googleapis/googleapis/blob/master/google/longrunning
    /operations.proto
'''
import functools
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import page_iterator
from google.api_core import retry as retries
from google.api_core import timeout as timeouts
from google.longrunning import operations_pb2
from grpc import Compression

class OperationsClient(object):
    '''Client for interacting with long-running operations within a service.

    Args:
        channel (grpc.Channel): The gRPC channel associated with the service
            that implements the ``google.longrunning.operations`` interface.
        client_config (dict):
            A dictionary of call options for each method. If not specified
            the default configuration is used.
    '''
    
    def __init__(self, channel, client_config = (None,)):
        self.operations_stub = operations_pb2.OperationsStub(channel)
        default_retry = retries.Retry(initial = 0.1, maximum = 60, multiplier = 1.3, predicate = retries.if_exception_type(core_exceptions.DeadlineExceeded, core_exceptions.ServiceUnavailable), timeout = 600)
        default_timeout = timeouts.TimeToDeadlineTimeout(timeout = 600)
        default_compression = Compression.NoCompression
        self._get_operation = gapic_v1.method.wrap_method(self.operations_stub.GetOperation, default_retry = default_retry, default_timeout = default_timeout, default_compression = default_compression)
        self._list_operations = gapic_v1.method.wrap_method(self.operations_stub.ListOperations, default_retry = default_retry, default_timeout = default_timeout, default_compression = default_compression)
        self._cancel_operation = gapic_v1.method.wrap_method(self.operations_stub.CancelOperation, default_retry = default_retry, default_timeout = default_timeout, default_compression = default_compression)
        self._delete_operation = gapic_v1.method.wrap_method(self.operations_stub.DeleteOperation, default_retry = default_retry, default_timeout = default_timeout, default_compression = default_compression)

    
    def get_operation(self, name, retry, timeout, compression, metadata = (gapic_v1.method.DEFAULT, gapic_v1.method.DEFAULT, gapic_v1.method.DEFAULT, None)):
