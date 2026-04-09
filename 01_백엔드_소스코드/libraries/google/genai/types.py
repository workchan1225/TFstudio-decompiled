# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from abc import ABC, abstractmethod
import datetime
from enum import Enum, EnumMeta
import inspect
import io
import json
import logging
import sys
import types as builtin_types
import typing
from typing import Any, Callable, Dict, List, Literal, Optional, Sequence, Union, _UnionGenericAlias
import pydantic
from pydantic import ConfigDict, Field, PrivateAttr, model_validator
from typing_extensions import Self, TypedDict
from  import _common
from _operations_converters import _GenerateVideosOperation_from_mldev, _GenerateVideosOperation_from_vertex, _ImportFileOperation_from_mldev, _UploadToFileSearchStoreOperation_from_mldev
if sys.version_info >= (3, 10):
    VersionedUnionType = Union[(builtin_types.UnionType, _UnionGenericAlias)]
    _UNION_TYPES = (typing.Union, builtin_types.UnionType)
else:
    VersionedUnionType = _UnionGenericAlias
    _UNION_TYPES = (typing.Union,)
_is_pillow_image_imported = False
ToolListUnion = list[ToolUnion]
ToolListUnionDict = list[ToolUnionDict]
SchemaUnion = Union[(dict[(Any, Any)], type, Schema, builtin_types.GenericAlias, VersionedUnionType)]
SchemaUnionDict = Union[(SchemaUnion, SchemaDict)]

class FunctionCallingConfig(_common.BaseModel):
    '''Function calling config.'''
    mode: Optional[FunctionCallingConfigMode] = Field(default = None, description = 'Optional. Function calling mode.')
    allowed_function_names: Optional[list[str]] = Field(default = None, description = 'Optional. Function names to call. Only set when the Mode is ANY. Function names should match [FunctionDeclaration.name]. With mode set to ANY, model will predict a function call from the set of function names provided.')
    stream_function_call_arguments: Optional[bool] = Field(default = None, description = 'Optional. When set to true, arguments of a single function call will be streamed out in multiple parts/contents/responses. Partial parameter results will be returned in the [FunctionCall.partial_args] field. This field is not supported in Gemini API.')


def FunctionCallingConfigDict():
    '''FunctionCallingConfigDict'''
    stream_function_call_arguments: Optional[bool] = 'Function calling config.'

FunctionCallingConfigDict = <NODE:27>(FunctionCallingConfigDict, 'FunctionCallingConfigDict', TypedDict, total = False)
FunctionCallingConfigOrDict = Union[(FunctionCallingConfig, FunctionCallingConfigDict)]

class LatLng(_common.BaseModel):
    '''An object that represents a latitude/longitude pair.

  This is expressed as a pair of doubles to represent degrees latitude and
  degrees longitude. Unless specified otherwise, this object must conform to the
  <a href="https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version">
  WGS84 standard</a>. Values must be within normalized ranges.
  '''
    latitude: Optional[float] = Field(default = None, description = 'The latitude in degrees. It must be in the range [-90.0, +90.0].')
    longitude: Optional[float] = Field(default = None, description = 'The longitude in degrees. It must be in the range [-180.0, +180.0]')


def LatLngDict():
    '''LatLngDict'''
    longitude: Optional[float] = 'An object that represents a latitude/longitude pair.\n\n  This is expressed as a pair of doubles to represent degrees latitude and\n  degrees longitude. Unless specified otherwise, this object must conform to the\n  <a href="https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version">\n  WGS84 standard</a>. Values must be within normalized ranges.\n  '

LatLngDict = <NODE:27>(LatLngDict, 'LatLngDict', TypedDict, total = False)
LatLngOrDict = Union[(LatLng, LatLngDict)]

class RetrievalConfig(_common.BaseModel):
    '''Retrieval config.'''
    lat_lng: Optional[LatLng] = Field(default = None, description = 'Optional. The location of the user.')
    language_code: Optional[str] = Field(default = None, description = 'The language code of the user.')


def RetrievalConfigDict():
    '''RetrievalConfigDict'''
    language_code: Optional[str] = 'Retrieval config.'

RetrievalConfigDict = <NODE:27>(RetrievalConfigDict, 'RetrievalConfigDict', TypedDict, total = False)
RetrievalConfigOrDict = Union[(RetrievalConfig, RetrievalConfigDict)]

class ToolConfig(_common.BaseModel):
    '''Tool config.

  This config is shared for all tools provided in the request.
  '''
    function_calling_config: Optional[FunctionCallingConfig] = Field(default = None, description = 'Optional. Function calling config.')
    retrieval_config: Optional[RetrievalConfig] = Field(default = None, description = 'Optional. Retrieval config.')


def ToolConfigDict():
    '''ToolConfigDict'''
    retrieval_config: Optional[RetrievalConfigDict] = 'Tool config.\n\n  This config is shared for all tools provided in the request.\n  '

ToolConfigDict = <NODE:27>(ToolConfigDict, 'ToolConfigDict', TypedDict, total = False)
ToolConfigOrDict = Union[(ToolConfig, ToolConfigDict)]

class ReplicatedVoiceConfig(_common.BaseModel):
    '''ReplicatedVoiceConfig is used to configure replicated voice.'''
    mime_type: Optional[str] = Field(default = None, description = 'The mime type of the replicated voice.\n      ')
    voice_sample_audio: Optional[bytes] = Field(default = None, description = 'The sample audio of the replicated voice.\n      ')


def ReplicatedVoiceConfigDict():
    '''ReplicatedVoiceConfigDict'''
    voice_sample_audio: Optional[bytes] = 'ReplicatedVoiceConfig is used to configure replicated voice.'

ReplicatedVoiceConfigDict = <NODE:27>(ReplicatedVoiceConfigDict, 'ReplicatedVoiceConfigDict', TypedDict, total = False)
ReplicatedVoiceConfigOrDict = Union[(ReplicatedVoiceConfig, ReplicatedVoiceConfigDict)]

class PrebuiltVoiceConfig(_common.BaseModel):
    '''The configuration for the prebuilt speaker to use.'''
    voice_name: Optional[str] = Field(default = None, description = 'The name of the preset voice to use.')


def PrebuiltVoiceConfigDict():
    '''PrebuiltVoiceConfigDict'''
    voice_name: Optional[str] = 'The configuration for the prebuilt speaker to use.'

PrebuiltVoiceConfigDict = <NODE:27>(PrebuiltVoiceConfigDict, 'PrebuiltVoiceConfigDict', TypedDict, total = False)
PrebuiltVoiceConfigOrDict = Union[(PrebuiltVoiceConfig, PrebuiltVoiceConfigDict)]

class VoiceConfig(_common.BaseModel):
    replicated_voice_config: Optional[ReplicatedVoiceConfig] = Field(default = None, description = 'If true, the model will use a replicated voice for the response.')
    prebuilt_voice_config: Optional[PrebuiltVoiceConfig] = Field(default = None, description = 'The configuration for the prebuilt voice to use.')


def VoiceConfigDict():
    '''VoiceConfigDict'''
    prebuilt_voice_config: Optional[PrebuiltVoiceConfigDict] = 'VoiceConfigDict'

VoiceConfigDict = <NODE:27>(VoiceConfigDict, 'VoiceConfigDict', TypedDict, total = False)
VoiceConfigOrDict = Union[(VoiceConfig, VoiceConfigDict)]

class SpeakerVoiceConfig(_common.BaseModel):
    '''Configuration for a single speaker in a multi speaker setup.'''
    speaker: Optional[str] = Field(default = None, description = 'Required. The name of the speaker. This should be the same as the speaker name used in the prompt.')
    voice_config: Optional[VoiceConfig] = Field(default = None, description = 'Required. The configuration for the voice of this speaker.')


def SpeakerVoiceConfigDict():
    '''SpeakerVoiceConfigDict'''
    voice_config: Optional[VoiceConfigDict] = 'Configuration for a single speaker in a multi speaker setup.'

SpeakerVoiceConfigDict = <NODE:27>(SpeakerVoiceConfigDict, 'SpeakerVoiceConfigDict', TypedDict, total = False)
SpeakerVoiceConfigOrDict = Union[(SpeakerVoiceConfig, SpeakerVoiceConfigDict)]

class MultiSpeakerVoiceConfig(_common.BaseModel):
    '''The configuration for the multi-speaker setup.

  This data type is not supported in Vertex AI.
  '''
    speaker_voice_configs: Optional[list[SpeakerVoiceConfig]] = Field(default = None, description = 'Required. All the enabled speaker voices.')


def MultiSpeakerVoiceConfigDict():
    '''MultiSpeakerVoiceConfigDict'''
    speaker_voice_configs: Optional[list[SpeakerVoiceConfigDict]] = 'The configuration for the multi-speaker setup.\n\n  This data type is not supported in Vertex AI.\n  '

MultiSpeakerVoiceConfigDict = <NODE:27>(MultiSpeakerVoiceConfigDict, 'MultiSpeakerVoiceConfigDict', TypedDict, total = False)
MultiSpeakerVoiceConfigOrDict = Union[(MultiSpeakerVoiceConfig, MultiSpeakerVoiceConfigDict)]

class SpeechConfig(_common.BaseModel):
    voice_config: Optional[VoiceConfig] = Field(default = None, description = 'Configuration for the voice of the response.')
    language_code: Optional[str] = Field(default = None, description = 'Optional. Language code (ISO 639. e.g. en-US) for the speech synthesization.')
    multi_speaker_voice_config: Optional[MultiSpeakerVoiceConfig] = Field(default = None, description = 'Optional. The configuration for the multi-speaker setup. It is mutually exclusive with the voice_config field. This field is not supported in Vertex AI.')


