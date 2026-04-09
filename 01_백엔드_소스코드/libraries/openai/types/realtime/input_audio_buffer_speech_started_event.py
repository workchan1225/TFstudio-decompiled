# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_speech_started_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferSpeechStartedEvent']

class InputAudioBufferSpeechStartedEvent(BaseModel):
    type: Literal['input_audio_buffer.speech_started'] = '\n    Sent by the server when in `server_vad` mode to indicate that speech has been\n    detected in the audio buffer. This can happen any time audio is added to the\n    buffer (unless speech is already detected). The client may want to use this\n    event to interrupt audio playback or provide visual feedback to the user.\n\n    The client should expect to receive a `input_audio_buffer.speech_stopped` event\n    when speech stops. The `item_id` property is the ID of the user message item\n    that will be created when speech stops and will also be included in the\n    `input_audio_buffer.speech_stopped` event (unless the client manually commits\n    the audio buffer during VAD activation).\n    '
