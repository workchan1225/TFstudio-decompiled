# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_session_updated_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from transcription_session import TranscriptionSession
__all__ = [
    'TranscriptionSessionUpdatedEvent']

class TranscriptionSessionUpdatedEvent(BaseModel):
    type: Literal['transcription_session.updated'] = 'TranscriptionSessionUpdatedEvent'
