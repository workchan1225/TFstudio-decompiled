# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_list_tools_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpListToolsInProgressEvent']

class ResponseMcpListToolsInProgressEvent(BaseModel):
    type: Literal['response.mcp_list_tools.in_progress'] = '\n    Emitted when the system is in the process of retrieving the list of available MCP tools.\n    '
