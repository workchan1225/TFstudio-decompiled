# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _extra_utils.pyc (Python 3.11)

'''Extra utils depending on types that are shared between sync and async modules.'''
import asyncio
import inspect
import io
import logging
import sys
import typing
from typing import Any, Callable, Dict, Optional, Union, get_args, get_origin
import mimetypes
import os
import pydantic
from  import _common
from  import _mcp_utils
from  import _transformers as t
from  import errors
from  import types
from _adapters import McpToGenAiToolAdapter
if sys.version_info >= (3, 10):
    from types import UnionType
else:
    UnionType = typing._UnionGenericAlias
if typing.TYPE_CHECKING:
    from mcp import ClientSession as McpClientSession
    from mcp.types import Tool as McpTool
else:
    McpClientSession: typing.Type = Any
    McpTool: typing.Type = Any
    
    try:
        from mcp import ClientSession as McpClientSession
        from mcp.types import Tool as McpTool
    except ImportError:
        McpClientSession = None
        McpTool = None

    _DEFAULT_MAX_REMOTE_CALLS_AFC = 10
    logger = logging.getLogger('google_genai.models')
    
    def _create_generate_content_config_model(config = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_gcs_uri(src = None):
        '''Extracts the first GCS URI from the source, if available.'''
        if isinstance(src, str) and src.startswith('gs://'):
            return src
        if None(src, dict) and src.get('gcs_uri'):
            return src['gcs_uri'][0] if src['gcs_uri'] else None
        if None(src, types.BatchJobSource) and src.gcs_uri:
            return src.gcs_uri[0] if src.gcs_uri else None

    
    def _get_bigquery_uri(src = None):
        '''Extracts the BigQuery URI from the source, if available.'''
        if isinstance(src, str) and src.startswith('bq://'):
            return src
        if None(src, dict) and src.get('bigquery_uri'):
            return src['bigquery_uri']
        if None(src, types.BatchJobSource) and src.bigquery_uri:
            return src.bigquery_uri

    
    def format_destination(src = None, config = None):
        '''Formats the destination uri based on the source uri for Vertex AI.'''
        pass
    # WARNING: Decompyle incomplete

    
    def find_afc_incompatible_tool_indexes(config = None):
        '''Checks if the config contains any AFC incompatible tools.

  A `types.Tool` object that contains `function_declarations` is considered a
  non-AFC tool for this execution path.

  Args:
    config: The GenerateContentConfig to check for incompatible tools.

  Returns:
    A list of indexes of the incompatible tools in the config.
  '''
        if not config:
            return []
        config_model = None(config)
        incompatible_tools_indexes = []
        if not config_model or config_model.tools:
            return incompatible_tools_indexes
        for index, tool in None(config_model.tools):
            if isinstance(tool, types.Tool) and tool.function_declarations:
                incompatible_tools_indexes.append(index)
            return incompatible_tools_indexes

    
    def get_function_map(config = None, mcp_to_genai_tool_adapters = None, is_caller_method_async = None):
        '''Returns a function map from the config.'''
        function_map = { }
        if not config:
            return function_map
        config_model = None(config)
        if config_model.tools:
            for tool in config_model.tools:
                if callable(tool):
                    if not inspect.iscoroutinefunction(tool) and is_caller_method_async:
                        raise errors.UnsupportedFunctionError(f'''Function {tool.__name__} is a coroutine function, which is not supported for automatic function calling. Please manually invoke {tool.__name__} to get the function response.''')
                    function_map[tool.__name__] = tool
                if mcp_to_genai_tool_adapters:
                    if not is_caller_method_async:
                        raise errors.UnsupportedFunctionError('MCP tools are not supported in synchronous methods.')
                    for tool_name, _ in mcp_to_genai_tool_adapters.items():
                        if function_map.get(tool_name):
                            raise ValueError(f'''Tool {tool_name} is already defined for the request.''')
                        function_map.update(mcp_to_genai_tool_adapters)
                        return function_map

    
    def convert_number_values_for_dict_function_call_args(args = None):
        '''Converts float values in dict with no decimal to integers.'''
        return args.items()()

    
    def convert_number_values_for_function_call_args(args = None):
        '''Converts float values with no decimal to integers.'''
        if isinstance(args, float) and args.is_integer():
            return int(args)
        if None(args, dict):
            return args.items()()
        if None(args, list):
            return args()

    
    def is_annotation_pydantic_model(annotation = None):
        
        try:
            if inspect.isclass(annotation):
                pass
            return issubclass(annotation, pydantic.BaseModel)
        except TypeError:
            return False


    
    def convert_if_exist_pydantic_model(value = None, annotation = None, param_name = None, func_name = ('value', Any, 'annotation', Any, 'param_name', str, 'func_name', str, 'return', Any)):
        pass
    # WARNING: Decompyle incomplete

    
    def convert_argument_from_function(args = None, function = None):
        signature = inspect.signature(function)
        func_name = function.__name__
        converted_args = { }
        for param_name, param in signature.parameters.items():
            if param_name in args:
                converted_args[param_name] = convert_if_exist_pydantic_model(args[param_name], param.annotation, param_name, func_name)
            return converted_args

    
    def invoke_function_from_dict_args(args = None, function_to_invoke = None):
        converted_args = convert_argument_from_function(args, function_to_invoke)
    # WARNING: Decompyle incomplete

    
    async def invoke_function_from_dict_args_async(args = None, function_to_invoke = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_function_response_parts(response = None, function_map = None):
        '''Returns the function response parts from the response.'''
        func_response_parts = []
    # WARNING: Decompyle incomplete

    
    async def get_function_response_parts_async(response = None, function_map = None):
        '''Returns the function response parts from the response.'''
        pass
    # WARNING: Decompyle incomplete

    
    def should_disable_afc(config = None):
        '''Returns whether automatic function calling is enabled.'''
        if not config:
            return False
        config_model = None(config)
    # WARNING: Decompyle incomplete

    
    def get_max_remote_calls_afc(config = None):
        if not config:
            return _DEFAULT_MAX_REMOTE_CALLS_AFC
        if should_disable_afc(config):
            raise ValueError('automatic function calling is not enabled, but SDK is trying to get max remote calls.')
        config_model = _create_generate_content_config_model(config)
    # WARNING: Decompyle incomplete

    
    def raise_error_for_afc_incompatible_config(config = None):
        '''Raises an error if the config is not compatible with AFC.'''
        if not config and config.tool_config or config.tool_config.function_calling_config:
            return None
        afc_config = None.automatic_function_calling
        disable_afc_config = afc_config.disable if afc_config else False
        stream_function_call = config.tool_config.function_calling_config.stream_function_call_arguments
        if not stream_function_call or disable_afc_config:
            raise ValueError('Running in streaming mode with stream_function_call_arguments enabled, this feature is not compatible with automatic function calling (AFC). Please set config.automatic_function_calling.disable to True to disable AFC or leave config.tool_config. function_calling_config.stream_function_call_arguments to be empty or set to False to disable streaming function call arguments.')
        return None

    
    def should_append_afc_history(config = None):
        if not config:
            return True
        config_model = None(config)
        if not config_model.automatic_function_calling:
            return True
        return not (None.automatic_function_calling.ignore_call_history)

    
    def parse_config_for_mcp_usage(config = None):
        '''Returns a parsed config with an appended MCP header if MCP tools or sessions are used.'''
        if not config:
            return None
        config_model = None(config)
        config_model_copy = config_model.model_copy(update = {
            'tools': None })
        config_model_copy.tools = config_model.tools
    # WARNING: Decompyle incomplete

    
    async def parse_config_for_mcp_sessions(config = None):
        '''Returns a parsed config with MCP sessions converted to GenAI tools.

  Also returns a map of MCP tools to GenAI tool adapters to be used for AFC.
  '''
        pass
    # WARNING: Decompyle incomplete

    
    def append_chunk_contents(contents = None, chunk = None):
        '''Appends the contents of the chunk to the contents list and returns it.'''
        pass
    # WARNING: Decompyle incomplete

    
    def prepare_resumable_upload(file = None, user_http_options = None, user_mime_type = None):
        '''Prepares the HTTP options, file bytes size and mime type for a resumable upload.

  This function inspects a file (from a path or an in-memory object) to
  determine its size and MIME type. It then constructs the necessary HTTP
  headers and options required to initiate a resumable upload session.
  '''
        size_bytes = None
        mime_type = user_mime_type
    # WARNING: Decompyle incomplete

    return None