def SpeechConfigDict():
    '''SpeechConfigDict'''
    multi_speaker_voice_config: Optional[MultiSpeakerVoiceConfigDict] = 'SpeechConfigDict'

SpeechConfigDict = <NODE:27>(SpeechConfigDict, 'SpeechConfigDict', TypedDict, total = False)
SpeechConfigOrDict = Union[(SpeechConfig, SpeechConfigDict)]

class AutomaticFunctionCallingConfig(_common.BaseModel):
    '''The configuration for automatic function calling.'''
    disable: Optional[bool] = Field(default = None, description = 'Whether to disable automatic function calling.\n      If not set or set to False, will enable automatic function calling.\n      If set to True, will disable automatic function calling.\n      ')
    maximum_remote_calls: Optional[int] = Field(default = 10, description = 'If automatic function calling is enabled,\n      maximum number of remote calls for automatic function calling.\n      This number should be a positive integer.\n      If not set, SDK will set maximum number of remote calls to 10.\n      ')
    ignore_call_history: Optional[bool] = Field(default = None, description = 'If automatic function calling is enabled,\n      whether to ignore call history to the response.\n      If not set, SDK will set ignore_call_history to false,\n      and will append the call history to\n      GenerateContentResponse.automatic_function_calling_history.\n      ')


def AutomaticFunctionCallingConfigDict():
    '''AutomaticFunctionCallingConfigDict'''
    ignore_call_history: Optional[bool] = 'The configuration for automatic function calling.'

AutomaticFunctionCallingConfigDict = <NODE:27>(AutomaticFunctionCallingConfigDict, 'AutomaticFunctionCallingConfigDict', TypedDict, total = False)
AutomaticFunctionCallingConfigOrDict = Union[(AutomaticFunctionCallingConfig, AutomaticFunctionCallingConfigDict)]

class ThinkingConfig(_common.BaseModel):
    '''The thinking features configuration.'''
    include_thoughts: Optional[bool] = Field(default = None, description = 'Indicates whether to include thoughts in the response. If true, thoughts are returned only if the model supports thought and thoughts are available.\n      ')
    thinking_budget: Optional[int] = Field(default = None, description = 'Indicates the thinking budget in tokens. 0 is DISABLED. -1 is AUTOMATIC. The default values and allowed ranges are model dependent.\n      ')
    thinking_level: Optional[ThinkingLevel] = Field(default = None, description = 'Optional. The level of thoughts tokens that the model should generate.')


def ThinkingConfigDict():
    '''ThinkingConfigDict'''
    thinking_level: Optional[ThinkingLevel] = 'The thinking features configuration.'

ThinkingConfigDict = <NODE:27>(ThinkingConfigDict, 'ThinkingConfigDict', TypedDict, total = False)
ThinkingConfigOrDict = Union[(ThinkingConfig, ThinkingConfigDict)]

class ImageConfig(_common.BaseModel):
    '''The image generation configuration to be used in GenerateContentConfig.'''
    aspect_ratio: Optional[str] = Field(default = None, description = 'Aspect ratio of the generated images. Supported values are\n      "1:1", "2:3", "3:2", "3:4", "4:3", "9:16", "16:9", and "21:9".')
    image_size: Optional[str] = Field(default = None, description = 'Optional. Specifies the size of generated images. Supported\n      values are `1K`, `2K`, `4K`. If not specified, the model will use default\n      value `1K`.')
    output_mime_type: Optional[str] = Field(default = None, description = 'MIME type of the generated image. This field is not\n      supported in Gemini API.')
    output_compression_quality: Optional[int] = Field(default = None, description = 'Compression quality of the generated image (for\n      ``image/jpeg`` only). This field is not supported in Gemini API.')


def ImageConfigDict():
    '''ImageConfigDict'''
    output_compression_quality: Optional[int] = 'The image generation configuration to be used in GenerateContentConfig.'

ImageConfigDict = <NODE:27>(ImageConfigDict, 'ImageConfigDict', TypedDict, total = False)
ImageConfigOrDict = Union[(ImageConfig, ImageConfigDict)]

class FileStatus(_common.BaseModel):
    '''Status of a File that uses a common error model.'''
    details: Optional[list[dict[(str, Any)]]] = Field(default = None, description = 'A list of messages that carry the error details. There is a common set of message types for APIs to use.')
    message: Optional[str] = Field(default = None, description = 'A list of messages that carry the error details. There is a common set of message types for APIs to use.')
    code: Optional[int] = Field(default = None, description = 'The status code. 0 for OK, 1 for CANCELLED')


def FileStatusDict():
    '''FileStatusDict'''
    code: Optional[int] = 'Status of a File that uses a common error model.'

FileStatusDict = <NODE:27>(FileStatusDict, 'FileStatusDict', TypedDict, total = False)
FileStatusOrDict = Union[(FileStatus, FileStatusDict)]

class File(_common.BaseModel):
    '''A file uploaded to the API.'''
    name: Optional[str] = Field(default = None, description = 'The `File` resource name. The ID (name excluding the "files/" prefix) can contain up to 40 characters that are lowercase alphanumeric or dashes (-). The ID cannot start or end with a dash. If the name is empty on create, a unique name will be generated. Example: `files/123-456`')
    display_name: Optional[str] = Field(default = None, description = "Optional. The human-readable display name for the `File`. The display name must be no more than 512 characters in length, including spaces. Example: 'Welcome Image'")
    mime_type: Optional[str] = Field(default = None, description = 'Output only. MIME type of the file.')
    size_bytes: Optional[int] = Field(default = None, description = 'Output only. Size of the file in bytes.')
    create_time: Optional[datetime.datetime] = Field(default = None, description = 'Output only. The timestamp of when the `File` was created.')
    expiration_time: Optional[datetime.datetime] = Field(default = None, description = 'Output only. The timestamp of when the `File` will be deleted. Only set if the `File` is scheduled to expire.')
    update_time: Optional[datetime.datetime] = Field(default = None, description = 'Output only. The timestamp of when the `File` was last updated.')
    sha256_hash: Optional[str] = Field(default = None, description = 'Output only. SHA-256 hash of the uploaded bytes. The hash value is encoded in base64 format.')
    uri: Optional[str] = Field(default = None, description = 'Output only. The URI of the `File`.')
    download_uri: Optional[str] = Field(default = None, description = 'Output only. The URI of the `File`, only set for downloadable (generated) files.')
    state: Optional[FileState] = Field(default = None, description = 'Output only. Processing state of the File.')
    source: Optional[FileSource] = Field(default = None, description = 'Output only. The source of the `File`.')
    video_metadata: Optional[dict[(str, Any)]] = Field(default = None, description = 'Output only. Metadata for a video.')
    error: Optional[FileStatus] = Field(default = None, description = 'Output only. Error status if File processing failed.')


def FileDict():
    '''FileDict'''
    error: Optional[FileStatusDict] = 'A file uploaded to the API.'

FileDict = <NODE:27>(FileDict, 'FileDict', TypedDict, total = False)
FileOrDict = Union[(File, FileDict)]
ContentUnion = Union[(Content, PartUnion, list[PartUnion])]
ContentUnionDict = Union[(Content, ContentDict, PartUnionDict, list[PartUnionDict])]

class GenerationConfigRoutingConfigAutoRoutingMode(_common.BaseModel):
    '''When automated routing is specified, the routing will be determined by the pretrained routing model and customer provided model routing preference.

  This data type is not supported in Gemini API.
  '''
    model_routing_preference: Optional[Literal[('UNKNOWN', 'PRIORITIZE_QUALITY', 'BALANCED', 'PRIORITIZE_COST')]] = Field(default = None, description = 'The model routing preference.')


def GenerationConfigRoutingConfigAutoRoutingModeDict():
    '''GenerationConfigRoutingConfigAutoRoutingModeDict'''
    model_routing_preference: Optional[Literal[('UNKNOWN', 'PRIORITIZE_QUALITY', 'BALANCED', 'PRIORITIZE_COST')]] = 'When automated routing is specified, the routing will be determined by the pretrained routing model and customer provided model routing preference.\n\n  This data type is not supported in Gemini API.\n  '

GenerationConfigRoutingConfigAutoRoutingModeDict = <NODE:27>(GenerationConfigRoutingConfigAutoRoutingModeDict, 'GenerationConfigRoutingConfigAutoRoutingModeDict', TypedDict, total = False)
GenerationConfigRoutingConfigAutoRoutingModeOrDict = Union[(GenerationConfigRoutingConfigAutoRoutingMode, GenerationConfigRoutingConfigAutoRoutingModeDict)]

class GenerationConfigRoutingConfigManualRoutingMode(_common.BaseModel):
    '''When manual routing is set, the specified model will be used directly.

  This data type is not supported in Gemini API.
  '''
    model_name: Optional[str] = Field(default = None, description = 'The model name to use. Only the public LLM models are accepted. See [Supported models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models).')


def GenerationConfigRoutingConfigManualRoutingModeDict():
    '''GenerationConfigRoutingConfigManualRoutingModeDict'''
    model_name: Optional[str] = 'When manual routing is set, the specified model will be used directly.\n\n  This data type is not supported in Gemini API.\n  '

GenerationConfigRoutingConfigManualRoutingModeDict = <NODE:27>(GenerationConfigRoutingConfigManualRoutingModeDict, 'GenerationConfigRoutingConfigManualRoutingModeDict', TypedDict, total = False)
GenerationConfigRoutingConfigManualRoutingModeOrDict = Union[(GenerationConfigRoutingConfigManualRoutingMode, GenerationConfigRoutingConfigManualRoutingModeDict)]

