# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_token_logprob.pyc (Python 3.11)

from typing import List, Optional
from _models import BaseModel
__all__ = [
    'ChatCompletionTokenLogprob',
    'TopLogprob']

class TopLogprob(BaseModel):
    token: str = 'TopLogprob'
    logprob: float = None


class ChatCompletionTokenLogprob(BaseModel):
    token: str = 'ChatCompletionTokenLogprob'
    top_logprobs: List[TopLogprob] = None
