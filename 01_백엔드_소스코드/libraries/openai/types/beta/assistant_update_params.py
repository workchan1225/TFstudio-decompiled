# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_update_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, TypedDict
from _types import SequenceNotStr
from assistant_tool_param import AssistantToolParam
from shared_params.metadata import Metadata
from shared.reasoning_effort import ReasoningEffort
from assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'AssistantUpdateParams',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch']

def AssistantUpdateParams():
    '''AssistantUpdateParams'''
    top_p: 'Optional[float]' = 'AssistantUpdateParams'

AssistantUpdateParams = <NODE:27>(AssistantUpdateParams, 'AssistantUpdateParams', TypedDict, total = False)

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
