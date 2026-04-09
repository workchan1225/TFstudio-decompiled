# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: method.pyc (Python 3.11)

'''Helpers for wrapping low-level gRPC methods with common functionality.

This is used by gapic clients to provide common error mapping, retry, timeout,
compression, pagination, and long-running operations to gRPC methods.
'''
import enum
import functools
from google.api_core import grpc_helpers
from google.api_core.gapic_v1 import client_info
from google.api_core.timeout import TimeToDeadlineTimeout
USE_DEFAULT_METADATA = object()

class _MethodDefault(enum.Enum):
    _DEFAULT_VALUE = object()

DEFAULT = _MethodDefault._DEFAULT_VALUE

def _is_not_none_or_false(value):
