# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_create_response.pyc (Python 3.11)

from typing import Union
from typing_extensions import TypeAlias
from transcription import Transcription
from transcription_verbose import TranscriptionVerbose
from transcription_diarized import TranscriptionDiarized
__all__ = [
    'TranscriptionCreateResponse']
TranscriptionCreateResponse: TypeAlias = Union[(Transcription, TranscriptionDiarized, TranscriptionVerbose)]
