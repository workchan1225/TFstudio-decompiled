# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread_create_and_run_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from shared.chat_model import ChatModel
from assistant_tool_param import AssistantToolParam
from shared_params.metadata import Metadata
from code_interpreter_tool_param import CodeInterpreterToolParam
from assistant_tool_choice_option_param import AssistantToolChoiceOptionParam
from threads.message_content_part_param import MessageContentPartParam
from assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'ThreadCreateAndRunParamsBase',
    'Thread',
    'ThreadMessage',
    'ThreadMessageAttachment',
    'ThreadMessageAttachmentTool',
    'ThreadMessageAttachmentToolFileSearch',
    'ThreadToolResources',
    'ThreadToolResourcesCodeInterpreter',
    'ThreadToolResourcesFileSearch',
    'ThreadToolResourcesFileSearchVectorStore',
    'ThreadToolResourcesFileSearchVectorStoreChunkingStrategy',
    'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto',
    'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic',
    'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch',
    'TruncationStrategy',
    'ThreadCreateAndRunParamsNonStreaming',
    'ThreadCreateAndRunParamsStreaming']

def ThreadCreateAndRunParamsBase():
    '''ThreadCreateAndRunParamsBase'''
    truncation_strategy: 'Optional[TruncationStrategy]' = 'ThreadCreateAndRunParamsBase'

ThreadCreateAndRunParamsBase = <NODE:27>(ThreadCreateAndRunParamsBase, 'ThreadCreateAndRunParamsBase', TypedDict, total = False)

def ThreadMessageAttachmentToolFileSearch():
    '''ThreadMessageAttachmentToolFileSearch'''
    type: "Required[Literal['file_search']]" = 'ThreadMessageAttachmentToolFileSearch'

ThreadMessageAttachmentToolFileSearch = <NODE:27>(ThreadMessageAttachmentToolFileSearch, 'ThreadMessageAttachmentToolFileSearch', TypedDict, total = False)
ThreadMessageAttachmentTool: 'TypeAlias' = Union[(CodeInterpreterToolParam, ThreadMessageAttachmentToolFileSearch)]

def ThreadMessageAttachment():
    '''ThreadMessageAttachment'''
    tools: 'Iterable[ThreadMessageAttachmentTool]' = 'ThreadMessageAttachment'

ThreadMessageAttachment = <NODE:27>(ThreadMessageAttachment, 'ThreadMessageAttachment', TypedDict, total = False)

def ThreadMessage():
    '''ThreadMessage'''
    metadata: 'Optional[Metadata]' = 'ThreadMessage'

ThreadMessage = <NODE:27>(ThreadMessage, 'ThreadMessage', TypedDict, total = False)

def ThreadToolResourcesCodeInterpreter():
    '''ThreadToolResourcesCodeInterpreter'''
    file_ids: 'SequenceNotStr[str]' = 'ThreadToolResourcesCodeInterpreter'

ThreadToolResourcesCodeInterpreter = <NODE:27>(ThreadToolResourcesCodeInterpreter, 'ThreadToolResourcesCodeInterpreter', TypedDict, total = False)

def ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto():
    '''ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto'''
    type: "Required[Literal['auto']]" = 'The default strategy.\n\n    This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.\n    '

ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto = <NODE:27>(ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto, 'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto', TypedDict, total = False)

def ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic():
    '''ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic'''
    max_chunk_size_tokens: 'Required[int]' = 'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic'

ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic = <NODE:27>(ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic, 'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic', TypedDict, total = False)

def ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic():
    '''ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic'''
    type: "Required[Literal['static']]" = 'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic'

ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic = <NODE:27>(ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic, 'ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic', TypedDict, total = False)
ThreadToolResourcesFileSearchVectorStoreChunkingStrategy: 'TypeAlias' = Union[(ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto, ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic)]

def ThreadToolResourcesFileSearchVectorStore():
    '''ThreadToolResourcesFileSearchVectorStore'''
    metadata: 'Optional[Metadata]' = 'ThreadToolResourcesFileSearchVectorStore'

ThreadToolResourcesFileSearchVectorStore = <NODE:27>(ThreadToolResourcesFileSearchVectorStore, 'ThreadToolResourcesFileSearchVectorStore', TypedDict, total = False)

def ThreadToolResourcesFileSearch():
    '''ThreadToolResourcesFileSearch'''
    vector_stores: 'Iterable[ThreadToolResourcesFileSearchVectorStore]' = 'ThreadToolResourcesFileSearch'

ThreadToolResourcesFileSearch = <NODE:27>(ThreadToolResourcesFileSearch, 'ThreadToolResourcesFileSearch', TypedDict, total = False)

def ThreadToolResources():
    '''ThreadToolResources'''
    file_search: 'ThreadToolResourcesFileSearch' = "\n    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n    "

ThreadToolResources = <NODE:27>(ThreadToolResources, 'ThreadToolResources', TypedDict, total = False)

def Thread():
    '''Thread'''
    tool_resources: 'Optional[ThreadToolResources]' = 'Options to create a new thread.\n\n    If no thread is provided when running a\n    request, an empty thread will be created.\n    '

Thread = <NODE:27>(Thread, 'Thread', TypedDict, total = False)

def ToolResourcesCodeInterpreter():
    '''ToolResourcesCodeInterpreter'''
    file_ids: 'SequenceNotStr[str]' = 'ToolResourcesCodeInterpreter'

ToolResourcesCodeInterpreter = <NODE:27>(ToolResourcesCodeInterpreter, 'ToolResourcesCodeInterpreter', TypedDict, total = False)

def ToolResourcesFileSearch():
    '''ToolResourcesFileSearch'''
    vector_store_ids: 'SequenceNotStr[str]' = 'ToolResourcesFileSearch'

ToolResourcesFileSearch = <NODE:27>(ToolResourcesFileSearch, 'ToolResourcesFileSearch', TypedDict, total = False)

def ToolResources():
    '''ToolResources'''
    file_search: 'ToolResourcesFileSearch' = "A set of resources that are used by the assistant's tools.\n\n    The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n    "

ToolResources = <NODE:27>(ToolResources, 'ToolResources', TypedDict, total = False)

def TruncationStrategy():
    '''TruncationStrategy'''
    last_messages: 'Optional[int]' = 'Controls for how a thread will be truncated prior to the run.\n\n    Use this to control the initial context window of the run.\n    '

TruncationStrategy = <NODE:27>(TruncationStrategy, 'TruncationStrategy', TypedDict, total = False)

def ThreadCreateAndRunParamsNonStreaming():
    '''ThreadCreateAndRunParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'ThreadCreateAndRunParamsNonStreaming'

ThreadCreateAndRunParamsNonStreaming = <NODE:27>(ThreadCreateAndRunParamsNonStreaming, 'ThreadCreateAndRunParamsNonStreaming', ThreadCreateAndRunParamsBase, total = False)

class ThreadCreateAndRunParamsStreaming(ThreadCreateAndRunParamsBase):
    stream: 'Required[Literal[True]]' = 'ThreadCreateAndRunParamsStreaming'

ThreadCreateAndRunParams = Union[(ThreadCreateAndRunParamsNonStreaming, ThreadCreateAndRunParamsStreaming)]
