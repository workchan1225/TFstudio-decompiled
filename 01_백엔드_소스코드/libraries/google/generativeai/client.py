# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from __future__ import annotations
import os
import contextlib
import inspect
import dataclasses
import pathlib
import threading
from typing import Any, cast
from collections.abc import Sequence
import httplib2
from io import IOBase

generativelanguage

protos
from google.auth import credentials
import google.generativeai.protos, generativeai
from google.auth import exceptions as ga_exceptions
from google import auth
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1
from google.api_core import operations_v1
import googleapiclient.http as googleapiclient
import googleapiclient.discovery as googleapiclient

try:
    from google.generativeai import version
    __version__ = version.__version__
except ImportError:
    __version__ = '0.0.0'

USER_AGENT = 'genai-py'
GENAI_API_DISCOVERY_URL = 'https://generativelanguage.googleapis.com/$discovery/rest'
patch_colab_gce_credentials = (lambda : pass# WARNING: Decompyle incomplete
)()

class FileServiceClient(glm.FileServiceClient):
    pass
# WARNING: Decompyle incomplete


class FileServiceAsyncClient(glm.FileServiceAsyncClient):
    
    async def create_file(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete


_ClientManager = <NODE:12>()

def configure(*, api_key, credentials, transport, client_options, client_info, default_metadata):
    '''Captures default client configuration.

    If no API key has been provided (either directly, or on `client_options`) and the
    `GOOGLE_API_KEY` environment variable is set, it will be used as the API key.

    Note: Not all arguments are detailed below. Refer to the `*ServiceClient` classes in
    `google.ai.generativelanguage` for details on the other arguments.

    Args:
        transport: A string, one of: [`rest`, `grpc`, `grpc_asyncio`].
        api_key: The API-Key to use when creating the default clients (each service uses
            a separate client). This is a shortcut for `client_options={"api_key": api_key}`.
            If omitted, and the `GOOGLE_API_KEY` environment variable is set, it will be
            used.
        default_metadata: Default (key, value) metadata pairs to send with every request.
            when using `transport="rest"` these are sent as HTTP headers.
    '''
    return _client_manager.configure(api_key = api_key, credentials = credentials, transport = transport, client_options = client_options, client_info = client_info, default_metadata = default_metadata)

_client_manager = _ClientManager()
_client_manager.configure()

def get_default_cache_client():
    return _client_manager.get_default_client('cache')


def get_default_file_client():
    return _client_manager.get_default_client('file')


def get_default_file_async_client():
    return _client_manager.get_default_client('file_async')


def get_default_generative_client():
    return _client_manager.get_default_client('generative')


def get_default_generative_async_client():
    return _client_manager.get_default_client('generative_async')


def get_default_operations_client():
    return _client_manager.get_default_client('operations')


def get_default_model_client():
    return _client_manager.get_default_client('model')


def get_default_retriever_client():
    return _client_manager.get_default_client('retriever')


def get_default_retriever_async_client():
    return _client_manager.get_default_client('retriever_async')


def get_default_permission_client():
    return _client_manager.get_default_client('permission')


def get_default_permission_async_client():
    return _client_manager.get_default_client('permission_async')
