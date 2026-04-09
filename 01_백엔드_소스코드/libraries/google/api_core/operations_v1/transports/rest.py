# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest.pyc (Python 3.11)

from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.longrunning import operations_pb2
import google.protobuf as google
from google.protobuf import empty_pb2
from google.protobuf import json_format
import grpc
from requests import __version__ as requests_version
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import general_helpers
from google.api_core import path_template
from google.api_core import rest_helpers
from google.api_core import retry as retries
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from base import OperationsTransport
PROTOBUF_VERSION = google.protobuf.__version__
OptionalRetry = Union[(retries.Retry, object)]
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = BASE_DEFAULT_CLIENT_INFO.gapic_version, grpc_version = None, rest_version = f'''requests@{requests_version}''')

class OperationsRestTransport(OperationsTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('OperationsRestTransport',)
