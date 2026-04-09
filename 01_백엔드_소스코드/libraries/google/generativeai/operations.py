# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operations.pyc (Python 3.11)

from __future__ import annotations
import functools
from typing import Iterator
from google.generativeai import protos
from google.generativeai import client as client_lib
from google.generativeai.types import model_types
from google.api_core import operation as operation_lib
from tqdm.auto import auto as tqdm

def list_operations(*, client):
    '''Calls the API to list all operations'''
    pass
# WARNING: Decompyle incomplete


def get_operation(name = None, *, client):
    '''Calls the API to get a specific operation'''
    pass
# WARNING: Decompyle incomplete


def delete_operation(name = None, *, client):
    '''Calls the API to delete a specific operation'''
    pass
# WARNING: Decompyle incomplete


class CreateTunedModelOperation(operation_lib.Operation):
    pass
# WARNING: Decompyle incomplete


def from_gapic(cls = None, *, operation, operations_client, result_type, metadata_type, grpc_metadata, **kwargs):
    '''`google.api_core.operation.from_gapic`, patched to allow subclasses.'''
    refresh = functools.partial(operations_client.get_operation, operation.name, metadata = grpc_metadata)
    cancel = functools.partial(operations_client.cancel_operation, operation.name, metadata = grpc_metadata)
# WARNING: Decompyle incomplete
