# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_arguments_done.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallArgumentsDone']

class ResponseMcpCallArgumentsDone(BaseModel):
    type: Literal['response.mcp_call_arguments.done'] = 'Returned when MCP tool call arguments are finalized during response generation.'
