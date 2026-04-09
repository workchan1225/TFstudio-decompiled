# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operations.pyc (Python 3.11)

import json
import logging
from typing import Any, Optional, TypeVar, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import types
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
logger = logging.getLogger('google_genai.operations')

def _FetchPredictOperationParameters_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetOperationParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetOperationParameters_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetProjectOperationParameters_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Operations(_api_module.BaseModule):
    
    def _get_videos_operation(self = None, *, operation_name, config):
        parameter_model = types._GetOperationParameters(operation_name = operation_name, config = config)
        if self._api_client.vertexai:
            request_dict = _GetOperationParameters_to_vertex(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{operationName}'.format_map(request_url_dict)
            else:
                path = '{operationName}'
        else:
            request_dict = _GetOperationParameters_to_mldev(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{operationName}'.format_map(request_url_dict)
            else:
                path = '{operationName}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _fetch_predict_videos_operation(self = None, *, operation_name, resource_name, config):
        parameter_model = types._FetchPredictOperationParameters(operation_name = operation_name, resource_name = resource_name, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _FetchPredictOperationParameters_to_vertex(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{resourceName}:fetchPredictOperation'.format_map(request_url_dict)
        else:
            path = '{resourceName}:fetchPredictOperation'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _get(self = None, *, operation_id, config):
        parameter_model = types._GetProjectOperationParameters(operation_id = operation_id, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _GetProjectOperationParameters_to_vertex(parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'operations/{operation_id}'.format_map(request_url_dict)
        else:
            path = 'operations/{operation_id}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    T = TypeVar('T', bound = types.Operation)
    
    def get(self = None, operation = None, *, config):
        '''Gets the status of an operation.'''
        operation_name = operation.name
        if not operation_name:
            raise ValueError('Operation name is empty.')
    # WARNING: Decompyle incomplete



class AsyncOperations(_api_module.BaseModule):
    
    async def _get_videos_operation(self = None, *, operation_name, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _fetch_predict_videos_operation(self = None, *, operation_name, resource_name, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _get(self = None, *, operation_id, config):
        pass
    # WARNING: Decompyle incomplete

    T = TypeVar('T', bound = types.Operation)
    
    async def get(self = None, operation = None, *, config):
        '''Gets the status of an operation.'''
        pass
    # WARNING: Decompyle incomplete
