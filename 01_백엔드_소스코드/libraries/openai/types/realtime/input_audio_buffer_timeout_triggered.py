# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_timeout_triggered.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferTimeoutTriggered']

class InputAudioBufferTimeoutTriggered(BaseModel):
    type: Literal['input_audio_buffer.timeout_triggered'] = "Returned when the Server VAD timeout is triggered for the input audio buffer.\n\n    This is configured\n    with `idle_timeout_ms` in the `turn_detection` settings of the session, and it indicates that\n    there hasn't been any speech detected for the configured duration.\n\n    The `audio_start_ms` and `audio_end_ms` fields indicate the segment of audio after the last\n    model response up to the triggering time, as an offset from the beginning of audio written\n    to the input audio buffer. This means it demarcates the segment of audio that was silent and\n    the difference between the start and end values will roughly match the configured timeout.\n\n    The empty audio will be committed to the conversation as an `input_audio` item (there will be a\n    `input_audio_buffer.committed` event) and a model response will be generated. There may be speech\n    that didn't trigger VAD but is still detected by the model, so the model may respond with\n    something relevant to the conversation or a prompt to continue speaking.\n    "
