# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

import asyncio
import os
from types import TracebackType
from typing import Optional, Union
import google.auth as google
import pydantic
from _api_client import BaseApiClient
from _base_url import get_base_url
from _replay_api_client import ReplayApiClient
from batches import AsyncBatches, Batches
from caches import AsyncCaches, Caches
from chats import AsyncChats, Chats
from file_search_stores import AsyncFileSearchStores, FileSearchStores
from files import AsyncFiles, Files
from live import AsyncLive
from models import AsyncModels, Models
from operations import AsyncOperations, Operations
from tokens import AsyncTokens, Tokens
from tunings import AsyncTunings, Tunings
from types import HttpOptions, HttpOptionsDict, HttpRetryOptions

class AsyncClient:
    '''Client for making asynchronous (non-blocking) requests.'''
    
    def __init__(self = None, api_client = None):
        self._api_client = api_client
        self._models = AsyncModels(self._api_client)
        self._tunings = AsyncTunings(self._api_client)
        self._caches = AsyncCaches(self._api_client)
        self._batches = AsyncBatches(self._api_client)
        self._files = AsyncFiles(self._api_client)
        self._file_search_stores = AsyncFileSearchStores(self._api_client)
        self._live = AsyncLive(self._api_client)
        self._tokens = AsyncTokens(self._api_client)
        self._operations = AsyncOperations(self._api_client)

    models = (lambda self = None: self._models)()
    tunings = (lambda self = None: self._tunings)()
    caches = (lambda self = None: self._caches)()
    file_search_stores = (lambda self = None: self._file_search_stores)()
    batches = (lambda self = None: self._batches)()
    chats = (lambda self = None: AsyncChats(modules = self.models))()
    files = (lambda self = None: self._files)()
    live = (lambda self = None: self._live)()
    auth_tokens = (lambda self = None: self._tokens)()
    operations = (lambda self = None: self._operations)()
    
    async def aclose(self = None):
        """Closes the async client explicitly.

    However, it doesn't close the sync client, which can be closed using the
    Client.close() method or using the context manager.

    Usage:
    .. code-block:: python

      from google.genai import Client

      async_client = Client(
          vertexai=True, project='my-project-id', location='us-central1'
      ).aio
      response_1 = await async_client.models.generate_content(
          model='gemini-2.0-flash',
          contents='Hello World',
      )
      response_2 = await async_client.models.generate_content(
          model='gemini-2.0-flash',
          contents='Hello World',
      )
      # Close the client to release resources.
      await async_client.aclose()
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', Optional[Exception], 'exc_value', Optional[Exception], 'traceback', Optional[TracebackType], 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self = None):
        
        try:
            asyncio.get_running_loop().create_task(self.aclose())
            return None
        except Exception:
            return None




class DebugConfig(pydantic.BaseModel):
    '''Configuration options that change client network behavior when testing.'''
    client_mode: Optional[str] = pydantic.Field(default_factory = (lambda : os.getenv('GOOGLE_GENAI_CLIENT_MODE', None)))
    replays_directory: Optional[str] = pydantic.Field(default_factory = (lambda : os.getenv('GOOGLE_GENAI_REPLAYS_DIRECTORY', None)))
    replay_id: Optional[str] = pydantic.Field(default_factory = (lambda : os.getenv('GOOGLE_GENAI_REPLAY_ID', None)))


class Client:
    '''Client for making synchronous requests.

  Use this client to make a request to the Gemini Developer API or Vertex AI
  API and then wait for the response.

  To initialize the client, provide the required arguments either directly
  or by using environment variables. Gemini API users and Vertex AI users in
  express mode can provide API key by providing input argument
  `api_key="your-api-key"` or by defining `GOOGLE_API_KEY="your-api-key"` as an
  environment variable

  Vertex AI API users can provide inputs argument as `vertexai=True,
  project="your-project-id", location="us-central1"` or by defining
  `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT` and
  `GOOGLE_CLOUD_LOCATION` environment variables.

  Attributes:
    api_key: The `API key <https://ai.google.dev/gemini-api/docs/api-key>`_ to
      use for authentication. Applies to the Gemini Developer API only.
    vertexai: Indicates whether the client should use the Vertex AI API
      endpoints. Defaults to False (uses Gemini Developer API endpoints).
      Applies to the Vertex AI API only.
    credentials: The credentials to use for authentication when calling the
      Vertex AI APIs. Credentials can be obtained from environment variables and
      default credentials. For more information, see `Set up Application Default
      Credentials
      <https://cloud.google.com/docs/authentication/provide-credentials-adc>`_.
      Applies to the Vertex AI API only.
    project: The `Google Cloud project ID
      <https://cloud.google.com/vertex-ai/docs/start/cloud-environment>`_ to use
      for quota. Can be obtained from environment variables (for example,
      ``GOOGLE_CLOUD_PROJECT``). Applies to the Vertex AI API only.
      Find your `Google Cloud project ID <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>`_.
    location: The `location
      <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations>`_
      to send API requests to (for example, ``us-central1``). Can be obtained
      from environment variables. Applies to the Vertex AI API only.
    debug_config: Config settings that control network behavior of the client.
      This is typically used when running test code.
    http_options: Http options to use for the client. These options will be
      applied to all requests made by the client. Example usage: `client =
      genai.Client(http_options=types.HttpOptions(api_version=\'v1\'))`.

  Usage for the Gemini Developer API:

  .. code-block:: python

    from google import genai

    client = genai.Client(api_key=\'my-api-key\')

  Usage for the Vertex AI API:

  .. code-block:: python

    from google import genai

    client = genai.Client(
        vertexai=True, project=\'my-project-id\', location=\'us-central1\'
    )
  '''
    
    def __init__(self = None, *, vertexai, api_key, credentials, project, location, debug_config, http_options):
        '''Initializes the client.

    Args:
       vertexai (bool): Indicates whether the client should use the Vertex AI
         API endpoints. Defaults to False (uses Gemini Developer API endpoints).
         Applies to the Vertex AI API only.
       api_key (str): The `API key
         <https://ai.google.dev/gemini-api/docs/api-key>`_ to use for
         authentication. Applies to the Gemini Developer API only.
       credentials (google.auth.credentials.Credentials): The credentials to use
         for authentication when calling the Vertex AI APIs. Credentials can be
         obtained from environment variables and default credentials. For more
         information, see `Set up Application Default Credentials
         <https://cloud.google.com/docs/authentication/provide-credentials-adc>`_.
         Applies to the Vertex AI API only.
       project (str): The `Google Cloud project ID
         <https://cloud.google.com/vertex-ai/docs/start/cloud-environment>`_ to
         use for quota. Can be obtained from environment variables (for example,
         ``GOOGLE_CLOUD_PROJECT``). Applies to the Vertex AI API only.
       location (str): The `location
         <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations>`_
         to send API requests to (for example, ``us-central1``). Can be obtained
         from environment variables. Applies to the Vertex AI API only.
       debug_config (DebugConfig): Config settings that control network behavior
         of the client. This is typically used when running test code.
       http_options (Union[HttpOptions, HttpOptionsDict]): Http options to use
         for the client.
    '''
        if not debug_config:
            pass
        self._debug_config = DebugConfig()
    # WARNING: Decompyle incomplete

    _get_api_client = (lambda vertexai, api_key, credentials = None, project = None, location = staticmethod, debug_config = (None, None, None, None, None, None, None), http_options = ('vertexai', Optional[bool], 'api_key', Optional[str], 'credentials', Optional[google.auth.credentials.Credentials], 'project', Optional[str], 'location', Optional[str], 'debug_config', Optional[DebugConfig], 'http_options', Optional[HttpOptions], 'return', BaseApiClient): if debug_config and debug_config.client_mode in ('record', 'replay', 'auto'):
ReplayApiClient(mode = debug_config.client_mode, replay_id = debug_config.replay_id, replays_directory = debug_config.replays_directory, vertexai = vertexai, api_key = api_key, credentials = credentials, project = project, location = location, http_options = http_options)None(vertexai = vertexai, api_key = api_key, credentials = credentials, project = project, location = location, http_options = http_options))()
    chats = (lambda self = None: Chats(modules = self.models))()
    aio = (lambda self = None: self._aio)()
    models = (lambda self = None: self._models)()
    tunings = (lambda self = None: self._tunings)()
    caches = (lambda self = None: self._caches)()
    file_search_stores = (lambda self = None: self._file_search_stores)()
    batches = (lambda self = None: self._batches)()
    files = (lambda self = None: self._files)()
    auth_tokens = (lambda self = None: self._tokens)()
    operations = (lambda self = None: self._operations)()
    vertexai = (lambda self = None:
