# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_text_done_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionTextDoneEvent',
    'Logprob',
    'Usage',
    'UsageInputTokenDetails']

class Logprob(BaseModel):
    token: Optional[str] = None
    bytes: Optional[List[int]] = None
    logprob: Optional[float] = None


class UsageInputTokenDetails(BaseModel):
    '''Details about the input tokens billed for this request.'''
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class Usage(BaseModel):
    type: Literal['tokens'] = 'Usage statistics for models billed by token usage.'
    input_token_details: Optional[UsageInputTokenDetails] = None


class TranscriptionTextDoneEvent(BaseModel):
    type: Literal['transcript.text.done'] = 'Emitted when the transcription is complete.\n\n    Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.\n    '
    logprobs: Optional[List[Logprob]] = None
    usage: Optional[Usage] = None
