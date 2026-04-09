# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion_usage.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'CompletionUsage',
    'CompletionTokensDetails',
    'PromptTokensDetails']

class CompletionTokensDetails(BaseModel):
    '''Breakdown of tokens used in a completion.'''
    accepted_prediction_tokens: Optional[int] = None
    audio_tokens: Optional[int] = None
    reasoning_tokens: Optional[int] = None
    rejected_prediction_tokens: Optional[int] = None


class PromptTokensDetails(BaseModel):
    '''Breakdown of tokens used in the prompt.'''
    audio_tokens: Optional[int] = None
    cached_tokens: Optional[int] = None


class CompletionUsage(BaseModel):
    total_tokens: int = 'Usage statistics for the completion request.'
    completion_tokens_details: Optional[CompletionTokensDetails] = None
    prompt_tokens_details: Optional[PromptTokensDetails] = None
