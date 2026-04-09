# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_dtmf_event_received_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferDtmfEventReceivedEvent']

class InputAudioBufferDtmfEventReceivedEvent(BaseModel):
    type: Literal['input_audio_buffer.dtmf_event_received'] = '**SIP Only:** Returned when an DTMF event is received.\n\n    A DTMF event is a message that\n    represents a telephone keypad press (0–9, *, #, A–D). The `event` property\n    is the keypad that the user press. The `received_at` is the UTC Unix Timestamp\n    that the server received the event.\n    '
