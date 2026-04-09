# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_diarized.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from transcription_diarized_segment import TranscriptionDiarizedSegment
__all__ = [
    'TranscriptionDiarized',
    'Usage',
    'UsageTokens',
    'UsageTokensInputTokenDetails',
    'UsageDuration']

class UsageTokensInputTokenDetails(BaseModel):
    '''Details about the input tokens billed for this request.'''
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class UsageTokens(BaseModel):
    type: Literal['tokens'] = 'Usage statistics for models billed by token usage.'
    input_token_details: Optional[UsageTokensInputTokenDetails] = None


class UsageDuration(BaseModel):
    type: Literal['duration'] = 'Usage statistics for models billed by audio input duration.'

Usage: TypeAlias = Annotated[(Union[(UsageTokens, UsageDuration)], PropertyInfo(discriminator = 'type'))]

class TranscriptionDiarized(BaseModel):
    text: str = '\n    Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.\n    '
    usage: Optional[Usage] = None
