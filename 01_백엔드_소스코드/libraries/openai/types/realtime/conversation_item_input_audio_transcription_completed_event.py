# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_input_audio_transcription_completed_event.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from log_prob_properties import LogProbProperties
__all__ = [
    'ConversationItemInputAudioTranscriptionCompletedEvent',
    'Usage',
    'UsageTranscriptTextUsageTokens',
    'UsageTranscriptTextUsageTokensInputTokenDetails',
    'UsageTranscriptTextUsageDuration']

class UsageTranscriptTextUsageTokensInputTokenDetails(BaseModel):
    '''Details about the input tokens billed for this request.'''
    audio_tokens: Optional[int] = None
    text_tokens: Optional[int] = None


class UsageTranscriptTextUsageTokens(BaseModel):
    type: Literal['tokens'] = 'Usage statistics for models billed by token usage.'
    input_token_details: Optional[UsageTranscriptTextUsageTokensInputTokenDetails] = None


class UsageTranscriptTextUsageDuration(BaseModel):
    type: Literal['duration'] = 'Usage statistics for models billed by audio input duration.'

Usage: TypeAlias = Union[(UsageTranscriptTextUsageTokens, UsageTranscriptTextUsageDuration)]

class ConversationItemInputAudioTranscriptionCompletedEvent(BaseModel):
    usage: Usage = "\n    This event is the output of audio transcription for user audio written to the\n    user audio buffer. Transcription begins when the input audio buffer is\n    committed by the client or server (when VAD is enabled). Transcription runs\n    asynchronously with Response creation, so this event may come before or after\n    the Response events.\n\n    Realtime API models accept audio natively, and thus input transcription is a\n    separate process run on a separate ASR (Automatic Speech Recognition) model.\n    The transcript may diverge somewhat from the model's interpretation, and\n    should be treated as a rough guide.\n    "
    logprobs: Optional[List[LogProbProperties]] = None
