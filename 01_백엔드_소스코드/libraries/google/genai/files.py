# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

import io
import json
import logging
import os
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _extra_utils
from  import _transformers as t
from  import types
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.files')

def _CreateFileParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateFileResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteFileParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteFileResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetFileParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFilesConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFilesParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListFilesResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Files(_api_module.BaseModule):
    
    def _list(self = None, *, config):
        parameter_model = types._ListFilesParameters(config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _ListFilesParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'files'.format_map(request_url_dict)
        else:
            path = 'files'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _create(self = None, *, file, config):
        parameter_model = types._CreateFileParameters(file = file, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _CreateFileParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'upload/v1beta/files'.format_map(request_url_dict)
        else:
            path = 'upload/v1beta/files'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, name, config):
        """Retrieves the file information from the service.

    Args:
      name (str): The name identifier for the file to retrieve.
      config (GetFileConfig): Optional, configuration for the get method.

    Returns:
      File: The file information.

    Usage:

    .. code-block:: python

      file = client.files.get(name='files/...')
      print(file.uri)
    """
        parameter_model = types._GetFileParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _GetFileParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'files/{file}'.format_map(request_url_dict)
        else:
            path = 'files/{file}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def delete(self = None, *, name, config):
        """Deletes a remotely stored file.

    Args:
      name (str): The name identifier for the file to delete.
      config (DeleteFileConfig): Optional, configuration for the delete method.

    Returns:
      DeleteFileResponse: The response for the delete method

    Usage:

    .. code-block:: python

      client.files.delete(name='files/...')
    """
        parameter_model = types._DeleteFileParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _DeleteFileParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'files/{file}'.format_map(request_url_dict)
        else:
            path = 'files/{file}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def upload(self = None, *, file, config):
        """Calls the API to upload a file using a supported file service.

    Args:
      file: A path to the file or an `IOBase` object to be uploaded. If it's an
        IOBase object, it must be opened in blocking (the default) mode and
        binary mode. In other words, do not use non-blocking mode or text mode.
        The given stream must be seekable, that is, it must be able to call
        `seek()` on 'path'.
      config: Optional parameters to set `diplay_name`, `mime_type`, and `name`.
    """
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        config_model = types.UploadFileConfig()
    # WARNING: Decompyle incomplete

    
    def download(self = None, *, file, config):
        """Downloads a file's data from storage.

    Files created by `upload` can't be downloaded. You can tell which files are
    downloadable by checking the `source` or `download_uri` property.

    Note: This method returns the data as bytes. For `Video` and
    `GeneratedVideo` objects there is an additional side effect, that it also
    sets the `video_bytes` property on the `Video` object.

    Args:
      file (str): A file name, uri, or file object. Identifying which file to
        download.
      config (DownloadFileConfigOrDict): Optional, configuration for the get
        method.

    Returns:
      File: The file data as bytes.

    Usage:

    .. code-block:: python

      for file client.files.list():
        if file.download_uri is not None:
          break
      else:
        raise ValueError('No files found with a `download_uri`.')
      data = client.files.download(file=file)
      # data = client.files.download(file=file.name)
      # data = client.files.download(file=file.download_uri)

      video = types.Video(uri=file.uri)
      video_bytes = client.files.download(file=video)
      video.video_bytes
    """
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        config_model = None
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, config):
        """Lists all files from the service.

    Args:
      config (ListFilesConfig): Optional, configuration for the list method.

    Returns:
      A Pager object that contains one page of files. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python

      for file in client.files.list(config={'page_size': 10}):
        print(file.name)
    """
        list_request = self._list
        return Pager('files', list_request, self._list(config = config), config)



class AsyncFiles(_api_module.BaseModule):
    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _create(self = None, *, file, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, name, config):
        """Retrieves the file information from the service.

    Args:
      name (str): The name identifier for the file to retrieve.
      config (GetFileConfig): Optional, configuration for the get method.

    Returns:
      File: The file information.

    Usage:

    .. code-block:: python

      file = await client.aio.files.get(name='files/...')
      print(file.uri)
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, name, config):
        """Deletes a remotely stored file.

    Args:
      name (str): The name identifier for the file to delete.
      config (DeleteFileConfig): Optional, configuration for the delete method.

    Returns:
      DeleteFileResponse: The response for the delete method

    Usage:

    .. code-block:: python

      await client.aio.files.delete(name='files/...')
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def upload(self = None, *, file, config):
        """Calls the API to upload a file asynchronously using a supported file service.

    Args:
      file: A path to the file or an `IOBase` object to be uploaded. If it's an
        IOBase object, it must be opened in blocking (the default) mode and
        binary mode. In other words, do not use non-blocking mode or text mode.
        The given stream must be seekable, that is, it must be able to call
        `seek()` on 'path'.
      config: Optional parameters to set `diplay_name`, `mime_type`, and `name`.
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def download(self = None, *, file, config):
        """Downloads a file's data from the file service.

    The Vertex-AI implementation of the API foes not include the file service.

    Files created by `upload` can't be downloaded. You can tell which files are
    downloadable by checking the `download_uri` property.

    Args:
      File (str): A file name, uri, or file object. Identifying which file to
        download.
      config (DownloadFileConfigOrDict): Optional, configuration for the get
        method.

    Returns:
      File: The file data as bytes.

    Usage:

    .. code-block:: python

      for file client.files.list():
        if file.download_uri is not None:
          break
      else:
        raise ValueError('No files found with a `download_uri`.')
      data = client.files.download(file=file)
      # data = client.files.download(file=file.name)
      # data = client.files.download(file=file.uri)
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, config):
        """Lists all files from the service asynchronously.

    Args:
      config (ListFilesConfig): Optional, configuration for the list method.

    Returns:
      A Pager object that contains one page of files. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python

      async for file in await client.aio.files.list(config={'page_size': 10}):
        print(file.name)
    """
        pass
    # WARNING: Decompyle incomplete
