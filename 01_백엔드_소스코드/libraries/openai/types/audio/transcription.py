# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'Transcription',
    'Logprob',
    'Usage',
    'UsageTokens',
    'UsageTokensInputTokenDetails',
    'UsageDuration']

class Logprob(BaseModel):
    token: Optional[str] = None
    bytes: Optional[List[float]] = None
    logprob: Optional[float] = None


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

class Transcription(BaseModel):
    text: str = '\n    Represents a transcription response returned by model, based on the provided input.\n    '
    logprobs: Optional[List[Logprob]] = None
    usage: Optional[Usage] = None
