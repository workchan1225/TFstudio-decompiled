# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_rate_limits.pyc (Python 3.11)

from _models import BaseModel
__all__ = [
    'ChatSessionRateLimits']

class ChatSessionRateLimits(BaseModel):
    max_requests_per_1_minute: int = 'Active per-minute request limit for the session.'
