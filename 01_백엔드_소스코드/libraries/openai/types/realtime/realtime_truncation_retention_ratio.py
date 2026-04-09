# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_truncation_retention_ratio.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeTruncationRetentionRatio',
    'TokenLimits']

class TokenLimits(BaseModel):
    """Optional custom token limits for this truncation strategy.

    If not provided, the model's default token limits will be used.
    """
    post_instructions: Optional[int] = None


class RealtimeTruncationRetentionRatio(BaseModel):
    type: Literal['retention_ratio'] = '\n    Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.\n    '
    token_limits: Optional[TokenLimits] = None
