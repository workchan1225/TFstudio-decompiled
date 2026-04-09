# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_created_event.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from realtime_session_create_request import RealtimeSessionCreateRequest
from realtime_transcription_session_create_request import RealtimeTranscriptionSessionCreateRequest
__all__ = [
    'SessionCreatedEvent',
    'Session']
Session: TypeAlias = Union[(RealtimeSessionCreateRequest, RealtimeTranscriptionSessionCreateRequest)]

class SessionCreatedEvent(BaseModel):
    type: Literal['session.created'] = 'Returned when a Session is created.\n\n    Emitted automatically when a new\n    connection is established as the first server event. This event will contain\n    the default Session configuration.\n    '
