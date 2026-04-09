# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_text_delta_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionTextDeltaEvent',
    'Logprob']

class Logprob(BaseModel):
    token: Optional[str] = None
    bytes: Optional[List[int]] = None
    logprob: Optional[float] = None


class TranscriptionTextDeltaEvent(BaseModel):
    type: Literal['transcript.text.delta'] = 'Emitted when there is an additional text delta.\n\n    This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.\n    '
    logprobs: Optional[List[Logprob]] = None
    segment_id: Optional[str] = None
