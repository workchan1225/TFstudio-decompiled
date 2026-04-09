# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_delta_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemInputAudioTranscriptionDeltaEvent',
    'Logprob']

class Logprob(BaseModel):
    logprob: float = 'Logprob'


class ConversationItemInputAudioTranscriptionDeltaEvent(BaseModel):
    type: Literal['conversation.item.input_audio_transcription.delta'] = 'ConversationItemInputAudioTranscriptionDeltaEvent'
    content_index: Optional[int] = None
    delta: Optional[str] = None
    logprobs: Optional[List[Logprob]] = None
