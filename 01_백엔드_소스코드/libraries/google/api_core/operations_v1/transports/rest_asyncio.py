# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest_asyncio.pyc (Python 3.11)

import json
from typing import Any, Callable, Coroutine, Dict, Optional, Sequence, Tuple
import warnings
from google.auth import __version__ as auth_version

try:
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession
except ImportError:
    e = None
    raise ImportError('The `async_rest` extra of `google-api-core` is required to use long-running operations.  Install it by running `pip install google-api-core[async_rest]`.'), e
    e = None
    del e

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import general_helpers
from google.api_core import path_template
from google.api_core import rest_helpers
from google.api_core import retry_async as retries_async
from google.auth.aio import credentials as ga_credentials_async
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import json_format
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO, OperationsTransport
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = BASE_DEFAULT_CLIENT_INFO.gapic_version, grpc_version = None, rest_version = f'''google-auth@{auth_version}''')

class AsyncOperationsRestTransport(OperationsTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('AsyncOperationsRestTransport',)
