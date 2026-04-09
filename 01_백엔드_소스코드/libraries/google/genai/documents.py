# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: documents.pyc (Python 3.11)

from functools import partial
import json
import logging
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import types
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.documents')

def _DeleteDocumentConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteDocumentParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetDocumentParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListDocumentsConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListDocumentsParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListDocumentsResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Documents(_api_module.BaseModule):
    
    def get(self = None, *, name, config):
        '''Gets metadata about a Document.

    Args:
      name (str): The resource name of the Document.
        Example: ragStores/rag-store-foo/documents/documents-bar
      config (GetDocumentConfig | None): Optional parameters for the request.

    Returns:
      The Document.
    '''
        parameter_model = types._GetDocumentParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _GetDocumentParameters_to_mldev(parameter_model)
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
        '''Deletes a Document.

    Args:
      name (str): The resource name of the Document.
        Example: ragStores/rag-store-foo/documents/documents-bar
      config (DeleteDocumentConfig | None): Optional parameters for the request.

    Returns:
      None
    '''
        parameter_model = types._DeleteDocumentParameters(name = name, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _DeleteDocumentParameters_to_mldev(parameter_model)
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

    
    def _list(self = None, *, parent, config):
        parameter_model = types._ListDocumentsParameters(parent = parent, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _ListDocumentsParameters_to_mldev(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{parent}/documents'.format_map(request_url_dict)
        else:
            path = '{parent}/documents'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, parent, config):
        '''Lists documents.

    Args:
      parent (str): The name of the RagStore containing the Documents.
      config (ListDocumentsConfig): Optional configuration for the list request.

    Returns:
      A Pager object that contains one page of documents. When iterating over
      the pager, it automatically fetches the next page if there are more.
    Usage:
    .. code-block:: python
      for document in client.documents.list(parent=\'rag_store_name\'):
        print(f"document: {document.name} - {document.display_name}")
    '''
        list_request = partial(self._list, parent = parent)
        return Pager('documents', list_request, self._list(parent = parent, config = config), config)



class AsyncDocuments(_api_module.BaseModule):
    
    async def get(self = None, *, name, config):
        '''Gets metadata about a Document.

    Args:
      name (str): The resource name of the Document.
        Example: ragStores/rag-store-foo/documents/documents-bar
      config (GetDocumentConfig | None): Optional parameters for the request.

    Returns:
      The Document.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, name, config):
        '''Deletes a Document.

    Args:
      name (str): The resource name of the Document.
        Example: ragStores/rag-store-foo/documents/documents-bar
      config (DeleteDocumentConfig | None): Optional parameters for the request.

    Returns:
      None
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, parent, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, parent, config):
        '''Lists documents asynchronously.

    Args:
      parent (str): The name of the RagStore containing the Documents.
      config (ListDocumentsConfig): Optional configuration for the list request.

    Returns:
      A Pager object that contains one page of documents. When iterating over
      the pager, it automatically fetches the next page if there are more.
    Usage:
    .. code-block:: python
      async for document in await
      client.aio.documents.list(parent=\'rag_store_name\'):
        print(f"document: {document.name} - {document.display_name}")
    '''
        pass
    # WARNING: Decompyle incomplete
