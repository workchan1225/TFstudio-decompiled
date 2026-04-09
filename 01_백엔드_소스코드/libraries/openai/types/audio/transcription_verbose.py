# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_verbose.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from transcription_word import TranscriptionWord
from transcription_segment import TranscriptionSegment
__all__ = [
    'TranscriptionVerbose',
    'Usage']

class Usage(BaseModel):
    type: Literal['duration'] = 'Usage statistics for models billed by audio input duration.'


class TranscriptionVerbose(BaseModel):
    text: str = '\n    Represents a verbose json transcription response returned by model, based on the provided input.\n    '
    segments: Optional[List[TranscriptionSegment]] = None
    usage: Optional[Usage] = None
    words: Optional[List[TranscriptionWord]] = None
