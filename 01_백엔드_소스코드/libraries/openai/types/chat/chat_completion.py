# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from completion_usage import CompletionUsage
from chat_completion_message import ChatCompletionMessage
from chat_completion_token_logprob import ChatCompletionTokenLogprob
__all__ = [
    'ChatCompletion',
    'Choice',
    'ChoiceLogprobs']

class ChoiceLogprobs(BaseModel):
    '''Log probability information for the choice.'''
    content: Optional[List[ChatCompletionTokenLogprob]] = None
    refusal: Optional[List[ChatCompletionTokenLogprob]] = None


class Choice(BaseModel):
    index: int = 'Choice'
    message: ChatCompletionMessage = None


class ChatCompletion(BaseModel):
    object: Literal['chat.completion'] = '\n    Represents a chat completion response returned by model, based on the provided input.\n    '
    service_tier: Optional[Literal[('auto', 'default', 'flex', 'scale', 'priority')]] = None
    system_fingerprint: Optional[str] = None
    usage: Optional[CompletionUsage] = None
