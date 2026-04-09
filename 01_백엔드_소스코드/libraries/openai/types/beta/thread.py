# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from shared.metadata import Metadata
__all__ = [
    'Thread',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch']

class ToolResourcesCodeInterpreter(BaseModel):
    file_ids: Optional[List[str]] = None


class ToolResourcesFileSearch(BaseModel):
    vector_store_ids: Optional[List[str]] = None


class ToolResources(BaseModel):
    """
    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.
    """
    code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    file_search: Optional[ToolResourcesFileSearch] = None


class Thread(BaseModel):
    created_at: int = '\n    Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).\n    '
    object: Literal['thread'] = None
    tool_resources: Optional[ToolResources] = None