class GenerationConfigRoutingConfig(_common.BaseModel):
    '''The configuration for routing the request to a specific model.

  This data type is not supported in Gemini API.
  '''
    auto_mode: Optional[GenerationConfigRoutingConfigAutoRoutingMode] = Field(default = None, description = 'Automated routing.')
    manual_mode: Optional[GenerationConfigRoutingConfigManualRoutingMode] = Field(default = None, description = 'Manual routing.')


def GenerationConfigRoutingConfigDict():
    '''GenerationConfigRoutingConfigDict'''
    manual_mode: Optional[GenerationConfigRoutingConfigManualRoutingModeDict] = 'The configuration for routing the request to a specific model.\n\n  This data type is not supported in Gemini API.\n  '

GenerationConfigRoutingConfigDict = <NODE:27>(GenerationConfigRoutingConfigDict, 'GenerationConfigRoutingConfigDict', TypedDict, total = False)
GenerationConfigRoutingConfigOrDict = Union[(GenerationConfigRoutingConfig, GenerationConfigRoutingConfigDict)]

class SafetySetting(_common.BaseModel):
    '''Safety settings.'''
    category: Optional[HarmCategory] = Field(default = None, description = 'Required. Harm category.')
    method: Optional[HarmBlockMethod] = Field(default = None, description = 'Optional. Specify if the threshold is used for probability or severity score. If not specified, the threshold is used for probability score. This field is not supported in Gemini API.')
    threshold: Optional[HarmBlockThreshold] = Field(default = None, description = 'Required. The harm block threshold.')


def SafetySettingDict():
    '''SafetySettingDict'''
    threshold: Optional[HarmBlockThreshold] = 'Safety settings.'

SafetySettingDict = <NODE:27>(SafetySettingDict, 'SafetySettingDict', TypedDict, total = False)
SafetySettingOrDict = Union[(SafetySetting, SafetySettingDict)]
SpeechConfigUnion = Union[(str, SpeechConfig)]
SpeechConfigUnionDict = Union[(str, SpeechConfig, SpeechConfigDict)]

class GenerateContentConfig(_common.BaseModel):
    '''Optional model configuration parameters.

  For more information, see `Content generation parameters
  <https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters>`_.
  '''
    http_options: Optional[HttpOptions] = Field(default = None, description = 'Used to override HTTP request options.')
    should_return_http_response: Optional[bool] = Field(default = None, description = " If true, the raw HTTP response will be returned in the 'sdk_http_response' field.")
    system_instruction: Optional[ContentUnion] = Field(default = None, description = 'Instructions for the model to steer it toward better performance.\n      For example, "Answer as concisely as possible" or "Don\'t use technical\n      terms in your response".\n      ')
    temperature: Optional[float] = Field(default = None, description = 'Value that controls the degree of randomness in token selection.\n      Lower temperatures are good for prompts that require a less open-ended or\n      creative response, while higher temperatures can lead to more diverse or\n      creative results.\n      ')
    top_p: Optional[float] = Field(default = None, description = 'Tokens are selected from the most to least probable until the sum\n      of their probabilities equals this value. Use a lower value for less\n      random responses and a higher value for more random responses.\n      ')
    top_k: Optional[float] = Field(default = None, description = 'For each token selection step, the ``top_k`` tokens with the\n      highest probabilities are sampled. Then tokens are further filtered based\n      on ``top_p`` with the final token selected using temperature sampling. Use\n      a lower number for less random responses and a higher number for more\n      random responses.\n      ')
    candidate_count: Optional[int] = Field(default = None, description = 'Number of response variations to return.\n      ')
    max_output_tokens: Optional[int] = Field(default = None, description = 'Maximum number of tokens that can be generated in the response.\n      ')
    stop_sequences: Optional[list[str]] = Field(default = None, description = 'List of strings that tells the model to stop generating text if one\n      of the strings is encountered in the response.\n      ')
    response_logprobs: Optional[bool] = Field(default = None, description = 'Whether to return the log probabilities of the tokens that were\n      chosen by the model at each step.\n      ')
    logprobs: Optional[int] = Field(default = None, description = 'Number of top candidate tokens to return the log probabilities for\n      at each generation step.\n      ')
    presence_penalty: Optional[float] = Field(default = None, description = 'Positive values penalize tokens that already appear in the\n      generated text, increasing the probability of generating more diverse\n      content.\n      ')
    frequency_penalty: Optional[float] = Field(default = None, description = 'Positive values penalize tokens that repeatedly appear in the\n      generated text, increasing the probability of generating more diverse\n      content.\n      ')
    seed: Optional[int] = Field(default = None, description = 'When ``seed`` is fixed to a specific number, the model makes a best\n      effort to provide the same response for repeated requests. By default, a\n      random number is used.\n      ')
    response_mime_type: Optional[str] = Field(default = None, description = 'Output response mimetype of the generated candidate text.\n      Supported mimetype:\n        - `text/plain`: (default) Text output.\n        - `application/json`: JSON response in the candidates.\n      The model needs to be prompted to output the appropriate response type,\n      otherwise the behavior is undefined.\n      This is a preview feature.\n      ')
    response_schema: Optional[SchemaUnion] = Field(default = None, description = "The `Schema` object allows the definition of input and output data types.\n      These types can be objects, but also primitives and arrays.\n      Represents a select subset of an [OpenAPI 3.0 schema\n      object](https://spec.openapis.org/oas/v3.0.3#schema).\n      If set, a compatible response_mime_type must also be set.\n      Compatible mimetypes: `application/json`: Schema for JSON response.\n\n      If `response_schema` doesn't process your schema correctly, try using\n      `response_json_schema` instead.\n      ")
    response_json_schema: Optional[Any] = Field(default = None, description = 'Optional. Output schema of the generated response.\n      This is an alternative to `response_schema` that accepts [JSON\n      Schema](https://json-schema.org/). If set, `response_schema` must be\n      omitted, but `response_mime_type` is required. While the full JSON Schema\n      may be sent, not all features are supported. Specifically, only the\n      following properties are supported: - `$id` - `$defs` - `$ref` - `$anchor`\n      - `type` - `format` - `title` - `description` - `enum` (for strings and\n      numbers) - `items` - `prefixItems` - `minItems` - `maxItems` - `minimum` -\n      `maximum` - `anyOf` - `oneOf` (interpreted the same as `anyOf`) -\n      `properties` - `additionalProperties` - `required` The non-standard\n      `propertyOrdering` property may also be set. Cyclic references are\n      unrolled to a limited degree and, as such, may only be used within\n      non-required properties. (Nullable properties are not sufficient.) If\n      `$ref` is set on a sub-schema, no other properties, except for than those\n      starting as a `$`, may be set.')
    routing_config: Optional[GenerationConfigRoutingConfig] = Field(default = None, description = 'Configuration for model router requests.\n      ')
    model_selection_config: Optional[ModelSelectionConfig] = Field(default = None, description = 'Configuration for model selection.\n      ')
    safety_settings: Optional[list[SafetySetting]] = Field(default = None, description = 'Safety settings in the request to block unsafe content in the\n      response.\n      ')
    tools: Optional[ToolListUnion] = Field(default = None, description = 'Code that enables the system to interact with external systems to\n      perform an action outside of the knowledge and scope of the model.\n      ')
    tool_config: Optional[ToolConfig] = Field(default = None, description = 'Associates model output to a specific function call.\n      ')
    labels: Optional[dict[(str, str)]] = Field(default = None, description = 'Labels with user-defined metadata to break down billed charges.')
    cached_content: Optional[str] = Field(default = None, description = 'Resource name of a context cache that can be used in subsequent\n      requests.\n      ')
    response_modalities: Optional[list[str]] = Field(default = None, description = 'The requested modalities of the response. Represents the set of\n      modalities that the model can return.\n      ')
    media_resolution: Optional[MediaResolution] = Field(default = None, description = 'If specified, the media resolution specified will be used.\n    ')
    speech_config: Optional[SpeechConfigUnion] = Field(default = None, description = 'The speech generation configuration.\n      ')
    audio_timestamp: Optional[bool] = Field(default = None, description = 'If enabled, audio timestamp will be included in the request to the\n       model.\n      ')
    automatic_function_calling: Optional[AutomaticFunctionCallingConfig] = Field(default = None, description = 'The configuration for automatic function calling.\n      ')
    thinking_config: Optional[ThinkingConfig] = Field(default = None, description = 'The thinking features configuration.\n      ')
    image_config: Optional[ImageConfig] = Field(default = None, description = 'The image generation configuration.\n      ')
    _convert_literal_to_enum = (lambda cls = None, value = pydantic.field_validator('response_schema', mode = 'before'): if typing.get_origin(value) is typing.Literal:
enum_vals = typing.get_args(value)if not (lambda .0: pass# WARNING: Decompyle incomplete
)(enum_vals()):
                raise ValueError(f'''Literal type {value} must be a list of strings.''')
            
            def <dictcomp>(.0):
                pass
            # WARNING: Decompyle incomplete

            return 'PlaceholderLiteralEnum'(<dictcomp>, enum_vals())
)()()
    _check_image_config_type = (lambda cls = None, value = pydantic.field_validator('image_config', mode = 'before'): if isinstance(value, GenerateImagesConfig):
raise ValueError('image_config must be an instance of ImageConfig or compatible dict.')value)()()


def GenerateContentConfigDict():
    '''GenerateContentConfigDict'''
    image_config: Optional[ImageConfigDict] = 'Optional model configuration parameters.\n\n  For more information, see `Content generation parameters\n  <https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters>`_.\n  '

