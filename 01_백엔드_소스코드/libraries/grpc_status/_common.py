# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

'''Reference implementation for status mapping in gRPC Python.'''
import grpc
_CODE_TO_GRPC_CODE_MAPPING = grpc.StatusCode()
GRPC_DETAILS_METADATA_KEY = 'grpc-status-details-bin'

def code_to_grpc_status_code(code):
    
    try:
        return _CODE_TO_GRPC_CODE_MAPPING[code]
    except KeyError:
        raise ValueError('Invalid status code %s' % code)
