# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_segment.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemInputAudioTranscriptionSegment']

class ConversationItemInputAudioTranscriptionSegment(BaseModel):
    type: Literal['conversation.item.input_audio_transcription.segment'] = 'Returned when an input audio transcription segment is identified for an item.'
