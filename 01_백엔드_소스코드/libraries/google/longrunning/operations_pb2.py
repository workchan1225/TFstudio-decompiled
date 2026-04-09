# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operations_pb2.pyc (Python 3.11)

'''Safe implementation of long-running operations with and without gRPC.

Multiplexes between versions of long-running operations with and without gRPC.
The former is preferred, but not possible in all environments (such as Google
AppEngine Standard).
'''

try:
    from google.longrunning.operations_grpc_pb2 import *
    from google.longrunning.operations_grpc_pb2 import _CANCELOPERATIONREQUEST, _DELETEOPERATIONREQUEST, _GETOPERATIONREQUEST, _LISTOPERATIONSREQUEST, _LISTOPERATIONSRESPONSE, _OPERATION, _OPERATIONINFO, _OPERATIONS
    return None
except ImportError:
    from google.longrunning.operations_proto_pb2 import *
    from google.longrunning.operations_proto_pb2 import _CANCELOPERATIONREQUEST, _DELETEOPERATIONREQUEST, _GETOPERATIONREQUEST, _LISTOPERATIONSREQUEST, _LISTOPERATIONSRESPONSE, _OPERATION, _OPERATIONINFO, _OPERATIONS
    return None
