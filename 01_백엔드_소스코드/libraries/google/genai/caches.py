# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: caches.pyc (Python 3.11)

import json
import logging
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _transformers as t
from  import types
from _api_client import BaseApiClient
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.caches')

def _Blob_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Content_to_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CreateCachedContentConfig_to_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CreateCachedContentConfig_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CreateCachedContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateCachedContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteCachedContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteCachedContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteCachedContentResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteCachedContentResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FileData_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FunctionCall_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FunctionCallingConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FunctionDeclaration_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetCachedContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetCachedContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GoogleMaps_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GoogleSearch_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsParameters_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListCachedContentsResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Part_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ToolConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Tool_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Tool_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _UpdateCachedContentConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateCachedContentConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateCachedContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateCachedContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Caches(_api_module.BaseModule):
    
    def create(self = None, *, model, config):
        """Creates a cached contents resource.

    Usage:

    .. code-block:: python

      contents = ... // Initialize the content to cache.
      response = client.caches.create(
          model= ... // The publisher model id
          contents=contents,
          config={
              'display_name': 'test cache',
              'system_instruction': 'What is the sum of the two pdfs?',
              'ttl': '86400s',
          },
      )
    """
        parameter_model = types._CreateCachedContentParameters(model = model, config = config)
        if self._api_client.vertexai:
            request_dict = _CreateCachedContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'cachedContents'.format_map(request_url_dict)
            else:
                path = 'cachedContents'
        else:
            request_dict = _CreateCachedContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'cachedContents'.format_map(request_url_dict)
            else:
                path = 'cachedContents'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, name, config):
        '''Gets cached content configurations.

    .. code-block:: python

      client.caches.get(name= ... ) // The server-generated resource name.
    '''
        parameter_model = types._GetCachedContentParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _GetCachedContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _GetCachedContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def delete(self = None, *, name, config):
        '''Deletes cached content.

    Usage:

    .. code-block:: python

      client.caches.delete(name= ... ) // The server-generated resource name.
    '''
        parameter_model = types._DeleteCachedContentParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _DeleteCachedContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _DeleteCachedContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def update(self = None, *, name, config):
        """Updates cached content configurations.

    .. code-block:: python

      response = client.caches.update(
          name= ... // The server-generated resource name.
          config={
              'ttl': '7600s',
          },
      )
    """
        parameter_model = types._UpdateCachedContentParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _UpdateCachedContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _UpdateCachedContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _list(self = None, *, config):
        parameter_model = types._ListCachedContentsParameters(config = config)
        if self._api_client.vertexai:
            request_dict = _ListCachedContentsParameters_to_vertex(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'cachedContents'.format_map(request_url_dict)
            else:
                path = 'cachedContents'
        else:
            request_dict = _ListCachedContentsParameters_to_mldev(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'cachedContents'.format_map(request_url_dict)
            else:
                path = 'cachedContents'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, config):
        '''Lists cached contents.

    Args:
      config (ListCachedContentsConfig): Optional configuration for the list
        request.

    Returns:
      A Pager object that contains one page of cached contents. When iterating
      over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      for cached_content in client.caches.list():
        print(cached_content.name)
    '''
        list_request = self._list
        return Pager('cached_contents', list_request, self._list(config = config), config)



class AsyncCaches(_api_module.BaseModule):
    
    async def create(self = None, *, model, config):
        """Creates a cached contents resource.

    Usage:

    .. code-block:: python

      contents = ... // Initialize the content to cache.
      response = await client.aio.caches.create(
          model= ... // The publisher model id
          contents=contents,
          config={
              'display_name': 'test cache',
              'system_instruction': 'What is the sum of the two pdfs?',
              'ttl': '86400s',
          },
      )
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, name, config):
        '''Gets cached content configurations.

    .. code-block:: python

      await client.aio.caches.get(name= ... ) // The server-generated resource
      name.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, name, config):
        '''Deletes cached content.

    Usage:

    .. code-block:: python

      await client.aio.caches.delete(name= ... ) // The server-generated
      resource name.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, *, name, config):
        """Updates cached content configurations.

    .. code-block:: python

      response = await client.aio.caches.update(
          name= ... // The server-generated resource name.
          config={
              'ttl': '7600s',
          },
      )
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, config):
        '''Lists cached contents asynchronously.

    Args:
      config (ListCachedContentsConfig): Optional configuration for the list
        request.

    Returns:
      A Pager object that contains one page of cached contents. When iterating
      over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      async for cached_content in await client.aio.caches.list():
        print(cached_content.name)
    '''
        pass
    # WARNING: Decompyle incomplete
