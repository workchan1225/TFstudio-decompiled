# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread_update_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import TypedDict
from _types import SequenceNotStr
from shared_params.metadata import Metadata
__all__ = [
    'ThreadUpdateParams',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch']

def ThreadUpdateParams():
    '''ThreadUpdateParams'''
    tool_resources: 'Optional[ToolResources]' = 'ThreadUpdateParams'

ThreadUpdateParams = <NODE:27>(ThreadUpdateParams, 'ThreadUpdateParams', TypedDict, total = False)

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
    file_search: 'ToolResourcesFileSearch' = "\n    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.\n    "

ToolResources = <NODE:27>(ToolResources, 'ToolResources', TypedDict, total = False)