GenerateContentConfigDict = <NODE:27>(GenerateContentConfigDict, 'GenerateContentConfigDict', TypedDict, total = False)
GenerateContentConfigOrDict = Union[(GenerateContentConfig, GenerateContentConfigDict)]
ContentListUnion = Union[(ContentUnion, list[ContentUnion])]
ContentListUnionDict = Union[(ContentUnionDict, list[ContentUnionDict])]

class _GenerateContentParameters(_common.BaseModel):
    '''Config for models.generate_content parameters.'''
    model: Optional[str] = Field(default = None, description = 'ID of the model to use. For a list of models, see `Google models\n    <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models>`_.')
    contents: Optional[ContentListUnion] = Field(default = None, description = 'Content of the request.\n      ')
    config: Optional[GenerateContentConfig] = Field(default = None, description = 'Configuration that contains optional model parameters.\n      ')


def _GenerateContentParametersDict():
    '''_GenerateContentParametersDict'''
    config: Optional[GenerateContentConfigDict] = 'Config for models.generate_content parameters.'

_GenerateContentParametersDict = <NODE:27>(_GenerateContentParametersDict, '_GenerateContentParametersDict', TypedDict, total = False)
_GenerateContentParametersOrDict = Union[(_GenerateContentParameters, _GenerateContentParametersDict)]

class HttpResponse(_common.BaseModel):
    '''A wrapper class for the http response.'''
    headers: Optional[dict[(str, str)]] = Field(default = None, description = 'Used to retain the processed HTTP headers in the response.')
    body: Optional[str] = Field(default = None, description = 'The raw HTTP response body, in JSON format.')


def HttpResponseDict():
    '''HttpResponseDict'''
    body: Optional[str] = 'A wrapper class for the http response.'

HttpResponseDict = <NODE:27>(HttpResponseDict, 'HttpResponseDict', TypedDict, total = False)
HttpResponseOrDict = Union[(HttpResponse, HttpResponseDict)]

class GoogleTypeDate(_common.BaseModel):
    '''Represents a whole or partial calendar date, such as a birthday.

  The time of day and time zone are either specified elsewhere or are
  insignificant. The date is relative to the Gregorian Calendar. This can
  represent one of the following: * A full date, with non-zero year, month, and
  day values. * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day. * A year and month,
  with a zero day (for example, a credit card expiration date). Related types: *
  google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp. This
  data type is not supported in Gemini API.
  '''
    day: Optional[int] = Field(default = None, description = "Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.")
    month: Optional[int] = Field(default = None, description = 'Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.')
    year: Optional[int] = Field(default = None, description = 'Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.')


def GoogleTypeDateDict():
    '''GoogleTypeDateDict'''
    year: Optional[int] = 'Represents a whole or partial calendar date, such as a birthday.\n\n  The time of day and time zone are either specified elsewhere or are\n  insignificant. The date is relative to the Gregorian Calendar. This can\n  represent one of the following: * A full date, with non-zero year, month, and\n  day values. * A month and day, with a zero year (for example, an anniversary).\n  * A year on its own, with a zero month and a zero day. * A year and month,\n  with a zero day (for example, a credit card expiration date). Related types: *\n  google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp. This\n  data type is not supported in Gemini API.\n  '

GoogleTypeDateDict = <NODE:27>(GoogleTypeDateDict, 'GoogleTypeDateDict', TypedDict, total = False)
GoogleTypeDateOrDict = Union[(GoogleTypeDate, GoogleTypeDateDict)]

class Citation(_common.BaseModel):
    '''Source attributions for content.

  This data type is not supported in Gemini API.
  '''
    end_index: Optional[int] = Field(default = None, description = 'Output only. End index into the content.')
    license: Optional[str] = Field(default = None, description = 'Output only. License of the attribution.')
    publication_date: Optional[GoogleTypeDate] = Field(default = None, description = 'Output only. Publication date of the attribution.')
    start_index: Optional[int] = Field(default = None, description = 'Output only. Start index into the content.')
    title: Optional[str] = Field(default = None, description = 'Output only. Title of the attribution.')
    uri: Optional[str] = Field(default = None, description = 'Output only. Url reference of the attribution.')


def CitationDict():
    '''CitationDict'''
    uri: Optional[str] = 'Source attributions for content.\n\n  This data type is not supported in Gemini API.\n  '

CitationDict = <NODE:27>(CitationDict, 'CitationDict', TypedDict, total = False)
CitationOrDict = Union[(Citation, CitationDict)]

class CitationMetadata(_common.BaseModel):
    '''Citation information when the model quotes another source.'''
    citations: Optional[list[Citation]] = Field(default = None, description = 'Contains citation information when the model directly quotes, at\n      length, from another source. Can include traditional websites and code\n      repositories.\n      ')
    _rename_citation_sources = (lambda cls = None, data = model_validator(mode = 'before'): if isinstance(data, dict) and 'citationSources' in data:
data['citations'] = data.pop('citationSources')data)()()


def CitationMetadataDict():
    '''CitationMetadataDict'''
    citations: Optional[list[CitationDict]] = 'Citation information when the model quotes another source.'

CitationMetadataDict = <NODE:27>(CitationMetadataDict, 'CitationMetadataDict', TypedDict, total = False)
CitationMetadataOrDict = Union[(CitationMetadata, CitationMetadataDict)]

class GroundingChunkMapsPlaceAnswerSourcesAuthorAttribution(_common.BaseModel):
    '''Author attribution for a photo or review.

  This data type is not supported in Gemini API.
  '''
    display_name: Optional[str] = Field(default = None, description = 'Name of the author of the Photo or Review.')
    photo_uri: Optional[str] = Field(default = None, description = 'Profile photo URI of the author of the Photo or Review.')
    uri: Optional[str] = Field(default = None, description = 'URI of the author of the Photo or Review.')


def GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict():
    '''GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict'''
    uri: Optional[str] = 'Author attribution for a photo or review.\n\n  This data type is not supported in Gemini API.\n  '

GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict = <NODE:27>(GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict, 'GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict', TypedDict, total = False)
GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionOrDict = Union[(GroundingChunkMapsPlaceAnswerSourcesAuthorAttribution, GroundingChunkMapsPlaceAnswerSourcesAuthorAttributionDict)]

class GroundingChunkMapsPlaceAnswerSourcesReviewSnippet(_common.BaseModel):
    '''Encapsulates a review snippet.

  This data type is not supported in Gemini API.
  '''
    author_attribution: Optional[GroundingChunkMapsPlaceAnswerSourcesAuthorAttribution] = Field(default = None, description = "This review's author.")
    flag_content_uri: Optional[str] = Field(default = None, description = 'A link where users can flag a problem with the review.')
    google_maps_uri: Optional[str] = Field(default = None, description = 'A link to show the review on Google Maps.')
    relative_publish_time_description: Optional[str] = Field(default = None, description = 'A string of formatted recent time, expressing the review time relative to the current time in a form appropriate for the language and country.')
    review: Optional[str] = Field(default = None, description = 'A reference representing this place review which may be used to look up this place review again.')
    review_id: Optional[str] = Field(default = None, description = 'Id of the review referencing the place.')
    title: Optional[str] = Field(default = None, description = 'Title of the review.')


def GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict():
    '''GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict'''
    title: Optional[str] = 'Encapsulates a review snippet.\n\n  This data type is not supported in Gemini API.\n  '

GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict = <NODE:27>(GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict, 'GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict', TypedDict, total = False)
GroundingChunkMapsPlaceAnswerSourcesReviewSnippetOrDict = Union[(GroundingChunkMapsPlaceAnswerSourcesReviewSnippet, GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict)]

class GroundingChunkMapsPlaceAnswerSources(_common.BaseModel):
    '''Sources used to generate the place answer.

  This data type is not supported in Gemini API.
  '''
    flag_content_uri: Optional[str] = Field(default = None, description = 'A link where users can flag a problem with the generated answer.')
    review_snippets: Optional[list[GroundingChunkMapsPlaceAnswerSourcesReviewSnippet]] = Field(default = None, description = 'Snippets of reviews that are used to generate the answer.')


def GroundingChunkMapsPlaceAnswerSourcesDict():
    '''GroundingChunkMapsPlaceAnswerSourcesDict'''
    review_snippets: Optional[list[GroundingChunkMapsPlaceAnswerSourcesReviewSnippetDict]] = 'Sources used to generate the place answer.\n\n  This data type is not supported in Gemini API.\n  '

GroundingChunkMapsPlaceAnswerSourcesDict = <NODE:27>(GroundingChunkMapsPlaceAnswerSourcesDict, 'GroundingChunkMapsPlaceAnswerSourcesDict', TypedDict, total = False)
GroundingChunkMapsPlaceAnswerSourcesOrDict = Union[(GroundingChunkMapsPlaceAnswerSources, GroundingChunkMapsPlaceAnswerSourcesDict)]

class GroundingChunkMaps(_common.BaseModel):
    '''Chunk from Google Maps. This data type is not supported in Gemini API.'''
    place_answer_sources: Optional[GroundingChunkMapsPlaceAnswerSources] = Field(default = None, description = 'Sources used to generate the place answer. This includes review snippets and photos that were used to generate the answer, as well as uris to flag content.')
    place_id: Optional[str] = Field(default = None, description = "This Place's resource name, in `places/{place_id}` format. Can be used to look up the Place.")
    text: Optional[str] = Field(default = None, description = 'Text of the place answer.')
    title: Optional[str] = Field(default = None, description = 'Title of the place.')
    uri: Optional[str] = Field(default = None, description = 'URI reference of the place.')


