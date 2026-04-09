# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import os as _os
import typing as _t
from typing_extensions import override
from  import types
from _types import NOT_GIVEN, Omit, NoneType, NotGiven, Transport, ProxiesTypes, omit, not_given
from _utils import file_from_path
from _client import Client, OpenAI, Stream, Timeout, Transport, AsyncClient, AsyncOpenAI, AsyncStream, RequestOptions
from _models import BaseModel
from _version import __title__, __version__
from _response import APIResponse, AsyncAPIResponse
from _constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from _exceptions import APIError, OpenAIError, ConflictError, NotFoundError, APIStatusError, RateLimitError, APITimeoutError, BadRequestError, APIConnectionError, AuthenticationError, InternalServerError, PermissionDeniedError, LengthFinishReasonError, UnprocessableEntityError, APIResponseValidationError, InvalidWebhookSignatureError, ContentFilterFinishReasonError
from _base_client import DefaultHttpxClient, DefaultAioHttpClient, DefaultAsyncHttpxClient
from _utils._logs import setup_logging as _setup_logging
from _legacy_response import HttpxBinaryResponseContent
__all__ = [
    'types',
    '__version__',
    '__title__',
    'NoneType',
    'Transport',
    'ProxiesTypes',
    'NotGiven',
    'NOT_GIVEN',
    'not_given',
    'Omit',
    'omit',
    'OpenAIError',
    'APIError',
    'APIStatusError',
    'APITimeoutError',
    'APIConnectionError',
    'APIResponseValidationError',
    'BadRequestError',
    'AuthenticationError',
    'PermissionDeniedError',
    'NotFoundError',
    'ConflictError',
    'UnprocessableEntityError',
    'RateLimitError',
    'InternalServerError',
    'LengthFinishReasonError',
    'ContentFilterFinishReasonError',
    'InvalidWebhookSignatureError',
    'Timeout',
    'RequestOptions',
    'Client',
    'AsyncClient',
    'Stream',
    'AsyncStream',
    'OpenAI',
    'AsyncOpenAI',
    'file_from_path',
    'BaseModel',
    'DEFAULT_TIMEOUT',
    'DEFAULT_MAX_RETRIES',
    'DEFAULT_CONNECTION_LIMITS',
    'DefaultHttpxClient',
    'DefaultAsyncHttpxClient',
    'DefaultAioHttpClient']
if not _t.TYPE_CHECKING:
    from _utils._resources_proxy import resources
from lib import azure as _azure, pydantic_function_tool
from version import VERSION
from lib.azure import AzureOpenAI, AsyncAzureOpenAI
from lib._old_api import *
from lib.streaming import AssistantEventHandler, AsyncAssistantEventHandler
_setup_logging()
__locals = locals()
for __name in __all__:
    if not __name.startswith('__'):
        __locals[__name].__module__ = 'openai'
        continue
        except (TypeError, AttributeError):
            continue
    import typing as _t
    import typing_extensions as _te
    import httpx as _httpx
    from _base_client import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES
    api_key: 'str | None' = None
    organization: 'str | None' = None
    project: 'str | None' = None
    webhook_secret: 'str | None' = None
    base_url: 'str | _httpx.URL | None' = None
    timeout: 'float | Timeout | None' = DEFAULT_TIMEOUT
    max_retries: 'int' = DEFAULT_MAX_RETRIES
    default_headers: '_t.Mapping[str, str] | None' = None
    default_query: '_t.Mapping[str, object] | None' = None
    http_client: '_httpx.Client | None' = None
    _ApiType = _te.Literal[('openai', 'azure')]
    api_type: '_ApiType | None' = _t.cast(_ApiType, _os.environ.get('OPENAI_API_TYPE'))
    api_version: 'str | None' = _os.environ.get('OPENAI_API_VERSION')
    azure_endpoint: 'str | None' = _os.environ.get('AZURE_OPENAI_ENDPOINT')
    azure_ad_token: 'str | None' = _os.environ.get('AZURE_OPENAI_AD_TOKEN')
    azure_ad_token_provider: '_azure.AzureADTokenProvider | None' = None
    
    class _ModuleClient(OpenAI):
        pass
    # WARNING: Decompyle incomplete

    
    class _AzureModuleClient(AzureOpenAI, _ModuleClient):
        pass

    
    class _AmbiguousModuleClientUsageError(OpenAIError):
        pass
    # WARNING: Decompyle incomplete

    
    def _has_openai_credentials():
        return _os.environ.get('OPENAI_API_KEY') is not None

    
    def _has_azure_credentials():
        if not azure_endpoint is not None:
            pass
        return _os.environ.get('AZURE_OPENAI_API_KEY') is not None

    
    def _has_azure_ad_credentials():
