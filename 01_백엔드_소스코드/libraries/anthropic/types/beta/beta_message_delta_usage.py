# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message_delta_usage.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from beta_server_tool_usage import BetaServerToolUsage
__all__ = [
    'BetaMessageDeltaUsage']

class BetaMessageDeltaUsage(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    cache_read_input_tokens: Optional[int] = None
    output_tokens: int = None
    server_tool_use: Optional[BetaServerToolUsage] = None
