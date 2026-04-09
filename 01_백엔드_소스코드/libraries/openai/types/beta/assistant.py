# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from assistant_tool import AssistantTool
from shared.metadata import Metadata
from assistant_response_format_option import AssistantResponseFormatOption
__all__ = [
    'Assistant',
    'ToolResources',
    'ToolResourcesCodeInterpreter',
    'ToolResourcesFileSearch']

class ToolResourcesCodeInterpreter(BaseModel):
    file_ids: Optional[List[str]] = None


class ToolResourcesFileSearch(BaseModel):
    vector_store_ids: Optional[List[str]] = None


class ToolResources(BaseModel):
    """A set of resources that are used by the assistant's tools.

    The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.
    """
    code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    file_search: Optional[ToolResourcesFileSearch] = None


class Assistant(BaseModel):
    created_at: int = 'Represents an `assistant` that can call the model and use tools.'
    description: Optional[str] = None
    instructions: Optional[str] = None
    model: str = None
    tools: List[AssistantTool] = None
    response_format: Optional[AssistantResponseFormatOption] = None
    temperature: Optional[float] = None
    tool_resources: Optional[ToolResources] = None
    top_p: Optional[float] = None
