# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rpc_status.pyc (Python 3.11)

'''Reference implementation for status mapping in gRPC Python.'''
import collections
import sys
from google.rpc import status_pb2
import grpc
from _common import GRPC_DETAILS_METADATA_KEY
from _common import code_to_grpc_status_code

def _Status():
    '''_Status'''
    pass

_Status = <NODE:27>(_Status, '_Status', collections.namedtuple('_Status', ('code', 'details', 'trailing_metadata')), grpc.Status)

def from_call(call):
    """Returns a google.rpc.status.Status message corresponding to a given grpc.Call.

    This is an EXPERIMENTAL API.

    Args:
      call: A grpc.Call instance.

    Returns:
      A google.rpc.status.Status message representing the status of the RPC.

    Raises:
      ValueError: If the gRPC call's code or details are inconsistent with the
        status code and message inside of the google.rpc.status.Status.
    """
    pass
# WARNING: Decompyle incomplete


def to_status(status):
    '''Convert a google.rpc.status.Status message to grpc.Status.

    This is an EXPERIMENTAL API.

    Args:
      status: a google.rpc.status.Status message representing the non-OK status
        to terminate the RPC with and communicate it to the client.

    Returns:
      A grpc.Status instance representing the input google.rpc.status.Status message.
    '''
    return _Status(code = code_to_grpc_status_code(status.code), details = status.message, trailing_metadata = ((GRPC_DETAILS_METADATA_KEY, status.SerializeToString()),))

__all__ = [
    'from_call',
    'to_status']
if sys.version_info[0] >= 3 or sys.version_info[1] >= 6:
    from  import _async as aio
    __all__.append('aio')
    return None
return None
