# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_tool_call.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from realtime_mcphttp_error import RealtimeMcphttpError
from realtime_mcp_protocol_error import RealtimeMcpProtocolError
from realtime_mcp_tool_execution_error import RealtimeMcpToolExecutionError
__all__ = [
    'RealtimeMcpToolCall',
    'Error']
Error: TypeAlias = Annotated[(Union[(RealtimeMcpProtocolError, RealtimeMcpToolExecutionError, RealtimeMcphttpError, None)], PropertyInfo(discriminator = 'type'))]

class RealtimeMcpToolCall(BaseModel):
    type: Literal['mcp_call'] = 'A Realtime item representing an invocation of a tool on an MCP server.'
    approval_request_id: Optional[str] = None
    error: Optional[Error] = None
    output: Optional[str] = None
