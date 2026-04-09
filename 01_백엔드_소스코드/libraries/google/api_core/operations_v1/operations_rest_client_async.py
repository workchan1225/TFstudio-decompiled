# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operations_rest_client_async.pyc (Python 3.11)

from typing import Optional, Sequence, Tuple, Union
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1
from google.api_core.operations_v1 import pagers_async as pagers
from google.api_core.operations_v1.transports.base import DEFAULT_CLIENT_INFO, OperationsTransport
from google.api_core.operations_v1.abstract_operations_base_client import AbstractOperationsBaseClient
from google.longrunning import operations_pb2

try:
    from google.auth.aio import credentials as ga_credentials
except ImportError:
    e = None
    raise ImportError('The `async_rest` extra of `google-api-core` is required to use long-running operations.  Install it by running `pip install google-api-core[async_rest]`.'), e
    e = None
    del e


class AsyncOperationsRestClient(AbstractOperationsBaseClient):
    pass
# WARNING: Decompyle incomplete
