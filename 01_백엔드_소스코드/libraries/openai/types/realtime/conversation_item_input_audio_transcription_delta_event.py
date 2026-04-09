# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_delta_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from log_prob_properties import LogProbProperties
__all__ = [
    'ConversationItemInputAudioTranscriptionDeltaEvent']

class ConversationItemInputAudioTranscriptionDeltaEvent(BaseModel):
    type: Literal['conversation.item.input_audio_transcription.delta'] = '\n    Returned when the text value of an input audio transcription content part is updated with incremental transcription results.\n    '
    content_index: Optional[int] = None
    delta: Optional[str] = None
    logprobs: Optional[List[LogProbProperties]] = None
