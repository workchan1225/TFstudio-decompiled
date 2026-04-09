# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_delta_usage.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from server_tool_usage import ServerToolUsage
__all__ = [
    'MessageDeltaUsage']

class MessageDeltaUsage(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None
    output_tokens: int = None
    server_tool_use: Optional[ServerToolUsage] = None
