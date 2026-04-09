# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_diarized_segment.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionDiarizedSegment']

class TranscriptionDiarizedSegment(BaseModel):
    type: Literal['transcript.text.segment'] = 'A segment of diarized transcript text with speaker metadata.'