def GroundingChunkMapsDict():
    '''GroundingChunkMapsDict'''
    uri: Optional[str] = 'Chunk from Google Maps. This data type is not supported in Gemini API.'

GroundingChunkMapsDict = <NODE:27>(GroundingChunkMapsDict, 'GroundingChunkMapsDict', TypedDict, total = False)
GroundingChunkMapsOrDict = Union[(GroundingChunkMaps, GroundingChunkMapsDict)]

class RagChunkPageSpan(_common.BaseModel):
    '''Represents where the chunk starts and ends in the document.

  This data type is not supported in Gemini API.
  '''
    first_page: Optional[int] = Field(default = None, description = 'Page where chunk starts in the document. Inclusive. 1-indexed.')
    last_page: Optional[int] = Field(default = None, description = 'Page where chunk ends in the document. Inclusive. 1-indexed.')


def RagChunkPageSpanDict():
    '''RagChunkPageSpanDict'''
    last_page: Optional[int] = 'Represents where the chunk starts and ends in the document.\n\n  This data type is not supported in Gemini API.\n  '

RagChunkPageSpanDict = <NODE:27>(RagChunkPageSpanDict, 'RagChunkPageSpanDict', TypedDict, total = False)
RagChunkPageSpanOrDict = Union[(RagChunkPageSpan, RagChunkPageSpanDict)]

class RagChunk(_common.BaseModel):
    '''A RagChunk includes the content of a chunk of a RagFile, and associated metadata.

  This data type is not supported in Gemini API.
  '''
    page_span: Optional[RagChunkPageSpan] = Field(default = None, description = 'If populated, represents where the chunk starts and ends in the document.')
    text: Optional[str] = Field(default = None, description = 'The content of the chunk.')


def RagChunkDict():
    '''RagChunkDict'''
    text: Optional[str] = 'A RagChunk includes the content of a chunk of a RagFile, and associated metadata.\n\n  This data type is not supported in Gemini API.\n  '

RagChunkDict = <NODE:27>(RagChunkDict, 'RagChunkDict', TypedDict, total = False)
RagChunkOrDict = Union[(RagChunk, RagChunkDict)]

class GroundingChunkRetrievedContext(_common.BaseModel):
    '''Chunk from context retrieved by the retrieval tools.

  This data type is not supported in Gemini API.
  '''
    document_name: Optional[str] = Field(default = None, description = 'Output only. The full document name for the referenced Vertex AI Search document.')
    rag_chunk: Optional[RagChunk] = Field(default = None, description = 'Additional context for the RAG retrieval result. This is only populated when using the RAG retrieval tool.')
    text: Optional[str] = Field(default = None, description = 'Text of the attribution.')
    title: Optional[str] = Field(default = None, description = 'Title of the attribution.')
    uri: Optional[str] = Field(default = None, description = 'URI reference of the attribution.')


def GroundingChunkRetrievedContextDict():
    '''GroundingChunkRetrievedContextDict'''
    uri: Optional[str] = 'Chunk from context retrieved by the retrieval tools.\n\n  This data type is not supported in Gemini API.\n  '

GroundingChunkRetrievedContextDict = <NODE:27>(GroundingChunkRetrievedContextDict, 'GroundingChunkRetrievedContextDict', TypedDict, total = False)
GroundingChunkRetrievedContextOrDict = Union[(GroundingChunkRetrievedContext, GroundingChunkRetrievedContextDict)]

class GroundingChunkWeb(_common.BaseModel):
    '''Chunk from the web.'''
    domain: Optional[str] = Field(default = None, description = 'Domain of the (original) URI. This field is not supported in Gemini API.')
    title: Optional[str] = Field(default = None, description = 'Title of the chunk.')
    uri: Optional[str] = Field(default = None, description = 'URI reference of the chunk.')


def GroundingChunkWebDict():
    '''GroundingChunkWebDict'''
    uri: Optional[str] = 'Chunk from the web.'

GroundingChunkWebDict = <NODE:27>(GroundingChunkWebDict, 'GroundingChunkWebDict', TypedDict, total = False)
GroundingChunkWebOrDict = Union[(GroundingChunkWeb, GroundingChunkWebDict)]

class GroundingChunk(_common.BaseModel):
    '''Grounding chunk.'''
    maps: Optional[GroundingChunkMaps] = Field(default = None, description = 'Grounding chunk from Google Maps. This field is not supported in Gemini API.')
    retrieved_context: Optional[GroundingChunkRetrievedContext] = Field(default = None, description = 'Grounding chunk from context retrieved by the retrieval tools. This field is not supported in Gemini API.')
    web: Optional[GroundingChunkWeb] = Field(default = None, description = 'Grounding chunk from the web.')


def GroundingChunkDict():
    '''GroundingChunkDict'''
    web: Optional[GroundingChunkWebDict] = 'Grounding chunk.'

GroundingChunkDict = <NODE:27>(GroundingChunkDict, 'GroundingChunkDict', TypedDict, total = False)
GroundingChunkOrDict = Union[(GroundingChunk, GroundingChunkDict)]

class Segment(_common.BaseModel):
    '''Segment of the content.'''
    end_index: Optional[int] = Field(default = None, description = 'Output only. End index in the given Part, measured in bytes. Offset from the start of the Part, exclusive, starting at zero.')
    part_index: Optional[int] = Field(default = None, description = 'Output only. The index of a Part object within its parent Content object.')
    start_index: Optional[int] = Field(default = None, description = 'Output only. Start index in the given Part, measured in bytes. Offset from the start of the Part, inclusive, starting at zero.')
    text: Optional[str] = Field(default = None, description = 'Output only. The text corresponding to the segment from the response.')


def SegmentDict():
    '''SegmentDict'''
    text: Optional[str] = 'Segment of the content.'

SegmentDict = <NODE:27>(SegmentDict, 'SegmentDict', TypedDict, total = False)
SegmentOrDict = Union[(Segment, SegmentDict)]

class GroundingSupport(_common.BaseModel):
    '''Grounding support.'''
    confidence_scores: Optional[list[float]] = Field(default = None, description = 'Confidence score of the support references. Ranges from 0 to 1. 1 is the most confident. For Gemini 2.0 and before, this list must have the same size as the grounding_chunk_indices. For Gemini 2.5 and after, this list will be empty and should be ignored.')
    grounding_chunk_indices: Optional[list[int]] = Field(default = None, description = "A list of indices (into 'grounding_chunk') specifying the citations associated with the claim. For instance [1,3,4] means that grounding_chunk[1], grounding_chunk[3], grounding_chunk[4] are the retrieved content attributed to the claim.")
    segment: Optional[Segment] = Field(default = None, description = 'Segment of the content this support belongs to.')


def GroundingSupportDict():
    '''GroundingSupportDict'''
    segment: Optional[SegmentDict] = 'Grounding support.'

GroundingSupportDict = <NODE:27>(GroundingSupportDict, 'GroundingSupportDict', TypedDict, total = False)
GroundingSupportOrDict = Union[(GroundingSupport, GroundingSupportDict)]

class RetrievalMetadata(_common.BaseModel):
    '''Metadata related to retrieval in the grounding flow.'''
    google_search_dynamic_retrieval_score: Optional[float] = Field(default = None, description = 'Optional. Score indicating how likely information from Google Search could help answer the prompt. The score is in the range `[0, 1]`, where 0 is the least likely and 1 is the most likely. This score is only populated when Google Search grounding and dynamic retrieval is enabled. It will be compared to the threshold to determine whether to trigger Google Search.')


def RetrievalMetadataDict():
    '''RetrievalMetadataDict'''
    google_search_dynamic_retrieval_score: Optional[float] = 'Metadata related to retrieval in the grounding flow.'

RetrievalMetadataDict = <NODE:27>(RetrievalMetadataDict, 'RetrievalMetadataDict', TypedDict, total = False)
RetrievalMetadataOrDict = Union[(RetrievalMetadata, RetrievalMetadataDict)]

class SearchEntryPoint(_common.BaseModel):
    '''Google search entry point.'''
    rendered_content: Optional[str] = Field(default = None, description = 'Optional. Web content snippet that can be embedded in a web page or an app webview.')
    sdk_blob: Optional[bytes] = Field(default = None, description = 'Optional. Base64 encoded JSON representing array of tuple.')


def SearchEntryPointDict():
    '''SearchEntryPointDict'''
    sdk_blob: Optional[bytes] = 'Google search entry point.'

SearchEntryPointDict = <NODE:27>(SearchEntryPointDict, 'SearchEntryPointDict', TypedDict, total = False)
SearchEntryPointOrDict = Union[(SearchEntryPoint, SearchEntryPointDict)]

class GroundingMetadataSourceFlaggingUri(_common.BaseModel):
    '''Source content flagging uri for a place or review.

  This is currently populated only for Google Maps grounding. This data type is
  not supported in Gemini API.
  '''
    flag_content_uri: Optional[str] = Field(default = None, description = 'A link where users can flag a problem with the source (place or review).')
    source_id: Optional[str] = Field(default = None, description = 'Id of the place or review.')


def GroundingMetadataSourceFlaggingUriDict():
    '''GroundingMetadataSourceFlaggingUriDict'''
    source_id: Optional[str] = 'Source content flagging uri for a place or review.\n\n  This is currently populated only for Google Maps grounding. This data type is\n  not supported in Gemini API.\n  '

GroundingMetadataSourceFlaggingUriDict = <NODE:27>(GroundingMetadataSourceFlaggingUriDict, 'GroundingMetadataSourceFlaggingUriDict', TypedDict, total = False)
GroundingMetadataSourceFlaggingUriOrDict = Union[(GroundingMetadataSourceFlaggingUri, GroundingMetadataSourceFlaggingUriDict)]

