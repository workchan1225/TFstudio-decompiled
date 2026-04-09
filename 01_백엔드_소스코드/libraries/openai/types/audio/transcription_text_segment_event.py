# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_text_segment_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionTextSegmentEvent']

class TranscriptionTextSegmentEvent(BaseModel):
    type: Literal['transcript.text.segment'] = '\n    Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.\n    '
