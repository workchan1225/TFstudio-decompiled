# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _transformers.pyc (Python 3.11)

'''Transformers for Google GenAI SDK.'''
import base64
from collections.abc import Iterable, Mapping
from enum import Enum, EnumMeta
import inspect
import io
import logging
import re
import sys
import time
import types as builtin_types
import typing
from typing import Any, GenericAlias, List, Optional, Sequence, Union
from _mcp_utils import mcp_to_gemini_tool
from _common import get_value_by_path as getv
if typing.TYPE_CHECKING:
    import PIL.Image as PIL
import pydantic
from  import _api_client
from  import _common
from  import types
logger = logging.getLogger('google_genai._transformers')
if sys.version_info >= (3, 10):
    VersionedUnionType = builtin_types.UnionType
    _UNION_TYPES = (typing.Union, builtin_types.UnionType)
    from typing import TypeGuard
else:
    VersionedUnionType = typing._UnionGenericAlias
    _UNION_TYPES = (typing.Union,)
    from typing_extensions import TypeGuard
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

    metric_name_sdk_api_map = {
        'exact_match': 'exactMatchSpec',
        'bleu': 'bleuSpec',
        'rouge_spec': 'rougeSpec' }
    metric_name_api_sdk_map = metric_name_sdk_api_map.items()()
    
    def _is_duck_type_of(obj = None, cls = None):
        '''Checks if an object has all of the fields of a Pydantic model.

  This is a duck-typing alternative to `isinstance` to solve dual-import
  problems. It returns False for dictionaries, which should be handled by
  `isinstance(obj, dict)`.

  Args:
    obj: The object to check.
    cls: The Pydantic model class to duck-type against.

  Returns:
    True if the object has all the fields defined in the Pydantic model, False
    otherwise.
  '''
        pass
    # WARNING: Decompyle incomplete

    
    def _resource_name(client = None, resource_name = None, *, collection_identifier, collection_hierarchy_depth):
        """Prepends resource name with project, location, collection_identifier if needed.

  The collection_identifier will only be prepended if it's not present
  and the prepending won't violate the collection hierarchy depth.
  When the prepending condition doesn't meet, returns the input
  resource_name.

  Args:
    client: The API client.
    resource_name: The user input resource name to be completed.
    collection_identifier: The collection identifier to be prepended. See
      collection identifiers in https://google.aip.dev/122.
    collection_hierarchy_depth: The collection hierarchy depth. Only set this
      field when the resource has nested collections. For example,
      `users/vhugo1802/events/birthday-dinner-226`, the collection_identifier is
      `users` and collection_hierarchy_depth is 4. See nested collections in
      https://google.aip.dev/122.

  Example:

    resource_name = 'cachedContents/123'
    client.vertexai = True
    client.project = 'bar'
    client.location = 'us-west1'
    _resource_name(client, 'cachedContents/123',
      collection_identifier='cachedContents')
    returns: 'projects/bar/locations/us-west1/cachedContents/123'

  Example:

    resource_name = 'projects/foo/locations/us-central1/cachedContents/123'
    # resource_name = 'locations/us-central1/cachedContents/123'
    client.vertexai = True
    client.project = 'bar'
    client.location = 'us-west1'
    _resource_name(client, resource_name,
      collection_identifier='cachedContents')
    returns: 'projects/foo/locations/us-central1/cachedContents/123'

  Example:

    resource_name = '123'
    # resource_name = 'cachedContents/123'
    client.vertexai = False
    _resource_name(client, resource_name,
      collection_identifier='cachedContents')
    returns 'cachedContents/123'

  Example:
    resource_name = 'some/wrong/cachedContents/resource/name/123'
    resource_prefix = 'cachedContents'
    client.vertexai = False
    # client.vertexai = True
    _resource_name(client, resource_name,
      collection_identifier='cachedContents')
    returns: 'some/wrong/cachedContents/resource/name/123'

  Returns:
    The completed resource name.
  """
        if not resource_name.startswith(f'''{collection_identifier}/'''):
            pass
        should_prepend_collection_identifier = f'''{collection_identifier}/{resource_name}'''.count('/') + 1 == collection_hierarchy_depth
        if client.vertexai:
            if resource_name.startswith('projects/'):
                return resource_name
            if None.startswith('locations/'):
                return f'''projects/{client.project}/{resource_name}'''
            if None.startswith(f'''{collection_identifier}/'''):
                return f'''projects/{client.project}/locations/{client.location}/{resource_name}'''
            if None:
                return f'''projects/{client.project}/locations/{client.location}/{collection_identifier}/{resource_name}'''
            return None
        if None:
            return f'''{collection_identifier}/{resource_name}'''

    
    def t_model(client = None, model = None):
        if not model:
            raise ValueError('model is required.')
        if '..' in model and '?' in model or '&' in model:
            raise ValueError('invalid model parameter.')
        if client.vertexai:
            if model.startswith('projects/') and model.startswith('models/') or model.startswith('publishers/'):
                return model
            if None in model:
                (publisher, model_id) = model.split('/', 1)
                return f'''publishers/{publisher}/models/{model_id}'''
            return f'''{model}'''
        if None.startswith('models/'):
            return model
        if None.startswith('tunedModels/'):
            return model
        return f'''{model}'''

    
    def t_models_url(api_client = None, base_models = None):
        if api_client.vertexai:
            if base_models:
                return 'publishers/google/models'
            return None
        if None:
            return 'models'

    
    def t_extract_models(response = None):
        if not response:
            return []
        models = None.get('models')
    # WARNING: Decompyle incomplete

    
    def t_caches_model(api_client = None, model = None):
        model = t_model(api_client, model)
        if not model:
            return None
        if None.startswith('publishers/') and api_client.vertexai:
            return f'''projects/{api_client.project}/locations/{api_client.location}/{model}'''
        if None.startswith('models/') and api_client.vertexai:
            return f'''projects/{api_client.project}/locations/{api_client.location}/publishers/google/{model}'''

    
    def pil_to_blob(img = None):
        
        try:
            import PIL.PngImagePlugin as PIL
            PngImagePlugin = PIL.PngImagePlugin
        except ImportError:
            PngImagePlugin = None

        bytesio = io.BytesIO()
    # WARNING: Decompyle incomplete

    
    def t_function_response(function_response = None):
        if not function_response:
            raise ValueError('function_response is required.')
        if isinstance(function_response, dict):
            return types.FunctionResponse.model_validate(function_response)
        if None(function_response, types.FunctionResponse):
            return function_response
        raise None(f'''Could not parse input as FunctionResponse. Unsupported function_response type: {type(function_response)}''')

    
    def t_function_responses(function_responses = None):
        if not function_responses:
            raise ValueError('function_responses are required.')
        if isinstance(function_responses, Sequence):
            return function_responses()
        return [
            None(function_responses)]

    
    def t_blobs(blobs = None):
        if isinstance(blobs, list):
            return blobs()
        return [
            None(blobs)]

    
    def t_blob(blob = None):
        if not blob:
            raise ValueError('blob is required.')
        if _is_duck_type_of(blob, types.Blob):
            return blob
        if None(blob, dict):
            return types.Blob.model_validate(blob)
    # WARNING: Decompyle incomplete

    
    def t_image_blob(blob = None):
        blob = t_blob(blob)
        if blob.mime_type and blob.mime_type.startswith('image/'):
            return blob
        raise None(f'''Unsupported mime type: {blob.mime_type!r}''')

    
    def t_audio_blob(blob = None):
        blob = t_blob(blob)
        if blob.mime_type and blob.mime_type.startswith('audio/'):
            return blob
        raise None(f'''Unsupported mime type: {blob.mime_type!r}''')

    
    def t_part(part = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_parts(parts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_image_predictions(predictions = None):
        if not predictions:
            return None
        images = None
        for prediction in predictions:
            if prediction.get('image'):
                images.append(types.GeneratedImage(image = types.Image(gcs_uri = prediction['image']['gcsUri'], image_bytes = prediction['image']['imageBytes'])))
            return images

    ContentType = Union[(types.Content, types.ContentDict, types.PartUnionDict)]
    
    def t_content(content = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_contents_for_embed(client = None, contents = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_contents(contents = None):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_null_fields(schema = None):
        '''Process null fields in the schema so it is compatible with OpenAPI.

  The OpenAPI spec does not support \'type: \'null\' in the schema. This function
  handles this case by adding \'nullable: True\' to the null field and removing
  the {\'type\': \'null\'} entry.

  https://swagger.io/docs/specification/v3_0/data-models/data-types/#null

  Example of schema properties before and after handling null fields:
    Before:
      {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "total_area_sq_mi": {
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": None,
          "title": "Total Area Sq Mi"
        }
      }

    After:
      {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "total_area_sq_mi": {
          "type": "integer",
          "nullable": true,
          "default": None,
          "title": "Total Area Sq Mi"
        }
      }
  '''
        if schema.get('type', None) == 'null':
            schema['nullable'] = True
            del schema['type']
            return None
        if None in schema:
            for item in schema['anyOf']:
                if 'type' in item and item['type'] == 'null':
                    schema['nullable'] = True
                    schema['anyOf'].remove({
                        'type': 'null' })
                    if len(schema['anyOf']) == 1:
                        for key, val in schema['anyOf'][0].items():
                            schema[key] = val
                            del schema['anyOf']
                            return None
                            return None

    
    def _raise_for_unsupported_schema_type(origin = None):
        '''Raises an error if the schema type is unsupported.'''
        raise ValueError(f'''Unsupported schema type: {origin}''')

    
    def _raise_for_unsupported_mldev_properties(schema = None, client = None):
        if not client or client.vertexai:
            if schema.get('additionalProperties') or schema.get('additional_properties'):
                raise ValueError('additionalProperties is not supported in the Gemini API.')
            return None
        return None

    
    def process_schema(schema = None, client = None, defs = None, *, order_properties):
        """Updates the schema and each sub-schema inplace to be API-compatible.

  - Inlines the $defs.

  Example of a schema before and after (with mldev):
    Before:

    `schema`

    {
        'items': {
            '$ref': '#/$defs/CountryInfo'
        },
        'title': 'Placeholder',
        'type': 'array'
    }


    `defs`

    {
      'CountryInfo': {
        'properties': {
          'continent': {
              'title': 'Continent',
              'type': 'string'
          },
          'gdp': {
              'title': 'Gdp',
              'type': 'integer'}
          },
        }
        'required':['continent', 'gdp'],
        'title': 'CountryInfo',
        'type': 'object'
      }
    }

    After:

    `schema`
     {
        'items': {
          'properties': {
            'continent': {
              'title': 'Continent',
              'type': 'string'
            },
            'gdp': {
              'title': 'Gdp',
              'type': 'integer'
            },
          }
          'required':['continent', 'gdp'],
          'title': 'CountryInfo',
          'type': 'object'
        },
        'type': 'array'
    }
  """
        pass
    # WARNING: Decompyle incomplete

    
    def _process_enum(enum = None, client = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_type_dict_str_any(origin = None):
        '''Verifies the schema is of type dict[str, Any] for mypy type checking.'''
        if isinstance(origin, dict):
            pass
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(origin())

    
    def t_schema(client = None, origin = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_speech_config(origin = None):
        if not origin:
            return None
        if None(origin, types.SpeechConfig):
            return origin
        if None(origin, str):
            return types.SpeechConfig(voice_config = types.VoiceConfig(prebuilt_voice_config = types.PrebuiltVoiceConfig(voice_name = origin)))
        if None(origin, dict):
            return types.SpeechConfig.model_validate(origin)
        raise None(f'''Unsupported speechConfig type: {type(origin)}''')

    
    def t_live_speech_config(origin = None):
        if _is_duck_type_of(origin, types.SpeechConfig):
            speech_config = origin
        if isinstance(origin, dict):
            speech_config = types.SpeechConfig.model_validate(origin)
    # WARNING: Decompyle incomplete

    
    def t_tool(client = None, origin = None):
        if not origin:
            return None
        if None.isfunction(origin) or inspect.ismethod(origin):
            return types.Tool(function_declarations = [
                types.FunctionDeclaration.from_callable(client = client, callable = origin)])
    # WARNING: Decompyle incomplete

    
    def t_tools(client = None, origin = None):
        if not origin:
            return []
        function_tool = None.Tool(function_declarations = [])
        tools = []
    # WARNING: Decompyle incomplete

    
    def t_cached_content_name(client = None, name = None):
        return _resource_name(client, name, collection_identifier = 'cachedContents')

    
    def t_batch_job_source(client = None, src = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_embedding_batch_job_source(client = None, src = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_batch_job_destination(dest = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_recv_batch_job_destination(dest = None):
        inline_responses = dest.get('inlinedResponses', { }).get('inlinedResponses', [])
        if not inline_responses:
            return dest
        for response in None:
            inner_response = response.get('response', { })
            if not inner_response:
                continue
            if 'embedding' in inner_response:
                dest['inlinedEmbedContentResponses'] = dest.pop('inlinedResponses')
            
            return dest

    
    def t_batch_job_name(client = None, name = None):
        if not client.vertexai:
            mldev_pattern = 'batches/[^/]+$'
            if re.match(mldev_pattern, name):
                return name.split('/')[-1]
            raise None(f'''Invalid batch job name: {name}.''')
        vertex_pattern = '^projects/[^/]+/locations/[^/]+/batchPredictionJobs/[^/]+$'
        if re.match(vertex_pattern, name):
            return name.split('/')[-1]
        if None.isdigit():
            return name
        raise None(f'''Invalid batch job name: {name}.''')

    
    def t_job_state(state = None):
        if state == 'BATCH_STATE_UNSPECIFIED':
            return 'JOB_STATE_UNSPECIFIED'
        if None == 'BATCH_STATE_PENDING':
            return 'JOB_STATE_PENDING'
        if None == 'BATCH_STATE_RUNNING':
            return 'JOB_STATE_RUNNING'
        if None == 'BATCH_STATE_SUCCEEDED':
            return 'JOB_STATE_SUCCEEDED'
        if None == 'BATCH_STATE_FAILED':
            return 'JOB_STATE_FAILED'
        if None == 'BATCH_STATE_CANCELLED':
            return 'JOB_STATE_CANCELLED'
        if None == 'BATCH_STATE_EXPIRED':
            return 'JOB_STATE_EXPIRED'

    LRO_POLLING_INITIAL_DELAY_SECONDS = 1
    LRO_POLLING_MAXIMUM_DELAY_SECONDS = 20
    LRO_POLLING_TIMEOUT_SECONDS = 900
    LRO_POLLING_MULTIPLIER = 1.5
    
    def t_resolve_operation(api_client = None, struct = None):
        name = struct.get('name')
    # WARNING: Decompyle incomplete

    
    def t_file_name(name = None):
        if _is_duck_type_of(name, types.File):
            name = name.name
        elif _is_duck_type_of(name, types.Video):
            name = name.uri
    # WARNING: Decompyle incomplete

    
    def t_tuning_job_status(status = None):
        if status == 'STATE_UNSPECIFIED':
            return types.JobState.JOB_STATE_UNSPECIFIED
        if None == 'CREATING':
            return types.JobState.JOB_STATE_RUNNING
        if None == 'ACTIVE':
            return types.JobState.JOB_STATE_SUCCEEDED
        if None == 'FAILED':
            return types.JobState.JOB_STATE_FAILED
        for state in None.JobState:
            if str(state.value) == status:
                
                return None, state
            return status

    
    def t_content_strict(content = None):
        if isinstance(content, dict):
            return types.Content.model_validate(content)
        if None(content, types.Content):
            return content
        raise None(f'''Could not convert input (type "{type(content)}") to `types.Content`''')

    
    def t_contents_strict(contents = None):
        if isinstance(contents, Sequence):
            return contents()
        return [
            None(contents)]

    
    def t_client_content(turns = None, turn_complete = None):
        pass
    # WARNING: Decompyle incomplete

    
    def t_tool_response(input = None):
        if not input:
            raise ValueError(f'''A tool response is required, got: \n{input}''')
        
        try:
            return types.LiveClientToolResponse(function_responses = t_function_responses(function_responses = input))
        except Exception:
            e = None
            raise ValueError(f'''Could not convert input (type "{type(input)}") to `types.LiveClientToolResponse`'''), e
            e = None
            del e


    
    def t_metrics(metrics = None):
        '''Prepares the metric payload for the evaluation request.

    Args:
        request_dict: The dictionary containing the request details.
        resolved_metrics: A list of resolved metric objects.

    Returns:
        The updated request dictionary with the prepared metric payload.
    '''
        metrics_payload = []
        for metric in metrics:
            metric_payload_item = { }
            metric_payload_item['aggregation_metrics'] = [
                'AVERAGE',
                'STANDARD_DEVIATION']
            metric_name = getv(metric, [
                'name']).lower()
            if metric_name == 'exact_match':
                metric_payload_item['exact_match_spec'] = { }
            elif metric_name == 'bleu':
                metric_payload_item['bleu_spec'] = { }
            elif metric_name.startswith('rouge'):
                rouge_type = metric_name.replace('_', '')
                metric_payload_item['rouge_spec'] = {
                    'rouge_type': rouge_type }
            elif hasattr(metric, 'prompt_template') and metric.prompt_template:
                pointwise_spec = {
                    'metric_prompt_template': metric.prompt_template }
                system_instruction = getv(metric, [
                    'judge_model_system_instruction'])
                if system_instruction:
                    pointwise_spec['system_instruction'] = system_instruction
                return_raw_output = getv(metric, [
                    'return_raw_output'])
                if return_raw_output:
                    pointwise_spec['custom_output_format_config'] = {
                        'return_raw_output': return_raw_output }
                metric_payload_item['pointwise_metric_spec'] = pointwise_spec
            else:
                raise ValueError(f'''Unsupported metric type or invalid metric name: {metric_name}''')
            metrics_payload.append(metric_payload_item)
            return metrics_payload

    return None
