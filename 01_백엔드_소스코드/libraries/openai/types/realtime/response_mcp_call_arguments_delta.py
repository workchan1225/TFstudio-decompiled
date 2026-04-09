# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_arguments_delta.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallArgumentsDelta']

class ResponseMcpCallArgumentsDelta(BaseModel):
    type: Literal['response.mcp_call_arguments.delta'] = 'Returned when MCP tool call arguments are updated during response generation.'
    obfuscation: Optional[str] = None