class GroundingMetadata(_common.BaseModel):
    '''Metadata returned to client when grounding is enabled.'''
    google_maps_widget_context_token: Optional[str] = Field(default = None, description = 'Optional. Output only. Resource name of the Google Maps widget context token to be used with the PlacesContextElement widget to render contextual data. This is populated only for Google Maps grounding. This field is not supported in Gemini API.')
    grounding_chunks: Optional[list[GroundingChunk]] = Field(default = None, description = 'List of supporting references retrieved from specified grounding source.')
    grounding_supports: Optional[list[GroundingSupport]] = Field(default = None, description = 'Optional. List of grounding support.')
    retrieval_metadata: Optional[RetrievalMetadata] = Field(default = None, description = 'Optional. Output only. Retrieval metadata.')
    retrieval_queries: Optional[list[str]] = Field(default = None, description = 'Optional. Queries executed by the retrieval tools. This field is not supported in Gemini API.')
    search_entry_point: Optional[SearchEntryPoint] = Field(default = None, description = 'Optional. Google search entry for the following-up web searches.')
    source_flagging_uris: Optional[list[GroundingMetadataSourceFlaggingUri]] = Field(default = None, description = 'Optional. Output only. List of source flagging uris. This is currently populated only for Google Maps grounding. This field is not supported in Gemini API.')
    web_search_queries: Optional[list[str]] = Field(default = None, description = 'Optional. Web search queries for the following-up web search.')


def GroundingMetadataDict():
    '''GroundingMetadataDict'''
    web_search_queries: Optional[list[str]] = 'Metadata returned to client when grounding is enabled.'

GroundingMetadataDict = <NODE:27>(GroundingMetadataDict, 'GroundingMetadataDict', TypedDict, total = False)
GroundingMetadataOrDict = Union[(GroundingMetadata, GroundingMetadataDict)]

class LogprobsResultCandidate(_common.BaseModel):
    '''Candidate for the logprobs token and score.'''
    log_probability: Optional[float] = Field(default = None, description = "The candidate's log probability.")
    token: Optional[str] = Field(default = None, description = "The candidate's token string value.")
    token_id: Optional[int] = Field(default = None, description = "The candidate's token id value.")


def LogprobsResultCandidateDict():
    '''LogprobsResultCandidateDict'''
    token_id: Optional[int] = 'Candidate for the logprobs token and score.'

LogprobsResultCandidateDict = <NODE:27>(LogprobsResultCandidateDict, 'LogprobsResultCandidateDict', TypedDict, total = False)
LogprobsResultCandidateOrDict = Union[(LogprobsResultCandidate, LogprobsResultCandidateDict)]

class LogprobsResultTopCandidates(_common.BaseModel):
    '''Candidates with top log probabilities at each decoding step.'''
    candidates: Optional[list[LogprobsResultCandidate]] = Field(default = None, description = 'Sorted by log probability in descending order.')


def LogprobsResultTopCandidatesDict():
    '''LogprobsResultTopCandidatesDict'''
    candidates: Optional[list[LogprobsResultCandidateDict]] = 'Candidates with top log probabilities at each decoding step.'

LogprobsResultTopCandidatesDict = <NODE:27>(LogprobsResultTopCandidatesDict, 'LogprobsResultTopCandidatesDict', TypedDict, total = False)
LogprobsResultTopCandidatesOrDict = Union[(LogprobsResultTopCandidates, LogprobsResultTopCandidatesDict)]

class LogprobsResult(_common.BaseModel):
    '''Logprobs Result'''
    chosen_candidates: Optional[list[LogprobsResultCandidate]] = Field(default = None, description = 'Length = total number of decoding steps. The chosen candidates may or may not be in top_candidates.')
    top_candidates: Optional[list[LogprobsResultTopCandidates]] = Field(default = None, description = 'Length = total number of decoding steps.')


def LogprobsResultDict():
    '''LogprobsResultDict'''
    top_candidates: Optional[list[LogprobsResultTopCandidatesDict]] = 'Logprobs Result'

LogprobsResultDict = <NODE:27>(LogprobsResultDict, 'LogprobsResultDict', TypedDict, total = False)
LogprobsResultOrDict = Union[(LogprobsResult, LogprobsResultDict)]

class SafetyRating(_common.BaseModel):
    '''Safety rating corresponding to the generated content.'''
    blocked: Optional[bool] = Field(default = None, description = 'Output only. Indicates whether the content was filtered out because of this rating.')
    category: Optional[HarmCategory] = Field(default = None, description = 'Output only. Harm category.')
    overwritten_threshold: Optional[HarmBlockThreshold] = Field(default = None, description = 'Output only. The overwritten threshold for the safety category of Gemini 2.0 image out. If minors are detected in the output image, the threshold of each safety category will be overwritten if user sets a lower threshold. This field is not supported in Gemini API.')
    probability: Optional[HarmProbability] = Field(default = None, description = 'Output only. Harm probability levels in the content.')
    probability_score: Optional[float] = Field(default = None, description = 'Output only. Harm probability score. This field is not supported in Gemini API.')
    severity: Optional[HarmSeverity] = Field(default = None, description = 'Output only. Harm severity levels in the content. This field is not supported in Gemini API.')
    severity_score: Optional[float] = Field(default = None, description = 'Output only. Harm severity score. This field is not supported in Gemini API.')


def SafetyRatingDict():
    '''SafetyRatingDict'''
    severity_score: Optional[float] = 'Safety rating corresponding to the generated content.'

SafetyRatingDict = <NODE:27>(SafetyRatingDict, 'SafetyRatingDict', TypedDict, total = False)
SafetyRatingOrDict = Union[(SafetyRating, SafetyRatingDict)]

class UrlMetadata(_common.BaseModel):
    '''Context of the a single url retrieval.'''
    retrieved_url: Optional[str] = Field(default = None, description = 'Retrieved url by the tool.')
    url_retrieval_status: Optional[UrlRetrievalStatus] = Field(default = None, description = 'Status of the url retrieval.')


def UrlMetadataDict():
    '''UrlMetadataDict'''
    url_retrieval_status: Optional[UrlRetrievalStatus] = 'Context of the a single url retrieval.'

UrlMetadataDict = <NODE:27>(UrlMetadataDict, 'UrlMetadataDict', TypedDict, total = False)
UrlMetadataOrDict = Union[(UrlMetadata, UrlMetadataDict)]

class UrlContextMetadata(_common.BaseModel):
    '''Metadata related to url context retrieval tool.'''
    url_metadata: Optional[list[UrlMetadata]] = Field(default = None, description = 'Output only. List of url context.')


def UrlContextMetadataDict():
    '''UrlContextMetadataDict'''
    url_metadata: Optional[list[UrlMetadataDict]] = 'Metadata related to url context retrieval tool.'

UrlContextMetadataDict = <NODE:27>(UrlContextMetadataDict, 'UrlContextMetadataDict', TypedDict, total = False)
UrlContextMetadataOrDict = Union[(UrlContextMetadata, UrlContextMetadataDict)]

class Candidate(_common.BaseModel):
    '''A response candidate generated from the model.'''
    content: Optional[Content] = Field(default = None, description = 'Contains the multi-part content of the response.\n      ')
    citation_metadata: Optional[CitationMetadata] = Field(default = None, description = 'Source attribution of the generated content.\n      ')
    finish_message: Optional[str] = Field(default = None, description = 'Describes the reason the model stopped generating tokens.\n      ')
    token_count: Optional[int] = Field(default = None, description = 'Number of tokens for this candidate.\n      ')
    finish_reason: Optional[FinishReason] = Field(default = None, description = 'The reason why the model stopped generating tokens.\n      If empty, the model has not stopped generating the tokens.\n      ')
    avg_logprobs: Optional[float] = Field(default = None, description = 'Output only. Average log probability score of the candidate.')
    grounding_metadata: Optional[GroundingMetadata] = Field(default = None, description = 'Output only. Metadata specifies sources used to ground generated content.')
    index: Optional[int] = Field(default = None, description = 'Output only. Index of the candidate.')
    logprobs_result: Optional[LogprobsResult] = Field(default = None, description = 'Output only. Log-likelihood scores for the response tokens and top tokens')
    safety_ratings: Optional[list[SafetyRating]] = Field(default = None, description = 'Output only. List of ratings for the safety of a response candidate. There is at most one rating per category.')
    url_context_metadata: Optional[UrlContextMetadata] = Field(default = None, description = 'Output only. Metadata related to url context retrieval tool.')


def CandidateDict():
    '''CandidateDict'''
    url_context_metadata: Optional[UrlContextMetadataDict] = 'A response candidate generated from the model.'

CandidateDict = <NODE:27>(CandidateDict, 'CandidateDict', TypedDict, total = False)
CandidateOrDict = Union[(Candidate, CandidateDict)]

class GenerateContentResponsePromptFeedback(_common.BaseModel):
    '''Content filter results for a prompt sent in the request.

  Note: This is sent only in the first stream chunk and only if no candidates
  were generated due to content violations.
  '''
    block_reason: Optional[BlockedReason] = Field(default = None, description = 'Output only. The reason why the prompt was blocked.')
    block_reason_message: Optional[str] = Field(default = None, description = 'Output only. A readable message that explains the reason why the prompt was blocked. This field is not supported in Gemini API.')
    safety_ratings: Optional[list[SafetyRating]] = Field(default = None, description = 'Output only. A list of safety ratings for the prompt. There is one rating per category.')


