# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared_params.metadata import Metadata
from code_interpreter_tool_param import CodeInterpreterToolParam
from threads.message_content_part_param import MessageContentPartParam
__all__ = [
    'ThreadCreateParams',
    'Message',
    'MessageAttachment',
    'MessageAttachmentTool',
    'MessageAttachmentToolFileSearch',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch',
    'ToolResourcesFileSearchVectorStore',
    'ToolResourcesFileSearchVectorStoreChunkingStrategy',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyAuto',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyStatic',
    'ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic']

def ThreadCreateParams():
    '''ThreadCreateParams'''
    tool_resources: 'Optional[ToolResources]' = 'ThreadCreateParams'

ThreadCreateParams = <NODE:27>(ThreadCreateParams, 'ThreadCreateParams', TypedDict, total = False)

def MessageAttachmentToolFileSearch():
    '''MessageAttachmentToolFileSearch'''
    type: "Required[Literal['file_search']]" = 'MessageAttachmentToolFileSearch'

MessageAttachmentToolFileSearch = <NODE:27>(MessageAttachmentToolFileSearch, 'MessageAttachmentToolFileSearch', TypedDict, total = False)
MessageAttachmentTool: 'TypeAlias' = Union[(CodeInterpreterToolParam, MessageAttachmentToolFileSearch)]

def MessageAttachment():
    '''MessageAttachment'''
    tools: 'Iterable[MessageAttachmentTool]' = 'MessageAttachment'

MessageAttachment = <NODE:27>(MessageAttachment, 'MessageAttachment', TypedDict, total = False)

def Message():
    '''Message'''
    metadata: 'Optional[Metadata]' = 'Message'

Message = <NODE:27>(Message, 'Message', TypedDict, total = False)

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
    file_search: 'ToolResourcesFileSearch' = "\n    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n    "

ToolResources = <NODE:27>(ToolResources, 'ToolResources', TypedDict, total = False)
