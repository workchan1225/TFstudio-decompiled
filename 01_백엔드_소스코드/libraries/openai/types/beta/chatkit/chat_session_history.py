# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_history.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'ChatSessionHistory']

class ChatSessionHistory(BaseModel):
    enabled: bool = 'History retention preferences returned for the session.'
    recent_threads: Optional[int] = None
