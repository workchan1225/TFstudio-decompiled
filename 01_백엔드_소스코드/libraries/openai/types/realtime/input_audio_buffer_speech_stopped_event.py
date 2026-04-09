# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_speech_stopped_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferSpeechStoppedEvent']

class InputAudioBufferSpeechStoppedEvent(BaseModel):
    type: Literal['input_audio_buffer.speech_stopped'] = '\n    Returned in `server_vad` mode when the server detects the end of speech in\n    the audio buffer. The server will also send an `conversation.item.created`\n    event with the user message item that is created from the audio buffer.\n    '
