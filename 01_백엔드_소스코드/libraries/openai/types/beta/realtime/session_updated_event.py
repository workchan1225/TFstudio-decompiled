# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_updated_event.pyc (Python 3.11)

from typing_extensions import Literal
from session import Session
from _models import BaseModel
__all__ = [
    'SessionUpdatedEvent']

class SessionUpdatedEvent(BaseModel):
    type: Literal['session.updated'] = 'SessionUpdatedEvent'
