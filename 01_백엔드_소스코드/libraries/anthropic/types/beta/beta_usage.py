# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_usage.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from beta_cache_creation import BetaCacheCreation
from beta_server_tool_usage import BetaServerToolUsage
__all__ = [
    'BetaUsage']

class BetaUsage(BaseModel):
    cache_creation: Optional[BetaCacheCreation] = None
    cache_creation_input_tokens: Optional[int] = None
    output_tokens: int = None
    server_tool_use: Optional[BetaServerToolUsage] = None
    service_tier: Optional[Literal[('standard', 'priority', 'batch')]] = None
