# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rate_limits_updated_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RateLimitsUpdatedEvent',
    'RateLimit']

class RateLimit(BaseModel):
    limit: Optional[int] = None
    name: Optional[Literal[('requests', 'tokens')]] = None
    remaining: Optional[int] = None
    reset_seconds: Optional[float] = None


class RateLimitsUpdatedEvent(BaseModel):
    type: Literal['rate_limits.updated'] = 'RateLimitsUpdatedEvent'