def GenerateContentResponsePromptFeedbackDict():
    '''GenerateContentResponsePromptFeedbackDict'''
    safety_ratings: Optional[list[SafetyRatingDict]] = 'Content filter results for a prompt sent in the request.\n\n  Note: This is sent only in the first stream chunk and only if no candidates\n  were generated due to content violations.\n  '

GenerateContentResponsePromptFeedbackDict = <NODE:27>(GenerateContentResponsePromptFeedbackDict, 'GenerateContentResponsePromptFeedbackDict', TypedDict, total = False)
GenerateContentResponsePromptFeedbackOrDict = Union[(GenerateContentResponsePromptFeedback, GenerateContentResponsePromptFeedbackDict)]

class ModalityTokenCount(_common.BaseModel):
    '''Represents token counting info for a single modality.'''
    modality: Optional[MediaModality] = Field(default = None, description = 'The modality associated with this token count.')
    token_count: Optional[int] = Field(default = None, description = 'Number of tokens.')


def ModalityTokenCountDict():
    '''ModalityTokenCountDict'''
    token_count: Optional[int] = 'Represents token counting info for a single modality.'

ModalityTokenCountDict = <NODE:27>(ModalityTokenCountDict, 'ModalityTokenCountDict', TypedDict, total = False)
ModalityTokenCountOrDict = Union[(ModalityTokenCount, ModalityTokenCountDict)]

class GenerateContentResponseUsageMetadata(_common.BaseModel):
    '''Usage metadata about the content generation request and response.

  This message provides a detailed breakdown of token usage and other relevant
  metrics. This data type is not supported in Gemini API.
  '''
    cache_tokens_details: Optional[list[ModalityTokenCount]] = Field(default = None, description = 'Output only. A detailed breakdown of the token count for each modality in the cached content.')
    cached_content_token_count: Optional[int] = Field(default = None, description = 'Output only. The number of tokens in the cached content that was used for this request.')
    candidates_token_count: Optional[int] = Field(default = None, description = 'The total number of tokens in the generated candidates.')
    candidates_tokens_details: Optional[list[ModalityTokenCount]] = Field(default = None, description = 'Output only. A detailed breakdown of the token count for each modality in the generated candidates.')
    prompt_token_count: Optional[int] = Field(default = None, description = 'The total number of tokens in the prompt. This includes any text, images, or other media provided in the request. When `cached_content` is set, this also includes the number of tokens in the cached content.')
    prompt_tokens_details: Optional[list[ModalityTokenCount]] = Field(default = None, description = 'Output only. A detailed breakdown of the token count for each modality in the prompt.')
    thoughts_token_count: Optional[int] = Field(default = None, description = 'Output only. The number of tokens that were part of the model\'s generated "thoughts" output, if applicable.')
    tool_use_prompt_token_count: Optional[int] = Field(default = None, description = 'Output only. The number of tokens in the results from tool executions, which are provided back to the model as input, if applicable.')
    tool_use_prompt_tokens_details: Optional[list[ModalityTokenCount]] = Field(default = None, description = 'Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.')
    total_token_count: Optional[int] = Field(default = None, description = 'The total number of tokens for the entire request. This is the sum of `prompt_token_count`, `candidates_token_count`, `tool_use_prompt_token_count`, and `thoughts_token_count`.')
    traffic_type: Optional[TrafficType] = Field(default = None, description = 'Output only. The traffic type for this request.')


def GenerateContentResponseUsageMetadataDict():
    '''GenerateContentResponseUsageMetadataDict'''
    traffic_type: Optional[TrafficType] = 'Usage metadata about the content generation request and response.\n\n  This message provides a detailed breakdown of token usage and other relevant\n  metrics. This data type is not supported in Gemini API.\n  '

GenerateContentResponseUsageMetadataDict = <NODE:27>(GenerateContentResponseUsageMetadataDict, 'GenerateContentResponseUsageMetadataDict', TypedDict, total = False)
GenerateContentResponseUsageMetadataOrDict = Union[(GenerateContentResponseUsageMetadata, GenerateContentResponseUsageMetadataDict)]

class GenerateContentResponse(_common.BaseModel):
    pass
# WARNING: Decompyle incomplete


def GenerateContentResponseDict():
    '''GenerateContentResponseDict'''
    usage_metadata: Optional[GenerateContentResponseUsageMetadataDict] = 'Response message for PredictionService.GenerateContent.'

GenerateContentResponseDict = <NODE:27>(GenerateContentResponseDict, 'GenerateContentResponseDict', TypedDict, total = False)
GenerateContentResponseOrDict = Union[(GenerateContentResponse, GenerateContentResponseDict)]

class EmbedContentConfig(_common.BaseModel):
    '''Optional parameters for the embed_content method.'''
    http_options: Optional[HttpOptions] = Field(default = None, description = 'Used to override HTTP request options.')
    task_type: Optional[str] = Field(default = None, description = 'Type of task for which the embedding will be used.\n      ')
    title: Optional[str] = Field(default = None, description = 'Title for the text. Only applicable when TaskType is\n      `RETRIEVAL_DOCUMENT`.\n      ')
    output_dimensionality: Optional[int] = Field(default = None, description = 'Reduced dimension for the output embedding. If set,\n      excessive values in the output embedding are truncated from the end.\n      Supported by newer models since 2024 only. You cannot set this value if\n      using the earlier model (`models/embedding-001`).\n      ')
    mime_type: Optional[str] = Field(default = None, description = 'Vertex API only. The MIME type of the input.\n      ')
    auto_truncate: Optional[bool] = Field(default = None, description = 'Vertex API only. Whether to silently truncate inputs longer than\n      the max sequence length. If this option is set to false, oversized inputs\n      will lead to an INVALID_ARGUMENT error, similar to other text APIs.\n      ')


def EmbedContentConfigDict():
    '''EmbedContentConfigDict'''
    auto_truncate: Optional[bool] = 'Optional parameters for the embed_content method.'

EmbedContentConfigDict = <NODE:27>(EmbedContentConfigDict, 'EmbedContentConfigDict', TypedDict, total = False)
EmbedContentConfigOrDict = Union[(EmbedContentConfig, EmbedContentConfigDict)]

class _EmbedContentParameters(_common.BaseModel):
    '''Parameters for the embed_content method.'''
    model: Optional[str] = Field(default = None, description = 'ID of the model to use. For a list of models, see `Google models\n    <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models>`_.')
    contents: Optional[ContentListUnion] = Field(default = None, description = 'The content to embed. Only the `parts.text` fields will be counted.\n      ')
    config: Optional[EmbedContentConfig] = Field(default = None, description = 'Configuration that contains optional parameters.\n      ')


def _EmbedContentParametersDict():
    '''_EmbedContentParametersDict'''
    config: Optional[EmbedContentConfigDict] = 'Parameters for the embed_content method.'

_EmbedContentParametersDict = <NODE:27>(_EmbedContentParametersDict, '_EmbedContentParametersDict', TypedDict, total = False)
_EmbedContentParametersOrDict = Union[(_EmbedContentParameters, _EmbedContentParametersDict)]

class ContentEmbeddingStatistics(_common.BaseModel):
    '''Statistics of the input text associated with the result of content embedding.'''
    truncated: Optional[bool] = Field(default = None, description = 'Vertex API only. If the input text was truncated due to having\n      a length longer than the allowed maximum input.\n      ')
    token_count: Optional[float] = Field(default = None, description = 'Vertex API only. Number of tokens of the input text.\n      ')


def ContentEmbeddingStatisticsDict():
    '''ContentEmbeddingStatisticsDict'''
    token_count: Optional[float] = 'Statistics of the input text associated with the result of content embedding.'

ContentEmbeddingStatisticsDict = <NODE:27>(ContentEmbeddingStatisticsDict, 'ContentEmbeddingStatisticsDict', TypedDict, total = False)
ContentEmbeddingStatisticsOrDict = Union[(ContentEmbeddingStatistics, ContentEmbeddingStatisticsDict)]

class ContentEmbedding(_common.BaseModel):
    '''The embedding generated from an input content.'''
    values: Optional[list[float]] = Field(default = None, description = 'A list of floats representing an embedding.\n      ')
    statistics: Optional[ContentEmbeddingStatistics] = Field(default = None, description = 'Vertex API only. Statistics of the input text associated with this\n      embedding.\n      ')


def ContentEmbeddingDict():
    '''ContentEmbeddingDict'''
    statistics: Optional[ContentEmbeddingStatisticsDict] = 'The embedding generated from an input content.'

ContentEmbeddingDict = <NODE:27>(ContentEmbeddingDict, 'ContentEmbeddingDict', TypedDict, total = False)
ContentEmbeddingOrDict = Union[(ContentEmbedding, ContentEmbeddingDict)]

class EmbedContentMetadata(_common.BaseModel):
    '''Request-level metadata for the Vertex Embed Content API.'''
    billable_character_count: Optional[int] = Field(default = None, description = 'Vertex API only. The total number of billable characters included\n      in the request.\n      ')


def EmbedContentMetadataDict():
    '''EmbedContentMetadataDict'''
    billable_character_count: Optional[int] = 'Request-level metadata for the Vertex Embed Content API.'

EmbedContentMetadataDict = <NODE:27>(EmbedContentMetadataDict, 'EmbedContentMetadataDict', TypedDict, total = False)
EmbedContentMetadataOrDict = Union[(EmbedContentMetadata, EmbedContentMetadataDict)]

