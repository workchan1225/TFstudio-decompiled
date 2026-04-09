# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: translation_verbose.pyc (Python 3.11)

from typing import List, Optional
from _models import BaseModel
from transcription_segment import TranscriptionSegment
__all__ = [
    'TranslationVerbose']

class TranslationVerbose(BaseModel):
    text: str = 'TranslationVerbose'
    segments: Optional[List[TranscriptionSegment]] = None
