# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client.pyc (Python 3.11)

from __future__ import annotations
import os
import logging
import urllib.parse as urllib
from typing import Any, Union, Mapping, TypeVar
from typing_extensions import Self, override
import httpx
from  import _exceptions
from _beta import Beta, AsyncBeta
from _types import NOT_GIVEN, Timeout, NotGiven
from _utils import is_dict, is_given
from _compat import model_copy
from _version import __version__
from _streaming import Stream, AsyncStream
from _exceptions import AnthropicError, APIStatusError
from _base_client import DEFAULT_MAX_RETRIES, BaseClient, SyncAPIClient, AsyncAPIClient, FinalRequestOptions
from _stream_decoder import AWSEventStreamDecoder
from resources.messages import Messages, AsyncMessages
from resources.completions import Completions, AsyncCompletions
log: 'logging.Logger' = logging.getLogger(__name__)
DEFAULT_VERSION = 'bedrock-2023-05-31'
_HttpxClientT = TypeVar('_HttpxClientT', bound = Union[(httpx.Client, httpx.AsyncClient)])
_DefaultStreamT = TypeVar('_DefaultStreamT', bound = Union[(Stream[Any], AsyncStream[Any])])

def _prepare_options(input_options = None):
    options = model_copy(input_options, deep = True)
    if is_dict(options.json_data):
        options.json_data.setdefault('anthropic_version', DEFAULT_VERSION)
        if is_given(options.headers):
            betas = options.headers.get('anthropic-beta')
            if betas:
                options.json_data.setdefault('anthropic_beta', betas.split(','))
    if options.url in frozenset({'/v1/complete', '/v1/messages', '/v1/messages?beta=true'}) and options.method == 'post':
        if not is_dict(options.json_data):
            raise RuntimeError('Expected dictionary json_data for post /completions endpoint')
        model = options.json_data.pop('model', None)
        model = urllib.parse.quote(str(model), safe = ':')
        stream = options.json_data.pop('stream', False)
        if stream:
            options.url = f'''/model/{model}/invoke-with-response-stream'''
        else:
            options.url = f'''/model/{model}/invoke'''
    if options.url.startswith('/v1/messages/batches'):
        raise AnthropicError('The Batch API is not supported in Bedrock yet')
    if options.url == '/v1/messages/count_tokens':
        raise AnthropicError('Token counting is not supported in Bedrock yet')
    return options


def _infer_region():
    '''
    Infer the AWS region from the environment variables or
    from the boto3 session if available.
    '''
    aws_region = os.environ.get('AWS_REGION')
# WARNING: Decompyle incomplete


def BaseBedrockClient():
    '''BaseBedrockClient'''
    _make_status_error = (lambda self = None, err_msg = None, *, body, response: if response.status_code == 400:
_exceptions.BadRequestError(err_msg, response = response, body = body)if None.status_code == 401:
_exceptions.AuthenticationError(err_msg, response = response, body = body)if None.status_code == 403:
_exceptions.PermissionDeniedError(err_msg, response = response, body = body)if None.status_code == 404:
_exceptions.NotFoundError(err_msg, response = response, body = body)if None.status_code == 409:
_exceptions.ConflictError(err_msg, response = response, body = body)if None.status_code == 422:
_exceptions.UnprocessableEntityError(err_msg, response = response, body = body)if None.status_code == 429:
_exceptions.RateLimitError(err_msg, response = response, body = body)if None.status_code == 503:
_exceptions.ServiceUnavailableError(err_msg, response = response, body = body)if None.status_code >= 500:
_exceptions.InternalServerError(err_msg, response = response, body = body)None(err_msg, response = response, body = body))()

BaseBedrockClient = <NODE:27>(BaseBedrockClient, 'BaseBedrockClient', BaseClient[(_HttpxClientT, _DefaultStreamT)])

def AnthropicBedrock():
    '''AnthropicBedrock'''
    pass
# WARNING: Decompyle incomplete

AnthropicBedrock = <NODE:27>(AnthropicBedrock, 'AnthropicBedrock', BaseBedrockClient[(httpx.Client, Stream[Any])], SyncAPIClient)

def AsyncAnthropicBedrock():
    '''AsyncAnthropicBedrock'''
    pass
# WARNING: Decompyle incomplete

AsyncAnthropicBedrock = <NODE:27>(AsyncAnthropicBedrock, 'AsyncAnthropicBedrock', BaseBedrockClient[(httpx.AsyncClient, AsyncStream[Any])], AsyncAPIClient)
