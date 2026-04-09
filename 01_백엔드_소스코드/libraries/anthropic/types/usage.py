# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: usage.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from cache_creation import CacheCreation
from server_tool_usage import ServerToolUsage
__all__ = [
    'Usage']

class Usage(BaseModel):
    cache_creation: Optional[CacheCreation] = None
    cache_creation_input_tokens: Optional[int] = None
    output_tokens: int = None
    server_tool_use: Optional[ServerToolUsage] = None
    service_tier: Optional[Literal[('standard', 'priority', 'batch')]] = None
