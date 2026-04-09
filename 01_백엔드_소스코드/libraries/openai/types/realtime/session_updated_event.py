# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_updated_event.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from realtime_session_create_request import RealtimeSessionCreateRequest
from realtime_transcription_session_create_request import RealtimeTranscriptionSessionCreateRequest
__all__ = [
    'SessionUpdatedEvent',
    'Session']
Session: TypeAlias = Union[(RealtimeSessionCreateRequest, RealtimeTranscriptionSessionCreateRequest)]

class SessionUpdatedEvent(BaseModel):
    type: Literal['session.updated'] = '\n    Returned when a session is updated with a `session.update` event, unless\n    there is an error.\n    '
