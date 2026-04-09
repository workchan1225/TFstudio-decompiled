# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared.chat_model import ChatModel
from assistant_tool_param import AssistantToolParam
from shared_params.metadata import Metadata
from shared.reasoning_effort import ReasoningEffort
from assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'AssistantCreateParams',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch',
    'ToolResourcesFileSearchVectorStore',
    'ToolResourcesFileSearchVectorStoreChunkingStrategy',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyAuto',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyStatic',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic']

def AssistantCreateParams():
    '''AssistantCreateParams'''
    top_p: 'Optional[float]' = 'AssistantCreateParams'

AssistantCreateParams = <NODE:27>(AssistantCreateParams, 'AssistantCreateParams', TypedDict, total = False)

def ToolResourcesCodeInterpreter():
    '''ToolResourcesCodeInterpreter'''
    file_ids: 'SequenceNotStr[str]' = 'ToolResourcesCodeInterpreter'

ToolResourcesCodeInterpreter = <NODE:27>(ToolResourcesCodeInterpreter, 'ToolResourcesCodeInterpreter', TypedDict, total = False)

def ToolResourcesFileSearchVectorStoreChunkingStrategyAuto():
    '''ToolResourcesFileSearchVectorStoreChunkingStrategyAuto'''
    type: "Required[Literal['auto']]" = 'The default strategy.\n\n    This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.\n    '

ToolResourcesFileSearchVectorStoreChunkingStrategyAuto = <NODE:27>(ToolResourcesFileSearchVectorStoreChunkingStrategyAuto, 'ToolResourcesFileSearchVectorStoreChunkingStrategyAuto', TypedDict, total = False)

def ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic():
    '''ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic'''
    max_chunk_size_tokens: 'Required[int]' = 'ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic'

ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic = <NODE:27>(ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic, 'ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic', TypedDict, total = False)

def ToolResourcesFileSearchVectorStoreChunkingStrategyStatic():
    '''ToolResourcesFileSearchVectorStoreChunkingStrategyStatic'''
    type: "Required[Literal['static']]" = 'ToolResourcesFileSearchVectorStoreChunkingStrategyStatic'

ToolResourcesFileSearchVectorStoreChunkingStrategyStatic = <NODE:27>(ToolResourcesFileSearchVectorStoreChunkingStrategyStatic, 'ToolResourcesFileSearchVectorStoreChunkingStrategyStatic', TypedDict, total = False)
ToolResourcesFileSearchVectorStoreChunkingStrategy: 'TypeAlias' = Union[(ToolResourcesFileSearchVectorStoreChunkingStrategyAuto, ToolResourcesFileSearchVectorStoreChunkingStrategyStatic)]

def ToolResourcesFileSearchVectorStore():
    '''ToolResourcesFileSearchVectorStore'''
    metadata: 'Optional[Metadata]' = 'ToolResourcesFileSearchVectorStore'

ToolResourcesFileSearchVectorStore = <NODE:27>(ToolResourcesFileSearchVectorStore, 'ToolResourcesFileSearchVectorStore', TypedDict, total = False)

def ToolResourcesFileSearch():
    '''ToolResourcesFileSearch'''
    vector_stores: 'Iterable[ToolResourcesFileSearchVectorStore]' = 'ToolResourcesFileSearch'

ToolResourcesFileSearch = <NODE:27>(ToolResourcesFileSearch, 'ToolResourcesFileSearch', TypedDict, total = False)

def ToolResources():
    '''ToolResources'''
    file_search: 'ToolResourcesFileSearch' = "A set of resources that are used by the assistant's tools.\n\n    The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n    "

ToolResources = <NODE:27>(ToolResources, 'ToolResources', TypedDict, total = False)
