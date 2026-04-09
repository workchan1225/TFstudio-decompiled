# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_failed_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemInputAudioTranscriptionFailedEvent',
    'Error']

class Error(BaseModel):
    '''Details of the transcription error.'''
    code: Optional[str] = None
    message: Optional[str] = None
    param: Optional[str] = None
    type: Optional[str] = None


class ConversationItemInputAudioTranscriptionFailedEvent(BaseModel):
    type: Literal['conversation.item.input_audio_transcription.failed'] = '\n    Returned when input audio transcription is configured, and a transcription\n    request for a user message failed. These events are separate from other\n    `error` events so that the client can identify the related Item.\n    '
