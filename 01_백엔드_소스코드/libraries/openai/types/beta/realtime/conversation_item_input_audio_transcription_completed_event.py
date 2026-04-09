# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_completed_event.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
__all__ = [
    'ConversationItemInputAudioTranscriptionCompletedEvent',
    'Usage',
    'UsageTranscriptTextUsageTokens',
    'UsageTranscriptTextUsageTokensInputTokenDetails',
    'UsageTranscriptTextUsageDuration',
    'Logprob']

class UsageTranscriptTextUsageTokensInputTokenDetails(BaseModel):
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class UsageTranscriptTextUsageTokens(BaseModel):
    type: Literal['tokens'] = 'UsageTranscriptTextUsageTokens'
    input_token_details: Optional[UsageTranscriptTextUsageTokensInputTokenDetails] = None


class UsageTranscriptTextUsageDuration(BaseModel):
    type: Literal['duration'] = 'UsageTranscriptTextUsageDuration'

Usage: TypeAlias = Union[(UsageTranscriptTextUsageTokens, UsageTranscriptTextUsageDuration)]

class Logprob(BaseModel):
    logprob: float = 'Logprob'


class ConversationItemInputAudioTranscriptionCompletedEvent(BaseModel):
    usage: Usage = 'ConversationItemInputAudioTranscriptionCompletedEvent'
    logprobs: Optional[List[Logprob]] = None
