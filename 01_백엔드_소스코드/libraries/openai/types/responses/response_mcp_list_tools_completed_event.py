# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_list_tools_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpListToolsCompletedEvent']

class ResponseMcpListToolsCompletedEvent(BaseModel):
    type: Literal['response.mcp_list_tools.completed'] = 'Emitted when the list of available MCP tools has been successfully retrieved.'
