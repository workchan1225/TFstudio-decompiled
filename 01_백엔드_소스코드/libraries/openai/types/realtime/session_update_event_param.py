# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_update_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from realtime_session_create_request_param import RealtimeSessionCreateRequestParam
from realtime_transcription_session_create_request_param import RealtimeTranscriptionSessionCreateRequestParam
__all__ = [
    'SessionUpdateEventParam',
    'Session']
Session: 'TypeAlias' = Union[(RealtimeSessionCreateRequestParam, RealtimeTranscriptionSessionCreateRequestParam)]

def SessionUpdateEventParam():
    '''SessionUpdateEventParam'''
    event_id: 'str' = '\n    Send this event to update the session’s configuration.\n    The client may send this event at any time to update any field\n    except for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.\n\n    When the server receives a `session.update`, it will respond\n    with a `session.updated` event showing the full, effective configuration.\n    Only the fields that are present in the `session.update` are updated. To clear a field like\n    `instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.\n    To clear a field like `turn_detection`, pass `null`.\n    '

SessionUpdateEventParam = <NODE:27>(SessionUpdateEventParam, 'SessionUpdateEventParam', TypedDict, total = False)