class EmbedContentResponse(_common.BaseModel):
    '''Response for the embed_content method.'''
    sdk_http_response: Optional[HttpResponse] = Field(default = None, description = 'Used to retain the full HTTP response.')
    embeddings: Optional[list[ContentEmbedding]] = Field(default = None, description = 'The embeddings for each request, in the same order as provided in\n      the batch request.\n      ')
    metadata: Optional[EmbedContentMetadata] = Field(default = None, description = 'Vertex API only. Metadata about the request.\n      ')


def EmbedContentResponseDict():
    '''EmbedContentResponseDict'''
    metadata: Optional[EmbedContentMetadataDict] = 'Response for the embed_content method.'

EmbedContentResponseDict = <NODE:27>(EmbedContentResponseDict, 'EmbedContentResponseDict', TypedDict, total = False)
EmbedContentResponseOrDict = Union[(EmbedContentResponse, EmbedContentResponseDict)]

class GenerateImagesConfig(_common.BaseModel):
    '''The config for generating an images.'''
    http_options: Optional[HttpOptions] = Field(default = None, description = 'Used to override HTTP request options.')
    output_gcs_uri: Optional[str] = Field(default = None, description = 'Cloud Storage URI used to store the generated images.')
    negative_prompt: Optional[str] = Field(default = None, description = 'Description of what to discourage in the generated images.')
    number_of_images: Optional[int] = Field(default = None, description = 'Number of images to generate.')
    aspect_ratio: Optional[str] = Field(default = None, description = 'Aspect ratio of the generated images. Supported values are\n      "1:1", "3:4", "4:3", "9:16", and "16:9".')
    guidance_scale: Optional[float] = Field(default = None, description = 'Controls how much the model adheres to the text prompt. Large\n      values increase output and prompt alignment, but may compromise image\n      quality.')
    seed: Optional[int] = Field(default = None, description = 'Random seed for image generation. This is not available when\n      ``add_watermark`` is set to true.')
    safety_filter_level: Optional[SafetyFilterLevel] = Field(default = None, description = 'Filter level for safety filtering.')
    person_generation: Optional[PersonGeneration] = Field(default = None, description = 'Allows generation of people by the model.')
    include_safety_attributes: Optional[bool] = Field(default = None, description = 'Whether to report the safety scores of each generated image and\n      the positive prompt in the response.')
    include_rai_reason: Optional[bool] = Field(default = None, description = 'Whether to include the Responsible AI filter reason if the image\n      is filtered out of the response.')
    language: Optional[ImagePromptLanguage] = Field(default = None, description = 'Language of the text in the prompt.')
    output_mime_type: Optional[str] = Field(default = None, description = 'MIME type of the generated image.')
    output_compression_quality: Optional[int] = Field(default = None, description = 'Compression quality of the generated image (for ``image/jpeg``\n      only).')
    add_watermark: Optional[bool] = Field(default = None, description = 'Whether to add a watermark to the generated images.')
    labels: Optional[dict[(str, str)]] = Field(default = None, description = 'User specified labels to track billing usage.')
    image_size: Optional[str] = Field(default = None, description = 'The size of the largest dimension of the generated image.\n      Supported sizes are 1K and 2K (not supported for Imagen 3 models).')
    enhance_prompt: Optional[bool] = Field(default = None, description = 'Whether to use the prompt rewriting logic.')


def GenerateImagesConfigDict():
    '''GenerateImagesConfigDict'''
    enhance_prompt: Optional[bool] = 'The config for generating an images.'

GenerateImagesConfigDict = <NODE:27>(GenerateImagesConfigDict, 'GenerateImagesConfigDict', TypedDict, total = False)
GenerateImagesConfigOrDict = Union[(GenerateImagesConfig, GenerateImagesConfigDict)]

class _GenerateImagesParameters(_common.BaseModel):
    '''The parameters for generating images.'''
    model: Optional[str] = Field(default = None, description = 'ID of the model to use. For a list of models, see `Google models\n    <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models>`_.')
    prompt: Optional[str] = Field(default = None, description = 'Text prompt that typically describes the images to output.\n      ')
    config: Optional[GenerateImagesConfig] = Field(default = None, description = 'Configuration for generating images.\n      ')


def _GenerateImagesParametersDict():
    '''_GenerateImagesParametersDict'''
    config: Optional[GenerateImagesConfigDict] = 'The parameters for generating images.'

_GenerateImagesParametersDict = <NODE:27>(_GenerateImagesParametersDict, '_GenerateImagesParametersDict', TypedDict, total = False)
_GenerateImagesParametersOrDict = Union[(_GenerateImagesParameters, _GenerateImagesParametersDict)]

class Image(_common.BaseModel):
    '''An image.'''
    gcs_uri: Optional[str] = Field(default = None, description = 'The Cloud Storage URI of the image. ``Image`` can contain a value\n      for this field or the ``image_bytes`` field but not both.')
    image_bytes: Optional[bytes] = Field(default = None, description = 'The image bytes data. ``Image`` can contain a value for this field\n      or the ``gcs_uri`` field but not both.')
    mime_type: Optional[str] = Field(default = None, description = 'The MIME type of the image.')
    _loaded_image: Optional['PIL_Image'] = None
    from_file = (lambda cls = None, *, location: import urllibimport pathlibimport mimetypesparsed_url = urllib.parse.urlparse(location)if parsed_url.scheme == 'https' and parsed_url.netloc == 'storage.googleapis.com':
parsed_url = parsed_url._replace(scheme = 'gs', netloc = '', path = f'''/{urllib.parse.unquote(parsed_url.path)}''')location = urllib.parse.urlunparse(parsed_url)if parsed_url.scheme == 'gs':
cls(gcs_uri = location)image_bytes = None.Path(location).read_bytes()if not mime_type:
(mime_type, _) = mimetypes.guess_type(location)image = cls(image_bytes = image_bytes, mime_type = mime_type)image)()
    
    def show(self = None):
        '''Shows the image.

    This method only works in a notebook environment.
    '''
        in_notebook = 'ipykernel' in sys.modules
        if in_notebook:
            
            try:
                IPython_display = display
                import IPython
            except ImportError:
                IPython_display = None

            if IPython_display:
                IPython_display.display(self._pil_image)
                return None
            return None
        img = self._pil_image
    # WARNING: Decompyle incomplete

    _pil_image = (lambda self = None: try:
PIL_Image = Imageimport PILexcept ImportError:
PIL_Image = Noneimport io# WARNING: Decompyle incomplete
)()
    
    def save(self = None, location = None):
        '''Saves the image to a file.

    Args:
        location: Local path where to save the image.
    '''
        import pathlib
    # WARNING: Decompyle incomplete


JOB_STATES_SUCCEEDED_VERTEX = [
    'JOB_STATE_SUCCEEDED']
JOB_STATES_SUCCEEDED_MLDEV = [
    'ACTIVE']
JOB_STATES_SUCCEEDED = JOB_STATES_SUCCEEDED_VERTEX + JOB_STATES_SUCCEEDED_MLDEV
JOB_STATES_ENDED_VERTEX = [
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED']
JOB_STATES_ENDED_MLDEV = [
    'ACTIVE',
    'FAILED']
JOB_STATES_ENDED = JOB_STATES_ENDED_VERTEX + JOB_STATES_ENDED_MLDEV

def ImageDict():
    '''ImageDict'''
    mime_type: Optional[str] = 'An image.'

ImageDict = <NODE:27>(ImageDict, 'ImageDict', TypedDict, total = False)
ImageOrDict = Union[(Image, ImageDict)]

class SafetyAttributes(_common.BaseModel):
    '''Safety attributes of a GeneratedImage or the user-provided prompt.'''
    categories: Optional[list[str]] = Field(default = None, description = 'List of RAI categories.')
    scores: Optional[list[float]] = Field(default = None, description = 'List of scores of each categories.')
    content_type: Optional[str] = Field(default = None, description = 'Internal use only.')


def SafetyAttributesDict():
    '''SafetyAttributesDict'''
    content_type: Optional[str] = 'Safety attributes of a GeneratedImage or the user-provided prompt.'

SafetyAttributesDict = <NODE:27>(SafetyAttributesDict, 'SafetyAttributesDict', TypedDict, total = False)
SafetyAttributesOrDict = Union[(SafetyAttributes, SafetyAttributesDict)]

class GeneratedImage(_common.BaseModel):
    '''An output image.'''
    image: Optional[Image] = Field(default = None, description = 'The output image data.')
    rai_filtered_reason: Optional[str] = Field(default = None, description = 'Responsible AI filter reason if the image is filtered out of the\n      response.')
    safety_attributes: Optional[SafetyAttributes] = Field(default = None, description = 'Safety attributes of the image. Lists of RAI categories and their\n      scores of each content.')
    enhanced_prompt: Optional[str] = Field(default = None, description = 'The rewritten prompt used for the image generation if the prompt\n      enhancer is enabled.')


def GeneratedImageDict():
    '''GeneratedImageDict'''
    enhanced_prompt: Optional[str] = 'An output image.'

GeneratedImageDict = <NODE:27>(GeneratedImageDict, 'GeneratedImageDict', TypedDict, total = False)
GeneratedImageOrDict = Union[(GeneratedImage, GeneratedImageDict)]

class GenerateImagesResponse(_common.BaseModel):
    '''The output images response.'''
    sdk_http_response: Optional[HttpResponse] = Field(default = None, description = 'Used to retain the full HTTP response.')
    generated_images: Optional[list[GeneratedImage]] = Field(default = None, description = 'List of generated images.')
    positive_prompt_safety_attributes: Optional[SafetyAttributes] = Field(default = None, description = 'Safety attributes of the positive prompt. Only populated if\n      ``include_safety_attributes`` is set to True.')
    images = (lambda self = None:
