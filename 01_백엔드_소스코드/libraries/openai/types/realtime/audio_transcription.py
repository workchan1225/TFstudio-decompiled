# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio_transcription.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'AudioTranscription']

class AudioTranscription(BaseModel):
    language: Optional[str] = None
    model: Union[(str, Literal[('whisper-1', 'gpt-4o-mini-transcribe', 'gpt-4o-mini-transcribe-2025-12-15', 'gpt-4o-transcribe', 'gpt-4o-transcribe-diarize')], None)] = None
    prompt: Optional[str] = None
