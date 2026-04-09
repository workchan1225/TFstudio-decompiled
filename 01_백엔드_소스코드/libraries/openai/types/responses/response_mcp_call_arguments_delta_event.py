# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_arguments_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallArgumentsDeltaEvent']

class ResponseMcpCallArgumentsDeltaEvent(BaseModel):
    type: Literal['response.mcp_call_arguments.delta'] = '\n    Emitted when there is a delta (partial update) to the arguments of an MCP tool call.\n    '
