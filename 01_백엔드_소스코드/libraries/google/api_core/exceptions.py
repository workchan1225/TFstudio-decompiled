# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

__doc__ = 'Exceptions raised by Google API core & clients.\n\nThis module provides base classes for all errors raised by libraries based\non :mod:`google.api_core`, including both HTTP and gRPC clients.\n'
from __future__ import absolute_import
from __future__ import unicode_literals
import http.client as http
from typing import Optional, Dict
from typing import Union
import warnings
from google.rpc import error_details_pb2

def _warn_could_not_import_grpcio_status():
    warnings.warn('Please install grpcio-status to obtain helpful grpc error messages.', ImportWarning)

# WARNING: Decompyle incomplete
