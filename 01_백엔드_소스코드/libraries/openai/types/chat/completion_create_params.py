# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared.chat_model import ChatModel
from shared_params.metadata import Metadata
from shared.reasoning_effort import ReasoningEffort
from chat_completion_audio_param import ChatCompletionAudioParam
from chat_completion_message_param import ChatCompletionMessageParam
from chat_completion_tool_union_param import ChatCompletionToolUnionParam
from shared_params.function_parameters import FunctionParameters
from shared_params.response_format_text import ResponseFormatText
from chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam
from shared_params.response_format_json_object import ResponseFormatJSONObject
from shared_params.response_format_json_schema import ResponseFormatJSONSchema
from chat_completion_function_call_option_param import ChatCompletionFunctionCallOptionParam
__all__ = [
    'CompletionCreateParamsBase',
    'FunctionCall',
    'Function',
    'ResponseFormat',
    'WebSearchOptions',
    'WebSearchOptionsUserLocation',
    'WebSearchOptionsUserLocationApproximate',
    'CompletionCreateParamsNonStreaming',
    'CompletionCreateParamsStreaming']

def CompletionCreateParamsBase():
    '''CompletionCreateParamsBase'''
    web_search_options: 'WebSearchOptions' = 'CompletionCreateParamsBase'

CompletionCreateParamsBase = <NODE:27>(CompletionCreateParamsBase, 'CompletionCreateParamsBase', TypedDict, total = False)
FunctionCall: 'TypeAlias' = Union[(Literal[('none', 'auto')], ChatCompletionFunctionCallOptionParam)]

def Function():
    '''Function'''
    parameters: 'FunctionParameters' = 'Function'

Function = <NODE:27>(Function, 'Function', TypedDict, total = False)
ResponseFormat: 'TypeAlias' = Union[(ResponseFormatText, ResponseFormatJSONSchema, ResponseFormatJSONObject)]

def WebSearchOptionsUserLocationApproximate():
    '''WebSearchOptionsUserLocationApproximate'''
    timezone: 'str' = 'Approximate location parameters for the search.'

WebSearchOptionsUserLocationApproximate = <NODE:27>(WebSearchOptionsUserLocationApproximate, 'WebSearchOptionsUserLocationApproximate', TypedDict, total = False)

def WebSearchOptionsUserLocation():
    '''WebSearchOptionsUserLocation'''
    type: "Required[Literal['approximate']]" = 'Approximate location parameters for the search.'

WebSearchOptionsUserLocation = <NODE:27>(WebSearchOptionsUserLocation, 'WebSearchOptionsUserLocation', TypedDict, total = False)

def WebSearchOptions():
    '''WebSearchOptions'''
    user_location: 'Optional[WebSearchOptionsUserLocation]' = '\n    This tool searches the web for relevant results to use in a response.\n    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).\n    '

WebSearchOptions = <NODE:27>(WebSearchOptions, 'WebSearchOptions', TypedDict, total = False)

def CompletionCreateParamsNonStreaming():
    '''CompletionCreateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'CompletionCreateParamsNonStreaming'

CompletionCreateParamsNonStreaming = <NODE:27>(CompletionCreateParamsNonStreaming, 'CompletionCreateParamsNonStreaming', CompletionCreateParamsBase, total = False)

class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'CompletionCreateParamsStreaming'

CompletionCreateParams = Union[(CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming)]
