# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_stores.pyc (Python 3.11)

from functools import cached_property
import io
import json
import logging
import os
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _extra_utils
from  import types
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from _operations_converters import _UploadToFileSearchStoreOperation_from_mldev
from documents import AsyncDocuments, Documents
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.filesearchstores')

def _CreateFileSearchStoreConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateFileSearchStoreParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteFileSearchStoreConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteFileSearchStoreParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetFileSearchStoreParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ImportFileConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ImportFileOperation_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ImportFileParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ImportFileResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFileSearchStoresConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFileSearchStoresParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFileSearchStoresResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UploadToFileSearchStoreConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UploadToFileSearchStoreParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UploadToFileSearchStoreResumableResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class FileSearchStores(_api_module.BaseModule):
    documents = (lambda self = None: Documents(self._api_client))()
    
    def create(self = None, *, config):
        '''Creates a File Search Store.

    Args:
      config (CreateFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      FileSearchStore
    '''
        parameter_model = types._CreateFileSearchStoreParameters(config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _CreateFileSearchStoreParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'fileSearchStores'.format_map(request_url_dict)
        else:
            path = 'fileSearchStores'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, name, config):
        '''Gets metadata about a FileSearchStore.

    Args:
      name (str): The resource name of the FileSearchStore. Example:
        `FileSearchStores/my-file-search-store-123`
      config (GetFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      A FileSearchStore object containing the metadata.
    '''
        parameter_model = types._GetFileSearchStoreParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _GetFileSearchStoreParameters_to_mldev(parameter_model)
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
        '''Deletes a FileSearchStore.

    Args:
      name (str): The resource name of the FileSearchStore. Example:
        `FileSearchStores/my-file-search-store-123`
      config (DeleteFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      None
    '''
        parameter_model = types._DeleteFileSearchStoreParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _DeleteFileSearchStoreParameters_to_mldev(parameter_model)
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
        parameter_model = types._ListFileSearchStoresParameters(config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _ListFileSearchStoresParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'fileSearchStores'.format_map(request_url_dict)
        else:
            path = 'fileSearchStores'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _upload_to_file_search_store(self = None, *, file_search_store_name, config):
        parameter_model = types._UploadToFileSearchStoreParameters(file_search_store_name = file_search_store_name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _UploadToFileSearchStoreParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'upload/v1beta/{file_search_store_name}:uploadToFileSearchStore'.format_map(request_url_dict)
        else:
            path = 'upload/v1beta/{file_search_store_name}:uploadToFileSearchStore'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def import_file(self = None, *, file_search_store_name, file_name, config):
        '''Imports a File from File Service to a FileSearchStore.

    This is a long-running operation, see aip.dev/151

    Args:
      file_search_store_name (str): The resource name of the FileSearchStore.
        Example: `fileSearchStores/my-file-search-store-123`
      file_name (str): The resource name of the File to import. Example:
        `files/abc-123`
      config (ImportFileConfig | None): Optional parameters for the request.

    Returns:
      ImportFileOperation.
    '''
        parameter_model = types._ImportFileParameters(file_search_store_name = file_search_store_name, file_name = file_name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _ImportFileParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{file_search_store_name}:importFile'.format_map(request_url_dict)
        else:
            path = '{file_search_store_name}:importFile'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def upload_to_file_search_store(self = None, *, file_search_store_name, file, config):
        """Calls the API to upload a file to the given file search store.

    Args:
      file_search_store_name: The resource name of the FileSearchStore. Example:
        `fileSearchStores/file-search-store-123`
      file: A path to the file or an `IOBase` object to be uploaded. If it's an
        IOBase object, it must be opened in blocking (the default) mode and
        binary mode. In other words, do not use non-blocking mode or text mode.
        The given stream must be seekable, that is, it must be able to call
        `seek()` on 'path'.
      config: Optional parameters to set `diplay_name`, `mime_type`, and others.
    """
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, config):
        '''Lists FileSearchStores.

    Args:
      config (ListFileSearchStoresConfig): Optional configuration for the list
        request.

    Returns:
      A Pager object that contains one page of file search stores. When
      iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      for file_search_store in client.file_search_stores.list():
        print(f"file search store: {file_search_store.name} -
        {file_search_store.display_name}")
    '''
        list_request = self._list
        return Pager('file_search_stores', list_request, self._list(config = config), config)



class AsyncFileSearchStores(_api_module.BaseModule):
    documents = (lambda self = None: AsyncDocuments(self._api_client))()
    
    async def create(self = None, *, config):
        '''Creates a File Search Store.

    Args:
      config (CreateFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      FileSearchStore
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, name, config):
        '''Gets metadata about a FileSearchStore.

    Args:
      name (str): The resource name of the FileSearchStore. Example:
        `FileSearchStores/my-file-search-store-123`
      config (GetFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      A FileSearchStore object containing the metadata.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, name, config):
        '''Deletes a FileSearchStore.

    Args:
      name (str): The resource name of the FileSearchStore. Example:
        `FileSearchStores/my-file-search-store-123`
      config (DeleteFileSearchStoreConfig | None): Optional parameters for the
        request.

    Returns:
      None
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _upload_to_file_search_store(self = None, *, file_search_store_name, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def import_file(self = None, *, file_search_store_name, file_name, config):
        '''Imports a File from File Service to a FileSearchStore.

    This is a long-running operation, see aip.dev/151

    Args:
      file_search_store_name (str): The resource name of the FileSearchStore.
        Example: `fileSearchStores/my-file-search-store-123`
      file_name (str): The resource name of the File to import. Example:
        `files/abc-123`
      config (ImportFileConfig | None): Optional parameters for the request.

    Returns:
      ImportFileOperation.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def upload_to_file_search_store(self = None, *, file_search_store_name, file, config):
        """Calls the API to upload a file to the given file search store.

    Args:
      file_search_store_name: The resource name of the FileSearchStore. Example:
        `fileSearchStores/file-search-store-123`
      file: A path to the file or an `IOBase` object to be uploaded. If it's an
        IOBase object, it must be opened in blocking (the default) mode and
        binary mode. In other words, do not use non-blocking mode or text mode.
        The given stream must be seekable, that is, it must be able to call
        `seek()` on 'path'.
      config: Optional parameters to set `diplay_name`, `mime_type` and others.
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, config):
        '''Lists FileSearchStores asynchronously.

    Args:
      config (ListFileSearchStoresConfig): Optional parameters for the request,
        such as page_size.

    Returns:
      A Pager object that contains one page of FileSearchStores. When iterating
      over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      async for file_search_store in await client.aio.file_search_stores.list():
        print(f"file search store: {file_search_store.name} -
        {file_search_store.display_name}")
    '''
        pass
    # WARNING: Decompyle incomplete
