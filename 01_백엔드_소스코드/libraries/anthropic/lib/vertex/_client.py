# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import TYPE_CHECKING, Any, Union, Mapping, TypeVar
from typing_extensions import Self, override
import httpx
from  import _exceptions
from _auth import load_auth, refresh_auth
from _beta import Beta, AsyncBeta
from _types import NOT_GIVEN, NotGiven
from _utils import is_dict, asyncify, is_given
from _compat import model_copy, typed_cached_property
from _models import FinalRequestOptions
from _version import __version__
from _streaming import Stream, AsyncStream
from _exceptions import AnthropicError, APIStatusError
from _base_client import DEFAULT_MAX_RETRIES, BaseClient, SyncAPIClient, AsyncAPIClient
from resources.messages import Messages, AsyncMessages
if TYPE_CHECKING:
    from google.auth.credentials import Credentials as GoogleCredentials
DEFAULT_VERSION = 'vertex-2023-10-16'
_HttpxClientT = TypeVar('_HttpxClientT', bound = Union[(httpx.Client, httpx.AsyncClient)])
_DefaultStreamT = TypeVar('_DefaultStreamT', bound = Union[(Stream[Any], AsyncStream[Any])])

def BaseVertexClient():
    '''BaseVertexClient'''
    region = (lambda self = None: raise RuntimeError('region not set'))()
    project_id = (lambda self = None: project_id = os.environ.get('ANTHROPIC_VERTEX_PROJECT_ID')if project_id:
project_id)()
    _make_status_error = (lambda self = None, err_msg = None, *, body, response: if response.status_code == 400:
_exceptions.BadRequestError(err_msg, response = response, body = body)if None.status_code == 401:
_exceptions.AuthenticationError(err_msg, response = response, body = body)if None.status_code == 403:
_exceptions.PermissionDeniedError(err_msg, response = response, body = body)if None.status_code == 404:
_exceptions.NotFoundError(err_msg, response = response, body = body)if None.status_code == 409:
_exceptions.ConflictError(err_msg, response = response, body = body)if None.status_code == 422:
_exceptions.UnprocessableEntityError(err_msg, response = response, body = body)if None.status_code == 429:
_exceptions.RateLimitError(err_msg, response = response, body = body)if None.status_code == 503:
_exceptions.ServiceUnavailableError(err_msg, response = response, body = body)if None.status_code == 504:
_exceptions.DeadlineExceededError(err_msg, response = response, body = body)if None.status_code >= 500:
_exceptions.InternalServerError(err_msg, response = response, body = body)None(err_msg, response = response, body = body))()

BaseVertexClient = <NODE:27>(BaseVertexClient, 'BaseVertexClient', BaseClient[(_HttpxClientT, _DefaultStreamT)])

def AnthropicVertex():
    '''AnthropicVertex'''
    pass
# WARNING: Decompyle incomplete

AnthropicVertex = <NODE:27>(AnthropicVertex, 'AnthropicVertex', BaseVertexClient[(httpx.Client, Stream[Any])], SyncAPIClient)

def AsyncAnthropicVertex():
    '''AsyncAnthropicVertex'''
    pass
# WARNING: Decompyle incomplete

AsyncAnthropicVertex = <NODE:27>(AsyncAnthropicVertex, 'AsyncAnthropicVertex', BaseVertexClient[(httpx.AsyncClient, AsyncStream[Any])], AsyncAPIClient)

def _prepare_options(input_options = None, *, project_id, region):
    options = model_copy(input_options, deep = True)
    if is_dict(options.json_data):
        options.json_data.setdefault('anthropic_version', DEFAULT_VERSION)
# WARNING: Decompyle incomplete
