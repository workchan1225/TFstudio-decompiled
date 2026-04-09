# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_update_event.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from realtime_session_create_request import RealtimeSessionCreateRequest
from realtime_transcription_session_create_request import RealtimeTranscriptionSessionCreateRequest
__all__ = [
    'SessionUpdateEvent',
    'Session']
Session: TypeAlias = Union[(RealtimeSessionCreateRequest, RealtimeTranscriptionSessionCreateRequest)]

class SessionUpdateEvent(BaseModel):
    type: Literal['session.update'] = '\n    Send this event to update the session’s configuration.\n    The client may send this event at any time to update any field\n    except for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.\n\n    When the server receives a `session.update`, it will respond\n    with a `session.updated` event showing the full, effective configuration.\n    Only the fields that are present in the `session.update` are updated. To clear a field like\n    `instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.\n    To clear a field like `turn_detection`, pass `null`.\n    '
    event_id: Optional[str] = None
