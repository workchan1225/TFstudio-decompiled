# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_created_event.pyc (Python 3.11)

from typing_extensions import Literal
from session import Session
from _models import BaseModel
__all__ = [
    'SessionCreatedEvent']

class SessionCreatedEvent(BaseModel):
    type: Literal['session.created'] = 'SessionCreatedEvent'
