# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_arguments_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallArgumentsDoneEvent']

class ResponseMcpCallArgumentsDoneEvent(BaseModel):
    type: Literal['response.mcp_call_arguments.done'] = 'Emitted when the arguments for an MCP tool call are finalized.'
