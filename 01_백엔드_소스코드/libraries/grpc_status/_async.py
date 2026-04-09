# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _async.pyc (Python 3.11)

'''Reference implementation for status mapping in gRPC Python.'''
from google.rpc import status_pb2
from grpc.experimental import aio
from _common import GRPC_DETAILS_METADATA_KEY
from _common import code_to_grpc_status_code

async def from_call(call = None):
    '''Returns a google.rpc.status.Status message from a given grpc.aio.Call.

    This is an EXPERIMENTAL API.

    Args:
      call: An grpc.aio.Call instance.

    Returns:
      A google.rpc.status.Status message representing the status of the RPC.
    '''
    pass
# WARNING: Decompyle incomplete

__all__ = [
    'from_call']
