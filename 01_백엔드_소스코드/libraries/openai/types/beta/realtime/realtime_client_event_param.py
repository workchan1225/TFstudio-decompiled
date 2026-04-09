# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_client_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from session_update_event_param import SessionUpdateEventParam
from response_cancel_event_param import ResponseCancelEventParam
from response_create_event_param import ResponseCreateEventParam
from transcription_session_update_param import TranscriptionSessionUpdateParam
from conversation_item_create_event_param import ConversationItemCreateEventParam
from conversation_item_delete_event_param import ConversationItemDeleteEventParam
from input_audio_buffer_clear_event_param import InputAudioBufferClearEventParam
from input_audio_buffer_append_event_param import InputAudioBufferAppendEventParam
from input_audio_buffer_commit_event_param import InputAudioBufferCommitEventParam
from conversation_item_retrieve_event_param import ConversationItemRetrieveEventParam
from conversation_item_truncate_event_param import ConversationItemTruncateEventParam
__all__ = [
    'RealtimeClientEventParam',
    'OutputAudioBufferClear']

def OutputAudioBufferClear():
    '''OutputAudioBufferClear'''
    event_id: 'str' = 'OutputAudioBufferClear'

OutputAudioBufferClear = <NODE:27>(OutputAudioBufferClear, 'OutputAudioBufferClear', TypedDict, total = False)
RealtimeClientEventParam: 'TypeAlias' = Union[(ConversationItemCreateEventParam, ConversationItemDeleteEventParam, ConversationItemRetrieveEventParam, ConversationItemTruncateEventParam, InputAudioBufferAppendEventParam, InputAudioBufferClearEventParam, OutputAudioBufferClear, InputAudioBufferCommitEventParam, ResponseCancelEventParam, ResponseCreateEventParam, SessionUpdateEventParam, TranscriptionSessionUpdateParam)]
